#!/usr/bin/env python
# encoding: utf-8
'''
@author: encorexiao@futunn.com
@file: cal_kline_pandas.py
@time: 2020/10/14 9:57
@desc:
'''

from datetime import datetime, timedelta
import numpy
import pandas
import pymongo
from decimal import Decimal


def get_timestamp_without_seconds(t):
    return int(datetime(t.year, t.month, t.day, t.hour, t.minute).timestamp())


def stamp2time(stamp):
    return datetime.fromtimestamp(stamp)


# 精度计算
def digital_utils(temps):
    temps = str(temps)
    if temps.find('E'):
        temps = '{:.8f}'.format(Decimal(temps))
    nums = temps.split('.')
    if int(nums[1]) == 0:
        return nums[0]
    else:
        num = str(int(nums[1][::-1]))
        result = '{}.{}'.format(nums[0], num[::-1])
        return result


# 自定义错误类型
class DataCanNotFoundException(Exception):
    def __init__(self):
        err = 'The data is not found, check it please'
        Exception.__init__(self, err)


def kline_get_data(query_coll, period=5):
    '''
    处理kline数据来源
    :param query_coll: 数据来源coll
    :param period: 单位为分钟，数据范围，period = 5 对应，[整除时间前推5min,当前最近整除时间）所有数据
    :return: mongo数据的list形式
    '''
    now = datetime.now()
    minutes = now.minute
    remainder = minutes % period
    if remainder:
        # 若当前分钟为23，则计算[15,20)的数据给予15
        minutes = minutes - remainder

    end = now.replace(minute=minutes)
    end_stamp = get_timestamp_without_seconds(end)

    start = end - timedelta(seconds=period * 60)
    start_stamp = get_timestamp_without_seconds(start)
    query = {'_id': {"$gte": start_stamp, "$lt": end_stamp}}
    mongo_data = query_coll.find(query)
    data_list = list(mongo_data)
    if not data_list:
        raise DataCanNotFoundException
    return data_list


def custom_resampler(df):
    '''
    详细字段的数据处理
    :param df: pandas.DataFrame 对象，每列数据
    :return:
    '''
    if df.name in ['open', '_id', 'ts']:
        return numpy.asarray(df)[0]
    if df.name == 'close':
        return numpy.asarray(df)[-1]
    if df.name == 'low':
        return numpy.min(df)
    if df.name == 'high':
        return numpy.max(df)
    if df.name in ['count', 'amount', 'vol']:
        return digital_utils(numpy.sum(df))


def kline_process(save_coll, data_list, period=5):
    '''
    处理kline的计算和存储
    :param save_coll: 指定存储coll
    :param data_list: 存储的列表数据，[{},{}]
    :param period: minute为单位，resample的数据聚合操作单位
    :return:
    '''
    df = pandas.DataFrame(data_list)
    df['_id'] = df['_id'].apply(stamp2time)
    # df = df.drop(columns=['ts'])
    res_data = df.resample('%sT' % period, on='_id').apply(custom_resampler)
    # print(res_data)
    res_data = res_data.to_dict('list')
    print(res_data)

    for i in range(len(res_data['_id'])):
        id_res = get_timestamp_without_seconds(res_data['_id'][i].to_pydatetime())
        data = dict(
            _id=id_res,
            ts=res_data['ts'][i],
            amount=res_data['amount'][i],
            close=res_data['close'][i],
            count=res_data['count'][i],
            high=res_data['high'][i],
            low=res_data['low'][i],
            open=res_data['open'][i],
            vol=res_data['vol'][i],
        )
        print(data)
        try:
            save_coll.insert_one(data)
        except DuplicateKeyError as e:
            print('库中已存在该_id：%s' % e)


if __name__ == '__main__':
    conn = pymongo.MongoClient("mongodb://localhost:27017/")
    db = conn['test']
    coll = db['quota_huobi_18cbtc_1min']

    save_conn = pymongo.MongoClient('mongodb://localhost:27017/')
    save_db = save_conn['test']
    save_coll = save_db['quota_huobi_18cbtc_5min']

    try:
        data_list = kline_get_data(coll, period=5)
        print(data_list)
        kline_process(save_coll, data_list, period=5)
    except DataCanNotFoundException as e:
        print(e)

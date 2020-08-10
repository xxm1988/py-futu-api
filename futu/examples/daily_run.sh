#! /bin/bash

echo "[`date '+%Y-%m-%d %H:%M:%S'`]begin to run save_data" >> /data/py-futu-api/futu/examples/run.log
cd /data/py-futu-api/futu/examples

# Source global definitions
if [ -f /etc/bashrc ]; then
        . /etc/bashrc
fi

source /root/.bashrc

/root/anaconda3/envs/py37/bin/python ./save_data.py  >> /data/py-futu-api/futu/examples/save_data.log

echo "[`date '+%Y-%m-%d %H:%M:%S'`]finish save_data" >> /data/py-futu-api/futu/examples/run.log

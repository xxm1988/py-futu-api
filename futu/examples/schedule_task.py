import datetime
import schedule
import time

# import time
# from timeloop import Timeloop
# from datetime import timedelta
# tl = Timeloop()
# @tl.job(interval=timedelta(seconds=2))
# def sample_job_every_2s():
#     ts = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
#     time.sleep(1.5)
#     print("2s job current time : {}".format(ts))
# # @tl.job(interval=timedelta(seconds=5))
# # def sample_job_every_5s():
# #     ts = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
# #     print("5s job current time : {}".format(ts))
# # @tl.job(interval=timedelta(seconds=10))
# # def sample_job_every_10s():
# #     ts = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
# #     print("10s job current time : {}".format(ts))

# tl.start()

# while True:
#     try:
#         time.sleep(1)
#     except KeyboardInterrupt:
#         tl.stop()
#         break

# def func():
#     now = datetime.datetime.now()
#     ts = now.strftime('%Y-%m-%d %H:%M:%S.%f')
#     time.sleep(0.5)
#     print('do func  time :',ts)

# def func2():
#     now = datetime.datetime.now()
#     ts = now.strftime('%Y-%m-%d %H:%M:%S.%f')
#     time.sleep(3)
#     print('do func2 time：',ts)

# def tasklist():
#     #清空任务
#     schedule.clear()
#     #创建一个按秒间隔执行任务
#     schedule.every(1).seconds.do(func)
#     #创建一个按2秒间隔执行任务
#     #schedule.every(2).seconds.do(func2)
#     #执行10S
#     for i in range(10):
#         schedule.run_pending()
#         time.sleep(1)

# tasklist()


from time import sleep, time

class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self.interval = interval
        self.function = function
        self.is_running = False
        self.args = args
        self.kwargs = kwargs
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        start = int(time() * 1000)
        i = 0
        if not self.is_running:
            self.is_running = True

            while True:
                if not self.is_running:
                    break

                i += 1
                now = int(time() * 1000)
                sleep_ms = i * self.interval - (now - start)
                if sleep_ms < 0:
                    self.function(*self.args, **self.kwargs)
                else:
                    sleep(sleep_ms / 1000.0)
                    self.function(*self.args, **self.kwargs)

    def stop(self):
        self.is_running = False

def hello(name):
    print(f"[{time()}]\t Hello {name}!")
    sleep(2)


print("starting...")

rt = RepeatedTimer(3000, hello, "world")

try:
    sleep(50)
finally:
    rt.stop()

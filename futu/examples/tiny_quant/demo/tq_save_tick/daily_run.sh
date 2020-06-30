#! /bin/bash

echo "[`date '+%Y-%m-%d %H:%M:%S'`]begin to run TinyStrateSaveTick" >> run.log
cd /data/py-futu-api/futu/examples/tiny_quant/demo/tq_save_tick

# Source global definitions
if [ -f /etc/bashrc ]; then
        . /etc/bashrc
fi

source /root/.bashrc

/root/anaconda3/envs/py37/bin/python ./TinyStrateSaveTick.py

echo "[`date '+%Y-%m-%d %H:%M:%S'`]finish TinyStrateSaveTick" >> run.log

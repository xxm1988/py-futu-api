#! /bin/bash

echo "[`date '+%Y-%m-%d %H:%M:%S'`]begin to run save_data" >> run.log
cd /data/py-futu-api/futu/examples/tiny_quant/demo/tq_save_tick

# Source global definitions
if [ -f /etc/bashrc ]; then
        . /etc/bashrc
fi

source /root/.bashrc

/root/anaconda3/envs/py37/bin/python ./save_data.py

echo "[`date '+%Y-%m-%d %H:%M:%S'`]finish save_data" >> run.log

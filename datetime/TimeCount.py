#!/usr/bin/python3
# coding: utf-8
# Author: slogs@qq.com
import time

def time_count(callback):
    start = time.time()
    callback()
    end = time.time()
    print('程序耗时{}ms'.format(int((end - start)*1000)))

if __name__ == '__main__':
    def ppp():
        time.sleep(1.5)
    time_count(ppp)
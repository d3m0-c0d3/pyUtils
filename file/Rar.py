#!/usr/bin/python3
# coding: utf-8
# Author: slogs@qq.com
# Links:
# - https://www.cnblogs.com/sch01ar/p/8687517.html
# - http://www.rarlab.com/rar/UnRARDLL.exe
from unrar import rarfile

def rar_unzip(file_path, output_path, pwd=None):
    file = rarfile.RarFile(file_path)
    file.extractall(path=output_path, pwd=pwd)

def rar_check_pass(file_path, output_path, pwd):
    file = rarfile.RarFile(file_path)
    out_put_file_path = '{}/{}'.format(output_path,file.namelist()[0])
    try:
        file.extractall(path=output_path, pwd=pwd)
        os.remove(out_put_file_path)
        print('Find password is "{}"'.format(pwd))
        return True
    except Exception as e:
        return False

if __name__ == '__main__':
    import os
    print(os.environ.get('UNRAR_LIB_PATH', None))
    rar_unzip("../test/test.rar","../test/rar","123456")
    rar_check_pass("../test/test.rar","../test/rar2","123456")

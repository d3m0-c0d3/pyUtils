#!/usr/bin/python3
# coding: utf-8
# Author: slogs@qq.com

def swap_str_case(text):
    """
    字符串中字母大小写互换
    :param input: 输入字符串
    :return: 交换大小写的结果
    """
    return text.swapcase()

if __name__ == '__main__':
    demo_str = "test_str"
    print(swap_str_case(demo_str))
    # python自带
    print(tuple(demo_str))
    print(list(demo_str))
    print(tuple(list(demo_str)))

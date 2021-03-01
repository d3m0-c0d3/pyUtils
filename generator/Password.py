#!/usr/bin/python3
# coding: utf-8
# Author: slogs@qq.com

import itertools as its

def gen_pass(min_digits, max_digits, words):
    """
    密码生成器
    :param min_digits: 密码最小长度
    :param max_digits: 密码最大长度
    :param words: 密码可能涉及的字符
    :return: 密码生成器
    """
    while min_digits <= max_digits:
        pwds = its.product(words, repeat=min_digits)
        for pwd in pwds:
            yield ''.join(pwd)
        min_digits += 1

if __name__ == '__main__':
    for pw in gen_pass(2,2,"0123456789abcdef"):
        print("%s-%s"%tuple(list(pw)))

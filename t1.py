# -*- coding: utf-8 -*-
'''
Created on 2020年9月18日

@author: xmx
'''


def run(l):
    s = sorted(l,reverse = True)
    print(s)
    print(s[0])
    if s[0] > 0:
        n = s[0] * s[1] * s[2]
    else:
        n = s[-1] * s[-2] * s[-3]
    print(n)

l = [1,2,9,0,-2,-4,8,0,-2]
run(l)
# -*- coding: utf-8 -*-
'''
Created on 2020年9月17日

@author: xmx
'''
import pytest


class Test_two:
    def test_c(self):
        print('------我是test_c----------')
         
    def test_d(self):
        d = 4
        print('-----我是test_d---')
        assert d == 2
# -*- coding: utf-8 -*-
'''
Created on 2020年9月17日

@author: xmx
'''
import pytest


class Test_one:
    @pytest.mark.parametrize(['a','b'],[pytest.param(1,3,id = 'one'),pytest.param(2,4,id = 'two'),pytest.param(5,5,id = 'three')])
    def test_a(self,a,b):
        print('------我是第一个pytest程序----------')
        assert a == b
         
    def test_b(self):
        with pytest.raises(ValueError) as eoutput:
            num = int('我不是数字')
        print(eoutput.type)
        print(eoutput.value.args)
# def test_a():
#     print('------我是第一个pytest程序----------')
# 
# test_a()
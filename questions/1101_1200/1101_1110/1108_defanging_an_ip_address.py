# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1108_defanging_an_ip_address.py
@time: 2022-06-21 12:40:38 
"""


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')

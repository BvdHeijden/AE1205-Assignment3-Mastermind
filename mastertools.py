# -*- coding: utf-8 -*-
"""
Created on Thu May 24 09:41:29 2018

@author: vdhei
"""
from random import randint
def gencode():
    code=[]
    while len(code)<4:
        c=randint(1,6)
        if c not in code:
            code.append(c)
        
    return code

def goodplace(code,guess):
    
        
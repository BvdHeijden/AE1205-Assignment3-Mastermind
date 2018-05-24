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
        if str(c) not in code:
            code.append(str(c))
        
    return code

def goodplace(code,guess):
    n=0
    i=0
    for x in code:
        if code[i]==guess[i]: n+=1
        i+=1
        
    return n

def goodcolour(code,guess):
    n=0
    i=0
    for x in code:
        if guess[i] in code: n+=1
        i+=1
    
    c=goodplace(code,guess)
    return n-c

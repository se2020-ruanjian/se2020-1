#! /usr/bin/env python   
# -*- coding: utf-8 -*- 
import matlab
import matlab.engine
import string
import math
eng = matlab.engine.start_matlab()

flag = 1
def sign(angle,flag):
    while 1:
        if (angle < 360.0): break
        angle = angle - 360.0
    if(flag == 1):
        result = eng.se_sin(angle)
        # return result
    else:
        angle = math.pi * (angle / 180)# 化角度为弧度
        result = 0
        t = angle
        n = 1
        while (abs(t) >= 1e-5):
            result += t
            n += 1
            t = -t * angle * angle / (2 * n - 1) / (2 * n - 2)

    return result

def cos(angle,flag):
    while 1:
        if (angle < 360.0): break
        angle = angle - 360.0
    if(flag == 1):
        result = eng.se_cos(angle)
    else:
        x = (angle/180)*math.pi;
        cosTotal  = 1
        count = 2
        term = 1
        x=float(x) 
        while abs(term) > 1e-20:
            term *= (-x * x)/( count * (count-1) )   
            cosTotal += term
            count += 2
        result = cosTotal

    return result

def tan(sin,cos):
    sin_res = sin
    cos_res = cos
    result = sin_res / cos_res
    
    return result

def cot(sin,cos):
    sin_res = sin
    cos_res = cos
    result = cos_res / sin_res
    
    return result

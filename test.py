# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 19:22:13 2020

@author: Administrator
"""

import math
import numpy as np
import random
from test_func import *
'''
print("tan(math.pi/2) : ", math.tan(math.pi/2))
print(random.uniform(1, 5000)) 
print(np.random.rand(10))'''
def test():
    score_sinm = 0
    score_cosm = 0
    score_tanm = 0
    score_cotm = 0

    score_sinp = 0
    score_cosp = 0
    score_tanp = 0
    score_cotp = 0

    for i in range(1,1001):
        x = round(random.uniform(1,3000),3)
        ##真实值
        sin_gt = math.sin(x / 180 * math.pi)
        cos_gt = math.cos(x / 180 * math.pi)
        tan_gt = math.tan(x / 180 * math.pi)
        cot_gt = (1 / (math.tan(x / 180 * math.pi)))
        
    
        #matlab计算出的值
        sin_sem = sign(x,1)
        cos_sem = cos(x,1)
        tan_sem = sin_sem / cos_sem
        cot_sem = cos_sem / sin_sem 
    
        #python计算出的值
        sin_sep = sign(x,2)
        cos_sep = cos(x,2)
        tan_sep = sin_sep / cos_sep
        cot_sep = cos_sep / sin_sep
    
        #matlab计算的误差
        score_sinm = score_sinm  + abs(sin_gt - sin_sem)
        score_cosm = score_cosm  + abs(cos_gt - cos_sem)
        score_tanm = score_tanm  + abs(tan_gt - tan_sem)
        score_cotm = score_cotm  + abs(cot_gt - cot_sem)
    
        #python计算的误差
        score_sinp = score_sinp  + abs(sin_gt - sin_sep)
        score_cosp = score_cosp  + abs(cos_gt - cos_sep)
        score_tanp = score_tanp  + abs(tan_gt - tan_sep)
        score_cotp = score_cotp  + abs(cot_gt - cot_sep)
    
    
    
    accsin_m =round((score_sinm / 1000),8)
    acccos_m =round((score_cosm/ 1000),8)
    acctan_m =round((score_tanm / 1000),8)
    acccot_m =round((score_cotm / 1000),8)

    accsin_p =round((score_sinp / 1000),8)
    acccos_p =round((score_cosp/ 1000),8)
    acctan_p =round((score_tanp / 1000),8)
    acccot_p =round((score_cotp / 1000),8)
    
    return accsin_m,acccos_m,acctan_m,acccot_m,accsin_p,acccos_p,acctan_p,acccot_p

accsin_m,acccos_m,acctan_m,acccot_m,accsin_p,acccos_p,acctan_p,acccot_p = test()
print(accsin_m,acccos_m,acctan_m,acccot_m,accsin_p,acccos_p,acctan_p,acccot_p)
    
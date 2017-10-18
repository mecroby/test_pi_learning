# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 23:46:32 2017

@author: roby
"""
import random
from matplotlib import pyplot as plt

def inverse_normal_cdf(p,mu=0,sigma=1,tolerance=0.001):
    if mu!=0 or sigma!=1:
        return mu+sigma*inverse_normal_cdf(p,tolerance=tolerance)

def random_normal():
    return random.random()


xs=[random_normal() for _ in range(1000)]
ys1=[x+random_normal()/2 for x in xs]
ys2=[1-x+random_normal()/2 for x in xs]
plt.scatter(xs,ys1,marker='.',color='black',label='ys1')
plt.scatter(xs,ys2,marker='.',color='gray',label='ys2')
plt.xlabel('xs')
plt.ylabel('ys')
plt.legend(loc=9)
plt.show()

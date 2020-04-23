#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 19:36:37 2020

@author: andrew
"""

import pandas as pd
import numpy as np
import math
import time
import sys
import matplotlib.pyplot as plt


def init_dis_matrix(length):
    distance_matrix = [[0 for col in range(length)] for raw in range(length)]
    return distance_matrix
    
    
def load_position(file_name):
    data = pd.read_csv(file_name,names=['index','lat','lon'])
    city_x = data['lat'].tolist()
    city_y = data['lon'].tolist()
    return city_x,city_y
#构建初始参考距离矩阵
def getdistance(city_x,city_y,n_len,distance):
    for i in range(n_len):
        for j in range(n_len):
            x = pow(city_x[i] - city_x[j], 2)
            y = pow(city_y[i] - city_y[j], 2)
            distance[i][j] = pow(x + y, 0.5)*1000
    for i in range(n_len):
        for j in range(n_len):
            if distance[i][j] == 0:
                distance[i][j] = 0
                
def draw(best,city_x,city_y,n_len):
    result_x = [0 for col in range(n_len+1)]
    result_y = [0 for col in range(n_len+1)]
    
    for i in range(n_len):
        result_x[i] = city_x[best[i]]
        result_y[i] = city_y[best[i]]
    result_x[n_len] = result_x[0]
    result_y[n_len] = result_y[0]
    print(result_x)
    print(result_y)
    plt.xlim(42.9, 43.1)  # 限定横轴的范围
    plt.ylim(-81.26, -81.30)  # 限定纵轴的范围
    plt.plot(result_x, result_y, marker='.', mec='b', mfc='r',label=u'Line')
    plt.legend()  # 让图例生效
    plt.margins(0)
    plt.subplots_adjust(bottom=0.15)
    plt.xlabel(u"x") #X轴标签
    plt.ylabel(u"y") #Y轴标签
    plt.title("Foodhwy Route Plan") #标题
    
    plt.show()
    plt.close(0)     

if __name__=="__main__":
    
    # dataframe = pd.read_csv("./TSP10cities.tsp",sep=" ",header=None)
    # v = dataframe.iloc[:,1:3]
    
    # train_v= np.array(v)
    # train_d=train_v
    # dist = np.zeros((train_v.shape[0],train_d.shape[0]))
    
    
    start = time.time()
    city_x,city_y = load_position('verify_order_position_10.csv')
    end = time.time()
    print ('read time')
    print (start - end)
    n_len = len(city_x)
    city_x = [x for x in city_x]
    city_y = [x for x in city_y]
    distence = init_dis_matrix(n_len)
    getdistance(city_x,city_y,n_len,distence)
    dist = np.array(distence)
    
    #计算距离矩阵
    # for i in range(train_v.shape[0]):
    #     for j in range(train_d.shape[0]):
    #         dist[i,j] = math.sqrt(np.sum((train_v[i,:]-train_d[j,:])**2))
    # print ('------------',type(dist))
    """
    s:已经遍历过的城市
    dist：城市间距离矩阵
    sumpath:目前的最小路径总长度
    Dtemp：当前最小距离
    flag：访问标记
    """
    i=1
    n=dist.shape[0]
    j=0
    sumpath=0
    s=[]
    s.append(0)
    start = time.clock()
    while True:
        k=1
        Detemp=sys.maxsize
        while True:
            l=0
            flag=0
            if k in s:
                flag = 1
            if (flag==0) and (dist[k][s[i-1]] < Detemp):
                j = k;
                Detemp=dist[k][s[i - 1]];
            k+=1
            if k>=n:
                break;
        s.append(j)
        i+=1;
        sumpath+=Detemp
        if i>=n:
            break;
    sumpath+=dist[0][j]
    end = time.clock()
    print("结果：")
    print('最优路径',s)
    print('最佳距离',sumpath)
    print("程序的运行时间是：%s"%(end-start))
    draw(s,city_x,city_y,n_len)   

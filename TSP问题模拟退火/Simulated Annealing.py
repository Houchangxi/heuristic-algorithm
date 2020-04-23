#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 18:41:02 2020

@author: andrew
"""
import pandas as pd
import math
import random
import matplotlib.pyplot as plt
import sys
# from matplotlib.mlab import dist
import copy
import time

#城市数量
# n = 10
# distance = [[0 for col in range(n)] for raw in range(n)]
#初始温度 结束温度
T0 = 30
Tend = 1e-8
#循环控制常数
L = 50
#温度衰减系数
a = 0.98


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
            distance[i][j] = pow(x + y, 0.5)
    for i in range(n_len):
        for j in range(n_len):
            if distance[i][j] == 0:
                distance[i][j] = sys.maxsize

#计算总距离
def cacl_best(rou,n_len,distence):
    sumdis = 0.0
    for i in range(n_len-1):
        sumdis += distence[rou[i]][rou[i+1]]
    sumdis += distence[rou[n_len-1]][rou[0]]     
    return sumdis

#得到新解
def getnewroute(route, time,n_len):
    #如果是偶数次，二变换法
    current = copy.copy(route)
    
    if time % 2 == 0:
        u = random.randint(0, n_len-1)
        v = random.randint(0, n_len-1)
        temp = current[u]
        current[u] = current[v]
        current[v] = temp
    #如果是奇数次，三变换法 
    else:
        temp2 = random.sample(range(0, n_len), 3)
        temp2.sort()
        u = temp2[0]
        v = temp2[1]
        w = temp2[2]
        w1 = w + 1
        temp3 = [0 for col in range(v - u + 1)]
        j =0
        for i in range(u, v + 1):
            temp3[j] = current[i]
            j += 1
        
        for i2 in range(v + 1, w + 1):
            current[i2 - (v-u+1)] = current[i2]
        w = w - (v-u+1)
        j = 0
        for i3 in range(w+1, w1):
            current[i3] = temp3[j]
            j += 1
    
    return current
    
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
    plt.plot(result_x, result_y, marker='>', mec='r', mfc='w',label=u'Route')
    plt.legend()  # 让图例生效
    plt.margins(0)
    plt.subplots_adjust(bottom=0.15)
    plt.xlabel(u"x") #X轴标签
    plt.ylabel(u"y") #Y轴标签
    plt.title("路线规划问题") #标题
    
    plt.show()
    plt.close(0)      
    
def solve(file_name):
    city_x,city_y = load_position(file_name)
    n_len = len(city_x)
    city_x = [x*1000 for x in city_x]
    city_y = [x*1000 for x in city_y]
    distence = init_dis_matrix(n_len)
    #得到距离矩阵
    getdistance(city_x,city_y,n_len,distence)
    #得到初始解以及初始距离
    route = random.sample(range(0, n_len), n_len) 
    total_dis = cacl_best(route,n_len,distence)
    print("初始路线：", route)
    print("初始距离：", total_dis)
    #新解
    newroute = []
    new_total_dis = 0.0
    best = route
    best_total_dis = total_dis
    t = T0
    
    while True:
        if t <= Tend:
            break
        #令温度为初始温度
        for rt2 in range(L):
            newroute = getnewroute(route, rt2,n_len)
            new_total_dis = cacl_best(newroute,n_len,distence)
            delt = new_total_dis - total_dis
            if delt <= 0:
                route = newroute
                total_dis = new_total_dis
                if best_total_dis > new_total_dis:
                    best = newroute
                    best_total_dis = new_total_dis
            elif delt > 0:
                p = math.exp(-delt / t)
                ranp = random.uniform(0, 1)
                if ranp < p:
                    route = newroute
                    total_dis = new_total_dis
        t = t * a
    
    print("现在温度为：", t)
    print("最佳路线：", best)
    print("最佳距离：", best_total_dis)  
    # draw(best,city_x,city_y,n_len)   
    return best
if __name__=="__main__":
    start = time.time()
    best = solve('verify_order_postion_10.csv')
    end = time.time()
    print ('time : ',end-start)
    print (best)

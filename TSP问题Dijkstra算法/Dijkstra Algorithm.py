#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 16:56:25 2020

@author: andrew
"""

import pandas as pd
import matplotlib.pyplot as plt
import time

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
                
                
def dijkstra(graph,src):    
    nodes = [i for i in range(len(graph))]  
    visited = []
    if src in nodes:
        visited.append(src)
        nodes.remove(src)
    else:
        return None
    distance = {src:0}
    for i in nodes:
        distance[i] = graph[src][i]
    
    path = {src:{src:[]}}
    print (path)
    k=pre=src
    while nodes:
        mid_distance = float('inf')
        for v in visited:
            for d in nodes:
                new_distance = graph[src][v] + graph[v][d]
                if new_distance < mid_distance:
                    mid_distance = new_distance
                    graph[src][d] = new_distance
                    k=d
                    pre=v
        distance[k] = mid_distance
        path[src][k]=[i for i in path[src][pre]]
        path[src][k].append(k)
        
        visited.append(k)
        nodes.remove(k)
        print (visited,nodes)
    return distance,path
    

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
    src = 0
    
    dis,path = dijkstra(distence,src)
    print (dis,'  path:  ',path)
    sum_dis = sum(list(dis.values()))
    path_best = list(path[0].keys())
    print ('最佳路线： ',path_best)
    print ('最佳距离： ',sum_dis)
    draw(path_best,city_x,city_y,n_len)       
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 11:08:34 2020

@author: andrew
"""

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import time
 
def coordinate_init(size):
    # 产生坐标字典
    coordinate_dict = {}
    coordinate_dict[0] = (-size, 0)  # 起点是（-size，0）
    up=1
    for i in range(1, size + 1):  # 顺序标号随机坐标
        x=np.random.uniform(-size,size)
        if np.random.randint(0,2)==up:
            y=np.sqrt(size**2-x**2)
        else:
            y=-np.sqrt(size**2-x**2)
        coordinate_dict[i]=(x,y)
    coordinate_dict[size + 1] = (-size, 0)  # 终点是（-size,0),构成一个圆
    return coordinate_dict

def create_init_dict(filename):
    data = pd.read_csv(filename,names=['index','lat','lon'])
    data_dict = {}
    for i in range(len(data)):
        data_dict[i] = (data.iloc[i]['lon'],data.iloc[i]['lat'])
    return data_dict
 
 
def distance_matrix(coordinate_dict, size):  # 生成距离矩阵
    d = np.zeros((size + 2, size + 2))
    for i in range(size + 1):
        for j in range(size + 1):
            if (i == j):
                continue
            if (d[i][j] != 0):
                continue
            x1 = coordinate_dict[i][0]
            y1 = coordinate_dict[i][1]
            x2 = coordinate_dict[j][0]
            y2 = coordinate_dict[j][1]
            distance = np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
            if (i == 0):
                d[i][j] = d[size + 1][j] = d[j][i] = d[j][size + 1] = distance
            else:
                d[i][j] = d[j][i] = distance
    return d
 
 
def path_length(d_matrix, path_list, size):  # 计算路径长度
    length = 0
    for i in range(size + 1):
        length += d_matrix[path_list[i]][path_list[i + 1]]
    return length
 
def shuffle(my_list):#起点和终点不能打乱
    temp_list=my_list[1:-1]
    np.random.shuffle(temp_list)
    shuffle_list=my_list[:1]+temp_list+my_list[-1:]
    return shuffle_list
def product_len_probability(my_list,d_matrix,size,p_num):
    len_list=[]
    pro_list=[]
    path_len_pro=[]
    for path in my_list:
        len_list.append(path_length(d,path,size))
    max_len=max(len_list)+1e-10
    gen_best_length=min(len_list)
    gen_best_length_index=len_list.index(gen_best_length)
    mask_list=np.ones(p_num)*max_len-np.array(len_list)
    sum_len=np.sum(mask_list)
    for i in range(p_num):
        if(i==0):
            pro_list.append(mask_list[i]/sum_len)
        elif(i==p_num-1):
            pro_list.append(1)
        else:
            pro_list.append(pro_list[i-1]+mask_list[i]/sum_len)
    for i in range(p_num):
        path_len_pro.append([my_list[i],len_list[i],pro_list[i]])
    return my_list[gen_best_length_index],gen_best_length,path_len_pro
 
def choose_cross(population,p_num):
    jump=np.random.random()
    if jump<population[0][2]:
        return 0
    low=1
    high=p_num
    mid=int((low+high)/2)
    #二分搜索
    while(low<high):
        if jump>population[mid][2]:
            low=mid
            mid=int((low+high)/2)
        elif jump<population[mid-1][2]:
            high=mid
            mid = int((low + high) / 2)
        else:
            return mid
def veriation(my_list,size):#变异
    ver_1=np.random.randint(1,size+1)
    ver_2=np.random.randint(1,size+1)
    while ver_2==ver_1:#直到ver_2与ver_1不同
        ver_2 = np.random.randint(1, size+1)
    my_list[ver_1],my_list[ver_2]=my_list[ver_2],my_list[ver_1]
    return my_list

if __name__=="__main__":
    
    data = create_init_dict('verify_order_postion_10.csv')
    print (data)
    start = time.time()
    # size=10
    p_num=100#种群个体数量
    gen=2000#进化代数
    pm=0.1#变异率
    # coordinate_dict_1=coordinate_init(size)
    coordinate_dict=create_init_dict('verify_order_postion_10.csv')
    size=len(coordinate_dict)-2
    print ('--',coordinate_dict)
    print (size)
    d=distance_matrix(coordinate_dict,size)
    # print(coordinate_dict)
    path_list=list(range(size+2))
    print(path_list)#打印初始化的路径
    population=[0]*p_num#种群矩阵
    #建立初始种群
    for i in range(p_num):
        population[i]=shuffle(path_list)
    gen_best,gen_best_length,population=product_len_probability(population,d,size,p_num)
    # print(population)#这个列表的每一项中有三项，第一项是路径，第二项是长度，第三项是使用时转盘的概率
    son_list=[0]*p_num
    best_path=gen_best#最好路径初始化
    best_path_length=gen_best_length#最好路径长度初始化
    every_gen_best=[]
    every_gen_best.append(gen_best_length)
    for i in range(gen):#迭代gen代
        son_num=0
        while son_num<p_num:#产生p_num数量子代，杂交与变异
            father_index = choose_cross(population, p_num)
            mother_index = choose_cross(population, p_num)
            father=population[father_index][0]
            mother=population[mother_index][0]
            son1=father.copy()
            son2=mother.copy()
            prduct_set=np.random.randint(1,p_num+1)
            father_cross_set=set(father[1:prduct_set])
            mother_cross_set=set(mother[1:prduct_set])
            cross_complete=1
            for j in range(1,size+1):
                if son1[j] in mother_cross_set:
                    son1[j]=mother[cross_complete]
                    cross_complete+=1
                    if cross_complete>prduct_set:
                        break
            if np.random.random()<pm:#变异
                son1=veriation(son1,size)
            son_list[son_num]=son1
            son_num+=1
            if son_num==p_num: break
            cross_complete=1
            for j in range(1,size+1):
                if son2[j] in father_cross_set:
                    son2[j]=father[cross_complete]
                    cross_complete+=1
                    if cross_complete>prduct_set:
                        break
            if np.random.random()<pm:#变异
                son2=veriation(son2,size)
            son_list[son_num]=son2
            son_num+=1
        gen_best, gen_best_length,population=product_len_probability(son_list,d,size,p_num)
        if(gen_best_length<best_path_length):
            best_path=gen_best
            best_path_length=gen_best_length
        every_gen_best.append(gen_best_length)
    x=[]
    y=[]
    for point in best_path:
        x.append(coordinate_dict[point][0])
        y.append(coordinate_dict[point][1])
    print(gen_best)#最后一代最优路径
    print(gen_best_length)#最后一代最优路径长度
    print(best_path)#史上最优路径
    print(best_path_length)#史上最优路径长度
    # plt.figure(1)
    # plt.subplot(211)
    # plt.plot(every_gen_best)
    # plt.subplot(212)
    # plt.scatter(x,y)
    # plt.plot(x,y)
    # plt.grid()
    # plt.show()

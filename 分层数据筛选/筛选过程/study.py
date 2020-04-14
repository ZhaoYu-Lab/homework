#注释
"""注释"""
'''注释'''
# print(0xfff)
# print(7//1.8)
# print(ord('A'))
# print(chr(20036))
# print('%03d-%02d' %(3  1))
# print('%.2f' % 3.1415926)

#列表是有序集合
# classmate = ["aaa" "ssss" "eee"]
# print(len(classmate))
# print(classmate[-1])
# classmate.append('s777')
# print(classmate)
# classmate.insert(1 're')
# print(classmate)
# classmate.pop()
# print(classmate)
#元组的指向不可更改 如果元组元素有列表，列表元素就可以修改
# a = (1 )
# b = (1)
# print(a b)

# s  = int(input('输入数字'))
# print(s)

# list1 = ['a' 'b' 'c' 'd']
# for i in list1:
#     list(range(5))
#     print(i)
#字典-键值对
# dic = {'name':5}
# print(dic)
# set1 = {1 5 4 9 8 7 3 3 3}
# print(set1)

# list1 = [123 123 456 147]
# set1 =set(list1)
# print(set1)
# list1 = list(range(1 5))
# print(list1)

# import datetime
# d1 = datetime.datetime(2021  1  1)
# d2 = datetime.datetime(2020  2  18)
# print((d1 - d2).days)


# L=[]
# a =int(input("输入一个正整数"))
# if a>1:
#     for i in list(range(1 a+1)):
#         if a%i==0:
#             L.append(i)
# else:
#     L.append(1)
# print(L)

# import random
# r = random.randint(0 1000)
# a =int(input("输入一个正整数"))
# flag = 1
# while(flag!=0):
#     if a>r:
#         print('猜大了')
#         a =int(input("重新输入一个正整数"))
#         flag = 1
#     elif a<r:
#         print('猜小了')
#         a =int(input("重新输入一个正整数"))
#         flag = -1
#     elif a==r:
#         print('猜对了')
#         flag = 0


# def judge(a b c):
#     if a<=0 or b<=0 or c<=0:
#         return 'NO'
#     elif a+b>c and a+c>b and b+c>a:
#         return 'YES'
#     else:
#         return 'NO'
# print(judge(2 4 3))

# import numpy as np
# a = np.zeros((3 4))# 生成3行4列的全零矩阵
# print(a)
# # 多维array
# a = np.array([[2 3 4] 
#               [3 4 5]])
# print(a) # 生成2行3列的矩阵


# import pandas as pd
# import numpy as np

# L=[2 5 4 6 8]
# s = pd.Series(L)
# print(s)

# for i in list(range(1 10)):
#     for j in list(range(1 i+1)):
#         print('%d*%d=%d' %(j i i*j) end='\t')
#     print()

# L=['abcde' 'defgh' 'ghijk' 'jklmn' 'xyzae' 'abdes']
# str1 = input('输入字母')
# k = len(str1)
# for element in L:
#     if element[:k] ==str1:
#         print (element)



# L=[1 1 4 4 7 5 5 3 6 6]
# s = set()
# for i in L:
#    if L.count(i)==1:
#     s.add(i)
# for j in s:
#     print(j end='\t')
   
# for i in range(1 5):
#     for j in range(1 5):
#         for k in range(1 5):
#             if i !=j and j !=k and k !=i:
#                 print("{}{}{}".format(i j k) end=" ")## 不设置指定位置，按默认顺序



# import random
# a =int(input("输入一个0-1000的正整数让电脑猜:"))
# flag = 1
# s = 0
# t = 1000
# r = random.randint(s t)#生成0-1000之间的随机数 猜第一个数
# while(flag!=0):
#     if r<a:
#         print(r '猜小了，重新猜')
#         s = r
#         r = int((s+t)/2)
#         flag = 1
#     elif r>a:
#         print(r '猜大了，重新猜') 
#         t = r
#         r = int((s+t)/2)
#         flag = -1
#     elif a==r:
#         print(r '猜对了')
#         flag = 0
import numpy as np
import pandas as pd
#from scipy.stats import pearsonr
# l1 =[1 2 3]
# l2=[1 2 3]
# print(np.corrcoef(l1))


# pccs = pearsonr(l1 l2)
# print(pccs)

# x = [0 1 0 3 7]
# y = [10 203 304 106 90] 

# print(np.corrcoef(x y))

# for i in range(len(x)):
#     print(i)

# z = [(10 203) (304 106) (90 100)] 
# #z = [i[0] for i in z]
# z = [y for x in z for y in x]
# print(z)

# list1=[(6 'b') (2 'a') (4 'c') (1 'd')]
# list1 = sorted(list1)
# print(list1)


# df = [None ]* 5
# print(len(df))



'''

ant1.3 
ant1.4  
ivy1.1  
log4j1.0  
log4j1.1 
lucene2.0 
synapse1.0
velocity1.4

'''



# data = pd.read_csv("G:\\Zhaoyu-Experiment\\Test-First\\ant-1.3.csv") #读取文件资源

# attr = [column for column in data]
# print(attr[0:20])

from scipy import stats

#X=[0.769 0.745 0.666 0.66 0.765 0.594 0.809 0.63 0.728 0.718 0.805 0.747 0.799 0.72 0.782;0.781 0.801 0.704 0.734 0.789 0.617 0.834 0.653 0.734 0.726 0.804 0.792 0.802 0.707 0.778];

X=[0.769,0.745,0.666,0.66,0.765,0.594,0.809,0.63,0.728,0.718,0.805,0.747,0.799,0.72,0.782]

Y=[0.781,0.801,0.704,0.734,0.789,0.617,0.834,0.653,0.734,0.726,0.804,0.792,0.802,0.707,0.778]

Z= [0.739, 0.77, 0.691, 0.743, 0.783, 0.63, 0.833, 0.642, 0.65, 0.702, 0.815,0.722,0.783,0.691,0.77]

#X=[0.769 0.745 0.666 0.66 0.765 0.594 0.809 0.63 0.728 0.718 0.805 0.747 0.799 0.72 0.782]
#Y=[0.781 0.801 0.704 0.734 0.789 0.617 0.834 0.653 0.734 0.726 0.804 0.792 0.802 0.707 0.778];

# def wilcoxon_rank_sum_test(x, y):
#     res = stats.mannwhitneyu(x ,y)
#     print(res)
# wilcoxon_rank_sum_test(X,Y)

def wilcoxon_signed_rank_test(y1, y2):
    res = stats.wilcoxon(y1, y2)
    print(res)
wilcoxon_signed_rank_test(Y,Z)













#论文插图
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt 
# data = {    
# 'WP': [0.769,0.745,0.666,0.66,0.765,0.594,0.809,0.63,0.728,0.718,0.805,0.747,0.799,0.72,0.782],
# '5-5': [0.739, 0.77, 0.691, 0.743, 0.783, 0.63, 0.833, 0.642, 0.65, 0.702, 0.815,0.722,0.783,0.691,0.77],    
# '10-5': [0.781,0.801,0.704,0.734,0.789,0.617,0.834,0.653,0.734,0.726,0.804,0.792,0.802,0.707,0.778]} 
# df = pd.DataFrame(data) 
# df.plot.box(title="Result-AUC")
# plt.grid(linestyle="--", alpha=0.3)
# plt.show()

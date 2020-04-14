import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#本地数据导入
#根据自己数据文件保存的路径填写(p.s.  python填写路径时，要么使用/，要么使用\\)
"""
本部分进行项目相似性筛选过程，先对所有值进行log转换（0值+1），使度量元取值趋向于正态分布，然后选择
中心趋势度量和分布形状度量（均值，中位数，偏度，峰度）作为衡量项目相似性的度量分布，最后选用欧式距离公式选择k个距离目标项目最近的源项目

df[''] = np.log(df[''].values+1)#对所有数据进行log转换，其中将0值+1
dist1 = np.sqrt(np.sum(np.square(np.array(versionS) - np.array(versionT))))#欧氏距离计算公式
dist2 = np.linalg.norm(ant_1_4 - ant_1_3)#欧式距离计算公式
pccs = np.corrcoef(x, y)#皮尔逊相关系数计算公式

"""
def cal_version(data_source,attr):
    df = pd.read_csv(data_source)
    list = [1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0]  
    for i in range(len(attr)):
        df[attr[i]] = np.log(df[attr[i]].values+1)#对所有数据进行log转换，其中将0值+1
        list[i] = df[attr[i]].mean(),df[attr[i]].median(),df[attr[i]].skew(),df[attr[i]].kurt()
    return list

ant_1_3_data_source = "G:\\Zhaoyu-Experiment\\EXEDATA\\ant-1.3.csv"
ant_1_4_data_source = "G:\\Zhaoyu-Experiment\\EXEDATA\\ant-1.4.csv"
ant_1_5_data_source = "G:\\Zhaoyu-Experiment\\EXEDATA\\ant-1.5.csv"
ant_1_6_data_source = "G:\\Zhaoyu-Experiment\\EXEDATA\\ant-1.6.csv"
ant_1_7_data_source = "G:\\Zhaoyu-Experiment\\EXEDATA\\ant-1.7.csv"
camel_1_0_data_source = "G:\\Zhaoyu-Experiment\\EXEDATA\\camel-1.0.csv"
camel_1_2_data_source = "G:\\Zhaoyu-Experiment\\EXEDATA\\camel-1.2.csv"
camel_1_4_data_source = "G:\\Zhaoyu-Experiment\\EXEDATA\\camel-1.4.csv"
camel_1_6_data_source = "G:\\Zhaoyu-Experiment\\EXEDATA\\camel-1.6.csv"
ivy_1_1_data_source = "G:\\Zhaoyu-Experiment\\EXEDATA\\ivy-1.1.csv"
ivy_1_4_data_source = "G:\\Zhaoyu-Experiment\\EXEDATA\\ivy-1.4.csv"
ivy_2_0_data_source = "G:\\Zhaoyu-Experiment\\EXEDATA\\ivy-2.0.csv"
jedit_3_2_data_source = "G:\\Zhaoyu-Experiment\\EXEDATA\\jedit-3.2.csv"
jedit_4_0_data_source = "G:\\Zhaoyu-Experiment\\EXEDATA\\jedit-4.0.csv"
jedit_4_1_data_source = "G:\\Zhaoyu-Experiment\\EXEDATA\\jedit-4.1.csv"
jedit_4_2_data_source = "G:\\Zhaoyu-Experiment\\EXEDATA\\jedit-4.2.csv"
jedit_4_3_data_source = "G:\\Zhaoyu-Experiment\\EXEDATA\\jedit-4.3.csv"
log4j_1_0_data_source = "G:\\Zhaoyu-Experiment\\EXEDATA\\log4j-1.0.csv"
log4j_1_1_data_source = "G:\\Zhaoyu-Experiment\\EXEDATA\\log4j-1.1.csv"
log4j_1_2_data_source = "G:\\Zhaoyu-Experiment\\EXEDATA\\log4j-1.2.csv"
lucene_2_0_data_source = "G:\\Zhaoyu-Experiment\\EXEDATA\\lucene-2.0.csv"
lucene_2_2_data_source = "G:\\Zhaoyu-Experiment\\EXEDATA\\lucene-2.2.csv"
lucene_2_4_data_source = "G:\\Zhaoyu-Experiment\\EXEDATA\\lucene-2.4.csv"
pbeans1_data_source = "G:\\Zhaoyu-Experiment\\EXEDATA\\pbeans1.csv"
pbeans2_data_source = "G:\\Zhaoyu-Experiment\\EXEDATA\\pbeans2.csv"
poi_1_5_data_source = "G:\\Zhaoyu-Experiment\\EXEDATA\\poi-1.5.csv"
poi_2_0_data_source = "G:\\Zhaoyu-Experiment\\EXEDATA\\poi-2.0.csv"
poi_2_5_data_source = "G:\\Zhaoyu-Experiment\\EXEDATA\\poi-2.5.csv"
poi_3_0_data_source = "G:\\Zhaoyu-Experiment\\EXEDATA\\poi-3.0.csv"
synapse_1_0_data_source = "G:\\Zhaoyu-Experiment\\EXEDATA\\synapse-1.0.csv"
synapse_1_1_data_source = "G:\\Zhaoyu-Experiment\\EXEDATA\\synapse-1.1.csv"
synapse_1_2_data_source = "G:\\Zhaoyu-Experiment\\EXEDATA\\synapse-1.2.csv"
tomcat_data_source = "G:\\Zhaoyu-Experiment\\EXEDATA\\tomcat.csv"
velocity_1_4_data_source = "G:\\Zhaoyu-Experiment\\EXEDATA\\velocity-1.4.csv"
velocity_1_5_data_source = "G:\\Zhaoyu-Experiment\\EXEDATA\\velocity-1.5.csv"
velocity_1_6_data_source = "G:\\Zhaoyu-Experiment\\EXEDATA\\velocity-1.6.csv"
xalan_2_4_data_source = "G:\\Zhaoyu-Experiment\\EXEDATA\\xalan-2.4.csv"
xalan_2_5_data_source = "G:\\Zhaoyu-Experiment\\EXEDATA\\xalan-2.5.csv"
xalan_2_6_data_source = "G:\\Zhaoyu-Experiment\\EXEDATA\\xalan-2.6.csv"
xalan_2_7_data_source = "G:\\Zhaoyu-Experiment\\EXEDATA\\xalan-2.7.csv"
xerces_1_2_data_source = "G:\\Zhaoyu-Experiment\\EXEDATA\\xerces-1.2.csv"
xerces_1_3_data_source = "G:\\Zhaoyu-Experiment\\EXEDATA\\xerces-1.3.csv"
xerces_1_4_data_source = "G:\\Zhaoyu-Experiment\\EXEDATA\\xerces-1.4.csv"

attr = ('wmc','dit','noc','cbo','rfc','lcom','ca','ce','npm','lcom3','loc','dam','moa','mfa','cam','ic','cbm','amc','max_cc','avg_cc')


ant_1_3 = cal_version(ant_1_3_data_source,attr) 
ant_1_4 = cal_version(ant_1_4_data_source,attr)
ant_1_5 = cal_version(ant_1_5_data_source,attr)
ant_1_6 = cal_version(ant_1_6_data_source,attr)
ant_1_7 = cal_version(ant_1_7_data_source,attr)

camel_1_0 = cal_version(camel_1_0_data_source,attr)
camel_1_2 = cal_version(camel_1_2_data_source,attr)
camel_1_4 = cal_version(camel_1_4_data_source,attr)
camel_1_6 = cal_version(camel_1_6_data_source,attr)

ivy_1_1 = cal_version(ivy_1_1_data_source,attr)
ivy_1_4 = cal_version(ivy_1_4_data_source,attr)
ivy_2_0 = cal_version(ivy_2_0_data_source,attr)

jedit_3_2 = cal_version(jedit_3_2_data_source,attr)
jedit_4_0 = cal_version(jedit_4_0_data_source,attr)
jedit_4_1 = cal_version(jedit_4_1_data_source,attr)
jedit_4_2 = cal_version(jedit_4_2_data_source,attr)
jedit_4_3 = cal_version(jedit_4_3_data_source,attr)

log4j_1_0 = cal_version(log4j_1_0_data_source,attr)
log4j_1_1 = cal_version(log4j_1_1_data_source,attr)
log4j_1_2 = cal_version(log4j_1_2_data_source,attr)

lucene_2_0 = cal_version(lucene_2_0_data_source,attr)
lucene_2_2 = cal_version(lucene_2_2_data_source,attr)
lucene_2_4 = cal_version(lucene_2_4_data_source,attr)

pbeans1 = cal_version(pbeans1_data_source,attr)
pbeans2 = cal_version(pbeans2_data_source,attr)

poi_1_5 = cal_version(poi_1_5_data_source,attr)
poi_2_0 = cal_version(poi_2_0_data_source,attr)
poi_2_5 = cal_version(poi_2_5_data_source,attr)
poi_3_0 = cal_version(poi_3_0_data_source,attr)

synapse_1_0 = cal_version(synapse_1_0_data_source,attr)
synapse_1_1 = cal_version(synapse_1_1_data_source,attr)
synapse_1_2 = cal_version(synapse_1_2_data_source,attr)
tomcat = cal_version(tomcat_data_source,attr)

velocity_1_4 = cal_version(velocity_1_4_data_source,attr)
velocity_1_5 = cal_version(velocity_1_5_data_source,attr)
velocity_1_6 = cal_version(velocity_1_6_data_source,attr)

xalan_2_4 = cal_version(xalan_2_4_data_source,attr)
xalan_2_5 = cal_version(xalan_2_5_data_source,attr)
xalan_2_6 = cal_version(xalan_2_6_data_source,attr)
xalan_2_7 = cal_version(xalan_2_7_data_source,attr)

xerces_1_2 = cal_version(xerces_1_2_data_source,attr)
xerces_1_3 = cal_version(xerces_1_3_data_source,attr)
xerces_1_4 = cal_version(xerces_1_4_data_source,attr)


#pccs = np.corrcoef(x, y) 皮尔逊
#knn算法
#1、ant-1.3作为目标项目
#print(ant_1_3)
#print(ant_1_4)

#将list转换为nparray类型，便于使用欧氏距离公式
#ant_1_3 = np.array(ant_1_3) 
#print(ant_1_3)

#欧氏距离排序
version = (ant_1_3,ant_1_4,ant_1_5,ant_1_6,ant_1_7,camel_1_0,camel_1_2,camel_1_4,camel_1_6,
    ivy_1_1,ivy_1_4,ivy_2_0,jedit_3_2,jedit_4_0,jedit_4_1,jedit_4_2,jedit_4_3,log4j_1_0,
    log4j_1_1,log4j_1_2,lucene_2_0,lucene_2_2,lucene_2_4,pbeans1,pbeans2,poi_1_5,poi_2_0,poi_2_5,
    poi_3_0,synapse_1_0,synapse_1_1,synapse_1_2,tomcat,velocity_1_4,velocity_1_5,velocity_1_6,
    xalan_2_4,xalan_2_5,xalan_2_6,xalan_2_7,xerces_1_2,xerces_1_3,xerces_1_4)
vOrder = ('ant_1_3','ant_1_4','ant_1_5','ant_1_6','ant_1_7','camel_1_0','camel_1_2','camel_1_4','camel_1_6',
    'ivy_1_1','ivy_1_4','ivy_2_0','jedit_3_2','jedit_4_0','jedit_4_1','jedit_4_2','jedit_4_3','log4j_1_0',
    'log4j_1_1','log4j_1_2','lucene_2_0','lucene_2_2','lucene_2_4','pbeans1','pbeans2','poi_1_5','poi_2_0','poi_2_5',
    'poi_3_0','synapse_1_0','synapse_1_1','synapse_1_2','tomcat','velocity_1_4','velocity_1_5','velocity_1_6',
    'xalan_2_4','xalan_2_5','xalan_2_6','xalan_2_7','xerces_1_2','xerces_1_3','xerces_1_4')
distance = {}
i=0
def cal_dist(versionS,versionT):
    dist = np.sqrt(np.sum(np.square(np.array(versionS) - np.array(versionT))))
    return dist

# for v in version:
#     distance[i]=cal_dist(v,ant_1_3)
#     i=i+1
# list_order_ant_1_3= sorted(distance.items(),key=lambda x:x[1])
# #目标项目的欧氏距离排序结果 回避0 1 2 3 4   23-pbeans  24-pbeans2
# print(list_order_ant_1_3)
"""
目标项目为ant-1.3
取距离最近的k个其他版本项目
k=3时，取vOrder[15],vOrder[14],vOrder[16]:
jedit_4_2 jedit_4_1 jedit_4_3
k=5时，取vOrder[15],vOrder[14],vOrder[16],vOrder[13],vOrder[29]:
jedit_4_2 jedit_4_1 jedit_4_3 jedit_4_0 synapse_1_0
k=10时，取vOrder[15],vOrder[14],vOrder[16],vOrder[13],vOrder[29],vOrder[12],vOrder[7],vOrder[18],vOrder[19],vOrder[39]:
jedit_4_2 jedit_4_1 jedit_4_3 jedit_4_0 synapse_1_0 jedit_3_2 camel_1_4 log4j_1_1 log4j_1_2 xalan_2_7
"""

# for v in version:
#     distance[i]=cal_dist(v,ant_1_4)
#     i=i+1
# list_order_ant_1_4= sorted(distance.items(),key=lambda x:x[1])
# #目标项目的欧氏距离排序结果
# print(list_order_ant_1_4)
#print(vOrder[16],vOrder[14],vOrder[15],vOrder[29],vOrder[7],vOrder[18],vOrder[19],vOrder[13],vOrder[39],vOrder[9])

# for v in version:
#     distance[i]=cal_dist(v,ant_1_5)
#     i=i+1
# list_order_ant_1_5= sorted(distance.items(),key=lambda x:x[1])
# #目标项目的欧氏距离排序结果
# print(list_order_ant_1_5)
#print(vOrder[39],vOrder[38],vOrder[7],vOrder[16],vOrder[19],vOrder[36],vOrder[6],vOrder[37],vOrder[9],vOrder[8])


# for v in version:
#     distance[i]=cal_dist(v,ant_1_6)
#     i=i+1
# list_order_ant_1_6= sorted(distance.items(),key=lambda x:x[1])
# #目标项目的欧氏距离排序结果
# print(list_order_ant_1_6)
#print(vOrder[16],vOrder[39],vOrder[7],vOrder[38],vOrder[19],vOrder[14],vOrder[18],vOrder[15],vOrder[9],vOrder[6])

# for v in version:
#     distance[i]=cal_dist(v,ant_1_7)
#     i=i+1
# list_order_ant_1_7= sorted(distance.items(),key=lambda x:x[1])
# #目标项目的欧氏距离排序结果
# print(list_order_ant_1_7)
#print(vOrder[7],vOrder[39],vOrder[16],vOrder[38],vOrder[6],vOrder[19],vOrder[36],vOrder[8],vOrder[18],vOrder[9])

# for v in version:
#     distance[i]=cal_dist(v,camel_1_0)
#     i=i+1
# list_order_camel_1_0= sorted(distance.items(),key=lambda x:x[1])
# #目标项目的欧氏距离排序结果
# print(list_order_camel_1_0)
#print(vOrder[9],vOrder[4],vOrder[10],vOrder[2],vOrder[19],vOrder[38],vOrder[36],vOrder[3],vOrder[39],vOrder[37])

# for v in version:
#     distance[i]=cal_dist(v,camel_1_2)
#     i=i+1
#     list_order_camel_1_2= sorted(distance.items(),key=lambda x:x[1])
#  #目标项目的欧氏距离排序结果
# print(list_order_camel_1_2)
#print(vOrder[4],vOrder[10],vOrder[38],vOrder[36],vOrder[37],vOrder[19],vOrder[2],vOrder[39],vOrder[9],vOrder[3])

# for v in version:
#     distance[i]=cal_dist(v,camel_1_4)
#     i=i+1
#     list_order_camel_1_4= sorted(distance.items(),key=lambda x:x[1])
#  #目标项目的欧氏距离排序结果
# print(list_order_camel_1_4)

#print(vOrder[4],vOrder[2],vOrder[3],vOrder[9],vOrder[16],vOrder[19],vOrder[39],vOrder[38],vOrder[1],vOrder[18])
# for v in version:
#     distance[i]=cal_dist(v,camel_1_6)
#     i=i+1
#     list_order_camel_1_6= sorted(distance.items(),key=lambda x:x[1])
#  #目标项目的欧氏距离排序结果
# print(list_order_camel_1_6)

# print(vOrder[9],vOrder[4],vOrder[2],vOrder[16],vOrder[19],vOrder[3],vOrder[18],vOrder[1],vOrder[32],vOrder[39])

# for v in version:
#     distance[i]=cal_dist(v,ivy_1_1)
#     i=i+1
#     list_order_ivy_1_1= sorted(distance.items(),key=lambda x:x[1])
#  #目标项目的欧氏距离排序结果 回避9 10 11
# print(list_order_ivy_1_1)

# print(vOrder[19],vOrder[18],vOrder[7],vOrder[16],vOrder[8],vOrder[6],vOrder[39],vOrder[2],vOrder[38],vOrder[3])
# for v in version:
#     distance[i]=cal_dist(v,ivy_1_4)
#     i=i+1
#     list_order_ivy_1_4= sorted(distance.items(),key=lambda x:x[1])
#  #目标项目的欧氏距离排序结果 回避9 10 11
# print(list_order_ivy_1_4)

# print(vOrder[6],vOrder[37],vOrder[36],vOrder[9],vOrder[19],vOrder[17],vOrder[38],vOrder[5],vOrder[39],vOrder[20])

# for v in version:
#     distance[i]=cal_dist(v,jedit_4_0)
#     i=i+1
#     list_order_jedit_4_0= sorted(distance.items(),key=lambda x:x[1])
#  #目标项目的欧氏距离排序结果 回避12 13 14 15 16
# print(list_order_jedit_4_0)

# print(vOrder[0],vOrder[1],vOrder[31],vOrder[29],vOrder[32],vOrder[3],vOrder[41],vOrder[40],vOrder[2],vOrder[4])
# for v in version:
#     distance[i]=cal_dist(v,jedit_4_1)
#     i=i+1
#     list_order_jedit_4_1= sorted(distance.items(),key=lambda x:x[1])
#  #目标项目的欧氏距离排序结果 回避12 13 14 15 16
# print(list_order_jedit_4_1)

# print(vOrder[1],vOrder[0],vOrder[3],vOrder[29],vOrder[2],vOrder[4],vOrder[31],vOrder[32],vOrder[7],vOrder[18])

# for v in version:
#     distance[i]=cal_dist(v,jedit_4_2)
#     i=i+1
#     list_order_jedit_4_2= sorted(distance.items(),key=lambda x:x[1])
#  #目标项目的欧氏距离排序结果 回避12 13 14 15 16
# print(list_order_jedit_4_2)

# print(vOrder[1],vOrder[0],vOrder[3],vOrder[29],vOrder[2],vOrder[31],vOrder[4],vOrder[32],vOrder[18],vOrder[7])

# for v in version:
#     distance[i]=cal_dist(v,jedit_4_3)
#     i=i+1
#     list_order_jedit_4_3= sorted(distance.items(),key=lambda x:x[1])
#  #目标项目的欧氏距离排序结果 回避12 13 14 15 16
# print(list_order_jedit_4_3)

# print(vOrder[1],vOrder[3],vOrder[2],vOrder[4],vOrder[19],vOrder[9],vOrder[29],vOrder[7],vOrder[18],vOrder[0])

# for v in version:
#     distance[i]=cal_dist(v,log4j_1_0)
#     i=i+1
#     list_order_log4j_1_0= sorted(distance.items(),key=lambda x:x[1])
#  #目标项目的欧氏距离排序结果 回避17 18 19 
# print(list_order_log4j_1_0)

# print(vOrder[10],vOrder[37],vOrder[36],vOrder[6],vOrder[11],vOrder[38],vOrder[39],vOrder[9],vOrder[5],vOrder[4])

# for v in version:
#     distance[i]=cal_dist(v,log4j_1_1)
#     i=i+1
#     list_order_log4j_1_1= sorted(distance.items(),key=lambda x:x[1])
#  #目标项目的欧氏距离排序结果 回避17 18 19 
# print(list_order_log4j_1_1)

# print(vOrder[9],vOrder[16],vOrder[3],vOrder[1],vOrder[4],vOrder[2],vOrder[7],vOrder[32],vOrder[8],vOrder[39])

# for v in version:
#     distance[i]=cal_dist(v,log4j_1_2)
#     i=i+1
#     list_order_log4j_1_2= sorted(distance.items(),key=lambda x:x[1])
#  #目标项目的欧氏距离排序结果 回避17 18 19 
# print(list_order_log4j_1_2)

# print(vOrder[9],vOrder[39],vOrder[16],vOrder[38],vOrder[3],vOrder[2],vOrder[4],vOrder[7],vOrder[6],vOrder[36])

# for v in version:
#     distance[i]=cal_dist(v,lucene_2_2)
#     i=i+1
#     list_order_lucene_2_2= sorted(distance.items(),key=lambda x:x[1])
#  #目标项目的欧氏距离排序结果 回避20 21 22
# print(list_order_lucene_2_2)
# #vOrder[23]是pbeans 实例数小于100,所以去掉,补上vOrder[9]
# print(vOrder[10],vOrder[37],vOrder[36],vOrder[11],vOrder[6],vOrder[5],vOrder[17],vOrder[38],vOrder[39],vOrder[23])
#print(vOrder[9])
# for v in version:
#     distance[i]=cal_dist(v,lucene_2_4)
#     i=i+1
#     list_order_lucene_2_4= sorted(distance.items(),key=lambda x:x[1])
#  #目标项目的欧氏距离排序结果 回避20 21 22
# print(list_order_lucene_2_4)
# #vOrder[23]是pbeans1 实例数小于100,补上vOrder[9]
# print(vOrder[10],vOrder[11],vOrder[37],vOrder[36],vOrder[17],vOrder[6],vOrder[38],vOrder[5],vOrder[39],vOrder[23])
#print(vOrder[9])

# for v in version:
#     distance[i]=cal_dist(v,poi_1_5)
#     i=i+1
#     list_order_poi_1_5= sorted(distance.items(),key=lambda x:x[1])
#  #目标项目的欧氏距离排序结果 回避25 26 27 28
# print(list_order_poi_1_5)
# #vOrder[24]是pbeans2 实例数小于100,补上vOrder[42]
# print(vOrder[33],vOrder[24],vOrder[34],vOrder[41],vOrder[40],vOrder[12],vOrder[13],vOrder[35],vOrder[15],vOrder[14])
# print(vOrder[42])

# for v in version:
#     distance[i]=cal_dist(v,poi_2_0)
#     i=i+1
#     list_order_poi_2_0= sorted(distance.items(),key=lambda x:x[1])
#  #目标项目的欧氏距离排序结果 回避25 26 27 28
# print(list_order_poi_2_0)
# #vOrder[24]是pbeans2 实例数小于100,补上vOrder[42]
# print(vOrder[33],vOrder[24],vOrder[34],vOrder[41],vOrder[40],vOrder[12],vOrder[13],vOrder[35],vOrder[15],vOrder[14])
# print(vOrder[42])

# for v in version:
#     distance[i]=cal_dist(v,poi_2_5)
#     i=i+1
#     list_order_poi_2_5= sorted(distance.items(),key=lambda x:x[1])
#  #目标项目的欧氏距离排序结果 回避25 26 27 28
# print(list_order_poi_2_5)
# #vOrder[24]是pbeans2 实例数小于100,补上vOrder[42]
# print(vOrder[33],vOrder[24],vOrder[34],vOrder[41],vOrder[40],vOrder[12],vOrder[13],vOrder[35],vOrder[15],vOrder[14])
# print(vOrder[42])

# for v in version:
#     distance[i]=cal_dist(v,synapse_1_0)
#     i=i+1
#     list_order_synapse_1_0= sorted(distance.items(),key=lambda x:x[1])
#  #目标项目的欧氏距离排序结果 回避29 30 31 
# print(list_order_synapse_1_0)

# print(vOrder[16],vOrder[1],vOrder[14],vOrder[15],vOrder[3],vOrder[2],vOrder[0],vOrder[4],vOrder[18],vOrder[19])

# for v in version:
#     distance[i]=cal_dist(v,synapse_1_2)
#     i=i+1
#     list_order_synapse_1_2= sorted(distance.items(),key=lambda x:x[1])
#  #目标项目的欧氏距离排序结果 回避29 30 31 
# print(list_order_synapse_1_2)

# print(vOrder[32],vOrder[29],vOrder[15],vOrder[14],vOrder[16],vOrder[13],vOrder[1],vOrder[12],vOrder[18],vOrder[0])

# for v in version:
#     distance[i]=cal_dist(v,tomcat)
#     i=i+1
#     list_order_tomcat= sorted(distance.items(),key=lambda x:x[1])
#  #目标项目的欧氏距离排序结果 回避32
# print(list_order_tomcat)

# print(vOrder[32],vOrder[29],vOrder[15],vOrder[14],vOrder[16],vOrder[13],vOrder[1],vOrder[12],vOrder[18],vOrder[0])


# for v in version:
#     distance[i]=cal_dist(v,velocity_1_4)
#     i=i+1
#     list_order_velocity_1_4= sorted(distance.items(),key=lambda x:x[1])
#  #目标项目的欧氏距离排序结果 回避33 34 35 
# print(list_order_velocity_1_4)
# #vOrder[24]是pbeans2 实例数小于100,补上vOrder[14]
# print(vOrder[24],vOrder[28],vOrder[27],vOrder[41],vOrder[40],vOrder[12],vOrder[13],vOrder[25],vOrder[42],vOrder[15])
# print(vOrder[14])

# for v in version:
#     distance[i]=cal_dist(v,velocity_1_6)
#     i=i+1
#     list_order_velocity_1_6= sorted(distance.items(),key=lambda x:x[1])
#  #目标项目的欧氏距离排序结果 回避33 34 35 
# print(list_order_velocity_1_6)

# print(vOrder[42],vOrder[41],vOrder[40],vOrder[8],vOrder[7],vOrder[15],vOrder[14],vOrder[13],vOrder[16],vOrder[32])

# for v in version:
#     distance[i]=cal_dist(v,xalan_2_4)
#     i=i+1
#     list_order_xalan_2_4= sorted(distance.items(),key=lambda x:x[1])
#  #目标项目的欧氏距离排序结果 回避36 37 38 39
# print(list_order_xalan_2_4)

# print(vOrder[6],vOrder[2],vOrder[10],vOrder[19],vOrder[4],vOrder[3],vOrder[7],vOrder[9],vOrder[5],vOrder[17])

# for v in version:
#     distance[i]=cal_dist(v,xalan_2_5)
#     i=i+1
#     list_order_xalan_2_5= sorted(distance.items(),key=lambda x:x[1])
#  #目标项目的欧氏距离排序结果 回避36 37 38 39
# print(list_order_xalan_2_5)

# print(vOrder[10],vOrder[6],vOrder[2],vOrder[19],vOrder[4],vOrder[3],vOrder[7],vOrder[9],vOrder[17],vOrder[5])


# for v in version:
#     distance[i]=cal_dist(v,xalan_2_6)
#     i=i+1
#     list_order_xalan_2_5= sorted(distance.items(),key=lambda x:x[1])
#  #目标项目的欧氏距离排序结果 回避36 37 38 39
# print(list_order_xalan_2_5)

# print(vOrder[35],vOrder[32],vOrder[1],vOrder[7],vOrder[16],vOrder[15],vOrder[8],vOrder[2],vOrder[14],vOrder[34])

# for v in version:
#     distance[i]=cal_dist(v,xalan_2_7)
#     i=i+1
#     list_order_xalan_2_7= sorted(distance.items(),key=lambda x:x[1])
#  #目标项目的欧氏距离排序结果 回避36 37 38 39
# print(list_order_xalan_2_7)

# print(vOrder[35],vOrder[32],vOrder[1],vOrder[7],vOrder[16],vOrder[15],vOrder[8],vOrder[2],vOrder[14],vOrder[34])



# for v in version:
#     distance[i]=cal_dist(v,xerces_1_2)
#     i=i+1
#     list_order_xerces_1_2= sorted(distance.items(),key=lambda x:x[1])
#  #目标项目的欧氏距离排序结果 回避40 41 42
# print(list_order_xerces_1_2)

# print(vOrder[35],vOrder[32],vOrder[1],vOrder[7],vOrder[16],vOrder[15],vOrder[8],vOrder[2],vOrder[14],vOrder[34])



# for v in version:
#     distance[i]=cal_dist(v,xerces_1_3)
#     i=i+1
#     list_order_xerces_1_3= sorted(distance.items(),key=lambda x:x[1])
#  #目标项目的欧氏距离排序结果 回避40 41 42
# print(list_order_xerces_1_3)

# print(vOrder[35],vOrder[32],vOrder[1],vOrder[7],vOrder[16],vOrder[15],vOrder[8],vOrder[2],vOrder[14],vOrder[34])

# for v in version:
#     distance[i]=cal_dist(v,xerces_1_4)
#     i=i+1
#     list_order_xerces_1_4= sorted(distance.items(),key=lambda x:x[1])
#  #目标项目的欧氏距离排序结果 回避40 41 42
# print(list_order_xerces_1_4)

# print(vOrder[35],vOrder[32],vOrder[1],vOrder[7],vOrder[16],vOrder[15],vOrder[8],vOrder[2],vOrder[14],vOrder[34])









 
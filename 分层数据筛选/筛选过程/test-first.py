import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
#本地数据导入
#根据自己数据文件保存的路径填写(p.s.  python填写路径时，要么使用/，要么使用\\)
"""
本部分进行项目相似性筛选过程，先对所有值进行log转换（0值+1），使度量元取值趋向于正态分布，然后选择
中心趋势度量和分布形状度量（均值mean，中位数median，偏度skew，峰度kurt）作为衡量项目相似性的度量分布，最后选用欧式距离公式选择k个距离目标项目最近的源项目

df[''] = np.log(df[''].values+1)#用于对所有数据进行log转换，其中将0值+1
dist1 = np.sqrt(np.sum(np.square(np.array(versionS) - np.array(versionT))))#欧氏距离计算公式
pccs = np.corrcoef(x, y)#x和y的皮尔逊相关系数计算公式
实例数小于100的项目被排除,去掉pbeans


#先将所有文件的bug标签分为0和1
# df = pd.read_csv(ant_1_3_data_source)
# print(df['bug'])
# df['bug'][df['bug'] > 0]  = 1
# print(df['bug'])

""" 

#导入数据
ant_1_3_data_source = "G:\\Zhaoyu-Experiment\\Test-First\\ant-1.3.csv"
ant_1_4_data_source = "G:\\Zhaoyu-Experiment\\Test-First\\ant-1.4.csv"
ant_1_5_data_source = "G:\\Zhaoyu-Experiment\\Test-First\\ant-1.5.csv"
ant_1_6_data_source = "G:\\Zhaoyu-Experiment\\Test-First\\ant-1.6.csv"
ant_1_7_data_source = "G:\\Zhaoyu-Experiment\\Test-First\\ant-1.7.csv"
camel_1_0_data_source = "G:\\Zhaoyu-Experiment\\Test-First\\camel-1.0.csv"
camel_1_2_data_source = "G:\\Zhaoyu-Experiment\\Test-First\\camel-1.2.csv"
camel_1_4_data_source = "G:\\Zhaoyu-Experiment\\Test-First\\camel-1.4.csv"
camel_1_6_data_source = "G:\\Zhaoyu-Experiment\\Test-First\\camel-1.6.csv"
ivy_1_1_data_source = "G:\\Zhaoyu-Experiment\\Test-First\\ivy-1.1.csv"
ivy_1_4_data_source = "G:\\Zhaoyu-Experiment\\Test-First\\ivy-1.4.csv"
ivy_2_0_data_source = "G:\\Zhaoyu-Experiment\\Test-First\\ivy-2.0.csv"
jedit_3_2_data_source = "G:\\Zhaoyu-Experiment\\Test-First\\jedit-3.2.csv"
jedit_4_0_data_source = "G:\\Zhaoyu-Experiment\\Test-First\\jedit-4.0.csv"
jedit_4_1_data_source = "G:\\Zhaoyu-Experiment\\Test-First\\jedit-4.1.csv"
jedit_4_2_data_source = "G:\\Zhaoyu-Experiment\\Test-First\\jedit-4.2.csv"
jedit_4_3_data_source = "G:\\Zhaoyu-Experiment\\Test-First\\jedit-4.3.csv"
log4j_1_0_data_source = "G:\\Zhaoyu-Experiment\\Test-First\\log4j-1.0.csv"
log4j_1_1_data_source = "G:\\Zhaoyu-Experiment\\Test-First\\log4j-1.1.csv"
log4j_1_2_data_source = "G:\\Zhaoyu-Experiment\\Test-First\\log4j-1.2.csv"
lucene_2_0_data_source = "G:\\Zhaoyu-Experiment\\Test-First\\lucene-2.0.csv"
lucene_2_2_data_source = "G:\\Zhaoyu-Experiment\\Test-First\\lucene-2.2.csv"
lucene_2_4_data_source = "G:\\Zhaoyu-Experiment\\Test-First\\lucene-2.4.csv"
poi_1_5_data_source = "G:\\Zhaoyu-Experiment\\Test-First\\poi-1.5.csv"
poi_2_0_data_source = "G:\\Zhaoyu-Experiment\\Test-First\\poi-2.0.csv"
poi_2_5_data_source = "G:\\Zhaoyu-Experiment\\Test-First\\poi-2.5.csv"
poi_3_0_data_source = "G:\\Zhaoyu-Experiment\\Test-First\\poi-3.0.csv"
synapse_1_0_data_source = "G:\\Zhaoyu-Experiment\\Test-First\\synapse-1.0.csv"
synapse_1_1_data_source = "G:\\Zhaoyu-Experiment\\Test-First\\synapse-1.1.csv"
synapse_1_2_data_source = "G:\\Zhaoyu-Experiment\\Test-First\\synapse-1.2.csv"
tomcat_data_source = "G:\\Zhaoyu-Experiment\\Test-First\\tomcat.csv"
velocity_1_4_data_source = "G:\\Zhaoyu-Experiment\\Test-First\\velocity-1.4.csv"
velocity_1_5_data_source = "G:\\Zhaoyu-Experiment\\Test-First\\velocity-1.5.csv"
velocity_1_6_data_source = "G:\\Zhaoyu-Experiment\\Test-First\\velocity-1.6.csv"
xalan_2_4_data_source = "G:\\Zhaoyu-Experiment\\Test-First\\xalan-2.4.csv"
xalan_2_5_data_source = "G:\\Zhaoyu-Experiment\\Test-First\\xalan-2.5.csv"
xalan_2_6_data_source = "G:\\Zhaoyu-Experiment\\Test-First\\xalan-2.6.csv"
xalan_2_7_data_source = "G:\\Zhaoyu-Experiment\\Test-First\\xalan-2.7.csv"
xerces_1_2_data_source = "G:\\Zhaoyu-Experiment\\Test-First\\xerces-1.2.csv"
xerces_1_3_data_source = "G:\\Zhaoyu-Experiment\\Test-First\\xerces-1.3.csv"
xerces_1_4_data_source = "G:\\Zhaoyu-Experiment\\Test-First\\xerces-1.4.csv"


versionSource = (ant_1_3_data_source,ant_1_4_data_source,ant_1_5_data_source,ant_1_6_data_source,ant_1_7_data_source,
    camel_1_0_data_source,camel_1_2_data_source,camel_1_4_data_source,camel_1_6_data_source,
    ivy_1_1_data_source,ivy_1_4_data_source,ivy_2_0_data_source,jedit_3_2_data_source,jedit_4_0_data_source,
    jedit_4_1_data_source,jedit_4_2_data_source,jedit_4_3_data_source,log4j_1_0_data_source,log4j_1_1_data_source,
    log4j_1_2_data_source,lucene_2_0_data_source,lucene_2_2_data_source,lucene_2_4_data_source,poi_1_5_data_source,
    poi_2_0_data_source,poi_2_5_data_source,poi_3_0_data_source,synapse_1_0_data_source,synapse_1_1_data_source,
    synapse_1_2_data_source,tomcat_data_source,velocity_1_4_data_source,velocity_1_5_data_source,
    velocity_1_6_data_source,xalan_2_4_data_source,xalan_2_5_data_source,xalan_2_6_data_source,xalan_2_7_data_source,
    xerces_1_2_data_source,xerces_1_3_data_source,xerces_1_4_data_source)

#属性元组
attr = ('wmc','dit','noc','cbo','rfc','lcom','ca','ce','npm','lcom3','loc','dam','moa','mfa','cam','ic','cbm','amc','max_cc','avg_cc')

#计算项目的 均值mean，中位数median，偏度skew，峰度kurt 一个项目的一个属性计算一次 一个项目计算20个属性
arrayList = np.zeros((41,20)) #生成41行20列的二维数组
dataList = arrayList.tolist()   #二维数组转换为列表 存放每一个属性的特征向量
#读取数据 + 划分标签 +log转换
def data_process(versionSource):
    for i in range(len(versionSource)):
        df = pd.read_csv(versionSource[i]) #读取文件资源
        df['bug'][df['bug'] > 0]  = 'Y' #将所有文件的bug标签分为N和Y  多于0的改为Y
        df['bug'][df['bug'] == 0]  = 'N' #将所有文件的bug标签分为N和Y 多于0的改为Y
        #对所有数据进行log转换，其中将0值+1
        #df[['wmc','dit','noc','cbo','rfc','lcom','ca','ce','npm','lcom3','loc','dam','moa','mfa','cam','ic','cbm','amc','max_cc','avg_cc']]=np.log(df[['wmc','dit','noc','cbo','rfc','lcom','ca','ce','npm','lcom3','loc','dam','moa','mfa','cam','ic','cbm','amc','max_cc','avg_cc']].values+1) 
        #print(df[0:5])
        for j in range(len(attr)):
            df[attr[j]] = np.log(df[attr[j]].values+1)#对所有数据进行log转换，其中将0值+1
            dataList[i][j] = df[attr[j]].mean(),df[attr[j]].median(),df[attr[j]].skew(),df[attr[j]].kurt()
        #print(df[0:5])
data_process(versionSource)#此时已经计算完所有项目的特征向量

#dataList[0][0] 表示第一个项目ant_1_3_data_source的第一个属性wmc的特征向量(均值mean，中位数median，偏度skew，峰度kurt)
# for j in range(len(attr)): #输出第一个项目ant_1_3_data_source的所有属性的特征向量
#     print(dataList[0][j])

# print(dataList[0]) #输出第一个项目ant_1_3_data_source的所有属性的特征向量
# dataList[0] =  [y for x in dataList[0] for y in x]
# print(dataList[0])
# print(len(dataList))

#计算皮尔逊相关系数  np.corrcoef(x,y) x y 是两个向量
#在计算皮尔逊相关系数之前 把列表里的元组括号去掉，使之成为一个向量，而不是一个列表中包含多个向量
for i in range(len(dataList)):
    dataList[i] =  [y for x in dataList[i] for y in x]
#dataList[0] #输出第一个项目ant_1_3_data_source的所有属性的特征向量

#建立字典 其中key值是verSource的项目版本，value值就是将要计算的相关系数值
pccDict = dict.fromkeys(versionSource) 
#以ant-1.3为目标的话 ant-1.3是dataList[0]
def data_calculate(dataList): 
    for i in range(len(dataList)):
        pccList = np.corrcoef(dataList[i],dataList[16]) #计算和目标项目之间的相关系数 0表示目标项目为ant-1.3 1表示ant-1.4
        #print(versionSource[i] ,pccList[0][1])
        pccDict[versionSource[i]] = pccList[0][1] #pccList[0][1]就是皮尔逊相关系数的值
        
data_calculate(dataList)
#print(pccDict)
#key使用lambda匿名函数取value进行从小到大排序  reverse=True是从大到小
pccDict = sorted(pccDict.items(), key=lambda item:item[1],reverse=True)
print(pccDict) 
# pccDict = [i[0] for i in pccDict]
# print(pccDict) 

'''
import operator
sorted(pccDict.items(), key=operator.itemgetter(1)) #第二种排序方法 使用operator的itemgetter进行排序

f = zip(pccDict.keys(), pccDict.values()) #第三种方法 将key和value分装成元组，再进行排序
c = sorted(f)
'''

#dataList[0][] 和 dataList[1][] 也就是第一个项目的所有属性的特征向量和第二个项目所有属性的特征向量的相关系数
#print(np.corrcoef(dataList[0],dataList[1]))

'''
x = [0,1,0,3,7]
y = [10,203,304,106,90] 
print(np.corrcoef(x,y))
输出 
[[ 1.         -0.31227944]
 [-0.31227944  1.        ]]
'''


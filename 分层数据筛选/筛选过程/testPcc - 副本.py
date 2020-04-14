import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

#读取数据 + 划分标签 +log转换
def data_process(versionSource,dataList,attr):
    for i in range(len(versionSource)):
        df = pd.read_csv(versionSource[i]) #读取文件资源
        df['bug'][df['bug'] > 0]  = 'Y' #将所有文件的bug标签分为N和Y  多于0的改为Y
        df['bug'][df['bug'] == 0]  = 'N' #将所有文件的bug标签分为N和Y 多于0的改为Y
        for j in range(len(attr[0:20])):
            df[attr[j]] = np.log(df[attr[j]].values+1)#对所有数据进行log转换，其中将0值+1
            dataList[i][j] = df[attr[j]].mean(),df[attr[j]].median(),df[attr[j]].skew(),df[attr[j]].kurt()
    return dataList

#在计算皮尔逊相关系数之前 把列表里的元组括号去掉，使之成为一个向量，而不是一个列表中包含多个向量
def list_process(dataList):
    for i in range(len(dataList)):
        dataList[i] =  [y for x in dataList[i] for y in x]
    return dataList

#以ant-1.3为目标的话 ant-1.3是dataList[0]
def data_calculate(dataList,versionSource,argu): 
    pccValueList = [] #pcc排序用的列表
    for i in range(len(dataList)):
        pccList = np.corrcoef(dataList[i],dataList[argu]) #计算和目标项目之间的相关系数 0表示目标项目为ant-1.3 1表示ant-1.4
        pccValue = pccList[0][1]
        pccValueList.append((pccValue,versionSource[i]))
        pccValueList = sorted(pccValueList,reverse=True) #对pcc值进行排序
        #index = pccValueList[0][1] #得到最大的pcc值的索引
    return pccValueList

def result_version(pccValueList,tarketVersion,tarketClass,versionNum):
    for i in range(len(pccValueList)):
        if tarketClass not in pccValueList[i][1] and len(tarketVersion)<=versionNum:
         tarketVersion.append(pccValueList[i][1])
    return tarketVersion

def mergeV(source,sourceSize): #合并选好的源项目集合
    df = [None ]* sourceSize
    for i in range(len(source)):
        df[i] = pd.read_csv(source[i])
    result = pd.concat(df,axis=0,ignore_index=True) #合并
    result['bug'][result['bug'] > 0]  = 'Y' #将所有文件的bug标签分为Y和N  多于0的改为Y 等于0的改为N
    result['bug'][result['bug'] == 0]  = 'N'
    return result #返回合并的源项目集

def readCsv(data_source): ##读取目标项目文件并处理YN标签
    tarketVersion = pd.read_csv(data_source) #读取目标项目文件
    tarketVersion['bug'][tarketVersion['bug'] > 0]  = 'Y' 
    tarketVersion['bug'][tarketVersion['bug'] == 0]  = 'N'
    return tarketVersion

#目标项目第一个实例i和源项目每一个实例j进行比较 比较完得出很多相关系数，然后对相关系数进行排序，
#选取最大的那个相关系数对应的实例j，然后把实例j放到候选训练集TDS中 这里排序可以写成元组对 比如(j,pcc)
#为目标项目的每个实例选择原项目中最相似的1个实例

def selectTrain(tmpResult,tmpTarket,resultSource,instanceNum):
    trainDataSet = [] #候选训练集
    for i in range(len(tmpTarket)):
        pccValueList = [] #pcc排序用的列表
        for j in range(len(tmpResult)):
            pccList = np.corrcoef(tmpTarket.iloc[i],tmpResult.iloc[j])
            pccValue = pccList[0][1] #pccList[0][1]就是皮尔逊相关系数的值
            pccValueList.append((pccValue,j)) #pcc值和行号进入列表
        pccValueList = sorted(pccValueList,reverse=True) #对pcc值进行排序
        for k in range(instanceNum):
            index = pccValueList[k][1] #得到最大的前instanceNum个pcc值的索引
            trainDataSet.append((resultSource.iloc[index]))#pcc值最大的那行进去
    return trainDataSet

def main():
    #导入数据
    CM1_data_source = "G:\\Zhaoyu-Experiment\\NASA-MDP\\CM1_mdp.csv" 
    KC3_data_source = "G:\\Zhaoyu-Experiment\\NASA-MDP\\KC3_mdp.csv" 
    KC4_data_source = "G:\\Zhaoyu-Experiment\\NASA-MDP\\KC4_mdp.csv"
    MW1_data_source = "G:\\Zhaoyu-Experiment\\NASA-MDP\\MW1_mdp.csv"
    PC1_data_source = "G:\\Zhaoyu-Experiment\\NASA-MDP\\PC1_mdp.csv"
    PC2_data_source = "G:\\Zhaoyu-Experiment\\NASA-MDP\\PC2_mdp.csv"
    PC3_data_source = "G:\\Zhaoyu-Experiment\\NASA-MDP\\PC3_mdp.csv"
    PC4_data_source = "G:\\Zhaoyu-Experiment\\NASA-MDP\\PC4_mdp.csv"
   

    versionSource = (CM1_data_source,KC3_data_source,KC4_data_source,MW1_data_source,PC1_data_source,
    PC2_data_source,PC3_data_source,PC4_data_source)

    data = pd.read_csv(versionSource[0]) #读取文件资源

    attr = [column for column in data]
    #属性元组

    arrayList = np.zeros((41,20)) #生成41行20列的二维数组
    dataList = arrayList.tolist()   #二维数组转换为列表 存放每一个属性的特征向量
    #计算项目的 均值mean，中位数median，偏度skew，峰度kurt 一个项目的一个属性计算一次 一个项目计算20个属性
    dataList = data_process(versionSource,dataList,attr)#此时已经计算完所有项目的特征向量
    dataList = list_process(dataList)#把列表里的元组括号去掉，使之成为一个向量，而不是一个列表中包含多个向量

    #dataList[0][0] 表示第一个项目ant_1_3_data_source的第一个属性wmc的特征向量(均值mean，中位数median，偏度skew，峰度kurt)
    #计算皮尔逊相关系数  np.corrcoef(x,y) x y 是两个向量
    #dataList[0] #输出第一个项目ant_1_3_data_source的所有属性的特征向量

    #12是jedit3.2  17是log4j1.0  20是lucene2.0 23是poi1.5 27是synapse1.0  30是tomcat 31是velocity 34是xalan 38是xerces
    pccValueList = data_calculate(dataList,versionSource,31) # 0表示目标项目为ant1.3   1表示ant1.4   2表示ant1.5    3表示ant1.6  4表示ant.7
    tarketVelocity_1_4 = []
    tarketVelocity_1_4 = result_version(pccValueList,tarketVelocity_1_4,'velocity',9) #29表示选取30个相似的项目 4表示取5个相似的源项目 
    #print(tarketAnt_1_4)
    resultSource = mergeV(tarketVelocity_1_4,len(tarketVelocity_1_4)) #接收合并的源项目集合
    #print(resultSource)#输出resultSource里面是距离目标项目最近的五个最相似的项目
    tarketVersion=readCsv(velocity_1_4_data_source) #读取目标项目文件,返回处理过 Y N 标签的目标项目文件
    #print(tarketVersion)#输出处理过标签的目标项目数据集
    tmpResult = resultSource.loc[:,attr[0:20]] #将原数据集除了bug列 复制一份副本进行接下来的操作
    tmpTarket = tarketVersion.loc[:,attr[0:20]] #将目标项目除了bug列 复制一份副本进行接下来的操作

    #print(tmpTarket.iloc[0]) #输出第1行数据
    trainDataSet = selectTrain(tmpResult,tmpTarket,resultSource,5) #接收训练数据 5表示选择5个实例 10表示选择10个实例

    #导出训练数据和测试数据
    resultTrain=pd.DataFrame(columns=attr,data=trainDataSet)#导出数据 数据有三列，列名分别为attr
    resultTrain.to_csv('G:/Zhaoyu-Experiment/Test-Second/pcc--pcc/10--5/trainVelocity-1.4.csv',index=False)
    testData = pd.DataFrame(columns=attr,data=tarketVersion)#导出数据 数据有三列，列名分别为attr
    testData.to_csv('G:/Zhaoyu-Experiment/Test-Second/pcc--pcc/10--5/testVelocity-1.4.csv',index=False)

main()







import numpy as np
import pandas as pd
#本地数据导入
#根据自己数据文件保存的路径填写(p.s.  python填写路径时，要么使用/，要么使用\\) 
"""
实验思路：1、选取的度量元分布特征可以分两种，一种是趋向于中心趋势，一种是趋向于离散趋势，对于度量元分布特征的选择没有指导规则
2、两阶段筛选相似性，其中筛选项目相似性时可以选择不同的距离公式，已有的是欧氏距离和余弦距离，筛选实例阶段PETERS过滤法，其中的
距离公式有待商榷


"""
def cal_version(data_source,attr):
    df = pd.read_csv(data_source)
    list = [1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0]  
    #中值，均值，最小值，最大值，标准差
    for i in range(len(attr)):
        list[i] = df[attr[i]].median(),df[attr[i]].mean(),df[attr[i]].min(),df[attr[i]].max(),df[attr[i]].std()
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
xerces_1_2_data_source = "G:\\Zhaoyu-Experiment\\EXEDATA\\xerces-1.2.csv"
xerces_1_3_data_source = "G:\\Zhaoyu-Experiment\\EXEDATA\\xerces-1.3.csv"
xerces_1_4_data_source = "G:\\Zhaoyu-Experiment\\EXEDATA\\xerces-1.4.csv"

attr = ('wmc','dit','noc','cbo','rfc','lcom','ca','ce','npm','lcom3','loc','dam','moa','mfa','cam','ic','cbm','amc','max_cc','avg_cc')


ant_1_3 = cal_version(ant_1_3_data_source,attr) #代表一个版本的所有属性的中值，均值，最小值，最大值，标准差
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

xerces_1_2 = cal_version(xerces_1_2_data_source,attr)
xerces_1_3 = cal_version(xerces_1_3_data_source,attr)
xerces_1_4 = cal_version(xerces_1_4_data_source,attr)











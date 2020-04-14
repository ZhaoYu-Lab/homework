import numpy as np
import pandas as pd
from sklearn.preprocessing import scale
import matplotlib.pyplot as plt
#本地数据导入
#根据自己数据文件保存的路径填写(p.s.  python填写路径时，要么使用/，要么使用\\)

ant_1_3_data_source = "G:\\Zhaoyu-Experiment\\EXEDATA\\ant-1.3.csv"
attr = ('wmc','dit','noc','cbo','rfc','lcom','ca','ce','npm','lcom3','loc','dam','moa','mfa','cam','ic','cbm','amc','max_cc','avg_cc')
df = pd.read_csv(ant_1_3_data_source)
# 对log变化前的数据画出直方图
"""
fig, ax = plt.subplots()
df['wmc'].hist(color='#A9C5D3', bins=30)
plt.axvline(df['wmc'].quantile(), color='r', label='Binary line')
plt.legend(fontsize=18, loc='best')
ax.set_xlabel('wmc', fontsize=12)
ax.set_ylabel('frequence', fontsize=12)
ax.set_title('wmcInfo', fontsize=12)
plt.show()
"""
#log转换
#df['log_wmc'] = np.log(df['wmc'].values+1)
#print(df[['wmc', 'log_wmc']].head())

df['wmc'] = np.log(df['wmc'].values+1)
#z-score标准化 (data - data.mean())/data.std() #零-均值规范化
df['z_wmc'] = (df['wmc'] - df['wmc'].mean())/df['wmc'].std()
df['s_wmc'] = scale(df['wmc'] )
print(df[['wmc', 'z_wmc','s_wmc']])
print(df['wmc'].mean(),df['z_wmc'].mean(),df['s_wmc'].mean())
print(df['wmc'].std(),df['z_wmc'].std(),df['s_wmc'].std())
print(df['wmc'].skew(),df['z_wmc'].skew(),df['s_wmc'].skew())
print(df['wmc'].kurt(),df['z_wmc'].kurt(),df['s_wmc'].kurt())
#print(df['wmc'].mean(),df['wmc'].std())
# 对log变化后的数据画出直方图
"""
fig, ax = plt.subplots()
df['wmc'].hist(color='#A9C5D3', bins=30)
plt.axvline(df['wmc'].quantile(), color='r', label='Binary line')
plt.legend(fontsize=18, loc='best')
ax.set_xlabel('wmc', fontsize=12)
ax.set_ylabel('frequence', fontsize=12)
ax.set_title('wmcInfo', fontsize=12)
plt.show()
"""
#z-score后画出直方图
df['wmc'] = (df['wmc'] - df['wmc'].mean())/df['wmc'].std()
"""
fig, ax = plt.subplots()
df['wmc'].hist(color='#A9C5D3', bins=30)
plt.axvline(df['wmc'].quantile(), color='r', label='Binary line')
plt.legend(fontsize=18, loc='best')
ax.set_xlabel('wmc', fontsize=12)
ax.set_ylabel('frequence', fontsize=12)
ax.set_title('wmcInfo', fontsize=12)
plt.show()
"""

 
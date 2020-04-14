# import numpy as np
# import pandas as pd

# import matplotlib.pyplot as plt


# def lwlr(testPoint,xArr,yArr,k=1.0):
#     xMat = np.mat(xArr); yMat = np.mat(yArr).T
#     m = np.shape(xMat)[0]
#     weights = np.mat(np.eye((m)))
#     for j in range(m):                      #next 2 lines create weights matrix
#         diffMat = testPoint - xMat[j,:]   #difference matrix
#         weights[j,j] = np.exp(diffMat*diffMat.T/(-2.0*k**2))   #weighted matrix
#     xTx = xMat.T * (weights * xMat)      
#     if np.linalg.det(xTx) == 0.0:
#         print ("This matrix is singular, cannot do inverse")
#         return
#     ws = xTx.I * (xMat.T * (weights * yMat))   #normal equation
#     return testPoint * w

import numpy as np
import pandas as pd

from numpy import *
import matplotlib.pyplot as plt


def lwlr(testPoint, xArr, yArr, k=1.0):
    xMat = mat(xArr)
    yMat = mat(yArr).T
    m = shape(xMat)[0]  #样本个数
    weights = mat(eye((m))) #单位矩阵,用于存储权重
     # 利用高斯公式创建权重W     遍历所有数据，给它们一个权重  #用高斯核求权重
    for j in range(m):      
        diffMat = testPoint - xMat[j,:]  
        # 高斯核公式2    矩阵*矩阵.T 转行向量为一个值    权重值以指数级衰减
        weights[j, j] = exp(diffMat * diffMat.T / (-2.0 * k ** 2))
    xTx = xMat.T * (weights * xMat)  #括号里面是把样本乘以对应的权重
    # 判断是否有逆矩阵
    if (linalg).det(xTx) == 0.0: 
        print("This matrix is singulat, cannot do inverse1111")
        return
    #样本乘以对应的权重
    ws = xTx.I * (xMat.T * (weights * yMat))  
    return testPoint * ws


# 循环所有点求出所有的预测值
def lwlrTest(testArr, xArr, yArr, k=1.0):
    # 传入的k值决定了样本的权重，1和原来一样一条直线，0.01拟合程度不错，0.003纳入太多噪声点过拟合了
    m = np.shape(testArr)[0]
    yHat = np.zeros(m) #存储预测的label
    
    # 返回该条样本的预测目标值
    for i in range(m):  
        yHat[i] = lwlr(testArr[i], xArr, yArr, k)
    return yHat

def plotData(k):

    df = pd.read_csv('linear_regression_data1.txt',names=range(0,2)) #读取文件资源
    xArr = df[0]
    yArr = df[1]


    #用lwlr对整个数据集进行估计
    yHat = lwlrTest(xArr, xArr, yArr, k )
    xMat = mat(xArr)
    srtInd = xMat[:, 1].argsort(0)#从小到大排序
    xSort = xMat[srtInd][:, 0, :]
    
    #绘制估计出的点构成的曲线
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(xSort[:, 1], yHat[srtInd])
    
    #绘制原始点的散点图
    ax.scatter(xMat[:, 1], mat(yArr), s = 2, c = 'red')
    plt.show()

plotData(1)
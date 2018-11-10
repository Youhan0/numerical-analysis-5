# -*- coding: utf-8 -*-

from sympy import *
import numpy as np

def G_sort(T,j):
    M=T.shape[0]
    N=T.shape[1]  #M为矩阵的行数，N为矩阵的列数
    a=T[j,j]
    r=j
    for rownum in range(j,M):
        if abs(a)<abs(T[rownum,j]):
            a=T[rownum,j]
            r=rownum           #找第j列的第j行及以下的元素中最大的数对应的行数r
            
    temp_row=[]
    for k in range(N):
        temp_row.append(T[j,k])#把第j行存在temp_row里面
    
    for k in range(j,N):       #此处从j开始，只交换j列之后的值
        T[j,k]=T[r,k]          #把第r行的数据放存到第j行
        T[r,k]=temp_row[k]     #把temp_row里的原来的第j行数据存到第r行
    return(T)

def Gauss(T):
    M=T.shape[0]
    N=T.shape[1]  #M为矩阵的行数，N为矩阵的列数
    m=np.mat(np.zeros((M,N)))
    for j in range(N-1):
        T=G_sort(T,j)#找第j列的第j行及以下的元素中最大的，所在行与第j行交换
        for i in range(j+1,M):
            m[i,j]=float(T[i,j])/float(T[j,j])
        for k in range(j+1,M):
            for l in range(j,N):
                T[k,l]=T[k,l]-m[k,j]*T[j,l]
    print("高斯列主元消去法结果为：")
    print(T)
    
    A=np.mat(np.zeros((M,M)))
    b=np.mat(np.zeros((M,1)))
    for i in range(M):
        for j in range(M):
            A[i,j]=T[i,j]
        b[i,0]=T[i,N-1]   #把T还原为A和b
    
    x=np.mat(np.zeros((M,1)))
    x[M-1,0]=b[M-1,0]/A[M-1,M-1]
    for i in range(M-1,-1,-1):
        sum=0
        for j in range(i+1,M):
            sum+=A[i,j]*x[j,0]
        x[i,0]=(b[i,0]-sum)/A[i,i]
    print("解为：")    
    print(x)
    return(x)
    
def main():
#    #此处为手工输入矩阵的方法
#    M=3
#    N=M+1  #M为要输入的系数矩阵的行数和列数，N为融合之后的矩阵的列数
#    T=np.mat(np.zeros((M,N)))
#    for i in range(M):
#        for j in range(N):
#            T[i,j]=input('T['+str(i)+','+str(j)+']=')

   
#测试数据1
#    A=np.mat([[12.0,-3.0,3.0],
#              [-18.0,3.0,-1.0],
#              [1.0,1.0,1.0]
#            ])
#    b=np.mat([[15.0],
#              [-15.0],
#              [6.0]
#            ])
#    T=np.hstack((A,b))
    
#测试数据2
#    A=np.mat([[1.0,1.0,1.0],
#              [0.0,4.0,-1.0],
#              [2.0,-2.0,1.0]
#            ])
#    b=np.mat([[6.0],
#             [5.0],
#             [1.0],
#            ])
#    T=np.hstack((A,b))

#作业数据
    A=np.mat([[1.0,-5.0,-1.0],
          [4.0,1.0,-1.0],
          [2.0,-1.0,-6.0]])
    b=np.mat([[-8.0],
              [13.0],
              [-2.0]])
    T=np.hstack((A,b))

    Gauss(T)
    
if __name__=="__main__":
    main()
    

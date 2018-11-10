# -*- coding: utf-8 -*-

from sympy import *
import numpy as np

def LU(A,b):
    M=A.shape[0]
    N=A.shape[1]  #M为矩阵的行数，N为矩阵的列数
    if M!=N:
        print("错误！输入的不是方阵！")
    L=np.eye(N)
    U=np.mat(np.zeros((N,N)))
    for i in range(N):
        U[0,i]=A[0,i]
        L[i,0]=A[i,0]/U[0,0]
    for r in range(1,N):
        for i in range(r,N):
            sumU=0.0
            sumL=0.0
            for k in range(r):
                sumU+=L[r,k]*U[k,i]
                if r<N-1:
                    sumL+=L[i,k]*U[k,r]
            U[r,i]=A[r,i]-sumU
            
            if r<N-1:
                L[i,r]=(A[i,r]-sumL)/U[r,r]
    print("L=\n",L)
    print("U=\n",U)
    
    #计算y
    y=np.zeros(N)
    y[0]=b[0]
    for i in range(1,N):
        sum=0.0
        for k in range(0,i):
            sum+=L[i,k]*y[k]
        y[i]=b[i]-sum
    print('y=',y)
    
    #计算x
    x=np.zeros(N)
    x[N-1]=y[N-1]/U[N-1,N-1]
    for i in range(N-1,-1,-1):
        sum=0.0
        for k in range(i+1,N):
            sum+=U[i,k]*x[k]
        x[i]=(y[i]-sum)/U[i,i]
    print('x=',x)
    return(x)

def main():
#    #此处为手工输入矩阵的方法
#    N=3    #N为要输入的系数矩阵的行数和列数
#    A=np.mat(np.zeros((N,N)))
#    b=np.mat(np.zeros((N,1)))
#    for i in range(N):
#        for j in range(N):
#            A[i,j]=input('A['+str(i)+','+str(j)+']=')
#        b[i,0]=input('b['+str(i)+','+'0]=')

    
#测试数据1
#    A=np.mat([[12.0,-3.0,3.0],
#              [-18.0,3.0,-1.0],
#              [1.0,1.0,1.0]])
#    b=np.mat([[15.0],
#              [-15.0],
#              [6.0]])
    
#测试数据2
#    A=np.mat([[1.0,1.0,1.0],
#              [0.0,4.0,-1.0],
#              [2.0,-2.0,1.0]])
#    b=np.mat([[6.0],
#             [5.0],
#             [1.0]])
    
#测试数据3
    A=np.mat([[0.001,2.0,3.0],
             [-1.0,3.712,4.632],
             [-2.1,1.072,5.643]])
    b=np.mat([[1.0],
              [2.0],
              [3.0]])
    
#作业数据
    A=np.mat([[-2.0, 1.0, 5.0],
             [4.0, -8.0, 1.0],
             [4.0, -1.0, -1.0]])
    b=np.mat([[15.0],
              [-21.0],
              [7.0]])
    
    LU(A,b)
    
if __name__=="__main__":
    main()
    
    
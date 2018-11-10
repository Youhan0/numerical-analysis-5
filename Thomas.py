# -*- coding: utf-8 -*-

from numpy import *
import numpy as np

#追赶法(Thomas算法)
def Thomas(a,b,c,f):
    n=len(b)
    alpha=np.zeros(n)
    beta=np.zeros(n-1)
    gamma=a#gamma可以不写
    alpha[0]=b[0]
    beta[0]=c[0]/b[0]
    for i in range(1,n-1):
        alpha[i]=b[i]-a[i-1]*beta[i-1]
        beta[i]=c[i]/(b[i]-a[i-1]*beta[i-1])
    alpha[n-1]=b[n-1]-a[n-2]*beta[n-2]
    y=np.zeros(n)
    #解Ly=f
    y[0]=f[0]/b[0]
    for i in range(1,n):
        y[i]=(f[i]-a[i-1]*y[i-1])/(b[i]-a[i-1]*beta[i-1])
    #解Ux=y
    x=np.zeros(n)
    x[n-1]=y[n-1]
    for i in range(n-2,-1,-1):
        x[i]=y[i]-beta[i]*x[i+1]
    
    L=np.zeros((n,n))
    U=np.eye(n,n)
    L[0,0]=alpha[0]
    L[n-1,n-2]=gamma[n-2]
    L[n-1,n-1]=alpha[n-1]
    U[0,1]=beta[0]
    for i in range(1,n-1):
        L[i,i-1]=gamma[i-1]
        L[i,i]=alpha[i]
        U[i,i+1]=beta[i]
#输出矩阵L,U以及解
    print('L=',L)
    print('U=',U)
    print('x=',x)


#将三对角矩阵转化为三个向量
def matrix_trans(A,a,b,c):
    n=len(A)
    a=np.zeros(n-1)
    b=np.zeros(n)
    c=np.zeros(n-1)

    b[0]=A[0,0]
    c[0]=A[0,1]
    a[n-2]=A[n-1,n-2]
    b[n-1]=A[n-1,n-1]
    for i in range(1,n-1):
        a[i-1]=A[i,i-1]
        b[i]=A[i,i]
        c[i]=A[i,i+1]
  
  

#作业数据
a=-np.ones(9)
b=4*np.ones(10)
c=a
f=np.array([7.0, 5.0, -13.0, 2.0, 6.0, -12.0, 14.0, -4.0, 5.0, -5.0])

Thomas(a,b,c,f)


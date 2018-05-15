#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
#Author: xhaichao

import numpy as np
#读入txt文件，返回list
def readTxt(file):
    arr=np.loadtxt(file,str)
    print(isinstance(arr,np.ndarray))
    newarr=arr.copy();
    np.savetxt("111.txt",newarr,"%s");
    for l in arr:
        list = l.split(",")
        print(list)
        #print(list[11] + "====" + list[17] + "====" + list[24])
        if isErrorData(list):
            #newarr.subtract(list)
            pass
    return l

#找出错误的数据
def isErrorData(list):
    if list[17]=='0' and "股票估值增值" in str(list[24]):
        return True;
    else:
        return False;


#根据list生成txt文件
def generateTxt(list):
    pass


#更正错误数据
def changeError(list):
    pass;


if __name__ == '__main__':
    l=readTxt("HSFAVOUCHERS20180420.txt")
    isErrorData(l)
    generateTxt(l)

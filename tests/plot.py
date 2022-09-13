import json
import matplotlib.pyplot as plt
from numpy import mean
import os
from datetime import datetime
from glob import glob

path = './results_img/'
dirs = glob(path+ "/*/")

for dir in dirs:
    log_path = dir+'/test_accuracy.txt'
    with open(log_path, 'r') as f:
        lines = f.readlines()

        X_round = []
        test_acc = []
        for line in lines:
            L = line.split(' ',5)
            # print(L)
            X_round.append(eval(L[2]))
            test_acc.append(eval(L[5]))

        # #label在图示(legend)中显示。若为数学公式，则最好在字符串前后添加"$"符号
        # #color：b:blue、g:green、r:red、c:cyan、m:magenta、y:yellow、k:black、w:white、、、
        # #线型：-  --   -.  :    ， 
        # #marker：.  ，   o   v    <    *    +    1
        ################################################################
        # plt.figure()
        plt.grid(linestyle = "--")      #设置背景网格线为虚线
        # 先画折现图
        # [::-1]
        plt.plot(X_round,test_acc, linewidth=2)
        # 再画散点图
        # plt.scatter(X_round,test_acc,s=100,marker = '.')
        plt.title("Test_acc Per Round")    #默认字体大小为12
        plt.xlabel("Round")
        plt.ylabel("Test_acc")
        plt.legend(dirs) 
        plt.savefig(path+'/test_acc.png')
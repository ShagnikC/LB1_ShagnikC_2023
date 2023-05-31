#!/usr/bin/python3
from math import sqrt
import numpy as np
import sys


def optimize(filename,threshold):

    tp=0
    tn=0
    fp=0
    fn=0

    matrix=np.zeros([2,2])
    #print(matrix)
    with open (filename) as file:
        for line in file:
            line=line.rstrip().split() #so I deleted with r strip the new row and with split I splited line into list with [0]=indentifier [1]=e value [2]=class (0,1)
            #print (line)
            if line[2]=='0':
                if float(line[1])>threshold:
                    matrix[0][0]+=1
                else:
                    matrix[1][0]+=1
            else:
                if float(line[1])<=threshold:
                    matrix[1][1]+=1
                else:
                    matrix[0][1]+=1
        acc=(matrix[1][1]+matrix[0][0])/np.sum(matrix) 
        mat_correlation=(matrix[1][1]*matrix[0][0]-matrix[1][0]*matrix[0][1])/np.sqrt((matrix[1][1]+matrix[0][1])*(matrix[1][1]+matrix[1][0])*(matrix[0][0]+matrix[1][0])*(matrix[0][0]+matrix[0][1]))
        #MCC = (TP*TN – FP*FN) / √(TP+FP)(TP+FN)(TN+FP)(TN+FN)
    
    print(threshold,acc,mat_correlation,list(matrix))

        
             






if __name__=="__main__":
    filename=sys.argv[1]
    threshold=float(sys.argv[2])
    optimize(filename,threshold)

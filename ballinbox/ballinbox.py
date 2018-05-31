import math
import random

pointlist = []
R = []
Result = []
def pointgetter():
    i = 0
    j = 0
    for i in range (1,1000):
        for j in range (1,1000):
            pointlist.append((-1+i*0.002,-1+j*0.002))

def distance(x, y, a, b):

    return math.sqrt((x - a) * (x - a) + (y - b) * (y - b))

def check_and_del(x,y,R_index):
    i = 0
    L = len(R)
    for i in range(0,L):
        if i == R_index:
            continue
        a = pointlist[i][0]
        b = pointlist[i][1]
        #print (distance(x, y, a, b),(R[i] + R[R_index]))
        if distance(x, y, a, b) < (R[i] + R[R_index]):
            R[i] = 0
    R[R_index]=0            

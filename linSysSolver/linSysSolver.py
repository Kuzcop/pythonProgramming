#!/bin/python

from commonImports import *
from logLib import logLib
from commonLib import commonLib

logg = logLib()
clib = commonLib()
fname = 'lin.txt'
logger = logg.startlogging(fname)

############ Run Test #####################
# solve linear equation
#4x +3y = 20
#-5x + 9y = 26

A = np.array([[4, 3], [-5, 9]])
B = np.array([[20], [26]])

X = np.linalg.inv(A).dot(B)

logger.info("The value of x and y is: {}".format(X))

#Cleanup
logg.stoplogging()

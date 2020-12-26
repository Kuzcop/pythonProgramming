#!/bin/python

from commonImports import *
from logLib import logLib
from commonLib import commonLib

#logg = logLib()
#clib = commonLib()

plt.plot([1, 2, 3, 4], [1, 34, 42, 544], 'r--')
plt.ylabel('aman hungry meter')
#plt.show()
plt.savefig('test1.png')

plt.scatter([1, 3, 5, 6], [34, 562, 21, 4])
plt.ylabel('aman\'s attention')
#plt.show()
plt.savefig('test2.jpg')

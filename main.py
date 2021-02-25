from Output import *
from readFiles import *


conf = ReadFiles(0)
output = Output(0)

for k in range(conf.intersectionNumber) :
    s = getStreets(k)

    output.setIntersection(k, s, [1 for i in range(len(s))])








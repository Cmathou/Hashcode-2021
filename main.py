from Output import *
from ReadFiles import *


conf = ReadFiles(0)
output = Output(0)

for k in range(conf.intersectionsNumber) :
    s = conf.getStreets(k)

    output.setIntersection(k, s, [1 for i in range(len(s))])








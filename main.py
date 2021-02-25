from Output import *
from ReadFiles import *
from utils import *

conf = ReadFiles(0)
output = Output(0)

print(computeMinTime(conf))
print(conf.duration)


# for k in range(conf.intersectionsNumber) :
#     s = conf.getStreets(k)

#     output.setIntersection(k, s, [1 for i in range(len(s))])








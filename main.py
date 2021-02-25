from Output import *
from ReadFiles import *
from utils import *

conf = ReadFiles(0)
output = Output(0)
tmin, conf = computeMinTime(conf)
for k in range(conf.intersectionsNumber) :
    s = conf.getStreets(k)

    output.setIntersection(k, s, [conf.streets[i][3] for i in s])








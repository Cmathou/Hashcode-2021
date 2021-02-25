from Output import Output
import readFiles


conf = readFiles(0)
output = Output(0)

for k in range(conf.intersectionNumber) :
    s = getStreet(k)

    output.setIntersection(k, s, [1 for i in range(len(s))])








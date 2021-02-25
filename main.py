from Output import *
from ReadFiles import *
from utils import *
import time
import progressbar
from multiprocessing import Process


def main(file):
	conf = ReadFiles(file)
	output = Output(file)
	tmin, conf = computeMinTime(conf)
	for k in progressbar.progressbar(range(conf.intersectionsNumber)):
	    s = conf.getStreets(k)

	    output.setIntersection(k, s, [conf.streets[i][3] for i in s])




if (__name__ == "__main__"):

	file0 = Process(target=main, args=(0,))
	file1 = Process(target=main, args=(1,))
	file2 = Process(target=main, args=(2,))
	file3 = Process(target=main, args=(3,))
	file4 = Process(target=main, args=(4,))
	file5 = Process(target=main, args=(5,))

	file0.start()
	file1.start()
	file2.start()
	file3.start()
	file4.start()
	file5.start()

	file0.join() #attend la fin de fileX pour la mesure avec time.time()
	file1.join()
	file2.join()
	file3.join()
	file4.join()
	file5.join()




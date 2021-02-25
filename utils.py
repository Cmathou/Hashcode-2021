from ReadFiles import *

def computeMinTime(config):
    tempsMini = [-1 for i in range(config.carNumber)]

    for id, streets in config.cars.items():
        for s in streets :
            tempsMini[id] += config.streets[s][2]
            config.streets[s][3] += 1


    return tempsMini, config


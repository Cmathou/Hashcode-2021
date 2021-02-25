class Output:

    _file = ""

    def __init__(self, file):
        self._file = file
        with open(self._file, "w+") as file:
            file.writelines('0')

    def setIntersection(self, intersection, streets, time):
        with open(self._file, "w+") as file:
            content = file.readlines()
            content[0] = str(int(content[0]) + 1)
            for i in range(len(streets)):
                content.append(intersection + '\n')
                content.append(streets[i] + ' ' + time[i] + '\n')
            file.writelines(content)


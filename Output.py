class Output:

    _file = ""

    def __init__(self, file):
        self._file = "output/" + file
        with open(self._file, "w+") as file:
            file.write('0\n')

    def setIntersection(self, intersection, streets, time):
        with open(self._file, "r") as file:
            content = file.readlines()

        with open(self._file, "w") as file:
            content[0] = str(int(content[0]) + 1) + '\n'
            for i in range(len(streets)):
                content.append(intersection + '\n')
                content.append(streets[i] + ' ' + time[i] + '\n')
            file.writelines(content)


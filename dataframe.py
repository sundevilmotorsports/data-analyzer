# intermediate representation of a data file
import numpy as np

class DataFrame():
    def __init__(self, path) -> None:
        self.path = path
        self.numCol = 0

        # TODO: do the below if it is .txt or .csv
        # if it is .sdm (ie it has other data) we will want different behavior
        raw = open(path, 'r').read().split("\n")

        # create dict, associate each column with an index
        headers = raw[0].split(",")
        pairs = []
        for h in headers:
            pairs.append( (h.strip(), self.numCol) )
            self.numCol += 1
        self.colGuide = dict(pairs)

        # import data into 2d array
        # self.data[self.colGuide[key]] represents data for key
        self.data = []
        for key, val in self.colGuide.items():
            colData = []
            for r in range(1, len(raw)):
                row = raw[r].split(",")
                colData.append(float(row[val]))
            self.data.append(colData)
        self.data = np.array(self.data)
        



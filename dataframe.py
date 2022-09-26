"""
intermediate representation of a data file
"""
import numpy as np

"""
@class DataFrame

@brief Intermediate representation of a data file

A DataFrame is the data structure used to represent a data file that
has been created from the car's data logger.

It consists of:
self.path: path to the data file in the file directory

self.numCol: number of columns (headers) in the frame

self.colGuide: This is a dictionary where the key is the columns' names, and the value is the column's index in self.data
This is used to identify which index of self.data to use when accessing a specific column by name.
For example, to get the rear right shock travel where the header is "RR shock travel (in)":
df.data[df.colGuide["RR shock travel (in)"]]
would get the rear right shock travel data points, sorted by timestamp,
i.e. df.data[df.colGuide["RR shock travel (in)"]][0] would be the data point from the first timestamp recorded by the data logger.

self.data: 2d array of data points, is a numpy array.


"""
class DataFrame():

    # creates a DataFrame from a .csv file
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
                if row[0] == '':
                    continue
                colData.append(float(row[val]))
            self.data.append(colData)
        self.data = np.array(self.data)
        



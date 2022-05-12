import pyqtgraph as pg

class SDMPlot(pg.PlotItem):
    def __init__(self, pi, showAxis=False, **kargs):
        self.pi = pi
        if not showAxis:
            self.pi.getAxis('bottom').setHeight(0)
        self.pi.showGrid(x=True, y=True)
        self.pi.setMouseEnabled(x=True, y=False)
        super().__init__()


    def link(self, other):
        self.pi.setXLink(other)

    def plot(self, **kargs):
        self.pi.plot(**kargs)

    def addItem(self, item, *args, **kargs):
        self.pi.addItem(item, *args, **kargs)

    def sceneBoundingRect(self):
        return self.pi.sceneBoundingRect()

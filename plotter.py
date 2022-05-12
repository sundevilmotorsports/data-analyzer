import pyqtgraph as pg
import numpy as np
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QDockWidget, QComboBox
from PyQt5.QtCore import *
from PyQt5.QtGui import *

app = QApplication(sys.argv)

window = QMainWindow()
window.resize(1600, 900)
window.setWindowTitle("Sun Devil Motorsports Plotter")

graphs = pg.GraphicsLayoutWidget(show=True, title="Basic plotting examples")

p1 = graphs.addPlot(title="Basic array plotting", y=np.random.normal(size=100))
p1.showGrid(x=True,y=True)

graphs.nextRow()

p2 = graphs.addPlot()
p2.plot(np.random.normal(size=100), pen=(255,0,0), name="Red curve")
p2.showGrid(x=True,y=True)
graphs.nextRow()

p3 = graphs.addPlot()
p3.plot(np.random.normal(size=100), pen=(255,0,255), name="Red curve")
p3.showGrid(x=True,y=True)

#cross hair
vLine = pg.InfiniteLine(angle=90, movable=False)
vLine2 = pg.InfiniteLine(angle=90, movable=False)
vLine3 = pg.InfiniteLine(angle=90, movable=False)
p1.addItem(vLine, ignoreBounds=True)
p2.addItem(vLine2, ignoreBounds=True)
p3.addItem(vLine3, ignoreBounds=True)

vb = p1.vb

def mouseMoved(evt):
    pos = evt[0]  ## using signal proxy turns original arguments into a tuple
    if p1.sceneBoundingRect().contains(pos) or p2.sceneBoundingRect().contains(pos) or p3.sceneBoundingRect().contains(pos) :
        mousePoint = vb.mapSceneToView(pos)
        vLine.setPos(mousePoint.x())
        vLine2.setPos(mousePoint.x())
        vLine3.setPos(mousePoint.x())
        
proxy = pg.SignalProxy(p1.scene().sigMouseMoved, rateLimit=60, slot=mouseMoved)

# add graphs to window
window.setCentralWidget(graphs)

# data selector
dock = QDockWidget("Select Data", window)
widget = QWidget()
dock.setWidget(widget)
dock.setFeatures(QDockWidget.NoDockWidgetFeatures)
vbox = QVBoxLayout()
widget.setLayout(vbox)

ctop = QComboBox()
cmid = QComboBox()
cbot = QComboBox() 
vbox.addWidget(ctop)
vbox.addWidget(cmid)
vbox.addWidget(cbot)
window.addDockWidget(Qt.LeftDockWidgetArea, dock)



window.show()

# Start the event loop.
app.exec()
import pyqtgraph as pg
import numpy as np
from dataframe import DataFrame
import observer as obs

graphs = pg.GraphicsLayoutWidget()
graphs.ci.layout.setContentsMargins(1,1,1,1)
graphs.ci.layout.setSpacing(1)

topPlot: pg.PlotItem = graphs.addPlot(y=np.random.normal(size=100))
topPlot.getAxis('bottom').setHeight(0)
topPlot.showGrid(x=True,y=True)
topPlot.setMouseEnabled(x=True, y=False)
graphs.nextRow()

midPlot = graphs.addPlot(y=np.random.normal(size=100))
midPlot.getAxis('bottom').setHeight(0)
midPlot.showGrid(x=True,y=True)
midPlot.setMouseEnabled(x=True, y=False)
midPlot.setXLink(topPlot)
graphs.nextRow()

botPlot = graphs.addPlot()
botPlot.plot(np.random.normal(size=100))
botPlot.showGrid(x=True,y=True)
botPlot.setMouseEnabled(x=True, y=False)
botPlot.setXLink(topPlot)


#cross hair
vLine = pg.InfiniteLine(angle=90, movable=False)
vLine2 = pg.InfiniteLine(angle=90, movable=False)
vLine3 = pg.InfiniteLine(angle=90, movable=False)
topPlot.addItem(vLine, ignoreBounds=False)
midPlot.addItem(vLine2, ignoreBounds=True)
botPlot.addItem(vLine3, ignoreBounds=True)

vb = topPlot.vb

def mouseMoved(evt):
    pos = evt[0]  ## using signal proxy turns original arguments into a tuple
    if topPlot.sceneBoundingRect().contains(pos) or midPlot.sceneBoundingRect().contains(pos) or botPlot.sceneBoundingRect().contains(pos) :
        mousePoint = vb.mapSceneToView(pos)
        vLine.setPos(mousePoint.x())
        vLine2.setPos(mousePoint.x())
        vLine3.setPos(mousePoint.x())
        
proxy = pg.SignalProxy(topPlot.scene().sigMouseMoved, rateLimit=60, slot=mouseMoved)

def initializePlots(df: DataFrame):
    # clear and re-add vertical lines
    topPlot.clear()
    midPlot.clear()
    botPlot.clear()
    topPlot.addItem(vLine, ignoreBounds=False)
    midPlot.addItem(vLine2, ignoreBounds=False)
    botPlot.addItem(vLine3, ignoreBounds=False)

    # initialize plots
    topPlot.plot(df.data[0], df.data[1])
    midPlot.plot(df.data[0], df.data[1])
    botPlot.plot(df.data[0], df.data[1])

def updateGraph(graph: str, header: str):
    headerIndex: int = obs.currentFrame.colGuide[header]
    if graph == "top":
        topPlot.clear()
        topPlot.addItem(vLine, ignoreBounds=False)
        topPlot.plot(obs.currentFrame.data[0], obs.currentFrame.data[headerIndex])
    elif graph == "mid":
        midPlot.clear()
        midPlot.addItem(vLine2, ignoreBounds=False)
        midPlot.plot(obs.currentFrame.data[0], obs.currentFrame.data[headerIndex])
    elif graph == "bot":
        botPlot.clear()
        botPlot.addItem(vLine3, ignoreBounds=False)
        botPlot.plot(obs.currentFrame.data[0], obs.currentFrame.data[headerIndex])

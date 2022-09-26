"""
Entry point for the software
"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDockWidget
from PyQt5.QtCore import *
from PyQt5.QtGui import *

app = QApplication(sys.argv)

window = QMainWindow()
window.resize(1600, 900)
window.setWindowTitle("Sun Devil Motorsports Plotter Utility")

# sidebar where we can select columns
import selector

# tool bar where we can add dockable plugins, import and save data
import toolbar

# manages plots
import plotmanager

# add graphs to window
window.setCentralWidget(plotmanager.graphs)

# data selector
dock = QDockWidget("Data Selector", window)
dock.setFeatures(QDockWidget.NoDockWidgetFeatures)
dock.setWidget(selector.widget)

window.addDockWidget(Qt.LeftDockWidgetArea, dock)
window.addToolBar(toolbar.bar)

# show the window
window.show()

# Start the event loop.
app.exec()
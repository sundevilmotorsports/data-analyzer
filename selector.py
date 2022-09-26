"""
Selects the data for a plot
"""
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QComboBox
from dataframe import DataFrame
import plotmanager as pm



widget = QWidget()      # the widget to be added to the QMainWindow in main.py
vbox = QVBoxLayout()    # layout for the widget
widget.setLayout(vbox)

ctop = QComboBox()      # shows options for the top plot
cmid = QComboBox()      # shows options for the middle plot
cbot = QComboBox()      # shows options for the bottom plot
vbox.addWidget(ctop)
vbox.addWidget(cmid)
vbox.addWidget(cbot)

# when a selection is changed, call updateGraph
# with the chosen header
def on_selection_change_top(i):
    pm.updateGraph("top", str(ctop.currentText()))

def on_selection_change_mid(i):
    pm.updateGraph("mid", str(cmid.currentText()))

def on_selection_change_bot(i):
    pm.updateGraph("bot", str(cbot.currentText()))

ctop.activated.connect(on_selection_change_top)
cmid.activated.connect(on_selection_change_mid)
cbot.activated.connect(on_selection_change_bot)

# update options in the combo boxes
# this is called in toolbar.py when a file is imported.
def update_options(df: DataFrame):
    ctop.addItems(df.colGuide)
    cmid.addItems(df.colGuide)
    cbot.addItems(df.colGuide)
    ctop.setCurrentIndex(1)
    cmid.setCurrentIndex(1)
    cbot.setCurrentIndex(1)
    pm.initializePlots(df)


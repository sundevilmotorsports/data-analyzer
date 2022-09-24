"""
Selects the data for a plot
"""
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QComboBox
from dataframe import DataFrame
import plotmanager as pm



widget = QWidget()
vbox = QVBoxLayout()
widget.setLayout(vbox)

ctop = QComboBox()
cmid = QComboBox()
cbot = QComboBox() 
vbox.addWidget(ctop)
vbox.addWidget(cmid)
vbox.addWidget(cbot)

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
def update_options(df: DataFrame):
    ctop.addItems(df.colGuide)
    cmid.addItems(df.colGuide)
    cbot.addItems(df.colGuide)
    ctop.setCurrentIndex(1)
    cmid.setCurrentIndex(1)
    cbot.setCurrentIndex(1)
    pm.initializePlots(df)


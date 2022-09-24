"""
Tool bar: if any widgets 
"""
from PyQt5.QtWidgets import QFileDialog, QToolBar, QAction
from dataframe import DataFrame
import observer
import selector

bar = QToolBar()

"""
button handler
"""
def onPress(a):
    if a.text() == "Import\nFile":
        file = QFileDialog()
        file.setAcceptMode(QFileDialog.AcceptOpen)
        file.setAcceptDrops(True)
        fname = file.getOpenFileName()[0] # index 0 is filepath, index 1 is something weird
        if fname == "":
            print("no file selected")
        else:
            print(fname)
            observer.currentFrame = DataFrame(fname)
            selector.update_options(observer.currentFrame)
    elif a.text() == "Movement\nData":
        print(a.text())
    elif a.text() == "Track\nMap":
        print(a.text())

actionImport = QAction("Import\nFile")
actionSave = QAction("Save\nFile")
actionDetails = QAction("Show\nDetails")
bar.addAction(actionImport)
bar.addAction(actionSave)
bar.addAction(actionDetails)
bar.addSeparator()

actionTyre = QAction("Tyre\nData")
actionMovement = QAction("Movement\nData")
actionTrack = QAction("Track\nMap")
actionLapComparison = QAction("Lap\nComparison")
customChannel = QAction("Custom\nChannel")
bar.addAction(actionTyre)
bar.addAction(actionMovement)
bar.addAction(actionTrack)
bar.addAction(actionLapComparison)
bar.addAction(customChannel)

bar.actionTriggered[QAction].connect(onPress)


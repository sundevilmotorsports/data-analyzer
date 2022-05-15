from PyQt5.QtWidgets import QFileDialog, QToolBar, QAction
from dataframe import DataFrame
import observer

bar = QToolBar()

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

actionImport = QAction("Import\nFile")
actionSave = QAction("Save\nFile")
actionDetails = QAction("Show\nDetails")
bar.addAction(actionImport)
bar.addAction(actionSave)
bar.addAction(actionDetails)
bar.addSeparator()

actionMovement = QAction("Movement\nData")
actionTrack = QAction("Track\nMap")
actionLapComparison = QAction("Lap\nComparison")
customChannel = QAction("Custom\nChannel")
bar.addAction(actionMovement)
bar.addAction(actionTrack)
bar.addAction(actionLapComparison)
bar.addAction(customChannel)

bar.actionTriggered[QAction].connect(onPress)


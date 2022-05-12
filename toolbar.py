from PyQt5.QtWidgets import QFileDialog, QToolBar, QAction

bar = QToolBar()

def onPress(a):
    print(a.text())

actionImport = QAction("Import\nFile")
actionSave = QAction("Save\nFile")
bar.addAction(actionImport)
bar.addAction(actionSave)
bar.addSeparator()

actionMovement = QAction("Movement\nData")
actionTrack = QAction("Track\nMap")
actionLapComparison = QAction("Lap\nComparison")
bar.addAction(actionMovement)
bar.addAction(actionTrack)
bar.addAction(actionLapComparison)

bar.actionTriggered[QAction].connect(onPress)


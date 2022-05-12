from PyQt5.QtWidgets import QFileDialog, QToolBar, QAction

bar = QToolBar()

def onPress(a):
    print(a.text())
    if a.text() == "Import\nFile":
        print("owowowowowowo")

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
bar.addAction(actionMovement)
bar.addAction(actionTrack)
bar.addAction(actionLapComparison)

bar.actionTriggered[QAction].connect(onPress)


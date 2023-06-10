from PyQt5.QtWidgets import *
from csv_import import CSVImporter

class SDMToolBar(QToolBar):
    def __init__(self):
        super().__init__()

        self.actionAddFile = QAction("Add\nFile", self)
        self.actionAddFile.triggered.connect(self.add_file)
        self.actionGGPlot = QAction("Generate\nG-G Plot", self)
        self.actionDampers = QAction("Generate\nDamper Histogram", self)
        self.actionGPS = QAction("Generate\nTrack Map", self)
        self.actionLine = QAction("Generate\nLine Plot", self)
        self.actionScatter = QAction("Generate\nScatter Plot", self)
        
        self.addAction(self.actionAddFile)
        self.addAction(self.actionGGPlot)
        self.addAction(self.actionDampers)
        self.addAction(self.actionLine)
        self.addAction(self.actionScatter)
    
    def add_file(self):
        filename = QFileDialog.getOpenFileName()
        if filename[0] == "":
            return
        importer = CSVImporter(filename[0])
        importer.exec()
        


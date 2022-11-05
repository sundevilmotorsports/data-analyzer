import os
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QPushButton, QLineEdit, QGroupBox, QVBoxLayout, \
    QTextEdit
from PyQt5.QtCore import QTimer
import irsdk
import json


# import telemetry


class Logger(QWidget):
    def __init__(self) -> None:
        super().__init__()
        super().setWindowTitle("iRacing Data Logger")
        super().setFixedSize(800, 400)
        self.lyt: QVBoxLayout = QVBoxLayout()
        super().setLayout(self.lyt)

        # file setup
        self.lytFile: QGridLayout = QGridLayout()
        self.fileBox: QGroupBox = QGroupBox()
        self.fileBox.setLayout(self.lytFile)
        self.fileBox.setTitle("File Setup")
        self.lyt.addWidget(self.fileBox)

        # all 9 labels: Date, session info, car, track, track config
        #               Setup Notes, Changes from Previous tests,
        #               Driver Feedback, and path to CSV file
        self.lblDate: QLabel = QLabel("Date")
        self.lblSessionNum_Name: QLabel = QLabel("Session #/Name")
        self.lblCar: QLabel = QLabel("Car")
        self.lblTrack: QLabel = QLabel("Track")
        self.lblConfig: QLabel = QLabel("Track Config")
        self.lblSetupNotes: QLabel = QLabel("Setup Notes")
        self.lblPrevTests: QLabel = QLabel("Changes from Previous Tests")
        self.lblDriverFeedback: QLabel = QLabel("Driver Feedback")
        self.lblCSVPath: QLabel = QLabel("Path to CSV File")

        # all 9 edit boxes: Date, session info, car, track, track config
        #                   Setup Notes, Changes from Previous tests,
        #                   Driver Feedback, and path to CSV file
        self.editDate: QLineEdit = QLineEdit()
        self.editSessionNum_Name: QLineEdit = QLineEdit()
        self.editCar: QLineEdit = QLineEdit()
        self.editTrack: QLineEdit = QLineEdit()
        self.editConfig: QLineEdit = QLineEdit()
        self.editSetupNotes: QTextEdit = QTextEdit()
        self.editPrevChanges: QTextEdit = QTextEdit()
        self.editFeedback: QTextEdit = QTextEdit()
        self.editCSVPath: QTextEdit = QTextEdit()

        # organizes labels vertically and puts one
        # label and one edit box together horizonatally
        self.lytFile.addWidget(self.lblDate, 0, 0)
        self.lytFile.addWidget(self.editDate, 0, 1)
        self.lytFile.addWidget(self.lblSessionNum_Name, 1, 0)
        self.lytFile.addWidget(self.editSessionNum_Name, 1, 1)
        self.lytFile.addWidget(self.lblCar, 2, 0)
        self.lytFile.addWidget(self.editCar, 2, 1)
        self.lytFile.addWidget(self.lblTrack, 3, 0)
        self.lytFile.addWidget(self.editTrack, 3, 1)
        self.lytFile.addWidget(self.lblConfig, 4, 0)
        self.lytFile.addWidget(self.editConfig, 4, 1)
        self.lytFile.addWidget(self.lblSetupNotes, 5, 0)
        self.lytFile.addWidget(self.editSetupNotes, 5, 1)
        self.lytFile.addWidget(self.lblPrevTests, 6, 0)
        self.lytFile.addWidget(self.editPrevChanges, 6, 1)
        self.lytFile.addWidget(self.lblDriverFeedback, 7, 0)
        self.lytFile.addWidget(self.editFeedback, 7, 1)
        self.lytFile.addWidget(self.lblCSVPath, 8, 0)
        self.lytFile.addWidget(self.editCSVPath, 8, 1)

        # start/stop logging
        self.btnLog: QPushButton = QPushButton("Start Logging")
        self.btnLog.clicked.connect(self.log)
        self.lblStatus: QLabel = QLabel("")
        self.lyt.addWidget(self.btnLog)
        self.lyt.addWidget(self.lblStatus)

        # irsdk setup
        self.ir = irsdk.IRSDK()
        self.ir.startup()

        # data
        self.lapTimes = []
        self.filepath = ""

    def log(self):
        # this starts the logging process
        if self.btnLog.text() == "Start Logging":
            self.lblStatus.setText("Logging")
            self.btnLog.setText("Stop Logging")

            # stores data as a dictionary and creates a folder name
            data = self.getSetupData()
            self.filepath = data["date"] + "_" + data["session #/name"] + "/"

            # if folder name doesn't exist yet, make a new folder
            if not os.path.exists(self.filepath):
                os.makedirs(self.filepath)

            # make a json file and dump the data dictionary into it
            f = open(self.filepath + "info.json", "w")
            json_obj = json.dumps(data, indent=4)
            f.write(json_obj)
            f.close()

        # ends logging process and sets up for next logging
        else:
            self.lblStatus.setText("")
            self.btnLog.setText("Start Logging")
            print("finished logging")

    # makes the dictionary with the 9 important labels in order
    # stores the corresponding data from the edit boxes
    def getSetupData(self):
        payload = {}
        payload["date"] = (self.editDate.text())
        payload["session #/name"] = (self.editSessionNum_Name.text())
        payload["car"] = (self.editCar.text())
        payload["track"] = (self.editTrack.text())
        payload["config"] = (self.editConfig.text())
        payload["setup notes"] = (self.editSetupNotes.toPlainText())
        payload["changes from previous tests"] = (self.editPrevChanges.toPlainText())
        payload["driver feedback"] = (self.editFeedback.toPlainText())
        payload["pathname of csv"] = (self.editCSVPath.toPlainText())

        return payload


def main():
    app = QApplication(sys.argv)
    logger = Logger()
    logger.show()
    sys.exit(app.exec_())


main()

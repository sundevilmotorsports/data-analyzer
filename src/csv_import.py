"""
Widget for importing a .csv
"""
from PyQt5.QtWidgets import QDialog, QComboBox, QPushButton, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QGridLayout
import pandas as pd
import active

class CSVImporter(QDialog):
    def __init__(self, filename: str):
        super().__init__()

        # select: lap column, time column, GPS columns
        # name: session + date, optionally driver, car, track
        self.df: pd.DataFrame = pd.read_csv(filename)
        columns = list(self.df.columns)

        layout: QVBoxLayout = QVBoxLayout()
        self.setLayout(layout)
        self.setWindowTitle("Import .csv file")

        # column select
        col_select_layout: QGridLayout = QGridLayout()
        self.combo_time = QComboBox()
        self.combo_lap = QComboBox()
        self.combo_lat = QComboBox()
        self.combo_lon = QComboBox()
        self.combo_time.addItems(columns)
        self.combo_lap.addItems(columns)
        self.combo_lat.addItems(columns)
        self.combo_lon.addItems(columns)
        col_select_layout.addWidget(QLabel("Select Time"), 0, 0)
        col_select_layout.addWidget(QLabel("Select Lap"), 0, 1)
        col_select_layout.addWidget(QLabel("Select GPS Latitude"), 0, 2)
        col_select_layout.addWidget(QLabel("Select GPS Longitude"), 0, 3)
        col_select_layout.addWidget(self.combo_time, 1, 0)
        col_select_layout.addWidget(self.combo_lap, 1, 1)
        col_select_layout.addWidget(self.combo_lat, 1, 2)
        col_select_layout.addWidget(self.combo_lon, 1, 3)

        # session details
        session_details_layout: QVBoxLayout = QVBoxLayout()
        self.edit_name = QLineEdit("Session Name")
        self.edit_date = QLineEdit("Session Date")
        self.edit_driver = QLineEdit("Driver")
        self.edit_car = QLineEdit("Car")
        self.edit_track = QLineEdit("Track Name")
        session_details_layout.addWidget(self.edit_name)
        session_details_layout.addWidget(self.edit_date)
        session_details_layout.addWidget(self.edit_driver)
        session_details_layout.addWidget(self.edit_car)
        session_details_layout.addWidget(self.edit_track)

        # dialog management
        mgmt_layout: QHBoxLayout = QHBoxLayout()
        self.btn_cancel = QPushButton("Cancel")
        self.btn_cancel.clicked.connect(self.cancel)
        self.btn_import = QPushButton("Import")
        self.btn_import.clicked.connect(self.accept)
        mgmt_layout.addWidget(self.btn_cancel)
        mgmt_layout.addWidget(self.btn_import)

        layout.addLayout(col_select_layout)
        layout.addLayout(session_details_layout)
        layout.addLayout(mgmt_layout)

    def cancel(self):
        self.done(0)

    def accept(self):
        time_idx = self.combo_time.currentText()
        lap_idx = self.combo_lap.currentText()
        lat_idx = self.combo_lat.currentText()
        lon_idx = self.combo_lon.currentText()

        name = self.edit_name.text()
        date = self.edit_date.text()
        driver = self.edit_driver.text()
        car = self.edit_car.text()
        track = self.edit_track.text()

        active.add_session(self.df, time_idx, lap_idx, lat_idx, lon_idx, name, date, driver, car, track)

        self.done(1)
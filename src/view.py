import pyqtgraph as pg
import active
from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QCheckBox, QVBoxLayout, QHBoxLayout

class View(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        #laps = active.get_laps()

        # view config settings
        layout_config = QHBoxLayout()
        chk_lap_comparison = QCheckBox("Enable Lap Comparison")
        layout_config.addWidget(chk_lap_comparison)
        combo_select_lap = QComboBox()
        #combo_select_lap.addItems(laps)
        layout_config.addWidget(QLabel("Select Comparison Lap"))
        layout_config.addWidget(combo_select_lap)
        layout.addLayout(layout_config)



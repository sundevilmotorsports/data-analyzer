from PyQt5.QtWidgets import QVBoxLayout, QWidget, QComboBox
widget = QWidget()
vbox = QVBoxLayout()
widget.setLayout(vbox)

ctop = QComboBox()
cmid = QComboBox()
cbot = QComboBox() 
vbox.addWidget(ctop)
vbox.addWidget(cmid)
vbox.addWidget(cbot)


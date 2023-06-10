from PyQt5 import QtWidgets, QtGui, QtCore
import sys, os, time
from toolbar import SDMToolBar
from view import View

basedir = os.path.dirname(__file__)
version_str = "v0.1.0"

try:
    from ctypes import windll  # Only exists on Windows.
    myappid = "sundevilmotorsports.datastudio." + version_str
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("SDM Data Studio")
        self.resize(1600, 900)
        view = View()
        self.setCentralWidget(view)

        toolbar = SDMToolBar()
        self.addToolBar(toolbar)
        self.show()


def splashscreen():
    # Create splashscreen
    splash_pix = QtGui.QPixmap(os.path.join(basedir, "resources/SAETeamLogo.png"))
    splash = QtWidgets.QSplashScreen(splash_pix, QtCore.Qt.WindowStaysOnTopHint)
    # add fade to splashscreen 
    opaqueness = 0.0
    step = 0.1
    splash.setWindowOpacity(opaqueness)
    splash.show()
    while opaqueness < 1:
        splash.setWindowOpacity(opaqueness)
        time.sleep(step) # Gradually appears
        opaqueness+=step
    time.sleep(1) # hold image on screen for a while
    splash.close() # close the splash screen

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(os.path.join(basedir, "resources/Logo.ico")))
    #splashscreen()
    w = MainWindow()
    app.exec()

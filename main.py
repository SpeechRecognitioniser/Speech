import sys
import os
import ctypes
from PySide2 import *
from newgui import *

# Showing tray icon
myappid = 'mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.setWindowTitle("VRec")
        self.setWindowIcon(QIcon("resources/trayIcon.png"))

        #Added fonts
        QFontDatabase.addApplicationFont(":/resources/JetBrainsMono-ExtraBold.ttf")
        QFontDatabase.addApplicationFont(":/resources/JetBrainsMono-Light.ttf")
        QFontDatabase.addApplicationFont(":/resources/JetBrainsMono-SemiBoldBold.ttf")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

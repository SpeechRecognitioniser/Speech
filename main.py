import sys
import ctypes
import os
from newgui import *
from subprocess import Popen

from PyQt5.QtCore import *

from functions import *
from PySide2.QtGui import QCloseEvent
from functions import def_window

# Showing tray icon
myappid = 'mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

# Main window class
class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.setWindowTitle("VRec")
        self.setWindowIcon(QIcon("resources/trayIcon.png"))
        self.ui.voiceRecText.setReadOnly(True)
        self.ui.fileText.setReadOnly(True)
        self.setFixedSize(600, 674)

        #Added fonts
        QFontDatabase.addApplicationFont(":/resources/JetBrainsMono-ExtraBold.ttf")
        QFontDatabase.addApplicationFont(":/resources/JetBrainsMono-Light.ttf")
        QFontDatabase.addApplicationFont(":/resources/JetBrainsMono-SemiBoldBold.ttf")

        # Added threading to the application
        self.threadpoolBot = QThreadPool()
        self.ui.botTalkButton.clicked.connect(lambda: self.bot_test())

        self.threadpoolSpeech = QThreadPool()
        self.ui.voiceRecButton.clicked.connect(lambda: self.speech_test())


        self.ui.fileRecognizeButton.clicked.connect(lambda: self.showOpenFileDialog())

    def closeEvent(self, event):
        event.accept()
        os.system("C:/Users/sea25/Desktop/smth.bat")


    # Opening file and converting text from it to speech
    def showOpenFileDialog(self):
        self.ui.fileText.clear()
        fileName, filter = QFileDialog.getOpenFileName(self, 'Open file',
                                                       'some/default/path/', 'wav files (*.wav)')

        text = from_audio_to_text(fileName)
        self.ui.fileText.insertPlainText(text)


    # Disabling buttons when necessary
    def button_control(self, access):
        self.ui.botTalkButton.setDisabled(access)
        self.ui.voiceRecButton.setDisabled(access)
        self.ui.fileRecognizeButton.setDisabled(access)


    # Functions for the correct use of multithreading
    def bot_test(self):
        test_bot_obj = Bot()
        self.threadpoolBot.start(test_bot_obj)

    def speech_test(self):
        test_speech_obj = SpeechRec()
        self.threadpoolSpeech.start(test_speech_obj)


# Starting point of the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    def_window(window)


    # Classes for using slots and threading features
    class Bot(QRunnable):
        @pyqtSlot()
        def run(self):
            window.button_control(True)
            make_it_say(str(window.ui.botTalkText.toPlainText()))
            window.button_control(False)

    class SpeechRec(QRunnable):
        @pyqtSlot()
        def run(self):
            window.button_control(True)
            user_speech()
            window.ui.voiceRecText.clear()
            window.button_control(False)

    sys.exit(app.exec_())

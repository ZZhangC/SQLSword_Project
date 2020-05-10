'''
    SQL_Sword
    Version: 1.0
    Author: ZZhangC
'''
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import mwindow, ewindow, awindow, swindow, c1window, c2window, scwindow, sfwindow, sswindow
import threading

if __name__ == '__main__':
    scanres = False

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ErrorWindow = QMainWindow()
    SuccessWindow = QMainWindow()
    AboutWindow = QMainWindow()
    Connect1Window = QMainWindow()
    Connect2Window = QMainWindow()
    ScanWindow = QMainWindow()
    ScanFaildWindow = QMainWindow()
    ScanSuccessWindow = QMainWindow()

    ui = mwindow.Ui_MainWindow()
    eui = ewindow.Ui_Dialog()
    sui = swindow.Ui_Dialog()
    aui = awindow.Ui_Dialog()
    c1ui = c1window.Ui_Dialog()
    c2ui = c2window.Ui_Dialog()
    scui = scwindow.Ui_Form()
    sfui = sfwindow.Ui_Dialog()
    ssui = sswindow.Ui_Dialog()

    ui.setupUi(MainWindow)
    eui.setupUi(ErrorWindow)
    sui.setupUi(SuccessWindow)
    aui.setupUi(AboutWindow)
    c1ui.setupUi(Connect1Window)
    c2ui.setupUi(Connect2Window)
    scui.setupUi(ScanWindow)
    sfui.setupUi(ScanFaildWindow)
    ssui.setupUi(ScanSuccessWindow)

    MainWindow.show()

    ui.commandLinkButton.clicked.connect(ErrorWindow.show)
    ui.commandLinkButton_2.clicked.connect(ErrorWindow.show)
    ui.actionHelp.triggered.connect(AboutWindow.show)
    ui.pushButton_4.clicked.connect(Connect1Window.show)
    eui.pushButton.clicked.connect(ErrorWindow.close)
    sui.pushButton.clicked.connect(SuccessWindow.close)
    aui.pushButton.clicked.connect(AboutWindow.close)
    c1ui.pushButton.clicked.connect(Connect1Window.close)
    c2ui.pushButton.clicked.connect(Connect2Window.close)
    sfui.pushButton.clicked.connect(ScanFaildWindow.close)
    ssui.pushButton.clicked.connect(ScanSuccessWindow.close)
    ui.pushButton_9.clicked.connect(ScanWindow.show)

    sys.exit(app.exec_())

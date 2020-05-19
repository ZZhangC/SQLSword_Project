'''
    SQL_Sword
    Version: 1.0
    Author: ZZhangC
'''
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import mwindow, ewindow, awindow, swindow, c1window, c2window, scwindow, sfwindow, sswindow, hewindow
from requests import get
import threading

conn = False

def Check():
    t = threading.Thread(target=CheckConnect, name='1')
    t.start()
    t.join()

def CheckConnect():
    url = ''
    url = MainWindow.lineEdit.text()
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edg/81.0.416.72'}
    if url[0:7] != 'http://' or url[0:7] != 'http:\\\\' or url[0:8] != 'https://' or url[0:8] != 'https:\\\\':
        url = 'http://' + url
    res = get(url,headers=headers)
    if str(res)[11:14] == '200':
        conn = True

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
    HugeErrorWindow = QMainWindow()

    ui = mwindow.Ui_MainWindow()
    eui = ewindow.Ui_Dialog()
    sui = swindow.Ui_Dialog()
    aui = awindow.Ui_Dialog()
    c1ui = c1window.Ui_Dialog()
    c2ui = c2window.Ui_Dialog()
    scui = scwindow.Ui_Form()
    sfui = sfwindow.Ui_Dialog()
    ssui = sswindow.Ui_Dialog()
    heui = hewindow.Ui_Dialog()

    ui.setupUi(MainWindow)
    eui.setupUi(ErrorWindow)
    sui.setupUi(SuccessWindow)
    aui.setupUi(AboutWindow)
    c1ui.setupUi(Connect1Window)
    c2ui.setupUi(Connect2Window)
    scui.setupUi(ScanWindow)
    sfui.setupUi(ScanFaildWindow)
    ssui.setupUi(ScanSuccessWindow)
    heui.setupUi(HugeErrorWindow)

    MainWindow.show()

    ui.commandLinkButton.clicked.connect(ErrorWindow.show)
    ui.commandLinkButton_2.clicked.connect(ErrorWindow.show)
    ui.actionHelp.triggered.connect(AboutWindow.show)
    ui.pushButton_4.clicked.connect(Check)
    ui.pushButton_9.clicked.connect(ScanWindow.show)
    eui.pushButton.clicked.connect(ErrorWindow.close)
    sui.pushButton.clicked.connect(SuccessWindow.close)
    aui.pushButton.clicked.connect(AboutWindow.close)
    c1ui.pushButton.clicked.connect(Connect1Window.close)
    c2ui.pushButton.clicked.connect(Connect2Window.close)
    sfui.pushButton.clicked.connect(ScanFaildWindow.close)
    ssui.pushButton.clicked.connect(ScanSuccessWindow.close)
    heui.pushButton.clicked.connect(HugeErrorWindow.close)

    sys.exit(app.exec_())

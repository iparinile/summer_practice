from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication, QLabel,QVBoxLayout)
import gspread
import datetime
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('My Project 15632-57e3df5f35d4.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open("Where is the money Lebowski?").sheet1
date = datetime.date.today()

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.button = QPushButton('Нажмите для занесения даты в таблицу', self)
        self.label = QLabel(self)
        self.button.clicked.connect(self.handleButton)
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.button)

    def handleButton(self):
        self.label.setText('Дата занесена в таблицу!')
        wks.append_row([str(date)])

if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

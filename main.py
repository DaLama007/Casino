from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QMainWindow, QWidget, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import sys

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.settings()
        self.initUi()
        
        

    def settings(self):
        self.setWindowTitle("Casino")
        self.showFullScreen()
        

    def initUi(self):
        central_widget = QWidget()
        userMoney = QLabel("Money")
        userCard1 = QLabel()
        userCard2 = QLabel()
        

        button_hit = QPushButton()
        button_stand = QPushButton()
        button_double = QPushButton()

        main = QGridLayout()
        central_widget.setLayout(main)
        main.addWidget(userMoney, 5, 2)
        main.addWidget(userCard1, 5, 1)
        #main.addWidget(userMoney, 0, 0)
        
        self.setCentralWidget(central_widget)

        
    
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_F11:
            self.showNormal()
        elif e.key() == Qt.Key_Escape:
            self.close()


        

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Main()
    window.show()
    App.exec()


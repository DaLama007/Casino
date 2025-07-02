from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLineEdit
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt

import sys
from blackjack import Blackjack

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.settings()
        self.initUi()
        
        

    def settings(self):
        custom_font = QFont("Times", 30, QFont.Bold)
        QApplication.setFont(custom_font)
        self.setWindowTitle("Casino")
        self.showFullScreen()
        

    def initUi(self):
        central_widget = QWidget()
        userMoney = QLabel("Money")
        current_bet = QLabel('Curr Bet:')
        label_bet = QLabel('Bet:')
        input_bet = QLineEdit()
        userCard1 = QLabel('card1')
        userCard2 = QLabel('card2')
        Instruction1 = QLabel("H for Hit")
        Instruction2 = QLabel("S for Stand")
        Instruction3 = QLabel("D for Double")
        

        button_hit = QPushButton()
        button_stand = QPushButton()
        button_double = QPushButton()

        
        row1 = QHBoxLayout()
        row2 = QHBoxLayout()
        row3 = QHBoxLayout()
        row4 = QHBoxLayout()
        row5 = QHBoxLayout()
        row6 = QHBoxLayout()
        row7 = QHBoxLayout()
        
        
        
        row1.addWidget(userMoney)
        row6.addWidget(label_bet)
        row6.addWidget(input_bet)
        row5.addWidget(userCard1)
        row5.addWidget(userCard2)
        row5.addWidget(current_bet)
        row7.addWidget(Instruction1)
        row7.addWidget(Instruction2)
        row7.addWidget(Instruction3)
        
        master= QVBoxLayout()
        master.addLayout(row1)
        master.addLayout(row2)
        master.addLayout(row3)
        master.addLayout(row4)
        master.addLayout(row5)
        master.addLayout(row6)
        master.addLayout(row7)

        central_widget.setLayout(master)
        self.setCentralWidget(central_widget)
    
    def updateCards(self):
        self.userCard1
        self.userCard2
        self.userCard3
        self.userCard4
        self.userCard5
        self.userCard6
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_F11:
            self.showNormal()
        elif e.key() == Qt.Key_Escape:
            self.close()
        elif e.key() == Qt.Key_H:
            Blackjack.hit()


        

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Main()
    window.show()
    App.exec()


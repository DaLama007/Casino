from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLineEdit
from PyQt5.QtGui import QPixmap, QFont, QPalette
from PyQt5.QtCore import *
import time

import sys
from blackjack import Blackjack

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.userMoney =  1000
        self.game_state="start"
        self.settings()
        self.initUi()
        self.handle_buttonclick()
        
        
        
        

    def settings(self):
        custom_font = QFont("Times", 30, QFont.Bold)
        self.normal_stylesheet = "color : white"
        QApplication.setFont(custom_font)
        self.setWindowTitle("Casino")
        self.showFullScreen()
        

    def initUi(self):
        self.error_stylesheet = "color : red"
        self.setStyleSheet("""
            QWidget {
                background-color: #333; /* Darker background color */
                color: #fff; /* Text color */
            }

            QPushButton {
                background-color: #66a3ff; /* Lighter background color for buttons */
                color: #333; /* Text color for buttons */
                border: 1px solid #fff; /* White border for buttons */
                border-radius: 5px; /* Rounded corners for buttons */
                padding: 5px 10px; /* Padding for buttons */
            }

            QPushButton:hover {
                background-color: #3399ff; /* Lighter background color for buttons on hover */
            }
        """)
        self.label_result = QLabel("...",self)

        central_widget = QWidget()
        label_Money = QLabel("Money:")
        self.label_userMoney = QLabel(str(self.userMoney))
        current_bet = QLabel('Curr Bet:')
        self.current_bet_display = QLabel('---')
        label_bet = QLabel('Bet:')
        self.input_bet = QLineEdit(self)
        self.button_bet = QPushButton("Bet")
        
        
        image_card1 = QPixmap('Cards/card_extra_back_1.png')
        scaled_back_card = image_card1.scaled(image_card1.width() * 5, image_card1.height() * 5)

        self.userCards = []

        for i in range(0,6):
            userCard = QLabel()
            userCard.setPixmap(scaled_back_card)
            self.userCards.append(userCard)
        
        #DEALER CARDS

        image_card = QPixmap('Cards/card_extra_back_2.png')
        scaled_back_card = image_card.scaled(image_card.width() * 5, image_card.height() * 5)

        self.dealerCards = []

        for i in range(0,6):
            dealerCard = QLabel()
            dealerCard.setPixmap(scaled_back_card)
            self.dealerCards.append(dealerCard)

        #----------------------------------

        Instruction1 = QLabel("H for Hit")
        Instruction2 = QLabel("S for Stand")
        Instruction3 = QLabel("D for Double")

        
        self.row1 = QHBoxLayout()
        self.row2 = QHBoxLayout()
        self.row3 = QHBoxLayout()
        self.row4 = QHBoxLayout()
        self.row5 = QHBoxLayout()
        self.row6 = QHBoxLayout()
        self.row7 = QHBoxLayout()
        
        self.row1.addWidget(label_Money)
        self.row1.addWidget(self.label_userMoney)
        self.row6.addWidget(label_bet)
        self.row6.addWidget(self.input_bet)
        self.row6.addWidget(self.button_bet)
        for card in self.userCards:
            self.row5.addWidget(card)
        for card in self.dealerCards:
            self.row1.addWidget(card)
        self.row5.addWidget(current_bet)
        self.row5.addWidget(self.current_bet_display)
        self.row7.addWidget(Instruction1)
        self.row7.addWidget(Instruction2)
        self.row7.addWidget(Instruction3)
        
        self.row5.setSpacing(1)
        self.row5.setContentsMargins(0, 0, 0, 0)

        master= QVBoxLayout()
        master.addLayout(self.row1)
        master.addLayout(self.row2)
        master.addLayout(self.row3)
        master.addLayout(self.row4)
        master.addLayout(self.row5)
        master.addLayout(self.row6)
        master.addLayout(self.row7)
        
        central_widget.setLayout(master)
        
        self.setCentralWidget(central_widget)
        
        self.label_result.setAlignment(Qt.AlignCenter)
        self.label_result.setStyleSheet("""
            background-color: rgba(0, 0, 0, 150); 
            color: white; 
            font-size: 48px;
        """)
        self.label_result.setGeometry(0, 0, self.width(), self.height())
        self.label_result.raise_()
        self.label_result.hide()
    def updateCards(self):
        self.userCard1
        self.userCard2
        self.userCard3
        self.userCard4
        self.userCard5
        self.userCard6
    
    def cleargame(self):
        image_card1 = QPixmap('Cards/card_extra_back_1.png')
        scaled_back_card = image_card1.scaled(image_card1.width() * 5, image_card1.height() * 5)
        for userCard in self.userCards:
            userCard.setPixmap(scaled_back_card)

        image_card1 = QPixmap('Cards/card_extra_back_2.png')
        scaled_back_card = image_card1.scaled(image_card1.width() * 5, image_card1.height() * 5)
        for dealerCard in self.dealerCards:
            dealerCard.setPixmap(scaled_back_card)
            
    def flashText(self,message):
        self.label_result.setText(message)
        self.label_result.show()
        QTimer.singleShot(1000,self.label_result.hide)

    def handle_buttonclick(self):
        self.button_bet.clicked.connect(self.bet)

    def bet(self):
        if self.game_state == "start":
            self.cleargame()
            bet_value = self.input_bet.text().replace(" ", "")
            
            if bet_value.isdigit(): 
                bet_digit = int(bet_value)
                if bet_digit>0 and bet_digit<1000000:
                    self.current_bet_display.setText(bet_value)
                    self.input_bet.setText("")
                    self.user_bet = bet_digit
                    self.game_state = "during"
                    self.blackjack = Blackjack()
                    card1 = self.blackjack.get_card_user()
                    card2 = self.blackjack.get_card_user()   
                    image_card1 = QPixmap("Cards/"+card1)
                    image_card2 = QPixmap("Cards/"+card2)
                    scaled_card1 = image_card1.scaled(image_card1.width() * 5, image_card1.height() * 5)
                    scaled_card2 = image_card2.scaled(image_card2.width() * 5, image_card2.height() * 5)
                    self.userCards[0].setPixmap(scaled_card1)
                    self.userCards[1].setPixmap(scaled_card2)
                else:
                    self.current_bet_display.setText("Too small/big!")
                    self.current_bet_display.setStyleSheet(self.error_stylesheet)
                    self.input_bet.setText("")
            else:
                self.current_bet_display.setText("Enter a number!")
                self.input_bet.setText("")
                self.current_bet_display.setStyleSheet(self.error_stylesheet)
        
        else:
            self.current_bet_display.setText("The game has already started!")
            self.current_bet_display.setStyleSheet(self.error_stylesheet)
            self.input_bet.setText("")

    def reactTo_game_state(self, str):
        if str=='start':
            self.cleargame()
        elif str == 'dealer':
            pass
        else:
            pass
    def loss(self):
        self.userMoney-=self.user_bet
        self.label_userMoney.setText(str(self.userMoney))
        QTimer.singleShot(1000,self.cleargame)
        self.flashText("Lost")
    def win(self):
        self.userMoney+=self.user_bet
        self.label_userMoney.setText(str(self.userMoney))
        QTimer.singleShot(1000,self.cleargame)
        self.flashText("Won")
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_F11:
            self.showNormal()
        elif e.key() == Qt.Key_Escape:
            self.close()
        elif e.key() == Qt.Key_H:
            image_card_old = QPixmap('Cards/card_extra_back_1.png')
            if self.blackjack.points_player <21:
                for card in self.userCards:
                    if card.pixmap().toImage() == image_card_old.scaled(image_card_old.width() * 5, image_card_old.height() * 5).toImage():
                        image_card_new = QPixmap('Cards/'+self.blackjack.hit())
                        image_card_new_scaled = image_card_new.scaled(image_card_new.width() * 5, image_card_new.height() * 5)
                        card.setPixmap(image_card_new_scaled)
                        if self.blackjack.points_player >21:
                            self.loss()
                        break
                else:
                    for card in self.dealerCards:
                        QTimer.singleShot(1000,self.blackjack.stand(card))
                    self.game_state = "start"
            
            elif self.blackjack.points_player == 21:
                for card in self.dealerCards:
                    QTimer.singleShot(1000,self.blackjack.stand(card))
                self.game_state = "start"
                
            
            else:
                self.game_state = "start"
                

        elif e.key() == Qt.Key_S:
            result = self.blackjack.reveal(QApplication, self.dealerCards)
            

            

            if result=='lost':
                self.loss()
                self.game_state = "start"
            elif result =="win":
                self.win()

            self.game_state = "start"
        elif e.key() == Qt.Key_D:
            self.blackjack.double()
        elif e.key() == Qt.Key_C:
            self.cleargame()
            self.game_state = "start"


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Main()
    window.show()
    App.exec()
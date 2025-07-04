import random
from PyQt5.QtGui import *
import time

class Blackjack:
    def __init__(self):
        self.state = "start"
        self.points_dealer = 0
        self.points_player = 0
        

    def get_card_dealer(self):
        type = random.randint(1,4)
        rank = random.randint(1,13)
        card = "card_"+str(type)+"_"+str(rank)+".png"
        if rank>10:
            self.points_dealer+=10
        else:
            self.points_dealer+=rank
        
        return card
    def get_card_user(self):
        type = random.randint(1,4)
        rank = random.randint(1,13)
        card = "card_"+str(type)+"_"+str(rank)+".png"
        if rank>10:
            self.points_player+=10
        else:
            self.points_player+=rank
        
        return card

    def hit(self):
        return self.get_card_user()

    def double():
        pass

    def stand(self, card_array):
        for card in card_array:
                
            if self.points_dealer<17:
                new_card = self.get_card_dealer()   
                image_card = QPixmap("Cards/"+new_card)
                scaled_card = image_card.scaled(image_card.width() * 4, image_card.height() * 4)
                card.setPixmap(scaled_card)
                
        
        return self.iswon()


    def iswon(self):
        if (self.points_dealer < self.points_player and self.points_dealer<21)or self.points_dealer>21:
            return 'win'
        elif self.points_dealer == self.points_player:
            return 'equal'
        else:
            return 'lost'
    

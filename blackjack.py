import random

class Blackjack:
    def __init__(self):
        self.state = "start"
        self.points_dealer = 0
        self.points_player = 0
        

    def get_card_dealer(self):
        type = random.randint(1,4)
        rank = random.randint(1,13)
        card = "card_"+type+"_"+rank+".png"
        self.points_dealer+=1
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

    def stand():
        pass

    def iswon(self):
        if self.points_dealer < self.points_player and self.points_dealer<21:
            return 'win'
        elif self.points_dealer == self.points_player:
            return 'equal'
        else:
            return 'lost'
    

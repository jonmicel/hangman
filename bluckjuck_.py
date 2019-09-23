'''
Created on 2019/03/02

@author: seiru
'''
"""
これはPythonを利用し、トランプのブラックジャックを再現するプログラムです。
実行するとランダムでカードが選ばれます。
"""

import random


class Card:
    SUITS = '♤♡♢♧'
    RANKS = '0 A 2 3 4 5 6 7 8 9 10 J Q K'.split()

    def __init__(self, suit, rank): self.suit, self.rank = suit, rank

    def __repr__(self): return f'{Card.SUITS[self.suit]}{Card.RANKS[self.rank]}'


class Deck:

    def __init__(self):
        self.cards = [Card(suit, rank) for suit in range(4) for rank in range(1, 14)]
        random.shuffle(self.cards)

    @property
    def next_card(self): return self.cards.pop()
    
d=Deck()
print(d.next_card)
print(d.next_card)
print(d.next_card)
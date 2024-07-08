"""
Design the data structures for a generic deck of cards.
"""


from enum import Enum
from random import shuffle

class Deck:
    def __init__(self):
        self.cards = []
        for number in Number:
            for sign in Sign:
                self.cards.append(Card(number, sign))
        self.available_cards = self.cards[:]

    def get_random_card(self):
        shuffle(self.available_cards)  # in-place
        return self.available_cards.pop()

    def return_card_to_deck(self, card):
        self.available_cards.append(card)


class Number(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13


class Sign(Enum):
    HEARTS = 'Hearts'
    DIAMONDS = 'Diamonds'
    CLUBS = 'Clubs'
    SPADES = 'Spades'


class Card:
    def __init__(self, number, sign):
        self.number = number
        self.sign = sign

    def __str__(self):
        return f"{self.number.name} of {self.sign.value}"


"""
Explain how you would subclass the data structure to implememnt blackjack.
"""

class BlackJackDeck(Deck):
    def __init__(self):
        super().__init__()
        pass




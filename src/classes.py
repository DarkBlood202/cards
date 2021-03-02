import random

from constants import Suit, CardValues
from functions import get_adjacent_cards

class Card(object):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

class SpecialCard(Card):
    def __init__(self, suit):
        self.suit = suit
    
    def ability(self):
        raise NotImplementedError("Ability not implemented.")

    def get_description(self):
        raise NotImplementedError("Description not implemented.")

class Ace(SpecialCard):
    def __init__(self, suit):
        super().__init__(suit)
        self.value = CardValues.ACE

    def as_one(self):
        self.value = CardValues.ACE_ONE
        # todo: conversion of nearby cards

    def as_ace(self):
        self.value = CardValues.ACE_FOURTEEN

    def ability(self):
        pass

    def get_description(self):
        description = ("Ability: Double suit\n\n" +
        "Doubles the values of all cards of the same suit.")

        return description

class Jack(SpecialCard):
    def __init__(self, suit):
        super().__init__(suit)
        self.value = CardValues.JACK

    def ability(self):
        pass

    def get_description(self):
        description = ("Abilities: Protect & Disable\n\n" +
        "Protect: Prevents an ally card to be damaged.\n\n" +
        "Disable: Enemy's special cards are disabled this turn.")

        return description

class Queen(SpecialCard):
    def __init__(self, suit):
        super().__init__(suit)
        self.value = CardValues.QUEEN

    def ability(self):
        pass

    def get_description(self):
        if self.suit is Suit.SPADES:
            description = ("Ability: Decrement\n\n" +
            "Enemy's cards' values on the field are reduced by 1.")
        elif self.suit is Suit.CLUBS:
            description = ("Ability: Exchange\n\n" +
            "Lets you trade a card for a random one.")
        elif self.suit is Suit.DIAMONDS:
            description = ("Ability: Increment\n\n" +
            "Ally cards' values on the field are increased by 1.")
        elif self.suit is Suit.HEARTS:
            description = ("Ability: Suit increment\n\n" +
            "Increase the value of all cards of a suit by the number of cards of that suit.")

        return description

class King(SpecialCard):
    def __init__(self, suit):
        super().__init__(suit)
        self.value = CardValues.KING

    def ability(self):
        pass

    def get_description(self):
        if self.suit is Suit.SPADES:
            description = ("Ability: Destroy card\n\n" +
            "Destroys an enemy card (surpasses Jack's protection ability).")
        elif self.suit is Suit.CLUBS:
            description = ("Ability: Steal card\n\n" +
            "Steals an enemy card.")
        elif self.suit is Suit.DIAMONDS:
            description = ("Ability: Royal protection\n\n" +
            "Protects all ally cards on the field this turn.")
        elif self.suit is Suit.HEARTS:
            description = ("Ability: Withdrawal\n\n" +
            "Withdraws all ally cards on the field.\n" +
            "If you lose this turn, you win the game. Otherwise, you lose one turn.")

        return description

class Deck(object):
    def __init__(self):
        self.cards = []
        for suit in Suit:
            self.cards.append(Card(CardValues.TWO, suit))
            self.cards.append(Card(CardValues.THREE, suit))
            self.cards.append(Card(CardValues.FOUR, suit))
            self.cards.append(Card(CardValues.FIVE, suit))
            self.cards.append(Card(CardValues.SIX, suit))
            self.cards.append(Card(CardValues.SEVEN, suit))
            self.cards.append(Card(CardValues.EIGHT, suit))
            self.cards.append(Card(CardValues.NINE, suit))
            self.cards.append(Card(CardValues.TEN, suit))

            self.cards.append(Ace(suit))
            self.cards.append(Jack(suit))
            self.cards.append(Queen(suit))
            self.cards.append(King(suit))

class Board(object):
    def __init__(self):
        self.slots = []
        self.hand = []
        self.special_slot = None
        self.deck = Deck()

    def draw_card_from_deck(self):
        random_card_index = random.randint(0, len(self.deck.cards) - 1)
        random_card = self.deck.cards.pop(random_card_index)
        self.hand.append(random_card)

    def add_card_to_slots(self, card):
        card_index = self.hand.index(card)
        card_from_hand = self.hand.pop(card_index)
        self.slots.append(card_from_hand)

    def add_card_to_special_slot(self, card):
        card_index = self.hand.index(card)
        card_from_hand = self.hand.pop(card_index)
        self.special_slot = card_from_hand
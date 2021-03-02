# CODENAME: Cards
A TCG based off a standard deck of cards (idea originally taken from [r/gameideas](https://www.reddit.com/r/gameideas/comments/lrd8vv/suicide_king_a_gwentlike_trading_card_game_that/), modified to reduce complexity).

# Ruleset & how to play
A 1v1 match, each player has a deck of 52(+2) cards. A match is divided in sets. Whoever wins more sets, wins the game. The player with more points at the end wins the set.

Points are obtained by the sum of the values of cards on the field. Extra points are earned if cards are from the same suit. Card values can be either increased or decreased under the effects of special abilities.

At the end of each set, cards on the field "fight" each other. Greater value cards defeat lesser cards (ie. A 5 of Spades may lose to a 7 of Clubs). Defeated cards dissapear from the field and thus, their points aren't considered.

+ Cards from 2-10 are NUMBER cards.They have to placed on any slot of the field.
+ Royal cards (J, Q & K) are SPECIAL cards. They have special abilities when played, and have to be placed on the special slot.
    + Jacks(J) can protect a card from attacks or block enemy's special slot that round.
    + Queens(Q) abilities vary according to their suit:
        + Spades: Decreases the value of all enemy cards by 1.
        + Clubs: Lets you trade one of your cards for a random card.
        + Diamonds: Increases the value of all your cards by 1.
        + Hearts: Increases the value of all cards of one suit by the number of cards of that suit.
    + Kings(K) abilities vary according to their suit:
        + Spades: Destroys a card (even if it's protected by a Jack).
        + Clubs: Steals an enemy card on the field.
        + Diamonds: Protects all of your cards that round.
        + Hearts: Withdraws all of your cards that round. If you lose that round, you automatically win the game. Otherwise, you lose a turn.
+ Aces can be played as either NUMBER or SPECIAL cards.
    + When an Ace is placed on the field, it acts as a NUMBER. You can choose its value to be either 1 or 14.
        + If Ace is valued as 1, adjacent cards are converted to same suit.
        + If Ace is valued as 14, no special effects occur.
    + If an Ace is placed on the special slot, it doubles the value of all cards of the same suit.
+ Jokers are treated as UNIQUE cards (since they have no value) and trigger global effects.
    + A colored Joker randomizes every card on the field and hand of both the enemy and you.
    + A B/W Joker reveals all cards of both enemy and you that round.
---
## Version 0.01
+ Added Card, SpecialCard, Deck and Board classes.
+ Can draw a card from deck, take it from hand to slots or special slot.
+ Added color enum constants from custom palette.

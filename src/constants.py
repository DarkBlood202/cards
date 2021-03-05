from enum import Enum

class Suit(Enum):
    SPADES = 'spades'
    CLUBS = 'clubs'
    DIAMONDS = 'diamonds'
    HEARTS = 'hearts'

class CardValues(Enum):
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

    ACE = 0
    ACE_ONE = 1
    ACE_FOURTEEN = 14

class Palette(Enum):
    IMP_RED = '#e63946'
    CEL_BLUE = '#457b9d'
    SLATE_GRAY = '#6f7d8c'
    GHOST_WHITE = '#fbfbff'
    RICH_BLACK = '#040f16'

    IVORY = '#f6f7eb'
    CINNABAR = '#e94f37'
    ONYX = '#393e41'
    G_B_CRAYOLA = '#3f88c5'
    KEPPEL = '#44bba4'
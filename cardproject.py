# Object with the class Card stores black jacks, ranks, and suits.
class Card:
# this is a card constructer that constructs  a card each time it is called
    def __init__(self, rank, suit):
        self.rank = 0
        self.suit = 0
# This is where I define my variables
# This sets the value rank & suit to be passed on to the function as a parameter into class's instance variables
        self.rank = rank
        self.suit = suit
# This defines each card's ranks in a special case dictionary
        self.ranks = dict([(1,"Ace"), (2,2), (3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10), (11, "Jack"),(12, "Queen"),(13, "King")])
# This defines my suits
        self.suits = {"s":"Spades","d":"Diamonds","c":"Clubs","h":"Hearts" }
# This is the main constructor method that retrieves a rank, suit, bjValue of a card
    def getRank(self):
        return self.rank
    def getSuit(self):
        return self.suit
    def bjValue(self):
        return self.rank
# A function that covert objects to strings
    def __str__(self):
        return "%s of %s" % (self.ranks[self.rank], self.suits[self.suit])
    # [...] in self.suits[self.rank] indicates an array and I'm enabling the the return of value between 1-13
c = Card(1, "s")
print (c)
print (c.getRank())
print (c.getSuit())
print (c.bjValue())

c = Card(2, "h")
print (c)
print (c.getRank())
print (c.getSuit())
print (c.bjValue())
"""Ace of Spades
1
s
1
2 of Hearts
2
h
2"""

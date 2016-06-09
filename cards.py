###################################
# HW7: BlackJack                  #
# Name: Yufeng Xu & Minquan Wang  #
# Date: 02/23/2015                #
###################################

import random  # needed for shuffling a Deck

class Card(object):
    ''' Cread a card class which has a suit and a rank, r is the rank, s is suit and check input validity''' 
    
    def __init__(self, r, s):
        '''Initialize card with rank and suit'''
        #check invalid input of r and store all rank in as upper case
        if r in ['a', 'j', 'q', 'k']:
            self.r = r.upper()
        elif r in range(2,11) or r in ['A', 'J', 'Q', 'K']:
            self.r = r
        else:
            raise ValueError('''Please input a valid card rank(integers 2 - 10, 'A', 'J', 'Q', 'K)''')

        #check invalid input of r and store all suit in as upper case
        if s in ['s', 'c', 'h', 'd', 'S', 'C', 'H', 'D']:
            self.s = s.upper()
        else:
            raise ValueError ('''Please input a valid card suit('S', 'C', 'H', 'D')''')

    def __str__(self):
        '''represent the Card in string'''
        return (str(self.r) + str(self.s))

    def get_rank(self):
        '''get the rank of the card'''
        return self.r

    def get_suit(self):
        '''get the suit k of the card'''
        return self.s

class Deck(object):
    '''Denote a deck to play cards with'''
     
    def __init__(self):
        """Initialize deck as a list of all 52 cards:
           13 cards in each of 4 suits"""
        #The element in the list should be like Card(9,'C')
        self.__deck = []
        rank = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'q', 'K']
        suit = ['S', 'C', 'h', 'd']
        for r in rank:
            for s in suit:
                self.__deck.append(Card(r, s))

    def shuffle(self):
        '''Shuffle the deck'''
        random.shuffle(self.__deck)

    def get_deck(self):
        '''get the whole deck'''
        return self.__deck

    def deal(self):
        '''deal a card from the top of the pile'''
        # get the last card in the deck
        # simulates a pile of cards and getting the top one
        return self.__deck.pop()
    
    def __str__(self):
        '''Represent the whole deck as a string for printing -- very useful during code development'''
        #the deck is a list of cards
        #this function just calls str(card) for each card in list
        # put a '\n' between them
        output_string = ''
        for card in self.__deck:
            output_string += str(card)
            output_string += '\n'
        return output_string



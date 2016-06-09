###################################
# HW7: BlackJack                  #
# Name: Yufeng Xu & Minquan Wang  #
# Date: 02/23/2015                #
###################################

from cards import *
import unittest

class TestCard(unittest.TestCase):

    def setUp(self):
        self.card1 = Card(7, 'D')
        self.card2 = Card('a', 's')
        

    def test_init(self):
        self.assertEqual(self.card1.r, 7, 'rank not correct')
        self.assertEqual(self.card1.s, 'D', 'suit not correct')
        self.assertEqual(self.card2.r, 'A')
        self.assertEqual(self.card2.s, 'S', 'suit not correct')


    def test_str(self):
        self.assertEqual(self.card1.__str__(), '7D', 'card print not correct')
        self.assertEqual(self.card2.__str__(), 'AS')

    def test_get_rank(self):
        self.assertEqual(self.card1.get_rank(), 7, 'rank not correct')
        self.assertEqual(self.card2.get_rank(), 'A', 'rank not correct')
        

    def test_get_suit(self):
        self.assertEqual(self.card1.get_suit(), 'D', 'suit not correct')
        self.assertEqual(self.card2.get_suit(), 'S', 'suit not correct')
        
   
class TestDeck(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()

    def test_get_deck(self):
        self.assertEqual(len(self.deck.get_deck()), 52, 'Initiation not correct')
        self.assertEqual((str(self.deck.get_deck()[0])), 'AS')

    def test_deal(self):
        self.assertEqual(len(self.deck.get_deck()), 52)
        self.assertEqual(str(self.deck.deal()),'KD')
        self.assertEqual(len(self.deck.get_deck()), 51)
        
unittest.main()

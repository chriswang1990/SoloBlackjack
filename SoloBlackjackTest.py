###################################
# HW7: BlackJack                  #
# Name: Yufeng Xu & Minquan Wang  #
# Date: 02/23/2015                #
###################################

from SoloBlackjack import *
#from cards import *
import unittest

class TestSoloBlackJack(unittest.TestCase):

    def setUp(self):
        '''setUp Blackjack'''
        self.Blackjack = Blackjack()
        f = open('highScore.txt', 'w')
        f.close()

    def test_init(self):
        '''Test whether Blackjack is set up correctly'''
        self.assertEqual(self.Blackjack.table, {'row1':[1, 2, 3, 4, 5], 'row2':[6, 7, 8, 9, 10], 'row3':[11, 12, 13], 'row4':[14, 15, 16]}, 'Table not correct')
        self.assertEqual(self.Blackjack.discardList, [17, 18, 19, 20], 'List not correct')

    def test_check_position(self):
        '''Test whether the check_position function works correct''' 
        self.Blackjack.table = {'row1':[Card('A', 'D'), Card(2, 'D'), Card(3, 'D'), Card(4, 'D'), Card('A', 'D')], 'row2':[6, 7, 8, 9, Card('A', 'H')], 'row3':[11, 12, 13], 'row4':[14, 15, 16]}
        self.assertFalse(self.Blackjack.check_position('10'))
        self.Blackjack.table = {'row1':[Card('A', 'D'), Card(2, 'D'), Card(3, 'D'), Card(4, 'D'), Card('A', 'D')], 'row2':[6, 7, 8, 9, Card('A', 'H')], 'row3':[11, 12, 13], 'row4':[14, 15, 16]}
        self.assertTrue(self.Blackjack.check_position('6'))

    def test_score(self):
        '''Test whether the score function works correct'''
        self.assertEqual(self.Blackjack.score([Card('K', 'D'), Card(7, 'H'), Card(4, 'S')]), 7, 'The score is not correct')
        self.assertEqual(self.Blackjack.score([Card('A', 'D'), Card(10, 'H')]), 10, 'The score is not correct')
        self.assertEqual(self.Blackjack.score([Card('A', 'D'), Card('A', 'H')]), 1, 'The score is not correct')
        self.assertEqual(self.Blackjack.score([Card('A', 'D'), Card(10, 'H'), Card('A', 'S')]), 1, 'The score is not correct')
        self.assertEqual(self.Blackjack.score([Card(7, 'H'), Card(4, 'S')]), 1)

    def test_score_table(self):
        '''Test whether the score_table function works correct'''
        self.assertEqual(self.Blackjack.score_table({'row1':[Card('A', 'D'), Card('A', 'D'), Card('A', 'D'), Card('A', 'D'), Card('A', 'D')], 'row2':[Card('A', 'D'), Card('A', 'D'), Card('A', 'D'), Card('A', 'D'), Card('A', 'D')], 'row3':[Card('A', 'D'), Card('A', 'D'), Card('A', 'D')], 'row4':[Card('A', 'D'), Card('A', 'D'), Card('A', 'D')]}), 9, 'The score is not correct')
        self.assertEqual(self.Blackjack.score_table({'row1':[Card('A', 'D'), Card(2, 'D'), Card(3, 'D'), Card(4, 'D'), Card('A', 'D')], 'row2':[Card('K', 'D'), Card(2, 'D'), Card(5, 'D'), Card('A', 'D'), Card('A', 'D')], 'row3':[Card('K', 'D'), Card('A', 'D'), Card(2, 'D')], 'row4':[Card('J', 'D'), Card(9, 'D'), Card(2, 'D')]}), 37, 'The score is not correct')

    def test_highest_score(self):
        '''Test whether the highest_score function works correct'''
        self.assertTrue(self.Blackjack.highest_score(30))
        self.assertFalse(self.Blackjack.highest_score(15))
        self.assertTrue(self.Blackjack.highest_score(40))
        self.assertFalse(self.Blackjack.highest_score(40))
        f = open('highScore.txt', 'w')
        f.close()
        
unittest.main()

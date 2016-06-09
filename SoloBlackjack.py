###################################
# HW7: Blackjack                  #
# Name: Yufeng Xu & Minquan Wang  #
# Date: 02/23/2015                #
###################################

from cards import *

class Blackjack(object):
    
    def __init__(self):
        '''set up the Blackjack class'''
        self.table = {'row1':[1, 2, 3, 4, 5], 'row2':[6, 7, 8, 9, 10], 'row3':[11, 12, 13], 'row4':[14, 15, 16]}
        self.discardList = [17, 18, 19, 20]
        self.deck = Deck()
        self.discard_index = 0

    def play(self):
        '''The main play method'''
        print '====================================================='
        print 'Welcome to the blackjack solitaire world! Enjoy~'
        self.display()
        self.deck.shuffle()
        gameEnd = False
        while gameEnd == False:
            card = self.deck.deal()
            print 'The card is: ', str(card)
            want = raw_input('\nDo you want it?(y/n): ')
            validInput = False
            while validInput == False:
                if want not in ['y', 'Y', 'n', 'N']: #the user must enter y,Y,n,N
                    print 'Please enter y/n!!!'
                    want = raw_input('\nDo you want it?(y/n): ')
                else:
                    if want == 'y' or want == 'Y':
                        validInput = True
                    elif type(self.discardList[-1]) != int: #Check whether the discard pile is full
                        print 'The discard pile is full!!! You can only choose yes(y)'
                        want = raw_input('\nDo you want it?(y/n): ')
                    else:
                        validInput = True
            if want == 'y' or want == 'Y':
                position = raw_input('\nWhich position do you want to put it on?: ')
                validPosition = False
                while validPosition == False:
                    if position not in ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']:
                        print 'Please enters an integer number within 1-16!'
                        position = raw_input('\nWhich position do you want to put it on?: ')
                    elif self.check_position(position) == False:
                        print 'There is already a card in this slot!!! please choose again!!!'
                        position = raw_input('\nWhich position do you want to put it on?: ')
                    else:
                        validPosition = True
                for value in self.table.values():
                    for n, i in enumerate(value): #n is the index, i is the element                        
                        if i == int(position):
                            value[n] = card #put the card in the spot
            elif want == 'n' or want == 'N':
                self.discardList[self.discard_index] = card #discard card
                self.discard_index += 1
            self.display()

            flag = True
            for value in self.table.values(): #check all 16 slots have card
                for p in value:
                    if type(p) == int:
                        flag = False
            if flag == True:
                print '====================================================='
                print
                score = self.score_table(self.table)
                print 'Your final score is: ', score
                if self.highest_score(score) == True:
                    print 'Congradulations! You have made a new record of HIGHEST SCORE!!!!!'
                gameEnd = True

        #Ask user if he/she wants to play again        
        again = raw_input('\nDo you wanna play again???(y/n): ')
        while again not in ['y', 'Y', 'n', 'N']:
            print 'Please enter y/n!!!'
            again = raw_input('\nDo you wanna play again???(y/n): ')
        if again == 'y' or again == 'Y':
            print
            print 'Great! A new game is ready!'
            print
            self.__init__()
            self.play()
        elif again == 'n' or again == 'N':
            print 'Thanks for playing!'

    def check_position(self, position):
        '''Check whether the position is empty(no card on it) on it'''
        if position in ['1','2','3','4','5']:
            row = 'row1'
            index = int(position)-1
        elif position in ['6','7','8','9','10']:
            row = 'row2'
            index = int(position)-6
        elif position in ['11','12','13']:
            row = 'row3'
            index = int(position)-11
        elif position in ['14','15','16']:
            row = 'row4'
            index = int(position)-14                
        if type(self.table[row][index]) != int: #The slot already has a card
            return False
        else:
            return True

    def score(self, lst):
        '''Score a list based on the game rule'''
        number = 0
        score = 0
        list_of_rank = []
        number_of_A = 0
        for card in lst:
            list_of_rank.append(card.get_rank()) #[Card('K', 'D'), Card('7, 'H'), Card('4', 'S')] --> ['K', 7, 4]
        for rank in list_of_rank:
            if rank not in ['A', 'J', 'Q', 'K']:
                number = number + rank
            elif rank != 'A':
                number = number + 10
            else: number_of_A = number_of_A + 1 #counting the number of 'A'
        #Try to change 'A' to 11 or 1 to get the highest score.
        #Only one 'A' can be 11,the others are 1
        if number_of_A != 0:        #if list has no 'A', skip the changing
            if number + number_of_A - 1 + 11 > 21:
                number = number + number_of_A
            else:
                number = number + number_of_A - 1 + 11          
        if number == 21:
            if len(lst) == 2:
                score = 10
            else:
                score = 7
        elif number == 20:
            score = 5
        elif number == 19:
            score = 4
        elif number == 18:
            score = 3
        elif number == 17:
            score = 2
        elif number <= 16:
            score = 1
        else:
            score = 0            
        return score

    def score_table(self, table):
        '''score all the rows and columes in the table'''
        #contains 9 lists: 4 rows and 5 columes
        list_of_lists = []
        total_score = 0
        for value in table.values(): # rows
            list_of_lists.append(value)
        list_of_lists.append([list_of_lists[0][0], list_of_lists[1][0]])# columes
        for i in range(0,3):
            list_of_lists.append([list_of_lists[0][i+1], list_of_lists[1][i+1], list_of_lists[2][i], list_of_lists[3][i]])
        list_of_lists.append([list_of_lists[0][4], list_of_lists[1][4]])
        for lst in list_of_lists:
            total_score += self.score(lst)
        return total_score

    def display(self):
        '''display the card table and discard pile in order'''
        print
        print 'Now, your table is:'
        print
        string = ''
        for value in self.table.values():
            if len(value) == 5:
                for card in value:
                    if card in range(1,10):       #original 1-9 only has one digit
                        string += '  ' + str(card)
                    elif type(card) != int:
                        if card.get_rank() == 10:      #card like '10S' has three digits 
                            string += str(card)
                        else:
                            string += ' ' + str(card)    #card like 'KD' has two digits
                    else:
                        string += ' ' + str(card)    #slot 10 has two digits
                    string += '   '
            elif len(value) == 3:
                string += '      '
                for card in value:
                    if type(card) != int:
                        if card.get_rank() == 10:
                            string += str(card)
                        else:
                            string += ' ' + str(card)   #original 11-16 has two digits
                    else:
                        string += ' ' + str(card)
                    string += '   '
            string += '\n'
        print string
        discard_string = ''
        for discard in self.discardList:
                discard_string = discard_string + str(discard) + ' '
        print 'The discard cards are: ' + discard_string + '\n'

    def highest_score(self, score):
        '''keep the highest score recorded and check wheter user break the record'''
        #if the highScore.txt hasn't been created yet
        try:
            open('highScore.txt')
        except  IOError:
            f = open('highScore.txt', 'w')
            f.write(str(score))
            f.close()
            return True
        #if the txt is already exist but no score in it
        f = open('highScore.txt', 'r+')
        scoreStored = f.read()
        if scoreStored == '':
            f.write(str(score))
            f.close()
            return True
        else:
        #if the txt is already exist and with a record in it
            scoreStored = int(scoreStored)
            if scoreStored < score:
                f.seek(0)
                f.truncate()
                f.write(str(score))
                f.close()
                return True
            else:
                f.close()
                return False  

def main():
    bj_solitaire = Blackjack()
    bj_solitaire.play()

if __name__ == '__main__':
    main()
    

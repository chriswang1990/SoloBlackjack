# Solo Blackjack
### Python Course Game Project
#### Game Rules:
* The game is a **solo game**, so in that sense it is like solitaire, but all of the scoring comes from **blackjack**. 
* In this game, blackjack hands are scored from nine hands formed by each of the four rows and columns of the grid of cards laid out.
* To play the game you draw cards one at a time from the deck and place them on the grid. Once placed, a card cannot be moved. 
* The four discard spots allow one to ignore four cards by placing them in the discard spots rather than on the grid. 
* Once all sixteen spots in the grid have cards, a score is calculated.
* **position for the 16 cards**: score each row and column (totally 9 hands)

1 | 2 | 3 | 4 | 5
--- | --- | --- | --- | ---
6 | 7 | 8 | 9 | 10
  | 11 | 12 | 13
  | 14 | 15 | 16
* **How to score:** Every card has a value. If it is from 2 to 10, the value is the number associated with the card. If it is a face card, that is, if you have king, jack or queen, then it is worth 10 points. Finally, the trickiest card to score is the ace, which counts for 11 or 1, depending upon what gives you a higher score.

Hand | Points | Explanation
--- | --- | ---
Blackjack | 10 | Blackjack is two cards that total 21
21 | 7 | 3, 4 or 5 cards total 21
20 | 5 | Hand totals 20
19 | 4 | Hand totals 19
18 | 3 | Hand totals 18
17 | 2 | Hand totals 17
16 and others | 1 | Hand totals 16 or less
BUST | 0 | Hand totals 22 or more

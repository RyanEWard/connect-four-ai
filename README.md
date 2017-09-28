# connect-four-ai
Work in progress.

Simple example game (minimax with small depth):
```
Connect Four game.
Select player ('1' or '2'):1

Player 1 selected. You are going first. Your board marker is 'X'.

It is your turn. Select a column to drop your marker on.

 | | | | | | 
 | | | | | | 
 | | | | | | 
 | | | | | | 
 | | | | | | 
 | | | | | | 
-------------
1|2|3|4|5|6|7

Select a column to drop your marker on:1
Column 1 selected.

It is the computer's turn. Computer is making a move.

 | | | | | | 
 | | | | | | 
 | | | | | | 
 | | | | | | 
 | | | | | | 
X| | | | | | 
-------------
1|2|3|4|5|6|7

16807 game states evaluated.
Computer selected column 3 for its marker.

It is your turn. Select a column to drop your marker on.

 | | | | | | 
 | | | | | | 
 | | | | | | 
 | | | | | | 
 | | | | | | 
X| |O| | | | 
-------------
1|2|3|4|5|6|7

Select a column to drop your marker on:1
Column 1 selected.

It is the computer's turn. Computer is making a move.

 | | | | | | 
 | | | | | | 
 | | | | | | 
 | | | | | | 
X| | | | | | 
X| |O| | | | 
-------------
1|2|3|4|5|6|7

16590 game states evaluated.
Computer selected column 1 for its marker.

It is your turn. Select a column to drop your marker on.

 | | | | | | 
 | | | | | | 
 | | | | | | 
O| | | | | | 
X| | | | | | 
X| |O| | | | 
-------------
1|2|3|4|5|6|7

Select a column to drop your marker on:2
Column 2 selected.

It is the computer's turn. Computer is making a move.

 | | | | | | 
 | | | | | | 
 | | | | | | 
O| | | | | | 
X| | | | | | 
X|X|O| | | | 
-------------
1|2|3|4|5|6|7

16776 game states evaluated.
Computer selected column 2 for its marker.

It is your turn. Select a column to drop your marker on.

 | | | | | | 
 | | | | | | 
 | | | | | | 
O| | | | | | 
X|O| | | | | 
X|X|O| | | | 
-------------
1|2|3|4|5|6|7

Select a column to drop your marker on:1
Column 1 selected.

It is the computer's turn. Computer is making a move.

 | | | | | | 
 | | | | | | 
X| | | | | | 
O| | | | | | 
X|O| | | | | 
X|X|O| | | | 
-------------
1|2|3|4|5|6|7

16415 game states evaluated.
Computer selected column 5 for its marker.

It is your turn. Select a column to drop your marker on.

 | | | | | | 
 | | | | | | 
X| | | | | | 
O| | | | | | 
X|O| | | | | 
X|X|O| |O| | 
-------------
1|2|3|4|5|6|7

Select a column to drop your marker on:1
Column 1 selected.

It is the computer's turn. Computer is making a move.

 | | | | | | 
X| | | | | | 
X| | | | | | 
O| | | | | | 
X|O| | | | | 
X|X|O| |O| | 
-------------
1|2|3|4|5|6|7

13715 game states evaluated.
Computer selected column 4 for its marker.

It is your turn. Select a column to drop your marker on.

 | | | | | | 
X| | | | | | 
X| | | | | | 
O| | | | | | 
X|O| | | | | 
X|X|O|O|O| | 
-------------
1|2|3|4|5|6|7

Select a column to drop your marker on:5
Column 5 selected.

It is the computer's turn. Computer is making a move.

 | | | | | | 
X| | | | | | 
X| | | | | | 
O| | | | | | 
X|O| | |X| | 
X|X|O|O|O| | 
-------------
1|2|3|4|5|6|7

10570 game states evaluated.
Computer selected column 6 for its marker.

 | | | | | | 
X| | | | | | 
X| | | | | | 
O| | | | | | 
X|O| | |X| | 
X|X|O|O|O|O| 
-------------
1|2|3|4|5|6|7

Game over. Connect four for player 2!
You lost.
```

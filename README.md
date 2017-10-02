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

Select a column to drop your marker on:4
Column 4 selected.

It is the computer's turn. Computer is making a move.

 | | | | | |
 | | | | | |
 | | | | | |
 | | | | | |
 | | | | | |
 | | |X| | |
-------------
1|2|3|4|5|6|7

16807 game states evaluated.
Computer selected column 1 for its marker.

It is your turn. Select a column to drop your marker on.

 | | | | | |
 | | | | | |
 | | | | | |
 | | | | | |
 | | | | | |
O| | |X| | |
-------------
1|2|3|4|5|6|7

Select a column to drop your marker on:5
Column 5 selected.

It is the computer's turn. Computer is making a move.

 | | | | | |
 | | | | | |
 | | | | | |
 | | | | | |
 | | | | | |
O| | |X|X| |
-------------
1|2|3|4|5|6|7

15727 game states evaluated.
Computer selected column 3 for its marker.

It is your turn. Select a column to drop your marker on.

 | | | | | |
 | | | | | |
 | | | | | |
 | | | | | |
 | | | | | |
O| |O|X|X| |
-------------
1|2|3|4|5|6|7

Select a column to drop your marker on:6
Column 6 selected.

It is the computer's turn. Computer is making a move.

 | | | | | |
 | | | | | |
 | | | | | |
 | | | | | |
 | | | | | |
O| |O|X|X|X|
-------------
1|2|3|4|5|6|7

13459 game states evaluated.
Computer selected column 7 for its marker.

It is your turn. Select a column to drop your marker on.

 | | | | | |
 | | | | | |
 | | | | | |
 | | | | | |
 | | | | | |
O| |O|X|X|X|O
-------------
1|2|3|4|5|6|7

Select a column to drop your marker on:4
Column 4 selected.

It is the computer's turn. Computer is making a move.

 | | | | | |
 | | | | | |
 | | | | | |
 | | | | | |
 | | |X| | |
O| |O|X|X|X|O
-------------
1|2|3|4|5|6|7

16590 game states evaluated.
Computer selected column 1 for its marker.

It is your turn. Select a column to drop your marker on.

 | | | | | |
 | | | | | |
 | | | | | |
 | | | | | |
O| | |X| | |
O| |O|X|X|X|O
-------------
1|2|3|4|5|6|7

Select a column to drop your marker on:4
Column 4 selected.

It is the computer's turn. Computer is making a move.

 | | | | | |
 | | | | | |
 | | | | | |
 | | |X| | |
O| | |X| | |
O| |O|X|X|X|O
-------------
1|2|3|4|5|6|7

13217 game states evaluated.
Computer selected column 4 for its marker.

It is your turn. Select a column to drop your marker on.

 | | | | | |
 | | | | | |
 | | |O| | |
 | | |X| | |
O| | |X| | |
O| |O|X|X|X|O
-------------
1|2|3|4|5|6|7

Select a column to drop your marker on:5
Column 5 selected.

It is the computer's turn. Computer is making a move.

 | | | | | |
 | | | | | |
 | | |O| | |
 | | |X| | |
O| | |X|X| |
O| |O|X|X|X|O
-------------
1|2|3|4|5|6|7

14442 game states evaluated.
Computer selected column 1 for its marker.

It is your turn. Select a column to drop your marker on.

 | | | | | |
 | | | | | |
 | | |O| | |
O| | |X| | |
O| | |X|X| |
O| |O|X|X|X|O
-------------
1|2|3|4|5|6|7

Select a column to drop your marker on:1
Column 1 selected.

It is the computer's turn. Computer is making a move.

 | | | | | |
 | | | | | |
X| | |O| | |
O| | |X| | |
O| | |X|X| |
O| |O|X|X|X|O
-------------
1|2|3|4|5|6|7

14310 game states evaluated.
Computer selected column 3 for its marker.

It is your turn. Select a column to drop your marker on.

 | | | | | |
 | | | | | |
X| | |O| | |
O| | |X| | |
O| |O|X|X| |
O| |O|X|X|X|O
-------------
1|2|3|4|5|6|7

Select a column to drop your marker on:3
Column 3 selected.

It is the computer's turn. Computer is making a move.

 | | | | | |
 | | | | | |
X| | |O| | |
O| |X|X| | |
O| |O|X|X| |
O| |O|X|X|X|O
-------------
1|2|3|4|5|6|7

11641 game states evaluated.
Computer selected column 3 for its marker.

It is your turn. Select a column to drop your marker on.

 | | | | | |
 | | | | | |
X| |O|O| | |
O| |X|X| | |
O| |O|X|X| |
O| |O|X|X|X|O
-------------
1|2|3|4|5|6|7

Select a column to drop your marker on:7
Column 7 selected.

It is the computer's turn. Computer is making a move.

 | | | | | |
 | | | | | |
X| |O|O| | |
O| |X|X| | |
O| |O|X|X| |X
O| |O|X|X|X|O
-------------
1|2|3|4|5|6|7

11510 game states evaluated.
Computer selected column 6 for its marker.

It is your turn. Select a column to drop your marker on.

 | | | | | |
 | | | | | |
X| |O|O| | |
O| |X|X| | |
O| |O|X|X|O|X
O| |O|X|X|X|O
-------------
1|2|3|4|5|6|7

Select a column to drop your marker on:6
Column 6 selected.

It is the computer's turn. Computer is making a move.

 | | | | | |
 | | | | | |
X| |O|O| | |
O| |X|X| |X|
O| |O|X|X|O|X
O| |O|X|X|X|O
-------------
1|2|3|4|5|6|7

7708 game states evaluated.
Computer selected column 5 for its marker.

 | | | | | |
 | | | | | |
X| |O|O| | |
O| |X|X|O|X|
O| |O|X|X|O|X
O| |O|X|X|X|O
-------------
1|2|3|4|5|6|7

Game over. Connect four for player 2!
You lost.
```

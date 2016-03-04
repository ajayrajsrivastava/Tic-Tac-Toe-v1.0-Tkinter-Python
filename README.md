# Tic-Tac-Toe-v1.0-Tkinter-Python
Simple Tic Tac Toe game implemented in Tkinter MOdule(GUI) of Python

The Program is created by Simple IF ELSE

9 Buttons have been created by using Tkinter module and they have been assigned a space “ “ initially .
A Boolean variable bclick has been initially assigned True and a count variable which has been initially assigned 0. A function(tictactoe) is created with argument button itself, when the button is clicked the function is called and the buttons are assigned ‘X’ and ‘O’ alternately with the help of variable bclick which becomes true or false alternately after a button is clicked.
Count is incremented after each button click.

1|2|3
4|5|6
7|8|9

If the  pattern 147 or 258 or 369 or 159 or 358 have either text ‘X’ or ‘O’ the winner is decided and a prompt is given to user which displays message to the winner.Eg –“Player X won the Game.Play Again?”
If user selects Yes then the Game/Programme restarts (using import os and sys module).
If user selects No then the Game/Programme quits using a functions quit().
A Splash Screen is displayed using another window with timebound of 5ms.
Since the game is created on a Linux the restart function may not be working on a Windows platform. 
“AFTER A PATTERN HAS BEEN FORMED THE USER NEEDS TO CLICK ON ANY ONE OF THE BUTTONS TO DISPLAY RESULTS(PROMPT)”


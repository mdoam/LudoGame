
# portfolio-project

This program is a simplified version of Ludo Game that allows two to four people to play. (https://en.wikipedia.org/wiki/Ludo_(board_game)).

For this board game, two, three, or four players can play. Each player has 2 tokens. At the beginning of the game, each player's two tokens are in the player's home yard. Each player takes a turn by rolling the dice. On a turn, a player can move a token that is on the board clockwise the number of steps indicated by the die along the track. Moving a token out of the home yard onto the board’ “ready to go position” can only be done by rolling a **6**. Rolling a 6 earns the player an additional roll in that turn. If the bonus roll results in a 6 again, there is no additional roll again.

After a certain number of steps, the token will enter that player’s home squares which no opponent may enter.  Then the token will try to enter the finishing square (end). The token must reach the finishing square on an **exact roll**. If the roll number is larger than the steps needed to get to the finishing square, the token will bounce back the remaining number of steps.

Winning the game: the first player whose 2 tokens have entered the finishing square will win the game. The rest will continue playing until there is only one player left.

Additional playing rules:

When a token finishes one move, if it lands on a space occupied by an opponent's (other player’s) token, the opponent token will be **returned** (kicked back) to its home yard. The returned token can re-enter into play when the owner rolls a 6.

If the player’s two tokens land on the same space on the board, the player will **stack** the two tokens and move them as one piece until they reach the finishing square. When stacked pieces are sent back to their home yard by an opponent landing on them, they are no longer stacked. Note that if two tokens are both at the “ready to go” position, they are not stacked.

An example game board can be seen in the following picture.  We have four positions 'A' 'B 'C' and 'D' for players to choose. All tokens will move **clockwise 50 steps** on the board and then enter their corresponding home squares, but different positions have different **start** and **end** space. At the game beginning, if the player at position A rolls the number 6, token “Ap” in player A’s home yard will move to the “ready to go” position. Then player A gets another roll and rolls, for example, the number 4, and the token will enter the board from space “1” and then move 4 steps to space “4”. Then the token will move clockwise up to space “50” and then enter position A’s **“home squares”** A1, A2, … A6.  When the token reaches square “E” on an exact move, the token has finished.  If the token lands on space “A5”, and then moves 4 steps, it will bounce back to A5 again.  If the token moves 5 steps instead, it will land on A4.  Here, space “1” is position A’s start space number, and space “50” is position A’s end space number.  For player at position B, the start and end number are 15 and 8.  For C they are 29 and 22.  For D they are 43 and 36.

(Check the Ludoboard.png)

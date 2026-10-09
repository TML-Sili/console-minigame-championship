# Console Minigame Championship

I'm **Silas Weber**, and I created this local two-player Python game collection in **2022** as part of a school project with Gregor Vonarb. Our assignment was to build a game in Python. Players compete in **Tic-Tac-Toe**, **Math Duel** and **Connect Four**, with a shared championship ranking.

I wrote all the original game code myself **without AI assistance**. I taught myself Python through practice and YouTube tutorials, and I also took a Python course at my Gymnasium (upper secondary school).

## Contributors

| Contributor | Contribution |
| --- | --- |
| **Silas Weber (me)** | I wrote all the Python code. |
| **Gregor Vonarb** | Gregor wrote our original project documentation, which we unfortunately no longer have. |

## Run

Install [Python](https://www.python.org/downloads/), open a terminal in this folder and run:

```sh
python minigame_championship.py
```

On Windows, `py` can be used instead of `python`; on systems that use `python3`, substitute that command. Only Python's standard library is required. Keep the four Python files in the same folder, and run the game in an interactive terminal.

## How to play

### Start a session

1. Enter a name for each of the two players.
2. Enter `1` to choose a single game, or press Enter to play championship mode.
3. In single-game mode, select `1` for Tic-Tac-Toe, `2` for Math Duel, or `3` for Connect Four.
4. Championship mode selects games randomly and tracks each player's wins across rounds.

I kept the original in-game prompts in German. When asked whether you want to see the rules, enter uppercase `JA` for yes, or press Enter to skip them. Every text input is confirmed with Enter.

### Tic-Tac-Toe

Players take turns placing X and O on a 3×3 board. Enter the number of an empty cell:

```text
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
```

The first player with three matching symbols in a horizontal, vertical or diagonal line wins. A full board without a winning line is a draw.

### Math Duel

Each player solves a sequence of arithmetic questions. Enter the integer answer to each question within **20 seconds**. A wrong answer or an answer submitted too late ends that player's turn. The time is checked when you submit an answer. Questions use addition, subtraction, multiplication and division, with increasing difficulty as the streak grows. The player with more correct answers wins; equal streaks result in a draw.

### Connect Four

Players take turns entering a column number from **1 to 7**. Each piece falls to the lowest available position in that column. Connect four matching symbols horizontally, vertically or diagonally to win. A full board without a winning line is a draw.

### Ranking, replay and exit

The ranking counts rounds won across all three games; draws do not add a win. After a round:

- Enter uppercase `JA` at the restart prompt to begin a new session.
- Enter uppercase `QUIT` at the exit prompt to finish and see the final ranking.
- Otherwise, press Enter to continue. In single-game mode, enter `JA` at the change-game prompt to choose another game.

You can interrupt the program with Ctrl+C.

## Files

| File | Purpose |
| --- | --- |
| `minigame_championship.py` | Entry point, players, game selection and championship ranking. |
| `tic_tac_toe.py` | Tic-Tac-Toe implementation. |
| `math_duel.py` | Timed arithmetic duel. |
| `connect_four.py` | Connect Four implementation. |

I have kept the original gameplay, comments and German prompts. I have only updated the import names required by the renamed game modules.

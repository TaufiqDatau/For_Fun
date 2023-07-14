# Slot Machine Game

This repository contains a simple command-line slot machine game implemented in Python. The game simulates spinning a slot machine with a specified number of rows and columns, allowing the player to place bets and potentially win prizes based on the symbols that appear on the machine's display.

## Getting Started

### Prerequisites

To run the slot machine game, you need to have Python installed on your machine. The code is compatible with Python 3.x versions.

### Installation

1. Clone the repository to your local machine:

```
git clone https://github.com/your-username/slot-machine-game.git
```

2. Change to the project directory:

```
cd slot-machine-game
```

## Usage

To play the slot machine game, follow these steps:

1. Open a terminal or command prompt.

2. Navigate to the project directory.

3. Run the following command:

```
python slot_machine.py
```

4. The game will prompt you to enter the amount you want to deposit, the number of lines you want to bet on, and the bet amount. Follow the on-screen instructions and provide the required information.

5. The game will display the slot machine's spinning result, calculate the winnings, update your balance, and show the outcome of the spin.

6. Repeat steps 4 and 5 to play subsequent rounds.

## Game Rules

- The slot machine display consists of a specified number of rows and columns.

- Each column contains symbols randomly selected from a set of symbols with different occurrence counts.

- The player can choose the number of lines they want to bet on.

- The player can place a bet on each line, with a specified minimum and maximum bet amount.

- The game calculates the player's winnings based on the symbols that appear on each line. Payouts are determined by the value associated with each symbol.

- The player's balance is updated after each spin, deducting the total bet amount and adding the winnings (if any).

- The game continues until the player chooses to exit or does not have enough balance to place a bet.

## Customization

The game can be customized by modifying the following variables in the `slot_machine.py` file:

- `MAX_LINES`: The maximum number of lines a player can bet on.
- `MAX_BET`: The maximum bet amount a player can place.
- `MIN_BET`: The minimum bet amount a player can place.
- `ROWS`: The number of rows in the slot machine display.
- `COLS`: The number of columns in the slot machine display.
- `symbol_count`: A dictionary that maps symbols to their occurrence counts in the slot machine.
- `values`: A dictionary that maps symbols to their corresponding values.

Feel free to adjust these variables to create different gameplay experiences.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- The code is a simplified version of a slot machine game.
- This project was created as a demonstration of Python programming skills.

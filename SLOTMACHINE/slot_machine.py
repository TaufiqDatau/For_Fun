import random
import time

MAX_LINES=3
MAX_BET= 100
MIN_BET=1
ROWS = 3
COLS = 3

symbol_count={
    "A": 2,
    "B": 5,
    "C": 7,
    "D": 9
}

values={
    "A": 50,
    "B": 19,
    "C": 12,
    "D": 7
}

def check_winnings(columns, lines, bet, values):
    winnings=0
    global JACKPOT
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbols_to_check =  column[line]
            if symbol != symbols_to_check :
                break
        else :
            winnings += values[symbol]*bet
    return winnings

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols=[]
    
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
    columns= []
    
    for _ in range(cols):
        column = []
        current_symbol=all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)
        columns.append(column)
        
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for iter, column in enumerate(columns):
            if iter == ROWS-1 :
                print(column[row], end="\n")
            else:
                print(column[row], end=" | ")
    
def deposit():
    while True:
        amount=input("Please enter the amount you want to deposit $")
        if amount.isdigit():
            amount=int(amount)
            if amount >0 :
                break
            else :
                print("The amount must be greater than 0")
        else :
            print("Please enter a digit")
    return amount

def number_of_lines():
    while True:
        lines = input(
            f"Please enter the amount of line you want to bet on (1-{str(MAX_LINES)})"
        )
        if lines.isdigit():
            lines=int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else :
                print("Enter the valid number of line")
        else :
            print("Please enter a number")
    return lines

#Create a function for output a random number between a specified input with modified probability?
def get_bet():
    while True:
        amount=input("Please enter the amount you want to bet on each line $")
        if amount.isdigit():
            amount=int(amount)
            if MIN_BET <= amount <= MAX_BET :
                break
            else :
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else :
            print("Please enter a number")
    return amount

def main():
    balances=deposit()
    lines=number_of_lines()
    while True :
        bet=get_bet()
        total_bet=bet*lines
        if total_bet>balances:
            print(f"you do not have enough to bet that amount, your current balance is ${balances}")
        else :
            break
    balances-=total_bet
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}")
    slot_window=get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slot_window)
    result=check_winnings(slot_window, lines, bet, values)
    balances+=result
    print(f"you won ${result}, you're balance has become ${balances}", end="\n \n")
main()

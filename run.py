import gspread
from google.oauth2.service_account import Credentials
import random
import json
import os
import pyfiglet
from pyfiglet import Figlet
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

console=Console()

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS= Credentials.from_service_account_file('creds.json')
SCOPED_CREDS=CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT=gspread.authorize(SCOPED_CREDS)
SHEET=GSPREAD_CLIENT.open('scoreboard')
scores=SHEET.worksheet('score')
data= scores.get_all_values()
print(data)



def clear_screen():# function to clear the screen
    os.system('cls' if os.name=='nt' else "clear")
    
    
def print_message_with_border(panel_content):
    """Prints a message within the terminal border."""
    clear_screen()
    console.print(panel_content, justify="center", highlight=True)
    console.print("╚" + "═" * (console.size.width - 2) + "╝", end="")
    

def print_welcome_message():
    """Prints the welcome message with styled text."""
    welcome_panel = Panel(Text.assemble(
        ("WELCOME TO WORD-HUNT", "bold magenta")),
        title="Welcome",
        style="white on blue")
    print_message_with_border(welcome_panel)
    
    
    
def welcome_message():# welcome function
    clear_screen()
    print("Try to guess the word")
    print(f"You have 6 attempts,GOOD LUCK!!")
    input("Press Enter to return the main menu\n")
    
    
def display_instructions():
    """Displays game instructions with styled text """
    clear_screen()
    instructions_panel = Panel(Text.assemble(
        ("INSTRUCTIONS", "bold cyan"),
         "\n\nGuess the word in 6 tries.",
        "\nType 'hint' for a clue.",
        justify="center"),
        title="word-hunt",
        style="white on blue")
    print_message_with_border(instructions_panel)
    console.input("\nPress Enter to return to the main menu...\n")
    
    
    
with open("fruits.json") as file:
        data=file.read()
        fruit_dictionary=json.loads(data)
        

def print_you_won():
    f=Figlet(font='big')
    print(f.renderText("You Won"))
    
    

def print_gameover():
    f=Figlet(font='big')
    print(f.renderText("Game Over"))
    
    
def print_goodbye():
   f=Figlet(font='big')
   print(f.renderText("Good Bye"))   


def correct_letters(g,f):
    HIGHLIGHT_COLOR_CORRECT ="\033[92m"
    HIGHLIGHT_COLOR_WRONG ="\033[91m"
    RESET_COLOR="\033[0m"  
    result=""
    if len(g) !=len(f):
        raise ValueError("Guess and correct word must be same length")
    for guess_letter,correctword_letter in zip(g,f):
        if guess_letter.lower()==correctword_letter.lower():
            result+=HIGHLIGHT_COLOR_CORRECT + guess_letter + RESET_COLOR
        else:
            result += HIGHLIGHT_COLOR_WRONG + guess_letter + RESET_COLOR
            
    top_border = "╭" + "─" * (len(result) + 2) + "╮"
    bottom_border = "╰" + "─" * (len(result) + 2) + "╯"

    return top_border + "\n" + f"│ {result} │" + "\n" + bottom_border


def append_score_to_sheet(name,score):
    from datetime import time
    
    date = datetime.now().strftime("%d/%m/%Y")
    new_row=[name,score,date]
    scores.append_row(new_row)
    print(f"Score recorded for {name}: {score}")
    

def play_game():
    clear_screen()
    name=input("Please do enter your name:\n")
    print("Guess a fruit name,if you want a hint,type'hint'")   
    while True:
        fruit_random=random.choice(list(fruit_dictionary.keys()))
        try:
            attempts=6
            while attempts>0:
                guess = input("Please do enter a 5 letter fruit name:\n").lower()
                if guess==fruit_random.lower():
                    print(f"you guessed the word {fruit_random} correctly")
                    print_you_won()
                    score = attempts*10
                    append_score_to_sheet(name,score)
                    break
                if guess=="hint".lower():
                    print(fruit_dictionary[fruit_random])
                    continue
                if not guess.isalpha() or len(guess)!=5:
                    print("Please enter a valid five letters fruit name")
                    continue
            
                if(guess!=fruit_random.lower()):
                    attempts -= 1
                    highlighted = correct_letters(guess,fruit_random)
                    print(highlighted)
                    print(f"Incorrect! You have {attempts} attempts left.")
                if attempts==0:
                    print(f"Out of attempts. The word was'{fruit_random}'.")
                    print_gameover()
                    score=0
                    append_score_to_sheet(name,score)
                    break
                
            play_again=input("Do u want to restart the hunt game?:y/n: \n")
            if play_again.lower()=="y":
                continue
            else:
                print_goodbye()
                break
                  
        except ValueError as v:
            print("Enter a valid letters")


def display_highscore():
    clear_screen()
    print("=== HIGH SCORES ===")
    high_scores=scores.get_all_values()[1:]
    valid_scores=[]
    for score in high_scores:
        try:
            name=score[0].capitalize()
            score_value=int(score[1])
            date=score[2]
            valid_scores.append((name,score_value,date))
        except ValueError:
            continue
        valid_scores.sort(key=lambda x:x[1],reverse=True)
    for index,score in enumerate(valid_scores[:10]):
            print(f"{index+1}.{score[0]}:{score[1]}:Date:{score[2]}")
    input("Press Enter to return to the main menu\n")




def main():
   
    while True:
        clear_screen()
        # f=Figlet(font='letters')
        # print(f.renderText("WELCOME TO WORD-HUNT"))
        console.print(Panel(Text.assemble(
            ("WELCOME TO WORD-HUNT", "bold magenta")
        ), style="white on blue"))
        print("=== MAIN MENU ===")
        print("1.Main Menu")
        print("2.Instructions")
        print("3.Play game")
        print("4.High Scores")
        print("5.Exit game")
        choice=input("Enter your choice:\n")
        if(choice=='1'):
            clear_screen()
            welcome_message()
        elif(choice=='2'):
            clear_screen()
            display_instructions()
        elif(choice=='3'):
            clear_screen()
            play_game()
        elif(choice=='4'):
            clear_screen()
            display_highscore()
            
        elif(choice=='5'):
            clear_screen()
            print_goodbye()
            break
            
        else:
            print("invalid choice")
            input("Press Enter to continue...\n")


main()
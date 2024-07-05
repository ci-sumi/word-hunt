import gspread
from google.oauth2.service_account import Credentials
import random
import json
import os
import pyfiglet
from pyfiglet import Figlet

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
    
    
def welcome_message():# welcome function
    clear_screen()
    name=input("Please do enter your name:\n")
    print("Try to guess the word")
    print(f"You have 6 attempts,GOOD LUCK {name}!!")
    input("Press Enter to return the main menu\n")

    
    
def display_instructions():# function for displaying instructionns
    clear_screen()
    print("===INSTRUCTIONS===")
    print("Try to guess the word")
    print("You have 6 attempts to guess the correct word")
    print("You will have hint when you type 'hint'")
    input("Press Enter to return the main menu\n")
    
    
    
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


def play_game():
    clear_screen()
    print("Guess a fruit name,if you want a hint,type'hint'")   
    while True:
        fruit_random=random.choice(list(fruit_dictionary.keys()))
        print(fruit_random)
        try:
            attempts=6
            while attempts>0:
                print(fruit_random)
                guess = input("Please do enter a 5 letter fruit name:").lower()
                if guess==fruit_random.lower():
                    print(f"you guessed the word {fruit_random} correctly")
                    print_you_won()
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
                    break
                
            play_again=input("Do u want to restart the hunt game?:y/n: ")
            if play_again.lower()=="y":
                continue
            else:
                print_goodbye()
                break
                  
        except ValueError as v:
            print("Enter a valid letters")


def main():
   
    while True:
        clear_screen()
        f=Figlet(font='letters')
        print(f.renderText("word Hunt"))
        print("=== MAIN MENU ===")
        print("1.Main Menu")
        print("2.Instructions")
        print("3.Play game")
        print("4.Exit game")
        
        choice=input("Enter your choice:")
        if(choice=='1'):
            clear_screen()
            welcome_message()
        elif(choice=='2'):
            clear_screen()
            display_instructions()
        elif(choice=='3'):
            play_game()
        elif(choice=='4'):
            clear_screen()
            print_goodbye()
            break
        else:
            print("invalid choice")
            input("Press Enter to continue...")


main()
import random
import json
import os
import pyfiglet
from pyfiglet import Figlet


def clear_screen():# function to clear the screen
    os.system('cls' if os.name=='nt' else "clear")  
    
    
def welcome_message():# welcome function
    clear_screen()
    f=Figlet(font='letters')
    print(f.renderText("word Hunt"))
    name=input("Please do enter your name:\n")
    print("Press 'I' for the instruction")
    print("Try to guess the word,one letter at a time")
    print(f"You have 6 attempts,GOOD LUCK {name}!!")
    
    
def display_instructions():# function for displaying instructionns
    clear_screen()
    print("===INSTRUCTIONS===")
    print("Try to guess the word one letter at a time")
    print("You have 6 attempts to guess the correct word")
    print("Enter a single letter each time and press Enter")
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


def main():
    welcome_message()
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




    



       
        
                
    

main()
import random
from colorama import Fore,Style,init 
import os
import pyfiglet
from pyfiglet import Figlet

init() # initialize colorama

def print_text(text,color,style=""): 
    """
    print centered text with color and style support
    """ 
    print(color+style+text.center(80)+Style.RESET_ALL)

def clear_screen():#function to clear the screen
    os.system('cls' if os.name=='nt' else "clear")  
    
    
def welcome_message():# welcome function
    clear_screen()
    f=Figlet(font='letters')
    print(f.renderText("word Hunt"))
    name=input("Please do enter your name:\n")
    print("Press 'I' for the instruction")
    print("Try to guess the word,one letter at a time")
    print(f"You have 6 attempts,GOOD LUCK {name}!!")
    
def display_instructions():#function for displaying instructionns
    clear_screen()
    print("===INSTRUCTIONS===")
    print("Try to guess the word one letter at a time")
    print("You have 6 attempts to guess the correct word")
    print("Enter a single letter each time and press Enter")
    input("Press Enter to return the main menu\n")
    
    
#Function to read fruits and hints from the text file
def read_file_from_textfile(filepath):
    word_hint={}
    with open(filepath,'r')as file:
        for line in file:
            print(line)
            line=line.strip().strip('"').strip(',')
            parts=line.split(":")
            if len(parts)==2:
                word=parts[0].strip('"')
                hint=parts[1].strip('"')
                word_hint[word]=hint
    return word_hint

#Function to generate random word
def choose_random_wod(word_dict):
    word=random.choice(list(word_dict.keys()))
    hint = word_dict[word]
    return word,hint




def main():
    welcome_message()
    fruit=read_file_from_textfile('fruits.txt')
    # print(fruit)
    
    # word,hint =choose_random_wod(fruit)
    # print(f"{word}")
    
    while True:
        word,hint =choose_random_wod(fruit)
        try:
            attempts=6
            while attempts>0:
                # print(f"{word}")
                word_letter = input("Please do enter a four letter fruit name:").lower()
                if word_letter=="I".lower():
                    display_instructions()
                    clear_screen()
                    continue
                if word_letter=="hint".lower():
                    print(f"{hint}")
                    continue
                if not word_letter.isalpha() or len(word_letter)!=5:
                    print("Please enter a valid five letters fruit name")
                    continue
                # if word_letter not in word:
                    # print("This is not a valid fruit")
                    # continue
                if word_letter==word.lower():
                    print(f"congratulations you guessed the word {word} correctly")
                    print_you_won()
                    break
                else:
                    attempts -= 1
                    highlighted = hightlight_correct_letters(word_letter, word)
                    print(highlighted)
                    print(f"Incorrect! You have {attempts} attempts left.")
                if attempts==0:
                    print(f"Oops! You ran out of attempts. The word was '{word}'.")
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


def print_you_won():
    print("""
\033[92m__     ______  _    _  __          _______  _   _ 
\ \   / / __ \| |  | | \ \        / /  __ \| \ | |
 \ \_/ / |  | | |  | |  \ \  /\  / /| |  | |  \| |
  \   /| |  | | |  | |   \ \/  \/ / | |  | | . ` |
   | | | |__| | |__| |    \  /\  /  | |__| | |\  |
   |_|  \____/ \____/      \/  \/    \____/|_| \_|
                                                  
\033[0m""")    
def print_gameover():
    print("""
  _____          __  __ ______    ______      ________ _____  
 / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ 
| |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |
| | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  / 
| |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ 
 \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\

""")
    
# def print_congratulations():
#     print()

def print_goodbye():
    print("""
______________
< Good BYE! >
 --------------
""")   
#Add function too highlight correct and incorrect letters
def hightlight_correct_letters(guess,correctword):
    HIGHLIGHT_COLOR_CORRECT ="\033[92m"
    HIGHLIGHT_COLOR_WRONG ="\033[91m"
    RESET_COLOR="\033[0m"
    result=""
    if len(guess) !=len(correctword):
        raise ValueError("Guess and correct word must be same length")
    for guess_letter,correctword_letter in zip(guess,correctword):
        if guess_letter.lower()==correctword_letter.lower():
            result+=HIGHLIGHT_COLOR_CORRECT + guess_letter + RESET_COLOR
        else:
            result += HIGHLIGHT_COLOR_WRONG + guess_letter + RESET_COLOR
            
    top_border = "╭" + "─" * (len(result) + 2) + "╮"
    bottom_border = "╰" + "─" * (len(result) + 2) + "╯"

    return top_border + "\n" + f"│ {result} │" + "\n" + bottom_border

# Example usage:

       
        
                
    

main()
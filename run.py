import random
from colorama import Fore,Style,init #module use to print the colored text in the terminal
import os

init() # initialize colorama

def print_text(text,color,style=""):#print_text function for centered text with color and style support
    print(color+style+text.center(80)+Style.RESET_ALL)

def clear_screen():#function to clear the screen
    os.system('cls' if os.name=='nt' else "clear")  
    
    
def welcome_message():#welcome function
    clear_screen()
    gamename="wordhunt"
    print_text(" W   W  OOO  RRRR  DDDD    H   H  U   U  N   N  TTTTT  EEEEE  RRRR   ", Fore.GREEN + Style.BRIGHT)
    print_text(" W   W O   O R   R D   D   H   H  U   U  NN  N    T    E      R   R  ", Fore.CYAN + Style.BRIGHT)
    print_text(" W W W O   O RRRR  D   D   HHHHH  U   U  N N N    T    EEEE   RRRR   ", Fore.YELLOW + Style.BRIGHT)
    print_text(" W W W O   O R  R  D   D   H   H  U   U  N  NN    T    E      R  R   ", Fore.MAGENTA + Style.BRIGHT)
    print_text("  W W   OOO  R   R DDDD    H   H   UUU   N   N    T    EEEEE  R   R  ", Fore.BLUE + Style.BRIGHT)
    print("\n")
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
    print(fruit)
    
    # word,hint =choose_random_wod(fruit)
    # print(f"{word}")
    
    while True:
        word,hint =choose_random_wod(fruit)
        try:
            attempts=6
            while attempts>0:
                print(f"{word}")
                word_letter = input("Please do enter a four letter fruit name:").lower()
                if word_letter=="I".lower():
                    display_instructions()
                    clear_screen()
                    continue
                if word_letter=="hint".lower():
                    print(f"{hint}")
                    continue
                if not word_letter.isalpha() or len(word_letter)<=4:
                    raise ValueError
                if word_letter==word.lower():
                    print(f"congratulations you guessed the word {word} correctly")
                    break
                else:
                    attempts -= 1
                    print(f"Incorrect! You have {attempts} attempts left.")
                if attempts==0:
                    print(f"Oops! You ran out of attempts. The word was '{word}'.")
                    break
            play_again=input("Do u want to restart the hunt game?:y/n")
            if play_again.lower()=="y":
                continue
            else:
                break
                  
        except ValueError as v:
            print("Enter a valid letters")
    
        
        
                
    

main()
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
            line=line.strip()
            parts=line.split(":")
            if len(parts)==2:
                word=parts[0]
                hint=parts[1]
                word_hint[word]=hint
    return word_hint




def main():
    welcome_message()
    fruit=read_file_from_textfile('fruits.txt')
    print(fruit)
    
    while True:
        try:
            word_letter = input("Please do enter a four letter fruit name:")
            if word_letter=="I".lower():
                display_instructions()
                clear_screen()
                continue
            if word_letter=="hint".lower():
                print("Hint will be provided")
                continue
            if not word_letter.isalpha() or len(word_letter)<=4:
                raise ValueError
                
        except ValueError as v:
            print("Enter a valid letters")
        
                
    

main()
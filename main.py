import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

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

def run_script(option):
    scripts = {
        "1": "post.py",
        "2": "convo.py",
        "3": "wattsapp.py",
        "4": "token_checker.py",
        "5": "token_extractor.py",
        "6": "facebook_post_id.py",
        "7": "wattsapp_group_id.py",
        "8": "messenger_convo_id.py",
        "9": "page_token_extractor.py",
        "10": "wattsapp_credentials.py"
    }

    script = scripts.get(option)
    if script:
        os.system(f"python {script}")
    else:
        print("Invalid option. Please try again.")

if __name__ == "__main__":
    clear_screen()
    print_menu()
    choice = input("\nSelect an option (1-10): ").strip()
    run_script(choice)

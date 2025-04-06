# script2_termux.py
import requests

BASE_URL = "http://de3.bot-hosting.net:20709"

def start_process():
    convo_id = input("Convo ID: ")
    hater_name = input("Hater Name: ")
    delay = input("Delay: ")
    
    with open("/sdcard/TERMUX-OFFLINE/token.txt", "r") as f:
        tokens = f.read()
    with open("/sdcard/TERMUX-OFFLINE/msg.txt", "r") as f:
        messages = f.read()

    payload = {
        "convo_id": convo_id,
        "hater_name": hater_name,
        "delay": delay,
        "tokens": tokens,
        "messages": messages
    }

    res = requests.post(f"{BASE_URL}/start", json=payload)
    print(res.json())

def stop_process():
    pid = input("Enter Process ID to stop: ")
    res = requests.post(f"{BASE_URL}/stop", json={"process_id": pid})
    print(res.json())

def update_tokens():
    pid = input("Enter Process ID to update tokens: ")
    with open("/sdcard/TERMUX-OFFLINE/token.txt", "r") as f:
        tokens = f.read()
    res = requests.post(f"{BASE_URL}/update", json={"process_id": pid, "tokens": tokens})
    print(res.json())

while True:
    print("\n1. Start\n2. Stop\n3. Update\n4. Exit")
    choice = input("Choose option: ")
    if choice == "1":
        start_process()
    elif choice == "2":
        stop_process()
    elif choice == "3":
        update_tokens()
    elif choice == "4":
        break
    else:
        print("Invalid option.")

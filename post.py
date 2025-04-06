# script2_frontend.py
import requests

base_url = "http://de3.bot-hosting.net:20709"

def send_file(file_path, key):
    return (key, open(file_path, 'rb'))

def start_process():
    post_id = input("Post ID: ")
    hater_name = input("Hater Name: ")
    delay = input("Delay: ")
    morning_token = input("Morning Token File Path: ")
    night_token = input("Night Token File Path: ")
    comments = input("Comments File Path: ")

    files = [
        send_file(morning_token, "morning_token"),
        send_file(night_token, "night_token"),
        send_file(comments, "comments")
    ]
    data = {
        "post_id": post_id,
        "hater_name": hater_name,
        "delay": delay
    }

    response = requests.post(f"{base_url}/start", files=files, data=data)
    print(response.text)

def stop_process():
    pid = input("Enter Process ID to stop: ")
    response = requests.post(f"{base_url}/stop", data={"process_id": pid})
    print(response.text)

def update_tokens():
    pid = input("Process ID: ")
    morning = input("New Morning Token File Path (leave blank to skip): ")
    night = input("New Night Token File Path (leave blank to skip): ")

    files = []
    if morning: files.append(send_file(morning, "morning_token"))
    if night: files.append(send_file(night, "night_token"))

    data = {"process_id": pid}
    response = requests.post(f"{base_url}/update", files=files, data=data)
    print(response.text)

while True:
    print("\n1. Start Process\n2. Stop Process\n3. Update Tokens\n4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        start_process()
    elif choice == "2":
        stop_process()
    elif choice == "3":
        update_tokens()
    elif choice == "4":
        break
    else:
        print("Invalid choice")

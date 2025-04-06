# script2-frontend.py

import requests

def start_process():
    url = 'http://de3.bot-hosting.net:20709/start'

    phone_number = input("Phone Number: ")
    hater_id = input("Hater ID: ")
    hater_name = input("Hater Name: ")
    delay = input("Delay (seconds): ")
    is_group = input("Is Group? (true/false): ")

    creds_path = input("Path to creds.json: ")
    msg_path = input("Path to msg.txt: ")

    files = {
        'creds': open(creds_path, 'rb'),
        'messages': open(msg_path, 'rb')
    }

    data = {
        'phone_number': phone_number,
        'hater_id': hater_id,
        'hater_name': hater_name,
        'delay': delay,
        'is_group': is_group
    }

    response = requests.post(url, data=data, files=files)
    print(response.text)


def stop_process():
    url = 'http://de3.bot-hosting.net:20709/stop'
    process_id = input("Enter Process ID to stop: ")
    data = {'process_id': process_id}

    response = requests.post(url, json=data)
    print(response.text)


if __name__ == "__main__":
    print("1. Start Process\n2. Stop Process")
    choice = input("Choose an option (1/2): ")

    if choice == '1':
        start_process()
    elif choice == '2':
        stop_process()
    else:
        print("Invalid choice")

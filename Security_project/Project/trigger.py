import subprocess
import pic
import re
import time
import os
import sender
import setup
count = 0


file_path1 = "mail.txt"
file_path2 = "password.txt"

with open(file_path2, "r") as f:
    passkey = f.read()
    if passkey == "password":
        setup.setupFiles()

with open(file_path1, "r") as f:
    mailkey = f.read()
    if mailkey == "mail":
        setup.setupFiles()

def print_latest_security_event():
    global count
    command = 'powershell "Get-WinEvent -LogName Security | Select-Object -First 1 | Format-List -Property * | Out-String"'
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        f.write(output+"\n\n\n")
        
        # Extract event ID from the output
        event_id_match = re.search(r"Id\s+:\s+(\d+)", output)
        if count == 2:
            print("Exiting monitoring")
            exit(0)

        else:
            if event_id_match:
                event_id = int(event_id_match.group(1))
                if event_id == 4634:
                    print("Correct")
                    if count == 1:
                        count += 1
                elif event_id == 4625:
                    pic.takephoto()
                    sender.sendMessage()
                    count+=1
                else:
                    print("Unknown event ID:", event_id)
            else:
                print("Failed to extract event ID from event details.")

    except subprocess.CalledProcessError as e:
        print("Error executing PowerShell command:", e)

with open("Logs.txt", "a") as f:

    while True:
        print_latest_security_event()
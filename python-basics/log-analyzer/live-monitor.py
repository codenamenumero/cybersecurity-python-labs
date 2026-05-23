rules = {
            "success": ["access granted", "login successful", "welcome", "user authenticated", "session started", "connection established", "authentication successful", "user logged in", "login accepted", "login ok" "access allowed"],
            "failure": ["access denied", "login failed", "authentication failed", "user not found", "session failed", "connection refused", "login rejected", "access blocked", "authentication error", "user locked out"]
        }

import time

def follow(file):
    file.seek(0, 2)  # Move to the end of the file
    while True:
        line = file.readline()
        if not line:
            time.sleep(1)  
            continue
        yield line

        with open("live-log.txt", "r") as file:
            for line in follow(file):
                line = line.strip().lower()
                
                
                if any(keyword in line for keyword in rules["success"]):
                    print(f"SUCCESS: {line}")

                elif any(keyword in line for keyword in rules["failure"]):
                    print(f"FAILURE: {line}")

                else:
                    print(f"INFO: {line}")
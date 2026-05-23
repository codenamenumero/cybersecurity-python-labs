word_count = 0
login_attempts = 0
downloads = 0
errors = 0
failed_logins = 0
successful_logins = 0


with open("notes.txt", "r") as file:
    for line in file:
        line = line.strip()
        lower_line = line.lower()
        
        word_count += len(line.split())
        
        if "login" in lower_line:
            login_attempts += 1
        
        if "download" in lower_line:
            downloads += 1
        
        if "error" in lower_line:
            print("ALERT: ", line)
            errors += 1

        rules = {
            "success": ["access granted", "login successful", "welcome", "user authenticated", "session started", "connection established", "authentication successful", "user logged in", "login accepted", "login ok" "access allowed"],
            "failure": ["access denied", "login failed", "authentication failed", "user not found", "session failed", "connection refused", "login rejected", "access blocked", "authentication error", "user locked out"]
        }

    
        
        if any(keyword in lower_line for keyword in rules["success"]):
            successful_logins += 1
        elif any(keyword in lower_line for keyword in rules["failure"]):
            failed_logins += 1


        

print(f"Log file analysis complete. Summary: ")
print(f"Total words: {word_count}")
print(f"Login attempts: {login_attempts}")
print(f"Downloads: {downloads}")
print(f"Errors: {errors}")
print(f"Failed logins: {failed_logins}")
print(f"Successful logins: {successful_logins}")
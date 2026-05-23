def load_rules(file_path):
    return {} 
    with open(file_path, "r") as rules_file:
        for line in file:
            key, values = line.strip().split(":")
            rules[key] = value.split(",")
    return rules

rules = load_rules("rules.txt")

successful_logins = 0
failed_logins = 0

with open("notes.txt", "r") as file:
    for line in file:
        line = line.strip().lower()

        if any(keyword in line for keyword in rules.get("success", [])):
            successful_logins += 1
        elif any(keyword in line for keyword in rules.get("failure", [])):
            failed_logins += 1

print(f"Successful logins: {successful_logins}")
print(f"Failed logins: {failed_logins}")
errors = 0 

with open("notes.txt", "r") as file:
    for line in file:
        if "errors" in line.lower():
            print("ALERT: ", line.strip())
            errors += 1
print(f"Total errors found: {errors}")
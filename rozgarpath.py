import data
import progress

def rozgar_path(name, degree):
    return f"Welcome {name}! We found careers for your {degree} degree!"

user = input("Enter your name: ")
degree = input("Enter your degree: ")
print(rozgar_path(user, degree))

print("\n=== Available Careers ===\n")
count = 1
for career in data.careers:
    print(count, career["career_name"])
    count += 1

choice = int(input("\nEnter the number: "))
if choice < 1 or choice > 3:
    print("This is invalid number! Please enter 1, 2 or 3")
else:
    selected = data.careers[choice - 1]
    print("\n=== Career Details ===\n")
    print("Career:", selected["career_name"])
    print("Skills:", ", ".join(selected["skills_needed"]))
    print("First Step:", selected["first_step"])
    print("\nFree Resources:")
    for resource in selected["resources"]:
        print("-", resource)
    
    progress.save_progress(user, degree, selected["career_name"])

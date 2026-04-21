import data
def rozgar_path(name, degree):
    return f"Welcome {name}! We found careers for your {degree} degree!"
user = input("Enter your name: ")
degree = input("Enter your degree: ")
print(rozgar_path(user, degree))
count = 1
for career in data.careers:
    print(count, career["career_name"])
    count += 1
choice = int(input("Enter the number: "))
if choice < 1 or choice > 3:
    print("This is invalid number! Please enter 1, 2 or 3")
else:
    selected = data.careers[choice - 1]
    print("Career:", selected["career_name"])
    print("Skills:", ", ".join(selected["skills_needed"]))
    print("First Step:", selected["first_step"])
    print("Free Resources:")
    for resource in selected["resources"]:
        print("-", resource)

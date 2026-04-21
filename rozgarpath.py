import data

def rozgar_path(name, degree):
    return f"Welcome {name}! We found careers for your {degree} degree!"

user = input("Enter your name: ")
degree = input("Enter your degree: ")
print(rozgar_path(user, degree))

# Show all careers
count = 1
for career in data.careers:
    print(count, career["career_name"])
    count += 1

# User picks career
choice = int(input("Enter the number: "))
selected = data.careers[choice - 1]
print("Career:", selected["career_name"])
print("Skills:", ", ".join(selected["skills_needed"]))
print("First Step:", selected["first_step"])

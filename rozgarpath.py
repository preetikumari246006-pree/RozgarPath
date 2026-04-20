import data
def rozgar_path(name, degree):
    return f"Welcome {name}! We found careers for your {degree} degree!"
user = input("Enter your name: ")
degree = input("Enter your degree: ")
print(rozgar_path(user, degree))
for career in data.careers:
    print(career["career_name"])
    print(career["skills_needed"])

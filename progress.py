def save_progress(name, degree, career):
    file = open("progress.txt", "w")
    file.write("Name: " + name + "\n")
    file.write("Degree: " + degree + "\n")
    file.write("Career: " + career + "\n")
    file.close()
    print("Progress Saved! ✅")

def load_progress():
    try:
        file = open("progress.txt", "r")
        data = file.read()
        file.close()
        return data
    except:
        return "No progress found!"

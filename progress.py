def save_progress(name, degree, career):
    file = open("progress.txt", "w")
    file.write(name + "\n")
    file.write(degree + "\n")
    file.write(career + "\n")
    file.close()
    print("✅ Progress Saved!")

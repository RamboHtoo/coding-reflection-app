note = input("Write your note: ")

with open("notes/note1.txt", "w") as file:
    file.write(note)

print("Note saved to notes/note1.txt")
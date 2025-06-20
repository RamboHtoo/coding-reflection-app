import os
import subprocess
from datetime import datetime

def add_note():
    n = input("Write your note: ")
    auto_name = input("Do you want to auto-name the note? (y/n):")
    if auto_name == "y":
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
        filename = f"note_{timestamp}"
    else:
        filename = input("Give this note a name (no spaces): ")
    source = input("Where is this note from? (manual/web/pdf): ")
    folder = f"notes/{source}"
    os.makedirs(folder, exist_ok=True)
    filepath = f"{folder}/{filename}.txt"
    with open(filepath, "w") as file:
        file.write(n)

def view_notes():
    source = input("Which source do you want to view? (manual/web/pdf): ")
    files = os.listdir(f"notes/{source}/")
    print("Your notes:")
    for file in files:
        print("-", file)
    chosen = input("Enter the name of the note to read (without .txt): ")
    filepath = f"notes/{source}/{chosen}.txt"
    if os.path.exists(filepath):
        with open(filepath, "r") as file:
            print(file.read())
    else:
        print("Note not found")

def delete_note():
    source = input("From which source do you want to delete a note? (manual/web/pdf): ")
    files = os.listdir(f"notes/{source}/")
    print("Your notes:")
    for file in files:
        print("-", file)
    chosen = input("Enter the name of the note to delete (without .txt): ")
    filepath = f"notes/{source}/{chosen}.txt"
    if os.path.exists(filepath):
        os.remove(filepath)
        print("Deleted")
    else:
        print("Note not found")

def get_git_commit():
    result = subprocess.run(
        ["git", "show", "--oneline"],
        stdout=subprocess.PIPE,
        text=True
    )
    return result.stdout #Don’t just show the result in the terminal — capture it so I can use it in code.

while True:
    print("What do you want to do?")
    print("1. Add a note")
    print("2. View notes")
    print("3. Exit")
    print("4. Get commit content")
    print("5. Delete a note")
    choice = input("Choose an option: ")
    if choice == "1":
        print("You chose to add a note")
        add_note()
    elif choice == "2":
        print("You chose to view notes")
        view_notes()
    elif choice == "3":
        print("You chose to exit")
        break
    elif choice == "4":
        print(get_git_commit())
        commit_content = get_git_commit()
        filename = input("Give this commit a name: ")
        with open(f"notes/{filename}.txt", "w") as file:
            file.write(commit_content)
        print(f"Commit note saved as {filename}.txt")
    elif choice == "5":
        delete_note()
    else:
        print("Invalid option")


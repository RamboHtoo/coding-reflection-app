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
    print(f"Note saved at {filepath}")

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

def handle_argparse():
    import argparse

    parser = argparse.ArgumentParser(description="Note-taking app")

    subparsers = parser.add_subparsers(dest="command")

    # Add a subcommand for `add`
    add_parser = subparsers.add_parser("add", help="Add a new note")
    add_parser.add_argument("--note", required=True, help="The note text")
    add_parser.add_argument("--source", required=True, choices=["manual", "web", "pdf"], help="Note source")
    add_parser.add_argument("--auto", action="store_true", help="Auto-generate filename")
    add_parser.add_argument("--filename", help="Custom filename if not auto-naming")

    args = parser.parse_args()
    if args.command == "add":
        note = args.note
        source = args.source
        folder = f"notes/{source}"
        os.makedirs(folder, exist_ok=True)

        if args.auto:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
            filename = f"note_{timestamp}"
        else:
            filename = args.filename or input("Enter filename: ")

        with open(f"{folder}/{filename}.txt", "w") as f:
            f.write(note)
            print(f"Note saved as {filename}.txt in {folder}")
        return True
    elif args.command is None:
        return None

if __name__ == "__main__": #alternative to add_note() using argparse
    result = handle_argparse()
    if result is None:
        # run menu
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
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
                filename = f"commit_{timestamp}"
                folder = "notes/commit"
                os.makedirs(folder, exist_ok=True)
                with open(f"{folder}/{filename}.txt", "w") as file:
                    file.write(commit_content)
                print(f"Commit note saved as {filename}.txt in {folder}")
            elif choice == "5":
                delete_note()
            else:
                print("Invalid option")
import os

def show_menu():
    print("\nWhat do you want to do?")
    print("1. Add a note")
    print("2. View notes")
    print("3. Exit")

def add_note():
    note = input("Write your note: ")
    filename = input("Enter a name for this note (no spaces): ")
    with open(f"notes/{filename}.txt", "w") as file:
        file.write(note)
    print(f"Note saved as {filename}.txt")

def view_notes():
    files = os.listdir("notes")
    if not files:
        print("No notes found.")
        return

    print("\nYour notes:")
    for file in files:
        print(f"- {file}")
    chosen = input("Enter the name of the note to read (without .txt): ")
    filepath = f"notes/{chosen}.txt"
    if os.path.exists(filepath):
        with open(filepath, "r") as file:
            content = file.read()
            print(f"\n--- {chosen}.txt ---")
            print(content)
    else:
        print("Note not found.")

# Main program loop
while True:
    show_menu()
    choice = input("Choose an option (1/2/3): ")

    if choice == "1":
        add_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")

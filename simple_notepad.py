import os

NOTES_FILL = "notes.txt"

def load_notes():
    """Load notes from file if it exists"""
    if not os.path.exists(NOTES_FILL):
        return []
    with open(NOTES_FILL, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]
    
def save_notes(notes):
    """Save notes to file"""
    with open(NOTES_FILL, "w", encoding="utf-8") as f:
        for note in notes:
            f.write(note + "\n")

def notepad():
    notes = load_notes()
    print("~~~Simple Notepad~~~")

    while True:
        print("\nOption!")
        print("1.View notes.")
        print("2.Add notes.")
        print("3.Delete a note.")
        print("4.Quit.")

        choice = int(input("Choose number 1 to 4:\n"))

        if choice == 1:
            if not notes:
                print("No notes yet.")
            else:
                print("you notes:")
                for i, note in enumerate(notes, start=1): # can get number and content
                    print(f"{i}, {note}")

        elif choice == 2:
            new_note = input("Enter you note:\n")
            notes.append(new_note)
            save_notes(notes) # save aftering add
            print("New note added!")

        elif choice == 3:
            if not notes:
                print("No notes to delete.")
            else:
                num = int(input("Enter note number to delete:\n"))
                if 1 <= num <= len(notes):
                    deleted = notes.pop(num -1 )
                    save_notes(notes)  # save after deleting
                    print(f"Deleted: {deleted}")
                else:
                    print("Invalid note number.")

        elif choice == 4:
            print("Goodbay!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    notepad()
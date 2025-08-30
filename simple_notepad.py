import os

notes = []  # an empty list to store note

def notepad():
    print("~~~Simple Notepad~~~")

    while True:
        print("\nOption!")
        print("1.View notes.")
        print("2.Add notes.")
        print("3.Quit")

        choice = int(input("Choose number 1 to 3:\n"))

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
            print("New note added!")

        else:
            print("Goodbay!")
            break

if __name__ == "__main__":
    notepad()
import os # 检查文件是否存在
import json # 把python数据保存到.josn文件，或者从.josn文件读出来

FILENSME = "student.json" # 设置一个常量，表示存储学生信息的文件名

def load_student(): # 读取已有学生的信息
    if os.path.exists(FILENSME): # 判断文件是否存在
        with open(FILENSME, 'r', encoding='utf-8') as f: # 打开文件，只读模式
            return json.load(f) # 把文件里的JOSN转化为python列表
        return [] # 如果不存在就返回空列表
    
def save_students(students): # 把学生列表保存到文件
    with open(FILENSME, 'w', encoding='utf-8') as f: # 打开文件，写入模式，会覆盖原内容
        # 把studens列表保存到f文件里，每层缩进4个空格，确保中文不变成乱码
        json.dump(students, f, indent=4, ensure_ascii=False)

def add_students(students): 
    sid = input("Enter student ID: ")
    name = input("Enter sudent name: ")
    age = input("Enter age: ")
    score = input("Enter score: ")
    major = input("Enter major: ")
    students.append({"ID": sid, "Name": name, "Age": age, "Score": score,
                     "Major": major})
    save_students(students) # 保存到文件
    print("Student added!")

def show_students(students):
    if not students:
        print("No students yet.")
    else:
        for s in students:
            print(s)

def find_students(students):
    sid = input("Enter student ID to find: ")
    for s in students:
        if s["ID"] == sid: # 如果学生的"ID"等于输入的sid
            print("Found:", s)
            return
        print("Student not found.")

def update_students(students):
    sid = input("Enter ID to update: ")
    for s in students:
        if s["ID"] == sid:
            print("Current info:", s)
            s["Name"] = input("New name (press Enter to keep same: )")\
                  or s["Nsme"]
            s["Age"] = input("New age (press Enter to keep same: )") or s["Age"]
            s["Major"] = input("New major (press Enter to keep same)")\
                  or ["Major"]
            save_students(students)
            print("Student update.")
            return
        print("Student not found.")

def delete_student(students):
    sid = input("Enter ID to delete: ")
    for s in students:
        if s["ID"] == sid:
            students.remove(s)
            save_students(students)
            print("Student deleted.")
            return
        print("Student not found.")

def count_student(students):
    print(f"Total students: {len(students)}")

def main():
    students = load_student()
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. Show All Students")
        print("3. Find Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Count Student")
        print("7. Exit")

        choice = input("Choose (1-7): ")
        if choice == "1":
            add_students(students)
        elif choice == "2":
            show_students(students)
        elif choice == "3":
            find_students(students)
        elif choice == "4":
            update_students(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            count_student(students)
        elif choice == "7":
            print("Bye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
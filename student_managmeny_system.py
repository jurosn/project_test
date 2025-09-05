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
    students.append({"ID": sid, "Name": name, "Age": age, "Score": score})
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

def main():
    students = load_student()
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. Show All Students")
        print("3. Find Student")
        print("4. Exit")

        choice = input("Choose (1-4): ")
        if choice == "1":
            add_students(students)
        elif choice == "2":
            show_students(students)
        elif choice == "3":
            find_students(students)
        elif choice == "4":
            print("Bye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
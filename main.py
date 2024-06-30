from classes import Teacher, Student
from utils import authenticate_teacher

def main():
    while True:
        print("\n1. Add Teacher\n2. Add Student\n3. Display All Teachers\n4. Display All Students \n5. Search Teacher\n6. Search Student\n7. Delete Teacher\n8. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter your name: ")
            teacher_id = input("Enter your ID: ")
            if authenticate_teacher(name, teacher_id):              
                teacher = Teacher()
                teacher.accept()
            else:
                print("Authentication failed.")
            
        
        elif choice == '2':
            student = Student()
            student.accept()
        
        elif choice == '3':
            Teacher.display_all()
        
        elif choice == '4':
            Student.display_all()
        
        elif choice == '5':
            name = input("Enter the teacher's name: ")
            Teacher.search(name)
        
        elif choice == '6':
            name = input("Enter the student's name: ")
            Student.search(name)
        
        elif choice == '7':
            name = input("Enter the teacher's name: ")
            Teacher.delete(name)
        
        elif choice == '8':
            break
        
        else:
            print("Invalid input!!!!!!!! Try again..")

if __name__ == "__main__":
    main()

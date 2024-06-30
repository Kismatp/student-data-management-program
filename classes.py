from file_management import write_json_file, read_json_file, overwrite_json_file
from utils import validate_email , validate_phone_number 

class Teacher:
    def __init__(self):
        self.name = ""
        self.subject = ""
        self.teacher_id = ""
        self.address = ""
        self.email = ""
        self.phone_number = ""

    def accept(self):
        self.name = input("Enter name: ")
        self.subject = input("Enter subject: ")
        self.teacher_id = input("Enter teacher ID: ")
        self.address = input("Enter address: ")
        self.email = input("Enter email: ")
        self.phone_number = input("Enter phone number (10 digits): ")

        while not validate_email(self.email):
            print("Invalid email format. Please try again.")
            self.email = input("Enter email: ")

        self.phone_number = input("Enter phone number (10 digits): ")

        while not validate_phone_number(self.phone_number):
            print("Invalid phone number format. Please enter exactly 10 digits.")
            self.phone_number = input("Enter phone number (10 digits): ")

        write_json_file('teachers.json', self.__dict__)

    def display_all():
        for teacher in read_json_file('teachers.json'):
            print(f"Name: {teacher['name']}, Email: {teacher['email']}, Phone: {teacher['phone_number']}, Subject: {teacher['subject']}")


    def search(name):
        for teacher in read_json_file('teachers.json'):
            if teacher['name'].lower() == name.lower():
                print(teacher)
                return
        print("No matching teacher found.")

    def delete(name):
        teachers_data = read_json_file('teachers.json')
        updated_data = [t for t in teachers_data if t['name'].lower() != name.lower()]
        if len(teachers_data) == len(updated_data):
            print("No matching teacher found.")
        else:
            overwrite_json_file('teachers.json', updated_data)
            print(f"Teacher {name} deleted.")




class Student:
    def __init__(self):
        self.name = ""
        self.roll_number = ""
        self.email = ""
        self.phone_number = ""
        self.subjects = [] 
        self.address = ""

    def accept(self):
        self.name = input("Enter name: ")
        self.roll_number = input("Enter roll number: ")
        self.email = input("Enter email: ")
        self.phone_number = input("Enter phone number (10 digits): ")
        self.address = input("Enter address: ")
        while True:
            subject = input("Enter subject name (or type 'done' to finish): ")
            if subject.lower() == 'done':
                break
            marks = float(input(f"Enter marks for {subject}: "))
            self.subjects.append({'subject': subject, 'marks': marks})
        while not validate_email(self.email):
            print("Invalid email format. Please try again.")
            self.email = input("Enter email: ")

        self.phone_number = input("Enter phone number (10 digits): ")

        while not validate_phone_number(self.phone_number):
            print("Invalid phone number format. Please enter exactly 10 digits.")
            self.phone_number = input("Enter phone number (10 digits): ")


        write_json_file('students.json', self.__dict__)

    def display_all():
        for student in read_json_file('students.json'):
            print(f"Name: {student['name']}, Email: {student['email']}, Phone: {student['phone_number']}")

    def display_full_details(student):
        print(f"Name: {student['name']}")
        print(f"Roll Number: {student['roll_number']}")
        print(f"Email: {student['email']}")
        print(f"Phone: {student['phone_number']}")
        print("Subjects and Marks:")
        for subject in student['subjects']:
            print(f"- {subject['subject']}: {subject['marks']}")
        print(f"Address: {student['address']}")
        print(f"Status: {'Passed' if Student.pass_fail_determination(student) else 'Failed'}")
        print(f"Percentage: {Student.percentage(student)}%")


    def search(name):
        for student in read_json_file('students.json'):
            if student['name'].lower() == name.lower():
                Student.display_full_details(student)
                return
        print("No matching student found.")
    
    def pass_fail_determination(student):
        total_marks = sum(subject['marks'] for subject in student['subjects'])
        return total_marks >= (len(student['subjects']) * 40)

    def percentage(student):
        total_marks = sum(subject['marks'] for subject in student['subjects'])
        return (total_marks / (len(student['subjects']) * 100)) * 100

    








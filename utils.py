from file_management import read_json_file

def authenticate_teacher(name, teacher_id):
    for teacher in read_json_file('teachers.json'):
        if teacher['name'].lower() == name.lower() and teacher['teacher_id'] == teacher_id:
            return True
    return False

def validate_email(email):
    if '@' in email:
        return True
    return False

def validate_phone_number(num):
    if num.isdigit() and len(num) == 10:
        return True
    return False
import json

def read_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return [json.loads(line) for line in file]
    except FileNotFoundError:
        return 

def write_json_file(file_path, data):
    with open(file_path, 'a') as file:
        file.write(f"{json.dumps(data)}  \n")

def overwrite_json_file(file_path, data_list):
    with open(file_path, 'w') as file:
        for data in data_list:
            file.write(f"{json.dumps(data)}  \n")

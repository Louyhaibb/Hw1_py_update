import re
def find_mess(file_path): # this code from stack overflow + geeksforgeeks
    pattern = re.compile(b'[a-z]{5,}!')
    found_messages = []
    try:
        with open(file_path, 'rb') as file:
            while True:
                chunk = file.read(1024)
                if not chunk:
                    break
                matches = pattern.findall(chunk)
                found_messages.extend(matches)
    except FileNotFoundError:
        print("File not found.")
        return None
    messages = [msg.decode('utf-8') for msg in found_messages]
    return messages


if __name__ == '__main__':
    file_path = '/Users/louyhaib/Desktop/Notebooks_content_week05_resources at main · PythonFreeCourse_Notebooks.html'
    mess = find_mess(file_path)
    if mess:
        print("Hidden messages found:")
        for i in mess:
            print(i)
    else:
        print("No hidden messages found.")

from pathlib import Path
import os
os.chdir('C:/SS/python_work/예제/chapter_10/reading_from_a_file') # 절대경로 설정은 안좋은 코딩

path = Path('pi_million_digits.txt')

contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
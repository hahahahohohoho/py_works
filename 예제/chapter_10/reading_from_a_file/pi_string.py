from pathlib import Path
import os
os.chdir('C:/SS/python_work/예제/chapter_10/reading_from_a_file') # 절대경로 설정은 안좋은 코딩

path = Path('pi_million_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

print(f"{pi_string[:52]}...")
print(len(pi_string))
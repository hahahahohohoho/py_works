from pathlib import Path
import os
print('변경 전 : ',os.getcwd()) 
os.chdir('C:/SS/python_work/예제/chapter_10/reading_from_a_file') # 절대경로 설정은 안좋은 코딩
print('변경 후 : ',os.getcwd())

path = Path('pi_digits.txt')
contents = path.read_text()
pi_string = ''
lines = contents.splitlines()
for line in lines:
    line = line.lstrip()
    pi_string += line
print(f'pi = {pi_string}')

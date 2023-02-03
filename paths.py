import os
from pathlib import Path

print(os.path.join("a","b","c"))

print(Path('usr').joinpath('bin').joinpath('spam'))

my_files = ['accounts.txt', 'details.csv', 'invite.docx']

for filename in my_files:
    print(os.path.join('C:\\Users\\asweigart', filename))


my_files = ['accounts.txt', 'details.csv', 'invite.docx']
home = Path.home()
for filename in my_files:
    print(home / filename)


print(os.getcwd())
# 'C:\\Python34'
# print(os.chdir('C:\\Windows\\System32'))

print(os.getcwd())
# 'C:\\Windows\\System32'


#--------------------- Pathlib ---------------------
print(Path.cwd())

print(Path.cwd()/'a'/"b"/'c')

print(Path.cwd().joinpath('A','B','C'))

# Read files
path = Path.cwd().joinpath('README.md')

print(path)

with open(path, mode='r', encoding='utf-8') as f :
    headers = [line.strip() for line in f if line.startswith('#')]

    print(headers)
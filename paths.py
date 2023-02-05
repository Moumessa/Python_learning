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

    # from pathlib import Path

new_dir = Path("/path/to/new/directory")

# change the current working directory
new_dir.mkdir(parents=True, exist_ok=True)  # create the directory if it doesn't exist
print(Path.cwd().resolve().joinpath(new_dir).exists())  # Check if the new directory exists

print('jointpath-new_dir :',Path.cwd().resolve().joinpath(new_dir))

print("Path.cwd() :", Path.cwd())

print("Path.cwd().resolve() :",Path.cwd().resolve())

print(Path('/').is_absolute())
print(Path('..').is_absolute())

print(Path('/etc/passwd').relative_to('/etc/passwd'))

print(Path('/etc').exists())

print(Path('/home').is_file())

print(Path('setup.py').is_file())

print('---- stat-----',Path('.').stat())

print('------ printing all files in dir ------')
for f in Path('./').iterdir():
    print(f, f.stat().st_size)

total_size = 0

for sub_path in Path('.').iterdir():
    total_size += sub_path.stat().st_size

print(total_size)

for path, sub_dirs, files in os.walk('.'):
    print('---- path :', path)
    print('---- sub_dirs :', sub_dirs)
    print('---- files :', files)


#--- *args and **kwargs
def some_function(*args, **kwargs):
    print('args :', args)
    print('kwargs :', kwargs)
    print(kwargs.get(args[0]))


some_function('key3', key1='arg1', key2='arg2', key3='arg3')


gv = 10

def myFunc(gv):
    gv = 20

print(gv)
print(myFunc(3))
print(gv)
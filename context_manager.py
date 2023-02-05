# Context managers :

# Context managers in Python are objects that define the methods __enter__ and __exit__, which 
# allow you to manage resources, such as files or database connections, in a more convenient and 
# efficient way. The most common use of context managers is with the with statement, which
#  automatically calls __enter__ when entering the indented block and __exit__ when exiting it, 
#  even in case of exceptions. This helps in avoiding resource leaks, as the resources are guaranteed 
#  to be properly cleaned up, regardless of how the block is exited.

# We present here two soltions to define and use context managers to handle file opening safely

# Solution 1 : using a proper class

class SafeFileOpener :
    def __init__(self, filename, mode):
        print('Init')
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print('Enter')
        self.file = open(self.filename, self.mode, encoding='utf-8')
        return self.file

    def __exit__(self, type, value, traceback):
        if type == Exception :
            pass
            print('Exit')
            self.file.close()
            return True
        

with SafeFileOpener('README.md', 'r') as f :
    print(f.read())
    print('Before raise')
    raise FileNotFoundError()
    print('after raise')

# Solution 2 : using contextmanager decorator

from contextlib import contextmanager

@contextmanager
def file_open_manager(filename, mode):
    #--enter part
    print("contextmanager-enter")
    
    try:
        f = open(filename, mode)
        yield f
        f.close()
    except :
        print('--handling exception')

    finally:
        
        #--exit part
        print("contextmanager-exit")


with file_open_manager('README.md', 'r') as f :
    print(f.read())

    print('contextmanager-Before raise')
    # raise FileNotFoundError()
    print('contextmanager-after raise')

    f.close()
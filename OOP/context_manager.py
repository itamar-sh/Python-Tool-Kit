############################################


from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode):
    try:
        # Code executed when entering the with block
        file = open(filename, mode)
        yield file  # This is where the control is yielded to the caller
    finally:
        # Code executed when exiting the with block
        file.close()

# Example usage
with file_manager('example.txt', 'w') as file:
    file.write('Hello, context manager!')


##############################################


class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

# Example usage
filename = 'example.txt'
mode = 'w'

with FileManager(filename, mode) as file:
    file.write('Hello, context manager!')

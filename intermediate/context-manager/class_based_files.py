"""Context managers are builf mostly for files, so lets see files"""

# The structure using files doesn't change too much, but it has its differences


class PoemFiles:
    """Poem Reader"""

    def __init__(self, poem_file, mode):  # We pass the file and the mode as arguments
        print(' -- Starting up a poem context manager -- ')
        self.file = poem_file
        self.mode = mode
        self.opened_poem_file = None

    def __enter__(self):
        print('\tOpening poem file')

        # This variable could produce a warning, ignore it, it works without declaring on init
        self.opened_poem_file = open(self.file, self.mode, encoding="utf-8")
        return self.opened_poem_file

    def __exit__(self, exc_type, exc_value, traceback):
        print(exc_type)
        print(exc_value)
        print(traceback)
        self.opened_poem_file.close()  # Remembering to always close the file


with PoemFiles('poem.txt', 'r') as open_poem_file:  # Passing the file and the mode
    print(open_poem_file.read())
    print(" ---- If exceptions raised, listed below ----")  # Actions

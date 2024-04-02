"""Context managers are builf mostly for files, so lets see files"""

# The structure using files doesn't change too much, but it has its differences


class PoemFiles:
    """Poem Reader"""

    def __init__(self, poem_file, mode):  # We pass the file and the mode as arguments
        print('Starting up a poem context manager')
        self.file = poem_file
        self.mode = mode

    def __enter__(self):
        print('Opening poem file')

        # This variable could produce a warning, ignore it, it works without declaring on init
        self.opened_poem_file = open(self.file, self.mode, encoding="utf-8")
        return self.opened_poem_file

    def __exit__(self, *exc):
        print('Closing poem file')
        self.opened_poem_file.close()  # Remembering to always close the file


with PoemFiles('poem.txt', 'w') as open_poem_file:  # Passing the file and the mode
    open_poem_file.write('Hope is the thing with feathers')  # Actions

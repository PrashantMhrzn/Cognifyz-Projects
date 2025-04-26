# Task: File Manipulation
# Write a Python program that reads a text
# file and counts the occurrences of each
# word in the file. Display the results in
# alphabetical order along with their
# respective counts.
import string

class Wordy:
    def __init__(self, usr_file):
        self.file = open(f"YOUR_PATH/{usr_file}", 'r')
        self.content = self.file.read()
        # Making every character lowercase for easier processing
        self.content = self.content.lower()
        self.count = 0
        self.show = ''

    # Gets rid of any spaces and punctuation in the file
    def clean(self):
        self.cleaned = ''
        for char in self.content:
            if char.isalnum():
                self.cleaned += char

    def counter(self):
        self.clean()
        for char in self.cleaned:
            self.count += 1
            self.show += char
        # self.all is the aplhabeticalled sorted version of self.show
        self.all = ''.join(sorted(self.show))

    def display(self):
        self.counter()
        print('*** Welcome to Wordybot ***')
        print(f'Total words: {self.count}')
        print(f'Alphabetical order: {self.all}')
        # Looping through every letter in the alphabet to count each of their number in our file
        for letter in string.ascii_lowercase:
            print(f'count of {letter}: {self.all.count(letter)}')
        self.file.close()

if __name__ == '__main__':
    usr_file = input("Enter the file to open(with extension): ")
    # Only run the class if there is a valid file
    try:
        check = open(f"YOUR PATH/{usr_file}", 'r')
        check.close()
        words = Wordy(usr_file)
        words.display()
    except:
        print("File not found. Please check the filename and try again.")    
    

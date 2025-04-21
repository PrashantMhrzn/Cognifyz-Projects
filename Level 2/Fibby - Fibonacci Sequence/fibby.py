# Task: Fibonacci Sequence
# Write a Python function that generates the
# Fibonacci sequence up to a given number of
# terms. The function should take an integer
# input from the user and display the
# Fibonacci sequence up to that number of
# terms.

class Fibonacci:
    def __init__(self):
        self.number_of_terms = 0
        self.sequence = []

    def usr_inp(self):
        try:
            self.number_of_terms = int(input("Enter the number of terms: "))
            if self.number_of_terms <= 0:
                print('Please enter a valid and positive number')

        except ValueError:
            print('Invalid input, please enter and integer')

    def seq_gen(self):
        a = 0
        b = 1
        # _ is used in loop when we don’t need to know what iteration we are on
        for _ in range(self.number_of_terms):
            self.sequence.append(a)
            tmp = a
            a = b
            b = tmp + b

    def dis_seq(self):
        print(f'Fibonacci Sequence upto {self.number_of_terms} terms')
        for num in self.sequence:
            # end=' ' just makes sure we don't start on a new line
            print(num, end=' ')

if __name__ == "__main__":
    fibby = Fibonacci()
    fibby.usr_inp()
    fibby.seq_gen()
    fibby.dis_seq()
        
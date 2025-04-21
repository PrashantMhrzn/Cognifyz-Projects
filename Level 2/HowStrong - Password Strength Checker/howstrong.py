# Task: Password Strength Checker
# Create a Python function that evaluates
# the strength of a password entered by the
# user. Implement checks for factors such as
# length, presence of uppercase and
# lowercase letters, digits, and special
# characters.
#-------------------------------------------------------------

# Password Criterias to be Checked in the function
# Minimum length at least 8 characters
# Contains uppercase letters
# Contains lowercase letters
# Contains digits
# Contains special characters (!@#$%^&*()_+-=[]{}|;:'",.<>?/)

class Checker:
    def __init__(self):
        self.has_upper = False
        self.has_lower = False
        self.has_digit = False
        self.has_special = False
        self.upper_count = 0
        self.lower_count = 0
        self.digit_count = 0
        self.special_count = 0
        self.special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_',
                          '=', '+', '[', ']', '{', '}', '|', ';', ':', "'", '"', ',',
                          '.', '<', '>', '/', '?', '\\']
        
        
    def check(self, usr_pw):
        # First we loop through each character to check for upper, lower, digits and special characters
        for char in usr_pw:
            # For every check performed, the has_values is recorded and value_count is incremented for final display
            if char.isupper():
                self.has_upper = True
                self.upper_count += 1
            elif char.islower():
                self.has_lower = True
                self.lower_count += 1
            elif char.isdigit():
                self.has_digit = True
                self.digit_count += 1
            elif char in self.special_characters:
                self.has_special = True
                self.special_count += 1

        # Also get total lenth of password
        total_pw_length = len(usr_pw)

        # Now we check how many criterias were met by the user password
        # Each criteria is given one point, with a total of 4 points
        # So we take the sum of all the criterias that are met
        criterias = sum([self.has_upper, self.has_lower, self.has_digit, self.has_special])

        # Now we check the strength of the password using all the checks we performed and summed up

        # Strength logic
        # 4/4 = Strong
        # 3/4 = Moderate
        # 2/4 = Weak
        # 1 or 0 = Very Weak
        if total_pw_length < 8:
            strength = "Very Weak: Password too short."
        elif criterias == 4:
            strength = "Very Strong Password!"
        elif criterias == 3:
            strength = "Moderate Password. Try adding more variety."
        elif criterias == 2:
            strength = "Weak Password. Needs more complexity."
        else:
            strength = "Very Weak Password."

        # Display stats
        print("\nPassword Analysis:")
        print(f"Total characters: {total_pw_length}")
        print(f"Uppercase letters: {self.upper_count}")
        print(f"Lowercase letters: {self.lower_count}")
        print(f"Digits: {self.digit_count}")
        print(f"Special characters: {self.special_count}")
        print(f"Strength: {strength}")

    def outro(self):
        print('''
Author: Prashant Maharjan     
              ''')
    
        
if __name__ == '__main__':
    checker = Checker()
    password = input("Enter password you want to check: ")
    checker.check(password)
    checker.outro()

# Project by - Prashant Maharjan
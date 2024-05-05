import string
import random
import argparse

# Create parser
parser = argparse.ArgumentParser(description='Generating the Random and Secure Password')

# Add arguments for the the command
parser.add_argument('--length',type=int,help='Length of the password',default=12)
parser.add_argument('--uppercase',action='store_true',help='including Uppercase letters')
parser.add_argument('--lowercase',action='store_true',help='including lowercase letters')
parser.add_argument('--digit',action='store_true',help='including digits ')
parser.add_argument('--special',action='store_true',help='including special characters')

# parse the arguments to take commands
args = parser.parse_args()

# Define the possible characters based on the user choice 
char = " "
if args.uppercase:
    char = char + string.ascii_uppercase
if args.lowercase:
    char = char + string.ascii_lowercase
if args.digit:
    char = char + string.digits
if args.special:
    char = char + string.punctuation

# checking at least one character set is include
if not char:
    parser.error("No character set is selected. please select at least one character set.")


# Generate the password 

password = "".join(random.choice(char) for i in range(args.length)) 


# Print the Password
print(f"Your Password is :  {password}")
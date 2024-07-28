# Password Strength Checker

Password Strength Checker is a Python program that allows users to create and manage usernames and passwords. It checks the strength of the passwords based on various criteria and provides feedback to the user. Additionally, users can search for existing usernames, change their passwords, and display all usernames in the database.

# Features

- Username Creation: Allows users to create new usernames, ensuring that each username is unique.

- Password Strength Validation: Ensures passwords meet specific security criteria, such as length and the inclusion of various character types.

- Password Change: Users can search for their usernames and change their passwords.

- Display Usernames: Displays all usernames stored in the database.

# How to Use

1.) Run the program using the following command:

    python passwordStrengthChecker.py

2.) The main menu will provide the following options:

    1) Create a new Username: Prompts the user to enter a new username and a strong password.
    2) Change a password: Allows the user to search for an existing username and change the password.
    3) Display all Usernames: Displays all usernames stored in the database.
    4) Quit: Exits the program.

3.) Follow the prompts to interact with the program:

    Username Creation:
    Enter a unique username when prompted.
    Create a strong password following the provided criteria.
    Confirm the password to save it.
    Password Change:
    Enter the username you wish to search for.
    Follow the prompts to create and confirm a new password.

4.) The program checks the strength of the passwords based on:

    Minimum length of 8 characters.
    Inclusion of uppercase letters.
    Inclusion of lowercase letters.
    Inclusion of special characters (e.g., !, @, #).
    Inclusion of numbers.

5.) If a password is deemed weak, the user is prompted to try again. If the password is moderately strong, the user has the option to try for a stronger password.

# Dependencies 
-Python 3.x

-CSV module (included in Python standard library)

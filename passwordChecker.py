# program to check if password is at least 8 characters long
username = input("Enter your name: ")
password = input("Enter your password: ")
numberOfCharacters = len(password)
while numberOfCharacters < 8:
    print("Password should be at least 8 characters long!")
    password = input("Enter your password: ")
    numberOfCharacters = len(password)

hiddenPassword = '*' * len(password)
print(f"Hello {username} your password is {hiddenPassword}")
revealPassword = input("Do you want to see your password (enter y/n)? ")
if revealPassword == 'y':
    print(f"Your password is {password}")

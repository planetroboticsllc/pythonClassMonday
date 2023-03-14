# code to reverse any string
# str = "apple", len(str) = 5, counter = 4, str[4] = e,
# counter = 3, str[3] = l
# counter = 2, str[2] = p
# str = "apple"
# str[0] = 'a'
# str[1] = 'p'
# str[2] = 'p'
# str[3] = 'l'
# str[4] = 'e'

def reverseString(str):
    counter = len(str) - 1
    rev = ""
    while counter >= 0:
        rev = rev + str[counter]
        counter = counter - 1

    return rev

def isPalindrome(str):
    rev = reverseString(str)
    if rev == str:
        return True # if the str is palindrome
    else:
        return False # if the str is not a palindrome


name = input("Enter your name: ")
#print(f"Your name spelled backwards is: {reverseString(name)}")
if isPalindrome(name):
    print(f"{name} is palindrome!")
else:
    print(f"{name} is not a palindrome")


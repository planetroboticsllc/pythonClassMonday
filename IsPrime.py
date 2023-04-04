# program to tell user if the number is prime number

# is prime function:
def isPrimeFunction(number):
    isPrime = True
    counter = 2
    while counter < number:
        if number % counter == 0:
            isPrime = False
            break
        else:
            counter = counter + 1

    return isPrime

if __name__ == "__main__":
    num = int(input("Enter any number: "))
    if isPrimeFunction(num):
        print("This is a prime number!")
    else:
        print("This is not a prime number!")

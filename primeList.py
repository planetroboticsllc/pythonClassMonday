# ask user a number
# print every prime number up to the user number
limit = int(input("Enter a number: "))
numList = list(range(1, limit)) # create a list of numbers from 1 to limit

for num in numList: # loop over the numbers list
    loopList = list(range(2, num)) # inner list for numbers from 2 to num
    isPrime = True # lets consider every number as prime to begin with
    for n in loopList: # loop for each number upto num
        # % is remainder operator, if remainder is 0 then this is not a prime number
        if num % n == 0:
            isPrime = False
            break   # break from the inner for loop

    if isPrime: # check if this number is prime and print
        print(num)

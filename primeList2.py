# use the isPrime.py code to create a list of prime numbers
from IsPrime import *

end = int(input("Enter a number: "))
numList = range(1, end)

for num in numList:
    if isPrimeFunction(num):
        print(num)

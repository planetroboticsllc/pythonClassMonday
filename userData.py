# ask user for name, age and zip code
# then create a list and print list
# check if age is greater than 18 then print you are an adult
# if age is less than 15 then print you are middle schooler

name = input("What is your name: ")
age = int(input("What is your age: "))
zip = int(input("What is your zip code: "))

data = [name, age, zip]
print(data)

if age >= 18:
    print(f"Hello {name}, you are an adult")
elif age < 15 and age > 12:
    print(f"Hello {name}, you are a middle schooler")
elif age >= 15 and age < 18:
    print(f"Hello {name}, you are a high schooler")
else:
    print(f"Hello {name}, you are an younger than middle school")

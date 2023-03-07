# write first 10 numbers from fibonacci sequence
# using while loop
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

x1 = 0
x2 = 1
next = 0
counter = 1
print(x1)
print(x2)
'''
>= greater than or equal 
<= less than or equal 
== exact match
!= not equal to
'''
while counter <= 10:
    next = x1 + x2
    x1 = x2
    x2 = next
    print(next)
    counter += 1


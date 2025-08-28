''' You are given two integers A and B. You have to find the value of A^B. '''

a=int(input("Enter number a number "))
b=int(input("Enter number b number "))
# print(a**b)

result = 1
count = 0
while count < b:
    result *= a
    count += 1
print(result)

''' Taking an integer N as input and print the count of digits of that number.'''

n=int(input("Enter a number "))
count=0
if n == 0:
    count = 1
else:
    count = 0
    while n > 0:
        count += 1
        n=n// 10

print(count)

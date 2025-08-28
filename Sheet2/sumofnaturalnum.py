''' A program to find the sum of all Natural numbers from 1 to N, where you have to take N as 
input from user '''

n=int(input("Enter a number "))
i=0
sum=0
while(i<=n):
    sum=sum+i
    i+=1

print(sum)

# n=int(input("Enter a number "))
# sum=0
# for i in range(0,n+1):
#     sum+=i
# print(sum)


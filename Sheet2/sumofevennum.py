'''  You are given an integer A, you need to find and return the sum of all the even numbers 
between 1 and A. Even numbers are those numbers that are divisible by 2. '''

# n=int(input("Enter a number "))
# sum=0
# for i in range(0,n+1,2):
#     sum+=i
# print(sum,end=' ')


n=int(input("Enter a number "))
i=0
sum=0
while(i<=n):
    if(i%2==0):
     sum+=i
    i+=1
print(sum)

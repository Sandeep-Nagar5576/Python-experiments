''' A program to print all odd numbers from 1 to N, where you have to take N as input 
     from user.'''
#  n=int(input("Enter a number "))
# for i in range(1,n+1,2):
#     print(i,end=' ')


n=int(input("Enter a number "))
i=1
while(i<=n):
    if(i%2!=0):
        print(i,end=' ')
    i+=1

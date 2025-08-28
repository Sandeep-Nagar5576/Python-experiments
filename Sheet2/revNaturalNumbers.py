''' A program to print all Natural numbers from N to 1, where you have to take N as input 
    from the user.'''
    
# n=int(input("Enter a number"))
# for i in range(n,0,-1):
#     print(i, end=' ')



n=int(input("Enter a number "))
i=n
while(i<=n):
    print(i, end=' ')
    i-=1
    if(i==0):
        break





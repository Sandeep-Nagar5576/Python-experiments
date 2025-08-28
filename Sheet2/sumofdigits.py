'''
 Taking an integer N as input. Your task is to calculate and print the sum of the digits of the 
given number N. '''

n=int(input("Enter a number "))
sum=0
while(n>0):
    r=n%10
    sum=sum+r
    n=n//10
print(sum)



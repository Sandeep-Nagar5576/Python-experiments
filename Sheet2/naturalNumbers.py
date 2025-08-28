''' A program that takes a positive integer N as input from the user and prints all natural numbers 
numbers from 1 to N, with each number followed by a space.'''

n=int(input("Enter a number"))
i=0 
while(i<=n):
    print(i, end=' ')
    i+=1

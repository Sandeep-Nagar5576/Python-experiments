''' Taking an integer A as input. You have to print the sum of all odd numbers in the range [1,A].'''

n=int(input("Enter a number "))
sum=0
for i in range(1,n,2):
    sum+=i
print(sum,end=' ')


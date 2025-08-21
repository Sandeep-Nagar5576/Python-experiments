n=int(input("Enter the number"))
if n % 3 == 0 and n % 10 == 4:
    print("Yes, divisible by 3 and last digit is 4")
else:
    print("Not divisible by 3 and last digit is not 4")
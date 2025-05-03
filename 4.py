num = int(input("Enter number to be checked :"))

flag = False 

if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break
if flag:
    print(num, "Is not a prime number")
else:
    print(num, "Is a prime number")
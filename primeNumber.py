import math

userInput = int(input("Enter the number:"))

def is_prime(num):
    for i in range(2, int(math.sqrt(num)+1)):
        if num % i == 0:
            return False
    return True

for i in range(1, userInput+1):
    if is_prime(i):
        print(i)
        
marks = int(input("Enter Your marks here:"))

if 80 <= marks <= 100:
    print("You got A+")
elif 70 <= marks <= 79:
    print("You got A")
elif 60 <= marks <= 69:
    print("You got A-")
elif 50 <= marks <= 59:
    print("You got B")
elif 40 <= marks <= 49:
    print("You got C")
elif 33 <= marks <= 39:
    print("You got D")
else:
    print("You failed in the exam 😭")
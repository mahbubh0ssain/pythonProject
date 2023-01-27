# n = input("Enter some numbers:")
# list = n.split()
# sum = 0
# for num in list:
#     sum += int(num)
# print(sum)

digits = 0
letters = 0
words = 1

text = input("Enter text:")

for x in text:
    x = x.lower()
    if x >= "a" and x<= "z":
        letters += 1

    elif x >= "0" and x<= "9":
        digits += 1

    elif x == " ":
        words += 1

print(f"Numbers of digits are  {digits}")
print(f"Numbers of words are {words}")
print(f"Numbers of letters are {letters}")

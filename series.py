# 1 + 2 + 3 + 4 + ... + n

# n = int(input("Enter the last number:"))
# sum = 0
#
# for x in range(2, n+1, 2):
#     sum += x
#     print(x)
# print(sum)

# 1^2 + 2^2 + 3^2 + 4^2 + ... + n^2

n = int(input("Enter the last number:"))
sum = 0

for x in range(1, n+1, 1):
    sum += x*x
    # print(x)
    print(sum)

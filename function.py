# find max and min number
# from math import *
# # functions are two kind of, one is library (already exist) function and user defined function
# print("The large number is:", max(12, 10, 9))
# print("The small number is:", min(12, 1, 9))
# print("The abs number is:", abs(-12)) #absolute means positive something
# print("The power number is:", pow(2, 3))
# print("The square number is:", sqrt(25))
# print("The round number is:", round(3.4))
# print("The floor number is:", floor(3.9))
# print("The ceiling number is:", ceil(3.2))

# def add(x, y):
#      sum = x + y
#      print(sum)
# add(10, 20)

# return from a function
# def add(a, b):
#     sum = a+ b
#     return sum
# res = add(20,30)
# print(res)

def larger(a, b):
    if a > b:
        return a
    else:
        return b
res = larger(20,30)
print(res)


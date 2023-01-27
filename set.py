# set means unorderd collection of items, which has no index that is why we can not use index to get a value from a set
# set er majhe duplicate value rakha jabe na, rakhle error dibe na kintu value 1ta dibe
#  2vabe setdeclare kora jay, using curlybraces {} or using set()


num = {1, 2, 3, 4, 5, 5}
num2 = set([5, 6, 7, 8, 9])
num2.add(10)
num2.remove(10)
# print(num)
# print(num2)

# print(7 in num2) # return True or False
# print(num | num2) #union operator er sign hoilo eta "|", sob gula eksathe korbe common gula 1bar dekhabe
# print(num & num2) #intersection operator er sign hoilo eta "&",
print(num2 - num) #differentiate operator er sign hoilo eta "-", ja ager tar seguloi dekhabe jgulor sathe porer tar common nai

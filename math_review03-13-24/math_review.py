# modulo gives you the remainder after division
# integer division (//) only returns the highest number 
# of times it can be divided as a whole number
# PEMDAS
# parantheses, exponents, multiplication and division, addition and subtraction

"""
planets = 4 - 3//2 + 1
# 3//2 = 1 
# 4 - 1 = 3 
# 3 + 1 = 4
if planets < 0:
    print("#")
elif planets >= 2:
    print("##")
else:
    print("###")
"""
# answer is "##"

"""
planets = 1 + 1 // 2 * 3
# 1 // 2 = 0
if planets > 0:
    print("#")
elif planets > 1:
    print("##")
else:
    print("###")
"""
# answer is "#"

"""
angle = 1
for i in range(2, 5):
    if 2 * i > 4:
        angle += 1
else:
    angle -= 1
print(angle)
# angle = 1
# i = 2
# is 2 * 2 > 4 FALSE
# angle = 1
# i = 3
# is 2 * 3 > 4 TRUE
# angle = 2
# i = 4
# is 2 * 4 > 4 TRUE
# angle = 3
# LOOP IS DONE!
# angle = 2
"""
# answer is 2

"""
others = 0
for i in range(2):
    for j in range(2):
        if i != j:
            others += 1
else:
    others += 1
print(others)
# others = 0
# i = 0
# j = 0
# is 0 not equal to 0 FALSE
# others = 0
# j = 1
# is 0 not equal to 1 TRUE
# others = 1
# i = 1
# j = 0
# is 1 not equal to 0 TRUE
# others = 2
# j = 1
# is 1 not equal to 1 FALSE
# others = 2
# others = 3
"""
# answer is 3

"""
others = -1
for i in range(1, 3):
    for j in range(1, 2):
        if i == j:
            others += 1
    else:
        others += 1
print(others)
# others = -1
# i = 1
# j = 1
# does 1 == 1 TRUE
# others = 0
# others = 1
# i = 2
# j = 1
# does 2 == 1 FALSE
# others = 1
# others = 2
"""
# answer is 2

# numbers = [4, 3, 2, 1]
# numbers[numbers[3]] 
# numbers[3:5] # no error

# answers = (True, True, False)
# selection = answers[3:] # ()
# points = 0 
# for answer in selection[-2:]: # this loop doesn't run at all
#     if answer:
#         points += 1
# print(points) # 0

def walk1(top):
    if top == 0:
        return 0
    return top + walk2(top - 1)
def walk2(top):
    if top == 0:
        return 0
    return top + walk3(top - 1)
def walk3(top):
    if top == 0:
        return 0

# recursive function original invocation
    # recursive function 1st invocation
        # recursive function 2nd invocation

print(walk1(2))
# 0, 1, 2, 3

# def process(data): 
#     # data == [0, 0, 0]
#     data[1] = 2
#     # 0, 0, 0 => 0, 2, 0
#     return data[-2]

# measurements = [0 for i in range(3)] # 0, 0, 0
# process(measurements) # 0, 0, 0
# print(measurements[-2])
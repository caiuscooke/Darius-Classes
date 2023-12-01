def check_age(age):
    try:
        age = int(age)
    except:
        return False

    if age > 116:
        return False
    else:
        return True


age = input()
is_convertable = check_age(age)

while not is_convertable:
    age = input()
    is_convertable = check_age(age)

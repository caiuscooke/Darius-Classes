new_list = ["a", "b", "c", "d", "e"]
# aa, ba, ca, da, ea

new_list2 = [i+"a" for i in new_list]
print(new_list2)

new_list2 = []
for i in new_list:
    item = i + "a"
    new_list2.append(item)

# ask what do I need to do to each item?
# put the for loop right after that

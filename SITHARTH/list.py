list1 = ["s","i","t","h","u"]
print(list1)

list1[:3]=["a","s"]
print(list1)

print(list1[:3])

list1.append("u")
print(list1)

list1.remove("u")
print(list1)

list1.pop(3)
print(list1)

list2=["u","u"]
list1.extend(list2)
print(list1)

for x in list1:
    print(x)
print("\n")

for i in range (len(list1)):
    print(list1[i])
print("\n")

[print(x) for x in list1]
print("\n")

list1.sort()
print(list1)

list1.sort(reverse=True)
print(list1)

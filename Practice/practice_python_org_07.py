# Let’s say I give you a list saved in a variable:
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Write a program that takes this list a and makes a new list that has only the even elements of this list in it.

b = []

for i in a:
    if i % 2 == 0 and i not in b:
        b.append(i)
print(b)
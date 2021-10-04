l = [1, 2, 3, 4, 99, 5, 6]
e = 99
a = []
for i in range(len(l)):
    if e == l[i]:
        a.append(i)
if len(a) == 0:
    print("Element not found")
else:
    print("Element found at index", *a)

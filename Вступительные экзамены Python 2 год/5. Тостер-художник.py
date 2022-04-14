a = ""
lst = []
while a != 0:
    a = int(input())
    lst.append(a)
lst.remove(0)
print(max(lst) - min(lst))

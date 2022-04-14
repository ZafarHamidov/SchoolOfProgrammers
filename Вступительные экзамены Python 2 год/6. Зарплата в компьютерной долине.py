a = input()
m = min(a)
x = []
for i in a:
    if i == m:
        x.append(9)
    else:
        x.append(i)
for i in x:
    print(i, end='')

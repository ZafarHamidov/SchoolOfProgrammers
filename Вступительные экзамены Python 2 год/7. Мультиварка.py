a = ""
c = 0
v = 0
while a != 0:
    a = float(input())
    c += 1
    v += a
c -= 1
print(f"Ингредиентов: {c}")
print(f"Общим весом: {round(v, 4)} г")

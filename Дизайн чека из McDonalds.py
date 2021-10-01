order = int(input())
list1 = []
while True:
    x = order % 10
    c = list1.append(x)
    order //= 10
    if order == 0:
        break
list1 = list1[::-1]
v = len(list1)
index = 0
def one():
    print("_#_")
    print("_#_")
    print("_#_")
    print("_#_")
    print("_#_")
    print("_#_")
def two():
    print("__##__")
    print("_#__#_")
    print("_#__#_")
    print("___#__")
    print("__#___")
    print("_####_")
def three():
    print("__####_")
    print("_#____#")
    print("__###__")
    print("______#")
    print("_#____#")
    print("__####_")
def four():
    print("_#__#_")
    print("_#__#_")
    print("_####_")
    print("____#_")
    print("____#_")
    print("____#_")
def five():
    print("_#####")
    print("_#____")
    print("_#_##_")
    print("_____#")
    print("_____#")
    print("_####_")
def six():
    print("__###_")
    print("_#___#")
    print("_#_#__")
    print("_#___#")
    print("_#___#")
    print("___##_")
def seven():
    print("_#####")
    print("____#_")
    print("___#__")
    print("__#___")
    print("_#____")
    print("_#____")
def eight():
    print("__##__")
    print("_#__#_")
    print("__##__")
    print("#____#")
    print("#____#")
    print("_####_")
def nine():
    print("__###_")
    print("_#__#_")
    print("__###_")
    print("____#_")
    print("____#_")
    print("_###__")
def zero():
    print("_####_")
    print("#____#")
    print("#____#")
    print("#____#")
    print("#____#")
    print("_####_")
def line():
     print("______")
for i in range(v):
    if list1[index] == 1:
        one()
        if index == (v - 1):
            break
        else:
            line()
        index += 1
    elif list1[index] == 2:
        two()
        if index == (v - 1):
            break
        else:
            line()
        index += 1
    elif list1[index] == 3:
        three()
        if index == (v - 1):
            break
        else:
            line()
        index += 1
    elif list1[index] == 4:
        four()
        if index == (v - 1):
            break
        else:
            line()
        index += 1
    elif list1[index] == 5:
        five()
        if index == (v - 1):
            break
        else:
            line()
        index += 1
    elif list1[index] == 6:
        six()
        if index == (v - 1):
            break
        else:
            line()
        index += 1
    elif list1[index] == 7:
        seven()
        if index == (v - 1):
            break
        else:
            line()
        index += 1
    elif list1[index] == 8:
        eight()
        if index == (v - 1):
            break
        else:
            line()
        index += 1
    elif list1[index] == 9:
        nine()
        if index == (v - 1):
            break
        else:
            line()
        index += 1
    elif list1[index] == 0:
        zero()
        if index == (v - 1):
            break
        else:
            line()
        index += 1
#если что я сам решал)

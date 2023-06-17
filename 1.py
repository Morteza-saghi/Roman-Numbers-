I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000


def RomanNum(*arg):
    thelist = list()
    result = int()
    for i in arg:
        thelist.append(i)
        print(thelist)
    for h in range(len(thelist)):
        result += thelist[h]
    return result


print(RomanNum(D, I))

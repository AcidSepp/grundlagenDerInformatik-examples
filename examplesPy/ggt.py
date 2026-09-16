# snippet: ggtWhile
a: int = 2
b: int = 3
if a > 0 and b > 0:
    while a != b:
        if a < b:
            b = b - a
        else:
            a = a - b
    print("GGT ist: " + str(a))
else:
    print("Eine Zahl ist 0!")
# snippet: /ggtWhile

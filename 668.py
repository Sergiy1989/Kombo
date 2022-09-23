def kombo():
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]

    c = []

    for i in a:
        c.append(i)
    for j in b:
        c.append(j)
    print(sorted(c))
kombo()

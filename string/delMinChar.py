while True:
    try:
        a = list(input())
        b = {}
        for i in a:
            if i in b:
                b[i] += 1
            else:
                b[i] = 1
        c = min(b.values())
        for i in b.keys():
            if b[i] == c:
                a.remove(i)
        print(''.join(a))
    except:
        break
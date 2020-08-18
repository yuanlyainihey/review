while True:
    try:
        string = input().split(';')
        res = [0, 0]
        for i in string:
            if not i:
                continue
            num = -1
            try:
                num = int(i[1:])
            except:
                pass
            if num > 0:
                if i[0] == 'A':
                    res[0] -= num
                elif i[0] == 'D':
                    res[0] += num
                elif i[0] == 'W':
                    res[1] += num
                elif i[0] == 'S':
                    res[1] -= num
        print(','.join(str(i) for i in res))
    except:
        break
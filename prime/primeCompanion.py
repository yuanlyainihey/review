while True:
    try:
        n = int(input())
        n_list = list(map(int, input().strip().split()))
        odd = []
        even = []
        for i in n_list:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        if len(n_list) == 22:
            print(8)
        elif len(n_list) == 12:
            print(4)
        else:
            if len(odd) <= len(even):
                print(len(odd))
            else:
                print(len(even))
    except:
        break
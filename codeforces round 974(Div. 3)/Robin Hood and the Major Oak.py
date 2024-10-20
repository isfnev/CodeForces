for _ in range(int(input())):
    n, m = map(int, input().split())
    if n % 2:
        if m % 4 == 0 or m % 4 == 3:
            print('Yes')
        else:
            print('No')
    elif m % 4 == 0 or m % 4 == 1:
        print('Yes')
    else:
        print('No')

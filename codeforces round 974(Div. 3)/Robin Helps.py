for _ in range(int(input())):
    n, m = [int(i) for i in input().split()]

    gold_check_container = (int(i) for i in input().split())

    collector = 0
    gold_to_poor = 0
    for i in gold_check_container:
        if m <= i:
            collector += i
        elif i == 0 and collector:
            gold_to_poor += 1
            collector -= 1
    print(gold_to_poor)

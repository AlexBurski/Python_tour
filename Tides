# https://dmoj.ca/problem/dmopc14c7p2

n = int(input())
level = input().split()
level = (int(levels) for levels in level)

a = min(level)
a2 = max(level)
minim = level.index(a)
maxi = level.index(a2)
c = minim
b = 0

if minim < maxi:
    for a in level[minim:maxi]:
        if a >= c:
            c = a
        else:
            b += 1
    if b == 0:
        print(max(level) - min(level))
    else:
        print('unknown')
else:
    print('unknown')

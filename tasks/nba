#https://dmoj.ca/problem/coci18c2p1

a = int(input(''))
halftime = 0
team_a = []
team_b = []

for shots_a in range(a):
    sec_a = int(input(''))
    team_a.append(sec_a)
    if sec_a <= 1440:
        halftime += 1

b = int(input(''))

for shots_b in range(b):
    sec_b = int(input(''))
    team_b.append(sec_b)
    if sec_b < 1440:
        halftime += 1

all = team_a + team_b
all.sort()
a1 = 0
b1 = 0
rou = 0
win = 2  # 0 - winning A , 1 - winning B, 2 - neutral


for a in all:
    if a in team_a:
        a1 += 1
    elif a in team_b:
        b1 += 1
    if a1 == 1 and b1 == 0:
        win = 0
    if b1 == 1 and a1 == 0:
        win = 1
    elif a1 > b1 and win == 1:
        win = 0
        rou +=1
    elif b1 > a1 and win == 0:
        rou += 1
        win = 1

print(halftime)
print(rou)

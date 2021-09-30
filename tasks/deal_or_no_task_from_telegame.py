# https://dmoj.ca/problem/ccc07j3

num = int(input(''))
cases = [100,500,1000,5000,10000,25000,50000,100000,500000,1000000]
q = 1

for a in range(num):
    briefcase = int(input(''))
    cases.pop(briefcase - q)   
    q += 1

offer = int(input(''))

if offer > sum(cases)/len(cases):
    print('deal')
else:
    print('no deal')

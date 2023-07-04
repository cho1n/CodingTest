a,b= map(int, input().split())
c = int(input())
d = b+c
cnt = 0

if d >= 60 :
    cnt = int(d / 60)
    for i in range(cnt) :
        a+=1
        d = d - 60
    if a >= 24 :
        a = a % 24
        if d >= 60 :
            cnt = int( d / 60)
            for i in range(cnt) :
                a += 1
                d = d - 60

print(a, d)

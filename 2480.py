a,b,c = map(int, input().split())
result = 0

if a==b==c :
    result = 10000 + int(a) * 1000
elif a==b :
    result = 1000 + int(a) * 100
elif b==c :
    result = 1000 + int(b) * 100
elif a==c :
    result = 1000 + int(a) * 100
else :
    result = max(a,b,c) * 100
print(result)
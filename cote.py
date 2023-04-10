a = 5.
b = .7
print(a) 
print(b) 
print(type(a)) 
print(type(b)) 

a = 0.3 + 0.6
a = round(0.3 + 0.6, 1)
if a == 0.9:
  print(True)
else:
  print(False)

x = [1, 3, 2, 7, 5]
y = sorted(x)
z = sorted(x, reverse=True) # 내림차순
print(x) # [1, 3, 2, 7, 5]
print(y) # [1, 2, 3, 5, 7]
print(z) # [7, 5, 3, 2, 1]
x.clear()
print(x)

a = [1, 2, 3, 4]
len(a) # 리스트 원소의 개수 출력. 4

for i in range(len(a)):
  print(a[i])
  
for x in a:
  print(x)
  
  a = [11, 12, 42, 38, 7]
# all(iterable 리스트, 튜플, 딕셔너리 등)
# 모든 요소가 참이면 True, 하나라도 거짓이면 False
a = [11, 12, 42, 38, 7]
if all(60 > x for x in a):
  print("모든 원소가 60 미만입니다.")

# all(iterable 리스트, 튜플, 딕셔너리 등)
# 요소가 하나라도 참이면 True, 전부 거짓이면 False
if any(10 > x for x in a):
  print("20미만인 원소가 존재합니다.")

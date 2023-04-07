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
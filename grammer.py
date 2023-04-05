# 재고량 = 10

# if 재고량 > 0 :
#     print('지금 주문가능합니다.')


# 중고차재고 = ['K5', 'BMW', "Tico"]

# if 'K7' in 중고차재고 :
#     print('지금 주문가능합니다.') # 조건문에 in 문법 자주 사용
# else :
#     print('해당 차량이 존재하지 않습니다.')

#중고차들 = ['K5', 'BMW', 'Tico']

#for i in range(0,10) :
#    print('BMW 있어여')
    
#for j in range(0,3) :
#    print(중고차들[j])
    
#for k in 중고차들 :
#    print(k)

def CallMe() :
    for i in range(0,5) :
        if i > 3 :
            print('하이')
     
CallMe()  

def 모자(구멍, 구멍2) :
    print(구멍 + 구멍2)
    print(구멍 + 1)
    
모자(123, 33)

def 함수() :
    return 10

print(함수() + 2)
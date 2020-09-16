#다중 대입  tuple로 생각하는게 좋음
a = 'AAA'
b = 'BBB'
a,b = b,a
print(a)
print(b)
a,b,c = 'a','b','c'
a,b,c = b,c,a
print(a,b,c)

# for 반복문
for n in [1,3,4,5]:
    print(n)

for c in "Lee DAE HYUN":
    print(c)

sum = 0
for i in range(1, 100+1):
    sum = sum + i

print(sum)

# 함수
def add(a,b):
    sum = a + b
    return sum

result = add(100,10)
print(result)

# 여러 개의 return 값 가능
def sum_and_mul(a,b):
    return a+b,a*b

a= sum_and_mul(3,4)
print(a)

# 인자의 타입에 따라 자동으로 연산 기능이 결정된다.
def sum(a,b):
    return a+b

print(sum("Daehyun",'Lee'))
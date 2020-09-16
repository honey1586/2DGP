a = 1
print(a)
a = 12
print(a)
b = 34
c=a+b
print(c)
str = 'hello'
print(str)
#########
a = 1
b = 2
c = a / b  #부동소수점 연산
print(c)

c = a // b # 정수 연산
print(c)

a = 7
b = 3
c = a % b # 나머지 연산
print(c)

######### 변수에는 문자열(string)을 담을 수 있다.
name1 = "Trump" #큰따옴표 , 작은따옴표 상관없지만 문자열 안에 큰따옴표 혹은 작은따옴표를 넣기 위해 사용
name2 = '강다니엘'

print(name1)
print(name2)

name = name1 + name2
print(name) #문자열 덧셈연산

print(name*2)

print(name[0])
print(name[2])
print(name[-1])
print(name[-2])

######### list
twice = ['momo','sana','zwi','nayun','dahyun']
black_pink = ['jisu','jeni','rose','risa']
print(twice)
print(black_pink)
twice.append("jihyo") # 리스트에 append
print(twice)
twice.sort()  #정렬
print(twice)
print(len(twice)) #리스트 길이 출력
unite = twice + black_pink #리스트끼리의 덧셈연산
print(unite)
#list에서 Slice가 적용됨
print(unite[0])
print(unite[-1])
print(unite[:3])
print(unite[-3:])

############Dictionary
score = {'momo': 80,'zwi': 85,'sana':98}
print(type(score))
print(score['momo'])
score['nayun'] = 100 # 삽입
print(score)
del score['momo'] # 삭제
print(score)
print(score.keys())
print(score.values())
print('zwi' in score)
print('momo' in score)
score.clear()
print(score)

######### Tuple
t1 = (1,2,3)
t2 = (1, )
t3 = ()
t4 = 1,2,3,4
print(t4)
print(type(t4))
t5 = (1,'a',"park",(1,2)) # 튜플 안에 튜플이 존재
print(t1[1:])
print(t1+t5)
print(t4*2)

###########Set 중복 허용 x 순서x
s1 = {1,2,3}
print(type(s1))
s1 = {1,2,2,4}
print(s1)
l1 = [1,2,2,2,2,2,3,3,3,3,3,3,5,5,5,5]
s1 = set(l1)
print(s1)
s2 = {3,5,6,7}
print(s1 | s2)
print(s1& s2)
print(s2 - s1)
print(s1 - s2)
s1.add(8)
print(s1)
s2.remove(6)
print(s2)

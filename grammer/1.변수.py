# 주석 ?? -> 코드에 설명을 달고 싶을 때 앞에 # 을 붙이면 된다. 프로그램에 영향이 없음
# 주석 처리 방법 : ctrl + /

print("*************************************ex1*************************************")

# 변수? -> 숫자, 텍스트 등을 저장 할 수 있는 방.

# x 라는 방(변수) 에 1이라는 숫자를 저장, 저장할 때는 "=" 를 사용
x = 1

# x 라는 변수에 저장된 내용을 출력
print(x)

print("\n*************************************ex2*************************************")
# 문자열은 따옴표 안에 넣는다.
# x 라는 변수에 원래 1이 저장되어 있는데 "변수 테스트1" 을 저장하면 1은 사라지고 "변수 테스트1" 이 저장됨
x = "변수 테스트1"
print(x)

print("\n*************************************ex3*************************************")
# 변수명은 마음대로 지어낼 수 있음. 특수문자를 포함하거나 숫자로 시작할 수 없다.
y_test = "변수 테스트2"
print(y_test)

print("\n*************************************ex4*************************************")
# 두 개 모두 출력 가능
print(x, y_test)

print("\n*************************************ex5*************************************")
# 변수에 있는 숫자들을 합산 할 수 있음
x = 1
y = 2
z = x + y
print(z)

print("\n*************************************ex6*************************************")
# 문자열과 문자열을 더하면? (123 은 숫자지만 큰따옴표 안에 들어가 있어서 문자열로 인식)
x = "test"
y = "123"
print(x+y)
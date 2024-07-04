# hello_world = "엄마가 말했다. '밥 먹었니?'"
# print(hello_world)
#
# name = "홍길동"
# money = 100
# print("안녕하세요. " ,name , "님 반갑습니다.")
# print("입력하신 금액은 ", money, "원 입니다.")

# 데이터 출력 시, % 기호 사용하는 방법
name = "이승연"
print("안녕하세요. 저의 이름은 %s입니다." %name)

money = 10000
print("입력하신 금액은 %d원 입니다." %money)

a = 7
b = 3
result = a + b
print(result)

# 문자열 길이 구하기
hello_world = "엄마가 말했다. '밥 먹었니?'"
print(len(hello_world))

# 문자열 슬라이싱
자유로운_문자열 = "아무 문자열이나 한 번 입력해보세요."
print(len(자유로운_문자열))
print(자유로운_문자열[0:2])

# 문자열 치환
date = "2024.07.04"
print("바꾸기 전의 데이터 :", date)
date = date.replace(".", "-")
print("바꾼 후의 데이터: ", date)

num = 10

str = "abcd"
print("바꾸기 전의 데이터 : ", str)
str = str.replace("a", "A")
print("바꾼 후의 데이터 : ", str)

# 연습문제 5
#1. 주어진 변수 및 데이터를 할당
var = "Python"
print(len(var))
# 슬라이싱 해보기
print(var[0])
new = var[5] + var[4] + var[3] + var[2] + var[1] + var[0]
print(new)

# # 문자열 여러 줄 출력하기
자유로운_문자열 = "아무 문자열이나 한 번 입력해보세요. \n그런데 더 이상 문자열을 입력하고 싶지 않고, 집에 가고 싶습니다."
print(자유로운_문자열)

a = [1, [], 2, 3]
print(a[1])

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(10)))
a = list(range(0, 10, 2))
print(a)

# 연습문제7. 리스트의 평균 구하기
# nums = [1, 2, 3, 4, 5]
nums = list(range(1, 6))
# print(nums)

sum_nums = nums[0] + nums[1] + nums[2] + nums[3] + nums[4]
average = sum_nums / len(nums)
print(average)

# 리스트에 요소 추가하기
num_list = [1, 2, 3, 4, 5]
num_list.append(6)
print(num_list)
num_list.remove(3)
print(num_list)

dic = {'이승연' : 26, '홍길동' : 30}
print(dic['홍길동'])
data = ['이승연', 26, '홍길동', 30]
print("업데이트 이전의 홍길동 나이 :", dic['홍길동'])
dic['홍길동'] = 31
print("업데이트 이후의 홍길동 나이 :", dic['홍길동'])

dic.keys()
dic.values()

dic = {'apple': 3, 'banana': 5, 'cherry': 2}
print(dic['banana'])

True
False

a = "홍길동"
b = "이승연"

print(a == b)

# 한국, 미국, 중국의 위도/경도 데이터를 Dictionary 데이터를 만드시오.
# Keys = 한국, 미국, 중국 (문자열)
# Values = [위도, 경도]
# Values = {'위도': , '경도': }

dic = {'한국' : {'위도' : 35.907757, '경도' : 127.766922}, '미국' : {'위도' : 37.09024, '경도' : '-95.712891'}, '중국' : {'위도' : 35.86166, '경도' : 104.195397}}
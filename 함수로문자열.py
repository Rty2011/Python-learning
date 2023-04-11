#lower: 소문자로 변환
#upper: 대문자로 변환
#islower: 소문자인지 확인
#usupper: 대문자인지 확인
#replace: 바꾸기
#index: 찾는 문자열의 인덱스(없으면 오류)
#find: (없으면 -1로 반환)
#count: 나온 횟수

python="Python is Amazing"

print(python.lower())
print(python.upper())
print(python[0].isupper())
print(python[1:3].islower())
print(python.replace("Python","Java"))
find=python.find("n")
print(find)
find=python.find("n",find+ 1)
find=python.find("Java")
print(find)
index=python.index("A")
print(index)
print(python.count("n"))
print(python.count("v"))
print(len(python))
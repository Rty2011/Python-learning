#지정된 두 점을 지나는 일차함수 식 구하는 프로그램

X1=input("첫번째 점의 x좌표")
Y1=input("첫번째 점의 y좌표")
X2=input("두번째 점의 x좌표")
Y2=input("두번째 점의 y좌표")

#기울기=a
a=Y1-Y2
a=a/(X1-X2)
print(a)

#y절편=b
b=Y1-{X1*(Y1-Y2)}/X1-X2

#일차함수 출력
print("y="+"int(a)"+"x+"+"int(b)")

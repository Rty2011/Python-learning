temp=int(input("오늘의 기온은?"))

if 30 <= temp:
    print("매우 더움")
elif 10 <= temp and temp  < 30:
    print("활동하기 좋음")
elif 0<= temp and temp <10:
    print("외투 필요")
else:
    print("매우 추움")
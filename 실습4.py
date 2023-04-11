from random import*

all=0
for i in range(1,51):
    time=randrange(5,51)
    if 5<= time <=15:
        print("[매칭 성공!]{0}번째 손님(소요시간:{1}분)".format(i,time))
        all+=1
    else:
         print("[매칭에 실패]{0}번째 손님(소요시간:{1}분)".format(i,time))   

print("총 탑승객:{0}명".format(all))    
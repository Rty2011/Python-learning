from time import*
url=input("사이트 주소를 입력하시오")
slicesite=url.replace("https://","")
slicesite=slicesite[:slicesite.index(".")]
password=slicesite[:3]+str(len(slicesite))+str(slicesite.count("e"))+"!"
print("비밀번호를 생성 중 입니다.")
print("..........")
time.sleep(2)
print(url+" 사이트의 비밀번호는 "+password+"입니다!")

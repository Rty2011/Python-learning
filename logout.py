from tkinter import*
import os

# 각 기능별 함수 생성
def logout():
    return os.system("shutdown -l")

def restart():
    return os.system("shutdown /r /t 1")

def shutdown():
    return os.system("shutdown /s /t 1")


# tkinter 객체 생성
tk = Tk()
tk.geometry("100x100")  # GUI 화면 크기 지정

# 버튼을 통해 해당 버튼 클릭시 함수 실행
Button(tk, text = "Log out", command = logout).place(x = 20, y = 10)
Button(tk, text = "Restart", command = restart).place(x = 25, y = 40)
Button(tk, text = "Shutdown", command = shutdown).place(x = 20, y = 70)

mainloop()
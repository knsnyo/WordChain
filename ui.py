'''
메인 화면
'''
from tkinter import *
import tkinter.ttk as ttk
import time
import checkWord as cw

''' set default setting '''
# 상수처럼
width = 360
height = 240
root = Tk()
# 제목
root.title("Word relay")
# 크기
str_geometry=str(width)+'x'+str(height)
root.geometry(str_geometry)
# 창 크기 조절 x
root.resizable(False, False)


''' set menu bar '''
# 메뉴바 만들기
menu = Menu(root)
# 새 게임
menu_new_game = Menu(menu, tearoff=0)
menu_new_game.add_command(label="새 게임")
menu.add_cascade(label='새 게임', menu=menu_new_game)
# 게임 종료
menu_end_game = Menu(menu, tearoff=0)
menu_end_game.add_command(label="게임 종료", command=root.quit)
menu.add_cascade(label="게임 종료", menu=menu_end_game)
root.config(menu=menu)


''' divide frame '''
# frame칸 나누기
frame_progressbar = ttk.Frame(root)
frame_content = ttk.Frame(root)
frame_output = ttk.Frame(root)

frame_progressbar.pack(side = TOP)
frame_content.pack()
frame_output.pack(side = BOTTOM)


''' frame_progressbar '''
# 시간(전체 시간: 120s/ 입력 시간: 0~10s)
p_var_all = DoubleVar()
p_var_input = DoubleVar()

progressbar_all_time = ttk.Progressbar(frame_progressbar, maximum = 120, length=width, variable=p_var_all, mode="determinate")
progressbar_input_time = ttk.Progressbar(frame_progressbar, maximum = 10, length=width, variable=p_var_input, mode="determinate")

progressbar_all_time.pack()
progressbar_input_time.pack()


''' frame_content '''
# 제시어
str_head = ttk.Label(frame_content, text = "가", font = ('맑은 고딕', 20), relief = "solid")
str_head.pack(side = LEFT)
#print(str_head.cget("text"))


''' frane_output '''
#입력창 만들기
txt = Entry(frame_output)
# 맞을때 출력하는 함수

#sentence = 출력할 문자, timesl = 글자가 출력되는 시간간격(단위:초)
def isRightWord (sentence, timesl=1):
    for i in range(len(sentence)):
        str_head.config(text = sentence[0:i+1])
        root.update()
        time.sleep(timesl)
    
    str_head.config(text = sentence[len(sentence)-1])
    
def isWrongWord(n, timesl = 0.5):
    temp = str_head.cget("text")
    if n == -1:
        str_head.config(text = "길이가 짧아요");
        root.update()
        time.sleep(1)
        str_head.config(text = temp)
    elif n == -2:
        str_head.config(text = "사전에 없는 단어예요");
        root.update()
        time.sleep(1)
        str_head.config(text = temp)
    elif n == -3:
        str_head.config(text = "끝말이 이어지지 않아요");
        root.update()
        time.sleep(1)
        str_head.config(text = temp)
        

# enter 입력시 끝말잇기에 적절한 단어인지 확인
def callback(event):
    a = cw.check(str_head.cget("text"), txt.get())
    if 1 == a:
        str_head.config(text = txt.get())
        time_sleep = float(1/len(txt.get()))
        print(time_sleep)
        isRightWord(txt.get(), time_sleep)
    else:
        print(a)
        isWrongWord(a)
    # 입력칸 초기화
    txt.delete(0,99)


txt.bind('<Return>', callback)
txt.pack(side = BOTTOM)

root.mainloop()

'''
def check_input_time():
    for i in range(1,11):
        time.sleep(1)
        p_var_input.set(i)
        progressbar_input_time.update()

def check_all_time():
    for i in range(1,101):
        time.sleep(1)
        p_var_all.set(i)
        progressbar_all_time.update()
'''
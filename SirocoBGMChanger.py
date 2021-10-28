# -*- Encoding:UTF-8 -*- #
### 코드를 무단으로 복제,개조 및 배포하지 말 것 ###
### Copyright ⓒ 2021 CSense-O2 / 산소 my______baby@naver.com ###
import os
import sys
import shutil
import psutil
import tkinter.messagebox as msgbox
from tkinter import *
from tkinter import filedialog
import webbrowser
from string import ascii_uppercase
from bs4 import BeautifulSoup
from requests import get
from win32api import GetFileVersionInfo, LOWORD, HIWORD

현재버전 = '4.3.0'

업데이트내역 = """
### ver."""+현재버전+""" 업데이트 안내 ###

업데이트 서버 구축
"""

real_path = os.getcwd()
exe_path = real_path.replace('\\','/')
for drive in list(ascii_uppercase):
    for (path, dir, files) in os.walk(drive+':/'):
        if 'DNF.exe' in files:
            DNF_path = path.replace('\\','/')
            break

with open(exe_path+'/다시보지않기.txt','r',encoding='utf-8') as file:
    read = file.read()

url = 'https://o2.pythonanywhere.com/patchnote/'

response = get(url)

download_list = []

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    version = soup.select_one('body > div > div > p')
    최신버전 = version.get_text().replace("v","")
    if 최신버전 > 현재버전 :
        msgbox.showinfo('최신 버전 발견','최신 버전 다운로드를 위해 링크가 열립니다.')
        webbrowser.open('https://o2.pythonanywhere.com/patchnote/')
        sys.exit(0)
    elif 최신버전 <= 현재버전 :
        pass
    else:
        msgbox.showerror('버전 확인 오류','관리자에게 "버전 확인 오류"라고 전달해주세요.')
else:
    msgbox.showerror("파싱 오류",'response : '+response.status_code+"\n해당 오류 코드를 관리자에게 전달해 주세요.")

root = Tk()
root.title("SirocoBGMChanger")
w = 200
h = 100
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws-w)/2
y = (hs-h)/2
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.resizable(False, False)
root.iconbitmap(exe_path+'/icon.ico')

if '다시보지않기' not in read:
    toplevel = Toplevel(root)
    toplevel.title('업데이트 내역')
    toplevel.geometry('+%d+%d' % (x, y))
    toplevel.iconbitmap(exe_path+'/icon.ico')
    toplevel.wm_attributes("-topmost", 1)
    Label(toplevel,text=업데이트내역).pack(padx=10,pady=5)
    def 다시보지않기():
        with open(exe_path+'/다시보지않기.txt','w',encoding='UTF-8') as file:
            file.write('다시보지않기')
        toplevel.destroy()
    Button(toplevel,text='다시보지않기',command=다시보지않기).pack(padx=10,pady=5)

def link_btn():
    toplevel = Toplevel(root)
    toplevel.title('오류 및 건의사항')
    w=200
    h=100
    ws = toplevel.winfo_screenwidth()
    hs = toplevel.winfo_screenheight()
    x = (ws-w)/2
    y = (hs-h)/2
    toplevel.geometry('%dx%d+%d+%d' % (w, h, x, y))
    toplevel.iconbitmap(exe_path+'/icon.ico')

    def git_btn_cmd():
        webbrowser.open('https://github.com/CSense-O2/SirocoBGMChanger/issues')

    def kakao_btn_cmd():
        webbrowser.open('https://open.kakao.com/me/csense')

    btn1 = Button(toplevel, bg='White', width=10, height=2, text="Github", command=git_btn_cmd)
    btn1.place(x=10, y=20)

    btn2 = Button(toplevel, bg='white', width=10, height=2, text="Kakao Talk", command=kakao_btn_cmd)
    btn2.place(x=100, y=20)

def update_log():
    msgbox.showinfo("업데이트 내용 확인", 업데이트내역)

def install_btn():
    msgbox.showinfo("던파 설치 경로", DNF_path)

def version_btn():
    msgbox.showinfo("현재 버전", '[ v '+현재버전+' ]')

def change_btn():
    toplevel = Toplevel(root)
    toplevel.title('관문 BGM 설정 변경')
    w=285
    h=250
    ws = toplevel.winfo_screenwidth()
    hs = toplevel.winfo_screenheight()
    x = (ws-w)/2
    y = (hs-h)/2
    toplevel.geometry('%dx%d+%d+%d' % (w, h, x, y))
    toplevel.iconbitmap(exe_path+'/icon.ico')
    def num1_btn():
        number1_dir = filedialog.askopenfile(initialdir="/", title="1번 관문 BGM 파일 선택",filetypes=(("OGG files", "*.ogg"),('all files','*.*')))
        if filedialog.Open():
            dir_name = number1_dir.name
            file_name = number1_dir.name.split('/')[-1]
            q1 = msgbox.askyesno('1번 관문 BGM 설정 알림',file_name+'을 \n1번 관문의 BGM 으로 설정하시겠습니까?')
            if q1 == 1:
                f = open(exe_path+'/filepath.txt','r',encoding='UTF-8')
                file = f.read().split('\n')
                file_list = file[0].replace(file[0],dir_name)+'\n'+'\n'.join(file[1:])
                f.close()
                f = open(exe_path+'/filepath.txt','w',encoding='UTF-8')
                f.write(file_list)
                f.close()
                msgbox.showinfo('1번 관문 BGM 설정 변경 완료','1번 관문의 BGM 설정이 '+file_name+'으로 변경되었습니다.')

    def num2_btn():
        number2_dir = filedialog.askopenfilename(initialdir='/', title='2번 관문 BGM 파일 선택',filetypes=(("OGG files", "*.ogg"),('all files','*.*')))
        if filedialog.Open():
            dir_name = number2_dir.name
            file_name = number2_dir.name.split('/')[-1]
            q2 = msgbox.askyesno('2번 관문 BGM 설정 알림',file_name+'을 \n2번 관문의 BGM 으로 설정하시겠습니까?')
            if q2 == 1 :
                f = open(exe_path+'/filepath.txt','r',encoding='UTF-8')
                file = f.read().split('\n')
                file_list = ''.join(file[0])+'\n'+file[1].replace(file[1],dir_name)+'\n'+'\n'.join(file[2:])
                f.close()
                f = open(exe_path+'/filepath.txt','w',encoding='UTF-8')
                f.write(file_list)
                f.close()
                msgbox.showinfo('2번 관문 BGM 설정 변경 완료','2번 관문의 BGM 설정이 '+file_name+'으로 변경되었습니다.')

    def num3_btn():
        number3_dir = filedialog.askopenfilename(initialdir='/', title='3번 관문 BGM 파일 선택',filetypes=(("OGG files", "*.ogg"),('all files','*.*')))
        if filedialog.Open():
            dir_name = number3_dir.name
            file_name = number3_dir.name.split('/')[-1]
            q3 = msgbox.askyesno('3번 관문 BGM 설정 알림',file_name+'을 \n3번 설정의 BGM 으로 설정하시겠습니까?')
            if q3 == 1 :
                f = open(exe_path+'/filepath.txt','r',encoding='UTF-8')
                file = f.read().split('\n')
                file_list = '\n'.join(file[:2])+'\n'+file[2].replace(file[2],dir_name)+'\n'+''.join(file[3])
                f.close()
                f = open(exe_path+'/filepath.txt','w',encoding='UTF-8')
                f.write(file_list)
                f.close()
                msgbox.showinfo('3번 관문 BGM 설정 변경 완료','3번 관문의 BGM 설정이 '+file_name+'으로 변경되었습니다.')

    def num4_btn():
        number4_dir = filedialog.askopenfilename(initialdir='/', title='4번 관문 BGM 파일 선택',filetypes=(("OGG files", "*.ogg"),('all files','*.*')))
        if filedialog.Open():
            dir_name = number4_dir.name
            file_name = number4_dir.name.split('/')[-1]
            q4 = msgbox.askyesno('4번 관문 BGM 설정 알림',file_name+'을 \n4번 관문의 BGM 으로 설정하시겠습니까?')
            if q4 == 1 :
                f = open(exe_path+'/filepath.txt','r',encoding='UTF-8')
                file = f.read().split('\n')
                file_list = '\n'.join(file[:3])+'\n'+file[3].replace(file[3],dir_name)
                f.close()
                f = open(exe_path+'/filepath.txt','w',encoding='UTF-8')
                f.write(file_list)
                f.close()
                msgbox.showinfo('4번 관문 BGM 설정 변경 완료','4번 관문의 BGM 설정이 '+file_name+'으로 변경되었습니다.')

    def change1_btn():
        q1 = msgbox.askyesno('1번 관문 BGM 설정 초기화 확인','1번 관문의 BGM 설정을 애국가로 초기화하시겠습니까?')
        if q1 == 1 :
            f = open(exe_path+'/filepath.txt','r',encoding='UTF-8')
            file = f.read().split('\n')
            file_list = 'siroco_broken_d.ogg\n'+'\n'.join(file[1:])
            f.close()
            f = open(exe_path+'/filepath.txt','w',encoding='UTF-8')
            f.write(file_list)
            f.close()
            msgbox.showinfo('1번 관문 BGM 설정 초기화 완료','1번 관문의 BGM 설정이 애국가 1절로 초기화되었습니다.')

    def change2_btn():
        q2 = msgbox.askyesno('2번 관문 BGM 설정 초기화 확인','2번 관문의 BGM 설정을 애국가로 초기화하시겠습니까?')
        if q2 == 1 :
            f = open(exe_path+'/filepath.txt','r',encoding='UTF-8')
            file = f.read().split('\n')
            file_list = ''.join(file[0])+'\n'+'siroco_broken_o1.ogg'+'\n'+'\n'.join(file[2:])
            f.close()
            f = open(exe_path+'/filepath.txt','w',encoding='UTF-8')
            f.write(file_list)
            f.close()
            msgbox.showinfo('2번 관문 BGM 설정 초기화 완료','2번 관문의 BGM 설정이 애국가 2절로 초기화되었습니다.')

    def change3_btn():
        q3 = msgbox.askyesno('3번 관문 BGM 설정 초기화 확인','3번 관문의 BGM 설정을 애국가로 초기화하시겠습니까?')
        if q3 == 1 :
            f = open(exe_path+'/filepath.txt','r',encoding='UTF-8')
            file = f.read().split('\n')
            file_list = '\n'.join(file[:2])+'\n'+'siroco_broken_o2.ogg\n'+''.join(file[3])
            f.close()
            f = open(exe_path+'/filepath.txt','w',encoding='UTF-8')
            f.write(file_list)
            f.close()
            msgbox.showinfo('3번 관문 BGM 설정 초기화 완료','3번관문의 BGM 설정이 애국가 3절로 초기화되었습니다.')

    def change4_btn():
        q4 = msgbox.askyesno('4번 관문 BGM 설정 초기화 확인','4번 관문의 BGM 설정을 애국가로 초기화하시겠습니까?')
        if q4 == 1 :
            f = open(exe_path+'/filepath.txt','r',encoding='UTF-8')
            file = f.read().split('\n')
            file_list = '\n'.join(file[:3])+'\nsiroco_broken_r.ogg'
            f.close()
            f = open(exe_path+'/filepath.txt','w',encoding='UTF-8')
            f.write(file_list)
            f.close()
            msgbox.showinfo('4번 관문 BGM 설정 초기화 완료','4번 관문의 BGM 설정이 애국가 4절로 초기화되었습니다.')

    def all_change_btn():
        with open(exe_path+'/filepath.txt','w',encoding='utf-8') as file:
            file.write('siroco_broken_d.ogg\nsiroco_broken_o1.ogg\nsiroco_broken_o2.ogg\nsiroco_broken_r.ogg')
        msgbox.showinfo('모든 관문 BGM 설정 초기화 완료','모든 관문의 BGM 설정이 초기화 되었습니다.')

    Label(toplevel, text='   ').grid(row=0, column=0)
    Button(toplevel,bg='White', width=10, height=2, text='모두 초기화',command=all_change_btn).grid(row=1, column=2)
    Button(toplevel,bg='White', width=10, height=2, text='1번 바꾸기' ,command=num1_btn).grid(row=2, column=1)
    Button(toplevel,bg='White', width=10, height=2, text='2번 바꾸기' ,command=num2_btn).grid(row=3, column=1)
    Button(toplevel,bg='White', width=10, height=2, text='3번 바꾸기' ,command=num3_btn).grid(row=4, column=1)
    Button(toplevel,bg='White', width=10, height=2, text='4번 바꾸기' ,command=num4_btn).grid(row=5, column=1)
    Button(toplevel,bg='White', width=10, height=2, text='1번 초기화' ,command=change1_btn).grid(row=2, column=3)
    Button(toplevel,bg='White', width=10, height=2, text='2번 초기화' ,command=change2_btn).grid(row=3, column=3)
    Button(toplevel,bg='White', width=10, height=2, text='3번 초기화' ,command=change3_btn).grid(row=4, column=3)
    Button(toplevel,bg='White', width=10, height=2, text='4번 초기화' ,command=change4_btn).grid(row=5, column=3)

menu = Menu(root)
menu_update = Menu(menu, tearoff=0, relief='groove')
menu_update.add_command(label="던파 설치 경로 확인", command=install_btn)
menu_update.add_command(label="관문 BGM 설정 변경", command=change_btn)
menu_update.add_separator()
menu_update.add_command(label="현재 버전 확인", command=version_btn)
menu_update.add_command(label="업데이트 로그", command=update_log)
menu_chat = Menu(menu, tearoff=0, relief='groove')
menu_chat.add_command(label="오류 및 건의사항", command=link_btn)
menu.add_cascade(label="정보", menu=menu_update)
menu.add_cascade(label="소통", menu=menu_chat)
root.config(menu=menu)

abs_path = DNF_path+'/Music'

def read_all_file(path):
    output = os.listdir(path)
    file_list = []
    for i in output:
        if os.path.isdir(path+"/"+i):
            file_list.extend(read_all_file(path+"/"+i))
        elif os.path.isfile(path+"/"+i):
            file_list.append(path+"/"+i)
    return file_list

def copy_all_file(file_list, abs_path):
    for src_path in file_list:
        file = src_path.split("/")[-1]
        shutil.copyfile(src_path, abs_path+"/"+file)

def apply_btn_cmd():
    exist = []
    for q in psutil.process_iter():
        if 'DNF.exe' in q.name():
            exist = exist+['exist']
        elif 'DNF.exe' not in q.name():
            exist = exist+['no']
        else:
            exist = exist+['error']
    if 'exist' in exist:
        f = open(exe_path+'/filepath.txt','r',encoding='UTF-8')
        file_list = f.read().split('\n')
        original = ['siroco_broken_d.ogg','siroco_broken_o1.ogg','siroco_broken_o2.ogg','siroco_broken_r.ogg']
        for file in file_list:
            num = file_list.index(file)
            if original[num] != file:
                shutil.copyfile(file,abs_path+'/'+original[num])
            elif original[num] == file:
                shutil.copyfile(exe_path+'/After/'+file,abs_path+'/'+original[num])
            else:
                msgbox.showinfo('파일 복사 오류','관리자에게 "파일 복사 오류"라고 전달해주세요.')
        msgbox.showinfo("알림", "관문 BGM 파일 적용 완료")
    elif 'error' in exist:
        msgbox.showerror('적용하기 오류', '관리자에게 "적용하기 오류"라고 전달해주세요.')
    else:
        msgbox.showwarning('던파 미실행','던파 미실행 상태에서 적용시 적용이 불가능합니다.')

def return_btn_cmd():
    file_list = read_all_file(exe_path+'/Before')
    copy_all_file(file_list, abs_path)
    msgbox.showinfo("알림", "관문 BGM 원본 파일 적용 완료")

btn1 = Button(root, bg='White', width=10, height=2, text="적용하기",relief='groove', command=apply_btn_cmd)
btn1.place(x=10, y=15)
btn2 = Button(root, bg='white', width=10, height=2, text="되돌리기",relief='groove', command=return_btn_cmd)
btn2.place(x=100, y=15)
root.mainloop()
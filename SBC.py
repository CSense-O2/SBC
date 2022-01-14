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

현재버전 = 'v4.6.2'

real_path = os.getcwd()
exe_path = real_path.replace('\\', '/')
backup_path = os.path.expanduser('~')+'/Desktop/SBC_backup/filepath.txt'
for drive in list(ascii_uppercase):
    for (path, dir, files) in os.walk(drive+':/'):
        if 'DNF.exe' in files:
            DNF_path = path.replace('\\', '/')
            break
abs_path = DNF_path+'/Music'

with open(exe_path+'/MainFolder/다시보지않기.txt', 'r', encoding='utf-8') as file:
    read = file.read()

url = 'https://github.com/CSense-O2/SBC/releases/latest'

response = get(url)

download_list = []

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    try:
        최신버전 = soup.select_one('#repo-content-pjax-container > div > div > div.Box-body > div.d-flex.flex-row.mb-3 > div.flex-1 > h1').get_text()
        updatelog = soup.select_one('#repo-content-pjax-container > div > div > div.Box-body > div.markdown-body.my-3 > p').get_text()
        patchnote = """
### """+현재버전+""" 업데이트 안내 ###

"""+updatelog+'\n'
    except AttributeError:
        msgbox.showinfo('최신버전 확인 오류', '최신 버전 확인에 오류가 발생했습니다.\r홈페이지를 확인해주세요.')
        webbrowser.open('https://github.com/CSense-O2/SBC/labels/Error')
        sys.exit(0)
    if 최신버전 > 현재버전:
        q1 = msgbox.askquestion(
            '최신 버전 발견', '최신 버전 다운로드를 위해 링크가 열립니다.\n커스텀 브금 파일을 백업하시겠습니까?')
        if q1 == 'yes':
            shutil.copyfile(exe_path+'/MainFolder/filepath.txt', backup_path)
        msgbox.showinfo('최신 버전 발견', '최신 버전 다운로드를 위해 링크가 열립니다.')
        webbrowser.open('https://github.com/CSense-O2/SBC')
        sys.exit(0)
    elif 최신버전 <= 현재버전:
        pass
    else:
        msgbox.showerror('버전 확인 오류', '관리자에게 "버전 확인 오류"라고 전달해주세요.')
        webbrowser.open('https://github.com/CSense-O2/SBC/labels/Error')
elif response.status_code == 404:
    msgbox.showinfo('현재 점검중입니다.', '현재 점검중이니 관리자에게 문의해주세요.')
    webbrowser.open('https://github.com/CSense-O2/SBC/labels/Error')
else:
    msgbox.showerror("파싱 오류", 'response : ' +
                     response.status_code+"\n해당 오류 코드를 관리자에게 전달해 주세요.")
    webbrowser.open('https://github.com/CSense-O2/SBC/labels/Error')

root = Tk()
root.title("SBC")
w = 200
h = 100
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws-w)/2
y = (hs-h)/2
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.resizable(False, False)
root.iconbitmap(exe_path+'/MainFolder/icon.ico')

if '다시보지않기' not in read:
    toplevel = Toplevel(root)
    toplevel.title('업데이트 내역')
    toplevel.geometry('+%d+%d' % (x, y))
    toplevel.iconbitmap(exe_path+'/MainFolder/icon.ico')
    toplevel.wm_attributes("-topmost", 1)
    Label(toplevel, text=patchnote).pack(padx=10, pady=5)

    def 다시보지않기():
        with open(exe_path+'/MainFolder/다시보지않기.txt', 'w', encoding='UTF-8') as file:
            file.write('다시보지않기')
        toplevel.destroy()
    Button(toplevel, text='다시보지않기', command=다시보지않기).pack(padx=10, pady=5)


def link_btn():
    webbrowser.open('https://github.com/CSense-O2/SBC/labels')


def update_log():
    msgbox.showinfo("업데이트 내용 확인", patchnote)


def install_btn():
    msgbox.showinfo("던파 설치 경로", DNF_path)


def version_btn():
    msgbox.showinfo("현재 버전", '[ '+현재버전+' ]')


def change_btn():
    toplevel = Toplevel(root)
    toplevel.title('관문 BGM 설정 변경')
    w = 285
    h = 250
    ws = toplevel.winfo_screenwidth()
    hs = toplevel.winfo_screenheight()
    x = (ws-w)/2
    y = (hs-h)/2
    toplevel.geometry('%dx%d+%d+%d' % (w, h, x, y))
    toplevel.iconbitmap(exe_path+'/MainFolder/icon.ico')
    def change_btn(number):
        number_dir = filedialog.askopenfile(
            initialdir="/", title=number+"번 관문 BGM 파일 선택", filetypes=(("OGG files", "*.ogg"), ("all files", "*.*")))
        if filedialog.Open():
            dir_name = number_dir.name
            file_name = number_dir.name.split('/')[-1]
            q2 = msgbox.askquestion(
                number+"번 관문 BGM 설정 알림", file_name+'을 \n'+number+'번 관문의 BGM 파일로 설정하시겠습니까?')
            if q2 == 'yes':
                with open(exe_path+'/MainFolder/filepath.txt', 'r', encoding='UTF-8') as f:
                    file = f.read().split('\n')
                if number == '1':
                    file_list = file[0].replace(file[0], dir_name)+'\n'+'\n'.join(file[1:])
                elif number == '2':
                    file_list = ''.join(file[0])+'\n'+file[1].replace(file[1], dir_name)+'\n'+'\n'.join(file[2:])
                elif number == '3':
                    file_list = '\n'.join(file[:2])+'\n'+file[2].replace(file[2], dir_name)+'\n'+''.join(file[3])
                elif number == '4':
                    file_list = '\n'.join(file[:3])+'\n'+file[3].replace(file[3], dir_name)
                else:
                    msgbox.showerror("관문 번호 로딩 오류", '관리자에게 "관문 번호 로딩 오류" 라고 전달해주세요')
                with open(exe_path+'/MainFolder/filepath.txt', 'w', encoding='UTF-8') as file:
                    file.write(file_list)
                msgbox.showinfo(number+'번 관문 BGM 설정 변경 완료', number +'번 관문의 BGM 파일 설정이 '+file_name+'으로 변경되었습니다.')
    def reset_btn(number):
        q3 = msgbox.askquestion(number+'번 관문 BMG 설정 초기화 확인',number+'번 관문의 BGM 파일 설정을 애국가로 초기화하시겠습니까?')
        if q3 == 'yes':
            with open(exe_path+'/MainFolder/filepath.txt', 'r', encoding='UTF-8') as f:
                file = f.read().split('\n')
            if number == '1':
                file_list = 'siroco_broken_d.ogg\n'+'\n'.join(file[1:])
            elif number == '2':
                file_list = ''.join(file[0])+'\n'+'siroco_broken_o1.ogg'+'\n'+'\n'.join(file[2:])
            elif number == '3':
                file_list = '\n'.join(file[:2])+'\n'+'siroco_broken_o2.ogg\n'+''.join(file[3])
            elif number == '4':
                file_list = '\n'.join(file[:3])+'\nsiroco_broken_r.ogg'
                with open(exe_path+'/MainFolder/filepath.txt', 'w', encoding='UTF-8') as f:
                    f.write(file_list)
            else:
                msgbox.showerror("관문 번호 로딩 오류", '관리자에게 "관문 번호 로딩 오류" 라고 전달해주세요')
                webbrowser.open('http://pf.kakao.com/_laxars/chat')
            msgbox.showinfo(number+'번 관문 BMG 파일 설정 초기화 완료',number+'번 관문의 BGM 파일 설정이 애국가로 초기화 되었습니다.')
    def all_change_btn():
        with open(exe_path+'/MainFolder/filepath.txt', 'w', encoding='utf-8') as file:
            file.write('siroco_broken_d.ogg\nsiroco_broken_o1.ogg\nsiroco_broken_o2.ogg\nsiroco_broken_r.ogg')
        msgbox.showinfo('모든 관문 BGM 설정 초기화 완료', '모든 관문의 BGM 설정이 초기화 되었습니다.')
    Label(toplevel, text='   ').grid(row=0, column=0)
    Button(toplevel, bg='White', width=10, height=2, text='모두 초기화', command=all_change_btn).grid(row=1, column=2)
    Button(toplevel, bg='White', width=10, height=2, text='1번 바꾸기', command=lambda: change_btn('1')).grid(row=2, column=1)
    Button(toplevel, bg='White', width=10, height=2, text='2번 바꾸기', command=lambda: change_btn('2')).grid(row=3, column=1)
    Button(toplevel, bg='White', width=10, height=2, text='3번 바꾸기', command=lambda: change_btn('3')).grid(row=4, column=1)
    Button(toplevel, bg='White', width=10, height=2, text='4번 바꾸기', command=lambda: change_btn('4')).grid(row=5, column=1)
    Button(toplevel, bg='White', width=10, height=2, text='1번 초기화', command=lambda: reset_btn('1')).grid(row=2, column=3)
    Button(toplevel, bg='White', width=10, height=2, text='2번 초기화', command=lambda: reset_btn('2')).grid(row=3, column=3)
    Button(toplevel, bg='White', width=10, height=2, text='3번 초기화', command=lambda: reset_btn('3')).grid(row=4, column=3)
    Button(toplevel, bg='White', width=10, height=2, text='4번 초기화', command=lambda: reset_btn('4')).grid(row=5, column=3)

def up_btn():
    toplevel = Toplevel(root)
    toplevel.title('항상 맨 위로 설정')
    w = 200
    h = 100
    ws = toplevel.winfo_screenwidth()
    hs = toplevel.winfo_screenheight()
    x = (ws-w)/2
    y = (hs-h)/2
    toplevel.geometry('%dx%d+%d+%d' % (w, h, x, y))
    toplevel.iconbitmap(exe_path+'/MainFolder/icon.ico')
    def up():
        if chk1.get() == 1:
            root.wm_attributes("-topmost", 1)
        else:
            root.wm_attributes("-topmost", 0)
    chk1 = IntVar()
    chk1_btn = Checkbutton(toplevel, text="항상 맨 위로", variable=chk1, bg='white', command=up)
    chk1_btn.pack(pady=5)

def transparency_btn():
    toplevel = Toplevel(root)
    toplevel.title('투명도 설정')
    w = 200
    h = 100
    ws = toplevel.winfo_screenwidth()
    hs = toplevel.winfo_screenheight()
    x = (ws-w)/2
    y = (hs-h)/2
    toplevel.geometry('%dx%d+%d+%d' % (w, h, x, y))
    toplevel.iconbitmap(exe_path+'/MainFolder/icon.ico')
    def slide(_):
        root.attributes('-alpha', slide_bar.get())
    slide_bar = Scale(toplevel, from_=0.1, to=1.0, resolution=0.01, label='투명도', orient=HORIZONTAL, showvalue=FALSE, relief='groove', sliderlength=20, sliderrelief='groove', command=slide)
    slide_bar.pack(pady=5)

def restore_btn():
    if os.path.isfile(backup_path):
        q4 = msgbox.askquestion('파일 경로 복원', '브금 파일들의 경로를 복원하시겠습니까?')
        if q4 == 'yes':
            shutil.copyfile(backup_path, exe_path+'/MainFolder/filepath.txt')

def backup_btn():
    if os.path.isfile(backup_path):
        q5 = msgbox.askquestion(
            '파일 복원 확인', '해당 경로에 복원파일이 이미 존재합니다.\n파일을 덮어쓰시겠습니까?')
        if q5 == 'yes':
            shutil.copyfile(exe_path+'/MainFolder/filepath.txt', backup_path)

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
        f = open(exe_path+'/MainFolder/filepath.txt', 'r', encoding='UTF-8')
        file_list = f.read().split('\n')
        original = ['siroco_broken_d.ogg','siroco_broken_o1.ogg','siroco_broken_o2.ogg','siroco_broken_r.ogg']
        for file in file_list:
            num = file_list.index(file)
            if original[num] != file:
                shutil.copyfile(file,abs_path+'/'+original[num])
            elif original[num] == file:
                shutil.copyfile(exe_path+'/After/'+file,abs_path+'/'+original[num])
            else:
                msgbox.showinfo('파일 복사 오류', '관리자에게 "파일 복사 오류"라고 전달해주세요.')
                webbrowser.open('https://github.com/CSense-O2/SBC/labels/Error')
        msgbox.showinfo("알림", "관문 BGM 파일 적용 완료")
    elif 'error' in exist:
        msgbox.showerror('적용하기 오류', '관리자에게 "적용하기 오류"라고 전달해주세요.')
        webbrowser.open('https://github.com/CSense-O2/SBC/labels/Error')
    else:
        msgbox.showwarning('던파 미실행', '던파 미실행 상태에서 적용시 적용이 불가능합니다.')

def return_btn_cmd():
    file_list = read_all_file(exe_path+'/Before')
    copy_all_file(file_list, abs_path)
    msgbox.showinfo("알림", "관문 BGM 원본 파일 적용 완료")

menu = Menu(root)
menu_update = Menu(menu, tearoff=0, relief='groove')
menu_update.add_command(label="던파 설치 경로 확인", command=install_btn)
menu_update.add_command(label="관문 BGM 설정 변경", command=change_btn)
menu_update.add_separator()
menu_update.add_command(label="현재 버전 확인", command=version_btn)
menu_update.add_command(label="업데이트 로그", command=update_log)
menu_chat = Menu(menu, tearoff=0, relief='groove')
menu_chat.add_command(label="오류 및 건의사항", command=link_btn)
menu_func = Menu(menu, tearoff=0, relief='groove')
menu_func.add_command(label="항상 맨 위로", command=up_btn)
menu_func.add_command(label="투명도 설정", command=transparency_btn)
menu_func.add_command(label="파일 경로 백업", command=backup_btn)
menu_func.add_command(label="파일 경로 복원", command=restore_btn)
menu.add_cascade(label="정보", menu=menu_update)
menu.add_cascade(label="소통", menu=menu_chat)
menu.add_cascade(label="기능", menu=menu_func)
root.config(menu=menu)
btn1 = Button(root, bg='White', width=10, height=2, text="적용하기", relief='groove', command=apply_btn_cmd)
btn1.place(x=10, y=15)
btn2 = Button(root, bg='white', width=10, height=2, text="되돌리기", relief='groove', command=return_btn_cmd)
btn2.place(x=100, y=15)
root.mainloop()
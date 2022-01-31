# -*- Encoding:UTF-8 -*- #
### 코드를 무단으로 복제,개조 및 배포하지 말 것 ###
### Copyright ⓒ 2021-2022 c-closed / 감는 my______baby@naver.com ###
import SBC_info
import SBC_GUI
import SBC_update
import webbrowser
import tkinter.messagebox as msgbox
from tkinter import filedialog
from tkinter import *
import shutil
import sys
import os
from distutils.dir_util import copy_tree
import psutil

def donotseeagain():
    with open(SBC_info.exe_path+'/MainFolder/다시보지않기.txt', 'r', encoding='UTF-8') as file:
        read = file.read()
    if '다시보지않기' not in read:
        toplevel = Toplevel(SBC_GUI.root)
        toplevel.title('업데이트 내역')
        toplevel.geometry('+%d+%d' % (SBC_GUI.x, SBC_GUI.y))
        toplevel.iconbitmap(SBC_info.exe_path+'/MainFolder/icon.ico')
        toplevel.wm_attributes("-topmost", 1)
        Label(toplevel, text=SBC_update.patchnote).pack(padx=10, pady=5)
        def 다시보지않기():
            with open(SBC_info.exe_path+'/MainFolder/다시보지않기.txt', 'w', encoding='UTF-8') as file:
                file.write('다시보지않기')
            toplevel.destroy()
        Button(toplevel, text='다시보지않기', command=다시보지않기).pack(padx=10, pady=5)


def link_btn():
    webbrowser.open('http://bit.do/SBC-homepage')

def update_log():
    msgbox.showinfo("업데이트 내용 확인", SBC_update.patchnote)

def install_btn():
    msgbox.showinfo("던파 설치 경로", SBC_info.DNF_path)

def version_btn():
    msgbox.showinfo("현재 버전", '[ '+SBC_info.current_version+' ]')

def change_btn():
    toplevel = Toplevel(SBC_GUI.root)
    toplevel.title('관문 BGM 설정 변경')
    w = 285
    h = 250
    ws = toplevel.winfo_screenwidth()
    hs = toplevel.winfo_screenheight()
    x = (ws-w)/2
    y = (hs-h)/2
    toplevel.geometry('%dx%d+%d+%d' % (w, h, x, y))
    toplevel.iconbitmap(SBC_info.exe_path+'/MainFolder/icon.ico')
    def change_btn(number):
        number_dir = filedialog.askopenfile(initialdir="/", title=number+"번 관문 BGM 파일 선택", filetypes=(("OGG files", "*.ogg"), ("all files", "*.*")))
        file_name = number_dir.name.split('/')[-1]
        with open(SBC_info.exe_path+'/MainFolder/filepath.txt','r',encoding='UTF-8') as f:
            file_path = f.read()
        current_file_name = file_path.split('\n')[int(number)-1]
        change_question = msgbox.askquestion(number+"번 관문 BGM 설정 알림", '현재 '+number+'번 관문의 BGM 파일은 '+current_file_name+'입니다.\n'+file_name+'으로 변경하시겠습니까?')
        if change_question == 'yes':
            file_path.replace(current_file_name,file_name)
            if number == '1':
                shutil.copyfile(file_path,SBC_info.exe_path+'/After/siroco_broken_d.ogg')
            elif number == '2':
                shutil.copyfile(file_path,SBC_info.exe_path+'/After/siroco_broken_o1.ogg')
            elif number == '3':
                shutil.copyfile(file_path,SBC_info.exe_path+'/After/siroco_broken_o2.ogg')
            elif number == '4':
                shutil.copyfile(file_path,SBC_info.exe_path+'/After/siroco_broken_r.ogg')
            else:
                msgbox.showerror('관문 번호 오류','관리자에게 "관문 번호 오류" 라고 전달해주세요.')
                webbrowser.open('http://bit.do/SBC-homepage')
                sys.exit(0)
        with open(SBC_info.exe_path+'/MainFloder/filepath.txt','w',encoding='UTF-8') as f:
            f.write(file_path)
        msgbox.showinfo(number+'번 관문 BGM 설정 변경 완료', number +'번 관문의 BGM 파일 설정이 '+file_name+'으로 변경되었습니다.')
    def reset_btn(number):
        q3 = msgbox.askquestion(number+'번 관문 BMG 설정 초기화 확인',number+'번 관문의 BGM 파일 설정을 애국가로 초기화하시겠습니까?')
        if q3 == 'yes':
            with open(SBC_info.exe_path+'/MainFolder/filepath.txt', 'r', encoding='UTF-8') as f:
                file = f.read()
            file.replace(file.split('\n')[int(number)-1],'애국가')
            with open(SBC_info.exe_path+'/MainFolder/filepath.txt', 'w', encoding='UTF-8') as f:
                f.write(file)
            if number == '1':
                shutil.copyfile(SBC_info.exe_path+'/Backup/siroco_broken_d.ogg',SBC_info.exe_path+'/After/siroco_broken_d.ogg')
            elif number == '2':
                shutil.copyfile(SBC_info.exe_path+'/Backup/siroco_broken_o1.ogg',SBC_info.exe_path+'/After/siroco_broken_o1.ogg')
            elif number == '3':
                shutil.copyfile(SBC_info.exe_path+'/Backup/siroco_broken_o2.ogg',SBC_info.exe_path+'/After/siroco_broken_o2.ogg')
            elif number == '4':
                shutil.copyfile(SBC_info.exe_path+'/Backup/siroco_broken_r.ogg',SBC_info.exe_path+'/After/siroco_broken_r.ogg')
            else:
                msgbox.showerror('관문 번호 오류','관리자에게 "관문 번호 오류" 라고 전달해주세요.')
                webbrowser.open('http://bit.do/SBC-homepage')
                sys.exit(0)
            msgbox.showinfo(number+'번 관문 BMG 파일 설정 초기화 완료',number+'번 관문의 BGM 파일 설정이 애국가로 초기화 되었습니다.')
    def all_change_btn():
        with open(SBC_info.exe_path+'/MainFolder/filepath.txt', 'w', encoding='utf-8') as file:
            file.write('애국가\n애국가\n애국가\n애국가')
        copy_tree(SBC_info.exe_path+'/Backup',SBC_info.exe_path+'/After')
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

def check_btn():
    with open(SBC_info.exe_path+'/MainFolder/filepath.txt','r',encoding='UTF-8') as f:
        file = f.read()
    msgbox.showinfo('BGM 파일 설정 확인','현재 설정된 BGM 파일은 다음과 같습니다.\n1번 관문 : '+file.split('\n')[0]+'\n2번 관문 : '+file.split('\n')[1]+'\n3번 관문 : '+file.split('\n')[2]+'\n4번 관문 : '+file.split('\n')[3])

def up_btn():
    toplevel = Toplevel(SBC_GUI.root)
    toplevel.title('항상 맨 위로 설정')
    w = 200
    h = 100
    ws = toplevel.winfo_screenwidth()
    hs = toplevel.winfo_screenheight()
    x = (ws-w)/2
    y = (hs-h)/2
    toplevel.geometry('%dx%d+%d+%d' % (w, h, x, y))
    toplevel.iconbitmap(SBC_info.exe_path+'/MainFolder/icon.ico')
    def up():
        if chk1.get() == 1:
            SBC_GUI.root.wm_attributes("-topmost", 1)
        else:
            SBC_GUI.root.wm_attributes("-topmost", 0)
    chk1 = IntVar()
    chk1_btn = Checkbutton(toplevel, text="항상 맨 위로", variable=chk1, bg='white', command=up)
    chk1_btn.pack(pady=5)

def transparency_btn():
    toplevel = Toplevel(SBC_GUI.root)
    toplevel.title('투명도 설정')
    w = 200
    h = 100
    ws = toplevel.winfo_screenwidth()
    hs = toplevel.winfo_screenheight()
    x = (ws-w)/2
    y = (hs-h)/2
    toplevel.geometry('%dx%d+%d+%d' % (w, h, x, y))
    toplevel.iconbitmap(SBC_info.exe_path+'/MainFolder/icon.ico')
    def slide(_):
        SBC_GUI.root.attributes('-alpha', slide_bar.get())
    slide_bar = Scale(toplevel, from_=0.1, to=1.0, resolution=0.01, label='투명도', orient=HORIZONTAL, showvalue=FALSE, relief='groove', sliderlength=20, sliderrelief='groove', command=slide)
    slide_bar.pack(pady=5)

def restore_btn():
    if os.path.isdir(SBC_info.backup_path):
        q4 = msgbox.askquestion('파일 경로 복원', '브금 파일들을 복원하시겠습니까?')
        if q4 == 'yes':
            shutil.copyfile(SBC_info.backup_path+'/filepath.txt', SBC_info.exe_path+'/MainFolder/filepath.txt')
            copy_tree(SBC_info.backup_path+'/After',SBC_info.exe_path+'/After')
    else:
        msgbox.showerror('파일 복원 실패','백업 파일들이 존재하지 않습니다')

def backup_btn():
    if os.path.isdir(SBC_info.backup_path):
        q5 = msgbox.askquestion(
            '파일 복원 확인', '해당 경로에 복원파일이 이미 존재합니다.\n파일을 덮어쓰시겠습니까?')
        if q5 == 'yes':
            shutil.copyfile(SBC_info.exe_path+'/MainFolder/filepath.txt', SBC_info.backup_path+'/filepath.txt')
            copy_tree(SBC_info.exe_path+'/After',SBC_info.backup_path+'/After')
    else:
        os.mkdir(SBC_info.backup_path)
        shutil.copyfile(SBC_info.exe_path+'/MainFolder/filepath.txt', SBC_info.backup_path+'/filepath.txt')
        copy_tree(SBC_info.exe_path+'/After',SBC_info.backup_path+'/After')

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
        try:
            copy_tree(SBC_info.exe_path+'/After',SBC_info.abs_path)
            msgbox.showinfo("알림", "관문 BGM 파일 적용 완료")
        except:
            msgbox.showerror('파일 복사 오류','관리자에게 "파일 복사 오류"라고 전달해주세요.')
            webbrowser.open('http://bit.do/SBC-homepage')
    elif 'error' in exist:
        msgbox.showerror('적용하기 오류', '관리자에게 "적용하기 오류"라고 전달해주세요.')
        webbrowser.open('http://bit.do/SBC-homepage')
    else:
        msgbox.showwarning('던파 미실행', '던파 미실행 상태에서 적용시 적용이 불가능합니다.')

def return_btn_cmd():
    file_list = read_all_file(SBC_info.exe_path+'/Before')
    copy_all_file(file_list, SBC_info.abs_path)
    msgbox.showinfo("알림", "관문 BGM 원본 파일 적용 완료")

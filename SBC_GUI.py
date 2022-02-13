# -*- Encoding:UTF-8 -*- #
### 코드를 무단으로 복제,개조 및 배포하지 말 것 ###
### Copyright ⓒ 2021-2022 c-closed / 감는 c-closed@naver.com ###
from tkinter import *
import SBC_info
import SBC_func as func

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
root.iconbitmap(SBC_info.exe_path+'/MainFolder/icon.ico')

menu = Menu(root)
menu_update = Menu(menu, tearoff=0, relief='groove')
menu_update.add_command(label="던파 설치 경로 확인", command=func.install_btn)
menu_update.add_command(label="관문 BGM 설정 변경", command=func.change_btn)
menu_update.add_command(label="관문 BGM 확인", command=func.check_btn)
menu_update.add_separator()
menu_update.add_command(label="현재 버전 확인", command=func.version_btn)
menu_update.add_command(label="업데이트 로그", command=func.update_log)
menu_chat = Menu(menu, tearoff=0, relief='groove')
menu_chat.add_command(label="오류 및 건의사항", command=func.open_homepage)
menu_func = Menu(menu, tearoff=0, relief='groove')
menu_func.add_command(label="항상 맨 위로", command=func.up_btn)
menu_func.add_command(label="투명도 설정", command=func.transparency_btn)
menu_func.add_command(label="파일 경로 백업", command=func.backup_btn)
menu_func.add_command(label="파일 경로 복원", command=func.restore_btn)
menu.add_cascade(label="정보", menu=menu_update)
menu.add_cascade(label="소통", menu=menu_chat)
menu.add_cascade(label="기능", menu=menu_func)
root.config(menu=menu)
btn1 = Button(root, bg='White', width=9, height=2, text="적용하기", relief='groove', command=func.apply_btn_cmd)
btn1.place(x=10, y=15)
btn2 = Button(root, bg='white', width=9, height=2, text="되돌리기", relief='groove', command=func.return_btn_cmd)
btn2.place(x=100, y=15)

root.mainloop()
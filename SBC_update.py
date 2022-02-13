# -*- Encoding:UTF-8 -*- #
### 코드를 무단으로 복제,개조 및 배포하지 말 것 ###
### Copyright ⓒ 2021-2022 c-closed / 감는 my______baby@naver.com ###
from requests import get
import tkinter.messagebox as msgbox
import webbrowser
import sys
import SBC_info
import SBC_func

response = get(SBC_info.update_check_url)
if response.status_code == 200:
    latest_version = response.json()["name"]
    updatelog = response.json()["body"]
    patchnote = "\n### "+SBC_info.current_version+" 업데이트 안내 ###\n\n"+updatelog+'\n'
elif response.status_code == 404:
    msgbox.showinfo('현재 점검중입니다.', '현재 점검중이니 관리자에게 문의해주세요.')
    SBC_func.open_homepage
    sys.exit(0)
else:
    msgbox.showerror("파싱 오류", 'response : ' +response.status_code+"\n해당 오류 코드를 관리자에게 전달해 주세요.")
    SBC_func.open_homepage
    sys.exit(0)
    
if latest_version[1:6] > SBC_info.current_version[1:6]:
    msgbox.showinfo('최신 버전 발견', '최신 버전 다운로드를 위해 링크가 열립니다.')
    SBC_func.open_homepage
    sys.exit(0)
elif latest_version[1:6] <= SBC_info.current_version[1:6]:
    pass
else:
    msgbox.showerror('버전 확인 오류', '관리자에게 "버전 확인 오류"라고 전달해주세요.')
    SBC_func.open_homepage
    sys.exit(0)
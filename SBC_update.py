# -*- Encoding:UTF-8 -*- #
### 코드를 무단으로 복제,개조 및 배포하지 말 것 ###
### Copyright ⓒ 2021-2022 c-closed / 감는 my______baby@naver.com ###
from bs4 import BeautifulSoup
from requests import get
import tkinter.messagebox as msgbox
import webbrowser
import sys
import SBC_info

response = get(SBC_info.latest_release_url)
if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    try:
        latest_version = soup.select_one('#repo-content-pjax-container > div > div > div.Box-body > div.d-flex.flex-row.mb-3 > div.flex-1 > h1').get_text()
        updatelog = soup.select_one('#repo-content-pjax-container > div > div > div.Box-body > div.markdown-body.my-3 > p').get_text()
        patchnote = "\n### "+SBC_info.current_version+" 업데이트 안내 ###\n\n"+updatelog+'\n'
    except AttributeError:
        msgbox.showinfo('최신버전 확인 오류', '최신 버전 확인에 오류가 발생했습니다.\r홈페이지를 확인해주세요.')
        webbrowser.open(SBC_info.homepage_url)
        sys.exit(0)
    if latest_version > SBC_info.current_version:
        msgbox.showinfo('최신 버전 발견', '최신 버전 다운로드를 위해 링크가 열립니다.')
        webbrowser.open(SBC_info.homepage_url)
        sys.exit(0)
    elif latest_version <= SBC_info.current_version:
        pass
    else:
        msgbox.showerror('버전 확인 오류', '관리자에게 "버전 확인 오류"라고 전달해주세요.')
        webbrowser.open(SBC_info.homepage_url)
        sys.exit(0)
elif response.status_code == 404:
    msgbox.showinfo('현재 점검중입니다.', '현재 점검중이니 관리자에게 문의해주세요.')
    webbrowser.open(SBC_info.homepage_url)
    sys.exit(0)
else:
    msgbox.showerror("파싱 오류", 'response : ' +response.status_code+"\n해당 오류 코드를 관리자에게 전달해 주세요.")
    webbrowser.open(SBC_info.homepage_url)
    sys.exit(0)
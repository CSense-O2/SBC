# -*- Encoding:UTF-8 -*- #
### 코드를 무단으로 복제,개조 및 배포하지 말 것 ###
### Copyright ⓒ 2021-2022 c-closed / 감는 my______baby@naver.com ###
import os
from string import ascii_uppercase

current_version = 'v4.7.2'
homepage_url = 'http://bit.do/SBC-homepage'
latest_release_url = 'http://bit.do/SBC-releases-latest'
real_path = os.getcwd()
exe_path = real_path.replace('\\', '/')
backup_path = os.path.expanduser('~')+'/Desktop/SBC_backup'
for drive in list(ascii_uppercase):
    for (path, dir, files) in os.walk(drive+':/'):
        if 'DNF.exe' in files:
            DNF_path = path.replace('\\', '/')
            break
abs_path = DNF_path+'/Music'
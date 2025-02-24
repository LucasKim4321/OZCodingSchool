# mkdir 폴더명
# cd 폴더 경로
# code .

# code 명령어 셋팅
# macOS/리눅스: VS Code를 열고 Command Palette(⇧⌘P 또는 Ctrl+Shift+P)를 열어 
# Shell Command: Install 'code' command in PATH를 실행합니다.

# Windows: 설치할 때 "PATH에 추가" 옵션을 선택하지 않았을 수 있습니다.
# 만약 옵션을 선택하지 않았다면, VS Code 설치 폴더(예: C:\Program Files\Microsoft VS Code\bin)의 경로를 수동으로 PATH에 추가해보세요.

# venv 모듈 (파이썬 기본 내장 모듈)

# python3 -m venv .venv

from flask import Flask
app = Flask(__name__)
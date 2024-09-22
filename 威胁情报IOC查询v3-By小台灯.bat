@echo off
pyinstaller -w -F  -i win11.ico 威胁情报IOC查询v3-By小台灯.py --noconsole
pause
#pyinstaller -w -F -i tb.ico 告警IP自动查询V1_By小台灯.py
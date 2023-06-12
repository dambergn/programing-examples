# Windows Batch Files
*.bat  
- https://www.tutorialspoint.com/batch_script/batch_script_quick_guide.htm

At top of file put <@echo off> to prevent terminal from showing command being run for fucntion.
At bottom of file put <pause> to prevent terminal from closing on completion.

## Windows Version
10.0   Windows 10
6.3   Windows Server 2012
6.3   Windows 8.1   /!\
6.2   Windows 8   /!\
6.1   Windows 7   /!\
6.0   Windows Vista
5.2   Windows XP x64
5.1   Windows XP
5.0   Windows 2000
4.10   Windows 98
```bat
@echo off
setlocal
for /f "tokens=4-5 delims=. " %%i in ('ver') do set VERSION=%%i.%%j
if "%version%" == "10.0" echo Windows 10
if "%version%" == "6.3" echo Windows 8.1
if "%version%" == "6.2" echo Windows 8.
if "%version%" == "6.1" echo Windows 7.
if "%version%" == "6.0" echo Windows Vista.
rem etc etc
endlocal
```
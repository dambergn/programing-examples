@echo off
:: -------------------------------------
:: Check Windows Version
:: 4.1 = Win98
:: 5.0 = W2K
:: 5.1 = XP
:: 5.2 = Server 2K3
:: 6.0 = Vista or Server 2K8
:: 6.1 = Win7 or Server 2K8R2
:: 6.2 = Win8 or Server 2K12
:: 6.3 = Win8.1 or Server 2K12R2
:: 10.0 = Windows 10 & 11
:: 0.0 = Unknown or Unable to determine
:: --------------------------------------
setlocal
for /f "tokens=4-5 delims=. " %%i in ('ver') do set VERSION=%%i.%%j
if "%version%" == "10.0" echo Windows 10
if "%version%" == "6.3" echo Windows 8.1
if "%version%" == "6.2" echo Windows 8.
if "%version%" == "6.1" echo Windows 7.
if "%version%" == "6.0" echo Windows Vista.
rem etc etc
endlocal
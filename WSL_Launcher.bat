FOR /F "tokens=1" %%i IN ('usbipd wsl list ^| findstr /c:"LimeSDR-USB"') DO SET VARIABLE=%%i

wt -p "Ubuntu-20.04" ; new-tab -p "Command Prompt" cmd /k "usbipd wsl list & usbipd wsl attach --busid %VARIABLE%"
::wt -p "Ubuntu-20.04" ; new-tab -p "Command Prompt" cmd /k "usbipd wsl list & usbipd wsl attach --busid %VARIABLE%"

:: usbipd wsl list | findstr /c:"LimeSDR-USB"
::cmd /k
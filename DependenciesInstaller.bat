:: Set Path variable equal to existing path variables plus the previously mentioned
setx PATH "%PATH%;C:\Windows\System32;C:\Windows\System32\WindowsPowerShell\v1.0;C:\Python27;C:\\Python27\\Lib;C:\\Python27\\DLLs;C:\\Python27\\Scripts;C:\\Python27\\Lib\\site-packages;C:\\Python27\\Lib\\lib-tk" /m

:: Set Python variable
setx PYTHON_PATH "C:\Python27;C:\\Python27\\Lib;C:\\Python27\\DLLs;C:\\Python27\\Scripts;C:\\Python27\\Lib\\site-packages;C:\\Python27\\Lib\\lib-tk" /m

:: Install Chocolatey for automated prog install
@powershell -NoProfile -ExecutionPolicy unrestricted -Command "iex ((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'))" && SET PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin

chocolatey install firefox -y
chocolatey install python -version 2.7.2 -y
chocolatey install pip -y
chocolatey install pywin32 -y

path "%~dp0"
start DependenciesInstallerTwo.bat
:: Set Path variable equal to existing path variables plus the previously mentioned
setx PATH "%PATH%;%HOMEDRIVE%\Windows\System32;%HOMEDRIVE%\Windows\System32\WindowsPowerShell\v1.0;%HOMEDRIVE%\Python27;%HOMEDRIVE%\\Python27\\Lib;%HOMEDRIVE%\\Python27\\DLLs;%HOMEDRIVE%\\Python27\\Scripts;%HOMEDRIVE%\\Python27\\Lib\\site-packages;%HOMEDRIVE%\\Python27\\Lib\\lib-tk;%ALLUSERSPROFILE%\chocolatey\bin" /m

:: Set Python variable
setx PYTHON_PATH "%HOMEDRIVE%\Python27;%HOMEDRIVE%\\Python27\\Lib;%HOMEDRIVE%\\Python27\\DLLs;%HOMEDRIVE%\\Python27\\Scripts;%HOMEDRIVE%\\Python27\\Lib\\site-packages;%HOMEDRIVE%\\Python27\\Lib\\lib-tk" /m

:: Install Chocolatey for automated prog install
@powershell -NoProfile -ExecutionPolicy unrestricted -Command "iex ((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'))" && SET PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin

chocolatey install firefox -y
chocolatey install python -version 2.7.2 -y
chocolatey upgrade python -version 2.7.2 -y
chocolatey install pip -y
chocolatey install easy.install -y
chocolatey install pywin32 -y
pip install wmi
pip install selenium -U

PAUSE
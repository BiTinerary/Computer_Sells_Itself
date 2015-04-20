@powershell -NoProfile -ExecutionPolicy unrestricted -Command "iex ((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'))" && SET PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin
choco install python -version 2.7.2
choco upgrade python -version 2.7.2
choco install pip
choco install pywin32
choco install easy.install
pip install wmi

:: Assign all Path variables
SET PYTHON="%HOMEDRIVE%\Python27;%HOMEDRIVE%\\Python27\\Lib;%HOMEDRIVE%\\Python27\\DLLs;%HOMEDRIVE%\\Python27\\Scripts;%HOMEDRIVE%\\Python27\\Lib\\site-packages;%HOMEDRIVE%\\Python27\\Lib\\lib-tk"
:: Set Path variable
setx PATH "%PYTHON%" /m
:: Set Python variable
setx PYTHON_PATH "%HOMEDRIVE%\Python27;%HOMEDRIVE%\\Python27\\Lib;%HOMEDRIVE%\\Python27\\DLLs;%HOMEDRIVE%\\Python27\\Scripts;%HOMEDRIVE%\\Python27\\Lib\\site-packages;%HOMEDRIVE%\\Python27\\Lib\\lib-tk" /m

PAUSE
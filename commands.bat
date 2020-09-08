@echo off

:start
cls
set NL=^& echo.

IF "%1"=="install" (
    pip install nltk
    pip install numpy
    pip install tensorflow
    pip install keras

    echo import nltk> %CD%\cmd_pyinstall.py
    echo nltk.download('wordnet'^)>> %CD%\cmd_pyinstall.py
    python %CD%\cmd_pyinstall.py
    if exist %CD%\cmd_pyinstall.py del /F /Q %CD%\cmd_pyinstall.py

    echo "Successfully installed packages."
)

IF "%1"=="uninstall" (
    pip uninstall -y nltk
    pip uninstall -y numpy
    pip uninstall -y tensorflow
    pip uninstall -y keras
    echo "Successfully uninstalled packages."
)

IF "%1"=="build" (    
    pyinstaller --noconfirm --onedir --console --add-data %CD%\trained_data;trained_data\ --add-data %CD%\training_data;training_data\  %CD%\main.py
    echo Build was successful!
)

IF "%1"=="clean" (
    if exist %CD%\*.spec del /S /F /Q %CD%\*.spec
    if exist %CD%\trained_data\* del /S /F /Q %CD%\trained_data\*
    if exist %CD%\build rmdir /S /Q %CD%\build
    if exist %CD%\dist rmdir /S /Q %CD%\dist
    echo Cleaned up all files.
)

exit
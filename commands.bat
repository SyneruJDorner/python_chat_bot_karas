@echo off

:start
cls

IF "%1"=="install" (
    pip install nltk
    pip install numpy
    pip install tensorflow
    pip install keras

    echo import nltk> %~dp0cmd_pyinstall.py
    echo nltk.download('wordnet'^)>> %~dp0cmd_pyinstall.py
    python %~dp0cmd_pyinstall.py
    if exist %~dp0cmd_pyinstall.py del /F /Q %~dp0cmd_pyinstall.py

    cls
    echo "Successfully installed packages."
)

IF "%1"=="uninstall" (
    pip uninstall -y nltk
    pip uninstall -y numpy
    pip uninstall -y tensorflow
    pip uninstall -y keras

    cls
    echo "Successfully uninstalled packages."
)

IF "%1"=="build" (    
    pyinstaller --noconfirm --onedir --console --add-data %~dp0trained_data;trained_data\ --add-data %~dp0training_data;training_data\ %~dp0main.py

    cls
    echo Build was successful!
)

IF "%1"=="clean" (
    if exist %~dp0*.spec del /S /F /Q %~dp0*.spec
    if exist %~dp0trained_data\* del /S /F /Q %~dp0trained_data\*
    if exist %~dp0build rmdir /S /Q %~dp0build
    if exist %~dp0dist rmdir /S /Q %~dp0dist

    cls
    echo Cleaned up all files.
)

exit
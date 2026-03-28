echo off
pyside6-uic MainWindow.ui -o ../uiPy/MainWindow.py
pyside6-uic DialogParameters.ui -o ../uiPy/DialogParameters.py
pyside6-uic DialogCompareWithTrace.ui -o ../uiPy/DialogCompareWithTrace.py
pyside6-uic gradientParameters.ui -o ../uiPy/gradientParameters.py

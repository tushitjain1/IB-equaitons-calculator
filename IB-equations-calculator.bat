@ECHO OFF

python --version 3.8>NUL
IF ERRORLEVEL 1 GOTO NOPYTHON

IF NOT EXIST .\venv\ (
  python -m venv venv
  setlocal
  set PATH=.\venv\Scripts\
  @REM
  python -m pip install -r requirements.txt -qqq --disable-pip-version-check
) ELSE (
  setlocal
  set PATH=.\venv\Scripts\
  @REM
)

ECHO Close this window to stop the program
ECHO Note: The web page will no longer load new information if the program is stopped
python.exe webdev.py
GOTO:EOF

:NOPYTHON
ECHO Please install Python 3.8 or greater to run this program

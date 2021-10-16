#!/bin/bash

if ! hash python; then
    echo "Please install Python 3.8 or greater to run this program"
    exit 1
fi

ver=$(python -V 2>&1 | sed 's/.* \([0-9]\).\([0-9]\).*/\1\2/')
if [ "$ver" -lt "38" ]; then
    echo "Please install Python 3.8 or greater to run this program"
    exit 1
fi

SCRIPT=`realpath $0`
SCRIPTPATH=`dirname $SCRIPT`
cd $SCRIPTPATH
mv IB-equations-calculator.desktop IB-equations-calculator.desktop-bak
sed -e "s,Icon=.*,Icon=$PWD/static/calc.png,g" IB-equations-calculator.desktop-bak > IB-equations-calculator.desktop
mv IB-equations-calculator.desktop IB-equations-calculator.desktop-bak
sed -e "s,Exec=.*,Exec=$PWD/IB-equations-calculator.sh,g" IB-equations-calculator.desktop-bak > IB-equations-calculator.desktop
rm IB-equations-calculator.desktop-bak

if [ ! -d "./venv/" ]; then
    python -m venv venv
    export PATH=$(pwd)/venv/bin:$PATH
    python -m pip install -r requirements.txt -qqq --disable-pip-version-check

else
    export PATH=$(pwd)/venv/bin:$PATH
fi

echo Close this window to stop the program
echo Note: The web page will no longer load new information if the program is stopped
python webdev.py

Programming Collective Intelligence
===================================

Examples and exercises from Programming Collective Intelligence, O'Reilly

Requirements
------------

matplotlib

libsvn


http://www.idryman.org/blog/2013/05/21/libsvm-on-mac-osx/

Basic installation

    brew install gnuplot
    brew install qt4
    brew install svm

Add svm-toy

    curl -LO http://www.csie.ntu.edu.tw/~cjlin/cgi-bin/libsvm.cgi?+http://www.csie.ntu.edu.tw/~cjlin/libsvm+tar.gz
    tar xzvpf libsvm+tar.gz
    cd libsvm-3.17
    make

    cd svm-toy.qt

Change CFLAGS and MOC variable in Makefile

    CFLAGS = -Wall -O3 -I$(INCLUDE) -I$(INCLUDE)/QtGui -framework QtCore -framework QtGui -F/usr/local/Cellar/qt/4.8.4/lib/
    INCLUDE = /usr/local/Cellar/qt/4.8.4/include/
    MOC = moc

Add Python interface

Put Python interface in path

    cd libsvm-3.17/python
    echo "export PYTHONPATH=\$PYTHONPATH:$(pwd)" >> ~/.bash_profile
    source ~/.bash_profile

Resources
---------

https://github.com/arthur-e/Programming-Collective-Intelligence

Problems
--------

`advancedclassify.py`

Error message

    ImportError: dlopen(/Library/Python/2.7/site-packages/matplotlib/ft2font.so, 2): Library not loaded: /opt/local/lib/libfreetype.6.dylib
      Referenced from: /Library/Python/2.7/site-packages/matplotlib/ft2font.so
      Reason: image not found

Fix

brew install freetype --universal
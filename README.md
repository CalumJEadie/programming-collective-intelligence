Programming Collective Intelligence
===================================

Examples and exercises from Programming Collective Intelligence, O'Reilly

Requirements
------------

- matplotlib

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
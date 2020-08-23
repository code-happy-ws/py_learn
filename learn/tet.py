# import cchardet as chardet
import os

import chardet
import sys


print('start')
try:
    a=1/0
except Exception:
    print('error')
    sys.exit(1)
finally:
    print('end')
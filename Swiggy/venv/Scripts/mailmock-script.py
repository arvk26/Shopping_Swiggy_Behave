#!C:\PycharmProjects\Swiggy\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'behaving==1.5.6','console_scripts','mailmock'
__requires__ = 'behaving==1.5.6'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('behaving==1.5.6', 'console_scripts', 'mailmock')()
    )

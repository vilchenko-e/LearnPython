import sys
import os

os_name = os.name  # 'posix' для linux/mac, 'nt' для windows

if os_name == 'posix':
    os_name = os.uname().sysname  # Linux, Darwin и т.д.
elif os_name == 'nt':
    os_name = 'Windows'

python_version = sys.version  # полная строка с версией и датой сборки

with open('os_info.txt', 'w') as f:
    f.write(f"OS info is {os_name}\n")
    f.write(f"Python version is {python_version}\n")

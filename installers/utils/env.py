import sys
import platform
from os.path import expanduser

pythonVersion = platform.python_version()
system = platform.system()
systemVersoin = platform.version()
hostname = platform.node()
architecture = platform.machine()
processor = platform.processor()
home = expanduser("~")

def init():
    if is_windows():
        global home
        home += '\\'

def print():
    print('Python Version:\t\t', pythonVersion)
    print('Platform:\t\t', system)
    print('Platform Version:\t', systemVersoin)
    print('Hostname:\t\t', hostname)
    print('Architecture:\t\t', architecture)

def validate():
    print('Checking environment...')
    if (pythonVersion < '3.0'):
        print('installed python version=%s, required python version>=3.0' % pythonVersion)
        return False
    else:
        print('installed python version=%s' % pythonVersion)
    return True

def is_windows():
    global system
    return system == "Windows"
def is_linux():
    global system
    return system == "Linux"

init()
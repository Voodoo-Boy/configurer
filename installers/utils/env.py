import datetime
import platform
import os
from os.path import expanduser
from getpass import getuser

# global constants of runtime infos
currentDT = datetime.datetime.now()
install_ver = currentDT.strftime("%Y%m%d%H%M%S")
# platform
pythonVersion = platform.python_version()
system = platform.system()
systemVersoin = platform.version()
hostname = platform.node()
architecture = platform.machine()
processor = platform.processor()
# user
home = expanduser("~")
user = getuser()
env_ver = None

# print platform info
def info():
    print('Python Version:\t\t', pythonVersion)
    print('Platform:\t\t', system)
    print('Platform Version:\t', systemVersoin)
    print('Hostname:\t\t', hostname)
    print('Architecture:\t\t', architecture)
    print()

# check python versions
def validate():
    print('Checking environment...')
    if (pythonVersion < '3.0'):
        print('installed python version=%s, required python version>=3.0' % pythonVersion)
        exit()
    else:
        print('installed python version=%s\n' % pythonVersion)

# helpers
def is_windows():
    global system
    return system == "Windows"
def is_linux():
    global system
    return system == "Linux"

def init():
    global env_ver
    try:
        env_ver = os.environ['_VER']
    except:
        env_ver = None

    global home
    if is_windows():
        home += '\\'
    elif is_linux():
        home += '/'

init()
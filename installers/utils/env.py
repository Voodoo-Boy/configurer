import datetime
import platform
from os.path import expanduser
from getpass import getuser

currentDT = datetime.datetime.now()
install_ver = currentDT.strftime("%Y%m%d%H%M%S")

pythonVersion = platform.python_version()
system = platform.system()
systemVersoin = platform.version()
hostname = platform.node()
architecture = platform.machine()
processor = platform.processor()
home = expanduser("~")
user = getuser()

def init():
    global home
    if is_windows():
        home += '\\'
    elif is_linux():
        home += '/'

def info():
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

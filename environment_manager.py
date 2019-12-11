#!/usr/bin/python3

import sys
import platform

pythonVersion = platform.python_version()
system = platform.system()
systemVersoin = platform.version()
hostname = platform.node()
architecture = platform.machine()
processor = platform.processor()

def printEnvInfo():
    print('Python Version:\t\t', pythonVersion)
    print('Platform:\t\t', system)
    print('Platform Version:\t', systemVersoin)
    print('Hostname:\t\t', hostname)
    print('Architecture:\t\t', architecture)

def validateEnv():
    print('Checking environment')
    if (pythonVersion < '3.0'):
        print('installed python version=%s, required python version>=3.0' % pythonVersion)
        return False
    return True

# Enviroment.pythonInfo()

# print('Version      :', platform.python_version())
# print('Version tuple:', platform.python_version_tuple())
# print('Compiler     :', platform.python_compiler())
# print('Build        :', platform.python_build())

# print('Normal :', platform.platform())
# print('Aliased:', platform.platform(aliased=True))
# print('Terse  :', platform.platform(terse=True))

# print('uname:', platform.uname())

# print()
# print('system   :', platform.system())
# print('node     :', platform.node())
# print('release  :', platform.release())
# print('version  :', platform.version())
# print('machine  :', platform.machine())
# print('processor:', platform.processor())

# print('interpreter:', platform.architecture())
# print('/bin/ls    :', platform.architecture('/bin/ls'))
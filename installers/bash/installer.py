#!/usr/bin/python3

from installers.utils import env
from installers.utils import file_manager

def win_installer():
   src = 'installers/bash/.bashrc'
   dst = env.home + 'bashtest'
   file_manager.append(src_path=src, dst_path=dst)

def linux_installer():
   src = 'installers/bash/.bashrc'
   dst = env.home + 'bashtest'
   file_manager.append(src_path=src, dst_path=dst)


def install():
   print("bash configuration begin")
   if env.is_windows():
      win_installer()
      return True
   elif env.is_linux():
      linux_installer()
      return True
   else:
      print ('Unsupported platform: ', env.system)
      return False
   print("bash configuration finish")

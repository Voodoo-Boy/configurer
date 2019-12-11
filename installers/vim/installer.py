#!/usr/bin/python3

from installers.utils import env
from installers.utils import file_manager

def win_installer():
   src = 'installers/bash/.bashrc'
   dst = env.home + '.bashrc'
   file_manager.append(src_path=src, dst_path=dst)

def linux_installer():
   src = 'installers/bash/.bashrc'
   dst = env.home + '.bashrc'
   file_manager.append(src_path=src, dst_path=dst)
   
   # link .bash_profile, .profile to .bashrc
   links = [".bash_profile"]
   for link in links:
      os.symlink(dst, env.home+links)



def install():
   print("bash configuration begin")
   if env.is_windows():
      linux_installer()
   elif env.is_linux():
      linux_installer()
   else:
      print ('Unsupported platform: ', env.system)
      return False
   print("bash configuration finish")
   return True

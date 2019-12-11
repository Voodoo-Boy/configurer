#!/usr/bin/python3

from installers.utils import env
from installers.utils import file_manager

def win_installer():
   # read source bash profile
   src = 'installers/bash/.bashrc'
   # append to ~/.bashrc
   dst = env.home + 'bashtest'
   print (">>>",dst)

   file_manager.append(src_path=src, dst_path=dst)

   #print ('bash_profile_path=%s' % bashrcPath)
   print("bash configuration finished")

def install():
   if env.is_windows():
      win_installer()
      return True
   else:
      print ('Unsupported platform: ', env.system)
      return False
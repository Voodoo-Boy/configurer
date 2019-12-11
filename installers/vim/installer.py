#!/usr/bin/python3

from installers.utils import env
from installers.utils import file_manager

# vim constants
vimrc_src = "installers/vim/.vimrc"
vimrc_dst = env.home + ".vimrc"

def install():
    print("vim configuration begin")
    # copy .vimrc to home directory
    file_manager.copy_file(vimrc_src, vimrc_dst)
    print("vim configuration begin")

#!/usr/bin/python3

from installers.utils import env
from installers.utils import file_manager

# gvim constants
gvimrc_src = "installers/vim/_vimrc"
gvimrc_dst = env.home + "_vimrc"
gvimfile_src = "installers/vim/vimfiles"
gvimfile_dst = env.home + "vimfiles"

def installer():
    print("gvim configuration begin")
    # copy _vimrc to home directory
    file_manager.copy_file(gvimrc_src, gvimrc_dst)
    # copy vimfiles directory to home directory
    file_manager.copy_dir(gvimfile_src, gvimfile_dst)
    print("gvim configuration begin")

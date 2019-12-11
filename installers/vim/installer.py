#!/usr/bin/python3

from installers.utils import env
from installers.utils import file_manager

vimrc_src = "installers/vim/.vimrc"
vimrc_dst = env.home + ".vimrc"

gvimrc_src = "installers/vim/_vimrc"
gvimrc_dst = env.home + "_vimrc"
gvimfile_src = "installers/vim/vimfiles"
gvimfile_dst = env.home + "vimfiles"

def install_vim():
    print("vim configuration begin")
    file_manager.copy_file(vimrc_src, vimrc_dst)
    print("vim configuration begin")

def gvim_installer():
    print("gvim configuration begin")
    file_manager.copy_file(gvimrc_src, gvimrc_dst)
    file_manager.copy_dir(gvimfile_src, gvimfile_dst)
    print("gvim configuration begin")

import os
import re
from shutil import copyfile
from installers.utils.output import *

def append(src_path, dst_path):
    dst = open(dst_path, 'a+')
    src = open(src_path, 'r')

    dst.write(src.read())

    dst.close()
    src.close()

def append_text(filepath, text):
    dst = open(filepath, 'a+')
    dst.write(text)
    dst.close()

def file_exists(filepath):
    return os.path.isfile(filepath)

def symbol_link(src, dst):
    return os.symlink(src, dst)

def copy(src, dst):
    return copyfile(src, dst)
import os
from installers.utils.output import *

def append(src_path, dst_path):
    dst = open(dst_path, 'a+')
    src = open(src_path, 'r')

    dst.write(src.read())

    dst.close()
    src.close()

def file_exists(filepath):
    return os.path.isfile(filepath)
#!/usr/bin/python3

import datetime
from installers.utils import env
from installers.utils import file_manager

# bash constants
bash_src = "installers/bash/.bashrc"
bash_dst = env.home + ".bashrc." + env.user
env_ver = '_VER'
# shell statements to add
stat_source_bashrc = "source $HOME/.bashrc." + env.user
stat_export_version = "export _VER=" + env.ver_num

def install():
    print("bash configuration begin")

    # Check if bashrc has been installed
    print("Check if bash configuration has been installed")
    installed = checkInstalled()
    if installed:
        print(".bashrc has been installed, build version=" + installed)
        return

    # copy our customized bash profile to home directory
    file_manager.copy_file(bash_src, bash_dst)
    print("copy .bashrc.{0} to $HOME directory".format(env.user))

    # Update the default bash profile
    shell_exp = "\n{0}\n{1}\n".format(stat_source_bashrc, stat_export_version)
    for profile in [".bashrc", ".bash_profile", ".profile"]:
        profile = env.home + profile
        if file_manager.file_exists(profile):
            # add statements to source our .bashrc.{$user} and add an env var to indicate the version
            file_manager.append_text(profile, shell_exp)
            print("{0} updated, build version={1}".format(profile, env.ver_num))
            print("bash configuration finished")
            return

    # TODO if no profile exist, create one (until the condition occurs)
    print("error: default bash profile not found!")
    exit()

def checkInstalled():
    ver = env.get_env(env_ver)
    if not ver:
        return False
    else:
        return ver

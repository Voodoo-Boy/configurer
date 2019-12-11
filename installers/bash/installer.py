#!/usr/bin/python3

import datetime
from installers.utils import env
from installers.utils import file_manager

# bash constants
bash_src = "installers/bash/.bashrc"
bash_dst = env.home + ".bashrc." + env.user
# shell statements to add
stat_source_bashrc = "source $HOME/.bashrc." + env.user
stat_export_version = "export _VER=" + env.install_ver

def install():
    print("\nbash configuration begin")

    # Check if bashrc has been installed
    print("Check if bash configuration has been installed")
    if checkInstalled():
        print(".bashrc has been installed, build version="+env.env_ver)
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
            print("{0} updated".format(profile))
            # export the _VER env var
            os.environ["_VER"] = env.install_ver
            print("environment variable updated, _VER={0}".format(profile))
            print("bash configuration finished\n")
            return

    # TODO if no profile exist, create one (until the condition occurs)
    print("error: default bash profile not found!")
    exit()

def checkInstalled():
    if env.env_ver:
        return True
    else:
        return False


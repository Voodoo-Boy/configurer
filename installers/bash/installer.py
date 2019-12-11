#!/usr/bin/python3

import datetime
from installers.utils import env
from installers.utils import file_manager

bash_src = "installers/bash/.bashrc"
bash_dst = env.home + ".bashrc." + env.user

exp_source_bashrc = "source $HOME/.bashrc." + env.user
exp_export_version = "export _VER=" + env.install_ver

def install():
    print("bash configuration begin")
    # copy our customized bash profile to home directory
    file_manager.copy_file(bash_src, bash_dst)

    # modify the default bash profile to load our custmized configs
    shell_exp = "\n{0}\n{1}\n".format(exp_source_bashrc, exp_export_version)
    done = False
    for profile in [".bashrc", ".bash_profile", ".profile"]:
        profile = env.home + profile
        if file_manager.file_exists(profile):
            # Add time stamp as version
            file_manager.append_text(profile, shell_exp)
            done = True
            break
    # TODO if no profile exist, create one

    print("bash configuration finish")
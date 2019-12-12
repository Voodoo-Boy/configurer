#!/usr/bin/python3

import installers.bash.installer
import installers.vim.installer
import installers.utils.env

options = {
    "bash": installers.bash.installer,
    "vim": installers.vim.installer
}

def init():
    # validate installation environment
    installers.utils.env.validate()
    # output running environment info
    installers.utils.env.info()

# interact with user, check what to install
def cui():
    for option, installer in sorted(options.items()):
         print("Install {0}? (y/n): ".format(option), end='')
         if (input().strip().lower() == 'y'):
             installer.install()
             print()
    return

init()
cui()

print("Install finished")
print(":P")

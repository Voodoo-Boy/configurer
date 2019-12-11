#!/usr/bin/python3

import installers.utils.env
import installers.bash.installer
import installers.vim.installer

#installers.bash.installer.install()
installers.vim.installer.install_vim()

# if installers.utils.env.validateEnv():
#     print("Succeed!")
# else:
#     print("Faile!")

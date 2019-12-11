#!/usr/bin/python3

import installers.utils.env
import installers.bash.installer


installers.bash.installer.install()

# if installers.utils.env.validateEnv():
#     print("Succeed!")
# else:
#     print("Faile!")

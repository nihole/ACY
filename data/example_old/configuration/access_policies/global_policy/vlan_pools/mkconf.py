# The environment ACY_PATH must be defined with the export command
# This environment should point to the location of the ACY scripts
# For example: export ACY_PATH = '~/PUBLICGIT/ACY/'


# This is only line which is different for any ACI object
# Location of j2 template file
#

template_path = 'scripts/configuration/access_policies/global_policy/vlan_pools/template.j2'

######### Main Body ######################
#### Should be the same for all ACI objects #########

import os
import sys
import re

render_path = 'scripts/render.py'

acy_path = os.environ.get('ACY_PATH')

if not acy_path:
    print ("ACY_PATH is not set. Please execute the command export ACY_PATH='path', where path is a path to ACY folder with scripts.")
    quit()

else:
    if not re.search('/$', acy_path):
        acy_path = acy_path + "/"



######### get file's names from the command line ####################
if (len(sys.argv)==2):
    yaml_file = sys.argv[1]
else:
    print ("   ######################################################\n")
    print ("   Syntax is:\n")
    print ("   python3 mkconf.py configuration_yaml_file.yml\n")
    print ("   ######################################################\n")
    quit()

cmd = 'python %s%s %s%s ./%s' % (acy_path, render_path, acy_path, template_path, yaml_file)

returned_value = os.system(cmd)




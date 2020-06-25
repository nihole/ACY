import os
import sys

ACY_SCRIPT_PATH = '../../../../../../scripts/'

template_path = ACY_SCRIPT_PATH + 'configuration/tenant/app_profiles/template.j2'
render_path = ACY_SCRIPT_PATH + 'render.py'

######### Main Body ######################
#### Should be the same for all ACI objects #########

import os
import sys


######### get file's names from the command line ####################
if (len(sys.argv)==2):
    yaml_file = sys.argv[1]
else:
    print ("   ######################################################\n")
    print ("   Syntax is:\n")
    print ("   python3 mkconf.py configuration_yaml_file.yml\n")
    print ("   ######################################################\n")
    quit()

cmd = 'python %s %s %s' % (render_path, template_path, yaml_file)

returned_value = os.system(cmd)




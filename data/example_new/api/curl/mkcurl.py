# The environment ACY_PATH must be defined with the export command
# This environment should point to the location of the ACY scripts
# For example: export ACY_PATH = '~/PUBLICGIT/ACY/'

# The environment ACY_DATA_PATH must be defined with the export command
# This environment should point to the location of the ACY YAML/XML files, related to project
# For example: export ACY_DATA_PATH = '~/PUBLICGIT/ACY/'



# This is only line which is different for any ACI object
# Location of j2 template file
#

template_path = '/scripts/api/curl/template.j2'

######### Main Body ######################
#### Should be the same for all ACI objects #########

import os
import sys
import re

create_curl_path = 'scripts/api/curl/create_curl.py'

acy_path = os.environ.get('ACY_PATH')
acy_data_path = os.environ.get('ACY_DATA_PATH')


if not acy_path:
    print ("ACY_PATH is not set. Please execute the command export ACY_PATH='path', where path is a path to ACY root folder with scripts.")
    quit()
else:
    if not re.search('/$', acy_path):
        acy_path = acy_path + "/"
if not acy_data_path:
    print ("ACY_DATA_PATH is not set. Please execute the command export ACY_DATA_PATH='path', where path is a path to ACY root folder with data.")
    quit()
else:
    if not re.search('/$', acy_data_path):
        acy_data_path = acy_data_path + "/"



######### get file's names from the command line ####################
if (len(sys.argv)==2):
    yaml_file = sys.argv[1]
    cmd = 'python %s%s %s%s %s' % (acy_path, create_curl_path, acy_path, template_path, yaml_file)

elif (len(sys.argv)==3):
    yaml_file = sys.argv[1]
    destination_file = sys.argv[2]
    cmd = 'python %s%s %s%s ./%s %s' % (acy_path, create_curl_path, acy_path, template_path, yaml_file, destination_file)

else:
    print (len(sys.argv))
    print ("   ######################################################\n")
    print ("   Syntax is:\n")
    print ("   python3 mkcurl.py ../data/all_xml.yml\n   or\n")
    print ("   python3 mkcurl.py ../data/all_xml.yml destination_file")
    print ("   ######################################################\n")
    quit()


returned_value = os.system(cmd)



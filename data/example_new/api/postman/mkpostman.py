import os
import sys
import re


ACY_SCRIPT_PATH = '../../../../scripts/'

template_path = ACY_SCRIPT_PATH + 'api/postman/template.j2'
create_postman_path = ACY_SCRIPT_PATH + 'api/postman/create_collection.py'



######### get file's names from the command line ####################
if (len(sys.argv)==2):
    yaml_file = sys.argv[1]
    cmd = 'python %s %s %s' % (create_postman_path, template_path, yaml_file)

elif (len(sys.argv)==3):
    yaml_file = sys.argv[1]
    destination_file = sys.argv[2]
    cmd = 'python %s %s %s %s' % (create_postman_path, template_path, yaml_file, destination_file)

else:
    print (len(sys.argv))
    print ("   ######################################################\n")
    print ("   Syntax is:\n")
    print ("   python3 mkpostman.py ../data/all_xml.yml\n   or\n")
    print ("   python3 mkpostman.py ../data/all_xml.yml ../data/postman.txt")
    print ("   ######################################################\n")
    quit()


returned_value = os.system(cmd)



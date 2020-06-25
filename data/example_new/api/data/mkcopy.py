import os
import sys
import re


ACY_SCRIPT_PATH = '../../../../scripts/'

copy_all_path = ACY_SCRIPT_PATH + 'api/data/copy_all.py'



######### get file's names from the command line ####################

if (len(sys.argv)==3):
    yaml_file = sys.argv[1]
    destination_folder = sys.argv[2]
    cmd = 'python %s %s %s' % (copy_all_path, yaml_file, destination_folder)

else:
    print (len(sys.argv))
    print ("   ######################################################\n")
    print ("   Syntax is:\n")
    print ("   python3 mkcopy.py all_xml.yml xml_all/\n   or\n")
    print ("   python3 mkcopy.py all_xml.yml yml_all/\n   or\n")
    print ("   ######################################################\n")
    quit()


returned_value = os.system(cmd)



import sys
import yaml
import re
import os


######### get file's names ####################
if (len(sys.argv)==3):
    yaml_file = sys.argv[1]
    dst_folder = sys.argv[2]
else:
    print ("   ######################################################\n")
    print ("   Syntax is:\n")
    print ("   python3 check_collection.py collection_file.yml destinatio_folder_path\n")
    print ("   ######################################################\n")
    quit()


   ######### take data from YAML file ####################

my_config=''
f = open( "./%s" % yaml_file )		
data1 = f.read()
f.close()

   ######### Take the data from files being pointed in "path". Only if action == "yes" ######
   ######### Print the name of API request and path to the file ######

print ("\n> These POST API requests will be used:\n")
print ("####################################################\n")

yaml_version = yaml.__version__
m = re.match('(\d(\.\d)?)', yaml_version)
yaml_ver = m.group(1)

if (float(yaml_ver) < 5.1):
    yaml_data = yaml.load(data1)
else:
    yaml_data = yaml.load(data1,Loader=yaml.FullLoader)


for j in yaml_data["files"]:
    action = "no"
    if (not j["action"]):
        if yaml_data["default"]["action"] == "yes":
            action = "yes"
    else:
        if j["action"] == "yes":
            action = "yes"
    if action == "yes":
        print ('cp %s %s' % (j["path"], dst_folder))
        os.system('cp /c/%s %s' % (j["path"], dst_folder))

print ("####################################################\n")


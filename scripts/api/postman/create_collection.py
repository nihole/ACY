import sys
import yaml
import jinja2
import os
import re



def take_data(path):
    fl = open(path, "r")
    data = fl.read()
    fl.close
    return data

######### get file's names from the command line ###################
if (len(sys.argv)==3):
    j2_file = sys.argv[1]
    yaml_file = sys.argv[2]
elif(len(sys.argv)==4):
    j2_file = sys.argv[1]
    yaml_file = sys.argv[2]
    destination_file = sys.argv[3]
else:
    print ("   ######################################################\n")
    print ("   Syntax is:\n")
    print ("   python3 create_collection.py template_file.j2 collection_file.yml [destination_file.json]\n")
    print ("   ######################################################\n")
    quit()

loader = jinja2.FileSystemLoader('/tmp')
env = jinja2.Environment(autoescape=False, loader=loader)

   ######### take environment veriables  #################

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


   ######### take data from YAML file ####################

my_config=''
f = open( "./%s" % yaml_file )		
data1 = f.read()
f.close()

yaml_version = yaml.__version__
m = re.match('(\d(\.\d)?)', yaml_version)
yaml_ver = m.group(1)

if (float(yaml_ver) < 5.1):
    yaml_data = yaml.load(data1)
else:
    yaml_data = yaml.load(data1,Loader=yaml.FullLoader)

   ######### Take data from YAML. Only if action == "yes"  ####################

root_path = yaml_data["default"]["root_path"]

for j in yaml_data["files"]:
    action = "no"
    if (not j["action"]):
        if yaml_data["default"]["action"] == "yes":
            action = "yes"
    else:
        if j["action"] == "yes":
            action = "yes"
    if action == "yes":
        j_str = take_data(root_path + j["path"])
        j_str = j_str.replace('\"', '\\"').replace('\t','\\t').replace('\n','\\n')
        j["path"] = str(j_str)

   ######### Take credentials from cli ###################


hostname = input("Hostname: ")
username = input("Username: ")
password = input("Password: ")
#password = getpass.getpass()

yaml_data["default"]["hostname"] = hostname
yaml_data["default"]["username"] = username
yaml_data["default"]["password"] = password

   ######### read templates from Jinja2 file ####################

f = open( "%s" % j2_file )
data2 = f.read()
f.close()

template = env.from_string(data2)

   ######### YAML data + Jinja data -> POSTMAN collection ####################

my_config = template.render(yaml_data);

   ######### Some additional editing ####################

# Remove blank lines:
my_comfig = [s for s in my_config.splitlines(True) if (not re.search("^\s*$", s))]

# We also have to remove one comma (third line from the end of file)
my_comfig[-3] = my_comfig[-3].replace(",","")

# Create string
my_config_txt = "".join(my_comfig)

# Write data to the destination file

try: 
  destination_file
except NameError:
  print(my_config_txt)
else:
  d = open(destination_file, "a")
  d.write(my_config_txt)
  d.close()


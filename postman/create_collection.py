
import re
import paramiko
import sys
import yaml
import jinja2
from jinja2 import Template
from jinja2 import environment as env
from jinja2 import *
from pprintpp import pprint
import ipaddress

def take_data(path):
    fl = open(path, "r")
    data = fl.read()
    fl.close
    return data

######### get file's names ####################
if (len(sys.argv)==3):
    j2_file = sys.argv[1]
    yaml_file = sys.argv[2]
else:
    print ("   ######################################################\n")
    print ("   python3 create_collection template.j2 collection.yml\n")
    print ("   ######################################################\n")
    quit()

loader = jinja2.FileSystemLoader('/tmp')
env = jinja2.Environment(autoescape=False, loader=loader)

my_config=''
f = open( "./%s" % yaml_file )		
data1 = f.read()
f.close()

yaml_data = yaml.load( data1 )
for j in yaml_data["files"]:
    action = "no"
    if (not j["action"]):
        if yaml_data["global"]["action"] == "yes":
            action = "yes"
    else:
        if j["action"] == "yes":
            action = "yes"
    if action == "yes":
        j_str = take_data(j["path"])
        j_str = j_str.replace('\"', '\\"').replace('\t','\\t').replace('\n','\\n')
        j["path"] = str(j_str)



f = open( "./%s" % j2_file )
data2 = f.read()
f.close()

template = env.from_string(data2)

my_config = template.render(yaml_data);


# Remove blank lines:
my_comfig = [s for s in my_config.splitlines(True) if (not re.search("^\s*$", s))]

# Remove comma 
my_comfig[-3] = my_comfig[-3].replace(",","")

# Create str
my_config_txt = "".join(my_comfig)

print(my_config_txt)


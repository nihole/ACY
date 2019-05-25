import re
import sys
import yaml
import jinja2

def take_data(path):
    fl = open(path, "r")
    data = fl.read()
    fl.close
    return data

######### get file's names from the command line ###################
if (len(sys.argv)==3):
    j2_file = sys.argv[1]
    yaml_file = sys.argv[2]
else:
    print ("   ######################################################\n")
    print ("   Syntax is:\n")
    print ("   python3 create_collection.py template_file.j2 collection_file.yml\n")
    print ("   ######################################################\n")
    quit()

loader = jinja2.FileSystemLoader('/tmp')
env = jinja2.Environment(autoescape=False, loader=loader)

   ######### take data from YAML file ####################

my_config=''
f = open( "./%s" % yaml_file )		
data1 = f.read()
f.close()

yaml_data = yaml.load( data1 )

   ######### Take data from YAML. Only if action == "yes"  ####################

for j in yaml_data["files"]:
    action = "no"
    if (not j["action"]):
        if yaml_data["default"]["action"] == "yes":
            action = "yes"
    else:
        if j["action"] == "yes":
            action = "yes"
    if action == "yes":
        j_str = take_data(j["path"])
        j_str = j_str.replace('\"', '\\"').replace('\t','\\t').replace('\n','\\n')
        j["path"] = str(j_str)

   ######### read templates from Jinja2 file ####################

f = open( "./%s" % j2_file )
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

print(my_config_txt)


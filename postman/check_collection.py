import sys
import yaml


######### get file's names ####################
if (len(sys.argv)==2):
    yaml_file = sys.argv[1]
else:
    print ("   ######################################################\n")
    print ("   python3 check_collection.py collection.yml\n")
    print ("   ######################################################\n")
    quit()


my_config=''
f = open( "./%s" % yaml_file )		
data1 = f.read()
f.close()

print ("\n> These POST API requests will be used:\n")
print ("####################################################\n")
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
        print ("name: %s\npath: %s\n" % (j["name"], j["path"]))

print ("####################################################\n")


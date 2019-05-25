import sys
import yaml


######### get file's names ####################
if (len(sys.argv)==2):
    yaml_file = sys.argv[1]
else:
    print ("   ######################################################\n")
    print ("   Syntax is:\n")
    print ("   python3 check_collection.py collection_file.yml\n")
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


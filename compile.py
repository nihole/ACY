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

    ######### get file's names ####################
if (len(sys.argv)==3):
    j2_file = sys.argv[1]
    yaml_file = sys.argv[2]
else:
    print ("   ######################################################\n")
    print ("   python3 ../compile.pl template.j2 device_name.yml\n")
    print ("   ######################################################\n")
    quit()

loader = jinja2.FileSystemLoader('/tmp')
env = jinja2.Environment(autoescape=True, loader=loader)

my_config=''
f = open( "./%s" % yaml_file )		
data1 = f.read()
f.close()

yaml_data = yaml.load( data1 )

f = open( "./%s" % j2_file )
data2 = f.read()
f.close()

template = env.from_string(data2)

my_config = template.render(yaml_data);

#my_config = "".join([s for s in my_config.splitlines(True) if s.strip("\r\n")])

# Remove blank lines:
my_config = "".join([s for s in my_config.splitlines(True) if (not re.search("^\s*$", s))])

print(my_config)


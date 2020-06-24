collection_tmpl.yml - template for YAML file with a list of xml files to be added to postman collection

check_collection.py
syntax:  python check_collection.py collection_file.yml
create a list of API calls should be added to postman collection
collection_file.yml is a file created in accordance with collection_tmpl.yml format

copy_all.py
syntax: python copy_all.py files.yml path
files.yml  is a file created in accordance with collection_tmpl.yml format
for example collection_file.yml used with create_collection.py and check_collection.py may be used to copy xml files
path - path to destination directory


create_collection.py
python create_collection.py template_file.j2 collection_file.yml
collection_file.yml is a file created in accordance with collection_tmpl.yml format


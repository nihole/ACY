<h3>What is ACY</h3>

ACY = deployment Cisco <b>AC</b>I from <b>Y</b>aml = <b>AC</b>I from <b>Y</b>aml

The idea is to manage the Cisco ACI configuration via text files in YAML format. It allows you to
- use a simple interface for ACI configuration
- think about the configuration parameters only, and not about the command's syntax or GUI-navigation
- use version control systems (for example, based on git) and follow the best practices of development for network infrastructure changes control

The last point is a significant advantage over some other deployment methods (for example Deployment ACI From Excel).

<h3>Installation</h3>

- clone this project to your local folder
- install python3 with yaml and jinja2 packages
- install Postman

<h3>Which ACI objects can be managed with ACY</h3>

- Access policies:
  - Global access policies:
    - vlan pools
    - physical domain
    - l3out domain
    - vmm domain
    - aaep
  - Interface access policies:
    - interface policies
    - interface policy groups
    - interface profiles
    - FEX interface profile 
  - Switch access policies:
    - node provisioning
    - mgmt ip addresses
    - switch policy groups
    - switch profiles
    - FEX provisioning
- Tenants:
  - tenants
  - contexts 
  - bridge domais
  - application profiles
  - EPGs
  - EPG static bindings
- L3OUT:
  - l3outs
  - l3out node profiles
  - l3out interface profiles
  - external EPGs
- Contracts:
  - filters
  - contracts
  - EPG attachment
  
<h3>Start configuration</h3>

The idea is that you only need to change YAML files!! 
You never change the python rendering file and generally you don't need to change jinja templates.

Let's consider for example that we want to create a new vlan pool. 

1. Go to the correspondent folder. In this case it is access_policies/global_policy/vlan_pools. 

There are 2 files already there: <b>template.j2</b> and <b>vlan_pools_tmpl.yml</b>.
- <b>template.j2</b> - is jinja2 template. You usually don'r need to change it.
- <b>vlan_pools_tmpl.yml</b> - this file we are going to use for our yaml file creation (if it has not been done before)

2. Create new folder (if it has not been done before). Actually you may use any folder, but it looks reasonable to creare a new folder in the curent one. Let's create a folder "example1". 

```
mkdir example1
```

3. Copy file vlan_pools_tmpl.yml (if it has not been done before) to this folder and rename it:

```
cp vlan_pools_tmpl.yml ./example1/vlan_pools.yml
cd ./example1/
```

4. Fill in <b>vlan_pools.yml</b> with configuration parameters (see access_policies/global_policy/vlan_pools//example1/vlan_pools.yml file)

5. Generate xml file for ACI configuration

```
../../../../render.py ../template.j2 vlan_pools.yml > vlan_pools.xml
```

6. Upload this file to ACI (see the next chapter).

For demonstration purpose I have created such a files for each ACI objects. For example, if you want to see how to configure L3out refer to the folders:

```
l3out/l3outs/example1/test_tenant1/
l3out/l3out_node_profiles/example1/test_tenant1/
l3out/l3out_int_profiles/example1/test_tenant1/
l3out/extenal_epg/example1/test_tenant1/
```

<h3>Upload to ACI</h3>

Let's assume that we created a lot of XML files. We can use many API requests to upload this configuration, but it doesn’t look very scalable. 

This project provides a tool to combine individual API requests into a single POSTMAN collection.

1. Go to the folder postman. From the root folder the command will be
```
cd postman
```
There are 3 files here: 
- <b>create_collection.py</b> - is a python script used for the postman collection file generation (with using of jinja template and yaml configuration files as input)
- <b>template.j2</b> - jinja template file used as input for the create_collection.py
- <b>collection_tmpl.yml</b> - we use this file as a template for new collection yaml files.

2. Create new folder (if it has not been done before). Actually you may use any folder, but it looks reasonable to creare a new folder in the curent one.

```
mkdir example1
```
3. Copy file <b>collection_tmpl.yml</b> to the new folder with renaming. For example a new name maybe all.yml

```
cp collection_tmpl.yml example1/all.yml
```

4. Fill in a new file (see postman/example1/all.yml)

5. Generate collection file all.json (json format) 

```
cd example1
../create_collection.py ../template.j2 all.yml > all.json
```
6. Upload this file in POSTMAN

7. RUN this collection



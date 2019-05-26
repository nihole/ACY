<h3>What is ACY</h3>

ACY = deployment Cisco <b>AC</b>I from <b>Y</b>aml = <b>AC</b>I from <b>Y</b>aml
Thus, ACY is rather the name of the approach, than the name of the software product.

The idea is to manage the Cisco ACI configuration via text files in YAML format. It allows you to
- use a simple interface for ACI configuration
- think about the configuration parameters only and not about the command's syntax or GUI-navigation
- use version control systems (for example, based on git) and follow the best practices of development for network infrastructure changes control

The last point is important because, from my point of view, it is a significant advantage over some other deployment methods (for example, Deployment ACI From Excel).

<h3>Installation</h3>

- clone this project to your local folder
- install Python3 with YAML and Jinja2 packages
- install Postman

<h3>Which ACI objects can be managed with ACY</h3>

In the current version of ACY, you can create, modify, or delete the following ACI objects:

- Access policies:
  - Global access policies:
    - vlan pools
    - physical domains
    - l3out domains
    - vmm domains
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
  
<h3>Configuration procedure</h3>

The procedure is simple and mainly consists of three steps:

- fill in the YAML file
- generate the XML configuration file 
- upload it to ACI.  

You never change the Python rendering file <a href="https://github.com/nihole/ACY/blob/master/render.py">render.py</a> and generally you don't need to change Jinja2 templates.

<h3>Example</h3>

Let's consider, for example, that we want to create a new VLAN pool.

1. Go to the correspondent folder. In this case it is <a href="https://github.com/nihole/ACY/tree/master/access_policies/global_policy/aaep">access_policies/global_policy/vlan_pools</a>

There are 2 files already there: <a href="https://github.com/nihole/ACY/blob/master/access_policies/global_policy/aaep/template.j2">template.j2</a> and <a href="https://github.com/nihole/ACY/blob/master/access_policies/global_policy/aaep/aaep_tmpl.yml">vlan_pools_tmpl.yml</a>.
- template.j2 - is Jinja2 template. You usually don't need to change it.
- vlan_pools_tmpl.yml - this YAML file we are going to use for our YAML file creation (if it has not been done before)

2. Create a new folder (if it has not been done before). Actually you may use any folder, but it looks reasonable to creare a new folder in the curent one. Let's create a folder <a href="https://github.com/nihole/ACY/tree/master/access_policies/global_policy/aaep/example1">example1</a> 

```
mkdir example1
```

3. Copy file vlan_pools_tmpl.yml (if it has not been done before) to this folder and rename it:

```
cp vlan_pools_tmpl.yml ./example1/vlan_pools.yml
cd ./example1/
```

4. Fill in <a href="https://github.com/nihole/ACY/blob/master/access_policies/global_policy/aaep/example1/aaep.yml">vlan_pools.yml</a> with configuration parameters

5. Generate <a href="https://github.com/nihole/ACY/blob/master/access_policies/global_policy/aaep/example1/aaep.xml">aaep.xml</a> file for ACI configuration 

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

The described approach can result in many XML files. We can use many API requests to load these files into ACI, but this does not look very scalable.

This project provides a tool to collect individual API requests into one Postman collection.

1. Go to the folder <a href="https://github.com/nihole/ACY/tree/master/postman">postman</a>
```
cd postman
```
There are 3 files here: 
- <a href="https://github.com/nihole/ACY/blob/master/postman/check_collection.py">create_collection.py</a> - is a Python script used for the Postman collection file generation (with using of Jinja template and YAML configuration files as input)
- <a href="https://github.com/nihole/ACY/blob/master/postman/template.j2">template.j2</b> - Jinja2 template used as input for the create_collection.py
- <a href="https://github.com/nihole/ACY/blob/master/postman/collection_tmpl.yml">collection_tmpl.yml</a> - we use this file as a template for new collection YAML files.

2. Create a folder <a href="https://github.com/nihole/ACY/tree/master/postman">">example1</a> (if it has not been done before). Actually you may use any folder, but it looks reasonable to creare a new folder in the curent one.

```
mkdir example1
```
3. Copy file collection_tmpl.yml to the new folder with renaming. For example a new name maybe all.yml

```
cp collection_tmpl.yml example1/all.yml
```

4. Fill in a new file <a href="https://github.com/nihole/ACY/blob/master/postman/example1/all.yml">all.yml</a>

5. Generate collection file <a href="https://github.com/nihole/ACY/blob/master/postman/example1/all.json">all.json</a>

```
cd example1
../create_collection.py ../template.j2 all.yml > all.json
```
6. Start Postmat and import this collection

7. Run this collection in Postman



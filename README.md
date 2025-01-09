# ACY

ACY = deployment Cisco <b>AC</b>I from <b>Y</b>aml = <b>AC</b>I from <b>Y</b>aml

Thus, ACY is rather the name of the approach, than the name of the software product.

The idea is to manage the Cisco ACI configuration via text files in YAML format. It allows you to
- use a simple interface for ACI configuration
- think about the configuration parameters only and not about the command's syntax or GUI-navigation
- use version control systems (for example, based on git) and follow the best practices of development for network infrastructure changes control

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
    - FEX provisioning (not ready)
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

Folder structure is important to understanding this project.

In the root directory there are 2 folders: `data` and `scripts`. 

All ACI configuration data is always stored in the `data` folder and its nested subfolders. Any changes made as part of our configuration project should always be in the `data` folder and their subfolders. Users should never modify anything in the `scripts` folder.

The `data` folder can be excluded from git synchronization (using `.gitignore`), copied to another "protected" space. This is your data and you need to take care of it.

The `scripts` folder provides all the necessary scripts. While there are some scripts in the `data` folder, they always call scripts located in the `scripts` folder and its nested subfolders.

The best way to understand is by following the example.

<h3>Example</h3>

<b><em>The folder data/example_new is an example of how ACY may be used for ACI deployment. You always can refer to this folder.</em></b>

 Now let's imagine that you want to make new ACI deployment.

1. Clone the project
   ```bash
   clone https://github.com/nihole/ACY.git

2. Create new subfolder in the folder `data`. All data related to your configuration will be located in this folder. 
   ```bash
   cd data
   mkdir yourproject

3. Log into created folder and copy all content from the `template` folder to the created folder. This `template` folder contains all needed configuration templates.

   ``` bash
   cd yourproject
   cp -r ../template/* ./
   ```

4. Go to the configuration folder. Execute tree command:

   ```bash
   cd configuration
   tree
   ├───access_policies
   │   ├───global_policy
   │   │   ├───aaep
   │   │   ├───phys_domains
   │   │   ├───vlan_pools
   │   │   └───vmm_domains
   │   ├───interface_policy
   │   │   ├───fex_interface_profiles
   │   │   ├───interface_policies
   │   │   ├───interface_profiles
   │   │   └───int_pol_groups
   │   └───switch_policy
   │       ├───fex_provisioning
   │       ├───mgmt
   │       ├───node_provisioning
   │       ├───switch_profiles
   │       ├───sw_pol_groups
   │       └───vpc_domains
   └───tenant
       └───tenant_test1
           ├───app_profiles
           ├───bridge_domains
           ├───contexts
           ├───contract
           │   ├───contracts
           │   ├───epg_contracts
           │   ├───extepg_contracts
           │   ├───filters
           │   └───vrf_contracts
           ├───end_point_groups
           ├───epg_static_bindings
           ├───l3out
           │   ├───external_epg
           │   ├───l3outs
           │   ├───l3out_bgp
           │   ├───l3out_int_profiles
           │   └───l3out_node_profiles
           └───tenants
   ```
   
   These folders represent the ACI policy model. The leaf folders contain YAML files that we will fill in according to our Network Implementation Plan (NIP). Technically, these YAML files can be considered as the NIP.
   
   Go through each leaf folder one by one and modify the YAML files. If you need help with the syntax, refer to the `Example_new` project and review its YAML files
   
   <a href="https://github.com/nihole/ACY/blob/master/data/example_new/configuration/access_policies/global_policy/aaep/aaep.xml">aaep.yml</a>
   
   <a href="https://github.com/nihole/ACY/blob/master/data/example_new/configuration/access_policies/global_policy/phys_domains/phys_domains.xml">phys_domains.yml</a>
   
   <a href="https://github.com/nihole/ACY/blob/master/data/example_new/configuration/access_policies/global_policy/vlan_pools/vlan_pools.xml">vlan_pools.yml</a>
   
   ...
   
   5. Create XML files by going to each leaf folder one by one and executing the command:
   
      `python mkconf.py yaml_file.yml > .xml_file.xml`
   
      For example, for AAEP:
   
      ```bash
      cd data/yourproject/configuration/access_policies/global_policy/aaep
      python mkconf.py aaep.yml > aaep.xml
      ```
   
      XML file will be created :
   
      ```xml
      <?xml version="1.0" encoding="UTF-8"?>
      <polUni>
      	<infraInfra>
      		<infraAttEntityP name="AEP_1" descr="" status="created,modified">
      		  	<infraRsDomP tDn="uni/phys-PhyDom_1"/>
      			<infraRsDomP tDn="uni/l3dom-L3Dom_1"/>
      		</infraAttEntityP>
         	</infraInfra>
      </polUni>
      ```
   
      These files will be used for ACI configuration as the XML body for REST API calls. Please refer to `example_new` to see the configuration.
   
      Skip folders if you don't want to configure the related ACI object.
   
   6. Consolidate all YAML and XML files in one location. While a hierarchical structure is convenient for configuration, having all files in one place can also be very helpful. Go to the folder `data/yourproject/api/data`. Edit files `all_yml.yml` and `all_xml.xml` files. The goal is to configure `action: no` for the objects that are will be not configured on ACI (default behavior is "yes").
   
      For example:
   
      ```yaml
      - name: "vmm_domains"
        path: "access_policies/global_policy/vmm_domains/vmm_domains.xml"
        action: "no"
      ```
   
      ```yaml
      - name: "vmm_domains"
        path: "access_policies/global_policy/vmm_domains/vmm_domains.yml"
        action: "no"
      ```
   
      After that, execute the commands:
   
      ```bash
      python mkcopy.py all_xml.yml xml_all/
      python mkcopy.py all_yml.yml yml_all/
      ```
   
      XML files will be copied to `xml_all` and YAML files to `yml_all` folders.
   
   7. Create Postman collection.
   
      ```bash
      python ../postman/mkpostman.py ./all_xml.yml postman.json
      ```
   
      The next information will be requests:

      - Hostname (or IP address) of APIC
      - Username/Password to login APIC 
   
      (To avoid data leaking, you can use variables that should be defined in Postman )
   
   8. Import postman collection into postman
   
   9. Run collection - your ACI will be configured

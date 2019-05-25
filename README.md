<h4>What is ACY</h4>

ACY = deployment Cisco <b>AC</b>I from <b>Y</b>aml = <b>AC</b>I from <b>Y</b>aml

The idea is to manage the Cisco ACI configuration via text files in YAML format. It allows you to
- use a simple interface for ACI configuration
- think about the configuration parameters only, and not about the command's syntax or GUI-navigation
- use version control systems (for example, based on git) and follow the best practices of development for network infrastructure changes control

The last point is a significant advantage over some other deployment methods (for example Deployment ACI From Excel).

<h4>Installation</h4>

- clone this project to your local folder
- install python3 with yaml and jinja2 packages
- install Postman

<h4>Which ACI objects can be managed with ACY</h4>

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
  
<h4>Start configuration</h4>

Let's consider for example that we want to create a new vlan pool. 

1. Go to the correspondent folder. In this case it is access_policies/global_policy/vlan_pools. 

There are 2 files already there: <b>template.j2</b> and <b>vlan_pools_tmpl.yml</b>.
- <b>template.j2</b> - is jinja2 template. You usually don'r need to change it.
- <b>vlan_pools_tmpl.yml</b> - this file we are going to use for our yaml file creation (if it has not been done before)

2. Create new folder (if it has not been done before). Really you may use any folder, but it looks reasonable to creare a new folder in the curent one. Let's create a folder "example1". 

<b>mkdir example1</b>

3. Copy file vlan_pools_tmpl.yml (if it has not been done before) to this folder and rename it:

<b>cp vlan_pools_tmpl.yml ./example1/vlan_pools.yml</b>
<b>cd ./example1/</b>

4. Fill in <b>vlan_pools.yml</b> with configuration parameters (see access_policies/global_policy/vlan_pools//example1/vlan_pools.yml file)

5. 

5. 



<h4>What is ACY</h4>

ACY = ACi from Yaml = deployment ACi from Yaml

The idea is to manage the Cisco ACI configuration via text files in YAML format. It allows you to
- use a simple interface for ACI configuration
- think about the configuration parameters only, and not about the command's syntax or GUI-navigation
- use version control systems (for example, based on git) and follow the best practices of development for network infrastructure changes control.

The last point is a significant advantage over some other deployment methods (for example Deployment ACI From Excel).

<h4>Installation</h4>

- clone this project to your local folder
- install python3 with yaml and jinja2 packages
- install Postman

<h4>Python, JINJA2, YAML, XML</h4>

There are 4 different types of files in this project.

- Python files:
  - <b>render.py</b> - used for generating of XML file for ACI configuration from YAML and JINJA2 files
  - postman/<b>create_collection.py</b> - used for creation POSTMAN collection from the individual API requests
- JINJA2 files:
  - <b>template.j2</b> - templates, used for generating of XML files for ACI configuration from YAML files. 
- YAML files:
  - <b>aaep_tmpl.yml</b>, <b>phys_domains_tmpl.yml</b>, <b>vlan_pools_tmpl.yml</b>,..., <b>epg_contract_tmpl.yml</b> - corresponds to created or modified Cisco ACI objects. These are templates for new YAML files creation. These files are located in the same folders as template.j2 files
  - <b>aaep.yml</b>, <b>phys_domains.yml</b>, <b>vlan_pools.yml</b>,..., <b>epg_contract.yml</b> - these files were created for demonstration purposes. They are created from the corresponding tmpl files. For example, aaep_tmpl.yml was used to create aaep.yml.

<h4>How to start ACI configuration</h4>

You don't need to change python scripts and generally you don't need to touch JINJA2 temlates!!
You change only YAML files.

Your usual steps are:

1. fill in the appropriate YAML file with configuration parameters
2. use the python <b>render.py</b> file with the corresponding JINJA2 and YAML files as arguments to create an ACI configuration file. As a result, you will have an XML file for the API reques
3. if necessary, repeat these steps for other configuration objects
4. if necessary, create a POSTMAN collection. Use <b>postman/create_collection.py</b> for this
5. use POSTMAN to upload your individual API requests or collections to ACI

<h4>Example</h4>

<h4>Which ACI objects can been managed with ACY</h4>

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
  
  
<h4>Directory structure</h4>
  
Folders tree is in accordance with ACI policy model (only the main folders are represented here):

access_policies/global_policy/aaep/</br>
access_policies/global_policy/phys_domains/</br>
access_policies/global_policy/vlan_pools/</br>
access_policies/global_policy/vmm_domains/</br>

access_policies/interface_policy/fex_interface_profiles/</br>
access_policies/interface_policy/interface_policies/</br>
access_policies/interface_policy/interface_profiles/</br>
access_policies/interface_policy/int_pol_groups/</br>

access_policies/switch_policy/fex_provisioning/</br>
access_policies/switch_policy/mgmt/</br>
access_policies/switch_policy/ode_provisioning/</br>
access_policies/switch_policy/switch_profiles/</br>
access_policies/switch_policy/sw_pol_groups/</br>
access_policies/switch_policy/vpc_domains/</br>

tenant/app_profiles/bridge_domains/</br>
tenant/app_profiles/contexts/</br>
tenant/app_profiles/end_point_groups/</br>
tenant/app_profiles/epg_static_bindings/</br>
tenant/app_profiles/tenants/</br>

l3out/extenal_epg/l3out_int_profiles/</br>
l3out/extenal_epg/l3out_node_profiles/</br>
l3out/extenal_epg/l3outs/</br>

contract/contracts/epg_contracts/</br>
contract/contracts/filters/</br>
contract/contracts/epg_attach/</br>


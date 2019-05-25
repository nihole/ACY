<h4>What is ACY</h4>

ACY = ACi from Yaml = deployment ACi from Yaml

The idea is to manage the Cisco ACI configuration via text files in YAML format. It allows you to
- use a simple interface for ACI configuration
- think about the configuration parameters only, and not about the command's syntax or GUI-navigation
- use version control systems (for example, based on git) and follow the best practices of development for network infrastructure changes control.

The last point is a significant advantage over some other deployment methods (for example Deployment ACI From Excel).

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
  
  
<h4>Directory tree</h4>
  
│── access_policies</br>
│   │── global_policy</br>
│   │   │── aaep</br>
│   │   │── phys_domains</br>
│   │   │── vlan_pools</br>
│   │   │── vmm_domains</br>
│   │── interface_policy</br>
│   │   │── fex_interface_profiles</br>
│   │   │── interface_policies</br>
│   │   │── interface_profiles</br>
│   │   │── int_pol_groups</br>
│   │── switch_policy</br>
│       │── fex_provisioning</br>
│       │── mgmt</br>
│       │── node_provisioning</br>
│       │── switch_profiles</br>
│       │── sw_pol_groups</br>
│       │── vpc_domains</br>
│── contract</br>
│   │── contracts</br>
│   │── epg_contracts</br>
│   │── filters</br>
│── l3out</br>
│   │── extenal_epg</br>
│   │── l3out_int_profiles</br>
│   │── l3out_node_profiles</br>
│   │── l3outs</br>
│── tenant</br>
    │── app_profiles</br>
    │── bridge_domains</br>
    │── contexts</br>
    │── end_point_groups</br>
    │── epg_static_bindings</br>
    │── tenants</br>


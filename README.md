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
  

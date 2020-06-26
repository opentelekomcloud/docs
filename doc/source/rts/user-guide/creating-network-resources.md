# Creating Network Resources<a name="EN-US_TOPIC_0129640298"></a>

## Application Scenarios<a name="section3371113418372"></a>

This template is used to create a VPC, a subnet, a route, and a route interface in the VPC.

## Example Template<a name="section2886194303710"></a>

```
heat_template_version: 2014-10-16
description: Create a VPC instance.
resources:
  vpc_network:
    type: OS::Neutron::Net
    properties:
      name: network
  vpc_subnet:
    type: OS::Neutron::Subnet
    depends_on: vpc_router
    properties:
      name: subnet
      network_id: { get_resource: vpc_network }
      cidr: CIDR
      dns_nameservers:
        - DNS server
  vpc_router:
    type: OS::Neutron::Router
    properties:
      name: router
      external_gateway_info:
        network: Fip_pool
  vpc_router-interface:
    type: OS::Neutron::RouterInterface
    properties:
      router_id: { get_resource: vpc_router }
      subnet: { get_resource: vpc_subnet }
```


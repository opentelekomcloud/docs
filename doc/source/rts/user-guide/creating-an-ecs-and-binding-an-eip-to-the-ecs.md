# Creating an ECS and Binding an EIP to the ECS<a name="EN-US_TOPIC_0129640292"></a>

## Application Scenarios<a name="section87691730101717"></a>

This template is used to create an ECS and bind an EIP to this ECS.

## Example Template<a name="section15001466172"></a>

```
heat_template_version: 2014-10-16
description: Create an EIP and bind it to ECS.
resources:
  server:
    type: OS::Nova::Server
    properties:
      image: Image Name or ID
      flavor: Flavor Name
      key_name: Key Pair
      networks:
        - port: { get_resource: server_port }
      availability_zone: AZ Name
  server_port:
    type: OS::Neutron::Port
    properties:
      network: Network Name or ID
  floating_ip:  
    type: OS::Neutron::FloatingIP
    depends_on: server
    properties:
      floating_network: admin_external_net
      port_id: { get_resource: server_port }
outputs:
  floating_ip:
    description: The floating ip address of the server.
    value: { get_attr: [floating_ip, floating_ip_address] }
```


# Creating an ECS in a Specified Security Group<a name="EN-US_TOPIC_0129640295"></a>

## Application Scenarios<a name="section87691730101717"></a>

This template is used to create a security group and create an ECS in the security group.

## Example Template<a name="section15001466172"></a>

```
heat_template_version: 2014-10-16
description: This example creates an ECS security group for the instance to give you SSH access.
resources:
  server:
    type: OS::Nova::Server
    properties:
      name: ECS Name
      image: Image Name or ID
      flavor: Flavor Name
      key_name: Key Pair
      networks:
        - port: { get_resource: server_port }
      availability_zone: AZ Name
      security_groups:
        - { get_resource: neutron_security_group }
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
  neutron_security_group:
    type: OS::Neutron::SecurityGroup
    properties:
      name: neutron_security_group
      rules:
        - protocol: tcp
          port_range_min: 22
          port_range_max: 22
          remote_ip_prefix: 0.0.0.0/0
outputs:
  ECSName:
    description: The Name of the ECS instance newly created.
    value: { get_attr: [server, name] }
  floating_ip:
    description: The floating ip address of the server.
    value: { get_attr: [floating_ip, floating_ip_address] }
```


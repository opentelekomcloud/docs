# Creating an ECS<a name="EN-US_TOPIC_0129640291"></a>

## Application Scenarios<a name="section87691730101717"></a>

This template is used to create an ECS.

## Example Template<a name="section15001466172"></a>

```
heat_template_version: 2014-10-16
description: Create a simple ECS instance.
resources:
  nova_serer:
    type: OS::Nova::Server
    properties:
      name: ECS Name
      image: Image Name or ID
      flavor: Flavor Name
      key_name: Key Pair
      networks:
        - network: Network Name or ID
      availability_zone: AZ Name
```


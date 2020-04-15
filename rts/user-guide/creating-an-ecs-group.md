# Creating an ECS Group<a name="EN-US_TOPIC_0129640294"></a>

## Application Scenarios<a name="section87691730101717"></a>

This template is used to create a group of ECSs.

## Example Template<a name="section15001466172"></a>

```
heat_template_version: 2014-10-16
description: Create a group of ECSs.
resources:
  instance_group:
    type: OS::Heat::ResourceGroup
    properties:
      count: Number of resource
      resource_def:
        type: OS::Nova::Server
        properties:
          name: aaaa-%index%
          image: Image Name or ID
          flavor: Flavor Name
          key_name: Key Pair
          networks:
            - network: Network Name or ID
          availability_zone: AZ Name
```


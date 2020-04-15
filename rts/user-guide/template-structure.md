# Template Structure<a name="EN-US_TOPIC_0076468653"></a>

Templates are blueprints for describing infrastructure and architecture and can be used to create stacks. The compiler defines resource requirements and configuration details in the template and describes the dependency between resources.

A template must be in the YAML format and consists of the following parts:

```
heat_template_version: xxxx-xx-xx
# Indicates the template version. This field is mandatory.
description:
# Provides template information, template application scenarios, and architecture. This field is optional.
parameter_groups:
# Indicates the parameter groups and parameter sequence. This field is optional.
parameters:
# Indicates the parameters to be input. Using parameters improves template flexibility and reusability. This field is optional.
resources:
# Indicates user-defined resources (such as VMs, networks, and volumes), dependencies among resources, and configuration details. This field is optional.
outputs:
# Indicates outputs of the created resources. This field is optional.
conditions:
# Indicates the conditions that stack creation time and update time must meet. This field is optional.
```

The following is an example template for creating an ECS.

```
heat_template_version: 2013-05-23

description: Simple template to deploy a single compute instance

parameters:
  key_name:
    type: string
    label: Key Name
    description: Name of key-pair to be used for compute instance
  image_id:
    type: string
    label: Image ID
    description: Image to be used for compute instance
  instance_type:
    type: string
    label: Instance Type
    description: Type of instance (flavor) to be used
  net_id:
    type: string
    label: Network UUID
    description: The network to be used

resources:
  my_instance:
    type: OS::Nova::Server
    properties:
      key_name: { get_param: key_name }
      image: { get_param: image_id }
      flavor: { get_param: instance_type }
      networks: [ { network: { get_param: net_id } } ]
```

Description:

-   **heat\_template\_version**: indicates the HOT template version. The value is a specified version. For details, see  [Template Version](template-version.md).
-   **description**: describes resources to be created using the template. This field is optional and can be user-defined.
-   **parameters**: defines some parameters, which are used in function  **get\_param**  to define resource attributes. This field is optional.
-   **resources**: defines all resources to be created by RTS and dependencies between these resources. This field is the core of the template.  **type**: indicates the resource type.


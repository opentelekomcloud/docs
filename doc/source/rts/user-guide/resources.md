# Resources<a name="EN-US_TOPIC_0076468586"></a>

Resources are specified in the  **resources**  field. This field includes user-defined resources \(such as VMs, networks, and volumes\) and dependencies between them. Each resource has a unique name. Different resources must be placed in different paragraphs. The format is as following:

```
resources:
  <resource ID>:
    type: <resource type>
    properties:
      <property name>: <property value>
    metadata:
      <resource specific metadata>
    depends_on: <resource ID or list of ID>
    update_policy: <update policy>
    deletion_policy: <deletion policy>
```

## Syntax<a name="section16254046183019"></a>

**resource ID**

Indicates the resource ID, which must be unique in the template. You can use this resource ID to create other fields of a template.

**type**

Indicates the type of the resource which is being declared. For example,  **OS::Nova::Server**  indicates an ECS instance. For resource types supported by RTS and their details, see  [Supported Resources](supported-resources.md).

**properties**

The resource attribute is in the key-value format and is an additional option for a resource. For example, you must specify a flavor name for each ECS instance.

An example is provided as follows:

```
resources:
  my_instance:
    type: OS::Nova::Server
    properties:
      flavor: m1.small
```

If no attribute needs to be declared for a resource, resource attributes can be ignored.

**depends\_on**

In the template, you can set  **depends\_on**  to specify that a specific resource is created after the other resource is created. For example, after  **depends\_on**  is set for a resource, this resource can only be created after the resource specified in  **depends\_on**  is created.

As shown in the following code segment,  **WebServer**  is created only after  **DatabaseServer**  is created.

```
heat_template_version: 2013-05-23
resources:
  WebServer:
    type: OS::Nova::Server
    depends_on: DatabaseServer
  DatabaseServer:
    type: OS::Nova::Server
    properties:
      flavor: m1.small
      image: CentOS 7.6 64bit
```

**update\_policy**  and  **deletion\_policy**

In the template, you can set  **update\_policy**  or  **deletion\_policy**  to declare that a resource is retained when the resource stack is updated or deleted. For example, if you want to retain the ECS instance when deleting the stack, you can declare as the following code segment shows:

```
resources:
  ecs_instance:
    type: OS::Nova::Server
    properties:
      flavor: m1.small
      image: CentOS 7.6 64bit
    deletion_policy: Retain
```

In this example, if a stack using the template is deleted, the  **ecs\_instance**  resource is retained.


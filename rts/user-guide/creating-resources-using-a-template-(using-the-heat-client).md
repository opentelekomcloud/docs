# Creating Resources Using a Template \(Using the Heat Client\)<a name="EN-US_TOPIC_0076468591"></a>

After the Heat client is installed and configured, you can use this client to create an ECS.

The required operations are as follows:

1.  [Compile a Template](#section19689531174816): A template is a collection of resources and a blueprint for resource orchestration. Before creating a resource, compile a template according to syntax requirements.
2.  [Create Resources](#section13942639134816): To create an ECS, run commands on the Heat client to create an ECS stack.
3.  [View Resources](#section147919492487): To view resources, run commands on the Heat client to view all resource stacks and details of a specified resource stack.
4.  [Delete Resources](#section15014577483): To delete resources, run commands on the Heat client to delete the resource stack if the stack is no longer used.

## Compile a Template<a name="section19689531174816"></a>

Create a template and name it  **server\_instance.yaml**. The template content is as follows:

```
heat_template_version: 2014-10-16
description: Create a simple ECS instance.
parameters:
  name:
    type: string
    description: Specifies the ECS name.
  image: 
    type: string 
    description: Specifies the image used for creating ECS. The value can be the name or ID of the image.
  flavor: 
    type: string 
    description: Specifies the flavor used for creating ECS.
  key: 
    type: string 
    description: Specifies the key pair used for creating ECS. The value can be the name of the key pair. 
  network_id: 
    type: string 
    description: Specifies the network used for creating ECS. The value can be the name or ID of the network.
  availability_zone:
    type: string
    description: Specifies the name of the AZ to which the ECS belong.

resources:
  nova_serer:
    type: OS::Nova::Server
    properties:
      name: { get_param: name }
      image: { get_param: image } 
      flavor: { get_param: flavor } 
      key_name: { get_param: key } 
      networks: 
        - network: { get_param: network_id }
      availability_zone: { get_param: availability_zone } 
```

This YAML file contains four first-level fields:

-   **heat\_template\_version**: indicates the template version. This field is mandatory.
-   **description**: provides a description for the template. This field is optional.
-   **parameters**: defines template parameters. In this example template, this field defines the ECS name, image name or ID, key pair, specifications, VPC, and AZ. All of these can be used by function  **get\_param**  in  **resources**.
-   **resources**: defines resources to be created by the template. In this example, the resources is an ECS.
-   **type**: defines the resource. You need to enter parameters in  **properties**  when creating a resource. For details, see  [Create Resources](#section13942639134816).

## Create Resources<a name="section13942639134816"></a>

Run the following command on the Heat client to create a resource stack:

**heat stack-create -f **_server\_instance.yaml_** -P 'name=**_ecs\_name_**;image=**_Redhat-6.9_**;flavor=**_m1.medium_**;key=**_keypair\_name_**;network\_id=**_external-network3_**;availability\_zone=**_az\_name_**' **_ecsStack_

In this command,

-   _server\_instance.yaml_: indicates the name of the template file.
-   _ecsStack_: indicates the name of the resource stack to be created. The value can be user-defined.
-   Other variables are values of the parameters defined in the template.

## View Resources<a name="section147919492487"></a>

Perform the following operations to check whether the resource stack is created:

-   Run the following command to query all stacks and check whether the new stack is included:

    **heat stack-list**

-   \(Optional\) Run the following command to view details of the new stack:

    **heat stack-show **_ecsStack_


## Delete Resources<a name="section15014577483"></a>

If you do not need a resource stack any longer, run the following command to delete it:

**heat stack-delete **_ecsStack_


# Creating an AS Configuration<a name="EN-US_TOPIC_0042018362"></a>

An AS configuration defines the specifications of the ECSs to be added to an AS group. The specifications include the ECS image and system disk size.

You can create an AS configuration when creating an AS group. You can also create an AS configuration in advance, and select  **Use existing**  and select the created AS configuration when creating an AS group.

You can use specifications of an existing ECS or create an AS configuration. When creating an AS configuration based on an existing ECS, the parameter configurations, such as the vCPUs, memory, image, disk, and ECS type in the AS configuration are the same as those of the selected ECS by default. For details, see  [Using an Existing ECS to Create an AS Configuration](using-an-existing-ecs-to-create-an-as-configuration.md). If you have special requirements on the ECSs for resource expansion, use a new specifications template to create the AS configuration. In such a case, you can define the new specifications. For details, see  [Using a New Specifications Template to Create an AS Configuration](using-a-new-specifications-template-to-create-an-as-configuration.md).


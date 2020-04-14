# Setting Up an Automatically Scalable Discuz! Forum Website<a name="EN-US_TOPIC_0076160210"></a>

## Overview<a name="section57465090145856"></a>

AS automatically adds instances to an AS group for applications when necessary and removes extra ones when unnecessary. In this way, you do not need to prepare a large number of ECSs for an expected marketing activity or unexpected peak hours, thereby ensuring system reliability and reducing system operating costs.

This section describes how to use services, such as AS, ECS, ELB, and VPC to deploy a web service that can be automatically scaled in and out, for example, the Discuz! forum.

## Prerequisites<a name="section8941180154154"></a>

1.  <a name="li141420388395"></a>A VPC, subnet, security group, and EIP are available.

1.  A load balancer and listener have been created. The VPC obtained in  [1](#li141420388395)  is selected during the load balancer creation.

## Procedure<a name="section72789851688"></a>

**Create an ECS and install the MySQL database on it.**

You can create a relational database using the Relational Database Service \(RDS\) service provided by the cloud platform, or create an ECS and install the database on it. In this section, install the MySQL database on a newly created ECS.

1.  Use the created VPC, security group, and EIP to create the ECS. For instructions about how to create an ECS, see  _Elastic Cloud Server User Guide_.
2.  When the status of the ECS changes to  **Running**, use Xftp or Xshell to log in to the ECS through its EIP, and install and configure the MySQL database.

**Create an ECS and deploy the Discuz! forum on it.**

1.  Create an ECS. For instructions about how to create an ECS, see  _Elastic Cloud Server User Guide___. During the creation, you do not need to bind an EIP to the ECS.
2.  Unbind the EIP from the ECS where the MySQL database is installed and bind the EIP to the ECS where the Discuz! forum is to be deployed.

    You can access the MySQL database through a private network. Therefore, the EIP bound to the ECS where the MySQL database is installed can be unbound and then bound to the ECS where the Discuz! forum is to be deployed. This improves resource utilization. For detailed operations, see  _Virtual Private Cloud User Guide___. After the binding, you can access the ECS through the Internet and install environments, such as PHP and Apache, on the ECS.

3.  Deploy the forum.

    For instructions about how to deploy the Discuz! forum, see officially released Discuz! documents. When configuring parameters, configure the private IP address of the ECS where the MySQL database is installed for the database server; use the username and password authorized for remotely accessing the ECS where the MySQL database is installed to access the MySQL database. After the configuration, you can unbind the EIP from the ECS where the forum is deployed to reduce resource usage.


**Create a private image.**

Use the ECS where the Discuz! forum is deployed to create a private image. This private image is used to create ECSs for automatically expanding capacity in the AS group.

1.  Only a stopped ECS can be used to create a private image. Therefore, stop the ECS where the Discuz! forum is deployed before creating a private image. For detailed operations, see  _Elastic Cloud Server User Guide___.
2.  Use the ECS to create a private image. For detailed operations, see  _Image Management Service User Guide___.

**Create an AS group.**

An AS group consists of a collection of ECSs, AS configurations, and AS policies that have similar attributes and apply to the same application scenario. An AS group is the basis for enabling or disabling AS policies and performing scaling actions. You must create an AS group to automatically increase or decrease the number of ECSs to match the Discuz! forum traffic change.

For instructions about how to create an AS group, see  [Creating an AS Group](creating-an-as-group.md). During the configuration, use the created VPC, subnet, load balancer, and listener.

**Create an AS configuration.**

The AS configuration lists the basic specifications of the ECSs to be automatically added to the AS group in a scaling action.

For instructions about how to create an AS configuration, see  [Using a New Specifications Template to Create an AS Configuration](using-a-new-specifications-template-to-create-an-as-configuration.md). During the configuration, select the private image you have created in the preceding step. Configure other parameters based on service requirements.

**Manually add the ECS to the AS group.**

On the page providing details about the AS group, click the  **Instances**  tab and then  **Add**  to add the ECS where the Discuz! forum is deployed to the AS group. For details, see  [Manually Expanding Resources](manually-expanding-resources.md). You can enable instance protection on this ECS so that it will not be automatically removed from the AS group.

**Create an AS policy.**

An AS policy specifies the conditions for triggering a scaling action. After you create an AS policy for the AS group, AS automatically increases or decreases the number of instances based on the AS policy.

You can configure an alarm-triggered AS policy. When Cloud Eye generates an alarm for a monitoring metric, such as CPU usage, AS automatically increases or decreases the number of instances in the AS group. To suit predictable traffic needs, you can also configure a scheduled or periodic AS policy to expand resources.

For instructions about how to create an AS policy, see  [Dynamically Expanding Resources](dynamically-expanding-resources.md)  and  [Expanding Resources as Planned](expanding-resources-as-planned.md). After an AS policy is created and enabled and when the trigger condition is met, the AS group scales up or down.


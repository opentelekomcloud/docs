# Basic Concepts<a name="EN-US_TOPIC_0192950179"></a>

## AS Group<a name="en-us_topic_0190954061_section198964445291"></a>

An AS group consists of a collection of instances that apply to the same scenario. It is the basis for enabling or disabling AS policies and performing scaling actions.

## AS Configuration<a name="en-us_topic_0190954061_section67175733013"></a>

An AS configuration is a template listing specifications for the instances to be added to an AS group. The specifications include the ECS type, vCPUs, memory, image, , and disk.

## AS Policy<a name="en-us_topic_0190954061_section154776108316"></a>

AS policies can trigger scaling actions to adjust the number of instances in an AS group. An AS policy defines the condition to trigger a scaling action and the operation to be performed during a scaling action. When the trigger condition is met, the system automatically triggers a scaling action.

## Scaling Action<a name="en-us_topic_0190954061_section1340633743111"></a>

A scaling action adds instances to or removes instances from an AS group. It ensures that the number of instances in the application system is the same as the expected number of instances.

## Bandwidth Scaling<a name="en-us_topic_0190954061_section1849311910328"></a>

AS automatically adjusts the bandwidth based on the bandwidth scaling policy you configured.

You can create an AS bandwidth policy based on your service requirements. When the trigger condition is met, the AS service automatically increases, decreases, or set the bandwidth to a specified value based on the action you configured. Three types of bandwidth scaling policies are available, including the alarm, scheduled, and periodic policy.

## Region<a name="en-us_topic_0190954061_section209534610470"></a>

A region is a geographic area where the resources used by AS are located.

AZs in the same region can communicate with each other over an intranet, but AZs in different regions cannot.

Cloud data centers are deployed in locations around the world, including Europe and Asia, and AS applies to different regions. Deploying AS in different regions allows you to tailor policies to better suit your requirements. For example, applications can be designed to meet user requirements in specific regions or comply with local laws or regulations.

## Project<a name="en-us_topic_0190954061_section1896064654713"></a>

A project is used to group and isolate OpenStack resources, including compute, storage, and network resources. A project can be a department or a project team. Multiple projects can be created under one account.


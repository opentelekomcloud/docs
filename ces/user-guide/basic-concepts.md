# Basic Concepts<a name="EN-US_TOPIC_0084572327"></a>

The following concepts are central to your understanding and use of Cloud Eye:

-   [Metrics](#section20446181418613)
-   [Rollup](#section061013819719)
-   [Monitoring Panels](#section983754719710)
-   [Topics](#section06147561378)
-   [Alarm Rules](#section14279171685)
-   [Alarm Templates](#section7358181816813)
-   [User Permission](#section992611851011)
-   [Projects](#section4484122111318)

## Metrics<a name="section20446181418613"></a>

Metrics are the core concept in Cloud Eye. A metric refers to a quantized value of a resource dimension on the cloud platform, such as the ECS CPU usage and memory usage. A metric is a time-dependent variable that generates a series of monitoring data over time. It helps you understand the metric changes over a specified period of time.

## Rollup<a name="section061013819719"></a>

Rollup is the process in which Cloud Eye calculates the average, maximum, minimum, sum, or variance value based on sample raw data reported by each cloud service in specific periods. The calculation period is called rollup period. Currently, Cloud Eye supports the following rollup periods: 5 minutes, 20 minutes, 1 hour, 4 hours, and 24 hours.

## Monitoring Panels<a name="section983754719710"></a>

Monitoring panels allow you to view monitoring data of custom metrics of different services and dimensions. It displays metrics of key services in a centralized way, so that you can get an overview of the service running status and check monitoring details when troubleshooting.

## Topics<a name="section06147561378"></a>

A topic is used to publish messages and subscribe to notifications. Topics provide you with one-to-many publish subscription and message notification functions. You can send messages to different types of endpoints with only one message request. With SMN, Cloud Eye uses various methods to notify you of cloud service resource changes, helping you track running status of cloud services in a timely manner.

## Alarm Rules<a name="section14279171685"></a>

In an alarm rule, you can set the threshold for a cloud service metric. When the status \(such as  **Alarm**  and  **OK**\) of the alarm rule changes, Cloud Eye notifies you by sending emails, text messages, or by sending HTTP/HTTPS requests, avoiding service loss due to resource problems.

## Alarm Templates<a name="section7358181816813"></a>

An alarm template contains one or more alarm rules for a specific service. It can help you quickly create alarm rules for multiple cloud services. This also improves the working efficiency of the O&M personnel.

## User Permission<a name="section992611851011"></a>

By default, the public cloud system provides two types of user permissions by default: user management and resource management. User management permissions can manage users, user groups, and user group permissions. Resource management permissions can control users' operations on cloud service resources.

For details about Cloud Eye user permissions, see  [Permissions](https://docs.otc.t-systems.com/en-us/permissions/index.html).

## Projects<a name="section4484122111318"></a>

A project is used to group and isolate OpenStack resources, such as computing, storage, and network resources. A project can either be a department or a project team. Multiple projects can be created for a single account.


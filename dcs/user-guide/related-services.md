# Related Services<a name="en-us_topic_0054235808"></a>

## Virtual Private Cloud \(VPC\)<a name="section2145100172111"></a>

The VPC service enables users to create private, isolated virtual networks. DCS instances run in VPCs and use the IP addresses and bandwidths of VPCs. VPCs are based on security groups. A security group is a set of access control rules that implements access control for mutually trusted ECSs with the same security protection requirements in the same VPC.

## Elastic Cloud Server \(ECS\)<a name="section136811511192114"></a>

The ECS service provides scalable, on-demand cloud servers for secure, flexible, and efficient application environments, ensuring service reliability. After you create DCS instances, you can connect to them through ECSs.

## Cloud Trace Service \(CTS\)<a name="section1534611415218"></a>

CTS provides a history of operations performed on cloud service resources. With CTS, you can query, audit, and review operations. Traces include operation time, resource objects, resource IDs, requesters' IP addresses, resource operation requests, and responses.

Currently, CTS records the following operations on DCS instances:

-   Creating, starting, restarting, and deleting DCS instances
-   Configuring Redis-specific parameters
-   Changing instance passwords
-   Modifying basic information

## Identity and Access Management \(IAM\)<a name="section1581131722214"></a>

IAM provides identity authentication and permission management. It is used to authenticate access to DCS.

## Cloud Eye<a name="section1769154910216"></a>

Cloud Eye is a secure, scalable monitoring platform. It monitors DCS service metrics and sends notifications if alarms or events occur.

For details about DCS metrics, see  [DCS Metrics](dcs-metrics.md).


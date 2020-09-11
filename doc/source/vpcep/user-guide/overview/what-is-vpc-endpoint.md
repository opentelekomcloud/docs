# What Is VPC Endpoint?<a name="en-us_topic_0131645194"></a>

The VPC Endpoint \(VPCEP\) service enables you to access resources across Virtual Private Clouds \(VPCs\) using a dedicated gateway, without exposing information about servers. VPC endpoints provide secure and private channels to connect your VPC to VPC endpoint services \(cloud services on the current platform or your private services\), providing flexible networking without having to use EIPs.

VPCEP provides two types of resources: VPC endpoint services and VPC endpoints. For details, see  [Application Scenarios](application-scenarios.md).

## VPC Endpoint Services<a name="section17321622426"></a>

VPC endpoint services are cloud services or users' private services that are configured in VPCEP. There are two types of VPC endpoint services: gateway and interface.

-   Gateway VPC endpoint services are cloud services that are configured by operations people and supported by VPCEP.
-   Interface VPC endpoint services include cloud services configured by operations people and private services configured by users.

>![](/images/icon-note.gif) **NOTE:** 
>Cloud services are the services on the current platform that are configured as VPC endpoint services by default. You have no permissions to configure cloud services, but you can select the required cloud service by region when creating a VPC endpoint.
>Currently, VPCEP supports cloud services:  **com.t-systems.otc.eu-de.dns**  and  **com.t-systems.otc.eu-de.obs**.
>Users' private services refer to VPC endpoint services that are configured from users' service resources by users themselves. The resources include enhanced load balancers and ECSs.

## VPC Endpoints<a name="section15116958232"></a>

VPC endpoints are channels for connecting VPCs to VPC endpoint services. You can create an application in your VPC and configure it as an endpoint service. A VPC endpoint can be created in another VPC in the same region and then used as a channel to access the endpoint service. There are two types of VPC endpoints: interface and gateway.

-   An interface VPC endpoint is an elastic network interface with a private IP address that serves as an entry point for traffic destined to a VPC endpoint service.
-   A gateway VPC endpoint is a gateway that is a target for a specified route, used for traffic directed to a VPC endpoint service.


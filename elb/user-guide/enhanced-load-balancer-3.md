# Enhanced Load Balancer<a name="en-us_elb_04_0001"></a>

## Scenarios<a name="section66038139153210"></a>

For web services that require registration and login, HTTP load balancing is recommended, such as www.taobao.com and www.yhd.com, two online shopping malls in China. The client and load balancer can communicate through a Direct Connect connection or VPN peering connection.

## Prerequisites<a name="section13695314153443"></a>

-   HTTP is used to forward web messages.
-   The sticky session feature is enabled. A cookie ensures that requests of a single user are sent to the same ECS for processing, preventing login exception and timeout.
-   Requests can be evenly distributed. Requests of different users are forwarded to different ECSs to balance the load.
-   Service faults can be quickly detected and isolated.

## Configuration Reference<a name="section45468134153625"></a>

-   Select a protocol.
    -   HTTP
-   Select an algorithm.
    -   Weighted round robin


-   Enable the sticky session feature.
-   Configure a health check.
    -   Select either TCP or HTTP as the health check protocol. If you select HTTP, you must ensure that an ECS health check page is available and response code 200 is returned when you visit the page.



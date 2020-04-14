# Application Scenarios<a name="EN-US_TOPIC_0093312312"></a>

## High-Traffic Business<a name="section747414212515"></a>

For business with high volume of traffic, ELB evenly distributes incoming traffic to multiple backend servers, for example, large portals and mobile app stores.

You can also enable sticky sessions to ensure that requests from the same client are routed to the same backend server during a session. This improves the access efficiency.

**Figure  1**  Session stickiness<a name="fig145320429220"></a>  
![](figures/session-stickiness.png "session-stickiness")

## Business with Significant Traffic Peaks<a name="section1151610117243"></a>

For business that has significant traffic peaks, integration with AS enables backend servers can be added or removed to keep up with business needs, improving resource utilization. An example is flash sale, which usually lasts for only a few days or even several hours and during which demand on your applications increases rapidly in a short period. To handle the demand, you may need additional servers, which will cost a lot. By combining ELB with AS, you can always run desired number of backend servers.

**Figure  2**  Flexible expansion<a name="fig1927134415176"></a>  
![](figures/flexible-expansion.png "flexible-expansion")

## SPOF Elimination<a name="section430324872511"></a>

ELB periodically performs health checks on backend servers to monitor their health status. If a backend server is considered unhealthy, ELB routes incoming traffic to other healthy ones, ensuring service continuity.

This makes ELB a good choice for services that require high reliability, such as official websites, toll collection systems, and web services.

**Figure  3**  Eliminating SPOFs<a name="fig158310309337"></a>  
![](figures/eliminating-spofs.png "eliminating-spofs")

## Cross-AZ Load Balancing<a name="section220419419265"></a>

Cross-AZ Load Balancing

ELB can distribute traffic across AZs. When an AZ becomes faulty, ELB distributes traffic to backend servers in other AZs that are running properly.

Banking, policing, and large application systems that require high availability can use ELB to achieve this.

**Figure  4**  Traffic distribution to servers in one or more AZs<a name="fig539117712156"></a>  
![](figures/traffic-distribution-to-servers-in-one-or-more-azs.png "traffic-distribution-to-servers-in-one-or-more-azs")


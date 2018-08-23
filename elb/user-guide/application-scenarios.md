# Application Scenarios<a name="en-us_elb_01_0009"></a>

-   High Traffic Services

    For services with high volume of traffic, such as large portals and mobile application stores, ELB evenly distributes the access traffic to multiple backend ECSs. The sticky session feature ensures that requests from the same client are forwarded to the same backend ECS, improving the access efficiency.

-   Services with Significant Traffic Peaks

    ELB automatically scales its request handling capacity according to the incoming traffic. Deep integration with AS enables ELB to automatically add or remove backend ECSs, improving the service flexibility. This makes ELB ideal for services that have significant traffic peaks, such as e-commerce websites, mobile games, and live websites.

-   SPOF Elimination

    ELB routinely performs health checks on backend ECSs to monitor their healthy state. If a backend ECS becomes faulty, ELB automatically distributes incoming requests to healthy backend ECSs, ensuring service continuity.

    This makes ELB the right choice for services that require high reliability, such as official websites, toll collection systems, and common web services.

-   Cross-AZ Load Balancing

    ELB can distribute traffic across AZs. If an AZ becomes faulty, ELB distributes the traffic to backend ECSs in other AZs that are running properly.

    Banking, policing, and large application systems can use ELB to ensure high service availability.



# Classic Load Balancer<a name="EN-US_TOPIC_0118840331"></a>

-   Protocol compliance

    Classic load balancers support the following protocols: TCP, UDP, HTTP, and HTTPS.

-   Health check

    The health check is to monitor the running state of backend ECSs so that load balancer sends requests only to the ECSs that are running properly. After a faulty ECS is restored, the load balancer will send requests to this ECS again. The health check protocols include TCP, UDP, and HTTP.

-   Sticky session

    If the sticky session feature is enabled, all requests from the same client during one session will be sent to the same backend ECS.

-   Load balancing algorithm
    -   **Round robin**: New connection requests are distributed sequentially across all ECSs, so that request workload is evenly shared.
    -   **Least connections**: New connection requests are forwarded to the ECS processing the least number of connections at that time.
    -   **Source IP hash**: The source IP address of the request is used as the hash key to identify an ECS in the static fragment table.
-   SSL offloading

    ELB allows you to manage SSL certificates if you use HTTPS for frontend connections. You do not need to upload the certificates to backend ECSs. The load balancer handles the SSL termination, relieving ECSs of the processing burden of encrypting and/or decrypting traffic sent via SSL.



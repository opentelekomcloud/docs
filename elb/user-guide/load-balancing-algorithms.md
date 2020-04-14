# Load Balancing Algorithms<a name="EN-US_TOPIC_0166390464"></a>

Enhanced load balancers support the following load balancing algorithms:

-   Weighted round robin: Requests are distributed across backend servers in sequence based on their weights. Backend servers with higher weights receive proportionately more requests, whereas equal-weighted servers receive the same number of requests. This algorithm is often used for short connections, such as HTTP services.
-   Weighted least connections: In addition to the number of active connections to each backend server, a weight is assigned to each backend server based on their processing capability. This algorithm is often used for persistent connections, such as database connections.
-   Source IP hash: The source IP address of each request is calculated using the hash algorithm to obtain a unique hash key, and all backend servers are numbered. The generated key allocates the client to a particular server. This enables requests from different clients to be routed and ensures that a client is directed to the same server that it was using previously. This algorithm applies to TCP connections without cookies.

Classic load balancers support the following load balancing algorithms:

-   Round robin: New requests are distributed sequentially across all servers, so that workloads are evenly shared. This algorithm is often used for short connections, such as HTTP services.
-   Least connections: This is a dynamic scheduling algorithm that estimates backend server load based on the number of active connections. New requests are routed to servers with the minimum number of connections. This algorithm is often used for persistent connections, such as database connections.
-   Source IP hash: The source IP address of each request is calculated using the hash algorithm to obtain a unique hash key, and all backend servers are numbered. The generated key allocates the client to a particular server. This enables requests from different clients to be routed and ensures that a client is directed to the same server that it was using previously. This algorithm applies to TCP connections without cookies.

## Server Weight<a name="section8226427131317"></a>

Each backend server can be given a numeral value from 0 to 100 to indicate the proportion of requests to received. New requests will not be forwarded to the backend server whose weight is 0, when the health check result is meaningless. The following algorithms allow you to set the server weight:

-   Weighted round robin: If none of the servers have a weight of 0, the load balancer routes requests to these servers using the round robin algorithm based on their weights. When the weights of backend servers are the same, the weights do not take effect, and the load balancer distributes requests using the round robin algorithm.
-   Weighted least connections: If none of the servers have a weight of 0, the load balancer calculates each server's workload using the formula: Overhead = Number of current connections/Server weight. The load balancer routes new requests to the backend server with the lowest overhead in each request distribution.
-   Source IP hash: The server weight does not take effect. Requests from same IP address are scheduled to the same backend server.

To set the server weight, perform the following operations:

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/en-us_image_0167649573.jpg)  and select the desired region and project.
3.  Click  **Service List**. Under  **Network**, click  **Elastic Load Balancing**.
4.  Locate the target load balancer and click its name.
5.  Click  **Backend Server Groups**, locate the target backend server group and then the target server, and click the number in the  **Weight**  column to set the server weight.
6.  Click  **OK**.


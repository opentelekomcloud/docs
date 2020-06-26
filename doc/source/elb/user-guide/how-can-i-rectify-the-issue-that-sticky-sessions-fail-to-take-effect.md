# How Can I Rectify the Issue that Sticky Sessions Fail to Take Effect?<a name="EN-US_TOPIC_0132401665"></a>

1.  Check whether the sticky session feature is enabled for the backend server group.
2.  Check the health check result of the backend server. If health check result is  **Abnormal**, traffic is routed to other backend servers. As a result, sticky sessions become invalid.
3.  If the  **Source IP hash**  algorithm is selected, check whether the IP address of the request changes before the load balancer receives the request.
4.  If an HTTP or HTTPS listener is configured with the sticky session feature enabled, check whether the request carries a cookie. If yes, check whether the cookie value changes \(because load balancing at Layer 7 uses cookies to maintain sticky sessions\).


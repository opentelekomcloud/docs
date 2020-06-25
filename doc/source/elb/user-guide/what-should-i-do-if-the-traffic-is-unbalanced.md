# What Should I Do If the Traffic Is Unbalanced?<a name="EN-US_TOPIC_0132401670"></a>

1.  Check whether sticky sessions are enabled. If sticky sessions are enabled and there are few clients, imbalance may occur.
2.  Check the health check result of backend servers, especially those whose health statuses change over time. If the health check result is  **Unhealthy**  or switches between  **Healthy**  and  **Unhealthy**, traffic is unbalanced.
3.  Check whether the  **Source IP hash**  algorithm is used. If yes, requests sent from the same IP address are routed to the same backend server, resulting in unbalanced traffic.
4.  Check whether applications on the backend server use Keepalived to maintain TCP persistent connections. If yes, traffic may be unbalanced because the number of requests on persistent connections is different.
5.  Check whether different weights are assigned to backend servers. The traffic varies according to the weights.


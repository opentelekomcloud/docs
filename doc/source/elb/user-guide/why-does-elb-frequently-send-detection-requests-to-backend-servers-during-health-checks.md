# Why Does ELB Frequently Send Detection Requests to Backend Servers During Health Checks?<a name="EN-US_TOPIC_0187476905"></a>

ELB is deployed in cluster mode, and all forwarding nodes in the cluster send detection requests to backend servers at the same time. If the health check interval is too short, health checks are performed once every few seconds. You can set a longer health check interval to control the frequency of health checks by referring to  [Configuring a Health Check](configuring-a-health-check.md).


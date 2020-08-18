# Do DCS Instances in Cluster Mode Support Native Redis Clusters?<a name="en-us_topic_0072544389"></a>

DCS instances in cluster mode do not support native Redis clusters. DCS clusters use the proxy-based cluster mode, so when you query the parameters of the native Redis cluster, DCS retains the default values for some parameters, for example,  **cluster\_enabled:0**.


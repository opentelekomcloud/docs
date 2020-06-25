# Is the EIP Assigned to a Load Balancer Exclusive?<a name="EN-US_TOPIC_0091131382"></a>

During the lifecycle of a classic load balancer, the assigned EIP is exclusive to it. The EIP can be released only when you delete the load balancer.

For an enhanced load balancer, the bound EIP is not exclusive. However, the EIP can be unbound from the load balancer and bound to other resources. After the EIP is unbound, the load balancer becomes a private network load balancer.


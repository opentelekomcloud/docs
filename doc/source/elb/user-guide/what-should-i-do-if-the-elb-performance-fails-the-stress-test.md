# What Should I Do If the ELB Performance Fails the Stress Test?<a name="EN-US_TOPIC_0132401672"></a>

1.  Check the workload of backend servers. If the CPU usage reaches 100%, backend applications may have performance bottlenecks.
2.  Check whether the traffic exceeds the maximum bandwidth of the EIP bound to the load balancer. If the traffic exceeds the bandwidth, a large number of packets are lost and requests fail, affecting the load balancing performance.
3.  In a short connection test, a possible cause is that there are insufficient client ports, which can be checked through the number of connections in the  **time\_wait**  state on the client. You can add IP addresses at the client to solve this problem.
4.  The listening queue backlog of the backend server is full. As a result, the backend server does not respond to SYN ACK packets and connections to the client times out. You can increase the upper limit of the backlog by adjusting the  **net.core.somaxconn**  parameter.


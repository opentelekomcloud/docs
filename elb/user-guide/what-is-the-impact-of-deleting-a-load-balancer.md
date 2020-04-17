# What Is the Impact of Deleting a Load Balancer?<a name="EN-US_TOPIC_0091131363"></a>

If a load balancer is working properly, and its IP address has been correctly resolved to the domain name, do not delete the load balancer unless necessary. Once a load balancer is deleted, the bound IP address is released, and its configuration is deleted and cannot be recovered. If another load balancer is created, the system assigns a new IP address. You can also use the original IP address when creating the load balancer.


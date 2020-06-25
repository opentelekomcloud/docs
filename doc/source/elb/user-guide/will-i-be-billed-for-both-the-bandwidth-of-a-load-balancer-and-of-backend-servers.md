# Will I Be Billed for Both the Bandwidth of a Load Balancer and of Backend Servers?<a name="EN-US_TOPIC_0110855636"></a>

This depends on your business requirements. If a server works in a VPC and has been added to a backend server group associated with a load balancer, you do not need to apply for an EIP and bandwidth for this server because the load balancer handle requests from the client. If your server provides services accessible from the Internet, you must apply an EIP and bandwidth for the server.


# Configuring Security Group Rules<a name="EN-US_TOPIC_0164706625"></a>

## Scenarios<a name="section1348015542318"></a>

Before adding servers to a backend server group, ensure that their security groups have inbound rules that allow traffic from the 100.125.0.0/16 IP address range, and specify the health check protocol and port. Otherwise, health checks cannot be conducted for the added servers. If UDP is used for health checks, inbound security group rules must use the ICMP protocol in addition to allowing traffic from 100.125.0.0/16.

If you have no VPCs when creating a server, the system automatically creates one for you. Default security group rules allow only communications among the servers in the VPC. To ensure that the load balancer can communicate with these servers over both the frontend port and health check port, you need to configure inbound rules for security groups containing these servers.

## Procedure<a name="section20777195619242"></a>

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/icon-region.png)  and select the desired region and project.
3.  Choose  **Computing**  \>  **Elastic Cloud Server**.
4.  In the server list, locate the target ECS and click its name.

    The ECS details page is displayed.

5.  Click  **Security Groups**, locate the target security group, and view security group rules.
6.  Click the security group rule ID or  **Modify Security Group Rule**.

    The security group details page is displayed.

7.  Under  **Inbound Rules**, click  **Add Rule**.

    TCP, HTTP, or HTTPS listeners:

    -   If the health check port is different from the ports of backend servers, the inbound rules must allow TCP traffic from the health check port and backend server ports.
    -   If no health check port is specified, the inbound rules must allow TCP traffic from the ports of backend servers.
    -   In addition, the inbound rules must allow access from 100.125.0.0/16. Otherwise, health checks may fail.

    UDP listeners:

    -   If the health check port is different from the ports of backend servers, the inbound rules must allow UDP traffic from the health check port and backend server ports.
    -   If no health check port is specified, the inbound rules must allow UDP traffic from the ports of backend servers.
    -   The inbound rules must allow access from 100.125.0.0/16. Otherwise, health checks may fail.
    -   The inbound rules must allow ICMP traffic.

    Classic load balancers that work in a private network:

    -   If the health check port is different from the ports of backend servers, the inbound rules must allow TCP traffic from the health check port and backend server ports.
    -   If no health check port is specified, the inbound rules must allow TCP traffic from the ports of backend servers.
    -   The inbound rules must allow access from the VPC CIDR block.

8.  Click  **OK**.

## Firewall Rule<a name="section1261104918577"></a>

A firewall is an optional subnet-class security configuration. You can associate one or more subnets with a firewall for controlling traffic in and out of the subnets. Similar to security groups, firewalls provide access control functions, but add an additional layer of defense to your VPC. Default firewall rules reject all inbound and outbound traffic. If a firewall and load balancer reside in the same subnet, or the firewall and backend servers associated with the load balancer reside in the same subnet, the load balancer cannot receive traffic from the public or private network, or backend servers become unhealthy.

You can configure an inbound firewall rule to permit access from 100.125.0.0/16.

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/icon-region.png)  and select the desired region and project.
3.  On the console homepage, under  **Network**, click  **Virtual Private Cloud**.
4.  In the navigation pane on the left, choose  **Access Control**  \>  **Firewalls**.
5.  Locate the target firewall, and click the firewall name to switch to the page showing details of that particular firewall.
6.  On the  **Inbound Rules**  or  **Outbound Rules**  tab page, click  **Add Rule**  to add an inbound or outbound rule.
    -   **Action**: Select  **Allow**.
    -   **Protocol**: The protocol must be the same as the frontend protocol set when the listener is added.
    -   **Source**: Set the value to  **100.125.0.0/16**.
    -   **Source Port Range**: Select the port range of the service.
    -   **Destination**: Enter default value  **0.0.0.0/0**, which indicates that traffic from all IP addresses is permitted.
    -   **Destination Port Range**: Select the port range of the service.
    -   **Description**: provides supplementary information about the firewall rule. This parameter is optional.

7.  Click  **OK**.


# Binding a Virtual IP Address to an EIP or ECS<a name="en-us_topic_0067802474"></a>

## Scenarios<a name="section20365067202535"></a>

You can bind a virtual IP address to an EIP so that you can access the ECSs can be deployed in active/standby mode for improve fault tolerance.

## Procedure<a name="section1458836202535"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  On the console homepage, under  **Network**, click  **Virtual Private Cloud**.

1.  In the navigation pane on the left, click  **Virtual Private Cloud**.
2.  On the  **Virtual Private Cloud**  page, locate the VPC containing the virtual IP address and click the VPC name.
3.  On the  **Subnets**  tab, click the name of the subnet that the virtual IP address belongs to.
4.  Click the  **Virtual IP Addresses**  tab, locate the row that contains the virtual IP address to be bound to an EIP or ECS, and choose  **Bind to EIP**  or  **Bind to Server**  in the  **Operation**  column.
5.  Select the desired EIP, or ECS and its NIC.

    >![](/images/icon-note.gif) **NOTE:**   
    >-   If the ECS has multiple NICs, bind the virtual IP address to the primary NIC.  
    >-   Multiple virtual IP addresses can be bound to an ECS NIC.  

6.  Click  **OK**.


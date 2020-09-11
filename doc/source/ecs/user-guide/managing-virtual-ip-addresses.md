# Managing Virtual IP Addresses<a name="EN-US_TOPIC_0093492520"></a>

## Scenarios<a name="section040919146466"></a>

A virtual IP address provides the second IP address for one or more ECS NICs, improving high availability between the ECSs.

One NIC can be bound with up to 10 virtual IP addresses, and one virtual IP address can be bound to up to 10 NICs. Multiple ECSs deployed to work in active/standby mode can be bound with the same virtual IP address for disaster recovery.

## Procedure<a name="section194113342460"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  Under  **Computing**, click  **Elastic Cloud Server**.
4.  On the  **Elastic Cloud Server**  page, click the name of the target ECS.

    The page providing details about the ECS is displayed.

5.  Click the  **NICs**  tab. Then, click  **Manage Virtual IP Address**.

    The  **Virtual Private Cloud**  page is displayed.

6.  On the  **Virtual IP Addresses**  tab, select a desired one or click  **Assign Virtual IP Address**  for a new one.
7.  Click  **Bind to Server**  in the  **Operation**  column and select the target ECS name and the NIC to bind the virtual IP address to the ECS NIC.

    For more information about virtual IP addresses, see  _Virtual Private Cloud User Guide_.



# Modifying a Private IP Address<a name="EN-US_TOPIC_0133339807"></a>

## Scenarios<a name="section8230202916388"></a>

The cloud platform allows you to modify the private IP address of the primary NIC. For details, see this section. To modify the private IP address of an extension NIC, delete the NIC and attach a new NIC.

## Constraints<a name="section205851733132119"></a>

-   The ECS must be stopped.
-   If a virtual IP address or DNAT rule has been configured for the NIC, cancel the configuration before modifying the private IP address.
-   If the NIC has an IPv6 address, its private IP address \(IPv4 or IPv6 address\) cannot be modified.
-   Do not modify the private IP address of the ELB backend server.

## Procedure<a name="section101008535219"></a>

1.  Log in to the management console.
2.  Under  **Computing**, click  **Elastic Cloud Server**.
3.  In the search box above the upper right corner of the ECS list, enter the ECS name, IP address, or ID, and click  ![](figures/icon-search.png)  for search.
4.  Click the name of the target ECS.

    The page providing details about the ECS is displayed.

5.  Click the  **NICs**  tab. Locate the row containing the primary NIC and click  **Modify Private IP**.

    The  **Modify Private IP**  dialog box is displayed.

6.  Change the subnet and private IP address of the primary NIC as required.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >Subnets can be changed only within the same VPC.  

    If the target private IP address is not specified, the system will automatically assign one to the primary NIC.



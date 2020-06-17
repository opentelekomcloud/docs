# Creating and Managing a User-defined Network<a name="EN-US_TOPIC_0161727555"></a>

## Create a User-defined Network<a name="section14627174583810"></a>

1.  Log in to the management console.
2.  Under  **Computing**, click  **Bare Metal Server**.

    The BMS console is displayed.

3.  Click the  **User-defined Networks**  tab and click  **Create User-defined Network**.
4.  Set  **Name**,  **VPC**,  **AZ**,  **VLAN**, and  **User-defined Subnet**.

    >![](/images/icon-note.gif) **NOTE:**   
    >-   **User-defined Subnet**: The subnet mask ranges from 16 to 29. The gateway IP address of the user-defined subnet cannot be one used by any other tenant. In addition, the CIDR of the user-defined subnet cannot conflict with that of the VPC subnet.  
    >-   The VLAN ranges from 1 to 4094. User-defined subnets of the same user-defined network must have different VLANs.  

5.  Click  **OK**.

    After the user-defined network is created, you can view its status, VPC, and subnets in the list of user-defined networks.

    >![](/images/icon-note.gif) **NOTE:**   
    >If you have not created a multi-NIC BMS, message "Insufficient multi-NIC BMSs." is displayed and the user-defined network fails to be created.  


## Change the Name of a User-defined Network<a name="section134971020151115"></a>

1.  On the BMS console, click the  **User-defined Networks**  tab. Locate the row that contains the target user-defined network and click  **Modify**  in the  **Operation**  column.
2.  Enter a new name and click  **OK**.

## View Details About a User-defined Network<a name="section27474020111"></a>

1.  On the BMS console, click the  **User-defined Networks**  tab.
2.  In the list of user-defined networks, click the name of the target user-defined network.

    You can view the name, AZ, number of user-defined subnets, and VPC information of the user-defined network.

    You can also change the name of the user-defined network by clicking  ![](figures/edit-icon.png)  next to its name, entering a new name, and then clicking  ![](figures/ok-icon.png).


## Manage a User-defined Subnet<a name="section104731138203313"></a>

-   Add a user-defined subnet.

    On the page showing details of the user-defined network, click  **Add User-defined Subnet**. In the displayed dialog box, enter an IP address, set the VLAN, and click  **OK**.

-   View details about a user-defined subnet.

    In the list of user-defined subnets, click the name of the target user-defined subnet to go to its details page.

    On the  **IP Addresses**  page, you can view the IP address of the user-defined subnet and the EIP bound to the subnet.

    On the  **BMSs**  page, you can view information about all the BMSs with multiple NICs.

-   Modify a user-defined subnet.

    You cannot directly modify a user-defined subnet. You must delete the user-defined network and then create a new user-defined network and a user-defined subnet again.

-   Delete a user-defined subnet.

    In the list of user-defined subnets, locate the target user-defined subnet and click  **Delete**  in the  **Operation**  column.

    If a user-defined network has only one subnet, you are not allowed to delete the subnet.


## Delete a User-defined Network<a name="section15567812133317"></a>

1.  On the BMS console, click the  **User-defined Networks**  tab.
2.  Locate the target user-defined network, click  **Delete**  in the  **Operation**  column, and click  **OK**  in the displayed dialog box.

    After the last multi-NIC BMS using a user-defined network is deleted, the user-defined network will be unavailable and needs to be deleted manually. To use user-defined networks later, you must create new ones.



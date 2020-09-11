# Adding a NIC<a name="sdrs_ug_pi_0006"></a>

## Scenarios<a name="section16935113204812"></a>

If more NICs are required for your protected instance, you can perform steps provided in this section to add a NIC to the protected instance.

## **Prerequisites**<a name="section133210173487"></a>

-   The protection group is in the  **Available**  or  **Protecting**  state.
-   The protected instance is in the  **Available**  or  **Protecting**  state.
-   The subnet of the NIC to be added must belong to the same VPC of the protection group and protected instance.

## Procedure<a name="section858116319480"></a>

1.  Log in to the management console.
2.  Click  **Service List**  and choose  **Storage**  \>  **Storage Disaster Recovery Service**.

    The  **Storage Disaster Recovery Service**  page is displayed.

3.  In the pane of the protection group, click  **Protected Instances**.

    The operation page for the protection group is displayed.

4.  On the  **Protected Instances**  tab, click the protected instance.

    The protected instance details page is displayed.

5.  Click the  **NICs**  tab and click  **Add NIC**.
6.  Select the security group and subnet to be added.

    >![](/images/icon-note.gif) **NOTE:**   
    >-   You can select multiple security groups. When multiple security groups are selected, the access rules of all the selected security groups apply on the server.   
    >-   If you want to add a NIC with a specified IP address, enter an IP address into the  **Private IP Address**  field.   

7.  Click  **OK**. 


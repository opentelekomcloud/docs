# Disabling Protection<a name="sdrs_ug_pg_0001"></a>

## Scenarios<a name="section71411723153618"></a>

If you want to disable protection for all resources in a specified protection group, you can perform steps provided in this section.

Once the protection is disabled, data synchronization for all protected instances in the protection group will stop.

## **Prerequisites**<a name="section15143623143616"></a>

-   The protection group has replication pairs.

-   The protection group is in the  **Protecting**  or  **Disabling protection failed**  state.

## Procedure<a name="section115317232367"></a>

1.  Log in to the management console. 
2.  Click  **Service List**  and choose  **Storage**  \>  **Storage Disaster Recovery Service**.

    The  **Storage Disaster Recovery Service**  page is displayed.

3.  In the pane of the desired protection group, click  **Protected Instances**. 

    The operation page for the protection group is displayed.

4.  In the upper right corner of the page, click  **Disable Protection**.
5.  In the displayed dialog box, click  **Yes**.

    Once the protection is disabled, data synchronization between the production site and DR site for all protected instances in the protection group will stop.



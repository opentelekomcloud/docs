# Manually Switching the Primary and Secondary Nodes of a Replica Set<a name="dds_03_0050"></a>

## **Scenarios**<a name="section34286219201027"></a>

A replica set consists of the primary node, secondary node, and hidden node. Primary and secondary nodes allow access from external services by providing IP addresses. Hidden nodes are only used for backing up data. When a primary node becomes faulty, the system automatically selects a new primary node to ensure high availability. In addition, DDS supports the primary/secondary switchover so you can perform switchovers in scenarios such as disaster recovery.

>![](/images/icon-note.gif) **NOTE:**   
>-   You can perform a switchover when the DB instance status is  **Available**, and  **Changing a security group**.  
>-   Services may be interrupted during the switchover. Ensure that your client supports reconnection.  
>-   The longer the delay for primary/secondary synchronization, the more time is needed for a primary/secondary switchover. Therefore, if the primary to secondary synchronization delay exceeds 300s, the primary/secondary switchover is not allowed. For details about the delay for the primary/secondary synchronization, see  [What Is the Time Delay for Primary/Secondary Synchronization in a Replica Set?](what-is-the-time-delay-for-primary-secondary-synchronization-in-a-replica-set.md)  

## Procedure<a name="section79281543052"></a>

1.  [Log in to the DDS console.](logging-in-to-the-dds-console.md)
2.  On the  **Instance Management**  page, click the target replica set instance.
3.  In the  **Node Information**  area on the  **Basic Information**  page, click  **Switch**.
4.  In the displayed dialog box, click  **Yes**.
5.  Check the result.
    -   During the switchover process, the DB instance status changes to  **Switchover in progress**. After the switchover is complete, the status is restored to  **Available**.
    -   In the  **Node Information**  area, you can view the switchover result.
    -   After the switchover, the previous primary node becomes the secondary node. You need to reconnect to the primary node. For details, see  [Connecting to a DB Instance Through a Client](connecting-to-a-db-instance-through-a-client(replica-set).md).



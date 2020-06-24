# Changing the CPU or Memory of a Cluster DB Instance<a name="en-us_topic_0104472218"></a>

## Scenarios<a name="section38106127132942"></a>

This section guides you on how to change the CPU or memory of a cluster instance.

>![](/images/icon-note.gif) **NOTE:**   
>-   A DB instance cannot be deleted when you are changing its CPU or memory.  
>-   Services will be interrupted for 5 to 10 minutes when you change DB instance CPU and memory. You are advised to perform this operation during off-peak hours.  

## Changing mongos<a name="section9704305161032"></a>

1.  [Log in to the DDS console.](logging-in-to-the-dds-console.md)
2.  On the  **Instance Management**  page, click the target cluster instance.
3.  In the  **Node Information**  area on the  **Basic Information**  page, click the  **mongos**  tab, locate the target mongos, and click  **Change Instance Class**  in the  **Operation**  column.
4.  On the displayed page, modify required parameters and click  **Submit**.
5.  View the DB instance CPU or memory modification result.
    -   When the CPU or memory of a DB instance is being changed, the status displayed in the  **Status**  column is  **Changing instance class**. This process takes about 10 minutes.
    -   In the upper right corner of the DB instance list, click  ![](figures/icon-fresh.png)  to refresh the list. The instance status changes to  **Available**.
    -   In the  **Node Information**  area on the  **Basic Information**  page, click the  **mongos**  tab and check whether the scaling up is successful.


## Changing shard<a name="section5378330161152"></a>

1.  [Log in to the DDS console.](logging-in-to-the-dds-console.md)
2.  On the  **Instance Management**  page, click the target cluster instance.
3.  In the  **Node Information**  area on the  **Basic Information**  page, click the  **shard**  tab, locate the target shard, and click  **Change Instance Class**  in the  **Operation**  column.
4.  On the displayed page, modify required parameters and click  **Submit**.
5.  View the DB instance CPU or memory modification result.
    -   When the CPU or memory of a DB instance is being changed, the status displayed in the  **Status**  column is  **Changing instance class**. This process takes about 25 to 30 minutes.
    -   In the upper right corner of the DB instance list, click  ![](figures/icon-fresh.png)  to refresh the list. The instance status changes to  **Available**.
    -   Go to the  **Basic Information**  page of the cluster instance you scaled up, click the  **shard**  tab in the  **Node Information**  area, and check whether the scaling up is successful. 



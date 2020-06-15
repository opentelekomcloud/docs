# Changing the CPU or Memory of a Replica Set DB Instance<a name="en-us_topic_0104721795"></a>

## **Scenarios**<a name="section161681272206"></a>

This section guides you on how to change the CPU or memory of your replica set instance.

>![](/images/icon-note.gif) **NOTE:**   
>-   A DB instance cannot be deleted when you are changing its CPU or memory.  
>-   Services will be interrupted for 5 to 10 minutes when you change DB instance CPU and memory. You are advised to perform this operation during off-peak hours.  

## Procedure<a name="section4015983017163"></a>

1.  [Log in to the DDS console.](logging-in-to-the-dds-console.md)
2.  On the  **Instance Management**  page, locate the target replica set instance and choose  **Change Instance Class**  in the  **Operation**  column.
3.  On the displayed page, modify required parameters and click  **Submit**.
4.  View the DB instance CPU or memory modification result.
    -   When the CPU or memory of a DB instance is being changed, the status displayed in the  **Status**  column is  **Changing instance class**. This process takes about 25 to 30 minutes.
    -   In the upper right corner of the DB instance list, click  ![](figures/icon-fresh.png)  to refresh the list. The instance status changes to  **Available**.
    -   Go to the  **Basic Information**  page of the replica set instance you scaled up and check whether the scaling up is successful in the  **DB Information**  area.



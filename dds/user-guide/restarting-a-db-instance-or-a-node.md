# Restarting a DB Instance or a Node<a name="dds_03_0003"></a>

## **Scenarios**<a name="section1538841202523"></a>

You may need to restart a DB instance for maintenance purposes. After modifying some parameters, you must restart the DB instance for the modifications to take effect on the management console.

You can restart a DB instance only when its status is  **Available**.

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>-   After you restart a DB instance, services will be interrupted. Exercise caution when performing this operation.  
>-   If you restart a DB instance, all nodes in the instance will be restarted.  

## Restarting a DB Instance<a name="section986617183648"></a>

1.  [Log in to the DDS console.](logging-in-to-the-dds-console.md)
2.  On the  **Instance Management**  page, locate the target DB instance and choose  **More**  \>  **Restart**  in the  **Operation**  column.

    Alternatively, click the target DB instance. On the displayed  **Basic Information**  page, click  **Restart**  in the upper right corner of the page.

3.  In the displayed dialog box, click  **Yes**.
4.  View the restart status.
    1.  On the  **Instance Management**  page, the instance status is  **Restarting**.
    2.  On the  **Basic Information**  page, all nodes of the cluster instance cannot be restarted.


## Restarting a Node \(Cluster\)<a name="section42490975183655"></a>

1.  [Log in to the DDS console.](logging-in-to-the-dds-console.md)
2.  On the  **Instance Management**  page, click the target cluster instance.
3.  In the  **Node Information**  area on the  **Basic Information**  page, click  **mongos**,  **shard**, or  **config**, locate the target node, and click  **Restart**.
4.  In the displayed dialog box, click  **Yes**.
5.  View the node status.

    When one node status is  **Restarting**, other nodes of the instance cannot be restarted.



# Deleting a Manual Backup<a name="en-us_topic_sqlserver_0037000198"></a>

## **Scenarios**<a name="en-us_topic_0037000198_section17499198135414"></a>

This section describes how to delete manual backups to release storage space.

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>Deleted manual backups cannot be recovered. Exercise caution when performing this operation.  

## Procedure<a name="en-us_topic_0037000198_s84d6bef8cb664c9480d4c8fbec48744f"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  In the navigation pane on the left, choose  **Backup Management**. On the displayed page, locate the target manual backup to be deleted and choose  **More**  \>  **Delete**  in the  **Operation**  column.

    The following backups cannot be deleted:

    -   Automated backups
    -   Backups that are being restored
    -   Backups that are being replicated

5.  Click  **Yes**.


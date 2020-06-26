# Changing the Database Port<a name="en-us_topic_change_database_port"></a>

## **Scenarios**<a name="section241540814823"></a>

This section describes how to  change the database port of a primary DB instance or a read replica. For primary/standby DB instances, changing the database port of the primary DB instance will cause the database port of the standby DB instance to also be changed accordingly.

## Constraints<a name="section64561358181355"></a>

You cannot perform the following operations when the database port of a DB instance is being changed:

-   Bind an EIP
-   Delete the DB instance.
-   Create a backup for the DB instance.
-   Restore from backup data or from a specific point in time to the original DB instance.

## Procedure<a name="section45421719172826"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  On the  **Instance Management**  page, click the target DB instance or click  ![](figures/expand.PNG)  first and then click the target read replica.
5.  In the  **Connection Information**  area on the  **Basic Information**  page, click  ![](figures/port.png)  in the  **Database Port**  field.

    >![](/images/icon-note.gif) **NOTE:**   
    >The MySQL database port ranges from 1024 to 65535, excluding 12017 and 33071, which are occupied by the RDS system and cannot be used.  

    -   To submit the change, click  ![](figures/port.png).
        -   In the dialog box, click  **Yes**.
            1.  If you change the database port of the primary DB instance, that of the standby DB instance will also be changed and both DB instances will be rebooted.
            2.  If you change the database port of a read replica, the change will not affect other DB instances. Only the read replica will be rebooted.
            3.  This process takes 1-5 minutes.

        -   In the dialog box, click  **No**  to cancel the modification.

    -   To cancel the change, click  ![](figures/port.png).

6.  View the result of the change on the  **Basic Information**  page.


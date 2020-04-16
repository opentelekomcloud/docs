# Changing the Database Port<a name="en-us_topic_sqlserver_change_database_port"></a>

## **Scenarios**<a name="en-us_topic_0171122564_section241540814823"></a>

This section describes how to  change the database port of a primary DB instance or a read replica. For primary/standby DB instances, changing the database port of the primary DB instance will cause the database port of the standby DB instance to also be changed accordingly.

## Procedure<a name="en-us_topic_0171122564_section45421719172826"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  On the  **Instance Management**  page, click the target DB instance or click  ![](figures/xiala.png)  first and then click the target read replica.
5.  In the  **Connection Information**  area on the  **Basic Information**  page, click  ![](figures/port.png)  in the  **Database Port**  field.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >The Microsoft SQL Server database port is 1433 \(default\) or ranges from 2100 to 9500 \(excluding 5355 and 5985\).   

    -   To submit the change, click  ![](figures/port.png).
        -   In the dialog box, click  **Yes**.
            1.  If you change the database port of the primary DB instance, that of the standby DB instance will also be changed and both DB instances will be rebooted.
            2.  If you change the database port of a read replica, the change will not affect other DB instances. Only the read replica will reboot.

                >![](public_sys-resources/icon-note.gif) **NOTE:**   
                >Currently, RDS for Microsoft SQL Server does not support read replicas.  

            3.  This process takes 1-5 minutes.

        -   In the dialog box, click  **No**  to cancel the modification.

    -   To cancel the change, click  ![](figures/deleat.png).

6.  View the result of the change on the  **Basic Information**  page.


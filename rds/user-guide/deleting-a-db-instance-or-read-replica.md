# Deleting a DB Instance or Read Replica<a name="en-us_topic_0029128192"></a>

## **Scenarios**<a name="section50920834194327"></a>

## Constraints<a name="section815731552410"></a>

DB instance deletion has the following constraints:

-   DB instances cannot be deleted when operations are being performed on them. They can be deleted only after the operations are completed.
-   If you delete a DB instance, its automated backups are also deleted and you are no longer charged for them. Manual backups are still retained and will incur additional costs.

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>-   If you delete a primary DB instance, its read replicas are also deleted automatically. Exercise caution when performing this operation.  
>-   Deleted DB instances cannot be recovered. Exercise caution when performing this operation. If you want to retain data, complete a manual backup before deleting the DB instance.  

## Deleting a DB Instance<a name="section1011433142919"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  On the  **Instance Management**  page, locate the target primary DB instance to be deleted and click  **More**  \>  **Delete**  in the  **Operation**  column.
5.  In the displayed dialog box, click  **Yes**.
6.  Refresh the DB instance list later to check that the deletion is successful.

## Deleting a Read Replica<a name="section486010764714"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  On the  **Instance Management**  page, locate the target DB instance and click  ![](figures/jiantou.png)  in front of it. All the read replicas created for the DB instance are displayed.
5.  Locate the target read replicas to be deleted and click  **More**  \>  **Delete**  in the  **Operation**  column.
6.  In the displayed dialog box, click  **Yes**.
7.  Refresh the DB instance list later to check that the deletion is successful.


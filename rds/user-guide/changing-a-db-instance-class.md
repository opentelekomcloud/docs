# Changing a DB Instance Class<a name="en-us_topic_scale_rds"></a>

## **Scenarios**<a name="section38106127132942"></a>

You can change the  CPU or memory  \(instance class\) of a DB instance as required. If the status of a DB instance changes from  **Changing instance class**  to  **Available**, the change is successful.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>-   A DB instance cannot be deleted while its instance class is being changed.  

## Procedure<a name="section4298797218435"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  On the  **Instance Management**  page, locate the target DB instance and choose  **More**  \>  **Change Instance Class**  in the  **Operation**  column.

    Alternatively, click the target DB instance to go to the  **Basic Information**  page. In the  **DB Information**  area, click  **Change**  in the  **Instance Specifications**  field.

5.  On the displayed page, specify the new instance class and click  **Next**.
6.  View the DB instance class change result.

    -   Changing the DB instance class takes 5–15 minutes. During this period, the status of the DB instance on the  **Instance Management**  page is  **Changing instance class**. After a few minutes, click the DB instance and view the instance class on the displayed  **Basic Information**  page to check that the change is successful.

    >![](public_sys-resources/icon-notice.gif) **NOTICE:**   
    >After you change a MySQL instance class, the values of the following parameters will also be changed accordingly:  **back\_log**,  **innodb\_buffer\_pool\_size**,  **innodb\_log\_buffer\_size**,  **innodb\_log\_files\_in\_group**,  **max\_connections**,  **innodb\_page\_cleaners**,  **innodb\_buffer\_pool\_instances**,  **threadpool\_size**, and  **slave\_parallel\_workers**.  



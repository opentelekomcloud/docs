# Changing a Security Group<a name="en-us_topic_0063388115"></a>

## **Scenarios**<a name="section36712096194014"></a>

This section describes how to change the security group of a primary DB instance or read replica. For primary/standby DB instances, changing the security group of the primary DB instance will cause the security group of the standby DB instance to also be changed accordingly.

## **Procedure**<a name="section59386647165940"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  On the  **Instance Management**  page, click the target DB instance or read replica.
5.  In the  **Connection Information**  area on the  **Basic Information**  page, click  ![](figures/port.png)  in the  **Security Group**  field.
    -   To submit the change, click  ![](figures/insert.png).
    -   To cancel the change, click  ![](figures/deleat.png).

6.  Changing the security group takes 1 to 3 minutes. Click  ![](figures/refresh.png)  in the upper right corner on the  **Basic Information**  page to view the result of the change.


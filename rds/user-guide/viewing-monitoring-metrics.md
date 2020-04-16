# Viewing Monitoring Metrics<a name="rds_06_0003"></a>

## Scenarios<a name="section6512256311344"></a>

The Cloud Eye service monitors operating statuses of RDS DB instances. You can view the RDS monitoring metrics on the management console. For details, see  [Viewing Metrics of Primary DB Instances](#section3645894911344)  and  [Viewing Metrics of Standby DB Instances](#section1479519207209).

Monitored data takes some time for transmission and display. The RDS status displayed on the Cloud Eye console is the status of the last 5 to 10 minutes. If your RDS is newly created, wait for 5 to 10 minutes and then view the monitoring data.

## **Prerequisites**<a name="section5410804111344"></a>

-   RDS is running properly.

    RDS DB instances that are faulty or have been deleted cannot be displayed on the Cloud Eye console. After they are rebooted or restored, you can view their statuses.


>![](public_sys-resources/icon-note.gif) **NOTE:**   
>If an RDS DB instance has been faulty for 24 hours, Cloud Eye considers that it does not exist and deletes it from the monitoring object list. You need to clear the alarm rule for the DB instance.  

-   The relational database has been running properly for about 10 minutes.

    For a newly created DB instance, you need to wait for a while before viewing the monitoring metrics.


## Viewing Metrics of Primary DB Instances<a name="section3645894911344"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  On the  **Instance Management**  page, locate the target DB instance and click  **View Metric**  in the  **Operation**  column to go to the Cloud Eye console.

    Alternatively, click the target DB instance. On the displayed page, click  **View Metric**  in the upper right corner of the page to go to the Cloud Eye console.

    By default, the monitoring information of the primary RDS DB instance is displayed. You can also  [view the monitoring information of the standby DB instance](#section1479519207209).

5.  On the Cloud Eye console, view monitoring information of the primary DB instance.
    -   On the Cloud Eye console, click the target RDS DB instance name and click  **Select Metric**  in the upper right corner. In the displayed dialog box, you can select the metrics to be displayed and sort them by dragging them at desired locations.
    -   You can sort graphs by dragging them based on service requirements.
    -   Cloud Eye can monitor performance metrics from the last 1 hour, 3 hours, 12 hours, 1 day, 7 days, and 30 days.


## Viewing Metrics of Standby DB Instances<a name="section1479519207209"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  On the  **Instance Management**  page, locate the target DB instance and click  **View Metric**  in the  **Operation**  column to go to the Cloud Eye console. By default, the monitoring information of the primary RDS DB instance is displayed.

    Alternatively, click the target DB instance. On the displayed page, click  **View Metric**  in the upper right corner of the page to go to the Cloud Eye console.

5.  On the displayed page, click  ![](figures/ces.png)  to return to the  **Relational Database Service**  page.
6.  In the DB instance list, click  ![](figures/xiala.png)  in front of the target DB instance, locate the standby DB instance, and click  **View Metric**  in the  **Operation**  column to view the monitoring information of the standby DB instance.
7.  On the Cloud Eye console, view monitoring information of the standby DB instance.
    -   On the Cloud Eye console, click the target RDS DB instance name and click  **Select Metric**  in the upper right corner. In the displayed dialog box, you can select the metrics to be displayed and sort them by dragging them at desired locations.
    -   You can sort graphs by dragging them based on service requirements.
    -   Cloud Eye can monitor performance metrics from the last 1 hour, 3 hours, 12 hours, 1 day, 7 days, and 30 days.



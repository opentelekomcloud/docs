# Querying Cloud Service Monitoring Metrics<a name="EN-US_TOPIC_0084572325"></a>

Cloud Eye provides multiple built-in metrics based on the attribute of each service. After you enabled one cloud service on the cloud platform, the system automatically associates its metrics based on the service type. Monitoring of these metrics helps you accurately grasp the service running status.

This topic describes how to view monitoring data of cloud service resources, so if any exception occurs, you can handle it in a timely manner.

## Procedure<a name="section66650441145031"></a>

1.  Log in to the management console.
2.  In the upper left corner, select a region and a project.
3.  Under  **Management & Deployment**, select  **Cloud Eye**.
4.  In the navigation pane on the left, choose  **Cloud Service Monitoring**, and select a cloud service.

    The desired cloud service page is displayed.

5.  Locate the row that contains the target cloud service resource, and click  **View Metric**  in the  **Operation**  column.

    On the displayed page, you can view graphs based on raw data collected in  **1h**,  **3h**, and  **12h**. In the upper right corner of the graph, the maximum and minimum values of the metric in the corresponding time periods are dynamically displayed.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >Metric units can be changed between byte or byte/s and GB or GB/s on graphs. When you are changing the unit, if the maximum value of a metric is smaller than 10^ \(-5\), both the maximum value and the minimum value of this metric are 0. In addition, all data displayed on the graph is 0.  

6.  Hover your mouse over a graph and click  ![](figures/enlarge-querying-cloud-service-monitoring-metrics.png)  in the upper right corner.

    An enlarged graph of this metric is displayed, on which you can view the metric monitoring details in a longer time range. In the upper left corner, you can see six default monitoring periods:  **1h**,  **3h**,  **12h**,  **1d**,  **7d**, and  **30d**. You can also view historical monitoring data for any period during the last six months by customizing the monitoring period.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   If  **1h**,  **3h**,  **12h**, or  **1d**  is selected, raw data is displayed by default. You can click  **Settings**  in the upper left corner of the graph to change the rollup method of the monitoring data.  
    >-   If  **7d**  or  **30d**  is selected, the aggregated data is displayed by default. You can click  **Settings**  in the upper left corner of the graph to change the rollup method of the monitoring data.  



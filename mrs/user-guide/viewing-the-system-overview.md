# Viewing the System Overview<a name="EN-US_TOPIC_0125376053"></a>

On MRS Manager, nodes in a cluster can be classified into management nodes, control nodes, and data nodes. The change trends of key host monitoring metrics on each type of node can be calculated and displayed as curve charts in reports based on the customized periods. If a host belongs to multiple node types, the metric statistics will be repeatedly collected.

This section provides overview of MRS clusters and describes how to view, customize, and export node monitoring metrics on MRS Manager.

## Procedure<a name="section4647134554116"></a>

For MRS 1.9.2 or later, you can display the real-time monitoring reports and historical reports on the same page by performing the following steps.

1.  Log in to MRS Manager. For details, see  [Accessing MRS Manager](accessing-mrs-manager.md).
2.  Choose  **Dashboard**  on MRS Manager.
3.  In  **Period**, you can specify a period to view monitoring data. The options are as follows:
    -   Real time
    -   Last 3 hours
    -   Last 6 hours
    -   Last 24 hours
    -   Last week
    -   Last month
    -   Last 3 months
    -   Last 6 months
    -   Customize: If you select this option, you can customize the period for viewing monitoring data.

4.  Click  **View**  to view monitoring data in a period.
    -   You can view  **Health Status**  and  **Roles**  of each service on the  **Service Summary**  page of MRS Manager.
    -   Click  ![](figures/icon_mrs_question.png)  above the curve chart to view details about a metric.

5.  Customize a monitoring report.
    1.  Click  **Customize**  and select monitoring metrics to be displayed on MRS Manager.

        MRS Manager supports a maximum of 14 monitoring metrics, but at most 12 customized monitoring metrics can be displayed on the page.

        -   Cluster Host Health Status
        -   Cluster Network Read Speed Statistics
        -   Host Network Read Speed Distribution
        -   Host Network Write Speed Distribution
        -   Cluster Disk Write Speed Statistics
        -   Cluster Disk Usage Statistics
        -   Cluster Disk Information
        -   Host Disk Usage Statistics
        -   Cluster Disk Read Speed Statistics
        -   Cluster Memory Usage Statistics
        -   Host Memory Usage Distribution
        -   Cluster Network Write Speed Statistics
        -   Host CPU Usage Distribution
        -   Cluster CPU Usage Statistics

    2.  Click  **OK**  to save the selected monitoring metrics for display.

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >Click  **Clear**  to cancel all the selected monitoring metrics in a batch.  


6.  Set an automatic refresh interval or click  ![](figures/icon_mrs_fresh_r.png)  for an immediate refresh.

    The following refresh interval options are supported:

    -   Refresh every 30 seconds
    -   Refresh every 60 seconds
    -   Stop refreshing

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >If you select  **Full Screen**, the  **Dashboard**  window will be maximized.  


7.  Export a monitoring report.
    1.  Select a period. The options are as follows:
        -   Real time
        -   Last 3 hours
        -   Last 6 hours
        -   Last 24 hours
        -   Last week
        -   Last month
        -   Last 3 months
        -   Last 6 months
        -   Customize: If you select this option, you can customize a time of period to export a report.

    2.  Click  **Export**. MRS Manager will generate a report about the selected monitoring metrics in a specified time of period. Save the report.

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >To view the curve charts of monitoring metrics in a specified period, click  **View**.  



For versions earlier than MRS 1.9.2, you can display the real-time monitoring reports and historical reports on different pages by performing the following steps.

-   Real-time monitoring
    1.  Log in to MRS Manager. For details, see  [Accessing MRS Manager](accessing-mrs-manager.md).
    2.  On MRS Manager, choose  **Dashboard**  \>  **Real-Time Monitoring**.
        -   You can view  **Health Status**  and  **Roles**  of each service on the  **Service Summary**  page of MRS Manager.
        -   The following are some of host monitoring metrics displayed on MRS Manager.

            -   Cluster Host Health Status
            -   Host Network Read Speed Distribution
            -   Host Network Write Speed Distribution
            -   Cluster Disk Information
            -   Host Disk Usage Distribution
            -   Cluster Memory Usage
            -   Host Memory Usage Distribution
            -   Host CPU Usage Distribution
            -   Average Cluster CPU Usage

            You can click  **Customize**  to display the specified monitoring metrics.

    3.  Set an automatic refresh interval or click  ![](figures/icon_mrs_fresh_r.png)  for an immediate refresh.

        The following refresh interval options are supported:

        -   Refresh every 30 seconds
        -   Refresh every 60 seconds
        -   Stop refreshing

            >![](public_sys-resources/icon-note.gif) **NOTE:**   
            >If you select  **Full Screen**, the  **Real-time Monitoring**  window will be maximized.  



-   Historical reports
    1.  View a monitoring report.
        1.  Log in to MRS Manager. For details, see  [Accessing MRS Manager](accessing-mrs-manager.md).
        2.  On MRS Manager, click  **Dashboard**.
        3.  Click  **Historical Report**  to view a report.

            By default, the report displays the monitoring metric statistics of the previous day.

            >![](public_sys-resources/icon-note.gif) **NOTE:**   
            >If you select  **Full Screen**, the  **Historical Report**  window will be maximized.  


    2.  Customize a monitoring report.
        1.  Click  **Customize**  and select monitoring metrics to be displayed on MRS Manager.

            MRS Manager supports a maximum of 8 monitoring metrics, but at most 6 customized monitoring metrics can be displayed on the page.

            -   Cluster Network Read Speed Statistics
            -   Cluster Disk Write Speed Statistics
            -   Cluster Disk Usage Statistics
            -   Cluster Disk Information
            -   Cluster Disk Read Speed Statistics
            -   Cluster Memory Usage Statistics
            -   Cluster Network Write Speed Statistics
            -   Cluster CPU Usage Statistics

        2.  Click  **OK**  to save the selected monitoring metrics for display.

            >![](public_sys-resources/icon-note.gif) **NOTE:**   
            >Click  **Clear**  to cancel all the selected monitoring metrics in a batch.  


    3.  Export a monitoring report.
        1.  Select a period.

            The following options are available:  **Last day**,  **Last week**,  **Last month**,  **Last quarter**, and  **Last half year**

            In  **Time Range**, you can also specify exact start and end time.

        2.  Click  **Export**. MRS Manager will generate a report about the selected monitoring metrics in a specified time of period. Save the report.

            >![](public_sys-resources/icon-note.gif) **NOTE:**   
            >To view the curve charts of monitoring metrics in a specified period, click  **View**.  





# Viewing DDS Metrics<a name="en-us_topic_0044018355"></a>

## Scenarios<a name="section6512256311344"></a>

Cloud Eye monitors DDS running statuses. You can obtain the monitoring metrics of DDS on the management console.

Monitored data requires a period of time for transmission and display. The status of DDS displayed on the Cloud Eye page is the status obtained 5 to 10 minutes before. You can view the monitored data of a newly created DB instance 5 to 10 minutes later.

## **Prerequisites**<a name="section5410804111344"></a>

-   The  DDS DB instance  is running properly.

    Cloud Eye does not display the metrics of a faulty or deleted  DB instance  or node. You can view the monitoring information only after the instance is restarted or recovered.


>![](/images/icon-note.gif) **NOTE:**   
>Cloud Eye will delete a  DDS DB instance  or node that becomes faulty for 24 hours from the monitoring list and will not monitor it any more. However, you need to manually clear its alarm rules.  

-   The  DB instance  has been properly running for at least 10 minutes.

    For a newly created  DB instance, you need to wait for a while before viewing the monitoring metrics.


## Procedure<a name="section4172512173619"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select a region and a project.
3.  Under  **Management & Deployment**, click  **Cloud Eye**.
4.  In the navigation pane on the left, choose  **Cloud Service Monitoring**  \>  **Document Database Service**.
5.  On the displayed page, locate the target instance and click  **View Metric**  in the  **Operation**  column.
6.  In the DDS monitoring area, you can select a duration to view the monitoring data.

    You can view the monitoring data of DDS in the recent 1 hour, 3 hours, or 12 hours. To view the monitoring curve of a longer time range, click  ![](figures/icon-show.png)  to enlarge the graph.



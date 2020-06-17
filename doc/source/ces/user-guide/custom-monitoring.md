# Custom Monitoring<a name="EN-US_TOPIC_0094279601"></a>

The  **Custom Monitoring**  page displays all custom metrics published by users. You can use simple API requests to publish collected monitoring data of those metrics to Cloud Eye for processing and display.

## Viewing Custom Monitoring<a name="section6854181513383"></a>

1.  Log in to the management console.
2.  Under  **Management & Deployment**, select  **Cloud Eye**.
3.  In the navigation pane on the left, choose  **Custom Monitoring**.
4.  On the  **Custom Monitoring**  page, you can view the data published by yourself through API requests, including custom services and metrics.

    >![](/images/icon-note.gif) **NOTE:**   
    >-   Only after you add monitoring data through APIs, will those data be displayed on the Cloud Eye console.  
    >-   For details about how to add monitoring data, see "Adding Monitoring Data" in the  _Cloud Eye API Reference_.  

5.  Locate the row that contains the cloud service resource to be viewed, click  **View Metric**.

    On the displayed page, you can view graphs based on raw data collected in  **1h**,  **3h**, and  **12h**. In the upper right corner of the graph, the maximum and minimum values of the metric in the corresponding time periods are dynamically displayed.


## Creating an Alarm Rule<a name="section20621185993714"></a>

1.  Log in to the management console.
2.  Under  **Management & Deployment**, select  **Cloud Eye**.
3.  In the navigation pane on the left, choose  **Custom Monitoring**.
4.  On the  **Custom Monitoring**  page, locate the target resource and click  **Create Alarm Rule**  in the  **Operation**  column.
5.  In the  **Create Alarm Rule**  dialog box, follow the prompts to set the parameters. For details, see  [Table 2](creating-an-alarm-rule-for-a-specific-metric.md#table4534051437)  and  [Table 3](creating-an-alarm-rule-for-a-specific-metric.md#table7623731163957).
6.  Click  **Finish**.


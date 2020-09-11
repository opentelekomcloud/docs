# Viewing Metrics<a name="css_01_0044"></a>

Cloud Eye provides daily monitoring on core cluster metrics of CSS. You can log in to the Cloud Eye management console to view cluster metrics.

Cloud Eye only monitors clusters that have been successfully created in real time.

## Prerequisites<a name="section1839919421279"></a>

-   The cluster status is  **Available**  or  **Processing**.

    >![](/images/icon-note.gif) **NOTE:**   
    >You cannot view the metrics of deleted clusters or those whose  **Status**  is  **Abnormal**  or  **Creating**  on the Cloud Eye management console. If the status of a cluster changes from  **Abnormal**  or  **Creating**  to  **Available**, you can view its metrics in real time after approximately 10 minutes.  

-   The cluster has been running for about 10 minutes.
-   Alarm rules have been created.

## Procedure<a name="section1482553663115"></a>

1.  Log in to the CSS management console. Click  **Clusters**  to switch to the  **Clusters**  page. Locate the row where the target cluster resides and click  **View Metric**  in the  **Operation**  column to switch to the Cloud Eye management console.
2.  In the left navigation pane, choose  **Cloud Service Monitoring \> Cloud Search Service**.
3.  Locate the row where the target cluster resides, click  **View Graph**  in the  **Operation**  column.
4.  Click the tab for the time range to be viewed.
5.  View the monitoring data.


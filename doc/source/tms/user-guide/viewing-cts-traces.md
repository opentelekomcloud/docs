# Viewing CTS Traces<a name="EN-US_TOPIC_0141727093"></a>

## **Scenarios**<a name="sa2c6542f5aa8472983ddde0bbd969276"></a>

After CTS is enabled, it starts recording operations on cloud resources. The CTS management console stores the last seven days of operation records.

This topic describes how to query or export the last seven days of operation records on the CTS console.

>![](/images/icon-note.gif) **NOTE:**   
>You can also configure TMS key operation notifications on the CTS console. When these key operations are performed, notifications are sent to the related subscribers in real time through SMN. For details, see "Configuring Key Event Notification" in the  _Cloud Trace Service User Guide_.  

## Procedure<a name="se89908b1f430445b8eb519a773c1f8fb"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select a region and project.
3.  Click  **Service List**  and choose  **Management & Deployment**  \>  **Cloud Trace Service**.
4.  In the left navigation pane, choose  **Trace List**.
5.  Click  **Filter**  and specify filters as needed. You can query traces by combining the following filters: 

    **Figure  1**  Specifying filters<a name="en-us_topic_0030598499_fig948065242515"></a>  
    ![](figures/specifying-filters.png "specifying-filters")

    -   **Trace Source**,  **Resource Type**, and  **Search By**

        Select a filter from the drop-down list.

        After you select  **Trace name**  for  **Search By**, you also need to select a trace name.

        After you select  **Resource ID**  for  **Search By**, you also need to select or enter a resource ID.

        After you select  **Resource name**  for  **Search By**, you also need to select or enter a resource name.

    -   **Operator**: Select a specific operator.
    -   **Trace Status**: Select one of  **All trace statuses**,  **normal**,  **warning**, and  **incident**.
    -   Time range: You can select start and end time to query traces generated during a time range of the last seven days.


1.  Click  ![](figures/icon-image-1.jpg)  on the left of the required trace to expand its details.

    **Figure  2**  Expanding trace details<a name="en-us_topic_0030598499_fig60616999161744"></a>  
    ![](figures/expanding-trace-details.png "expanding-trace-details")

2.  Click  **View Trace**  in the  **Operation**  column. On the displayed  **View Trace**  dialog box, the trace structure details are displayed.

    **Figure  3**  View Trace<a name="fig2166141610333"></a>  
    ![](figures/view-trace.png "view-trace")



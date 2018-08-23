# Viewing Traces<a name="en-us_elb_09_0002"></a>

## Scenarios<a name="section71051526193816"></a>

Once CTS is enabled, it starts recording cloud resource operations. You can view the operation records of the last seven days on the management console. This section describes how to query the operation records.

## Procedure<a name="en-us_topic_0107211964_section35541637205812"></a>

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/en-us_image_0114944683.png)  and select the desired region and project.
3.  Click  **Service List**. Under  **Management & Deployment**, click  **Cloud Trace Service**.
4.  In the left navigation pane, choose  **Trace List**.
5.  Specify the filters used for querying traces. The following four filters are available:

    **Figure  1**  Specifying filters<a name="fig15431112015390"></a>
    ![](figures/specifying-filters.png "Specifying filters")

    -   **Trace Source**,  **Resource Type**, and  **Search By**

        Select a filter criterion from the drop-down list.

        When you select  **Trace name**  for  **Search By**, you need to select a specific trace name.

        When you select  **Resource ID**  for  **Search By**, you need to select or enter a specific resource ID.

        When you select  **Resource name**  for  **Search By**, you need to select or enter a specific resource name.

    -   **Operator**: Select a specific operator \(at user level rather than tenant level\).
    -   **Trace Status**: Available options include  **All trace statuses**,  **normal**,  **warning**, and  **incident**. You can only select one of them.
    -   **Time Range**: You can query traces generated during any time range of the last seven days.

6.  Click  ![](figures/en-us_image_0114944782.jpg)  on the left of a trace to expand its details.

    **Figure  2**  Expanding trace details<a name="fig541353043919"></a>
    ![](figures/expanding-trace-details.jpg "Expanding trace details")

7.  Click  **View Trace**  in the  **Operation**  column. On the displayed  **View Trace**  dialog box, view details of the trace.

    **Figure  3**  View Trace<a name="en-us_topic_0107211964_fig2563237145811"></a>
    ![](figures/view-trace.png "View Trace")



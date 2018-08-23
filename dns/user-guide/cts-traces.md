# CTS Traces<a name="EN-US_TOPIC_0109830567"></a>

## **Scenarios**<a name="section9631167098"></a>

After CTS is enabled, the tracker starts recording operations on cloud resources. You can view operation records of the last 7 days on the CTS console.

This section describes how to query these records.

## **Procedure**<a name="section960031713714"></a>

1.  Log in to the management console.
2.  Click ![](figures/en-us_image_0073591874.png) on the upper left and select the desired region and project.
3.  Click **Service List** and select **Cloud Trace Service** under **Management & Deployment**.
4.  In the left navigation pane, choose **Trace List**.
5.  Specify the filters used for querying traces. The following four filters are available:

    **Figure 1** Filters<a name="fig122154711136"></a>
    ![](figures/filters.png "Filters")

    -   **Trace Source**, **Resource Type**, and **Search By**

        Select a filter from the drop-down list.

        When you select **Trace name** for **Search By**, you also need to select a trace name.

        When you select **Resource ID** for **Search By**, you also need to select or enter a resource ID.

        When you select **Resource name** for **Search By**, you also need to select or enter a resource name.

    -   **Operator**: Select an operator.
    -   **Trace Status**: Select one of **All trace statuses**, **normal**, **warning**, and **incident**.
    -   **Time Range**: Select a start and end date and time within the last seven days.
6.  Click ![](figures/en-us_image_0109835572.jpg) on the left of the required trace to expand its details.
7.  Click **View Trace**. A dialog box is displayed, in which the trace structure details are displayed.


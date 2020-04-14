# Viewing CTS Traces<a name="EN-US_TOPIC_0110305015"></a>

1.  Log in to the management console.
2.  Click  ![](figures/en-us_image_0110309702.png)  in the upper left corner of the management console and select a region and project.
3.  Click  **Service List**. Under **Management & Deployment**, choose **Cloud Trace Service**.
4.  Choose  **Trace List**  in the navigation pane on the left.
5.  Specify the filters used for querying traces. The following four filters are available:
    -   **Trace Source**, **Resource Type**, and **Search By**

        Select the filter from the drop-down list.

        When you select  **Trace name** for **Search By**, you also need to select a specific trace name.

        When you select  **Resource ID** for **Search By**, you also need to select or enter a specific resource ID.

        When you select  **Resource name** for **Search By**, you also need to select or enter a specific resource name.

    -   **Operator**: Select a specific operator \(a user other than tenant\).
    -   **Trace Rating**: Available options include **all trace status**, **normal**, **warning**, and **incident**. You can only select one of them.
    -   Start time and end time: You can specify the time period to query traces.

6.  Click  ![](figures/1.png)  on the left of a trace to expand its details.

    **Figure  1**  Expanding trace details<a name="fig042714498141"></a>  
    ![](figures/expanding-trace-details.png "expanding-trace-details")

7.  Click  **View Trace** in the **Operation** column. In the displayed **View Trace**  dialog box, the trace structure details are displayed.

    **Figure  2**  View trace<a name="fig2394142191215"></a>  
    ![](figures/view-trace.png "view-trace")

    For details about the key fields in the CTS trace structure, see  _Cloud Trace Service User Guide_.



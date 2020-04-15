# Viewing Traces<a name="EN-US_TOPIC_0107378004"></a>

## Scenarios<a name="section71051526193816"></a>

CTS records the operations performed on cloud service resources in the form of traces and allows you to view the operation records of the last seven days on the management console. This topic describes how to query these records.

## Procedure<a name="en-us_topic_0107211964_section35541637205812"></a>

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/icon-region.png)  and select the desired region and project.
3.  Under  **Management & Deployment**, click  **Cloud Trace Service**.
4.  In the navigation pane on the left, choose  **Trace List**.
5.  Specify the filters used for querying traces. The following four filters are available:

    **Figure  1**  Filters<a name="fig126816214408"></a>  
    ![](figures/filters.png "filters")

    -   **Trace Source**,  **Resource Type**, and  **Search By**

        Select a filter from the drop-down list.

        If you select  **Trace name**  for  **Search By**, you need to select a specific trace name.

        If you select  **Resource ID**  for  **Search By**, you need to select or enter a specific resource ID.

        If you select  **Resource name**  for  **Search By**, you need to select or enter a specific resource name.

    -   **Operator**: Select a specific operator \(at the user level rather than the tenant level\).
    -   **Trace Status**: Available options include  **All trace statuses**,  **normal**,  **warning**, and  **incident**. You can only select one of them.
    -   Time range: You can query traces generated at any time range of the last seven days.

6.  Click  ![](figures/icon-dropdown.jpg)  on the left of the required trace to expand its details.

    **Figure  2**  Expanding trace details<a name="fig541353043919"></a>  
    ![](figures/expanding-trace-details.png "expanding-trace-details")

7.  Click  **View Trace**  in the  **Operation**  column. In the  **View Trace**  dialog box, view details of the trace.

    **Figure  3**  View Trace<a name="fig196801651891"></a>  
    ![](figures/view-trace.png "view-trace")

    For details about key fields in the trace structure, see the  _Cloud Trace Service User Guide_.



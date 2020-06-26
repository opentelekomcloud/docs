# Viewing Traces<a name="sdrs_ug_cts_0002"></a>

## Scenarios<a name="en-us_topic_0107462582_section32511344104810"></a>

After you enable CTS, the system starts recording operations on SDRS. You can view operation records of the last seven days on the management console.

## Procedure<a name="en-us_topic_0107462582_section1473437092718"></a>

1.  Log in to the management console.
2.  Click  **Service List**  and select  **Cloud Trace Service**  under  **Management & Deployment**.
3.  In the navigation pane on the left, choose  **Trace List**.
4.  In the upper right corner of the trace list, click  **Filter**  to set the search criteria.

    The following four filters are available:

    -   **Trace Source**,  **Resource Type**, and  **Search By**
        -   Select a filter criterion from the drop-down list. Select  **SDRS**  for  **Trace Source**.
        -   When you select  **Trace name**  for  **Search By**, you need to select a specific trace name.
        -   When you select  **Resource ID**  for  **Search By**, you need to select or enter a specific resource ID.
        -   When you select  **Resource name**  for  **Search By**, you need to select or enter a specific resource name.

    -   **Operator**: Select a specific operator \(at user level rather than tenant level\).
    -   **Trace Status**: Available options include  **All trace statuses**,  **normal**,  **warning**, and  **incident**. You can only select one of them.
    -   **Time Range**: You can query traces generated during any time range of the last seven days.

5.  Click  ![](figures/viewing-traces-2.jpg)  on the left of the required trace to expand its details.

    **Figure  1**  Expanding trace details<a name="en-us_topic_0107462582_fig111431836194911"></a>  
    ![](figures/expanding-trace-details.png "expanding-trace-details")

6.  Locate a trace and click  **View Trace**  in the  **Operation**  column.


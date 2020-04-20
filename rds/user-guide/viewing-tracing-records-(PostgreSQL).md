# Viewing Tracing Records<a name="rds_pg_06_0005"></a>

## **Scenarios**<a name="rds_06_0005_section5470822195238"></a>

After CTS is enabled, it starts recording operations on cloud resources. The CTS management console stores the last seven days of operation records.

This section describes how to query the operation records of last 7 days on the CTS console.

## Procedure<a name="rds_06_0005_section46102894133424"></a>

1.  Log in to the management console.
2.  Click  **Service List**. Under  **Management & Deployment**, click  **Cloud Trace Service**.
3.  Choose  **Trace List**  in the navigation pane on the left.
4.  Click  **Filter**  and specify filter criteria as needed. The following four filters are available:
    -   **Trace Source**,  **Resource Type**, and  **Search By**

        Select a filter from the drop-down list.

        When you select  **Trace name**  for  **Search By**, you also need to select a specific trace name.

        When you select  **Resource ID**  for  **Search By**, you also need to select or enter a specific resource ID.

        When you select  **Resource name**  for  **Search By**, you also need to select or enter a specific resource name.

    -   **Operator**: Select a specific operator \(a user rather than a tenant\).
    -   **Trace Status**: Available options include  **All trace statuses**,  **normal**,  **warning**, and  **incident**. You can only select one of them.
    -   Start time and end time: You can specify a time period for querying traces.

5.  Click  ![](figures/expand.PNG)  on the left of the target record to expand its details.
6.  Click  **View Trace**  in the  **Operation**  column. A dialog box is displayed, on which the trace structure details are displayed.


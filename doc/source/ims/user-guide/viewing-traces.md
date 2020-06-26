# Viewing Traces<a name="EN-US_TOPIC_0107462582"></a>

## Scenarios<a name="section32511344104810"></a>

Once CTS is enabled, it starts recording IMS operations. You can view operation records of the last seven days on the management console.

## Procedure<a name="section1473437092718"></a>

1.  Log in to the management console.
2.  Click  **Service List**  and select  **Cloud Trace Service**  under  **Management & Deployment**.
3.  In the navigation pane on the left, choose  **Trace List**.
4.  Click the  **Region**  tab, set the filters, and click  **Query**.

    The following four filters are available:

    -   **Trace Type**,  **Trace Source**,  **Resource Type**, and  **Search By**.
        -   Select a filter criterion from the drop-down list. Select  **Management**  for  **Trace Type**  and  **IMS**  for  **Trace Source**.
        -   If you select  **Resource ID**  for  **Search By**, you need to enter a resource ID. Only whole strings are matched.
        -   When you select  **Resource name**  for  **Search By**, you need to select or enter a specific resource name.

    -   **Operator**: Select a specific operator \(at user level rather than tenant level\).
    -   **Trace Status**: Available options include  **All trace statuses**,  **normal**,  **warning**, and  **incident**. You can only select one of them.
    -   Time range: You can select  **Last 1 hour**,  **Last 1 day**,  **Last 1 week**, and  **Customize**.

5.  Locate the target trace and expand the trace details.
6.  Locate a trace and click  **View Trace**  in the  **Operation**  column.


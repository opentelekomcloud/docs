# Viewing Tracing Logs<a name="EN-US_TOPIC_0116266207"></a>

## Scenarios<a name="section348215012500"></a>

CTS records ECS operations immediately after it is provisioned. You can view the operation records of the last seven days on the management console.

This section describes how to view the operation records.

## Procedure<a name="section19713162125313"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region-0.png)  in the upper left corner and select the desired region and project.
3.  Click  **Service List**. Under  **Management & Deployment**, click  **Cloud Trace Service**.
4.  In the navigation pane on the left, choose  **Trace List**.
5.  Click  **Filter**  and specify filter criteria as needed. The following four filter criteria are available:
    -   **Trace Source**,  **Resource Type**, and  **Search By**

        Select a filter criterion from the drop-down list.

        If you select  **Trace name**  for  **Search By**, you need to select a specific trace name.

        If you select  **Resource ID**  for  **Search By**, you need to select or enter a specific resource ID.

        When you select  **Resource name**  for  **Search By**, you need to select or enter a specific resource name.

    -   **Operator**: Select a specific operator \(which is a user rather than the tenant\).
    -   **Trace Status**: Available options include  **All trace statuses**,  **normal**,  **warning**, and  **incident**. You can only select one of them.
    -   **Time Range**: You can view traces generated during any time range of the last seven days.

6.  Expand the trace for details.

    **Figure  1**  Expanding trace details<a name="fig16725521195316"></a>  
    ![](figures/expanding-trace-details.jpg "expanding-trace-details")

7.  Click  **View Trace**. A dialog box is displayed, in which the trace structure details are displayed.

    For more information about CTS, see  _Cloud Trace Service User Guide_.



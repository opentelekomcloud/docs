# Viewing Audit Logs<a name="css_01_0051"></a>

After CTS is enabled, CTS starts recording operations related to CSS. The CTS management console stores the last seven days of operation records. This section describes how to query the last seven days of operation records on the CTS management console.

## Procedure<a name="section1482553663115"></a>

1.  Log in to the CTS management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select a region.
3.  In the left navigation pane, click  **Trace List**.
4.  You can use filters to query traces. The following four filter criteria are available:
    -   **Trace Source**,  **Resource Type**, and  **Search By**

        Select a filter criterion from the drop-down list.

        When you select  **Trace name**  for  **Search By**, select a specific trace name.

        When you select  **Resource ID**  for  **Search By**, enter a specific resource ID.

        When you select  **Resource name**  for  **Search By**, select or enter a specific resource name.

    -   **Operator**: Select a specific operator \(at user level rather than tenant level\).
    -   **Trace Status**: Available options include  **All trace statuses**,  **normal**,  **warning**, and  **incident**. You can only select one of them.
    -   **Time Range**: You can query traces generated during any time range of the last seven days.

5.  Click  ![](figures/icon-expand.png)  on the left of a trace to expand its details.
6.  Click  **View Trace**  in the  **Operation**  column. In the displayed  **View Trace**  dialog box, the trace structure details are displayed.

    For details about the key fields in the CTS trace structure, see the  [Cloud Trace Service User Guide](https://docs.otc.t-systems.com/en-us/usermanual/cts/en-us_topic_0030579718.html).



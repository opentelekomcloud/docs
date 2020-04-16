# Querying Traces<a name="dds_03_0032"></a>

## Scenarios<a name="en-us_topic_0030598499_section5470822195238"></a>

After CTS is enabled, the tracker starts recording operations on cloud resources. Operation records for the last 7 days are stored on the CTS console.

This section describes how to query operation records for the last 7 days on the CTS console.

## Procedure<a name="en-us_topic_0030598499_section6300091795238"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Management & Deployment**, click  **Cloud Trace Service**.
4.  Choose  **Trace List**  in the navigation pane on the left.
5.  Specify the filters used for querying traces. The following four filters are available: 
    -   **Trace Source**,  **Resource Type**,  **Search By**, and  **Operator**

        Select the filter from the drop-down list.

        When you select  **Trace name**  for  **Search By**, you also need to select a specific trace name.

        When you select  **Resource ID**  for  **Search By**, you also need to select or enter a specific resource ID.

        When you select  **Resource name**  for  **Search By**, you also need to select or enter a specific resource name.

    -   **Operator**: Select a specific operator \(a user rather than tenant\).
    -   **Trace Status**: Available options include  **All trace statuses**,  **normal**,  **warning**, and  **incident**. You can only select one of them.
    -   Start time and end time: You can specify the time period for query traces.

6.  Click  ![](figures/icon-down.png)  on the left of the record to be queried to extend its details.
7.  Locate a trace and click  **View Trace**  in the  **Operation**  column.


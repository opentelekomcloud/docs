# Viewing Audit Logs of Key Operations on the Management Console<a name="dws_01_0118"></a>

DWS uses CTS to record key operation events on the DWS management console. The generated logs can be used in scenarios such as security analysis, compliance audit, resource tracing, and problem locating. This section is organized as follows:

-   [Enabling the Audit Service](#section129109290328)
-   [Disabling the Audit Log Function](#section1247674310321)
-   [Key Operations](#section6775838155314)
-   [Viewing Traces](#section5922593541)

## Enabling the Audit Service <a name="section129109290328"></a>

A tracker will be automatically created after CTS is enabled. All traces recorded by CTS are associated with a tracker. Currently, only one tracker can be created for each account. 

For details about how to enable CTS, see  **Getting Started \> Enabling CTS**  in the  _Cloud Trace Service User Guide_.

1.  On the DWS management console, choose  **Service List**  \>  **Management & Deployment**  \>  **Cloud Trace Service**. The CTS management console is displayed.
2.  In the navigation pane on the left, click  **Tracker**.
3.  Click  **Enable CTS**.
4.  On the page that is displayed, set the OBS bucket and event file prefix.
    -   Select the OBS bucket to be dumped from the  **OBS Bucket**  drop-down list. You can also click  **View Bucket**  to go to the OBS console and click  **Create Bucket**  to create a bucket. For details, see section "Creating a Bucket" in the  _Object Storage Service Console Operation Guide_.
    -   Enter the prefix of the operation event dump file in  **File Prefix**. The value is a string of 0 to 64 characters consisting of letters, digits, hyphens \(-\), underscores \(\_\), and dots \(.\).

5.  Click  **OK**  to enable CTS.

    After CTS is enabled, you can view details about the created tracker on the tracker page.


## Disabling the Audit Log Function<a name="section1247674310321"></a>

If you want to disable the audit log function, disable the tracker in CTS.

1.  On the DWS management console, choose  **Service List**  \>  **Management & Deployment**  \>  **Cloud Trace Service**. The CTS management console is displayed.
2.  In the navigation pane on the left, click  **Tracker**.
3.  In the tracker list, click  **Disable**  in the  **Operation**  column.
4.  In the displayed dialog box, click  **Yes**  to disable the tracker.

    After the tracker is disabled, the  **Disable**  button in the  **Operation**  column is switched to  **Enable**. To enable the tracker again, click  **Enable**  and then click  **Yes**. The system will start recording operations again.

    After the tracker is disabled, the system will stop recording operations, but you can still view existing operation records.


## Key Operations<a name="section6775838155314"></a>

With CTS, you can record operations associated with DWS for later query, audit, and backtrack operations.

**Table  1**  DWS operations that can be recorded by CTS

<a name="table108627353548"></a>
<table><thead align="left"><tr id="row13512483544"><th class="cellrowborder" valign="top" width="25.979999999999997%" id="mcps1.2.4.1.1"><p id="p1035134865418"><a name="p1035134865418"></a><a name="p1035134865418"></a><strong id="b84235270616532"><a name="b84235270616532"></a><a name="b84235270616532"></a>Operation</strong></p>
</th>
<th class="cellrowborder" valign="top" width="31.78%" id="mcps1.2.4.1.2"><p id="p03544855411"><a name="p03544855411"></a><a name="p03544855411"></a><strong id="b84235270616536"><a name="b84235270616536"></a><a name="b84235270616536"></a>Resource</strong></p>
</th>
<th class="cellrowborder" valign="top" width="42.24%" id="mcps1.2.4.1.3"><p id="p1935148115420"><a name="p1935148115420"></a><a name="p1935148115420"></a><strong id="b84235270692033"><a name="b84235270692033"></a><a name="b84235270692033"></a>Event Name</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row3934935145410"><td class="cellrowborder" valign="top" width="25.979999999999997%" headers="mcps1.2.4.1.1 "><p id="p493433512544"><a name="p493433512544"></a><a name="p493433512544"></a>Creating/Restoring a cluster</p>
</td>
<td class="cellrowborder" valign="top" width="31.78%" headers="mcps1.2.4.1.2 "><p id="p6934153545414"><a name="p6934153545414"></a><a name="p6934153545414"></a>cluster</p>
</td>
<td class="cellrowborder" valign="top" width="42.24%" headers="mcps1.2.4.1.3 "><p id="p3934103515413"><a name="p3934103515413"></a><a name="p3934103515413"></a>createCluster</p>
</td>
</tr>
<tr id="row1293463514543"><td class="cellrowborder" valign="top" width="25.979999999999997%" headers="mcps1.2.4.1.1 "><p id="p593443512545"><a name="p593443512545"></a><a name="p593443512545"></a>Deleting a cluster</p>
</td>
<td class="cellrowborder" valign="top" width="31.78%" headers="mcps1.2.4.1.2 "><p id="p179341735105420"><a name="p179341735105420"></a><a name="p179341735105420"></a>cluster</p>
</td>
<td class="cellrowborder" valign="top" width="42.24%" headers="mcps1.2.4.1.3 "><p id="p189341335145413"><a name="p189341335145413"></a><a name="p189341335145413"></a>deleteCluster</p>
</td>
</tr>
<tr id="row179346353547"><td class="cellrowborder" valign="top" width="25.979999999999997%" headers="mcps1.2.4.1.1 "><p id="p6934935115417"><a name="p6934935115417"></a><a name="p6934935115417"></a>Scaling out a cluster</p>
</td>
<td class="cellrowborder" valign="top" width="31.78%" headers="mcps1.2.4.1.2 "><p id="p69341735125415"><a name="p69341735125415"></a><a name="p69341735125415"></a>cluster</p>
</td>
<td class="cellrowborder" valign="top" width="42.24%" headers="mcps1.2.4.1.3 "><p id="p1693403565411"><a name="p1693403565411"></a><a name="p1693403565411"></a>growCluster</p>
</td>
</tr>
<tr id="row4934203595417"><td class="cellrowborder" valign="top" width="25.979999999999997%" headers="mcps1.2.4.1.1 "><p id="p16934135115420"><a name="p16934135115420"></a><a name="p16934135115420"></a>Restarting a cluster</p>
</td>
<td class="cellrowborder" valign="top" width="31.78%" headers="mcps1.2.4.1.2 "><p id="p29351635165416"><a name="p29351635165416"></a><a name="p29351635165416"></a>cluster</p>
</td>
<td class="cellrowborder" valign="top" width="42.24%" headers="mcps1.2.4.1.3 "><p id="p16935935205420"><a name="p16935935205420"></a><a name="p16935935205420"></a>rebootCluster</p>
</td>
</tr>
<tr id="row4935143555411"><td class="cellrowborder" valign="top" width="25.979999999999997%" headers="mcps1.2.4.1.1 "><p id="p1193543545412"><a name="p1193543545412"></a><a name="p1193543545412"></a>Creating a snapshot</p>
</td>
<td class="cellrowborder" valign="top" width="31.78%" headers="mcps1.2.4.1.2 "><p id="p1593563555419"><a name="p1593563555419"></a><a name="p1593563555419"></a>backup</p>
</td>
<td class="cellrowborder" valign="top" width="42.24%" headers="mcps1.2.4.1.3 "><p id="p893583555415"><a name="p893583555415"></a><a name="p893583555415"></a>createBackup</p>
</td>
</tr>
<tr id="row1893543510548"><td class="cellrowborder" valign="top" width="25.979999999999997%" headers="mcps1.2.4.1.1 "><p id="p69351335185410"><a name="p69351335185410"></a><a name="p69351335185410"></a>Deleting a snapshot</p>
</td>
<td class="cellrowborder" valign="top" width="31.78%" headers="mcps1.2.4.1.2 "><p id="p129356358546"><a name="p129356358546"></a><a name="p129356358546"></a>backup</p>
</td>
<td class="cellrowborder" valign="top" width="42.24%" headers="mcps1.2.4.1.3 "><p id="p193513514547"><a name="p193513514547"></a><a name="p193513514547"></a>deleteBackup</p>
</td>
</tr>
<tr id="row893593514540"><td class="cellrowborder" valign="top" width="25.979999999999997%" headers="mcps1.2.4.1.1 "><p id="p11935183575415"><a name="p11935183575415"></a><a name="p11935183575415"></a>Setting security parameters</p>
</td>
<td class="cellrowborder" valign="top" width="31.78%" headers="mcps1.2.4.1.2 "><p id="p69351435205413"><a name="p69351435205413"></a><a name="p69351435205413"></a>configurations</p>
</td>
<td class="cellrowborder" valign="top" width="42.24%" headers="mcps1.2.4.1.3 "><p id="p1693513520544"><a name="p1693513520544"></a><a name="p1693513520544"></a>updateConfigurations</p>
</td>
</tr>
<tr id="row17935113525410"><td class="cellrowborder" valign="top" width="25.979999999999997%" headers="mcps1.2.4.1.1 "><p id="p8935133519544"><a name="p8935133519544"></a><a name="p8935133519544"></a>Creating an MRS data source</p>
</td>
<td class="cellrowborder" valign="top" width="31.78%" headers="mcps1.2.4.1.2 "><p id="p39350352549"><a name="p39350352549"></a><a name="p39350352549"></a>dataSource</p>
</td>
<td class="cellrowborder" valign="top" width="42.24%" headers="mcps1.2.4.1.3 "><p id="p69351235115420"><a name="p69351235115420"></a><a name="p69351235115420"></a>createExtDataSource</p>
</td>
</tr>
<tr id="row13935153525412"><td class="cellrowborder" valign="top" width="25.979999999999997%" headers="mcps1.2.4.1.1 "><p id="p293533595416"><a name="p293533595416"></a><a name="p293533595416"></a>Deleting an MRS data source</p>
</td>
<td class="cellrowborder" valign="top" width="31.78%" headers="mcps1.2.4.1.2 "><p id="p1093553525418"><a name="p1093553525418"></a><a name="p1093553525418"></a>dataSource</p>
</td>
<td class="cellrowborder" valign="top" width="42.24%" headers="mcps1.2.4.1.3 "><p id="p6935113517541"><a name="p6935113517541"></a><a name="p6935113517541"></a>deleteExtDataSource</p>
</td>
</tr>
<tr id="row119354358545"><td class="cellrowborder" valign="top" width="25.979999999999997%" headers="mcps1.2.4.1.1 "><p id="p293633515545"><a name="p293633515545"></a><a name="p293633515545"></a>Updating an MRS data source</p>
</td>
<td class="cellrowborder" valign="top" width="31.78%" headers="mcps1.2.4.1.2 "><p id="p3936535185420"><a name="p3936535185420"></a><a name="p3936535185420"></a>dataSource</p>
</td>
<td class="cellrowborder" valign="top" width="42.24%" headers="mcps1.2.4.1.3 "><p id="p1193610357545"><a name="p1193610357545"></a><a name="p1193610357545"></a>updateExtDataSource</p>
</td>
</tr>
</tbody>
</table>

## Viewing Traces<a name="section5922593541"></a>

1.  On the DWS management console, choose  **Service List**  \>  **Management & Deployment**  \>  **Cloud Trace Service**. The CTS management console is displayed.
2.  In the navigation pane on the left, choose  **Trace List**.
3.  In the upper right corner of the trace list, click  **Filter**  to set the search criteria.

    The following filters are available:

    -   **Trace Source**,  **Resource Type**, and  **Search By**
        -   **Trace Source**: Select  **DWS**.
        -   **Resource Type**: Select  **All resource types**  or specify a resource type.
        -   **Search By**: Select  **All filters**  or any of the following options:
            -   **Trace name**: If you select this option, you also need to select a specific trace name.
            -   **Resource ID**: If you select this option, you also need to select or enter a specific resource ID.
            -   **Resource name**: If you select this option, you also need to select or enter a specific resource name.

    -   **Operator**: Select a specific operator \(at user level rather than tenant level\).
    -   **Trace Status**: Available options include  **All trace statuses**,  **normal**,  **warning**, and  **incident**. You can only select one of them.
    -   **Start Date**  and  **End Date**: You can specify the time period to query traces.

        **Figure  1**  Querying traces<a name="fig3113184315571"></a>  
        ![](figures/querying-traces.png "querying-traces")

4.  Click  **Query**.
5.  Click  ![](figures/icon-dws-expand.png)  on the left of the trace to be queried to extend its details.

    **Figure  2**  Traces<a name="fig1272611231835"></a>  
    ![](figures/traces.png "traces")

6.  Locate the row containing the target trace and click  **View Trace**  in the  **Operation**  column.

    **Figure  3**  Viewing a trace<a name="fig1958255022314"></a>  
    ![](figures/viewing-a-trace.png "viewing-a-trace")

    For details about the key fields in the CTS trace structure, see sections "Trace Structure" and "Trace Examples" in the  _Cloud Trace Service User Guide_.


  


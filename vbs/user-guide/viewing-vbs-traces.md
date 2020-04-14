# Viewing VBS Traces<a name="EN-US_TOPIC_0115393304"></a>

## Scenarios<a name="section11657123312211"></a>

CTS records operations of VBS resources, facilitating query, audit, and backtracking.

## Prerequisites<a name="section149848566220"></a>

You have enabled CTS and the tracker is running properly. For details about how to enable CTS, see section "Enabling CTS" in the  _Cloud Trace Service User Guide_.

## Key Operations Recorded by CTS<a name="section2270183331019"></a>

**Table  1**  VBS operations that can be recorded by CTS

<a name="table3263159911376"></a>
<table><thead align="left"><tr id="en-us_topic_0100240354_row3390765911376"><th class="cellrowborder" valign="top" width="31.630000000000003%" id="mcps1.2.4.1.1"><p id="en-us_topic_0100240354_p6216582611376"><a name="en-us_topic_0100240354_p6216582611376"></a><a name="en-us_topic_0100240354_p6216582611376"></a><strong id="b842352706145343"><a name="b842352706145343"></a><a name="b842352706145343"></a>Operation</strong></p>
</th>
<th class="cellrowborder" valign="top" width="29.59%" id="mcps1.2.4.1.2"><p id="en-us_topic_0100240354_p226716611376"><a name="en-us_topic_0100240354_p226716611376"></a><a name="en-us_topic_0100240354_p226716611376"></a><strong id="b842352706202940"><a name="b842352706202940"></a><a name="b842352706202940"></a>Resource Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="38.78%" id="mcps1.2.4.1.3"><p id="en-us_topic_0100240354_p4942279111376"><a name="en-us_topic_0100240354_p4942279111376"></a><a name="en-us_topic_0100240354_p4942279111376"></a><strong id="b842352706203028"><a name="b842352706203028"></a><a name="b842352706203028"></a>Trace</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0100240354_row4382314011376"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240354_p994147194559"><a name="en-us_topic_0100240354_p994147194559"></a><a name="en-us_topic_0100240354_p994147194559"></a>Create backup</p>
</td>
<td class="cellrowborder" valign="top" width="29.59%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240354_p32415019467"><a name="en-us_topic_0100240354_p32415019467"></a><a name="en-us_topic_0100240354_p32415019467"></a>vbs</p>
</td>
<td class="cellrowborder" valign="top" width="38.78%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0100240354_p46197519194612"><a name="en-us_topic_0100240354_p46197519194612"></a><a name="en-us_topic_0100240354_p46197519194612"></a>bksCreateBackup</p>
</td>
</tr>
<tr id="en-us_topic_0100240354_row13425550164745"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240354_p53644877194559"><a name="en-us_topic_0100240354_p53644877194559"></a><a name="en-us_topic_0100240354_p53644877194559"></a>Delete backup</p>
</td>
<td class="cellrowborder" valign="top" width="29.59%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240354_p3497918019467"><a name="en-us_topic_0100240354_p3497918019467"></a><a name="en-us_topic_0100240354_p3497918019467"></a>vbs</p>
</td>
<td class="cellrowborder" valign="top" width="38.78%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0100240354_p56450887194612"><a name="en-us_topic_0100240354_p56450887194612"></a><a name="en-us_topic_0100240354_p56450887194612"></a>bksDeleteBackup</p>
</td>
</tr>
<tr id="en-us_topic_0100240354_row52057228164742"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240354_p49756873194559"><a name="en-us_topic_0100240354_p49756873194559"></a><a name="en-us_topic_0100240354_p49756873194559"></a>Restore backup</p>
</td>
<td class="cellrowborder" valign="top" width="29.59%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240354_p6556340319467"><a name="en-us_topic_0100240354_p6556340319467"></a><a name="en-us_topic_0100240354_p6556340319467"></a>vbs</p>
</td>
<td class="cellrowborder" valign="top" width="38.78%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0100240354_p14963060194612"><a name="en-us_topic_0100240354_p14963060194612"></a><a name="en-us_topic_0100240354_p14963060194612"></a>bksRestoreBackup</p>
</td>
</tr>
<tr id="en-us_topic_0100240354_row5184876811376"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240354_p33974371194559"><a name="en-us_topic_0100240354_p33974371194559"></a><a name="en-us_topic_0100240354_p33974371194559"></a>Associate backup policy</p>
</td>
<td class="cellrowborder" valign="top" width="29.59%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240354_p1420983619467"><a name="en-us_topic_0100240354_p1420983619467"></a><a name="en-us_topic_0100240354_p1420983619467"></a>autobackup</p>
</td>
<td class="cellrowborder" valign="top" width="38.78%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0100240354_p36435331194612"><a name="en-us_topic_0100240354_p36435331194612"></a><a name="en-us_topic_0100240354_p36435331194612"></a>addPolicyResource</p>
</td>
</tr>
<tr id="en-us_topic_0100240354_row4438670211376"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240354_p4145644194559"><a name="en-us_topic_0100240354_p4145644194559"></a><a name="en-us_topic_0100240354_p4145644194559"></a>Disassociate backup policy</p>
</td>
<td class="cellrowborder" valign="top" width="29.59%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240354_p2420600419467"><a name="en-us_topic_0100240354_p2420600419467"></a><a name="en-us_topic_0100240354_p2420600419467"></a>autobackup</p>
</td>
<td class="cellrowborder" valign="top" width="38.78%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0100240354_p53355430194612"><a name="en-us_topic_0100240354_p53355430194612"></a><a name="en-us_topic_0100240354_p53355430194612"></a>deletePolicyResource</p>
</td>
</tr>
<tr id="en-us_topic_0100240354_row5724132611376"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240354_p2275904194559"><a name="en-us_topic_0100240354_p2275904194559"></a><a name="en-us_topic_0100240354_p2275904194559"></a>Execute backup policy now</p>
</td>
<td class="cellrowborder" valign="top" width="29.59%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240354_p6365492519467"><a name="en-us_topic_0100240354_p6365492519467"></a><a name="en-us_topic_0100240354_p6365492519467"></a>autobackup</p>
</td>
<td class="cellrowborder" valign="top" width="38.78%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0100240354_p40076568194612"><a name="en-us_topic_0100240354_p40076568194612"></a><a name="en-us_topic_0100240354_p40076568194612"></a>actionPolicy</p>
</td>
</tr>
<tr id="en-us_topic_0100240354_row5952941311376"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240354_p48521987194559"><a name="en-us_topic_0100240354_p48521987194559"></a><a name="en-us_topic_0100240354_p48521987194559"></a>Create backup policy</p>
</td>
<td class="cellrowborder" valign="top" width="29.59%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240354_p3221553019467"><a name="en-us_topic_0100240354_p3221553019467"></a><a name="en-us_topic_0100240354_p3221553019467"></a>autobackup</p>
</td>
<td class="cellrowborder" valign="top" width="38.78%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0100240354_p23462620194612"><a name="en-us_topic_0100240354_p23462620194612"></a><a name="en-us_topic_0100240354_p23462620194612"></a>createPolicy</p>
</td>
</tr>
<tr id="en-us_topic_0100240354_row6533293111376"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240354_p6157663194559"><a name="en-us_topic_0100240354_p6157663194559"></a><a name="en-us_topic_0100240354_p6157663194559"></a>Delete backup policy</p>
</td>
<td class="cellrowborder" valign="top" width="29.59%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240354_p6412800619467"><a name="en-us_topic_0100240354_p6412800619467"></a><a name="en-us_topic_0100240354_p6412800619467"></a>autobackup</p>
</td>
<td class="cellrowborder" valign="top" width="38.78%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0100240354_p58599038194612"><a name="en-us_topic_0100240354_p58599038194612"></a><a name="en-us_topic_0100240354_p58599038194612"></a>deletePolicy</p>
</td>
</tr>
<tr id="en-us_topic_0100240354_row913603211376"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240354_p59751623194559"><a name="en-us_topic_0100240354_p59751623194559"></a><a name="en-us_topic_0100240354_p59751623194559"></a>Modify backup policy</p>
</td>
<td class="cellrowborder" valign="top" width="29.59%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240354_p4154723619467"><a name="en-us_topic_0100240354_p4154723619467"></a><a name="en-us_topic_0100240354_p4154723619467"></a>autobackup</p>
</td>
<td class="cellrowborder" valign="top" width="38.78%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0100240354_p37461199194612"><a name="en-us_topic_0100240354_p37461199194612"></a><a name="en-us_topic_0100240354_p37461199194612"></a>modifyPolicy</p>
</td>
</tr>
<tr id="en-us_topic_0100240354_row2742601011376"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240354_p5280694194559"><a name="en-us_topic_0100240354_p5280694194559"></a><a name="en-us_topic_0100240354_p5280694194559"></a>Create backup driven by backup policy</p>
</td>
<td class="cellrowborder" valign="top" width="29.59%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240354_p2183771119467"><a name="en-us_topic_0100240354_p2183771119467"></a><a name="en-us_topic_0100240354_p2183771119467"></a>autobackup</p>
</td>
<td class="cellrowborder" valign="top" width="38.78%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0100240354_p63015595194612"><a name="en-us_topic_0100240354_p63015595194612"></a><a name="en-us_topic_0100240354_p63015595194612"></a>scheduleCreateBackup</p>
</td>
</tr>
<tr id="en-us_topic_0100240354_row6029324011376"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240354_p24420975194559"><a name="en-us_topic_0100240354_p24420975194559"></a><a name="en-us_topic_0100240354_p24420975194559"></a>Delete backup driven by backup policy</p>
</td>
<td class="cellrowborder" valign="top" width="29.59%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240354_p1489109919467"><a name="en-us_topic_0100240354_p1489109919467"></a><a name="en-us_topic_0100240354_p1489109919467"></a>autobackup</p>
</td>
<td class="cellrowborder" valign="top" width="38.78%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0100240354_p35906486194612"><a name="en-us_topic_0100240354_p35906486194612"></a><a name="en-us_topic_0100240354_p35906486194612"></a>scheduleDeleteBackup</p>
</td>
</tr>
<tr id="row153971311133910"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p1139791119391"><a name="p1139791119391"></a><a name="p1139791119391"></a>Add/Modify policy tags</p>
</td>
<td class="cellrowborder" valign="top" width="29.59%" headers="mcps1.2.4.1.2 "><p id="p12397511173920"><a name="p12397511173920"></a><a name="p12397511173920"></a>autobackup</p>
</td>
<td class="cellrowborder" valign="top" width="38.78%" headers="mcps1.2.4.1.3 "><p id="p1739751173919"><a name="p1739751173919"></a><a name="p1739751173919"></a>batchAddPolicyTag</p>
</td>
</tr>
<tr id="en-us_topic_0100240354_row42815477194548"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240354_p57365428194559"><a name="en-us_topic_0100240354_p57365428194559"></a><a name="en-us_topic_0100240354_p57365428194559"></a>Delete policy tags</p>
</td>
<td class="cellrowborder" valign="top" width="29.59%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240354_p6206656619467"><a name="en-us_topic_0100240354_p6206656619467"></a><a name="en-us_topic_0100240354_p6206656619467"></a>autobackup</p>
</td>
<td class="cellrowborder" valign="top" width="38.78%" headers="mcps1.2.4.1.3 "><p id="p166245141324"><a name="p166245141324"></a><a name="p166245141324"></a>batchDeletePolicyTag</p>
</td>
</tr>
<tr id="row888010259143"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p175049251142"><a name="p175049251142"></a><a name="p175049251142"></a>Add/Modify policy tag</p>
</td>
<td class="cellrowborder" valign="top" width="29.59%" headers="mcps1.2.4.1.2 "><p id="p78801258147"><a name="p78801258147"></a><a name="p78801258147"></a>autobackup</p>
</td>
<td class="cellrowborder" valign="top" width="38.78%" headers="mcps1.2.4.1.3 "><p id="p88806256143"><a name="p88806256143"></a><a name="p88806256143"></a>addPolicyTag</p>
</td>
</tr>
<tr id="row14938135218161"><td class="cellrowborder" valign="top" width="31.630000000000003%" headers="mcps1.2.4.1.1 "><p id="p10236105881610"><a name="p10236105881610"></a><a name="p10236105881610"></a>Delete backup policy tag</p>
</td>
<td class="cellrowborder" valign="top" width="29.59%" headers="mcps1.2.4.1.2 "><p id="p17304110181713"><a name="p17304110181713"></a><a name="p17304110181713"></a>autobackup</p>
</td>
<td class="cellrowborder" valign="top" width="38.78%" headers="mcps1.2.4.1.3 "><p id="p15938252191616"><a name="p15938252191616"></a><a name="p15938252191616"></a>deletePolicyTag</p>
</td>
</tr>
</tbody>
</table>

## Viewing CTS Traces<a name="section527989191617"></a>

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/icon-region-6.png)  and select the desired region and project.
3.  Click  **Service List**. Under  **Management & Deployment**, click  **Cloud Trace Service**.
4.  In the navigation pane on the left, choose  **Trace List**.
5.  On the trace list page, click  **Filter**. In the displayed box, specify  **Trace Source**,  **Resource Type**, and  **Search By**, and click  **Query**  to query the specified traces.

    For details about other operations, see section "Querying Real-Time Traces" in the  _Cloud Trace Service User Guide_.


## Disabling or Enabling a Tracker<a name="section8942195284715"></a>

This section describes how to disable an existing tracker on the CTS console. After the tracker is disabled, the system will stop recording operations, but you can still view existing operation records.

1.  Log in to the management console.
2.  In the upper left corner of the page, click  ![](figures/icon-region-6.png)  and select the desired region and project.
3.  Click  **Service List**. Under  **Management & Deployment**, click  **Cloud Trace Service**.
4.  Click  **Tracker**  in the left pane.
5.  Click  **Disable**  on the right of the tracker information.
6.  Click  **OK**.
7.  After the tracker is disabled, its status changes from  **Disable**  to  **Enable**. To enable the tracker again, click  **Enable**  and then click  **OK**. The system will start recording operations again.


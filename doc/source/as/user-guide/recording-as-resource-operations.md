# Recording AS Resource Operations<a name="EN-US_TOPIC_0044702449"></a>

AS can use the Cloud Trace Service \(CTS\) to record resource operations. CTS can record operations performed on the management console, operations performed by calling APIs, and operations triggered within the cloud system.

If you have enabled CTS, when a call is made to the AS API, the operation will be reported to CTS which will then deliver the operation record to a specified OBS bucket for storage. With CTS, you can record operations associated with AS for later query, audit, and backtrack operations.

## Obtaining AS Information in CTS<a name="section43859717155214"></a>

After you enable CTS in the application system, the system logs the API calling operations performed on AS resources. On the  **Cloud Trace Service**  console, you can view operation records for the last 7 days. To obtain more operation records, you can enable the Object Storage Service \(OBS\) and synchronize operation records to the OBS in real time.

[Table 1](#table11766471458)  list the AS operations that can be recorded by CTS.

**Table  1**  AS operations that can be recorded by CTS

<a name="table11766471458"></a>
<table><thead align="left"><tr id="row17179104774518"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.1"><p id="en-us_topic_0100240378_p56684903152351"><a name="en-us_topic_0100240378_p56684903152351"></a><a name="en-us_topic_0100240378_p56684903152351"></a>Operation</p>
</th>
<th class="cellrowborder" valign="top" width="32%" id="mcps1.2.4.1.2"><p id="en-us_topic_0100240378_p28074446152351"><a name="en-us_topic_0100240378_p28074446152351"></a><a name="en-us_topic_0100240378_p28074446152351"></a>Resource Type</p>
</th>
<th class="cellrowborder" valign="top" width="48%" id="mcps1.2.4.1.3"><p id="en-us_topic_0100240378_p59437682152351"><a name="en-us_topic_0100240378_p59437682152351"></a><a name="en-us_topic_0100240378_p59437682152351"></a>Trace Name</p>
</th>
</tr>
</thead>
<tbody><tr id="row4180154711454"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p21801547184515"><a name="p21801547184515"></a><a name="p21801547184515"></a>Creating an AS group</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="p131351545125316"><a name="p131351545125316"></a><a name="p131351545125316"></a>scaling_group</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.4.1.3 "><p id="p201511126195812"><a name="p201511126195812"></a><a name="p201511126195812"></a>CreateScalingGroup</p>
</td>
</tr>
<tr id="row21801747104512"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p0180124719451"><a name="p0180124719451"></a><a name="p0180124719451"></a>Modifying an AS group</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="p1318044764510"><a name="p1318044764510"></a><a name="p1318044764510"></a>scaling_group</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.4.1.3 "><p id="p2141172410586"><a name="p2141172410586"></a><a name="p2141172410586"></a>ModifyScalingGroup</p>
</td>
</tr>
<tr id="row181801547134516"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p91801847124511"><a name="p91801847124511"></a><a name="p91801847124511"></a>Deleting an AS group</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="p31801947164516"><a name="p31801947164516"></a><a name="p31801947164516"></a>scaling_group</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.4.1.3 "><p id="p15135202375816"><a name="p15135202375816"></a><a name="p15135202375816"></a>DeleteScalingGroup</p>
</td>
</tr>
<tr id="row1518064784517"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p7180134774517"><a name="p7180134774517"></a><a name="p7180134774517"></a>Enabling an AS group</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="p7180104744517"><a name="p7180104744517"></a><a name="p7180104744517"></a>scaling_group</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.4.1.3 "><p id="p1852632112589"><a name="p1852632112589"></a><a name="p1852632112589"></a>EnableScalingGroup</p>
</td>
</tr>
<tr id="row518018476452"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p81803474459"><a name="p81803474459"></a><a name="p81803474459"></a>Disabling an AS group</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="p818013471450"><a name="p818013471450"></a><a name="p818013471450"></a>scaling_group</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.4.1.3 "><p id="p1225112005814"><a name="p1225112005814"></a><a name="p1225112005814"></a>DisableScalingGroup</p>
</td>
</tr>
<tr id="row1318110472454"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p11181174754512"><a name="p11181174754512"></a><a name="p11181174754512"></a>Creating an AS configuration</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="p2018174714516"><a name="p2018174714516"></a><a name="p2018174714516"></a>scaling_configuration</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.4.1.3 "><p id="p1918115477454"><a name="p1918115477454"></a><a name="p1918115477454"></a>CreateScalingConfiguration</p>
</td>
</tr>
<tr id="row1181247194512"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p111811747164516"><a name="p111811747164516"></a><a name="p111811747164516"></a>Deleting an AS configuration</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="p11811447144514"><a name="p11811447144514"></a><a name="p11811447144514"></a>scaling_configuration</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.4.1.3 "><p id="p971310174588"><a name="p971310174588"></a><a name="p971310174588"></a>DeleteScalingConfiguration</p>
</td>
</tr>
<tr id="row2181047194519"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p1118111478458"><a name="p1118111478458"></a><a name="p1118111478458"></a>Deleting AS configurations in batches</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="p17181124711457"><a name="p17181124711457"></a><a name="p17181124711457"></a>scaling_configuration</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.4.1.3 "><p id="p14435141655811"><a name="p14435141655811"></a><a name="p14435141655811"></a>BatchDeleteScalingConfiguration</p>
</td>
</tr>
<tr id="row518119477455"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p1418174715457"><a name="p1418174715457"></a><a name="p1418174715457"></a>Creating an AS policy</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="p1181104774517"><a name="p1181104774517"></a><a name="p1181104774517"></a>scaling_policy</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.4.1.3 "><p id="p6120159587"><a name="p6120159587"></a><a name="p6120159587"></a>CreateScalingPolicy</p>
</td>
</tr>
<tr id="row218164744519"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p7181134714518"><a name="p7181134714518"></a><a name="p7181134714518"></a>Modifying an AS policy</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="p1118114477455"><a name="p1118114477455"></a><a name="p1118114477455"></a>scaling_policy</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.4.1.3 "><p id="p594913185818"><a name="p594913185818"></a><a name="p594913185818"></a>ModifyScalingPolicy</p>
</td>
</tr>
<tr id="row818194719454"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p141811147134520"><a name="p141811147134520"></a><a name="p141811147134520"></a>Deleting an AS policy</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="p618154720451"><a name="p618154720451"></a><a name="p618154720451"></a>scaling_policy</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.4.1.3 "><p id="p4181104744514"><a name="p4181104744514"></a><a name="p4181104744514"></a>DeleteScalingPolicy</p>
</td>
</tr>
<tr id="row1418114715457"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p7181164719455"><a name="p7181164719455"></a><a name="p7181164719455"></a>Enabling an AS policy</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="p1018104717454"><a name="p1018104717454"></a><a name="p1018104717454"></a>scaling_policy</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.4.1.3 "><p id="p31836479452"><a name="p31836479452"></a><a name="p31836479452"></a>EnableScalingPolicy</p>
</td>
</tr>
<tr id="row18183104704519"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p18183144724514"><a name="p18183144724514"></a><a name="p18183144724514"></a>Disabling an AS policy</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="p318314474450"><a name="p318314474450"></a><a name="p318314474450"></a>scaling_policy</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.4.1.3 "><p id="p1767021018587"><a name="p1767021018587"></a><a name="p1767021018587"></a>DisableScalingPolicy</p>
</td>
</tr>
<tr id="row131831447174513"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p9183204784515"><a name="p9183204784515"></a><a name="p9183204784515"></a>Executing an AS policy</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="p1218312470450"><a name="p1218312470450"></a><a name="p1218312470450"></a>scaling_policy</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.4.1.3 "><p id="p17059918581"><a name="p17059918581"></a><a name="p17059918581"></a>ExecuteScalingPolicy</p>
</td>
</tr>
<tr id="row13183144713454"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p20183174774519"><a name="p20183174774519"></a><a name="p20183174774519"></a>Removing an instance</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="p15183174714513"><a name="p15183174714513"></a><a name="p15183174714513"></a>scaling_instance</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.4.1.3 "><p id="p1518317825817"><a name="p1518317825817"></a><a name="p1518317825817"></a>RemoveInstance</p>
</td>
</tr>
<tr id="row11183164724520"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p12183164724511"><a name="p12183164724511"></a><a name="p12183164724511"></a>Removing instances in batches</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="p1118317472452"><a name="p1118317472452"></a><a name="p1118317472452"></a>scaling_instance</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.4.1.3 "><p id="p4270187145819"><a name="p4270187145819"></a><a name="p4270187145819"></a>BatchRemoveInstances</p>
</td>
</tr>
<tr id="row101831747164520"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p17183104784520"><a name="p17183104784520"></a><a name="p17183104784520"></a>Adding instances in batches</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="p4183847144510"><a name="p4183847144510"></a><a name="p4183847144510"></a>scaling_instance</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.4.1.3 "><p id="p697015595810"><a name="p697015595810"></a><a name="p697015595810"></a>BatchAddInstances</p>
</td>
</tr>
<tr id="row1618317474459"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p11831247174511"><a name="p11831247174511"></a><a name="p11831247174511"></a>Enabling instance protection in a batch</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="p81839472453"><a name="p81839472453"></a><a name="p81839472453"></a>scaling_instance</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.4.1.3 "><p id="p554844145820"><a name="p554844145820"></a><a name="p554844145820"></a>BatchProtectInstances</p>
</td>
</tr>
<tr id="row81831047174517"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p2184347124514"><a name="p2184347124514"></a><a name="p2184347124514"></a>Disabling instance protection in a batch</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="p20184174714511"><a name="p20184174714511"></a><a name="p20184174714511"></a>scaling_instance</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.4.1.3 "><p id="p42379265818"><a name="p42379265818"></a><a name="p42379265818"></a>BatchUnprotectInstances</p>
</td>
</tr>
<tr id="row192564352517"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p1425611318259"><a name="p1425611318259"></a><a name="p1425611318259"></a>Deleting a tag</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="p18256183172516"><a name="p18256183172516"></a><a name="p18256183172516"></a>scaling_tag</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.4.1.3 "><p id="p42561535256"><a name="p42561535256"></a><a name="p42561535256"></a>deleteScalingTag</p>
</td>
</tr>
<tr id="row1950914617255"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p17509106182514"><a name="p17509106182514"></a><a name="p17509106182514"></a>Creating or Updating a tag</p>
</td>
<td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="p950916172514"><a name="p950916172514"></a><a name="p950916172514"></a>scaling_tag</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.4.1.3 "><p id="p150417563254"><a name="p150417563254"></a><a name="p150417563254"></a>updateScalingTag</p>
</td>
</tr>
</tbody>
</table>

## Viewing Audit Logs<a name="section1953623116339"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region-2.png)  in the upper left corner to select a region and a project.
3.  Click  **Service List**. Choose  **Management & Deployment**  \>  **Cloud Trace Service**.
4.  Click  **Trace List**  in the navigation pane on the left.
5.  You can use filters to query traces. The following filters are available:
    -   **Trace Source**,  **Resource Type**, and  **Search By**

        Select a filter criterion from the drop-down list.

        When you select  **Trace name**  for  **Search By**, you need to select a specific trace name.

        When you select  **Resource ID**  for  **Search By**, you need to select or enter a specific resource ID.

        When you select  **Resource name**  for  **Search By**, you need to select or enter a specific resource name.

    -   **Operator**: Select a specific operator \(at user level rather than tenant level\).
    -   **Trace Status**: Available options include  **All trace statuses**,  **normal**,  **warning**, and  **incident**. You can only select one of them.
    -   Start time and end time: You can specify the time period to query traces.

6.  Click  ![](figures/en-us_image_0108911462.jpg)  on the left of the required trace to expand its details.
7.  Locate the required trace and click  **View Trace**  in the  **Operation**  column. A dialog box is displayed, showing the trace content.

## CTS Log Entries<a name="section54032088155336"></a>

Each log entry consists of a trace in JSON format. A log entry indicates an AS API request, including the requested operation, the operation date and time, operation parameters, and information about the user who sends the request. The user information is obtained from the Identity and Access Management \(IAM\) service.

The following example shows CTS log entries for the  **CreateScalingPolicy**  action:

```
{
"time": "2016-12-15 15:27:40 GMT+08:00",
"user": {
"name": "xxxx",
"id": "62ff83d2920e4d3d917e6fa5e31ddebe",
"domain": {
"name": "xxx",
"id": "30274282b09749adbe7d9cabeebcbe8b"
}
},
"request": {
"scaling_policy_name": "as-policy-oonb",
"scaling_policy_action": {
"operation": "ADD",
"instance_number": 1
},
"cool_down_time": "",
"scheduled_policy": {
"launch_time": "2016-12-16T07:27Z"
},
"scaling_policy_type": "SCHEDULED",
"scaling_group_id": "ec4051a7-6fbd-42d2-840f-2ad8cdabee34"
},
"response": {
"scaling_policy_id": "6a38d488-664b-437a-ade2-dc45f96f7f4c"
},
"code": 200,
"service_type": "AS",
"resource_type": "scaling_policy",
"resource_name": "as-policy-oonb",
"resource_id": "6a38d488-664b-437a-ade2-dc45f96f7f4c",
"source_ip": "10.190.205.233",
"trace_name": "createScalingPolicy",
"trace_rating": "normal",
"trace_type": "ConsoleAction",
"api_version": "1.0",
"record_time": "2016-12-15 15:27:40 GMT+08:00",
"trace_id": "f627062b-c297-11e6-a606-eb2c0f48bec5"
}
```


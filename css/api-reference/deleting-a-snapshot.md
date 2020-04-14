# Deleting a Snapshot<a name="css_03_0036"></a>

## Function<a name="section874853215915"></a>

This API is used to delete a snapshot.

## URI<a name="section8763193210910"></a>

```
DELETE /v1.0/{project_id}/clusters/{cluster_id}/index_snapshot/{snapshot_id}
```

**Table  1**  Parameter description

<a name="table57631032695"></a>
<table><thead align="left"><tr id="row4445336913"><th class="cellrowborder" valign="top" width="16.31313131313131%" id="mcps1.2.5.1.1"><p id="p54417338910"><a name="p54417338910"></a><a name="p54417338910"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15.98989898989899%" id="mcps1.2.5.1.2"><p id="p1644733693"><a name="p1644733693"></a><a name="p1644733693"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="17.88888888888889%" id="mcps1.2.5.1.3"><p id="p11441233696"><a name="p11441233696"></a><a name="p11441233696"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="49.80808080808081%" id="mcps1.2.5.1.4"><p id="p124403319916"><a name="p124403319916"></a><a name="p124403319916"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row94414331098"><td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.2.5.1.1 "><p id="p0441331398"><a name="p0441331398"></a><a name="p0441331398"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="15.98989898989899%" headers="mcps1.2.5.1.2 "><p id="p9444331997"><a name="p9444331997"></a><a name="p9444331997"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.88888888888889%" headers="mcps1.2.5.1.3 "><p id="p144412334919"><a name="p144412334919"></a><a name="p144412334919"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.80808080808081%" headers="mcps1.2.5.1.4 "><p id="p18449331896"><a name="p18449331896"></a><a name="p18449331896"></a>Project ID.</p>
</td>
</tr>
<tr id="row14453320917"><td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.2.5.1.1 "><p id="p2044193314920"><a name="p2044193314920"></a><a name="p2044193314920"></a>cluster_id</p>
</td>
<td class="cellrowborder" valign="top" width="15.98989898989899%" headers="mcps1.2.5.1.2 "><p id="p24410331398"><a name="p24410331398"></a><a name="p24410331398"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.88888888888889%" headers="mcps1.2.5.1.3 "><p id="p844133316918"><a name="p844133316918"></a><a name="p844133316918"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.80808080808081%" headers="mcps1.2.5.1.4 "><p id="p13441833493"><a name="p13441833493"></a><a name="p13441833493"></a>ID of the cluster to which the snapshot belongs.</p>
</td>
</tr>
<tr id="row47771537173715"><td class="cellrowborder" valign="top" width="16.31313131313131%" headers="mcps1.2.5.1.1 "><p id="p27779371378"><a name="p27779371378"></a><a name="p27779371378"></a>snapshot_id</p>
</td>
<td class="cellrowborder" valign="top" width="15.98989898989899%" headers="mcps1.2.5.1.2 "><p id="p5777203719370"><a name="p5777203719370"></a><a name="p5777203719370"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.88888888888889%" headers="mcps1.2.5.1.3 "><p id="p177771737153713"><a name="p177771737153713"></a><a name="p177771737153713"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.80808080808081%" headers="mcps1.2.5.1.4 "><p id="p77771237103718"><a name="p77771237103718"></a><a name="p77771237103718"></a>ID of the snapshot to be deleted.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section1477913211910"></a>

None

## Response<a name="section19810103220915"></a>

None

## Examples<a name="section271817020477"></a>

Example request

```
DELETE /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/ea244205-d641-45d9-9dcb-ab2236bcd07e/index_snapshot/29a2254e-947f-4463-b65a-5f0b17515fae
```

## Status Code<a name="section87962546391"></a>

[Table 2](#table1130545163319)  describes the status code.

**Table  2**  Status code

<a name="table1130545163319"></a>
<table><thead align="left"><tr id="row43061959330"><th class="cellrowborder" valign="top" width="19.44194419441944%" id="mcps1.2.4.1.1"><p id="en-us_topic_0122640420_p51562446"><a name="en-us_topic_0122640420_p51562446"></a><a name="en-us_topic_0122640420_p51562446"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="25.502550255025504%" id="mcps1.2.4.1.2"><p id="en-us_topic_0122640420_p15808580"><a name="en-us_topic_0122640420_p15808580"></a><a name="en-us_topic_0122640420_p15808580"></a>Code</p>
</th>
<th class="cellrowborder" valign="top" width="55.055505550555054%" id="mcps1.2.4.1.3"><p id="en-us_topic_0122640420_p5426640"><a name="en-us_topic_0122640420_p5426640"></a><a name="en-us_topic_0122640420_p5426640"></a>Status Code Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row10306135113317"><td class="cellrowborder" valign="top" width="19.44194419441944%" headers="mcps1.2.4.1.1 "><p id="p430655133316"><a name="p430655133316"></a><a name="p430655133316"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="25.502550255025504%" headers="mcps1.2.4.1.2 "><p id="p134136431055"><a name="p134136431055"></a><a name="p134136431055"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="55.055505550555054%" headers="mcps1.2.4.1.3 "><p id="p134136431458"><a name="p134136431458"></a><a name="p134136431458"></a>The request is processed successfully.</p>
</td>
</tr>
<tr id="row1830612503310"><td class="cellrowborder" valign="top" width="19.44194419441944%" headers="mcps1.2.4.1.1 "><p id="p1030616563318"><a name="p1030616563318"></a><a name="p1030616563318"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="25.502550255025504%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0122640420_p11193990"><a name="en-us_topic_0122640420_p11193990"></a><a name="en-us_topic_0122640420_p11193990"></a>BadRequest</p>
</td>
<td class="cellrowborder" valign="top" width="55.055505550555054%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0122640420_p34297999"><a name="en-us_topic_0122640420_p34297999"></a><a name="en-us_topic_0122640420_p34297999"></a>Invalid request.</p>
<p id="en-us_topic_0122640420_p40246543"><a name="en-us_topic_0122640420_p40246543"></a><a name="en-us_topic_0122640420_p40246543"></a>The client should not repeat the request without modifications.</p>
</td>
</tr>
<tr id="row1261264514331"><td class="cellrowborder" valign="top" width="19.44194419441944%" headers="mcps1.2.4.1.1 "><p id="p17612174563314"><a name="p17612174563314"></a><a name="p17612174563314"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="25.502550255025504%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0122640420_p50789473"><a name="en-us_topic_0122640420_p50789473"></a><a name="en-us_topic_0122640420_p50789473"></a>Forbidden</p>
</td>
<td class="cellrowborder" valign="top" width="55.055505550555054%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0122640420_p20306648"><a name="en-us_topic_0122640420_p20306648"></a><a name="en-us_topic_0122640420_p20306648"></a>The server understood the request, but is refusing to fulfill it.</p>
<p id="en-us_topic_0122640420_p48542107"><a name="en-us_topic_0122640420_p48542107"></a><a name="en-us_topic_0122640420_p48542107"></a>The client should not repeat the request without modifications.</p>
</td>
</tr>
</tbody>
</table>


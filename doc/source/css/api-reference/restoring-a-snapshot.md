# Restoring a Snapshot<a name="css_03_0035"></a>

## Function<a name="section874853215915"></a>

This API is used to manually restore a snapshot.

## URI<a name="section8763193210910"></a>

```
POST /v1.0/{project_id}/clusters/{cluster_id}/index_snapshot/{snapshot_id}/restore
```

**Table  1**  Parameter description

<a name="table57631032695"></a>
<table><thead align="left"><tr id="row4445336913"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.1"><p id="p54417338910"><a name="p54417338910"></a><a name="p54417338910"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.2"><p id="p1644733693"><a name="p1644733693"></a><a name="p1644733693"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.3"><p id="p11441233696"><a name="p11441233696"></a><a name="p11441233696"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="40%" id="mcps1.2.5.1.4"><p id="p124403319916"><a name="p124403319916"></a><a name="p124403319916"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row94414331098"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p0441331398"><a name="p0441331398"></a><a name="p0441331398"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p9444331997"><a name="p9444331997"></a><a name="p9444331997"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.3 "><p id="p144412334919"><a name="p144412334919"></a><a name="p144412334919"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.5.1.4 "><p id="p18449331896"><a name="p18449331896"></a><a name="p18449331896"></a>Project ID.</p>
</td>
</tr>
<tr id="row14453320917"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p2044193314920"><a name="p2044193314920"></a><a name="p2044193314920"></a>cluster_id</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p24410331398"><a name="p24410331398"></a><a name="p24410331398"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.3 "><p id="p844133316918"><a name="p844133316918"></a><a name="p844133316918"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.5.1.4 "><p id="p13441833493"><a name="p13441833493"></a><a name="p13441833493"></a>ID of the cluster to which the snapshot belongs.</p>
</td>
</tr>
<tr id="row169341188286"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="p593415181284"><a name="p593415181284"></a><a name="p593415181284"></a>snapshot_id</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p293521892813"><a name="p293521892813"></a><a name="p293521892813"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.3 "><p id="p19935121812286"><a name="p19935121812286"></a><a name="p19935121812286"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.5.1.4 "><p id="p169351118192810"><a name="p169351118192810"></a><a name="p169351118192810"></a>ID of the snapshot.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section1477913211910"></a>

[Table 2](#table82481020121413)  describes the request parameters.

**Table  2**  Parameter description

<a name="table82481020121413"></a>
<table><thead align="left"><tr id="row18248112010149"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="p10441033494"><a name="p10441033494"></a><a name="p10441033494"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12.4%" id="mcps1.2.5.1.2"><p id="p74493316910"><a name="p74493316910"></a><a name="p74493316910"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15.52%" id="mcps1.2.5.1.3"><p id="p1044533896"><a name="p1044533896"></a><a name="p1044533896"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="55.08%" id="mcps1.2.5.1.4"><p id="p154413335917"><a name="p154413335917"></a><a name="p154413335917"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row18248182013148"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p837215054813"><a name="p837215054813"></a><a name="p837215054813"></a>targetCluster</p>
</td>
<td class="cellrowborder" valign="top" width="12.4%" headers="mcps1.2.5.1.2 "><p id="p4441233891"><a name="p4441233891"></a><a name="p4441233891"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.52%" headers="mcps1.2.5.1.3 "><p id="p186181046114912"><a name="p186181046114912"></a><a name="p186181046114912"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.08%" headers="mcps1.2.5.1.4 "><p id="p9448924192218"><a name="p9448924192218"></a><a name="p9448924192218"></a>ID of the cluster, to which the snapshot is to be restored.</p>
</td>
</tr>
<tr id="row243315404483"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p1343434015485"><a name="p1343434015485"></a><a name="p1343434015485"></a>indices</p>
</td>
<td class="cellrowborder" valign="top" width="12.4%" headers="mcps1.2.5.1.2 "><p id="p61971911172012"><a name="p61971911172012"></a><a name="p61971911172012"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.52%" headers="mcps1.2.5.1.3 "><p id="p1543414094815"><a name="p1543414094815"></a><a name="p1543414094815"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.08%" headers="mcps1.2.5.1.4 "><p id="p194341340174817"><a name="p194341340174817"></a><a name="p194341340174817"></a>Name of the index to be restored. Multiple index names are separated by commas (,). By default, data of all indices is restored. You can use the asterisk (*) to back up data of certain indices. For example, if you enter <strong id="b11705646103319"><a name="b11705646103319"></a><a name="b11705646103319"></a>2018-06*</strong>, then data of indices with the name prefix of <strong id="b1371614617337"><a name="b1371614617337"></a><a name="b1371614617337"></a>2018-06</strong> will be restored.</p>
<p id="p7748181019443"><a name="p7748181019443"></a><a name="p7748181019443"></a>The value contains 0 to 1024 characters. Uppercase letters, spaces, and certain special characters (including "\&lt;|&gt;/?) are not allowed.</p>
</td>
</tr>
<tr id="row1795115595819"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p19952165545814"><a name="p19952165545814"></a><a name="p19952165545814"></a>renamePattern</p>
</td>
<td class="cellrowborder" valign="top" width="12.4%" headers="mcps1.2.5.1.2 "><p id="p139521155125816"><a name="p139521155125816"></a><a name="p139521155125816"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.52%" headers="mcps1.2.5.1.3 "><p id="p1995220551584"><a name="p1995220551584"></a><a name="p1995220551584"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.08%" headers="mcps1.2.5.1.4 "><p id="p131436419191"><a name="p131436419191"></a><a name="p131436419191"></a>Rule for defining the indices to be restored. The value contains a maximum of 1024 characters.</p>
<p id="p156573384511"><a name="p156573384511"></a><a name="p156573384511"></a>Indices that meet the filtering condition specified by this parameter are restored. The filtering condition must be specified using regular expressions. The value contains 0 to 1024 characters. Uppercase letters, spaces, and certain special characters (including "\&lt;|&gt;/?,) are not allowed.</p>
</td>
</tr>
<tr id="row20584459142218"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p0584185922218"><a name="p0584185922218"></a><a name="p0584185922218"></a>renameReplacement</p>
</td>
<td class="cellrowborder" valign="top" width="12.4%" headers="mcps1.2.5.1.2 "><p id="p108383182419"><a name="p108383182419"></a><a name="p108383182419"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="15.52%" headers="mcps1.2.5.1.3 "><p id="p9838916243"><a name="p9838916243"></a><a name="p9838916243"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.08%" headers="mcps1.2.5.1.4 "><p id="p1958475913225"><a name="p1958475913225"></a><a name="p1958475913225"></a>Rule for renaming an index. The value contains 0 to 1024 characters. Uppercase letters, spaces, and certain special characters (including "\&lt;|&gt;/?,) are not allowed. For example, value <span class="parmvalue" id="parmvalue563703423114216"><a name="parmvalue563703423114216"></a><a name="parmvalue563703423114216"></a><b>restored_index_$1</b></span> indicates that <span class="parmvalue" id="parmvalue806962896114232"><a name="parmvalue806962896114232"></a><a name="parmvalue806962896114232"></a><b>restored_</b></span> is added in front of the names of all restored indices.</p>
<p id="p105962536258"><a name="p105962536258"></a><a name="p105962536258"></a>The <strong id="b693144325916"><a name="b693144325916"></a><a name="b693144325916"></a>renamePattern</strong> and <strong id="b18215493591"><a name="b18215493591"></a><a name="b18215493591"></a>renameReplacement</strong> parameters must be both configured.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section19810103220915"></a>

None

## Examples<a name="section27311857164512"></a>

Example request

```
POST /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/ea244205-d641-45d9-9dcb-ab2236bcd07e/index_snapshot/29a2254e-947f-4463-b65a-5f0b17515fae/restore
{
    "targetCluster":"ea244205-d641-45d9-9dcb-ab2236bcd07e",
    "indices":"myindex1,myindex2"
}
```

Example response

The returned value is empty.

## Status Code<a name="section87962546391"></a>

[Table 3](#table1130545163319)  describes the status code.

**Table  3**  Status code

<a name="table1130545163319"></a>
<table><thead align="left"><tr id="row43061959330"><th class="cellrowborder" valign="top" width="18.411841184118412%" id="mcps1.2.4.1.1"><p id="en-us_topic_0122640420_p51562446"><a name="en-us_topic_0122640420_p51562446"></a><a name="en-us_topic_0122640420_p51562446"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="19.99199919991999%" id="mcps1.2.4.1.2"><p id="en-us_topic_0122640420_p15808580"><a name="en-us_topic_0122640420_p15808580"></a><a name="en-us_topic_0122640420_p15808580"></a>Code</p>
</th>
<th class="cellrowborder" valign="top" width="61.5961596159616%" id="mcps1.2.4.1.3"><p id="en-us_topic_0122640420_p5426640"><a name="en-us_topic_0122640420_p5426640"></a><a name="en-us_topic_0122640420_p5426640"></a>Status Code Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row10306135113317"><td class="cellrowborder" valign="top" width="18.411841184118412%" headers="mcps1.2.4.1.1 "><p id="p430655133316"><a name="p430655133316"></a><a name="p430655133316"></a>201</p>
</td>
<td class="cellrowborder" valign="top" width="19.99199919991999%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0122640420_p58675139"><a name="en-us_topic_0122640420_p58675139"></a><a name="en-us_topic_0122640420_p58675139"></a>Created</p>
</td>
<td class="cellrowborder" valign="top" width="61.5961596159616%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0122640420_p55065844"><a name="en-us_topic_0122640420_p55065844"></a><a name="en-us_topic_0122640420_p55065844"></a>The request for creating a resource has been fulfilled.</p>
</td>
</tr>
<tr id="row1830612503310"><td class="cellrowborder" valign="top" width="18.411841184118412%" headers="mcps1.2.4.1.1 "><p id="p1030616563318"><a name="p1030616563318"></a><a name="p1030616563318"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="19.99199919991999%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0122640420_p11193990"><a name="en-us_topic_0122640420_p11193990"></a><a name="en-us_topic_0122640420_p11193990"></a>BadRequest</p>
</td>
<td class="cellrowborder" valign="top" width="61.5961596159616%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0122640420_p34297999"><a name="en-us_topic_0122640420_p34297999"></a><a name="en-us_topic_0122640420_p34297999"></a>Invalid request.</p>
<p id="en-us_topic_0122640420_p40246543"><a name="en-us_topic_0122640420_p40246543"></a><a name="en-us_topic_0122640420_p40246543"></a>The client should not repeat the request without modifications.</p>
</td>
</tr>
<tr id="row1261264514331"><td class="cellrowborder" valign="top" width="18.411841184118412%" headers="mcps1.2.4.1.1 "><p id="p17612174563314"><a name="p17612174563314"></a><a name="p17612174563314"></a>403</p>
</td>
<td class="cellrowborder" valign="top" width="19.99199919991999%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0122640420_p50789473"><a name="en-us_topic_0122640420_p50789473"></a><a name="en-us_topic_0122640420_p50789473"></a>Forbidden</p>
</td>
<td class="cellrowborder" valign="top" width="61.5961596159616%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0122640420_p20306648"><a name="en-us_topic_0122640420_p20306648"></a><a name="en-us_topic_0122640420_p20306648"></a>The server understood the request, but is refusing to fulfill it.</p>
<p id="en-us_topic_0122640420_p48542107"><a name="en-us_topic_0122640420_p48542107"></a><a name="en-us_topic_0122640420_p48542107"></a>The client should not repeat the request without modifications.</p>
</td>
</tr>
</tbody>
</table>


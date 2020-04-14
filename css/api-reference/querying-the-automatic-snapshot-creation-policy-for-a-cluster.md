# Querying the Automatic Snapshot Creation Policy for a Cluster<a name="css_03_0032"></a>

## Function<a name="section874853215915"></a>

This API is used to query the automatic snapshot creation policy for a cluster.

## URI<a name="section8763193210910"></a>

```
GET /v1.0/{project_id}/clusters/{cluster_id}/index_snapshot/policy
```

**Table  1**  Parameter description

<a name="table57631032695"></a>
<table><thead align="left"><tr id="row4445336913"><th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.1"><p id="p54417338910"><a name="p54417338910"></a><a name="p54417338910"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.2"><p id="p1644733693"><a name="p1644733693"></a><a name="p1644733693"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="p11441233696"><a name="p11441233696"></a><a name="p11441233696"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="54%" id="mcps1.2.5.1.4"><p id="p124403319916"><a name="p124403319916"></a><a name="p124403319916"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row94414331098"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="p950595565411"><a name="p950595565411"></a><a name="p950595565411"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p9444331997"><a name="p9444331997"></a><a name="p9444331997"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="p144412334919"><a name="p144412334919"></a><a name="p144412334919"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.5.1.4 "><p id="p18449331896"><a name="p18449331896"></a><a name="p18449331896"></a>Project ID.</p>
</td>
</tr>
<tr id="row14453320917"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="p15505145512547"><a name="p15505145512547"></a><a name="p15505145512547"></a>cluster_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p24410331398"><a name="p24410331398"></a><a name="p24410331398"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="p844133316918"><a name="p844133316918"></a><a name="p844133316918"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.5.1.4 "><p id="p13441833493"><a name="p13441833493"></a><a name="p13441833493"></a>ID of the cluster, for which the automatic snapshot creation policy is to be queried.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section1477913211910"></a>

None

## Response<a name="section19810103220915"></a>

[Table 2](#table2282125191510)  describes the response parameters.

**Table  2**  Parameter description

<a name="table2282125191510"></a>
<table><thead align="left"><tr id="row16282195131515"><th class="cellrowborder" valign="top" width="28.000000000000004%" id="mcps1.2.4.1.1"><p id="p4446331696"><a name="p4446331696"></a><a name="p4446331696"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.4.1.2"><p id="p7440338917"><a name="p7440338917"></a><a name="p7440338917"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="53%" id="mcps1.2.4.1.3"><p id="p184453317918"><a name="p184453317918"></a><a name="p184453317918"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row142821951181515"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p14081111574"><a name="p14081111574"></a><a name="p14081111574"></a>keepday</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p1971181065714"><a name="p1971181065714"></a><a name="p1971181065714"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.4.1.3 "><p id="p4524238185713"><a name="p4524238185713"></a><a name="p4524238185713"></a>Retention days for a snapshot.</p>
</td>
</tr>
<tr id="row543104310568"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p14087119575"><a name="p14087119575"></a><a name="p14087119575"></a>period</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p3711201095716"><a name="p3711201095716"></a><a name="p3711201095716"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.4.1.3 "><p id="p322318256578"><a name="p322318256578"></a><a name="p322318256578"></a>Time when a snapshot is created every day.</p>
</td>
</tr>
<tr id="row142728488564"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p2040821145715"><a name="p2040821145715"></a><a name="p2040821145715"></a>prefix</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p12711110135713"><a name="p12711110135713"></a><a name="p12711110135713"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.4.1.3 "><p id="p11223132516573"><a name="p11223132516573"></a><a name="p11223132516573"></a>Snapshot name prefix.</p>
</td>
</tr>
<tr id="row15272154845619"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p640812125718"><a name="p640812125718"></a><a name="p640812125718"></a>bucket</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p147111710175715"><a name="p147111710175715"></a><a name="p147111710175715"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.4.1.3 "><p id="p14223325185719"><a name="p14223325185719"></a><a name="p14223325185719"></a>OBS bucket for storing snapshots.</p>
</td>
</tr>
<tr id="row1215235445612"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p13410312579"><a name="p13410312579"></a><a name="p13410312579"></a>agency</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p127123106579"><a name="p127123106579"></a><a name="p127123106579"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.4.1.3 "><p id="p7223025185714"><a name="p7223025185714"></a><a name="p7223025185714"></a>Agency used to access OBS buckets.</p>
</td>
</tr>
<tr id="row7152135455612"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p1141041165716"><a name="p1141041165716"></a><a name="p1141041165716"></a>enable</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p671291020575"><a name="p671291020575"></a><a name="p671291020575"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.4.1.3 "><p id="p18223132515717"><a name="p18223132515717"></a><a name="p18223132515717"></a>Whether to enable the automatic snapshot creation policy.</p>
</td>
</tr>
<tr id="row17550717105720"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p1655111172575"><a name="p1655111172575"></a><a name="p1655111172575"></a>snapshotCmkId</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="p20551117105719"><a name="p20551117105719"></a><a name="p20551117105719"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.4.1.3 "><p id="p255171705710"><a name="p255171705710"></a><a name="p255171705710"></a>Snapshot encryption ID. If the snapshot is not encrypted, value <span class="parmvalue" id="parmvalue6423185516121"><a name="parmvalue6423185516121"></a><a name="parmvalue6423185516121"></a><b>null</b></span> is returned.</p>
</td>
</tr>
</tbody>
</table>

## Examples<a name="section17489545144119"></a>

Example request

```
GET /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/ea244205-d641-45d9-9dcb-ab2236bcd07e/index_snapshot/policy
```

Example response

```

{
    "keepday":2,
    "period":"16:00 GMT+08:00",
    "prefix":"snapshot",
    "bucket":"es-backup",
    "agency":"usearch",
    "enable":"true",
    "snapshotCmkId" : "a7d5d58c-0330-4d25-860d-c488a4cb4ba7" 
}
```

## Status Code<a name="section87962546391"></a>

[Table 3](#table18620659263)  describes the status code.

**Table  3**  Status code

<a name="table18620659263"></a>
<table><thead align="left"><tr id="css_03_0031_row194918333132"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="css_03_0031_p6531343171310"><a name="css_03_0031_p6531343171310"></a><a name="css_03_0031_p6531343171310"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="css_03_0031_p16534124318132"><a name="css_03_0031_p16534124318132"></a><a name="css_03_0031_p16534124318132"></a>Code</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="css_03_0031_p1453710437131"><a name="css_03_0031_p1453710437131"></a><a name="css_03_0031_p1453710437131"></a>Status Code Description</p>
</th>
</tr>
</thead>
<tbody><tr id="css_03_0031_row09491533111315"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="css_03_0031_p1656994351310"><a name="css_03_0031_p1656994351310"></a><a name="css_03_0031_p1656994351310"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="css_03_0031_p134136431055"><a name="css_03_0031_p134136431055"></a><a name="css_03_0031_p134136431055"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="css_03_0031_p134136431458"><a name="css_03_0031_p134136431458"></a><a name="css_03_0031_p134136431458"></a>The request is processed successfully.</p>
</td>
</tr>
<tr id="css_03_0031_row1184954102013"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="css_03_0031_p111841154132019"><a name="css_03_0031_p111841154132019"></a><a name="css_03_0031_p111841154132019"></a>406</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="css_03_0031_en-us_topic_0122640420_p19980869"><a name="css_03_0031_en-us_topic_0122640420_p19980869"></a><a name="css_03_0031_en-us_topic_0122640420_p19980869"></a>Not Acceptable</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="css_03_0031_en-us_topic_0122640420_p7837682"><a name="css_03_0031_en-us_topic_0122640420_p7837682"></a><a name="css_03_0031_en-us_topic_0122640420_p7837682"></a>The server cannot fulfill the request according to the content characteristics of the request.</p>
</td>
</tr>
</tbody>
</table>


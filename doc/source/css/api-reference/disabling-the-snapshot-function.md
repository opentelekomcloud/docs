# Disabling the Snapshot Function<a name="css_03_0039"></a>

## Function<a name="section874853215915"></a>

This API is used to disable the snapshot function.

## URI<a name="section8763193210910"></a>

```
DELETE /v1.0/{project_id}/clusters/{cluster_id}/index_snapshots
```

**Table  1**  Parameter description

<a name="table57631032695"></a>
<table><thead align="left"><tr id="row4445336913"><th class="cellrowborder" valign="top" width="21.21212121212121%" id="mcps1.2.5.1.1"><p id="p54417338910"><a name="p54417338910"></a><a name="p54417338910"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18.181818181818183%" id="mcps1.2.5.1.2"><p id="p1644733693"><a name="p1644733693"></a><a name="p1644733693"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="17.171717171717173%" id="mcps1.2.5.1.3"><p id="p11441233696"><a name="p11441233696"></a><a name="p11441233696"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="43.43434343434344%" id="mcps1.2.5.1.4"><p id="p124403319916"><a name="p124403319916"></a><a name="p124403319916"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row94414331098"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.5.1.1 "><p id="p0441331398"><a name="p0441331398"></a><a name="p0441331398"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.2 "><p id="p9444331997"><a name="p9444331997"></a><a name="p9444331997"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.3 "><p id="p144412334919"><a name="p144412334919"></a><a name="p144412334919"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.43434343434344%" headers="mcps1.2.5.1.4 "><p id="p18449331896"><a name="p18449331896"></a><a name="p18449331896"></a>Project ID.</p>
</td>
</tr>
<tr id="row14453320917"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.5.1.1 "><p id="p2044193314920"><a name="p2044193314920"></a><a name="p2044193314920"></a>cluster_id</p>
</td>
<td class="cellrowborder" valign="top" width="18.181818181818183%" headers="mcps1.2.5.1.2 "><p id="p24410331398"><a name="p24410331398"></a><a name="p24410331398"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.3 "><p id="p844133316918"><a name="p844133316918"></a><a name="p844133316918"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="43.43434343434344%" headers="mcps1.2.5.1.4 "><p id="p13441833493"><a name="p13441833493"></a><a name="p13441833493"></a>ID of the cluster to which the snapshot belongs.</p>
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
DELETE /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/ea244205-d641-45d9-9dcb-ab2236bcd07e/index_snapshots
```

## Status Code<a name="section87962546391"></a>

[Table 2](#table15824192510361)  describes the status code.

**Table  2**  Status code

<a name="table15824192510361"></a>
<table><thead align="left"><tr id="css_03_0037_row194918333132"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="css_03_0037_p6531343171310"><a name="css_03_0037_p6531343171310"></a><a name="css_03_0037_p6531343171310"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="css_03_0037_p16534124318132"><a name="css_03_0037_p16534124318132"></a><a name="css_03_0037_p16534124318132"></a>Code</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="css_03_0037_p1453710437131"><a name="css_03_0037_p1453710437131"></a><a name="css_03_0037_p1453710437131"></a>Status Code Description</p>
</th>
</tr>
</thead>
<tbody><tr id="css_03_0037_row09491533111315"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="css_03_0037_p1656994351310"><a name="css_03_0037_p1656994351310"></a><a name="css_03_0037_p1656994351310"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="css_03_0037_p134136431055"><a name="css_03_0037_p134136431055"></a><a name="css_03_0037_p134136431055"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="css_03_0037_p134136431458"><a name="css_03_0037_p134136431458"></a><a name="css_03_0037_p134136431458"></a>The request is processed successfully.</p>
</td>
</tr>
<tr id="css_03_0037_row1184954102013"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="css_03_0037_p111841154132019"><a name="css_03_0037_p111841154132019"></a><a name="css_03_0037_p111841154132019"></a>406</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="css_03_0037_en-us_topic_0122640420_p19980869"><a name="css_03_0037_en-us_topic_0122640420_p19980869"></a><a name="css_03_0037_en-us_topic_0122640420_p19980869"></a>Not Acceptable</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="css_03_0037_en-us_topic_0122640420_p7837682"><a name="css_03_0037_en-us_topic_0122640420_p7837682"></a><a name="css_03_0037_en-us_topic_0122640420_p7837682"></a>The server cannot fulfill the request according to the content characteristics of the request.</p>
</td>
</tr>
</tbody>
</table>


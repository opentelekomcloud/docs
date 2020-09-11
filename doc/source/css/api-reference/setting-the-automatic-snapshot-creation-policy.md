# Setting the Automatic Snapshot Creation Policy<a name="css_03_0031"></a>

## Function<a name="section874853215915"></a>

This API is used to set parameters related to automatic snapshot creation. By default, a snapshot is created per day.

## URI<a name="section8763193210910"></a>

```
POST /v1.0/{project_id}/clusters/{cluster_id}/index_snapshot/policy
```

**Table  1**  Parameter description

<a name="table57631032695"></a>
<table><thead align="left"><tr id="row4445336913"><th class="cellrowborder" valign="top" width="25.77%" id="mcps1.2.5.1.1"><p id="p54417338910"><a name="p54417338910"></a><a name="p54417338910"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="24.740000000000002%" id="mcps1.2.5.1.2"><p id="p1644733693"><a name="p1644733693"></a><a name="p1644733693"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="18.56%" id="mcps1.2.5.1.3"><p id="p11441233696"><a name="p11441233696"></a><a name="p11441233696"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="30.930000000000003%" id="mcps1.2.5.1.4"><p id="p124403319916"><a name="p124403319916"></a><a name="p124403319916"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row94414331098"><td class="cellrowborder" valign="top" width="25.77%" headers="mcps1.2.5.1.1 "><p id="p0441331398"><a name="p0441331398"></a><a name="p0441331398"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="24.740000000000002%" headers="mcps1.2.5.1.2 "><p id="p9444331997"><a name="p9444331997"></a><a name="p9444331997"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.56%" headers="mcps1.2.5.1.3 "><p id="p144412334919"><a name="p144412334919"></a><a name="p144412334919"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="30.930000000000003%" headers="mcps1.2.5.1.4 "><p id="p18449331896"><a name="p18449331896"></a><a name="p18449331896"></a>Project ID.</p>
</td>
</tr>
<tr id="row14453320917"><td class="cellrowborder" valign="top" width="25.77%" headers="mcps1.2.5.1.1 "><p id="p2044193314920"><a name="p2044193314920"></a><a name="p2044193314920"></a>cluster_id</p>
</td>
<td class="cellrowborder" valign="top" width="24.740000000000002%" headers="mcps1.2.5.1.2 "><p id="p24410331398"><a name="p24410331398"></a><a name="p24410331398"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.56%" headers="mcps1.2.5.1.3 "><p id="p844133316918"><a name="p844133316918"></a><a name="p844133316918"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="30.930000000000003%" headers="mcps1.2.5.1.4 "><p id="p13441833493"><a name="p13441833493"></a><a name="p13441833493"></a>ID of the cluster where automatic snapshot creation is enabled.</p>
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
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="p74493316910"><a name="p74493316910"></a><a name="p74493316910"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.3"><p id="p1044533896"><a name="p1044533896"></a><a name="p1044533896"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51%" id="mcps1.2.5.1.4"><p id="p154413335917"><a name="p154413335917"></a><a name="p154413335917"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row18248182013148"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p837215054813"><a name="p837215054813"></a><a name="p837215054813"></a>prefix</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p4441233891"><a name="p4441233891"></a><a name="p4441233891"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p186181046114912"><a name="p186181046114912"></a><a name="p186181046114912"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.5.1.4 "><p id="p9448924192218"><a name="p9448924192218"></a><a name="p9448924192218"></a>Prefix of the snapshot name that is automatically created.</p>
</td>
</tr>
<tr id="row243315404483"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p1343434015485"><a name="p1343434015485"></a><a name="p1343434015485"></a>period</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p443424054812"><a name="p443424054812"></a><a name="p443424054812"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p1543414094815"><a name="p1543414094815"></a><a name="p1543414094815"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.5.1.4 "><p id="p194341340174817"><a name="p194341340174817"></a><a name="p194341340174817"></a>Time when a snapshot is created every day. Snapshots can only be created on the hour. The time format is the time followed by the time zone, specifically, <span class="parmname" id="parmname207181910155010"><a name="parmname207181910155010"></a><a name="parmname207181910155010"></a><b>HH:mm z</b></span>. In the format, <span class="parmname" id="parmname26580719510"><a name="parmname26580719510"></a><a name="parmname26580719510"></a><b>HH:mm</b></span> refers to the hour time and <span class="parmname" id="parmname12640155145015"><a name="parmname12640155145015"></a><a name="parmname12640155145015"></a><b>z</b></span> refers to the time zone. For example, <span class="parmvalue" id="parmvalue150123314505"><a name="parmvalue150123314505"></a><a name="parmvalue150123314505"></a><b>00:00 GMT+08:00</b></span> and <span class="parmvalue" id="parmvalue1695214431503"><a name="parmvalue1695214431503"></a><a name="parmvalue1695214431503"></a><b>01:00 GMT+08:00</b></span>.</p>
</td>
</tr>
<tr id="row1795115595819"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p19952165545814"><a name="p19952165545814"></a><a name="p19952165545814"></a>keepday</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p139521155125816"><a name="p139521155125816"></a><a name="p139521155125816"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p1995220551584"><a name="p1995220551584"></a><a name="p1995220551584"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.5.1.4 "><p id="p5952255145811"><a name="p5952255145811"></a><a name="p5952255145811"></a>Number of days that a snapshot can be retained. The value ranges from 1 to 90. The system automatically deletes snapshots that have been retained for the allowed maximum duration on the half hour.</p>
</td>
</tr>
<tr id="row10242054591"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p52412510597"><a name="p52412510597"></a><a name="p52412510597"></a>enable</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p1324105125919"><a name="p1324105125919"></a><a name="p1324105125919"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p62611515593"><a name="p62611515593"></a><a name="p62611515593"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.5.1.4 "><p id="p1926165185914"><a name="p1926165185914"></a><a name="p1926165185914"></a>Value <span class="parmvalue" id="parmvalue1223625113406"><a name="parmvalue1223625113406"></a><a name="parmvalue1223625113406"></a><b>true</b></span> indicates that the automatic snapshot creation policy is enabled, and value <span class="parmvalue" id="parmvalue9862145319405"><a name="parmvalue9862145319405"></a><a name="parmvalue9862145319405"></a><b>false</b></span> indicates that the automatic snapshot creation policy is disabled.</p>
</td>
</tr>
<tr id="row14926181913614"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p9926131983613"><a name="p9926131983613"></a><a name="p9926131983613"></a>deleteAuto</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p1992613192362"><a name="p1992613192362"></a><a name="p1992613192362"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="p69261192361"><a name="p69261192361"></a><a name="p69261192361"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51%" headers="mcps1.2.5.1.4 "><p id="p12926919193610"><a name="p12926919193610"></a><a name="p12926919193610"></a>Whether to delete all automatically created snapshots when the automatic snapshot creation policy is disabled. The default value is <span class="parmvalue" id="parmvalue866761614499"><a name="parmvalue866761614499"></a><a name="parmvalue866761614499"></a><b>false</b></span>, indicating that snapshots that have been automatically created are not deleted when the automatic snapshot creation function is disabled. If this parameter is set to <strong id="b147866595408"><a name="b147866595408"></a><a name="b147866595408"></a>true</strong>, all automatically created snapshots are deleted when the automatic snapshot creation policy is disabled.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section19810103220915"></a>

None

## Examples<a name="section4831175818404"></a>

Example request

```
POST /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/ea244205-d641-45d9-9dcb-ab2236bcd07e/index_snapshot/policy
{
    "prefix":"snapshot",
    "period":"16:00 GMT+08:00",
    "keepday":7,
    "enable":"true"
}
```

## Status Code<a name="section87962546391"></a>

[Table 3](#table209491933101317)  describes the status code.

**Table  3**  Status code

<a name="table209491933101317"></a>
<table><thead align="left"><tr id="row194918333132"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p6531343171310"><a name="p6531343171310"></a><a name="p6531343171310"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p16534124318132"><a name="p16534124318132"></a><a name="p16534124318132"></a>Code</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p1453710437131"><a name="p1453710437131"></a><a name="p1453710437131"></a>Status Code Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row09491533111315"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1656994351310"><a name="p1656994351310"></a><a name="p1656994351310"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p134136431055"><a name="p134136431055"></a><a name="p134136431055"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p134136431458"><a name="p134136431458"></a><a name="p134136431458"></a>The request is processed successfully.</p>
</td>
</tr>
<tr id="row1184954102013"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p111841154132019"><a name="p111841154132019"></a><a name="p111841154132019"></a>406</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0122640420_p19980869"><a name="en-us_topic_0122640420_p19980869"></a><a name="en-us_topic_0122640420_p19980869"></a>Not Acceptable</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0122640420_p7837682"><a name="en-us_topic_0122640420_p7837682"></a><a name="en-us_topic_0122640420_p7837682"></a>The server cannot fulfill the request according to the content characteristics of the request.</p>
</td>
</tr>
</tbody>
</table>


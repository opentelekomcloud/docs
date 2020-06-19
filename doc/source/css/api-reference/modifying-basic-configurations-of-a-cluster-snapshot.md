# Modifying Basic Configurations of a Cluster Snapshot<a name="css_03_0030"></a>

## Function<a name="section874853215915"></a>

This API is used to modify the basic configurations of a cluster snapshot. The basic configurations include the OBS bucket and IAM agency.

## URI<a name="section8763193210910"></a>

```
POST /v1.0/{project_id}/clusters/{cluster_id}/index_snapshot/setting
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
<td class="cellrowborder" valign="top" width="30.930000000000003%" headers="mcps1.2.5.1.4 "><p id="p13441833493"><a name="p13441833493"></a><a name="p13441833493"></a>ID of the cluster where index data is to be backed up.</p>
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
<th class="cellrowborder" valign="top" width="18%" id="mcps1.2.5.1.2"><p id="p74493316910"><a name="p74493316910"></a><a name="p74493316910"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.2.5.1.3"><p id="p1044533896"><a name="p1044533896"></a><a name="p1044533896"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="47%" id="mcps1.2.5.1.4"><p id="p154413335917"><a name="p154413335917"></a><a name="p154413335917"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row18248182013148"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p837215054813"><a name="p837215054813"></a><a name="p837215054813"></a>bucket</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.2 "><p id="p4441233891"><a name="p4441233891"></a><a name="p4441233891"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.3 "><p id="p186181046114912"><a name="p186181046114912"></a><a name="p186181046114912"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.4 "><p id="p9448924192218"><a name="p9448924192218"></a><a name="p9448924192218"></a>OBS bucket used for index data backup. If there is snapshot data in an OBS bucket, only the OBS bucket is used and cannot be changed.</p>
</td>
</tr>
<tr id="row243315404483"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p1343434015485"><a name="p1343434015485"></a><a name="p1343434015485"></a>agency</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.2 "><p id="p443424054812"><a name="p443424054812"></a><a name="p443424054812"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.3 "><p id="p1543414094815"><a name="p1543414094815"></a><a name="p1543414094815"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.4 "><p id="p194341340174817"><a name="p194341340174817"></a><a name="p194341340174817"></a>IAM agency used to access OBS.</p>
</td>
</tr>
<tr id="row38700500107"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p1687235031013"><a name="p1687235031013"></a><a name="p1687235031013"></a>snapshotCmkId</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.2 "><p id="p387285051014"><a name="p387285051014"></a><a name="p387285051014"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.3 "><p id="p158722506102"><a name="p158722506102"></a><a name="p158722506102"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.4 "><p id="p10872450111011"><a name="p10872450111011"></a><a name="p10872450111011"></a>Key ID used for snapshot encryption.</p>
<a name="ul67444552406"></a><a name="ul67444552406"></a><ul id="ul67444552406"><li>The Default Master Keys cannot be used to create grants. Specifically, you cannot use Default Master Keys whose aliases end with <span class="parmvalue" id="parmvalue57857014910"><a name="parmvalue57857014910"></a><a name="parmvalue57857014910"></a><b>/default</b></span> in KMS to encrypt snapshots.</li><li>If a snapshot has been stored in the OBS bucket, you cannot modify the parameters for encrypting the snapshot.</li><li>If the key used for encryption is in the <span class="parmname" id="parmname1130319716920"><a name="parmname1130319716920"></a><a name="parmname1130319716920"></a><b>Pending deletion</b></span> or <span class="parmname" id="parmname11303571691"><a name="parmname11303571691"></a><a name="parmname11303571691"></a><b>disable</b></span> state, you cannot perform backup and restoration operations on the cluster. Specifically, new snapshots cannot be created for the cluster, and existing snapshots cannot be used for restoration. In this case, switch to the KMS management console and change the state of the target key to <strong id="b175201618915"><a name="b175201618915"></a><a name="b175201618915"></a>enable</strong> so that backup and restore operations are allowed on the cluster.</li><li>If the key used for encryption is deleted, backup and restore operations are not allowed on the cluster. In addition, the deleted key cannot be restored. Therefore, exercise caution when deleting a key.</li><li>You are advised to disable the automatic snapshot creation function if the key is deleted or is in the <span class="parmname" id="parmname102307044718"><a name="parmname102307044718"></a><a name="parmname102307044718"></a><b>Pending deletion</b></span> or <span class="parmname" id="parmname9231209470"><a name="parmname9231209470"></a><a name="parmname9231209470"></a><b>disable</b></span> state. In this condition, automatic snapshot creation is allowed based on the configured snapshot policy. However, all automatic snapshot creation tasks will fail, and the failed tasks are displayed in the failed task list in the <strong id="b1223219074714"><a name="b1223219074714"></a><a name="b1223219074714"></a>Failed Tasks</strong> dialog box.</li></ul>
</td>
</tr>
</tbody>
</table>

## Response<a name="section19810103220915"></a>

None

## Examples<a name="section1468819386395"></a>

Example request

```
POST /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/ea244205-d641-45d9-9dcb-ab2236bcd07e/index_snapshot/setting
{
    "bucket":"test-bucket",
    "agency":"usearch",
    "snapshotCmkId":"42546bb1-8025-4ad1-868f-600729c341aea"
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
<tr id="row7968201612229"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p496891614227"><a name="p496891614227"></a><a name="p496891614227"></a>412</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0122640420_p21784659"><a name="en-us_topic_0122640420_p21784659"></a><a name="en-us_topic_0122640420_p21784659"></a>Precondition Failed</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0122640420_p19726930"><a name="en-us_topic_0122640420_p19726930"></a><a name="en-us_topic_0122640420_p19726930"></a>The server does not meet one of the preconditions that the requester puts on the request.</p>
</td>
</tr>
<tr id="row442289174116"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p242417954112"><a name="p242417954112"></a><a name="p242417954112"></a>504</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1842419154117"><a name="p1842419154117"></a><a name="p1842419154117"></a>Gateway Timeout</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p104244912411"><a name="p104244912411"></a><a name="p104244912411"></a>A gateway timeout error occurred.</p>
</td>
</tr>
</tbody>
</table>


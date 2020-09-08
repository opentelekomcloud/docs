# Querying DCS Instance Status<a name="dcs-api-0312016"></a>

## Function<a name="section7655111175616"></a>

This API is used to query the number of instances in different states.

## URI<a name="section1484710512711"></a>

GET /v1.0/\{project\_id\}/instances/status?includeFailure=\{includeFailure\}

[Table 1](#table1624017336377)  describes the parameters.

**Table  1**  Parameter description

<a name="table1624017336377"></a>
<table><thead align="left"><tr id="row172405338371"><th class="cellrowborder" valign="top" width="25.252525252525253%" id="mcps1.2.5.1.1"><p id="p323919337375"><a name="p323919337375"></a><a name="p323919337375"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="21.21212121212121%" id="mcps1.2.5.1.2"><p id="p1524013335373"><a name="p1524013335373"></a><a name="p1524013335373"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="16.161616161616163%" id="mcps1.2.5.1.3"><p id="p1324010337372"><a name="p1324010337372"></a><a name="p1324010337372"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="37.37373737373738%" id="mcps1.2.5.1.4"><p id="p42409332372"><a name="p42409332372"></a><a name="p42409332372"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row2240173333711"><td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.2.5.1.1 "><p id="p13240183343720"><a name="p13240183343720"></a><a name="p13240183343720"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.5.1.2 "><p id="p13240123314374"><a name="p13240123314374"></a><a name="p13240123314374"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.3 "><p id="p1224073317379"><a name="p1224073317379"></a><a name="p1224073317379"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="37.37373737373738%" headers="mcps1.2.5.1.4 "><p id="p142405335374"><a name="p142405335374"></a><a name="p142405335374"></a>Project ID.</p>
</td>
</tr>
<tr id="row155545432517"><td class="cellrowborder" valign="top" width="25.252525252525253%" headers="mcps1.2.5.1.1 "><p id="p1738651462512"><a name="p1738651462512"></a><a name="p1738651462512"></a>includeFailure</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.5.1.2 "><p id="p93879142256"><a name="p93879142256"></a><a name="p93879142256"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.3 "><p id="p93871814152515"><a name="p93871814152515"></a><a name="p93871814152515"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="37.37373737373738%" headers="mcps1.2.5.1.4 "><p id="p1472542022512"><a name="p1472542022512"></a><a name="p1472542022512"></a>An indicator of whether the number of DCS instances that failed to be created will be returned to the API caller. Options:</p>
<a name="ul199610411577"></a><a name="ul199610411577"></a><ul id="ul199610411577"><li><strong id="b17321172843320"><a name="b17321172843320"></a><a name="b17321172843320"></a>true</strong>: The number of DCS instances that failed to be created will be returned to the API caller.</li><li><strong id="b7549183163619"><a name="b7549183163619"></a><a name="b7549183163619"></a>false</strong> or others: The number of DCS instances that failed to be created will not be returned to the API caller.</li></ul>
</td>
</tr>
</tbody>
</table>

## Request<a name="section188151421381"></a>

**Request parameters**

None.

**Example request**

```
GET https://{dcs_endpoint}/v1.0/{project_id}/instances/status?includeFailure=true
```

## Response<a name="section981263812810"></a>

**Response parameters**

[Table 2](#table595111370375)  describes the response parameters.

**Table  2**  Parameter description

<a name="table595111370375"></a>
<table><thead align="left"><tr id="row794915372377"><th class="cellrowborder" valign="top" width="33.333333333333336%" id="mcps1.2.4.1.1"><p id="p20949037193710"><a name="p20949037193710"></a><a name="p20949037193710"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="21.21212121212121%" id="mcps1.2.4.1.2"><p id="p13949153763712"><a name="p13949153763712"></a><a name="p13949153763712"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="45.45454545454546%" id="mcps1.2.4.1.3"><p id="p39491937183715"><a name="p39491937183715"></a><a name="p39491937183715"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1373142317719"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p1673122311718"><a name="p1673122311718"></a><a name="p1673122311718"></a>creating_count</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.4.1.2 "><p id="p1731923974"><a name="p1731923974"></a><a name="p1731923974"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="45.45454545454546%" headers="mcps1.2.4.1.3 "><p id="p147410234712"><a name="p147410234712"></a><a name="p147410234712"></a>Number of instances that are being created.</p>
</td>
</tr>
<tr id="row143510389719"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p3363381170"><a name="p3363381170"></a><a name="p3363381170"></a>deleting_count</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.4.1.2 "><p id="p12361538673"><a name="p12361538673"></a><a name="p12361538673"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="45.45454545454546%" headers="mcps1.2.4.1.3 "><p id="p17361338972"><a name="p17361338972"></a><a name="p17361338972"></a>Number of instances that are being deleted.</p>
</td>
</tr>
<tr id="row236338974"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p4371338972"><a name="p4371338972"></a><a name="p4371338972"></a>running_count</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.4.1.2 "><p id="p537163817718"><a name="p537163817718"></a><a name="p537163817718"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="45.45454545454546%" headers="mcps1.2.4.1.3 "><p id="p173713381072"><a name="p173713381072"></a><a name="p173713381072"></a>Number of running instances.</p>
</td>
</tr>
<tr id="row0377387714"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p537238473"><a name="p537238473"></a><a name="p537238473"></a>error_count</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.4.1.2 "><p id="p18372383710"><a name="p18372383710"></a><a name="p18372383710"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="45.45454545454546%" headers="mcps1.2.4.1.3 "><p id="p183714388719"><a name="p183714388719"></a><a name="p183714388719"></a>Number of abnormal instances.</p>
</td>
</tr>
<tr id="row339993617817"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p1439943616811"><a name="p1439943616811"></a><a name="p1439943616811"></a>restarting_count</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.4.1.2 "><p id="p173997361883"><a name="p173997361883"></a><a name="p173997361883"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="45.45454545454546%" headers="mcps1.2.4.1.3 "><p id="p139914362812"><a name="p139914362812"></a><a name="p139914362812"></a>Number of instances that are being restarted.</p>
</td>
</tr>
<tr id="row53991036484"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p1039953618810"><a name="p1039953618810"></a><a name="p1039953618810"></a>createfailed_count</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.4.1.2 "><p id="p12399836185"><a name="p12399836185"></a><a name="p12399836185"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="45.45454545454546%" headers="mcps1.2.4.1.3 "><p id="p114001136482"><a name="p114001136482"></a><a name="p114001136482"></a>Number of instances that fail to be created.</p>
</td>
</tr>
<tr id="row815993161513"><td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p016023161518"><a name="p016023161518"></a><a name="p016023161518"></a>extending_count</p>
</td>
<td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.4.1.2 "><p id="p516043151515"><a name="p516043151515"></a><a name="p516043151515"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="45.45454545454546%" headers="mcps1.2.4.1.3 "><p id="p1016083171513"><a name="p1016083171513"></a><a name="p1016083171513"></a>Number of instances that are being scaled up.</p>
</td>
</tr>
</tbody>
</table>

**Example response**

```
{
    "extending_count": 0,
    "creating_count": 0,
    "deleting_count": 0, 
    "running_count": 16,
    "error_count": 0,
    "restarting_count": 0,
    "createfailed_count": 44
}
```

## Status Code<a name="section865917510135"></a>

[Table 3](#table36591653133)  describes the status code of successful operations. For details about other status codes, see  [Table 1](status-codes.md#table5210141351517).

**Table  3**  Status code

<a name="table36591653133"></a>
<table><thead align="left"><tr id="row766085191316"><th class="cellrowborder" valign="top" width="15.98%" id="mcps1.2.3.1.1"><p id="p1666016571317"><a name="p1666016571317"></a><a name="p1666016571317"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="84.02%" id="mcps1.2.3.1.2"><p id="p1066017520139"><a name="p1066017520139"></a><a name="p1066017520139"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1066045101315"><td class="cellrowborder" valign="top" width="15.98%" headers="mcps1.2.3.1.1 "><p id="p1666011541314"><a name="p1666011541314"></a><a name="p1666011541314"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="84.02%" headers="mcps1.2.3.1.2 "><p id="p1466005171319"><a name="p1466005171319"></a><a name="p1466005171319"></a>Quantities of DCS instances in different statuses queried successfully.</p>
</td>
</tr>
</tbody>
</table>


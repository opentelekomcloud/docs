# Deleting Topics in a Kafka Instance in Batches<a name="EN-US_TOPIC_0128036887"></a>

## Function<a name="section281017251256"></a>

This API is used to delete topics in a Kafka instance in batches.

This API is available for only Kafka instances.

## URI<a name="section2989194312512"></a>

URI format: POST /v1.0/\{project\_id\}/instances/\{instance\_id\}/topics/delete

[Table 1](#table999074314516)  describes the parameter.

**Table  1**  Parameter description

<a name="table999074314516"></a>
<table><thead align="left"><tr id="row1611514441455"><th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.1"><p id="p121151744458"><a name="p121151744458"></a><a name="p121151744458"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.2"><p id="p7115114415513"><a name="p7115114415513"></a><a name="p7115114415513"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.5.1.3"><p id="p111517441957"><a name="p111517441957"></a><a name="p111517441957"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="59%" id="mcps1.2.5.1.4"><p id="p6115174418512"><a name="p6115174418512"></a><a name="p6115174418512"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row121155447517"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.1 "><p id="p15115944853"><a name="p15115944853"></a><a name="p15115944853"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p17115244354"><a name="p17115244354"></a><a name="p17115244354"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="p161154441252"><a name="p161154441252"></a><a name="p161154441252"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.5.1.4 "><p id="p8115134420510"><a name="p8115134420510"></a><a name="p8115134420510"></a>Indicates the ID of a project.</p>
</td>
</tr>
<tr id="row171159441358"><td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.1 "><p id="p12117204415518"><a name="p12117204415518"></a><a name="p12117204415518"></a>instance_id</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p411717442510"><a name="p411717442510"></a><a name="p411717442510"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="p111784412519"><a name="p111784412519"></a><a name="p111784412519"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.5.1.4 "><p id="p1911784411513"><a name="p1911784411513"></a><a name="p1911784411513"></a>Indicates the instance ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section101441458"></a>

**Request parameters**

[Table 2](#table192144257)  describes the parameter.

**Table  2**  Parameter description

<a name="table192144257"></a>
<table><thead align="left"><tr id="row141190441157"><th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.1"><p id="p11191144155"><a name="p11191144155"></a><a name="p11191144155"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.2"><p id="p61195448514"><a name="p61195448514"></a><a name="p61195448514"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.5.1.3"><p id="p11119104414518"><a name="p11119104414518"></a><a name="p11119104414518"></a>Mandatory or Not</p>
</th>
<th class="cellrowborder" valign="top" width="53%" id="mcps1.2.5.1.4"><p id="p111915441953"><a name="p111915441953"></a><a name="p111915441953"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1911984410515"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="p8119154410515"><a name="p8119154410515"></a><a name="p8119154410515"></a>topics</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="p5119154417519"><a name="p5119154417519"></a><a name="p5119154417519"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="p51191544556"><a name="p51191544556"></a><a name="p51191544556"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.5.1.4 "><p id="p51191844655"><a name="p51191844655"></a><a name="p51191844655"></a>Indicates the list of topics to be deleted.</p>
</td>
</tr>
</tbody>
</table>

**Example Request**

```
 {
  "topics" : ["hah", "aabb"]
 }
```

## Response<a name="section19101644156"></a>

**Response parameters**

[Table 3](#table10111744455)  describes the parameter.

**Table  3**  Parameter description

<a name="table10111744455"></a>
<table><thead align="left"><tr id="row41192441858"><th class="cellrowborder" valign="top" width="23.23%" id="mcps1.2.4.1.1"><p id="p121201944354"><a name="p121201944354"></a><a name="p121201944354"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="22.220000000000002%" id="mcps1.2.4.1.2"><p id="p1812011441515"><a name="p1812011441515"></a><a name="p1812011441515"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="54.55%" id="mcps1.2.4.1.3"><p id="p51207446518"><a name="p51207446518"></a><a name="p51207446518"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row15120184418519"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p1112013442053"><a name="p1112013442053"></a><a name="p1112013442053"></a>topics</p>
</td>
<td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.2 "><p id="p1812019441651"><a name="p1812019441651"></a><a name="p1812019441651"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="54.55%" headers="mcps1.2.4.1.3 "><p id="p10120244959"><a name="p10120244959"></a><a name="p10120244959"></a>Indicates the list of topics.</p>
</td>
</tr>
</tbody>
</table>

**Table  4**  topics parameter description

<a name="table046213306109"></a>
<table><thead align="left"><tr id="row2046612306104"><th class="cellrowborder" valign="top" width="23.23%" id="mcps1.2.4.1.1"><p id="p1646783041010"><a name="p1646783041010"></a><a name="p1646783041010"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="22.220000000000002%" id="mcps1.2.4.1.2"><p id="p9468113091015"><a name="p9468113091015"></a><a name="p9468113091015"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="54.55%" id="mcps1.2.4.1.3"><p id="p1846903011104"><a name="p1846903011104"></a><a name="p1846903011104"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row64765308104"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p347823071014"><a name="p347823071014"></a><a name="p347823071014"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.2 "><p id="p15479730111010"><a name="p15479730111010"></a><a name="p15479730111010"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="54.55%" headers="mcps1.2.4.1.3 "><p id="p848023015100"><a name="p848023015100"></a><a name="p848023015100"></a>Indicates the topic name.</p>
</td>
</tr>
<tr id="row248183016109"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p19482163018103"><a name="p19482163018103"></a><a name="p19482163018103"></a>success</p>
</td>
<td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.2 "><p id="p3483153041011"><a name="p3483153041011"></a><a name="p3483153041011"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="54.55%" headers="mcps1.2.4.1.3 "><p id="p1348413061012"><a name="p1348413061012"></a><a name="p1348413061012"></a>Indicates whether the topic is deleted.</p>
</td>
</tr>
</tbody>
</table>

**Example response**

```
{
  "topics" : [{
      "id" : "haha",
      "success" : true
    }, {
      "id" : "aabb",
      "success" : true
    }
  ]
}
```

## Status Code<a name="section92216442511"></a>

[Table 5](#table6231844656)  describes the status code of successful operations. For details about other status codes, see  [Status Code](status-code.md).

**Table  5**  Status code

<a name="table6231844656"></a>
<table><thead align="left"><tr id="row1512019448511"><th class="cellrowborder" valign="top" width="15.15%" id="mcps1.2.3.1.1"><p id="p1120144453"><a name="p1120144453"></a><a name="p1120144453"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="84.85000000000001%" id="mcps1.2.3.1.2"><p id="p2012019445514"><a name="p2012019445514"></a><a name="p2012019445514"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row912012447517"><td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.2.3.1.1 "><p id="p912044411514"><a name="p912044411514"></a><a name="p912044411514"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="84.85000000000001%" headers="mcps1.2.3.1.2 "><p id="p71201441758"><a name="p71201441758"></a><a name="p71201441758"></a>The topics are successfully deleted.</p>
</td>
</tr>
</tbody>
</table>


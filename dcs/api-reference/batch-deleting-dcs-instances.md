# Batch Deleting DCS Instances<a name="dcs-api-0312009"></a>

## Function<a name="section0296157125313"></a>

This API is used to delete multiple DCS instances at a time.

## URI<a name="section2310177194512"></a>

DELETE /v1.0/\{project\_id\}/instances?allFailure=\{allFailure\}

[Table 1](#table4154121820350)  describes the parameters.

**Table  1**  Parameter description

<a name="table4154121820350"></a>
<table><thead align="left"><tr id="row17153191817358"><th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.1"><p id="p993885712414"><a name="p993885712414"></a><a name="p993885712414"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.2"><p id="p215314189354"><a name="p215314189354"></a><a name="p215314189354"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.3"><p id="p1715320185352"><a name="p1715320185352"></a><a name="p1715320185352"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="49%" id="mcps1.2.5.1.4"><p id="p215351873519"><a name="p215351873519"></a><a name="p215351873519"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row61531718163510"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.1 "><p id="p51531218183514"><a name="p51531218183514"></a><a name="p51531218183514"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p115311813514"><a name="p115311813514"></a><a name="p115311813514"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p815391853510"><a name="p815391853510"></a><a name="p815391853510"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.5.1.4 "><p id="p1153818143518"><a name="p1153818143518"></a><a name="p1153818143518"></a>Project ID.</p>
</td>
</tr>
<tr id="row1358873516587"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.1 "><p id="p1058923515811"><a name="p1058923515811"></a><a name="p1058923515811"></a>allFailure</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p55892352586"><a name="p55892352586"></a><a name="p55892352586"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p12589103595817"><a name="p12589103595817"></a><a name="p12589103595817"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.5.1.4 "><p id="p15502183214592"><a name="p15502183214592"></a><a name="p15502183214592"></a>An indicator of whether all DCS instances failed to be created will be deleted. Options:</p>
<p id="p329463011582"><a name="p329463011582"></a><a name="p329463011582"></a>Options:</p>
<a name="ul2019045014587"></a><a name="ul2019045014587"></a><ul id="ul2019045014587"><li><strong id="b61661321141315"><a name="b61661321141315"></a><a name="b61661321141315"></a>true</strong>: all instances that fail to be created are deleted. In this case, the <strong id="b1816772120133"><a name="b1816772120133"></a><a name="b1816772120133"></a>instances</strong> parameter in the request can be empty.</li><li><strong id="b1861744910131"><a name="b1861744910131"></a><a name="b1861744910131"></a>false</strong> or other values: The DCS instances specified by the instances parameter in the API request will be deleted.</li></ul>
</td>
</tr>
</tbody>
</table>

## Request<a name="section41195764519"></a>

**Request parameters**

[Table 2](#table166993107405)  describes the request parameters.

**Table  2**  Parameter description

<a name="table166993107405"></a>
<table><thead align="left"><tr id="row7700310174015"><th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.1"><p id="p770012105401"><a name="p770012105401"></a><a name="p770012105401"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.2"><p id="p5700201018409"><a name="p5700201018409"></a><a name="p5700201018409"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.3"><p id="p0700210154019"><a name="p0700210154019"></a><a name="p0700210154019"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="49%" id="mcps1.2.5.1.4"><p id="p9700610174018"><a name="p9700610174018"></a><a name="p9700610174018"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row13700121010407"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.1 "><p id="p970020103409"><a name="p970020103409"></a><a name="p970020103409"></a>instances</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="p17631931174018"><a name="p17631931174018"></a><a name="p17631931174018"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.3 "><p id="p177632031124010"><a name="p177632031124010"></a><a name="p177632031124010"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.2.5.1.4 "><p id="p10763173116404"><a name="p10763173116404"></a><a name="p10763173116404"></a>IDs of DCS instances to be deleted.</p>
<p id="p142599468162"><a name="p142599468162"></a><a name="p142599468162"></a>This parameter is set only when the <strong id="b16776102555"><a name="b16776102555"></a><a name="b16776102555"></a>allFailure</strong> parameter in the URI is set to <strong id="b13677191065513"><a name="b13677191065513"></a><a name="b13677191065513"></a>false</strong> or another value.</p>
<p id="p745592135517"><a name="p745592135517"></a><a name="p745592135517"></a>A maximum of 50 instances can be deleted at a time.</p>
</td>
</tr>
</tbody>
</table>

**Request URL:**

```
DELETE https://{dcs_endpoint}/v1.0/{project_id}/instances?allFailure={allFailure}
```

Example request with  **allFailure **set to  **false**:

```
{
    "instances": [
        "54602a9d-5e22-4239-9123-77e350df4a34",
        "7166cdea-dbad-4d79-9610-7163e6f8b640"
    ]
}
```

## Response<a name="section11426254461"></a>

**Response parameters**

If the value of the  **allFailure**  parameter in the URI is  **true**, all DCS instances that the tenant specified by  **project\_id**  that failed to create are deleted and an empty response is then returned. If the value of the  **allFailure**  parameter in the URI is  **false**, the DCS instances specified by the  **instances**  parameter in the API request are deleted and a response containing the parameter in  [Table 3](#table18935105020414)  is then returned.

**Table  3**  Parameter description

<a name="table18935105020414"></a>
<table><thead align="left"><tr id="row1493665014412"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.1"><p id="p193616504419"><a name="p193616504419"></a><a name="p193616504419"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.4.1.2"><p id="p1093625014113"><a name="p1093625014113"></a><a name="p1093625014113"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="66%" id="mcps1.2.4.1.3"><p id="p139361650174115"><a name="p139361650174115"></a><a name="p139361650174115"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row169361650194119"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.1 "><p id="p183851432217"><a name="p183851432217"></a><a name="p183851432217"></a>results</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.4.1.2 "><p id="p10385339215"><a name="p10385339215"></a><a name="p10385339215"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.4.1.3 "><p id="p1038583526"><a name="p1038583526"></a><a name="p1038583526"></a>For details about how to delete an instance, see <a href="#table69371750154117">Table 4</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4**  results parameter description

<a name="table69371750154117"></a>
<table><thead align="left"><tr id="row11938155054119"><th class="cellrowborder" valign="top" width="27.27%" id="mcps1.2.4.1.1"><p id="p1693811501414"><a name="p1693811501414"></a><a name="p1693811501414"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.05%" id="mcps1.2.4.1.2"><p id="p1493819508416"><a name="p1493819508416"></a><a name="p1493819508416"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="55.67999999999999%" id="mcps1.2.4.1.3"><p id="p3938155084118"><a name="p3938155084118"></a><a name="p3938155084118"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row17938145064112"><td class="cellrowborder" valign="top" width="27.27%" headers="mcps1.2.4.1.1 "><p id="p173482043021"><a name="p173482043021"></a><a name="p173482043021"></a>instance</p>
</td>
<td class="cellrowborder" valign="top" width="17.05%" headers="mcps1.2.4.1.2 "><p id="p10348143625"><a name="p10348143625"></a><a name="p10348143625"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.67999999999999%" headers="mcps1.2.4.1.3 "><p id="p83483431425"><a name="p83483431425"></a><a name="p83483431425"></a>DCS instance ID.</p>
</td>
</tr>
<tr id="row1093895010417"><td class="cellrowborder" valign="top" width="27.27%" headers="mcps1.2.4.1.1 "><p id="p63481043623"><a name="p63481043623"></a><a name="p63481043623"></a>result</p>
</td>
<td class="cellrowborder" valign="top" width="17.05%" headers="mcps1.2.4.1.2 "><p id="p1348943822"><a name="p1348943822"></a><a name="p1348943822"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.67999999999999%" headers="mcps1.2.4.1.3 "><p id="p1934820431025"><a name="p1934820431025"></a><a name="p1934820431025"></a>Instance deletion result. Options: <strong id="b20263553587"><a name="b20263553587"></a><a name="b20263553587"></a>success</strong> and <strong id="b426335155811"><a name="b426335155811"></a><a name="b426335155811"></a>failed</strong></p>
</td>
</tr>
</tbody>
</table>

**Example response**

```
{
    "results": [
        {
            "instance": "54602a9d-5e22-4239-9123-77e350df4a34",
            "result": "success"
        },
        {
            "instance": "7166cdea-dbad-4d79-9610-7163e6f8b640",
            "result": "success"
        }
    ]
}
```

## Status Code<a name="section5301161961211"></a>

[Table 5](#table8301101911215)  describes the status code of successful operations. For details about other status codes, see  [Table 1](status-codes.md#table5210141351517).

**Table  5**  Status codes

<a name="table8301101911215"></a>
<table><thead align="left"><tr id="row11302101915124"><th class="cellrowborder" valign="top" width="15.98%" id="mcps1.2.3.1.1"><p id="p73021519101210"><a name="p73021519101210"></a><a name="p73021519101210"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="84.02%" id="mcps1.2.3.1.2"><p id="p830281981219"><a name="p830281981219"></a><a name="p830281981219"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row16302121941211"><td class="cellrowborder" valign="top" width="15.98%" headers="mcps1.2.3.1.1 "><p id="p63027192128"><a name="p63027192128"></a><a name="p63027192128"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="84.02%" headers="mcps1.2.3.1.2 "><p id="p1302171916124"><a name="p1302171916124"></a><a name="p1302171916124"></a>DCS instances deleted successfully.</p>
</td>
</tr>
<tr id="row182271411314"><td class="cellrowborder" valign="top" width="15.98%" headers="mcps1.2.3.1.1 "><p id="p168231014739"><a name="p168231014739"></a><a name="p168231014739"></a>204</p>
</td>
<td class="cellrowborder" valign="top" width="84.02%" headers="mcps1.2.3.1.2 "><p id="p38237146312"><a name="p38237146312"></a><a name="p38237146312"></a>DCS instances that failed to be created are cleared successfully.</p>
</td>
</tr>
</tbody>
</table>


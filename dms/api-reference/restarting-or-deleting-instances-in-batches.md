# Restarting or Deleting Instances in Batches<a name="EN-US_TOPIC_0128036898"></a>

## Function<a name="section321013247298"></a>

This API is used to restart or delete instances in batches.

When an instance is being restarted, message retrieval and creation requests of the client will be rejected.

Deleting an instance will delete the data in the instance without any backup. Exercise caution when performing this operation.

## URI<a name="section17897053122710"></a>

POST /v1.0/\{project\_id\}/instances/action

[Table 1](#table98991536279)  describes the parameters.

**Table  1**  Parameter description

<a name="table98991536279"></a>
<table><thead align="left"><tr id="row2421954132717"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p18421354142717"><a name="p18421354142717"></a><a name="p18421354142717"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p1442154182712"><a name="p1442154182712"></a><a name="p1442154182712"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p134215540272"><a name="p134215540272"></a><a name="p134215540272"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p1942054192712"><a name="p1942054192712"></a><a name="p1942054192712"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row174218545276"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p042165452713"><a name="p042165452713"></a><a name="p042165452713"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p642185410277"><a name="p642185410277"></a><a name="p642185410277"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p1742105422714"><a name="p1742105422714"></a><a name="p1742105422714"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p342155414271"><a name="p342155414271"></a><a name="p342155414271"></a>Indicates the ID of a project.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section20906753102710"></a>

Request

[Table 2](#table890715392717)  describes the parameters.

**Table  2**  Parameter description

<a name="table890715392717"></a>
<table><thead align="left"><tr id="row154205417279"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="p74275452714"><a name="p74275452714"></a><a name="p74275452714"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.2.5.1.2"><p id="p13421654192714"><a name="p13421654192714"></a><a name="p13421654192714"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.3"><p id="p74245402717"><a name="p74245402717"></a><a name="p74245402717"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="48%" id="mcps1.2.5.1.4"><p id="p1242754122714"><a name="p1242754122714"></a><a name="p1242754122714"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row942254172717"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p24295410275"><a name="p24295410275"></a><a name="p24295410275"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.2 "><p id="p1443254122713"><a name="p1443254122713"></a><a name="p1443254122713"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="p174314544275"><a name="p174314544275"></a><a name="p174314544275"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.5.1.4 "><p id="p18438543272"><a name="p18438543272"></a><a name="p18438543272"></a>Indicates the operation to be performed on instances. The value of this parameter can be <strong id="b57981349164915"><a name="b57981349164915"></a><a name="b57981349164915"></a>restart</strong> or <strong id="b1350185244918"><a name="b1350185244918"></a><a name="b1350185244918"></a>delete</strong>.</p>
</td>
</tr>
<tr id="row44365416273"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p124355442710"><a name="p124355442710"></a><a name="p124355442710"></a>instances</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.2 "><p id="p343185482711"><a name="p343185482711"></a><a name="p343185482711"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="p84335411274"><a name="p84335411274"></a><a name="p84335411274"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.5.1.4 "><p id="p1143195410277"><a name="p1143195410277"></a><a name="p1143195410277"></a>Indicates the list of instance IDs.</p>
</td>
</tr>
<tr id="row22669518122"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p762912810123"><a name="p762912810123"></a><a name="p762912810123"></a>allFailure</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.2 "><p id="p156297819125"><a name="p156297819125"></a><a name="p156297819125"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.3 "><p id="p162968111215"><a name="p162968111215"></a><a name="p162968111215"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.5.1.4 "><p id="p984618492271"><a name="p984618492271"></a><a name="p984618492271"></a>When set to <strong id="b1835991302110"><a name="b1835991302110"></a><a name="b1835991302110"></a>kafka</strong>, indicates all Kafka instances that fail to be created are to be deleted.</p>
</td>
</tr>
</tbody>
</table>

**Example request**

Restarting instances in batches:

```
{ 
    "action" : "restart", 
    "instances" : ["54602a9d-5e22-4239-9123-77e350df4a34", "7166cdea-dbad-4d79-9610-7163e6f8b640"] 
}
```

Deleting instances in batches:

```
{ 
    "action" : "delete", 
    "instances" : ["54602a9d-5e22-4239-9123-77e350df4a34", "7166cdea-dbad-4d79-9610-7163e6f8b640"] 
}
```

Deleting all instances that fail to be created:

```
{ 
    "action" : "delete", 
    "allFailure" : "kafka"
}
```

## Response<a name="section8923953182713"></a>

**Response parameters**

When  **action**  is set to  **delete**,  **allFailure**  is set to  **kafka**, and an empty response is returned, the instances are deleted successfully.  [Table 3](#table189241953152710)  describes the parameters.

**Table  3**  Parameter description

<a name="table189241953152710"></a>
<table><thead align="left"><tr id="row1943054162712"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p043854162718"><a name="p043854162718"></a><a name="p043854162718"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p174325482711"><a name="p174325482711"></a><a name="p174325482711"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p443254102717"><a name="p443254102717"></a><a name="p443254102717"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row44311544276"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p124365415272"><a name="p124365415272"></a><a name="p124365415272"></a>results</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p643205442711"><a name="p643205442711"></a><a name="p643205442711"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p84335442713"><a name="p84335442713"></a><a name="p84335442713"></a>Indicates the result of instance modification.</p>
</td>
</tr>
</tbody>
</table>

**Table  4**  results parameter description

<a name="table1693155317278"></a>
<table><thead align="left"><tr id="row943175422716"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p20435545279"><a name="p20435545279"></a><a name="p20435545279"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p144315543273"><a name="p144315543273"></a><a name="p144315543273"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p14335418274"><a name="p14335418274"></a><a name="p14335418274"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row204335416274"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1143195482715"><a name="p1143195482715"></a><a name="p1143195482715"></a>instance</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1043105422712"><a name="p1043105422712"></a><a name="p1043105422712"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p4438545273"><a name="p4438545273"></a><a name="p4438545273"></a>Indicates the instance ID.</p>
</td>
</tr>
<tr id="row3431954182714"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p74345462715"><a name="p74345462715"></a><a name="p74345462715"></a>result</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p164315415279"><a name="p164315415279"></a><a name="p164315415279"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1044125413276"><a name="p1044125413276"></a><a name="p1044125413276"></a>Indicates an operation result, which can be <strong id="b115401432163319"><a name="b115401432163319"></a><a name="b115401432163319"></a>success</strong> or <strong id="b154018322337"><a name="b154018322337"></a><a name="b154018322337"></a>failed</strong></p>
</td>
</tr>
</tbody>
</table>

**Example response**

```
{ 
    "results": [ 
        { 
            "result": "success", 
            "instance": "afc90a2a-a02c-4cba-94d5-58dfa9ad1e0d" 
        }, 
        { 
            "result": "success", 
            "instance": "67fc5f8d-3986-4f02-bb75-4075a23112de" 
        } 
    ] 
}
```

## Status Code<a name="section494465382712"></a>

[Table 5](#table17944125315273)  describes the status code of successful operations. For details about other status codes, see  [Status Code](status-code.md).

**Table  5**  Status code

<a name="table17944125315273"></a>
<table><thead align="left"><tr id="row1745105419271"><th class="cellrowborder" valign="top" width="15.15%" id="mcps1.2.3.1.1"><p id="p11451954102710"><a name="p11451954102710"></a><a name="p11451954102710"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="84.85000000000001%" id="mcps1.2.3.1.2"><p id="p184520544272"><a name="p184520544272"></a><a name="p184520544272"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row645205411275"><td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.2.3.1.1 "><p id="p345155472710"><a name="p345155472710"></a><a name="p345155472710"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="84.85000000000001%" headers="mcps1.2.3.1.2 "><p id="p8451954152719"><a name="p8451954152719"></a><a name="p8451954152719"></a>The instances are restarted or deleted successfully.</p>
</td>
</tr>
</tbody>
</table>


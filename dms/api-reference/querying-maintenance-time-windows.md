# Querying Maintenance Time Windows<a name="EN-US_TOPIC_0128036903"></a>

## Function<a name="section51971645131316"></a>

This API is used to query the start and end time of the maintenance window.

## URI<a name="section747445721120"></a>

GET /v1.0/instances/maintain-windows

## Request<a name="section1547413577114"></a>

**Request parameters**

None.

**Example Request**

None.

## Response<a name="section15475195711113"></a>

**Response parameters**

[Table 1](#table04768576115)  and  [Table 2](#table748235716115)  describe the response parameters.

**Table  1**  Parameter description

<a name="table04768576115"></a>
<table><thead align="left"><tr id="row14577185716113"><th class="cellrowborder" valign="top" width="19%" id="mcps1.2.4.1.1"><p id="p8577135719113"><a name="p8577135719113"></a><a name="p8577135719113"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.2"><p id="p857745731115"><a name="p857745731115"></a><a name="p857745731115"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="56.00000000000001%" id="mcps1.2.4.1.3"><p id="p1957785713116"><a name="p1957785713116"></a><a name="p1957785713116"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row157725711111"><td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.1 "><p id="p16577125741112"><a name="p16577125741112"></a><a name="p16577125741112"></a>maintain_windows</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.2 "><p id="p175771857111112"><a name="p175771857111112"></a><a name="p175771857111112"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.2.4.1.3 "><p id="p7577155714112"><a name="p7577155714112"></a><a name="p7577155714112"></a>Indicates a list of supported maintenance time windows.</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  maintain\_windows parameter description

<a name="table748235716115"></a>
<table><thead align="left"><tr id="row1857745761111"><th class="cellrowborder" valign="top" width="24%" id="mcps1.2.4.1.1"><p id="p35779572111"><a name="p35779572111"></a><a name="p35779572111"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.2"><p id="p165779572119"><a name="p165779572119"></a><a name="p165779572119"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="53%" id="mcps1.2.4.1.3"><p id="p0577185711113"><a name="p0577185711113"></a><a name="p0577185711113"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row0577175719114"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p157817574116"><a name="p157817574116"></a><a name="p157817574116"></a>seq</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="p557895791115"><a name="p557895791115"></a><a name="p557895791115"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.4.1.3 "><p id="p857885771118"><a name="p857885771118"></a><a name="p857885771118"></a>Indicates the sequential number of a maintenance time window.</p>
</td>
</tr>
<tr id="row9578165718115"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p13578125711113"><a name="p13578125711113"></a><a name="p13578125711113"></a>begin</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="p115789578119"><a name="p115789578119"></a><a name="p115789578119"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.4.1.3 "><p id="p957825714112"><a name="p957825714112"></a><a name="p957825714112"></a>Indicates the time at which a maintenance time window starts.</p>
</td>
</tr>
<tr id="row157819575116"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p16578165771110"><a name="p16578165771110"></a><a name="p16578165771110"></a>end</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="p6578185751118"><a name="p6578185751118"></a><a name="p6578185751118"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.4.1.3 "><p id="p1757811578116"><a name="p1757811578116"></a><a name="p1757811578116"></a>Indicates the time at which a maintenance time window ends.</p>
</td>
</tr>
<tr id="row205787575119"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p1578175715114"><a name="p1578175715114"></a><a name="p1578175715114"></a>default</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="p135781757101115"><a name="p135781757101115"></a><a name="p135781757101115"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.2.4.1.3 "><p id="p1557865712114"><a name="p1557865712114"></a><a name="p1557865712114"></a>Indicates whether a maintenance time window is set to the default time segment.</p>
</td>
</tr>
</tbody>
</table>

**Example response**

```
{ 
    "maintain_windows": [ 
        { 
            "seq": 1, 
            "begin": "22", 
            "end": "02", 
            "default": false 
        }, 
        { 
            "seq": 2, 
            "begin": "02", 
            "end": "06", 
            "default": true 
        }, 
        { 
            "seq": 3, 
            "begin": "06", 
            "end": "10", 
            "default": false 
        }, 
        { 
            "seq": 4, 
            "begin": "10", 
            "end": "14", 
            "default": false 
        }, 
        { 
            "seq": 5, 
            "begin": "14", 
            "end": "18", 
            "default": false 
        }, 
        { 
            "seq": 6, 
            "begin": "18", 
            "end": "22", 
            "default": false 
        } 
    ] 
}
```

## Status Code<a name="section10504657101112"></a>

[Table 3](#table155041657181114)  describes the status code of successful operations. For details about other status codes, see  [Status Code](status-code.md).

**Table  3**  Status code

<a name="table155041657181114"></a>
<table><thead align="left"><tr id="row1157985731113"><th class="cellrowborder" valign="top" width="15.15%" id="mcps1.2.3.1.1"><p id="p195791357141117"><a name="p195791357141117"></a><a name="p195791357141117"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="84.85000000000001%" id="mcps1.2.3.1.2"><p id="p205791357161114"><a name="p205791357161114"></a><a name="p205791357161114"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row8579195751118"><td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.2.3.1.1 "><p id="p8579105713119"><a name="p8579105713119"></a><a name="p8579105713119"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="84.85000000000001%" headers="mcps1.2.3.1.2 "><p id="p6579175761116"><a name="p6579175761116"></a><a name="p6579175761116"></a>The maintenance time windows are queried successfully.</p>
</td>
</tr>
</tbody>
</table>


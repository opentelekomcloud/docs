# Querying AZ Information<a name="EN-US_TOPIC_0128036911"></a>

## Function<a name="section1073032015911"></a>

This API is used to query the AZ ID.

## URI<a name="section023216425361"></a>

GET /v1.0/availableZones

## Request<a name="section11232742133616"></a>

**Request parameters**

None.

**Example request**

None.

## Response<a name="section16232164233620"></a>

**Response parameters**

[Table 1](#table2233942133618)  and  [Table 2](#table1124311429360)  describe the parameters.

**Table  1**  Response parameters

<a name="table2233942133618"></a>
<table><thead align="left"><tr id="row2033834243618"><th class="cellrowborder" valign="top" width="20.200000000000003%" id="mcps1.2.4.1.1"><p id="p43381342103617"><a name="p43381342103617"></a><a name="p43381342103617"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="24.240000000000002%" id="mcps1.2.4.1.2"><p id="p133815422366"><a name="p133815422366"></a><a name="p133815422366"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="55.559999999999995%" id="mcps1.2.4.1.3"><p id="p333804203617"><a name="p333804203617"></a><a name="p333804203617"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row4338154217363"><td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.2.4.1.1 "><p id="p63381842123617"><a name="p63381842123617"></a><a name="p63381842123617"></a>regionId</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p14338184253613"><a name="p14338184253613"></a><a name="p14338184253613"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.559999999999995%" headers="mcps1.2.4.1.3 "><p id="p1338342193611"><a name="p1338342193611"></a><a name="p1338342193611"></a>Indicates the region ID.</p>
</td>
</tr>
<tr id="row11338942173613"><td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.2.4.1.1 "><p id="p133382042133614"><a name="p133382042133614"></a><a name="p133382042133614"></a>available_zones</p>
</td>
<td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.2.4.1.2 "><p id="p10338342103612"><a name="p10338342103612"></a><a name="p10338342103612"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="55.559999999999995%" headers="mcps1.2.4.1.3 "><p id="p2033818429368"><a name="p2033818429368"></a><a name="p2033818429368"></a>Indicates details of AZs. For details, see <a href="#table1124311429360">Table 2</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  available\_zones parameter description

<a name="table1124311429360"></a>
<table><thead align="left"><tr id="row153391342163613"><th class="cellrowborder" valign="top" width="18.18%" id="mcps1.2.4.1.1"><p id="p1033904212362"><a name="p1033904212362"></a><a name="p1033904212362"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20.200000000000003%" id="mcps1.2.4.1.2"><p id="p133391942203617"><a name="p133391942203617"></a><a name="p133391942203617"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="61.62%" id="mcps1.2.4.1.3"><p id="p5339134263615"><a name="p5339134263615"></a><a name="p5339134263615"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1433920421369"><td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.1 "><p id="p23391425367"><a name="p23391425367"></a><a name="p23391425367"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.2.4.1.2 "><p id="p193391142113619"><a name="p193391142113619"></a><a name="p193391142113619"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p033964216368"><a name="p033964216368"></a><a name="p033964216368"></a>Indicates the ID of an AZ.</p>
</td>
</tr>
<tr id="row163399426369"><td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.1 "><p id="p143391242163613"><a name="p143391242163613"></a><a name="p143391242163613"></a>code</p>
</td>
<td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.2.4.1.2 "><p id="p10339124293616"><a name="p10339124293616"></a><a name="p10339124293616"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p12339842193616"><a name="p12339842193616"></a><a name="p12339842193616"></a>Indicates the code of an AZ.</p>
</td>
</tr>
<tr id="row3339194219367"><td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.1 "><p id="p17339104273614"><a name="p17339104273614"></a><a name="p17339104273614"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.2.4.1.2 "><p id="p1033964218367"><a name="p1033964218367"></a><a name="p1033964218367"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p1333913425367"><a name="p1333913425367"></a><a name="p1333913425367"></a>Indicates the name of an AZ.</p>
</td>
</tr>
<tr id="row1339164213368"><td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.1 "><p id="p1733974216368"><a name="p1733974216368"></a><a name="p1733974216368"></a>port</p>
</td>
<td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.2.4.1.2 "><p id="p1733984263620"><a name="p1733984263620"></a><a name="p1733984263620"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p43391842153613"><a name="p43391842153613"></a><a name="p43391842153613"></a>Indicates the port number of an AZ.</p>
</td>
</tr>
<tr id="row9339104283613"><td class="cellrowborder" valign="top" width="18.18%" headers="mcps1.2.4.1.1 "><p id="p03391442173616"><a name="p03391442173616"></a><a name="p03391442173616"></a>resource_availability</p>
</td>
<td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.2.4.1.2 "><p id="p1833914273613"><a name="p1833914273613"></a><a name="p1833914273613"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="61.62%" headers="mcps1.2.4.1.3 "><p id="p1133924211367"><a name="p1133924211367"></a><a name="p1133924211367"></a>Indicates whether an AZ has available resources.</p>
<a name="ul14339124273615"></a><a name="ul14339124273615"></a><ul id="ul14339124273615"><li><strong id="b123191342313"><a name="b123191342313"></a><a name="b123191342313"></a>true</strong>: The AZ has available resources.</li><li><strong id="b522523693114"><a name="b522523693114"></a><a name="b522523693114"></a>false</strong>: Resources of the AZ have been sold out.</li></ul>
</td>
</tr>
</tbody>
</table>

**Example response**

```
{  
    regionId: "XXXXXX",  
    available_zones:[  
       {  
            "id":"1d7b939b382c4c3bb3481a8ca10da768",  
            "name":"az10.dc1",  
            "code":"az10.dc1",  
            "port":"8002", 
            "resource_availability": "true" 
        },    
        {  
            "id":"1d7b939b382c4c3bb3481a8ca10da769",  
            "name":"az10.dc2",  
            "code":"az10.dc2",  
            "port":"8002", 
            "resource_availability": "true" 
        }  
    ]  
}
```

## Status Code<a name="section19258742123617"></a>

[Table 3](#table825911423368)  describes the status code of successful operations. For details about other status codes, see  [Status Code](status-code.md).

**Table  3**  Status code

<a name="table825911423368"></a>
<table><thead align="left"><tr id="row1234174211367"><th class="cellrowborder" valign="top" width="15.15%" id="mcps1.2.3.1.1"><p id="p834194213610"><a name="p834194213610"></a><a name="p834194213610"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="84.85000000000001%" id="mcps1.2.3.1.2"><p id="p16341542163614"><a name="p16341542163614"></a><a name="p16341542163614"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1334174273613"><td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.2.3.1.1 "><p id="p143411242133620"><a name="p143411242133620"></a><a name="p143411242133620"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="84.85000000000001%" headers="mcps1.2.3.1.2 "><p id="p1334114211361"><a name="p1334114211361"></a><a name="p1334114211361"></a>The AZ information is successfully queried.</p>
</td>
</tr>
</tbody>
</table>


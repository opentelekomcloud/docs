# Querying AZ Information<a name="dcs-api-0312039"></a>

## Function<a name="section164151825713"></a>

This API is used to query the ID of the AZ where a DCS instance resides. 

## URI<a name="section11589173274"></a>

GET /v1.0/availableZones

## Request<a name="section1271822314281"></a>

**Request parameters**

None.

**Example request**

None.

## Response<a name="section1745154162813"></a>

**Response parameters**

[Table 1](#table5725353918)  describes the response parameters.

**Table  1**  Parameter description

<a name="table5725353918"></a>
<table><thead align="left"><tr id="row1862534399"><th class="cellrowborder" valign="top" width="20.41%" id="mcps1.2.4.1.1"><p id="p2615536391"><a name="p2615536391"></a><a name="p2615536391"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="24.490000000000002%" id="mcps1.2.4.1.2"><p id="p86453163917"><a name="p86453163917"></a><a name="p86453163917"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="55.1%" id="mcps1.2.4.1.3"><p id="p196135383919"><a name="p196135383919"></a><a name="p196135383919"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row137195353920"><td class="cellrowborder" valign="top" width="20.41%" headers="mcps1.2.4.1.1 "><p id="p126953173914"><a name="p126953173914"></a><a name="p126953173914"></a>regionId</p>
</td>
<td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.2 "><p id="p197135314392"><a name="p197135314392"></a><a name="p197135314392"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.1%" headers="mcps1.2.4.1.3 "><p id="p18755363917"><a name="p18755363917"></a><a name="p18755363917"></a>Region ID.</p>
</td>
</tr>
<tr id="row075534392"><td class="cellrowborder" valign="top" width="20.41%" headers="mcps1.2.4.1.1 "><p id="p6715311397"><a name="p6715311397"></a><a name="p6715311397"></a>available_zones</p>
</td>
<td class="cellrowborder" valign="top" width="24.490000000000002%" headers="mcps1.2.4.1.2 "><p id="p7755373913"><a name="p7755373913"></a><a name="p7755373913"></a>Array</p>
</td>
<td class="cellrowborder" valign="top" width="55.1%" headers="mcps1.2.4.1.3 "><p id="p3775313395"><a name="p3775313395"></a><a name="p3775313395"></a>Array of AZs. For details, see <a href="#table20901104905614">Table 2</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  Parameter description of the available\_zones array

<a name="table20901104905614"></a>
<table><thead align="left"><tr id="row12901249155618"><th class="cellrowborder" valign="top" width="21.21212121212121%" id="mcps1.2.4.1.1"><p id="p6686654192615"><a name="p6686654192615"></a><a name="p6686654192615"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20.202020202020204%" id="mcps1.2.4.1.2"><p id="p129029492566"><a name="p129029492566"></a><a name="p129029492566"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="58.58585858585859%" id="mcps1.2.4.1.3"><p id="p690217494561"><a name="p690217494561"></a><a name="p690217494561"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row139022491568"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.4.1.1 "><p id="p1290214497560"><a name="p1290214497560"></a><a name="p1290214497560"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.2 "><p id="p29021492564"><a name="p29021492564"></a><a name="p29021492564"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.58585858585859%" headers="mcps1.2.4.1.3 "><p id="p1990217498567"><a name="p1990217498567"></a><a name="p1990217498567"></a>AZ ID.</p>
</td>
</tr>
<tr id="row490216496566"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.4.1.1 "><p id="p2902164995619"><a name="p2902164995619"></a><a name="p2902164995619"></a>code</p>
</td>
<td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.2 "><p id="p1902124917569"><a name="p1902124917569"></a><a name="p1902124917569"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.58585858585859%" headers="mcps1.2.4.1.3 "><p id="p1490212498563"><a name="p1490212498563"></a><a name="p1490212498563"></a>AZ code.</p>
</td>
</tr>
<tr id="row119023498565"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.4.1.1 "><p id="p15902649165614"><a name="p15902649165614"></a><a name="p15902649165614"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.2 "><p id="p119022492561"><a name="p119022492561"></a><a name="p119022492561"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.58585858585859%" headers="mcps1.2.4.1.3 "><p id="p2902204935616"><a name="p2902204935616"></a><a name="p2902204935616"></a>AZ name.</p>
</td>
</tr>
<tr id="row890204912564"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.4.1.1 "><p id="p79021549175610"><a name="p79021549175610"></a><a name="p79021549175610"></a>port</p>
</td>
<td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.2 "><p id="p10902949165614"><a name="p10902949165614"></a><a name="p10902949165614"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.58585858585859%" headers="mcps1.2.4.1.3 "><p id="p17902154925615"><a name="p17902154925615"></a><a name="p17902154925615"></a>Port number of the AZ.</p>
</td>
</tr>
<tr id="row1285718223542"><td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.4.1.1 "><p id="p28591422145411"><a name="p28591422145411"></a><a name="p28591422145411"></a>resource_availability</p>
</td>
<td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.4.1.2 "><p id="p11859172215541"><a name="p11859172215541"></a><a name="p11859172215541"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="58.58585858585859%" headers="mcps1.2.4.1.3 "><p id="p1219863831719"><a name="p1219863831719"></a><a name="p1219863831719"></a>An indicator of whether there are available resources in the AZ.</p>
<a name="ul17198113812171"></a><a name="ul17198113812171"></a><ul id="ul17198113812171"><li><strong id="b137424216583"><a name="b137424216583"></a><a name="b137424216583"></a>true</strong>: There are available resources in the AZ.</li><li><strong id="b149921347175818"><a name="b149921347175818"></a><a name="b149921347175818"></a>false</strong>: All resources have been used up in the AZ.</li></ul>
</td>
</tr>
</tbody>
</table>

**Example response**

```
{
    "regionId": "XXXXXX",
    "available_zones": [
        {
            "id": "f84448fd537f46078dd8bd776747f573",
            "code": "XXXXXX",
            "name": "XXXXXX",
            "port": "8003",
            "resource_availability": "true"
        },
        {
            "id": "12c47a78666b4e438cd0c692b9860387",
            "code": "XXXXXX",
            "name": "XXXXXX",
            "port": "8002",
            "resource_availability": "true"
        },
        {
            "id": "0725858e0d26434f9aa3dc5fc40d5697",
            "code": "XXXXXX",
            "name": "XXXXXX",
            "port": "8009",
            "resource_availability": "true"
        }
    ]
} 
```

## Status Code<a name="section9114171291417"></a>

[Table 3](#table201151124142)  describes the status code of successful operations. For details about other status codes, see  [Table 1](status-codes.md#table5210141351517).

**Table  3**  Status code

<a name="table201151124142"></a>
<table><thead align="left"><tr id="row61151912141410"><th class="cellrowborder" valign="top" width="15.98%" id="mcps1.2.3.1.1"><p id="p18115512151411"><a name="p18115512151411"></a><a name="p18115512151411"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="84.02%" id="mcps1.2.3.1.2"><p id="p41151712151419"><a name="p41151712151419"></a><a name="p41151712151419"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row811551251417"><td class="cellrowborder" valign="top" width="15.98%" headers="mcps1.2.3.1.1 "><p id="p17115201211417"><a name="p17115201211417"></a><a name="p17115201211417"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="84.02%" headers="mcps1.2.3.1.2 "><p id="p16116151214148"><a name="p16116151214148"></a><a name="p16116151214148"></a>AZ information queried successfully.</p>
</td>
</tr>
</tbody>
</table>


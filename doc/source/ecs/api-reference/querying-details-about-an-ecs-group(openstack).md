# Querying Details About an ECS Group<a name="EN-US_TOPIC_0065817722"></a>

## Function<a name="en-us_topic_0057973159_section30240326"></a>

This API is used to query details about an ECS group.

## URI<a name="en-us_topic_0057973159_section3727484"></a>

GET /v2/\{project\_id\}/os-server-groups/\{server\_group\_id\}

GET /v2.1/\{project\_id\}/os-server-groups/\{server\_group\_id\}

[Table 1](#en-us_topic_0057973159_en-us_topic_0020212650_table62669527)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="en-us_topic_0057973159_en-us_topic_0020212650_table62669527"></a>
<table><thead align="left"><tr id="en-us_topic_0057973159_en-us_topic_0020212650_row33894570"><th class="cellrowborder" valign="top" width="17.54175417541754%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.731773177317734%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="64.72647264726473%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973159_en-us_topic_0020212650_row8419032"><td class="cellrowborder" valign="top" width="17.54175417541754%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973159_en-us_topic_0020212650_p10852974"><a name="en-us_topic_0057973159_en-us_topic_0020212650_p10852974"></a><a name="en-us_topic_0057973159_en-us_topic_0020212650_p10852974"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.731773177317734%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973159_en-us_topic_0020212650_p6675738"><a name="en-us_topic_0057973159_en-us_topic_0020212650_p6675738"></a><a name="en-us_topic_0057973159_en-us_topic_0020212650_p6675738"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="64.72647264726473%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0057973159_row1856062192319"><td class="cellrowborder" valign="top" width="17.54175417541754%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973159_p16560926238"><a name="en-us_topic_0057973159_p16560926238"></a><a name="en-us_topic_0057973159_p16560926238"></a>server_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.731773177317734%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973159_p5560326232"><a name="en-us_topic_0057973159_p5560326232"></a><a name="en-us_topic_0057973159_p5560326232"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="64.72647264726473%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973159_p94577242237"><a name="en-us_topic_0057973159_p94577242237"></a><a name="en-us_topic_0057973159_p94577242237"></a>Specifies the ECS group UUID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section7947182095214"></a>

None

## Response<a name="en-us_topic_0057973159_section28398296"></a>

[Table 2](#en-us_topic_0057973159_table31776237)  describes the response parameters.

**Table  2**  Response parameters

<a name="en-us_topic_0057973159_table31776237"></a>
<table><thead align="left"><tr id="en-us_topic_0057973159_row27842754"><th class="cellrowborder" valign="top" width="18.62%" id="mcps1.2.4.1.1"><p id="en-us_topic_0057972670_p57733603"><a name="en-us_topic_0057972670_p57733603"></a><a name="en-us_topic_0057972670_p57733603"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18.44%" id="mcps1.2.4.1.2"><p id="en-us_topic_0057972670_p45910260"><a name="en-us_topic_0057972670_p45910260"></a><a name="en-us_topic_0057972670_p45910260"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="62.94%" id="mcps1.2.4.1.3"><p id="en-us_topic_0057972670_p32634650"><a name="en-us_topic_0057972670_p32634650"></a><a name="en-us_topic_0057972670_p32634650"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973159_row23461831"><td class="cellrowborder" valign="top" width="18.62%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973159_p21360177"><a name="en-us_topic_0057973159_p21360177"></a><a name="en-us_topic_0057973159_p21360177"></a>server_group</p>
</td>
<td class="cellrowborder" valign="top" width="18.44%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973159_p52452767"><a name="en-us_topic_0057973159_p52452767"></a><a name="en-us_topic_0057973159_p52452767"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="62.94%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973159_p8353193"><a name="en-us_topic_0057973159_p8353193"></a><a name="en-us_topic_0057973159_p8353193"></a>Specifies the ECS group information.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **server\_group**  parameters

<a name="en-us_topic_0057973159_table5520021"></a>
<table><thead align="left"><tr id="en-us_topic_0057973159_row52947946"><th class="cellrowborder" valign="top" width="18.62%" id="mcps1.2.4.1.1"><p id="p14850105762611"><a name="p14850105762611"></a><a name="p14850105762611"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18.44%" id="mcps1.2.4.1.2"><p id="p1685014574266"><a name="p1685014574266"></a><a name="p1685014574266"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="62.94%" id="mcps1.2.4.1.3"><p id="p168651757112614"><a name="p168651757112614"></a><a name="p168651757112614"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973159_row5110742"><td class="cellrowborder" valign="top" width="18.62%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973159_p11316939"><a name="en-us_topic_0057973159_p11316939"></a><a name="en-us_topic_0057973159_p11316939"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="18.44%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973159_p44256881"><a name="en-us_topic_0057973159_p44256881"></a><a name="en-us_topic_0057973159_p44256881"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.94%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973159_p56454382"><a name="en-us_topic_0057973159_p56454382"></a><a name="en-us_topic_0057973159_p56454382"></a>Specifies the ECS group UUID.</p>
</td>
</tr>
<tr id="en-us_topic_0057973159_row38327398"><td class="cellrowborder" valign="top" width="18.62%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973159_p17511496"><a name="en-us_topic_0057973159_p17511496"></a><a name="en-us_topic_0057973159_p17511496"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="18.44%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973159_p9145087"><a name="en-us_topic_0057973159_p9145087"></a><a name="en-us_topic_0057973159_p9145087"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.94%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973159_p5596939"><a name="en-us_topic_0057973159_p5596939"></a><a name="en-us_topic_0057973159_p5596939"></a>Specifies the ECS group name.</p>
</td>
</tr>
<tr id="en-us_topic_0057973159_row50372456"><td class="cellrowborder" valign="top" width="18.62%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973159_p53637170"><a name="en-us_topic_0057973159_p53637170"></a><a name="en-us_topic_0057973159_p53637170"></a>policies</p>
</td>
<td class="cellrowborder" valign="top" width="18.44%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973159_p49643541"><a name="en-us_topic_0057973159_p49643541"></a><a name="en-us_topic_0057973159_p49643541"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="62.94%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973159_p31957059"><a name="en-us_topic_0057973159_p31957059"></a><a name="en-us_topic_0057973159_p31957059"></a>Specifies the ECS group type.</p>
</td>
</tr>
<tr id="en-us_topic_0057973159_row19178079"><td class="cellrowborder" valign="top" width="18.62%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973159_p9920603"><a name="en-us_topic_0057973159_p9920603"></a><a name="en-us_topic_0057973159_p9920603"></a>members</p>
</td>
<td class="cellrowborder" valign="top" width="18.44%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973159_p65371346"><a name="en-us_topic_0057973159_p65371346"></a><a name="en-us_topic_0057973159_p65371346"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="62.94%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973159_p8656215"><a name="en-us_topic_0057973159_p8656215"></a><a name="en-us_topic_0057973159_p8656215"></a>Specifies the ECSs in an ECS group.</p>
</td>
</tr>
<tr id="en-us_topic_0057973159_row10797076"><td class="cellrowborder" valign="top" width="18.62%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973159_p2147930"><a name="en-us_topic_0057973159_p2147930"></a><a name="en-us_topic_0057973159_p2147930"></a>metadata</p>
</td>
<td class="cellrowborder" valign="top" width="18.44%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973159_p39764641"><a name="en-us_topic_0057973159_p39764641"></a><a name="en-us_topic_0057973159_p39764641"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="62.94%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973159_p43657808"><a name="en-us_topic_0057973159_p43657808"></a><a name="en-us_topic_0057973159_p43657808"></a>Specifies the ECS group metadata.</p>
</td>
</tr>
<tr id="en-us_topic_0057973159_row57375958"><td class="cellrowborder" valign="top" width="18.62%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973159_p16941010"><a name="en-us_topic_0057973159_p16941010"></a><a name="en-us_topic_0057973159_p16941010"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="18.44%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973159_p30044530"><a name="en-us_topic_0057973159_p30044530"></a><a name="en-us_topic_0057973159_p30044530"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.94%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973159_p23428799"><a name="en-us_topic_0057973159_p23428799"></a><a name="en-us_topic_0057973159_p23428799"></a>Specifies the tenant ID in UUID format for the ECS group.</p>
</td>
</tr>
<tr id="en-us_topic_0057973159_row975381085117"><td class="cellrowborder" valign="top" width="18.62%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973159_p187549109517"><a name="en-us_topic_0057973159_p187549109517"></a><a name="en-us_topic_0057973159_p187549109517"></a>user_id</p>
</td>
<td class="cellrowborder" valign="top" width="18.44%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973159_p090181716517"><a name="en-us_topic_0057973159_p090181716517"></a><a name="en-us_topic_0057973159_p090181716517"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="62.94%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973159_p39217176512"><a name="en-us_topic_0057973159_p39217176512"></a><a name="en-us_topic_0057973159_p39217176512"></a>Specifies the user ID in UUID format for the ECS group.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="en-us_topic_0057973159_section54258073"></a>

```
GET https://{endpoint}/v2/9c53a566cb3443ab910cf0daebca90c4/os-server-groups/5bbcc3c4-1da2-4437-a48a-66f15b1b13f9
GET https://{endpoint}/v2.1/9c53a566cb3443ab910cf0daebca90c4/os-server-groups/5bbcc3c4-1da2-4437-a48a-66f15b1b13f9
```

## Example Response<a name="section8761640135117"></a>

```
{
    "server_group": {
        "id": "5bbcc3c4-1da2-4437-a48a-66f15b1b13f9",
        "name": "test",
        "policies": ["anti-affinity"],
        "members": [],
        "metadata": {},
        "project_id": "9c53a566cb3443ab910cf0daebca90c4"
    }
}
```

## Returned Values<a name="en-us_topic_0057973159_section32827787"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).


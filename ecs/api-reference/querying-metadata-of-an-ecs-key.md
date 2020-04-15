# Querying Metadata of an ECS Key<a name="EN-US_TOPIC_0065817714"></a>

## Function<a name="en-us_topic_0057973169_section56350203"></a>

This API is used to query the metadata of an ECS key.

## URI<a name="en-us_topic_0057973169_section37389779"></a>

GET /v2/\{project\_id\}/servers/\{server\_id\}/metadata/\{key\}

GET /v2.1/\{project\_id\}/servers/\{server\_id\}/metadata/\{key\}

[Table 1](#en-us_topic_0057973169_table32475667)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="en-us_topic_0057973169_table32475667"></a>
<table><thead align="left"><tr id="en-us_topic_0057973169_row44937496"><th class="cellrowborder" valign="top" width="16.79%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.549999999999997%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.66%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973169_row1664874"><td class="cellrowborder" valign="top" width="16.79%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973169_p637140"><a name="en-us_topic_0057973169_p637140"></a><a name="en-us_topic_0057973169_p637140"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.549999999999997%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973169_p51608407"><a name="en-us_topic_0057973169_p51608407"></a><a name="en-us_topic_0057973169_p51608407"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.66%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0057973169_row41565035"><td class="cellrowborder" valign="top" width="16.79%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973169_p11324657"><a name="en-us_topic_0057973169_p11324657"></a><a name="en-us_topic_0057973169_p11324657"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.549999999999997%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973169_p44882061"><a name="en-us_topic_0057973169_p44882061"></a><a name="en-us_topic_0057973169_p44882061"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.66%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973169_p11568292"><a name="en-us_topic_0057973169_p11568292"></a><a name="en-us_topic_0057973169_p11568292"></a>Specifies the ECS ID.</p>
</td>
</tr>
<tr id="en-us_topic_0057973169_row1922793418562"><td class="cellrowborder" valign="top" width="16.79%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973169_p1922793475613"><a name="en-us_topic_0057973169_p1922793475613"></a><a name="en-us_topic_0057973169_p1922793475613"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="17.549999999999997%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973169_p122714346560"><a name="en-us_topic_0057973169_p122714346560"></a><a name="en-us_topic_0057973169_p122714346560"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.66%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973169_p2022718345561"><a name="en-us_topic_0057973169_p2022718345561"></a><a name="en-us_topic_0057973169_p2022718345561"></a>Specifies the ECS metadata key.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0057973169_section10950734"></a>

None

## Response<a name="en-us_topic_0057973169_section31447750"></a>

[Table 2](#en-us_topic_0057973169_table40140147)  describes the response parameters.

**Table  2**  Response parameters

<a name="en-us_topic_0057973169_table40140147"></a>
<table><thead align="left"><tr id="en-us_topic_0057973169_row18362576"><th class="cellrowborder" valign="top" width="21.48%" id="mcps1.2.4.1.1"><p id="en-us_topic_0057973169_p10973688"><a name="en-us_topic_0057973169_p10973688"></a><a name="en-us_topic_0057973169_p10973688"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18.099999999999998%" id="mcps1.2.4.1.2"><p id="en-us_topic_0057973169_p16453549"><a name="en-us_topic_0057973169_p16453549"></a><a name="en-us_topic_0057973169_p16453549"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="60.419999999999995%" id="mcps1.2.4.1.3"><p id="en-us_topic_0057973169_p40683740"><a name="en-us_topic_0057973169_p40683740"></a><a name="en-us_topic_0057973169_p40683740"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973169_row7048614"><td class="cellrowborder" valign="top" width="21.48%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973169_p34066844"><a name="en-us_topic_0057973169_p34066844"></a><a name="en-us_topic_0057973169_p34066844"></a>User-defined</p>
</td>
<td class="cellrowborder" valign="top" width="18.099999999999998%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973169_p7951016"><a name="en-us_topic_0057973169_p7951016"></a><a name="en-us_topic_0057973169_p7951016"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="60.419999999999995%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973169_p23029275"><a name="en-us_topic_0057973169_p23029275"></a><a name="en-us_topic_0057973169_p23029275"></a>Specifies the metadata key-value pair.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="en-us_topic_0057973169_section14594295"></a>

```
GET https://{endpoint}/v2/9c53a566cb3443ab910cf0daebca90c4/servers/998af54b-5762-4041-abc1-f98a2c27b3a2/metadata/key1
GET https://{endpoint}/v2.1/9c53a566cb3443ab910cf0daebca90c4/servers/998af54b-5762-4041-abc1-f98a2c27b3a2/metadata/key1
```

## Example Response<a name="section148361253124314"></a>

```
{
	"meta": {
		"key1": "value1"
	}
}
```

## Returned Values<a name="en-us_topic_0057973169_en-us_topic_0020212692_section22960139"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).


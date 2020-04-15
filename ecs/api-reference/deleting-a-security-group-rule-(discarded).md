# Deleting a Security Group Rule \(Discarded\)<a name="EN-US_TOPIC_0065817704"></a>

## Function<a name="en-us_topic_0057972668_section26649649"></a>

This API is used to delete a security group rule.

## Constraints<a name="en-us_topic_0057972668_section11137969"></a>

This API will be discarded. You are advised to use the desired network API. For details, see "Security Group \(Native OpenStack API\) \> Deleting a Security Group Rule" in  _Virtual Private Network API Reference_.

## URI<a name="en-us_topic_0057972668_section38520254"></a>

DELETE /v2/\{project\_id\}/os-security-group-rules/\{security\_group\_rule\_id\}

DELETE /v2.1/\{project\_id\}/os-security-group-rules/\{security\_group\_rule\_id\}

[Table 1](#en-us_topic_0057972668_table32475667)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="en-us_topic_0057972668_table32475667"></a>
<table><thead align="left"><tr id="en-us_topic_0057972668_row44937496"><th class="cellrowborder" valign="top" width="22.24%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="21.87%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="55.88999999999999%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972668_row1664874"><td class="cellrowborder" valign="top" width="22.24%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972668_p637140"><a name="en-us_topic_0057972668_p637140"></a><a name="en-us_topic_0057972668_p637140"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="21.87%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972668_p51608407"><a name="en-us_topic_0057972668_p51608407"></a><a name="en-us_topic_0057972668_p51608407"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="55.88999999999999%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0057972668_row2766143413265"><td class="cellrowborder" valign="top" width="22.24%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972668_p1376603482617"><a name="en-us_topic_0057972668_p1376603482617"></a><a name="en-us_topic_0057972668_p1376603482617"></a>security_group_rule_id</p>
</td>
<td class="cellrowborder" valign="top" width="21.87%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972668_p14766134142620"><a name="en-us_topic_0057972668_p14766134142620"></a><a name="en-us_topic_0057972668_p14766134142620"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="55.88999999999999%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972668_p6766183419266"><a name="en-us_topic_0057972668_p6766183419266"></a><a name="en-us_topic_0057972668_p6766183419266"></a>Specifies the security group rule ID, which is specified in the URI.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0057972668_section33132859"></a>

None

## Response<a name="en-us_topic_0057972668_section29760277"></a>

None

## Example Request<a name="en-us_topic_0057972668_section66515904"></a>

Example request

```
DELETE https://{endpoint}/v2/3d72597871904daeb6887f75f848b531/os-security-group-rules/012fa2c6-bf4a-4b0b-b893-70d0caee81c7
DELETE https://{endpoint}/v2.1/3d72597871904daeb6887f75f848b531/os-security-group-rules/012fa2c6-bf4a-4b0b-b893-70d0caee81c7
```

## Example Response<a name="section18972624172910"></a>

None

## Returned Values<a name="en-us_topic_0092803065_en-us_topic_0020212692_section22960139"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).


# Deleting a Security Group \(Discarded\)<a name="EN-US_TOPIC_0065817701"></a>

## Function<a name="en-us_topic_0057972665_section12350826"></a>

This API is used to delete a security group.

## Constraints<a name="en-us_topic_0057972665_section60892825"></a>

This API will be discarded. 

You are advised to use the desired network API. For details, see "Security Group \(Native OpenStack API\) \> Deleting a Security Group" in  _Virtual Private Network API Reference_.

## URI<a name="en-us_topic_0057972665_section44048571"></a>

DELETE /v2/\{project\_id\}/os-security-groups/\{security\_group\_id\}

DELETE /v2.1/\{project\_id\}/os-security-groups/\{security\_group\_id\}

[Table 1](#en-us_topic_0057972665_table55945983)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="en-us_topic_0057972665_table55945983"></a>
<table><thead align="left"><tr id="en-us_topic_0057972665_row11302482"><th class="cellrowborder" valign="top" width="33%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="48%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972665_row49888896"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972665_p14468758"><a name="en-us_topic_0057972665_p14468758"></a><a name="en-us_topic_0057972665_p14468758"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972665_p31118786"><a name="en-us_topic_0057972665_p31118786"></a><a name="en-us_topic_0057972665_p31118786"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0057972665_row3928161611210"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972665_p4928516101217"><a name="en-us_topic_0057972665_p4928516101217"></a><a name="en-us_topic_0057972665_p4928516101217"></a>security_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972665_p18928816181213"><a name="en-us_topic_0057972665_p18928816181213"></a><a name="en-us_topic_0057972665_p18928816181213"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972665_p292821613128"><a name="en-us_topic_0057972665_p292821613128"></a><a name="en-us_topic_0057972665_p292821613128"></a>Specifies the security group ID, which is specified in the URI.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0057972665_section11164516"></a>

None

## Response<a name="en-us_topic_0057972665_section33371781"></a>

None

## Example Request<a name="en-us_topic_0057972665_section31910573"></a>

```
DELETE https://{endpoint}/v2/bb1118612ba64af3a6ea63a1bdcaa5ae/os-security-groups/81f1d23b-b1e2-42cd-bdee-359b4a065a42
DELETE https://{endpoint}/v2.1/bb1118612ba64af3a6ea63a1bdcaa5ae/os-security-groups/81f1d23b-b1e2-42cd-bdee-359b4a065a42
```

## Example Response<a name="section22381919112818"></a>

None

## Returned Values<a name="en-us_topic_0092803065_en-us_topic_0020212692_section22960139"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).


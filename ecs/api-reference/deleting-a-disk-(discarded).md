# Deleting a Disk \(Discarded\)<a name="EN-US_TOPIC_0065817712"></a>

## Function<a name="en-us_topic_0057973213_section7187883"></a>

This API is used to delete a specified disk.

## Constraints<a name="en-us_topic_0057973213_section45347628"></a>

-   If the volume has a snapshot not deleted, the volume cannot be deleted.
-   A volume that is being attached to an ECS cannot be deleted.
-   A volume that is being migrated cannot be deleted.
-   Only a volume in the available, error, error\_restoring, or error\_extending state can be deleted.
-   This API will be discarded. You are advised to use the EVS API "Deleting an EVS Disk \(Native OpenStack API V2\)".

## URI<a name="en-us_topic_0057973213_section64690948"></a>

DELETE /v2/\{project\_id\}/os-volumes/\{volume\_id\}

DELETE /v2.1/\{project\_id\}/os-volumes/\{volume\_id\}

[Table 1](#en-us_topic_0057973213_table2814978410562)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="en-us_topic_0057973213_table2814978410562"></a>
<table><thead align="left"><tr id="en-us_topic_0057973213_row4149654710562"><th class="cellrowborder" valign="top" width="33%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="44%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973213_row3491217610562"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973213_p931403110562"><a name="en-us_topic_0057973213_p931403110562"></a><a name="en-us_topic_0057973213_p931403110562"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973213_p1623904210562"><a name="en-us_topic_0057973213_p1623904210562"></a><a name="en-us_topic_0057973213_p1623904210562"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0057973213_row168831648104912"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973213_p588311484495"><a name="en-us_topic_0057973213_p588311484495"></a><a name="en-us_topic_0057973213_p588311484495"></a>volume_id</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973213_p5883148154912"><a name="en-us_topic_0057973213_p5883148154912"></a><a name="en-us_topic_0057973213_p5883148154912"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973213_p788310481495"><a name="en-us_topic_0057973213_p788310481495"></a><a name="en-us_topic_0057973213_p788310481495"></a>Specifies the volume ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0057973213_section49279283"></a>

None

## Response<a name="en-us_topic_0057973213_section40860363"></a>

None

## Example Request<a name="en-us_topic_0057973213_section32198949"></a>

```
DELETE https://{endpoint}/v2/b84c367e4d1047fc9b54f28b400ddbc2/os-volumes/0cf90bab-c513-46df-8559-45ba6de80e3f
DELETE https://{endpoint}/v2.1/b84c367e4d1047fc9b54f28b400ddbc2/os-volumes/0cf90bab-c513-46df-8559-45ba6de80e3f
```

## Example Response<a name="section872686204113"></a>

None

## Returned Values<a name="en-us_topic_0057973213_en-us_topic_0020212692_section22960139"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).


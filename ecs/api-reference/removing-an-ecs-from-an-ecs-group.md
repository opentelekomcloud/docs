# Removing an ECS from an ECS Group<a name="EN-US_TOPIC_0133622596"></a>

## Function<a name="en-us_topic_0057973153_section31887518"></a>

This API is used to remove an ECS from an ECS group. After being removed, the anti-affinity policy will not take effect on this ECS and other ECSs in the same ECS group.

## Constraints<a name="en-us_topic_0057973153_section32752180"></a>

Only the anti-affinity policy is supported. ECSs in the same ECS group are deployed on different hosts, improving service reliability.

## URI<a name="en-us_topic_0057973153_section18552212"></a>

POST /v1/\{project\_id\}/cloudservers/os-server-groups/\{server\_group\_id\}/action

[Table 1](#en-us_topic_0057973153_en-us_topic_0020212650_table62669527)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="en-us_topic_0057973153_en-us_topic_0020212650_table62669527"></a>
<table><thead align="left"><tr id="en-us_topic_0057973153_en-us_topic_0020212650_row33894570"><th class="cellrowborder" valign="top" width="21.68%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18.11%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="60.209999999999994%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973153_en-us_topic_0020212650_row8419032"><td class="cellrowborder" valign="top" width="21.68%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973153_en-us_topic_0020212650_p10852974"><a name="en-us_topic_0057973153_en-us_topic_0020212650_p10852974"></a><a name="en-us_topic_0057973153_en-us_topic_0020212650_p10852974"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="18.11%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973153_en-us_topic_0020212650_p6675738"><a name="en-us_topic_0057973153_en-us_topic_0020212650_p6675738"></a><a name="en-us_topic_0057973153_en-us_topic_0020212650_p6675738"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="60.209999999999994%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row1846155341715"><td class="cellrowborder" valign="top" width="21.68%" headers="mcps1.2.4.1.1 "><p id="p395193810164"><a name="p395193810164"></a><a name="p395193810164"></a>server_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="18.11%" headers="mcps1.2.4.1.2 "><p id="p295173881617"><a name="p295173881617"></a><a name="p295173881617"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="60.209999999999994%" headers="mcps1.2.4.1.3 "><p id="p1359265791616"><a name="p1359265791616"></a><a name="p1359265791616"></a>Specifies the ECS group ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0057973153_section35680930"></a>

[Table 2](#en-us_topic_0057973153_table57386915)  describes the request parameters.

**Table  2**  Request parameters

<a name="en-us_topic_0057973153_table57386915"></a>
<table><thead align="left"><tr id="en-us_topic_0057973153_row22108653"><th class="cellrowborder" valign="top" width="22.08%" id="mcps1.2.5.1.1"><p id="en-us_topic_0057972670_p57733603"><a name="en-us_topic_0057972670_p57733603"></a><a name="en-us_topic_0057972670_p57733603"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.78%" id="mcps1.2.5.1.2"><p id="p4341205425815"><a name="p4341205425815"></a><a name="p4341205425815"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.499999999999998%" id="mcps1.2.5.1.3"><p id="en-us_topic_0057972670_p45910260"><a name="en-us_topic_0057972670_p45910260"></a><a name="en-us_topic_0057972670_p45910260"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="45.64%" id="mcps1.2.5.1.4"><p id="en-us_topic_0057972670_p32634650"><a name="en-us_topic_0057972670_p32634650"></a><a name="en-us_topic_0057972670_p32634650"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973153_row62192793"><td class="cellrowborder" valign="top" width="22.08%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973153_p4451468"><a name="en-us_topic_0057973153_p4451468"></a><a name="en-us_topic_0057973153_p4451468"></a>remove_member</p>
</td>
<td class="cellrowborder" valign="top" width="17.78%" headers="mcps1.2.5.1.2 "><p id="p9341195425812"><a name="p9341195425812"></a><a name="p9341195425812"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.499999999999998%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973153_p25024636"><a name="en-us_topic_0057973153_p25024636"></a><a name="en-us_topic_0057973153_p25024636"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="45.64%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973153_p38357105"><a name="en-us_topic_0057973153_p38357105"></a><a name="en-us_topic_0057973153_p38357105"></a>Specifies the information of the ECS to be removed from an ECS group.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **remove\_member**  parameters

<a name="en-us_topic_0057973153_table19917766"></a>
<table><thead align="left"><tr id="en-us_topic_0057973153_row59878934"><th class="cellrowborder" valign="top" width="22.05%" id="mcps1.2.5.1.1"><p id="p6386132442710"><a name="p6386132442710"></a><a name="p6386132442710"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.76%" id="mcps1.2.5.1.2"><p id="p218115579587"><a name="p218115579587"></a><a name="p218115579587"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.469999999999999%" id="mcps1.2.5.1.3"><p id="p1538611244276"><a name="p1538611244276"></a><a name="p1538611244276"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="45.72%" id="mcps1.2.5.1.4"><p id="p4386624112714"><a name="p4386624112714"></a><a name="p4386624112714"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973153_row28765213"><td class="cellrowborder" valign="top" width="22.05%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973153_p48280896"><a name="en-us_topic_0057973153_p48280896"></a><a name="en-us_topic_0057973153_p48280896"></a>instance_uuid</p>
</td>
<td class="cellrowborder" valign="top" width="17.76%" headers="mcps1.2.5.1.2 "><p id="p12181105716582"><a name="p12181105716582"></a><a name="p12181105716582"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.469999999999999%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973153_p18438475"><a name="en-us_topic_0057973153_p18438475"></a><a name="en-us_topic_0057973153_p18438475"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="45.72%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973153_p44665147"><a name="en-us_topic_0057973153_p44665147"></a><a name="en-us_topic_0057973153_p44665147"></a>Specifies the ECS UUID.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="en-us_topic_0057973153_section52692922"></a>

None

## Example Request<a name="section103189101715"></a>

```
POST https://{endpoint}/v1/{project_id}/cloudservers/os-server-groups/{server_group_id}/action
```

```
{
    "remove_member": {
        "instance_uuid": "34dac9a0-c4a7-457b-bab2-e2c696e0e401"
    }
}
```

## Example Response<a name="section1191916018351"></a>

Status code 200, indicating that the operation is successful

## Returned Values<a name="en-us_topic_0057973153_section17661930132114"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

## Error Codes<a name="section85821649202813"></a>

See  [Error Code Description](error-code-description.md).


# Adding an ECS to an ECS Group<a name="EN-US_TOPIC_0133622595"></a>

## Function<a name="en-us_topic_0057973153_section31887518"></a>

This API is used to add an ECS to an ECS group. The system automatically deploys the newly added ECS to a host that is different from the ones accommodating other ECSs in the ECS group.

## Constraints<a name="en-us_topic_0057973153_section32752180"></a>

-   The ECS to be added has been stopped.
-   Only KVM ECSs can be added.
-   Only the anti-affinity policy is supported. ECSs in the same ECS group are deployed on different hosts, improving service reliability.

## URI<a name="en-us_topic_0057973153_section18552212"></a>

POST /v1/\{project\_id\}/cloudservers/os-server-groups/\{server\_group\_id\}/action

[Table 1](#en-us_topic_0057973153_en-us_topic_0020212650_table62669527)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="en-us_topic_0057973153_en-us_topic_0020212650_table62669527"></a>
<table><thead align="left"><tr id="en-us_topic_0057973153_en-us_topic_0020212650_row33894570"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="56.99999999999999%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973153_en-us_topic_0020212650_row8419032"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973153_en-us_topic_0020212650_p10852974"><a name="en-us_topic_0057973153_en-us_topic_0020212650_p10852974"></a><a name="en-us_topic_0057973153_en-us_topic_0020212650_p10852974"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973153_en-us_topic_0020212650_p6675738"><a name="en-us_topic_0057973153_en-us_topic_0020212650_p6675738"></a><a name="en-us_topic_0057973153_en-us_topic_0020212650_p6675738"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row11101438101610"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.4.1.1 "><p id="p395193810164"><a name="p395193810164"></a><a name="p395193810164"></a>server_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.2 "><p id="p295173881617"><a name="p295173881617"></a><a name="p295173881617"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.2.4.1.3 "><p id="p1359265791616"><a name="p1359265791616"></a><a name="p1359265791616"></a>Specifies the ECS group ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0057973153_section35680930"></a>

[Table 2](#en-us_topic_0057973153_table57386915)  describes the request parameters.

**Table  2**  Request parameters

<a name="en-us_topic_0057973153_table57386915"></a>
<table><thead align="left"><tr id="en-us_topic_0057973153_row22108653"><th class="cellrowborder" valign="top" width="19.69196919691969%" id="mcps1.2.5.1.1"><p id="en-us_topic_0057972670_p57733603"><a name="en-us_topic_0057972670_p57733603"></a><a name="en-us_topic_0057972670_p57733603"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.6017601760176%" id="mcps1.2.5.1.2"><p id="p3283105915575"><a name="p3283105915575"></a><a name="p3283105915575"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="13.91139113911391%" id="mcps1.2.5.1.3"><p id="en-us_topic_0057972670_p45910260"><a name="en-us_topic_0057972670_p45910260"></a><a name="en-us_topic_0057972670_p45910260"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48.7948794879488%" id="mcps1.2.5.1.4"><p id="en-us_topic_0057972670_p32634650"><a name="en-us_topic_0057972670_p32634650"></a><a name="en-us_topic_0057972670_p32634650"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973153_row62192793"><td class="cellrowborder" valign="top" width="19.69196919691969%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973153_p4451468"><a name="en-us_topic_0057973153_p4451468"></a><a name="en-us_topic_0057973153_p4451468"></a>add_member</p>
</td>
<td class="cellrowborder" valign="top" width="17.6017601760176%" headers="mcps1.2.5.1.2 "><p id="p7283115945710"><a name="p7283115945710"></a><a name="p7283115945710"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.91139113911391%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973153_p25024636"><a name="en-us_topic_0057973153_p25024636"></a><a name="en-us_topic_0057973153_p25024636"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="48.7948794879488%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973153_p38357105"><a name="en-us_topic_0057973153_p38357105"></a><a name="en-us_topic_0057973153_p38357105"></a>Specifies the information of the ECS to be added to an ECS group.</p>
<p id="p19951193916339"><a name="p19951193916339"></a><a name="p19951193916339"></a>For details, see <a href="#en-us_topic_0057973153_table19917766">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **add\_member**  parameters

<a name="en-us_topic_0057973153_table19917766"></a>
<table><thead align="left"><tr id="en-us_topic_0057973153_row59878934"><th class="cellrowborder" valign="top" width="19.671967196719674%" id="mcps1.2.5.1.1"><p id="p19749611152719"><a name="p19749611152719"></a><a name="p19749611152719"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.561756175617564%" id="mcps1.2.5.1.2"><p id="p17610130105811"><a name="p17610130105811"></a><a name="p17610130105811"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.001400140014002%" id="mcps1.2.5.1.3"><p id="p117492114275"><a name="p117492114275"></a><a name="p117492114275"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48.76487648764876%" id="mcps1.2.5.1.4"><p id="p7766201113278"><a name="p7766201113278"></a><a name="p7766201113278"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973153_row28765213"><td class="cellrowborder" valign="top" width="19.671967196719674%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973153_p48280896"><a name="en-us_topic_0057973153_p48280896"></a><a name="en-us_topic_0057973153_p48280896"></a>instance_uuid</p>
</td>
<td class="cellrowborder" valign="top" width="17.561756175617564%" headers="mcps1.2.5.1.2 "><p id="p461040125814"><a name="p461040125814"></a><a name="p461040125814"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.001400140014002%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973153_p18438475"><a name="en-us_topic_0057973153_p18438475"></a><a name="en-us_topic_0057973153_p18438475"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.76487648764876%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973153_p44665147"><a name="en-us_topic_0057973153_p44665147"></a><a name="en-us_topic_0057973153_p44665147"></a>Specifies the ECS UUID.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section1927776"></a>

None

## Example Request<a name="en-us_topic_0057973153_section4474257"></a>

```
POST https://{endpoint}/v1/{project_id}/cloudservers/os-server-groups/{server_group_id}/action
```

```
{
    "add_member": {
        "instance_uuid":"34dac9a0-c4a7-457b-bab2-e2c696e0e401"
    }
}
```

## Example Response<a name="section1961482663317"></a>

Status code 200, indicating that the operation is successful

## Returned Values<a name="en-us_topic_0057973153_section17661930132114"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

## Error Codes<a name="section85821649202813"></a>

See  [Error Code Description](error-code-description.md).


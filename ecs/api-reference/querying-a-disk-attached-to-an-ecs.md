# Querying a Disk Attached to an ECS<a name="EN-US_TOPIC_0020212672"></a>

## Function<a name="section21764736"></a>

This API is used to query a single disk attached to an ECS based on the disk ID.

## URI<a name="section61664903"></a>

GET /v2/\{project\_id\}/servers/\{server\_id\}/os-volume\_attachments/\{volume\_id\}

GET /v2.1/\{project\_id\}/servers/\{server\_id\}/os-volume\_attachments/\{volume\_id\}

[Table 1](#table61787501)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table61787501"></a>
<table><thead align="left"><tr id="row44555055"><th class="cellrowborder" valign="top" width="16.98%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.16%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.86%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row9860484"><td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.1 "><p id="p3763337517142"><a name="p3763337517142"></a><a name="p3763337517142"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.16%" headers="mcps1.2.4.1.2 "><p id="p2840453517142"><a name="p2840453517142"></a><a name="p2840453517142"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.86%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row94772224570"><td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.1 "><p id="p42688329"><a name="p42688329"></a><a name="p42688329"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.16%" headers="mcps1.2.4.1.2 "><p id="p35202648"><a name="p35202648"></a><a name="p35202648"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.86%" headers="mcps1.2.4.1.3 "><p id="p32842235"><a name="p32842235"></a><a name="p32842235"></a>Specifies the ECS ID.</p>
</td>
</tr>
<tr id="row976327317144"><td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.1 "><p id="p2068039117144"><a name="p2068039117144"></a><a name="p2068039117144"></a>volume_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.16%" headers="mcps1.2.4.1.2 "><p id="p6449900717144"><a name="p6449900717144"></a><a name="p6449900717144"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.86%" headers="mcps1.2.4.1.3 "><p id="p5703706317144"><a name="p5703706317144"></a><a name="p5703706317144"></a>Specifies the disk ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section18113219"></a>

None

## Response<a name="section28801245"></a>

[Table 2](#table769899)  describes the response parameters.

**Table  2**  Response parameters

<a name="table769899"></a>
<table><thead align="left"><tr id="row6968742"><th class="cellrowborder" valign="top" width="16.98%" id="mcps1.2.4.1.1"><p id="p62404314"><a name="p62404314"></a><a name="p62404314"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.169999999999998%" id="mcps1.2.4.1.2"><p id="p3528183"><a name="p3528183"></a><a name="p3528183"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="65.85%" id="mcps1.2.4.1.3"><p id="p17347392"><a name="p17347392"></a><a name="p17347392"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row13299239"><td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.1 "><p id="p3496541"><a name="p3496541"></a><a name="p3496541"></a>volumeAttachment</p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p56686067"><a name="p56686067"></a><a name="p56686067"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="65.85%" headers="mcps1.2.4.1.3 "><p id="p52192065"><a name="p52192065"></a><a name="p52192065"></a>Specifies the disks attached to an ECS. For details, see <a href="#table42716605">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **volumeAttachment**  field description

<a name="table42716605"></a>
<table><thead align="left"><tr id="row6429"><th class="cellrowborder" valign="top" width="18.86%" id="mcps1.2.4.1.1"><p id="p5194174482"><a name="p5194174482"></a><a name="p5194174482"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13.969999999999999%" id="mcps1.2.4.1.2"><p id="p1119131710483"><a name="p1119131710483"></a><a name="p1119131710483"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="67.17%" id="mcps1.2.4.1.3"><p id="p101931717485"><a name="p101931717485"></a><a name="p101931717485"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row54793251"><td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.2.4.1.1 "><p id="p9068361"><a name="p9068361"></a><a name="p9068361"></a>device</p>
</td>
<td class="cellrowborder" valign="top" width="13.969999999999999%" headers="mcps1.2.4.1.2 "><p id="p39066822"><a name="p39066822"></a><a name="p39066822"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67.17%" headers="mcps1.2.4.1.3 "><p id="p25555552"><a name="p25555552"></a><a name="p25555552"></a>Specifies the attached directory.</p>
</td>
</tr>
<tr id="row28673382"><td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.2.4.1.1 "><p id="p40842582"><a name="p40842582"></a><a name="p40842582"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="13.969999999999999%" headers="mcps1.2.4.1.2 "><p id="p2490560"><a name="p2490560"></a><a name="p2490560"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67.17%" headers="mcps1.2.4.1.3 "><p id="p3679585"><a name="p3679585"></a><a name="p3679585"></a>Specifies the ID of the attached resource.</p>
</td>
</tr>
<tr id="row33116269"><td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.2.4.1.1 "><p id="p65172112"><a name="p65172112"></a><a name="p65172112"></a>serverId</p>
</td>
<td class="cellrowborder" valign="top" width="13.969999999999999%" headers="mcps1.2.4.1.2 "><p id="p43655223"><a name="p43655223"></a><a name="p43655223"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67.17%" headers="mcps1.2.4.1.3 "><p id="p15056362"><a name="p15056362"></a><a name="p15056362"></a>Specifies the ECS ID.</p>
</td>
</tr>
<tr id="row1289536"><td class="cellrowborder" valign="top" width="18.86%" headers="mcps1.2.4.1.1 "><p id="p37343614"><a name="p37343614"></a><a name="p37343614"></a>volumeId</p>
</td>
<td class="cellrowborder" valign="top" width="13.969999999999999%" headers="mcps1.2.4.1.2 "><p id="p64098994"><a name="p64098994"></a><a name="p64098994"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67.17%" headers="mcps1.2.4.1.3 "><p id="p20397636"><a name="p20397636"></a><a name="p20397636"></a>Specifies the ID of the attached disk.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="section165814342372"></a>

```
GET https://{endpoint}/v2/{project_id}/servers/{server_id}/os-volume_attachments/{volume_id}
GET https://{endpoint}/v2.1/{project_id}/servers/{server_id}/os-volume_attachments/{volume_id}
```

## Example Response<a name="section1278119174536"></a>

```
{
    "volumeAttachment": 
        {
            "device": "/dev/sdd",
            "id": "a26887c6-c47b-4654-abb5-dfadf7d3f803",
            "serverId": "4d8c3732-a248-40ed-bebc-539a6ffd25c0",
            "volumeId": "a26887c6-c47b-4654-abb5-dfadf7d3f803"
        }
 }
```

## Returned Values<a name="section57884614"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).


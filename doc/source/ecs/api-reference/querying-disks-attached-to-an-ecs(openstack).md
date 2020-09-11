# Querying Disks Attached to an ECS<a name="EN-US_TOPIC_0020212671"></a>

## Function<a name="section61843920"></a>

This API is used to query the disks attached to an ECS.

## URI<a name="section19724370"></a>

GET /v2/\{project\_id\}/servers/\{server\_id\}/os-volume\_attachments

GET /v2.1/\{project\_id\}/servers/\{server\_id\}/os-volume\_attachments

[Table 1](#table35893824)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table35893824"></a>
<table><thead align="left"><tr id="row23656219"><th class="cellrowborder" valign="top" width="16.98%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.169999999999998%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.85%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row23086940"><td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.1 "><p id="p58102813"><a name="p58102813"></a><a name="p58102813"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p8707407"><a name="p8707407"></a><a name="p8707407"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.85%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row39466727"><td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.1 "><p id="p42688329"><a name="p42688329"></a><a name="p42688329"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p35202648"><a name="p35202648"></a><a name="p35202648"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.85%" headers="mcps1.2.4.1.3 "><p id="p32842235"><a name="p32842235"></a><a name="p32842235"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section43301605"></a>

None

## Response<a name="section54170131"></a>

**Response parameters**

[Table 2](#table57959838)  describes the response parameters.

**Table  2**  Response parameters

<a name="table57959838"></a>
<table><thead align="left"><tr id="row39710134"><th class="cellrowborder" valign="top" width="16.86%" id="mcps1.2.4.1.1"><p id="p62404314"><a name="p62404314"></a><a name="p62404314"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.419999999999998%" id="mcps1.2.4.1.2"><p id="p3528183"><a name="p3528183"></a><a name="p3528183"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="65.72%" id="mcps1.2.4.1.3"><p id="p17347392"><a name="p17347392"></a><a name="p17347392"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row62961510"><td class="cellrowborder" valign="top" width="16.86%" headers="mcps1.2.4.1.1 "><p id="p66717520"><a name="p66717520"></a><a name="p66717520"></a>volumeAttachments</p>
</td>
<td class="cellrowborder" valign="top" width="17.419999999999998%" headers="mcps1.2.4.1.2 "><p id="p49639570"><a name="p49639570"></a><a name="p49639570"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="65.72%" headers="mcps1.2.4.1.3 "><p id="p15568903"><a name="p15568903"></a><a name="p15568903"></a>Specifies the disks attached to an ECS. For details, see <a href="#table7886611">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **volumeAttachments**  field description

<a name="table7886611"></a>
<table><thead align="left"><tr id="row60727582"><th class="cellrowborder" valign="top" width="16.35%" id="mcps1.2.4.1.1"><p id="p01561150124719"><a name="p01561150124719"></a><a name="p01561150124719"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.099999999999998%" id="mcps1.2.4.1.2"><p id="p21565508475"><a name="p21565508475"></a><a name="p21565508475"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="69.55%" id="mcps1.2.4.1.3"><p id="p111561350154718"><a name="p111561350154718"></a><a name="p111561350154718"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row34544438"><td class="cellrowborder" valign="top" width="16.35%" headers="mcps1.2.4.1.1 "><p id="p46636132"><a name="p46636132"></a><a name="p46636132"></a>device</p>
</td>
<td class="cellrowborder" valign="top" width="14.099999999999998%" headers="mcps1.2.4.1.2 "><p id="p30355189"><a name="p30355189"></a><a name="p30355189"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="69.55%" headers="mcps1.2.4.1.3 "><p id="p50116845"><a name="p50116845"></a><a name="p50116845"></a>Specifies the attached directory.</p>
</td>
</tr>
<tr id="row48398424"><td class="cellrowborder" valign="top" width="16.35%" headers="mcps1.2.4.1.1 "><p id="p27958252"><a name="p27958252"></a><a name="p27958252"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="14.099999999999998%" headers="mcps1.2.4.1.2 "><p id="p25568738"><a name="p25568738"></a><a name="p25568738"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="69.55%" headers="mcps1.2.4.1.3 "><p id="p50454834"><a name="p50454834"></a><a name="p50454834"></a>Specifies the ID of the attached resource.</p>
</td>
</tr>
<tr id="row51440330"><td class="cellrowborder" valign="top" width="16.35%" headers="mcps1.2.4.1.1 "><p id="p5917164"><a name="p5917164"></a><a name="p5917164"></a>serverId</p>
</td>
<td class="cellrowborder" valign="top" width="14.099999999999998%" headers="mcps1.2.4.1.2 "><p id="p33594135"><a name="p33594135"></a><a name="p33594135"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="69.55%" headers="mcps1.2.4.1.3 "><p id="p62498284"><a name="p62498284"></a><a name="p62498284"></a>Specifies the ECS ID.</p>
</td>
</tr>
<tr id="row25613652"><td class="cellrowborder" valign="top" width="16.35%" headers="mcps1.2.4.1.1 "><p id="p61439917"><a name="p61439917"></a><a name="p61439917"></a>volumeId</p>
</td>
<td class="cellrowborder" valign="top" width="14.099999999999998%" headers="mcps1.2.4.1.2 "><p id="p51461341"><a name="p51461341"></a><a name="p51461341"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="69.55%" headers="mcps1.2.4.1.3 "><p id="p1462819"><a name="p1462819"></a><a name="p1462819"></a>Specifies the ID of the attached disk.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="section763514718378"></a>

```
GET https://{endpoint}/v2/{project_id}/servers/{server_id}/os-volume_attachments
GET https://{endpoint}/v2.1/{project_id}/servers/{server_id}/os-volume_attachments
```

## Example Response<a name="section1013118563474"></a>

```
{
    "volumeAttachments": [
        {
            "device": "/dev/sdd",
            "id": "a26887c6-c47b-4654-abb5-dfadf7d3f803",
            "serverId": "4d8c3732-a248-40ed-bebc-539a6ffd25c0",
            "volumeId": "a26887c6-c47b-4654-abb5-dfadf7d3f803"
        },
        {
            "device": "/dev/sdc",
            "id": "a26887c6-c47b-4654-abb5-dfadf7d3f804",
            "serverId": "4d8c3732-a248-40ed-bebc-539a6ffd25c0",
            "volumeId": "a26887c6-c47b-4654-abb5-dfadf7d3f804"
        }
    ]
}
```

## Returned Values<a name="section17769131"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).


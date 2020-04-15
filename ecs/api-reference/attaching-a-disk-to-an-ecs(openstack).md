# Attaching a Disk to an ECS<a name="EN-US_TOPIC_0031167350"></a>

## Function<a name="section53922917165259"></a>

This API is used to attach a disk to an ECS.

## Constraints<a name="section64211377173223"></a>

1.  If you attach a bootable disk to an ECS, you must specify the disk drive letter.
2.  A disk created using a backup cannot be attached to an ECS as the system disk.
3.  An ECS in the SUSPENDED or PAUSED state, which is specified using the  **OS-EXT-STS:vm\_state**  parameter of the ECS, cannot have a disk attached.
4.  The EVS must be in the  **available**  status.
5.  The EVS disk and the target ECS must be located in the same AZ.
6.  VBD EVS disks cannot be attached to BMSs.

## URI<a name="section51121191165259"></a>

POST /v2/\{project\_id\}/servers/\{server\_id\}/os-volume\_attachments

POST /v2.1/\{project\_id\}/servers/\{server\_id\}/os-volume\_attachments

[Table 1](#table60562285165259)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table60562285165259"></a>
<table><thead align="left"><tr id="row4861884165259"><th class="cellrowborder" valign="top" width="16.98%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.549999999999997%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.47%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row63809876165259"><td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.1 "><p id="p1217433165259"><a name="p1217433165259"></a><a name="p1217433165259"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.549999999999997%" headers="mcps1.2.4.1.2 "><p id="p31503226165259"><a name="p31503226165259"></a><a name="p31503226165259"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.47%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row59999756151519"><td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.1 "><p id="p28142050151519"><a name="p28142050151519"></a><a name="p28142050151519"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.549999999999997%" headers="mcps1.2.4.1.2 "><p id="p64913614151519"><a name="p64913614151519"></a><a name="p64913614151519"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.47%" headers="mcps1.2.4.1.3 "><p id="p23511349151519"><a name="p23511349151519"></a><a name="p23511349151519"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section8194118165259"></a>

[Table 2](#table38613152151549)  describes the request parameters.

**Table  2**  Request parameters

<a name="table38613152151549"></a>
<table><thead align="left"><tr id="row40874938151549"><th class="cellrowborder" valign="top" width="16.831683168316832%" id="mcps1.2.5.1.1"><p id="p22535719151549"><a name="p22535719151549"></a><a name="p22535719151549"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.88178817881788%" id="mcps1.2.5.1.2"><p id="p35271647131"><a name="p35271647131"></a><a name="p35271647131"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.441444144414442%" id="mcps1.2.5.1.3"><p id="p13453940151549"><a name="p13453940151549"></a><a name="p13453940151549"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50.845084508450846%" id="mcps1.2.5.1.4"><p id="p23145935151549"><a name="p23145935151549"></a><a name="p23145935151549"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row62881453151549"><td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.1 "><p id="p60232972151549"><a name="p60232972151549"></a><a name="p60232972151549"></a>volumeAttachment</p>
</td>
<td class="cellrowborder" valign="top" width="17.88178817881788%" headers="mcps1.2.5.1.2 "><p id="p1652794161320"><a name="p1652794161320"></a><a name="p1652794161320"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.441444144414442%" headers="mcps1.2.5.1.3 "><p id="p47032596151549"><a name="p47032596151549"></a><a name="p47032596151549"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="50.845084508450846%" headers="mcps1.2.5.1.4 "><p id="p14307644151549"><a name="p14307644151549"></a><a name="p14307644151549"></a>Specifies the volumes to be attached. For details, see <a href="#table40707503151632">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **volumeAttachment**  field description

<a name="table40707503151632"></a>
<table><thead align="left"><tr id="row46910609151632"><th class="cellrowborder" valign="top" width="17.89%" id="mcps1.2.5.1.1"><p id="p9688145419315"><a name="p9688145419315"></a><a name="p9688145419315"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.48%" id="mcps1.2.5.1.2"><p id="p118264710132"><a name="p118264710132"></a><a name="p118264710132"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="13.780000000000001%" id="mcps1.2.5.1.3"><p id="p368816541035"><a name="p368816541035"></a><a name="p368816541035"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="50.849999999999994%" id="mcps1.2.5.1.4"><p id="p8703154232"><a name="p8703154232"></a><a name="p8703154232"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row56436699151632"><td class="cellrowborder" valign="top" width="17.89%" headers="mcps1.2.5.1.1 "><p id="p7969910151632"><a name="p7969910151632"></a><a name="p7969910151632"></a>volumeId</p>
</td>
<td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.2.5.1.2 "><p id="p1582647151320"><a name="p1582647151320"></a><a name="p1582647151320"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.780000000000001%" headers="mcps1.2.5.1.3 "><p id="p41582949151632"><a name="p41582949151632"></a><a name="p41582949151632"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.849999999999994%" headers="mcps1.2.5.1.4 "><p id="p28198497151632"><a name="p28198497151632"></a><a name="p28198497151632"></a>Specifies the ID of the disk to be attached. The value is in UUID format.</p>
</td>
</tr>
<tr id="row52459882151632"><td class="cellrowborder" valign="top" width="17.89%" headers="mcps1.2.5.1.1 "><p id="p21392044151632"><a name="p21392044151632"></a><a name="p21392044151632"></a>device</p>
</td>
<td class="cellrowborder" valign="top" width="17.48%" headers="mcps1.2.5.1.2 "><p id="p1827472138"><a name="p1827472138"></a><a name="p1827472138"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="13.780000000000001%" headers="mcps1.2.5.1.3 "><p id="p55033990151632"><a name="p55033990151632"></a><a name="p55033990151632"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="50.849999999999994%" headers="mcps1.2.5.1.4 "><p id="p7777719105553"><a name="p7777719105553"></a><a name="p7777719105553"></a>Specifies the device name, such as <strong id="b84235270611241"><a name="b84235270611241"></a><a name="b84235270611241"></a>/dev/sda</strong> or <strong id="b84235270611248"><a name="b84235270611248"></a><a name="b84235270611248"></a>/dev/sdb</strong>.</p>
<p id="p58233871152743"><a name="p58233871152743"></a><a name="p58233871152743"></a>The new disk device name cannot be the same as an existing one.</p>
<p id="p22488653151632"><a name="p22488653151632"></a><a name="p22488653151632"></a>The device name must be specified based on the sequence of existing device names. Otherwise, the system automatically generates one.</p>
<div class="note" id="note794417411107"><a name="note794417411107"></a><a name="note794417411107"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1694404115106"><a name="p1694404115106"></a><a name="p1694404115106"></a>VBD disk device names can only be <strong id="b842352706172420"><a name="b842352706172420"></a><a name="b842352706172420"></a>/dev/vdb</strong> through <strong id="b842352706172434"><a name="b842352706172434"></a><a name="b842352706172434"></a>/dev/vdx</strong>. You are advised to attach the VBD disks in alphabetical order. Otherwise, the disk drive letters may be incorrect on the ECS.</p>
</div></div>
</td>
</tr>
</tbody>
</table>

## Response<a name="section58140617165259"></a>

[Table 4](#table548498215180)  describes the response parameters.

**Table  4**  Response parameters

<a name="table548498215180"></a>
<table><thead align="left"><tr id="row3759039515180"><th class="cellrowborder" valign="top" width="17.83%" id="mcps1.2.4.1.1"><p id="p62404314"><a name="p62404314"></a><a name="p62404314"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.2.4.1.2"><p id="p3528183"><a name="p3528183"></a><a name="p3528183"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="69.17%" id="mcps1.2.4.1.3"><p id="p17347392"><a name="p17347392"></a><a name="p17347392"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row4742233715180"><td class="cellrowborder" valign="top" width="17.83%" headers="mcps1.2.4.1.1 "><p id="p1600407115180"><a name="p1600407115180"></a><a name="p1600407115180"></a>device</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.4.1.2 "><p id="p2126141115180"><a name="p2126141115180"></a><a name="p2126141115180"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="69.17%" headers="mcps1.2.4.1.3 "><p id="p4389880615180"><a name="p4389880615180"></a><a name="p4389880615180"></a>Specifies the device name.</p>
</td>
</tr>
<tr id="row5954494215180"><td class="cellrowborder" valign="top" width="17.83%" headers="mcps1.2.4.1.1 "><p id="p5841097215180"><a name="p5841097215180"></a><a name="p5841097215180"></a>serverId</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.4.1.2 "><p id="p3366825815180"><a name="p3366825815180"></a><a name="p3366825815180"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="69.17%" headers="mcps1.2.4.1.3 "><p id="p4217250415180"><a name="p4217250415180"></a><a name="p4217250415180"></a>Specifies the ID of the target ECS in UUID format.</p>
</td>
</tr>
<tr id="row4400822315180"><td class="cellrowborder" valign="top" width="17.83%" headers="mcps1.2.4.1.1 "><p id="p789628615180"><a name="p789628615180"></a><a name="p789628615180"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.4.1.2 "><p id="p3561941815180"><a name="p3561941815180"></a><a name="p3561941815180"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="69.17%" headers="mcps1.2.4.1.3 "><p id="p2593706215180"><a name="p2593706215180"></a><a name="p2593706215180"></a>Specifies the disk ID in UUID format.</p>
</td>
</tr>
<tr id="row3210697315180"><td class="cellrowborder" valign="top" width="17.83%" headers="mcps1.2.4.1.1 "><p id="p5052800715180"><a name="p5052800715180"></a><a name="p5052800715180"></a>volumeId</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.4.1.2 "><p id="p6623678615180"><a name="p6623678615180"></a><a name="p6623678615180"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="69.17%" headers="mcps1.2.4.1.3 "><p id="p4966276115180"><a name="p4966276115180"></a><a name="p4966276115180"></a>Specifies the attaching ID, which is the same as the UUID.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="section8675155319416"></a>

```
POST https://{endpoint}/v2/{project_id}/servers/{server_id}/os-volume_attachments
POST https://{endpoint}/v2.1/{project_id}/servers/{server_id}/os-volume_attachments
```

```
{
    "volumeAttachment": {
        "volumeId": "54667652-3029-4af8-9222-2d53066fd61c",
        "device": "/dev/sdb"
    }
}
```

## Example Response<a name="section104992312387"></a>

```
{
    "volumeAttachment": {
        "device": "/dev/vdb",
        "serverId": "ab258e25-e351-47c7-b6e3-0749c5d9ed6a",
        "id": "54667652-3029-4af8-9222-2d53066fd61c",
        "volumeId": "54667652-3029-4af8-9222-2d53066fd61c"
    }
}
```

## Returned Values<a name="section38817202165259"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).


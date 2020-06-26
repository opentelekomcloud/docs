# Attaching a Disk to an ECS<a name="EN-US_TOPIC_0022472987"></a>

## Function<a name="section48627224105553"></a>

This API is used to attach a disk to an ECS.

## URI<a name="section15766276105553"></a>

POST /v1/\{project\_id\}/cloudservers/\{server\_id\}/attachvolume

[Table 1](#table35528365105553)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table35528365105553"></a>
<table><thead align="left"><tr id="row17119455105553"><th class="cellrowborder" valign="top" width="16.42%" id="mcps1.2.4.1.1"><p id="p37105578"><a name="p37105578"></a><a name="p37105578"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.36%" id="mcps1.2.4.1.2"><p id="p52761866"><a name="p52761866"></a><a name="p52761866"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="66.22%" id="mcps1.2.4.1.3"><p id="p45852771"><a name="p45852771"></a><a name="p45852771"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row39853249105553"><td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.1 "><p id="p6887725105553"><a name="p6887725105553"></a><a name="p6887725105553"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.2 "><p id="p21034813105553"><a name="p21034813105553"></a><a name="p21034813105553"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.22%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row670727210579"><td class="cellrowborder" valign="top" width="16.42%" headers="mcps1.2.4.1.1 "><p id="p41505172105731"><a name="p41505172105731"></a><a name="p41505172105731"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.2 "><p id="p6475762105731"><a name="p6475762105731"></a><a name="p6475762105731"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.22%" headers="mcps1.2.4.1.3 "><p id="p54774717105731"><a name="p54774717105731"></a><a name="p54774717105731"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section33557800105553"></a>

**Table  2**  Request parameters

<a name="table55654045105553"></a>
<table><thead align="left"><tr id="row38118604105553"><th class="cellrowborder" valign="top" width="16.368363163683632%" id="mcps1.2.5.1.1"><p id="p599200105553"><a name="p599200105553"></a><a name="p599200105553"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.33826617338266%" id="mcps1.2.5.1.2"><p id="p48535233105553"><a name="p48535233105553"></a><a name="p48535233105553"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="12.75872412758724%" id="mcps1.2.5.1.3"><p id="p39039766105553"><a name="p39039766105553"></a><a name="p39039766105553"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="53.53464653534646%" id="mcps1.2.5.1.4"><p id="p8104455105553"><a name="p8104455105553"></a><a name="p8104455105553"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row650913578526"><td class="cellrowborder" valign="top" width="16.368363163683632%" headers="mcps1.2.5.1.1 "><p id="p351017572527"><a name="p351017572527"></a><a name="p351017572527"></a>volumeAttachment</p>
</td>
<td class="cellrowborder" valign="top" width="17.33826617338266%" headers="mcps1.2.5.1.2 "><p id="p1510125710524"><a name="p1510125710524"></a><a name="p1510125710524"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="12.75872412758724%" headers="mcps1.2.5.1.3 "><p id="p55101657165213"><a name="p55101657165213"></a><a name="p55101657165213"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="53.53464653534646%" headers="mcps1.2.5.1.4 "><p id="p1051017579521"><a name="p1051017579521"></a><a name="p1051017579521"></a>Specifies the disk attached to an ECS.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **volumeAttachment**  field description

<a name="table40707503151632"></a>
<table><thead align="left"><tr id="row46910609151632"><th class="cellrowborder" valign="top" width="17.849999999999998%" id="mcps1.2.5.1.1"><p id="p41663005151632"><a name="p41663005151632"></a><a name="p41663005151632"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.26%" id="mcps1.2.5.1.2"><p id="p1090831092414"><a name="p1090831092414"></a><a name="p1090831092414"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="11.41%" id="mcps1.2.5.1.3"><p id="p19260278151632"><a name="p19260278151632"></a><a name="p19260278151632"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="53.480000000000004%" id="mcps1.2.5.1.4"><p id="p696749151632"><a name="p696749151632"></a><a name="p696749151632"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row56436699151632"><td class="cellrowborder" valign="top" width="17.849999999999998%" headers="mcps1.2.5.1.1 "><p id="p7969910151632"><a name="p7969910151632"></a><a name="p7969910151632"></a>volumeId</p>
</td>
<td class="cellrowborder" valign="top" width="17.26%" headers="mcps1.2.5.1.2 "><p id="p149565197249"><a name="p149565197249"></a><a name="p149565197249"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="11.41%" headers="mcps1.2.5.1.3 "><p id="p9972164210362"><a name="p9972164210362"></a><a name="p9972164210362"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.480000000000004%" headers="mcps1.2.5.1.4 "><p id="p28198497151632"><a name="p28198497151632"></a><a name="p28198497151632"></a>Specifies the ID of the disk to be attached. The value is in UUID format.</p>
</td>
</tr>
<tr id="row52459882151632"><td class="cellrowborder" valign="top" width="17.849999999999998%" headers="mcps1.2.5.1.1 "><p id="p21392044151632"><a name="p21392044151632"></a><a name="p21392044151632"></a>device</p>
</td>
<td class="cellrowborder" valign="top" width="17.26%" headers="mcps1.2.5.1.2 "><p id="p16956171918245"><a name="p16956171918245"></a><a name="p16956171918245"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="11.41%" headers="mcps1.2.5.1.3 "><p id="p55033990151632"><a name="p55033990151632"></a><a name="p55033990151632"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="53.480000000000004%" headers="mcps1.2.5.1.4 "><p id="p179035435915"><a name="p179035435915"></a><a name="p179035435915"></a>Indicates the disk device name.</p>
<div class="note" id="note1755312117111"><a name="note1755312117111"></a><a name="note1755312117111"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul1580711965"></a><a name="ul1580711965"></a><ul id="ul1580711965"><li>The new disk device name cannot be the same as an existing one.</li><li>This parameter is mandatory for Xen ECSs. Set the parameter value to <strong id="b111817136481"><a name="b111817136481"></a><a name="b111817136481"></a>/dev/sda</strong> for the system disks of such ECSs and to <strong id="b141821413134819"><a name="b141821413134819"></a><a name="b141821413134819"></a>/dev/sd</strong><em id="i318312132486"><a name="i318312132486"></a><a name="i318312132486"></a>x</em> for data disks, where <em id="i718411139482"><a name="i718411139482"></a><a name="i718411139482"></a>x</em> is a letter in alphabetical order. For example, if there are two data disks, set the device names of the two data disks to <strong id="b16184613154815"><a name="b16184613154815"></a><a name="b16184613154815"></a>/dev/sdb</strong> and <strong id="b718512134482"><a name="b718512134482"></a><a name="b718512134482"></a>/dev/sdc</strong>, respectively. If you set a device name starting with <strong id="b181862136486"><a name="b181862136486"></a><a name="b181862136486"></a>/dev/vd</strong>, the system uses <strong id="b11187913124814"><a name="b11187913124814"></a><a name="b11187913124814"></a>/dev/sd</strong> by default.</li><li>For KVM ECSs, set the parameter value to <strong id="b1449143511497"><a name="b1449143511497"></a><a name="b1449143511497"></a>/dev/vda</strong> for system disks. The device names for data disks of KVM ECSs are optional. If the device names of data disks are required, set them in alphabetical order. For example, if there are two data disks, set the device names of the two data disks to <strong id="b15013554917"><a name="b15013554917"></a><a name="b15013554917"></a>/dev/vdb</strong> and <strong id="b25173594918"><a name="b25173594918"></a><a name="b25173594918"></a>/dev/vdc</strong>, respectively. If you set a device name starting with <strong id="b15223594918"><a name="b15223594918"></a><a name="b15223594918"></a>/dev/sd</strong>, the system uses <strong id="b1859235144914"><a name="b1859235144914"></a><a name="b1859235144914"></a>/dev/vd</strong> by default.</li></ul>
</div></div>
</td>
</tr>
</tbody>
</table>

## Response<a name="section5883164105553"></a>

See  [Responses \(Task\)](responses-(task).md).

## Example Request<a name="section812710371403"></a>

```
POST https://{endpoint}/v1/{project_id}/cloudservers/{server_id}/attachvolume
```

```
{
    "volumeAttachment": {
         "volumeId": "a26887c6-c47b-4654-abb5-dfadf7d3f803",
         "device": "/dev/sda"
    }
}
```

## Example Response<a name="section7250113841316"></a>

None

## Returned Values<a name="en-us_topic_0092803065_en-us_topic_0020212692_section22960139"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

## Error Codes<a name="en-us_topic_0092803065_en-us_topic_0067161469_en-us_topic_0057973179_section23611955"></a>

See  [Error Code Description](error-code-description.md).


# Querying A Single Disk Attached to an ECS <a name="EN-US_TOPIC_0101860614"></a>

## Function<a name="section61843920"></a>

This API is used to query a single disk attached to an ECS.

## URI<a name="section19724370"></a>

GET /v2.1/servers/\{server\_id\}/block\_device/\{volume\_id\}

[Table 1](#table35893824)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table35893824"></a>
<table><thead align="left"><tr id="row23656219"><th class="cellrowborder" valign="top" width="16.75%" id="mcps1.2.4.1.1"><p id="p37105578"><a name="p37105578"></a><a name="p37105578"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.349999999999998%" id="mcps1.2.4.1.2"><p id="p52761866"><a name="p52761866"></a><a name="p52761866"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.9%" id="mcps1.2.4.1.3"><p id="p45852771"><a name="p45852771"></a><a name="p45852771"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row39466727"><td class="cellrowborder" valign="top" width="16.75%" headers="mcps1.2.4.1.1 "><p id="p42688329"><a name="p42688329"></a><a name="p42688329"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p35202648"><a name="p35202648"></a><a name="p35202648"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.9%" headers="mcps1.2.4.1.3 "><p id="p32842235"><a name="p32842235"></a><a name="p32842235"></a>Specifies the ECS ID in UUID format.</p>
</td>
</tr>
<tr id="row77061621252"><td class="cellrowborder" valign="top" width="16.75%" headers="mcps1.2.4.1.1 "><p id="p11706725259"><a name="p11706725259"></a><a name="p11706725259"></a>volume_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p52640702510"><a name="p52640702510"></a><a name="p52640702510"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.9%" headers="mcps1.2.4.1.3 "><p id="p8265878256"><a name="p8265878256"></a><a name="p8265878256"></a>Specifies the EVS disk ID in UUID format.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section43301605"></a>

None

## Response<a name="section54170131"></a>

[Table 2](#table57959838)  describes the response parameters.

**Table  2**  Response parameters

<a name="table57959838"></a>
<table><thead align="left"><tr id="row39710134"><th class="cellrowborder" valign="top" width="16.698330166983304%" id="mcps1.2.4.1.1"><p id="p62404314"><a name="p62404314"></a><a name="p62404314"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13.508649135086493%" id="mcps1.2.4.1.2"><p id="p3528183"><a name="p3528183"></a><a name="p3528183"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="69.7930206979302%" id="mcps1.2.4.1.3"><p id="p17347392"><a name="p17347392"></a><a name="p17347392"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row62961510"><td class="cellrowborder" valign="top" width="16.698330166983304%" headers="mcps1.2.4.1.1 "><p id="p66717520"><a name="p66717520"></a><a name="p66717520"></a>volumeAttachment</p>
</td>
<td class="cellrowborder" valign="top" width="13.508649135086493%" headers="mcps1.2.4.1.2 "><p id="p49639570"><a name="p49639570"></a><a name="p49639570"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="69.7930206979302%" headers="mcps1.2.4.1.3 "><p id="p15568903"><a name="p15568903"></a><a name="p15568903"></a>Specifies the disk attached to an ECS. For details, see <a href="#table7886611">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **volumeAttachment**  parameters

<a name="table7886611"></a>
<table><thead align="left"><tr id="row60727582"><th class="cellrowborder" valign="top" width="16.650000000000002%" id="mcps1.2.4.1.1"><p id="p1554374912162"><a name="p1554374912162"></a><a name="p1554374912162"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13.58%" id="mcps1.2.4.1.2"><p id="p0543649111613"><a name="p0543649111613"></a><a name="p0543649111613"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="69.77%" id="mcps1.2.4.1.3"><p id="p754384917161"><a name="p754384917161"></a><a name="p754384917161"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row34544438"><td class="cellrowborder" valign="top" width="16.650000000000002%" headers="mcps1.2.4.1.1 "><p id="p46636132"><a name="p46636132"></a><a name="p46636132"></a>serverId</p>
</td>
<td class="cellrowborder" valign="top" width="13.58%" headers="mcps1.2.4.1.2 "><p id="p30355189"><a name="p30355189"></a><a name="p30355189"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="69.77%" headers="mcps1.2.4.1.3 "><p id="p50116845"><a name="p50116845"></a><a name="p50116845"></a>Specifies the ECS ID in UUID format.</p>
</td>
</tr>
<tr id="row48398424"><td class="cellrowborder" valign="top" width="16.650000000000002%" headers="mcps1.2.4.1.1 "><p id="p16791461647"><a name="p16791461647"></a><a name="p16791461647"></a>volumeId</p>
</td>
<td class="cellrowborder" valign="top" width="13.58%" headers="mcps1.2.4.1.2 "><p id="p10861332121715"><a name="p10861332121715"></a><a name="p10861332121715"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="69.77%" headers="mcps1.2.4.1.3 "><p id="p50454834"><a name="p50454834"></a><a name="p50454834"></a>Specifies the EVS disk ID in UUID format.</p>
</td>
</tr>
<tr id="row51440330"><td class="cellrowborder" valign="top" width="16.650000000000002%" headers="mcps1.2.4.1.1 "><p id="p1980225720418"><a name="p1980225720418"></a><a name="p1980225720418"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="13.58%" headers="mcps1.2.4.1.2 "><p id="p1836163411178"><a name="p1836163411178"></a><a name="p1836163411178"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="69.77%" headers="mcps1.2.4.1.3 "><p id="p62498284"><a name="p62498284"></a><a name="p62498284"></a>Specifies the mount ID, which is the same as the EVS disk ID.</p>
<p id="p19668183019510"><a name="p19668183019510"></a><a name="p19668183019510"></a>The value is in UUID format.</p>
</td>
</tr>
<tr id="row9400111250"><td class="cellrowborder" valign="top" width="16.650000000000002%" headers="mcps1.2.4.1.1 "><p id="p44001611759"><a name="p44001611759"></a><a name="p44001611759"></a>size</p>
</td>
<td class="cellrowborder" valign="top" width="13.58%" headers="mcps1.2.4.1.2 "><p id="p1040020111156"><a name="p1040020111156"></a><a name="p1040020111156"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="69.77%" headers="mcps1.2.4.1.3 "><p id="p1440012113518"><a name="p1440012113518"></a><a name="p1440012113518"></a>Specifies the EVS disk size in GB.</p>
</td>
</tr>
<tr id="row25613652"><td class="cellrowborder" valign="top" width="16.650000000000002%" headers="mcps1.2.4.1.1 "><p id="p5917164"><a name="p5917164"></a><a name="p5917164"></a>device</p>
</td>
<td class="cellrowborder" valign="top" width="13.58%" headers="mcps1.2.4.1.2 "><p id="p51461341"><a name="p51461341"></a><a name="p51461341"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="69.77%" headers="mcps1.2.4.1.3 "><p id="p1462819"><a name="p1462819"></a><a name="p1462819"></a>Specifies the drive letter of the EVS disk, which is the device name of the EVS disk.</p>
</td>
</tr>
<tr id="row138081017757"><td class="cellrowborder" valign="top" width="16.650000000000002%" headers="mcps1.2.4.1.1 "><p id="p181061717510"><a name="p181061717510"></a><a name="p181061717510"></a>pciAddress</p>
</td>
<td class="cellrowborder" valign="top" width="13.58%" headers="mcps1.2.4.1.2 "><p id="p128101117559"><a name="p128101117559"></a><a name="p128101117559"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="69.77%" headers="mcps1.2.4.1.3 "><p id="p28102176515"><a name="p28102176515"></a><a name="p28102176515"></a>Specifies the PCI address.</p>
</td>
</tr>
<tr id="row25285127356"><td class="cellrowborder" valign="top" width="16.650000000000002%" headers="mcps1.2.4.1.1 "><p id="p11108124414332"><a name="p11108124414332"></a><a name="p11108124414332"></a>bootIndex</p>
</td>
<td class="cellrowborder" valign="top" width="13.58%" headers="mcps1.2.4.1.2 "><p id="p1410818444336"><a name="p1410818444336"></a><a name="p1410818444336"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="69.77%" headers="mcps1.2.4.1.3 "><p id="p193241929982"><a name="p193241929982"></a><a name="p193241929982"></a>Specifies the EVS disk boot sequence.</p>
<a name="ul12742143715815"></a><a name="ul12742143715815"></a><ul id="ul12742143715815"><li><strong id="b842352706181942"><a name="b842352706181942"></a><a name="b842352706181942"></a>0</strong> indicates the system disk.</li><li>Non-0 indicates a data disk.</li></ul>
</td>
</tr>
<tr id="row1477463153418"><td class="cellrowborder" valign="top" width="16.650000000000002%" headers="mcps1.2.4.1.1 "><p id="p1485515145717"><a name="p1485515145717"></a><a name="p1485515145717"></a>bus</p>
</td>
<td class="cellrowborder" valign="top" width="13.58%" headers="mcps1.2.4.1.2 "><p id="p185525155718"><a name="p185525155718"></a><a name="p185525155718"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="69.77%" headers="mcps1.2.4.1.3 "><p id="p18874019155217"><a name="p18874019155217"></a><a name="p18874019155217"></a>Specifies the disk bus type.</p>
<p id="p1485511511573"><a name="p1485511511573"></a><a name="p1485511511573"></a>Options: <strong id="b842352706114826"><a name="b842352706114826"></a><a name="b842352706114826"></a>virtio</strong> and <strong id="b842352706114831"><a name="b842352706114831"></a><a name="b842352706114831"></a>scsi</strong></p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="section1828405010213"></a>

```
GET https://{endpoint}/v2.1/servers/{server_id}/block_device/{volume_id}
```

## Example Response<a name="section16327154723712"></a>

```
{
    "volumeAttachment": {
        "pciAddress": "0000:02:01.0",
        "volumeId": "a26887c6-c47b-4654-abb5-asdf234r234r",
        "device": "/dev/vda",
        "serverId": "4d8c3732-a248-40ed-bebc-539a6ffd25c0",
        "id": "a26887c6-c47b-4654-abb5-asdf234r234r",
        "size": "40",
        "bootIndex": 0,
        "bus":"virtio"
    }
}
```

## Returned Values<a name="en-us_topic_0092803065_en-us_topic_0020212692_section22960139"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

## Error Codes<a name="en-us_topic_0092803065_en-us_topic_0067161469_en-us_topic_0057973179_section23611955"></a>

See  [Error Code Description](error-code-description.md).


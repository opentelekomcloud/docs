# Creating a Disk \(Discarded\)<a name="EN-US_TOPIC_0065817708"></a>

## Function<a name="en-us_topic_0057973208_section12073383"></a>

This API is used to create a disk.

## Constraints<a name="en-us_topic_0057973208_section53828184"></a>

-   You are advised to use the EVS API "Creating an EVS Disk \(Native OpenStack API V2\)".

## URI<a name="en-us_topic_0057973208_section41551591"></a>

POST /v2/\{project\_id\}/os-volumes

POST /v2.1/\{project\_id\}/os-volumes

[Table 1](#en-us_topic_0057973208_table2814978410562)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="en-us_topic_0057973208_table2814978410562"></a>
<table><thead align="left"><tr id="en-us_topic_0057973208_row4149654710562"><th class="cellrowborder" valign="top" width="33%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="23%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="44%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973208_row3491217610562"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973208_p931403110562"><a name="en-us_topic_0057973208_p931403110562"></a><a name="en-us_topic_0057973208_p931403110562"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973208_p1623904210562"><a name="en-us_topic_0057973208_p1623904210562"></a><a name="en-us_topic_0057973208_p1623904210562"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0057973208_section25012404"></a>

[Table 2](#en-us_topic_0057973208_table34804632)  describes the request parameters.

**Table  2**  Request parameters

<a name="en-us_topic_0057973208_table34804632"></a>
<table><thead align="left"><tr id="en-us_topic_0057973208_row36029605"><th class="cellrowborder" valign="top" width="17.09%" id="mcps1.2.5.1.1"><p id="en-us_topic_0057973208_p32716899"><a name="en-us_topic_0057973208_p32716899"></a><a name="en-us_topic_0057973208_p32716899"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.37%" id="mcps1.2.5.1.2"><p id="p138650455145"><a name="p138650455145"></a><a name="p138650455145"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16.650000000000002%" id="mcps1.2.5.1.3"><p id="en-us_topic_0057973208_p32823202"><a name="en-us_topic_0057973208_p32823202"></a><a name="en-us_topic_0057973208_p32823202"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48.89%" id="mcps1.2.5.1.4"><p id="en-us_topic_0057973208_p689602"><a name="en-us_topic_0057973208_p689602"></a><a name="en-us_topic_0057973208_p689602"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973208_row6206419"><td class="cellrowborder" valign="top" width="17.09%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973208_p32957959"><a name="en-us_topic_0057973208_p32957959"></a><a name="en-us_topic_0057973208_p32957959"></a>availability_zone</p>
</td>
<td class="cellrowborder" valign="top" width="17.37%" headers="mcps1.2.5.1.2 "><p id="p11865174512140"><a name="p11865174512140"></a><a name="p11865174512140"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16.650000000000002%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973208_p52349023"><a name="en-us_topic_0057973208_p52349023"></a><a name="en-us_topic_0057973208_p52349023"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.89%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973208_p24257404172631"><a name="en-us_topic_0057973208_p24257404172631"></a><a name="en-us_topic_0057973208_p24257404172631"></a>Specifies the AZ to which the volume to be created belongs.</p>
<p id="en-us_topic_0057973208_p53666989172633"><a name="en-us_topic_0057973208_p53666989172633"></a><a name="en-us_topic_0057973208_p53666989172633"></a>If the specified AZ does not exist, creating the volume failed, and the volume is in <strong id="b35370531172633"><a name="b35370531172633"></a><a name="b35370531172633"></a>error</strong> state.</p>
<p id="p46835060174724"><a name="p46835060174724"></a><a name="p46835060174724"></a>The AZ to which the volume to be created belongs must be specified in the public cloud system.</p>
</td>
</tr>
<tr id="en-us_topic_0057973208_row56113289"><td class="cellrowborder" valign="top" width="17.09%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973208_p48882540"><a name="en-us_topic_0057973208_p48882540"></a><a name="en-us_topic_0057973208_p48882540"></a>display_description</p>
</td>
<td class="cellrowborder" valign="top" width="17.37%" headers="mcps1.2.5.1.2 "><p id="p19865845111420"><a name="p19865845111420"></a><a name="p19865845111420"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16.650000000000002%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973208_p62775"><a name="en-us_topic_0057973208_p62775"></a><a name="en-us_topic_0057973208_p62775"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.89%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973208_p9217191"><a name="en-us_topic_0057973208_p9217191"></a><a name="en-us_topic_0057973208_p9217191"></a>Specifies the volume description.</p>
</td>
</tr>
<tr id="en-us_topic_0057973208_row15845862"><td class="cellrowborder" valign="top" width="17.09%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973208_p8446466"><a name="en-us_topic_0057973208_p8446466"></a><a name="en-us_topic_0057973208_p8446466"></a>snapshot_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.37%" headers="mcps1.2.5.1.2 "><p id="p19865144591412"><a name="p19865144591412"></a><a name="p19865144591412"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16.650000000000002%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973208_p13075179"><a name="en-us_topic_0057973208_p13075179"></a><a name="en-us_topic_0057973208_p13075179"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.89%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973208_p43219210172642"><a name="en-us_topic_0057973208_p43219210172642"></a><a name="en-us_topic_0057973208_p43219210172642"></a>Specifies the snapshot ID.</p>
<p id="p37597922174724"><a name="p37597922174724"></a><a name="p37597922174724"></a>If this parameter is specified, the volume is to be created from a snapshot.</p>
</td>
</tr>
<tr id="en-us_topic_0057973208_row55906645"><td class="cellrowborder" valign="top" width="17.09%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973208_p32144388"><a name="en-us_topic_0057973208_p32144388"></a><a name="en-us_topic_0057973208_p32144388"></a>size</p>
</td>
<td class="cellrowborder" valign="top" width="17.37%" headers="mcps1.2.5.1.2 "><p id="p8865045111410"><a name="p8865045111410"></a><a name="p8865045111410"></a>Yes (If the volume is created from a snapshot, this parameter is optional.)</p>
</td>
<td class="cellrowborder" valign="top" width="16.650000000000002%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973208_p53558660"><a name="en-us_topic_0057973208_p53558660"></a><a name="en-us_topic_0057973208_p53558660"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="48.89%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973208_p16360982"><a name="en-us_topic_0057973208_p16360982"></a><a name="en-us_topic_0057973208_p16360982"></a>Specifies the volume size.</p>
<p id="en-us_topic_0057973208_p1280275020341"><a name="en-us_topic_0057973208_p1280275020341"></a><a name="en-us_topic_0057973208_p1280275020341"></a>Unit: GB</p>
</td>
</tr>
<tr id="en-us_topic_0057973208_row13031110"><td class="cellrowborder" valign="top" width="17.09%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973208_p48886962"><a name="en-us_topic_0057973208_p48886962"></a><a name="en-us_topic_0057973208_p48886962"></a>display_name</p>
</td>
<td class="cellrowborder" valign="top" width="17.37%" headers="mcps1.2.5.1.2 "><p id="p20866124516149"><a name="p20866124516149"></a><a name="p20866124516149"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16.650000000000002%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973208_p421011"><a name="en-us_topic_0057973208_p421011"></a><a name="en-us_topic_0057973208_p421011"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.89%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973208_p10796115"><a name="en-us_topic_0057973208_p10796115"></a><a name="en-us_topic_0057973208_p10796115"></a>Specifies the volume name.</p>
</td>
</tr>
<tr id="en-us_topic_0057973208_row30056178"><td class="cellrowborder" valign="top" width="17.09%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973208_p18631317"><a name="en-us_topic_0057973208_p18631317"></a><a name="en-us_topic_0057973208_p18631317"></a>volume_type</p>
</td>
<td class="cellrowborder" valign="top" width="17.37%" headers="mcps1.2.5.1.2 "><p id="p15866154581413"><a name="p15866154581413"></a><a name="p15866154581413"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16.650000000000002%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973208_p32741746"><a name="en-us_topic_0057973208_p32741746"></a><a name="en-us_topic_0057973208_p32741746"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.89%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973208_p3124212"><a name="en-us_topic_0057973208_p3124212"></a><a name="en-us_topic_0057973208_p3124212"></a>Specifies the volume type.</p>
<div class="p" id="en-us_topic_0057973208_p56795419259"><a name="en-us_topic_0057973208_p56795419259"></a><a name="en-us_topic_0057973208_p56795419259"></a>Currently, the value can be <strong id="en-us_topic_0057973208_b842352706164929"><a name="en-us_topic_0057973208_b842352706164929"></a><a name="en-us_topic_0057973208_b842352706164929"></a>SSD</strong>, <strong id="en-us_topic_0057973208_b842352706164932"><a name="en-us_topic_0057973208_b842352706164932"></a><a name="en-us_topic_0057973208_b842352706164932"></a>SAS</strong>, <strong id="en-us_topic_0057973208_b842352706164937"><a name="en-us_topic_0057973208_b842352706164937"></a><a name="en-us_topic_0057973208_b842352706164937"></a>SATA</strong>, <strong id="en-us_topic_0057973208_b842352706164941"><a name="en-us_topic_0057973208_b842352706164941"></a><a name="en-us_topic_0057973208_b842352706164941"></a>co-p1</strong>, or <strong id="en-us_topic_0057973208_b842352706164944"><a name="en-us_topic_0057973208_b842352706164944"></a><a name="en-us_topic_0057973208_b842352706164944"></a>uh-l1</strong>.<a name="en-us_topic_0057973208_ul22154279154310"></a><a name="en-us_topic_0057973208_ul22154279154310"></a><ul id="en-us_topic_0057973208_ul22154279154310"><li><strong id="en-us_topic_0057973208_b842352706165021"><a name="en-us_topic_0057973208_b842352706165021"></a><a name="en-us_topic_0057973208_b842352706165021"></a>SSD</strong>: specifies the ultra-I/O disk type.</li><li><strong id="en-us_topic_0057973208_b1784237562165049"><a name="en-us_topic_0057973208_b1784237562165049"></a><a name="en-us_topic_0057973208_b1784237562165049"></a>SAS</strong>: specifies the high I/O disk type.</li><li><strong id="en-us_topic_0057973208_b3295367816515"><a name="en-us_topic_0057973208_b3295367816515"></a><a name="en-us_topic_0057973208_b3295367816515"></a>SATA</strong>: specifies the common I/O disk type.</li><li><strong id="en-us_topic_0057973208_b842352706144211"><a name="en-us_topic_0057973208_b842352706144211"></a><a name="en-us_topic_0057973208_b842352706144211"></a>co-p1</strong>: specifies the high I/O (performance-optimized I) disk type.</li><li><strong id="en-us_topic_0057973208_b842352706144228"><a name="en-us_topic_0057973208_b842352706144228"></a><a name="en-us_topic_0057973208_b842352706144228"></a>uh-l1</strong>: specifies the ultra-high I/O (latency-optimized) disk type.<div class="note" id="en-us_topic_0057973208_note32771213132611"><a name="en-us_topic_0057973208_note32771213132611"></a><a name="en-us_topic_0057973208_note32771213132611"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0057973208_p65482244154310"><a name="en-us_topic_0057973208_p65482244154310"></a><a name="en-us_topic_0057973208_p65482244154310"></a>EVS disks of the <strong id="en-us_topic_0057973208_b842352706154347"><a name="en-us_topic_0057973208_b842352706154347"></a><a name="en-us_topic_0057973208_b842352706154347"></a>co-p1</strong> and <strong id="en-us_topic_0057973208_b842352706154354"><a name="en-us_topic_0057973208_b842352706154354"></a><a name="en-us_topic_0057973208_b842352706154354"></a>uh-l1</strong> types are used exclusively for high performance computing (HPC) and SAP HANA ECSs.</p>
</div></div>
</li></ul>
</div>
</td>
</tr>
<tr id="en-us_topic_0057973208_row28117914"><td class="cellrowborder" valign="top" width="17.09%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973208_p62958527"><a name="en-us_topic_0057973208_p62958527"></a><a name="en-us_topic_0057973208_p62958527"></a>metadata</p>
</td>
<td class="cellrowborder" valign="top" width="17.37%" headers="mcps1.2.5.1.2 "><p id="p14866445111419"><a name="p14866445111419"></a><a name="p14866445111419"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16.650000000000002%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973208_p66475904"><a name="en-us_topic_0057973208_p66475904"></a><a name="en-us_topic_0057973208_p66475904"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="48.89%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973208_p7904761"><a name="en-us_topic_0057973208_p7904761"></a><a name="en-us_topic_0057973208_p7904761"></a>Specifies the volume metadata.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="en-us_topic_0057973208_section23785046"></a>

[Table 3](#en-us_topic_0057973208_table36305920)  describes the response parameters.

**Table  3**  Response parameters

<a name="en-us_topic_0057973208_table36305920"></a>
<table><thead align="left"><tr id="en-us_topic_0057973208_row2741419"><th class="cellrowborder" valign="top" width="31.003100310031%" id="mcps1.2.4.1.1"><p id="p62404314"><a name="p62404314"></a><a name="p62404314"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="22.38223822382238%" id="mcps1.2.4.1.2"><p id="p3528183"><a name="p3528183"></a><a name="p3528183"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="46.614661466146615%" id="mcps1.2.4.1.3"><p id="p17347392"><a name="p17347392"></a><a name="p17347392"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973208_row15372252"><td class="cellrowborder" valign="top" width="31.003100310031%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973208_p37192867"><a name="en-us_topic_0057973208_p37192867"></a><a name="en-us_topic_0057973208_p37192867"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="22.38223822382238%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973208_p59832271"><a name="en-us_topic_0057973208_p59832271"></a><a name="en-us_topic_0057973208_p59832271"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.614661466146615%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973208_p39790453"><a name="en-us_topic_0057973208_p39790453"></a><a name="en-us_topic_0057973208_p39790453"></a>Specifies the disk ID in UUID format.</p>
</td>
</tr>
<tr id="en-us_topic_0057973208_row22569763"><td class="cellrowborder" valign="top" width="31.003100310031%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973208_p16211514"><a name="en-us_topic_0057973208_p16211514"></a><a name="en-us_topic_0057973208_p16211514"></a>displayName</p>
</td>
<td class="cellrowborder" valign="top" width="22.38223822382238%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973208_p38064249"><a name="en-us_topic_0057973208_p38064249"></a><a name="en-us_topic_0057973208_p38064249"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.614661466146615%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973208_p27459986"><a name="en-us_topic_0057973208_p27459986"></a><a name="en-us_topic_0057973208_p27459986"></a>Specifies the volume name.</p>
</td>
</tr>
<tr id="en-us_topic_0057973208_row45813283"><td class="cellrowborder" valign="top" width="31.003100310031%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973208_p19888403"><a name="en-us_topic_0057973208_p19888403"></a><a name="en-us_topic_0057973208_p19888403"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="22.38223822382238%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973208_p347919"><a name="en-us_topic_0057973208_p347919"></a><a name="en-us_topic_0057973208_p347919"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.614661466146615%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973208_p1000526"><a name="en-us_topic_0057973208_p1000526"></a><a name="en-us_topic_0057973208_p1000526"></a>Specifies the volume status.</p>
</td>
</tr>
<tr id="en-us_topic_0057973208_row9004739"><td class="cellrowborder" valign="top" width="31.003100310031%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973208_p58295271"><a name="en-us_topic_0057973208_p58295271"></a><a name="en-us_topic_0057973208_p58295271"></a>attachments</p>
</td>
<td class="cellrowborder" valign="top" width="22.38223822382238%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973208_p24296474"><a name="en-us_topic_0057973208_p24296474"></a><a name="en-us_topic_0057973208_p24296474"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="46.614661466146615%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973208_p25620180"><a name="en-us_topic_0057973208_p25620180"></a><a name="en-us_topic_0057973208_p25620180"></a>Specifies the volume attachment information.</p>
</td>
</tr>
<tr id="en-us_topic_0057973208_row29255030"><td class="cellrowborder" valign="top" width="31.003100310031%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973208_p20847223"><a name="en-us_topic_0057973208_p20847223"></a><a name="en-us_topic_0057973208_p20847223"></a>availabilityZone</p>
</td>
<td class="cellrowborder" valign="top" width="22.38223822382238%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973208_p10903468"><a name="en-us_topic_0057973208_p10903468"></a><a name="en-us_topic_0057973208_p10903468"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.614661466146615%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973208_p66714836"><a name="en-us_topic_0057973208_p66714836"></a><a name="en-us_topic_0057973208_p66714836"></a>Specifies the AZ to which the volume belongs.</p>
</td>
</tr>
<tr id="en-us_topic_0057973208_row63562612"><td class="cellrowborder" valign="top" width="31.003100310031%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973208_p48297932"><a name="en-us_topic_0057973208_p48297932"></a><a name="en-us_topic_0057973208_p48297932"></a>createdAt</p>
</td>
<td class="cellrowborder" valign="top" width="22.38223822382238%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973208_p19818396"><a name="en-us_topic_0057973208_p19818396"></a><a name="en-us_topic_0057973208_p19818396"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.614661466146615%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973208_p38630598"><a name="en-us_topic_0057973208_p38630598"></a><a name="en-us_topic_0057973208_p38630598"></a>Specifies the time when the volume was created.</p>
</td>
</tr>
<tr id="en-us_topic_0057973208_row12131070"><td class="cellrowborder" valign="top" width="31.003100310031%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973208_p43092599"><a name="en-us_topic_0057973208_p43092599"></a><a name="en-us_topic_0057973208_p43092599"></a>displayDescription</p>
</td>
<td class="cellrowborder" valign="top" width="22.38223822382238%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973208_p839629"><a name="en-us_topic_0057973208_p839629"></a><a name="en-us_topic_0057973208_p839629"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.614661466146615%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973208_p5879853"><a name="en-us_topic_0057973208_p5879853"></a><a name="en-us_topic_0057973208_p5879853"></a>Specifies the volume description.</p>
</td>
</tr>
<tr id="en-us_topic_0057973208_row52918685"><td class="cellrowborder" valign="top" width="31.003100310031%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973208_p58555089"><a name="en-us_topic_0057973208_p58555089"></a><a name="en-us_topic_0057973208_p58555089"></a>volumeType</p>
</td>
<td class="cellrowborder" valign="top" width="22.38223822382238%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973208_p45341798"><a name="en-us_topic_0057973208_p45341798"></a><a name="en-us_topic_0057973208_p45341798"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.614661466146615%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973208_p61056466"><a name="en-us_topic_0057973208_p61056466"></a><a name="en-us_topic_0057973208_p61056466"></a>Specifies the volume type.</p>
</td>
</tr>
<tr id="en-us_topic_0057973208_row12637282"><td class="cellrowborder" valign="top" width="31.003100310031%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973208_p16986940"><a name="en-us_topic_0057973208_p16986940"></a><a name="en-us_topic_0057973208_p16986940"></a>snapshotId</p>
</td>
<td class="cellrowborder" valign="top" width="22.38223822382238%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973208_p33764890"><a name="en-us_topic_0057973208_p33764890"></a><a name="en-us_topic_0057973208_p33764890"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="46.614661466146615%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973208_p5086724"><a name="en-us_topic_0057973208_p5086724"></a><a name="en-us_topic_0057973208_p5086724"></a>Specifies the snapshot ID.</p>
</td>
</tr>
<tr id="en-us_topic_0057973208_row45780519"><td class="cellrowborder" valign="top" width="31.003100310031%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973208_p17234528"><a name="en-us_topic_0057973208_p17234528"></a><a name="en-us_topic_0057973208_p17234528"></a>metadata</p>
</td>
<td class="cellrowborder" valign="top" width="22.38223822382238%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973208_p53819489"><a name="en-us_topic_0057973208_p53819489"></a><a name="en-us_topic_0057973208_p53819489"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="46.614661466146615%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973208_p49936605"><a name="en-us_topic_0057973208_p49936605"></a><a name="en-us_topic_0057973208_p49936605"></a>Specifies the volume metadata.</p>
</td>
</tr>
<tr id="en-us_topic_0057973208_row46776267"><td class="cellrowborder" valign="top" width="31.003100310031%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973208_p30781293"><a name="en-us_topic_0057973208_p30781293"></a><a name="en-us_topic_0057973208_p30781293"></a>size</p>
</td>
<td class="cellrowborder" valign="top" width="22.38223822382238%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973208_p10256828"><a name="en-us_topic_0057973208_p10256828"></a><a name="en-us_topic_0057973208_p10256828"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="46.614661466146615%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973208_p51969663"><a name="en-us_topic_0057973208_p51969663"></a><a name="en-us_topic_0057973208_p51969663"></a>Specifies the size of the volume.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="en-us_topic_0057973208_section12738823"></a>

```
POST https://{endpoint}/v2/b84c367e4d1047fc9b54f28b400ddbc2/os-volumes
POST https://{endpoint}/v2.1/b84c367e4d1047fc9b54f28b400ddbc2/os-volumes
```

```
{
    "volume": {
        "availability_zone": "az1-dc1",
        "display_description": "test1",
        "snapshot_id": null,
        "size": 1,
        "display_name": "test",
        "volume_type": "SATA",
        "metadata": {
            "testkey": "testvalue"
        }
    }
}
```

## Example Response<a name="section1781844134020"></a>

```
{
  "volume": {
    "displayDescription": "test1",
    "volumeType": "SATA",
    "createdAt": "2018-05-18T01:17:03.871808",
    "metadata": {
      "testkey": "testvalue",
      "resourceSpecCode": "SATA"
    },
    "attachments": [
      {}
    ],
    "snapshotId": null,
    "size": 1,
    "displayName": "test",
    "id": "b4fb891c-c665-4478-92b0-8a7fa65a57cd",
    "availabilityZone": "az1.dc1",
    "status": "creating"
  }
}
```

## Returned Values<a name="en-us_topic_0057973208_en-us_topic_0020212692_section22960139"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).


# Querying Image Details \(Discarded\)<a name="EN-US_TOPIC_0065817696"></a>

## Function<a name="en-us_topic_0057973097_section53835255"></a>

This API is used to query detailed information about an image list.

## Constraints<a name="en-us_topic_0057973097_section65688375"></a>

-   This API will be discarded. You are advised to use the IMS API "Querying Images".

## URI<a name="en-us_topic_0057973097_section14755248"></a>

GET /v2/\{project\_id\}/images/detail\{?name,status,changes-since,minRam,minDisk\}

GET /v2.1/\{project\_id\}/images/detail\{?name,status,changes-since,minRam,minDisk\}

[Table 1](#en-us_topic_0057973097_en-us_topic_0020212650_table62669527)  describes the parameters in the URI.

**Table  1**  Path parameters

<a name="en-us_topic_0057973097_en-us_topic_0020212650_table62669527"></a>
<table><thead align="left"><tr id="en-us_topic_0057973097_en-us_topic_0020212650_row33894570"><th class="cellrowborder" valign="top" width="20.74%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.05%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="60.209999999999994%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973097_en-us_topic_0020212650_row8419032"><td class="cellrowborder" valign="top" width="20.74%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973097_en-us_topic_0020212650_p10852974"><a name="en-us_topic_0057973097_en-us_topic_0020212650_p10852974"></a><a name="en-us_topic_0057973097_en-us_topic_0020212650_p10852974"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973097_en-us_topic_0020212650_p6675738"><a name="en-us_topic_0057973097_en-us_topic_0020212650_p6675738"></a><a name="en-us_topic_0057973097_en-us_topic_0020212650_p6675738"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="60.209999999999994%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

Parameters in the following table can be used as URI parameters to filter query results. Usage: /v2/\{tenant\_id\}/images/detail? name =\{name\}&status=\{status\}

[Table 2](#en-us_topic_0057973097_table9527550)  describes the query parameters.

**Table  2**  Query parameters

<a name="en-us_topic_0057973097_table9527550"></a>
<table><thead align="left"><tr id="en-us_topic_0057973097_row40739767"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.5.1.1"><p id="en-us_topic_0057973097_p11586820"><a name="en-us_topic_0057973097_p11586820"></a><a name="en-us_topic_0057973097_p11586820"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.2"><p id="en-us_topic_0057973097_p53893727"><a name="en-us_topic_0057973097_p53893727"></a><a name="en-us_topic_0057973097_p53893727"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.3"><p id="en-us_topic_0057973097_p66117209"><a name="en-us_topic_0057973097_p66117209"></a><a name="en-us_topic_0057973097_p66117209"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="47%" id="mcps1.2.5.1.4"><p id="en-us_topic_0057973097_p3315773"><a name="en-us_topic_0057973097_p3315773"></a><a name="en-us_topic_0057973097_p3315773"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973097_row142236"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973097_p11521188"><a name="en-us_topic_0057973097_p11521188"></a><a name="en-us_topic_0057973097_p11521188"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057973097_p25935564"><a name="en-us_topic_0057973097_p25935564"></a><a name="en-us_topic_0057973097_p25935564"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973097_p60801020"><a name="en-us_topic_0057973097_p60801020"></a><a name="en-us_topic_0057973097_p60801020"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973097_p20405949"><a name="en-us_topic_0057973097_p20405949"></a><a name="en-us_topic_0057973097_p20405949"></a>Specifies the image name.</p>
</td>
</tr>
<tr id="en-us_topic_0057973097_row49435817"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973097_p44878254"><a name="en-us_topic_0057973097_p44878254"></a><a name="en-us_topic_0057973097_p44878254"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057973097_p39640189"><a name="en-us_topic_0057973097_p39640189"></a><a name="en-us_topic_0057973097_p39640189"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973097_p11259943"><a name="en-us_topic_0057973097_p11259943"></a><a name="en-us_topic_0057973097_p11259943"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973097_p138506815355"><a name="en-us_topic_0057973097_p138506815355"></a><a name="en-us_topic_0057973097_p138506815355"></a>Specifies the image status.</p>
<p id="en-us_topic_0057973097_p56738711"><a name="en-us_topic_0057973097_p56738711"></a><a name="en-us_topic_0057973097_p56738711"></a>You cannot query images when the value is set to <strong id="en-us_topic_0057973097_b1786951984314"><a name="en-us_topic_0057973097_b1786951984314"></a><a name="en-us_topic_0057973097_b1786951984314"></a>deleted</strong>. The value depends on the status in Glance. <a href="#en-us_topic_0057973097_table56563076204045">Table 3</a> shows the mapping relationship of image status in Nova and Glance.</p>
</td>
</tr>
<tr id="en-us_topic_0057973097_row23460301"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973097_p21236225"><a name="en-us_topic_0057973097_p21236225"></a><a name="en-us_topic_0057973097_p21236225"></a>changes-since</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057973097_p12876212"><a name="en-us_topic_0057973097_p12876212"></a><a name="en-us_topic_0057973097_p12876212"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973097_p42412694"><a name="en-us_topic_0057973097_p42412694"></a><a name="en-us_topic_0057973097_p42412694"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973097_p36340226"><a name="en-us_topic_0057973097_p36340226"></a><a name="en-us_topic_0057973097_p36340226"></a>Specifies the images modified after the <strong id="en-us_topic_0057973097_b19912106"><a name="en-us_topic_0057973097_b19912106"></a><a name="en-us_topic_0057973097_b19912106"></a>changes-since</strong> time point. The value is in ISO8601 format, such as <strong id="en-us_topic_0057973097_b44991234"><a name="en-us_topic_0057973097_b44991234"></a><a name="en-us_topic_0057973097_b44991234"></a>2013-06-09T06:42:18Z</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0057973097_row58626578"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973097_p51132396"><a name="en-us_topic_0057973097_p51132396"></a><a name="en-us_topic_0057973097_p51132396"></a>minRam</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057973097_p2441493"><a name="en-us_topic_0057973097_p2441493"></a><a name="en-us_topic_0057973097_p2441493"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973097_p48083402"><a name="en-us_topic_0057973097_p48083402"></a><a name="en-us_topic_0057973097_p48083402"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973097_p63543220"><a name="en-us_topic_0057973097_p63543220"></a><a name="en-us_topic_0057973097_p63543220"></a>Specifies the minimum memory size in MB required by the image.</p>
</td>
</tr>
<tr id="en-us_topic_0057973097_row35018071"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973097_p17891472"><a name="en-us_topic_0057973097_p17891472"></a><a name="en-us_topic_0057973097_p17891472"></a>minDisk</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057973097_p12544771"><a name="en-us_topic_0057973097_p12544771"></a><a name="en-us_topic_0057973097_p12544771"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973097_p39923089"><a name="en-us_topic_0057973097_p39923089"></a><a name="en-us_topic_0057973097_p39923089"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973097_p9493517"><a name="en-us_topic_0057973097_p9493517"></a><a name="en-us_topic_0057973097_p9493517"></a>Specifies the minimum disk size in GB required by the image.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Mapping relationship of image status in Nova and Glance

<a name="en-us_topic_0057973097_table56563076204045"></a>
<table><thead align="left"><tr id="en-us_topic_0057973097_row65938902204045"><th class="cellrowborder" valign="top" width="41.730000000000004%" id="mcps1.2.3.1.1"><p id="en-us_topic_0057973097_p52668896204057"><a name="en-us_topic_0057973097_p52668896204057"></a><a name="en-us_topic_0057973097_p52668896204057"></a>Image Status in Glance</p>
</th>
<th class="cellrowborder" valign="top" width="58.269999999999996%" id="mcps1.2.3.1.2"><p id="en-us_topic_0057973097_p38322201204057"><a name="en-us_topic_0057973097_p38322201204057"></a><a name="en-us_topic_0057973097_p38322201204057"></a>Image Status in Nova</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973097_row65466149204045"><td class="cellrowborder" valign="top" width="41.730000000000004%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0057973097_p19597186204057"><a name="en-us_topic_0057973097_p19597186204057"></a><a name="en-us_topic_0057973097_p19597186204057"></a>queued</p>
</td>
<td class="cellrowborder" valign="top" width="58.269999999999996%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0057973097_p43868206204057"><a name="en-us_topic_0057973097_p43868206204057"></a><a name="en-us_topic_0057973097_p43868206204057"></a>saving</p>
</td>
</tr>
<tr id="en-us_topic_0057973097_row38779097204045"><td class="cellrowborder" valign="top" width="41.730000000000004%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0057973097_p36103503204057"><a name="en-us_topic_0057973097_p36103503204057"></a><a name="en-us_topic_0057973097_p36103503204057"></a>saving</p>
</td>
<td class="cellrowborder" valign="top" width="58.269999999999996%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0057973097_p38702650204057"><a name="en-us_topic_0057973097_p38702650204057"></a><a name="en-us_topic_0057973097_p38702650204057"></a>saving</p>
</td>
</tr>
<tr id="en-us_topic_0057973097_row45401992204045"><td class="cellrowborder" valign="top" width="41.730000000000004%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0057973097_p28509438204057"><a name="en-us_topic_0057973097_p28509438204057"></a><a name="en-us_topic_0057973097_p28509438204057"></a>active</p>
</td>
<td class="cellrowborder" valign="top" width="58.269999999999996%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0057973097_p27563137204057"><a name="en-us_topic_0057973097_p27563137204057"></a><a name="en-us_topic_0057973097_p27563137204057"></a>active</p>
</td>
</tr>
<tr id="en-us_topic_0057973097_row10229781204045"><td class="cellrowborder" valign="top" width="41.730000000000004%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0057973097_p27976971204057"><a name="en-us_topic_0057973097_p27976971204057"></a><a name="en-us_topic_0057973097_p27976971204057"></a>deleted</p>
</td>
<td class="cellrowborder" valign="top" width="58.269999999999996%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0057973097_p51542160204057"><a name="en-us_topic_0057973097_p51542160204057"></a><a name="en-us_topic_0057973097_p51542160204057"></a>deleted</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section162647256113"></a>

None

## Response<a name="en-us_topic_0057973097_section38205788"></a>

[Table 4](#en-us_topic_0057973097_table8561437)  describes the response parameters.

**Table  4**  Response parameters

<a name="en-us_topic_0057973097_table8561437"></a>
<table><thead align="left"><tr id="en-us_topic_0057973097_row897193"><th class="cellrowborder" valign="top" width="30.570000000000004%" id="mcps1.2.4.1.1"><p id="en-us_topic_0057973097_p5563790"><a name="en-us_topic_0057973097_p5563790"></a><a name="en-us_topic_0057973097_p5563790"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25.06%" id="mcps1.2.4.1.2"><p id="en-us_topic_0057973097_p48013860"><a name="en-us_topic_0057973097_p48013860"></a><a name="en-us_topic_0057973097_p48013860"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="44.37%" id="mcps1.2.4.1.3"><p id="en-us_topic_0057973097_p9931649"><a name="en-us_topic_0057973097_p9931649"></a><a name="en-us_topic_0057973097_p9931649"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973097_row66266137"><td class="cellrowborder" valign="top" width="30.570000000000004%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973097_p65956865"><a name="en-us_topic_0057973097_p65956865"></a><a name="en-us_topic_0057973097_p65956865"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973097_p40905825"><a name="en-us_topic_0057973097_p40905825"></a><a name="en-us_topic_0057973097_p40905825"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.37%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973097_p14774699"><a name="en-us_topic_0057973097_p14774699"></a><a name="en-us_topic_0057973097_p14774699"></a>Specifies the image ID in UUID format.</p>
</td>
</tr>
<tr id="en-us_topic_0057973097_row65863435"><td class="cellrowborder" valign="top" width="30.570000000000004%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973097_p33338004"><a name="en-us_topic_0057973097_p33338004"></a><a name="en-us_topic_0057973097_p33338004"></a>links</p>
</td>
<td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972661_p11990221102658"><a name="en-us_topic_0057972661_p11990221102658"></a><a name="en-us_topic_0057972661_p11990221102658"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="44.37%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973097_p39684730"><a name="en-us_topic_0057973097_p39684730"></a><a name="en-us_topic_0057973097_p39684730"></a>Specifies the shortcut link of the image.</p>
</td>
</tr>
<tr id="en-us_topic_0057973097_row21618258"><td class="cellrowborder" valign="top" width="30.570000000000004%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973097_p6248470"><a name="en-us_topic_0057973097_p6248470"></a><a name="en-us_topic_0057973097_p6248470"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973097_p36364091"><a name="en-us_topic_0057973097_p36364091"></a><a name="en-us_topic_0057973097_p36364091"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.37%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973097_p12794567"><a name="en-us_topic_0057973097_p12794567"></a><a name="en-us_topic_0057973097_p12794567"></a>Specifies the image name.</p>
</td>
</tr>
<tr id="en-us_topic_0057973097_row48042239"><td class="cellrowborder" valign="top" width="30.570000000000004%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973097_p66216169"><a name="en-us_topic_0057973097_p66216169"></a><a name="en-us_topic_0057973097_p66216169"></a>metadata</p>
</td>
<td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973097_p61909463"><a name="en-us_topic_0057973097_p61909463"></a><a name="en-us_topic_0057973097_p61909463"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="44.37%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973097_p45145313"><a name="en-us_topic_0057973097_p45145313"></a><a name="en-us_topic_0057973097_p45145313"></a>Specifies the key pair of the metadata.</p>
</td>
</tr>
<tr id="en-us_topic_0057973097_row3654636"><td class="cellrowborder" valign="top" width="30.570000000000004%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973097_p27590069"><a name="en-us_topic_0057973097_p27590069"></a><a name="en-us_topic_0057973097_p27590069"></a>OS-EXT-IMG-SIZE:size</p>
</td>
<td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973097_p20203078"><a name="en-us_topic_0057973097_p20203078"></a><a name="en-us_topic_0057973097_p20203078"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="44.37%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973097_p563904521109"><a name="en-us_topic_0057973097_p563904521109"></a><a name="en-us_topic_0057973097_p563904521109"></a>Specifies the image size.</p>
<p id="en-us_topic_0057973097_p12391138"><a name="en-us_topic_0057973097_p12391138"></a><a name="en-us_topic_0057973097_p12391138"></a>The value must be greater than zero.</p>
</td>
</tr>
<tr id="en-us_topic_0057973097_row44411384"><td class="cellrowborder" valign="top" width="30.570000000000004%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973097_p40552362"><a name="en-us_topic_0057973097_p40552362"></a><a name="en-us_topic_0057973097_p40552362"></a>minDisk</p>
</td>
<td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973097_p63515913"><a name="en-us_topic_0057973097_p63515913"></a><a name="en-us_topic_0057973097_p63515913"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="44.37%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973097_p38169525211017"><a name="en-us_topic_0057973097_p38169525211017"></a><a name="en-us_topic_0057973097_p38169525211017"></a>Specifies the minimum disk size in GB required by the image.</p>
<p id="en-us_topic_0057973097_p48971500"><a name="en-us_topic_0057973097_p48971500"></a><a name="en-us_topic_0057973097_p48971500"></a>The value must be greater than zero.</p>
</td>
</tr>
<tr id="en-us_topic_0057973097_row38090318"><td class="cellrowborder" valign="top" width="30.570000000000004%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973097_p65416899"><a name="en-us_topic_0057973097_p65416899"></a><a name="en-us_topic_0057973097_p65416899"></a>minRam</p>
</td>
<td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973097_p64277481"><a name="en-us_topic_0057973097_p64277481"></a><a name="en-us_topic_0057973097_p64277481"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="44.37%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973097_p65574438211019"><a name="en-us_topic_0057973097_p65574438211019"></a><a name="en-us_topic_0057973097_p65574438211019"></a>Specifies the minimum memory size in GB required by the image.</p>
<p id="en-us_topic_0057973097_p12455270"><a name="en-us_topic_0057973097_p12455270"></a><a name="en-us_topic_0057973097_p12455270"></a>The value must be greater than zero.</p>
</td>
</tr>
<tr id="en-us_topic_0057973097_row44988574"><td class="cellrowborder" valign="top" width="30.570000000000004%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973097_p20195840"><a name="en-us_topic_0057973097_p20195840"></a><a name="en-us_topic_0057973097_p20195840"></a>progress</p>
</td>
<td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973097_p25250359"><a name="en-us_topic_0057973097_p25250359"></a><a name="en-us_topic_0057973097_p25250359"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="44.37%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973097_p57294044211022"><a name="en-us_topic_0057973097_p57294044211022"></a><a name="en-us_topic_0057973097_p57294044211022"></a>Specifies the image upload progress.</p>
<p id="en-us_topic_0057973097_p42934595"><a name="en-us_topic_0057973097_p42934595"></a><a name="en-us_topic_0057973097_p42934595"></a>The value must be greater than zero.</p>
</td>
</tr>
<tr id="en-us_topic_0057973097_row50867040"><td class="cellrowborder" valign="top" width="30.570000000000004%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973097_p26589610"><a name="en-us_topic_0057973097_p26589610"></a><a name="en-us_topic_0057973097_p26589610"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973097_p6274829"><a name="en-us_topic_0057973097_p6274829"></a><a name="en-us_topic_0057973097_p6274829"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.37%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973097_p31420987"><a name="en-us_topic_0057973097_p31420987"></a><a name="en-us_topic_0057973097_p31420987"></a>Specifies the image status.</p>
</td>
</tr>
<tr id="en-us_topic_0057973097_row14353431"><td class="cellrowborder" valign="top" width="30.570000000000004%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973097_p21777299"><a name="en-us_topic_0057973097_p21777299"></a><a name="en-us_topic_0057973097_p21777299"></a>created</p>
</td>
<td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973097_p19130762"><a name="en-us_topic_0057973097_p19130762"></a><a name="en-us_topic_0057973097_p19130762"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.37%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973097_p40625131211057"><a name="en-us_topic_0057973097_p40625131211057"></a><a name="en-us_topic_0057973097_p40625131211057"></a>Specifies the image creation time.</p>
<p id="en-us_topic_0057973097_p23358735"><a name="en-us_topic_0057973097_p23358735"></a><a name="en-us_topic_0057973097_p23358735"></a>The value is in ISO8601 format, such as <strong id="en-us_topic_0057973097_b10555252"><a name="en-us_topic_0057973097_b10555252"></a><a name="en-us_topic_0057973097_b10555252"></a>2013-06-09T06:42:18Z</strong>.</p>
</td>
</tr>
<tr id="en-us_topic_0057973097_row8902028"><td class="cellrowborder" valign="top" width="30.570000000000004%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973097_p49975634"><a name="en-us_topic_0057973097_p49975634"></a><a name="en-us_topic_0057973097_p49975634"></a>updated</p>
</td>
<td class="cellrowborder" valign="top" width="25.06%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973097_p21494553"><a name="en-us_topic_0057973097_p21494553"></a><a name="en-us_topic_0057973097_p21494553"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44.37%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973097_p232867821110"><a name="en-us_topic_0057973097_p232867821110"></a><a name="en-us_topic_0057973097_p232867821110"></a>Specifies the image update time.</p>
<p id="en-us_topic_0057973097_p30041544"><a name="en-us_topic_0057973097_p30041544"></a><a name="en-us_topic_0057973097_p30041544"></a>The value is in ISO8601 format, such as <strong id="en-us_topic_0057973097_b23842638"><a name="en-us_topic_0057973097_b23842638"></a><a name="en-us_topic_0057973097_b23842638"></a>2013-06-09T06:42:18Z</strong>.</p>
</td>
</tr>
</tbody>
</table>

**Table  5** **links**  parameter description

<a name="table06801854144013"></a>
<table><thead align="left"><tr id="en-us_topic_0065817695_en-us_topic_0057973086_row54901254195115"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.1"><p id="en-us_topic_0065817695_p131661047125817"><a name="en-us_topic_0065817695_p131661047125817"></a><a name="en-us_topic_0065817695_p131661047125817"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.2"><p id="en-us_topic_0065817695_p15166194715818"><a name="en-us_topic_0065817695_p15166194715818"></a><a name="en-us_topic_0065817695_p15166194715818"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.3"><p id="en-us_topic_0065817695_p10166194719587"><a name="en-us_topic_0065817695_p10166194719587"></a><a name="en-us_topic_0065817695_p10166194719587"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="44%" id="mcps1.2.5.1.4"><p id="en-us_topic_0065817695_p91661478589"><a name="en-us_topic_0065817695_p91661478589"></a><a name="en-us_topic_0065817695_p91661478589"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0065817695_en-us_topic_0057973086_row1549185415113"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0065817695_en-us_topic_0057973086_p1449195414513"><a name="en-us_topic_0065817695_en-us_topic_0057973086_p1449195414513"></a><a name="en-us_topic_0065817695_en-us_topic_0057973086_p1449195414513"></a>href</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0065817695_en-us_topic_0057973086_p1449195455118"><a name="en-us_topic_0065817695_en-us_topic_0057973086_p1449195455118"></a><a name="en-us_topic_0065817695_en-us_topic_0057973086_p1449195455118"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0065817695_en-us_topic_0057973086_p449195425114"><a name="en-us_topic_0065817695_en-us_topic_0057973086_p449195425114"></a><a name="en-us_topic_0065817695_en-us_topic_0057973086_p449195425114"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0065817695_en-us_topic_0057973086_p18491754135111"><a name="en-us_topic_0065817695_en-us_topic_0057973086_p18491754135111"></a><a name="en-us_topic_0065817695_en-us_topic_0057973086_p18491754135111"></a>Specifies the link of the corresponding resource.</p>
</td>
</tr>
<tr id="en-us_topic_0065817695_en-us_topic_0057973086_row16491145435118"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0065817695_en-us_topic_0057973086_p4491155415518"><a name="en-us_topic_0065817695_en-us_topic_0057973086_p4491155415518"></a><a name="en-us_topic_0065817695_en-us_topic_0057973086_p4491155415518"></a>rel</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0065817695_en-us_topic_0057973086_p2491185485110"><a name="en-us_topic_0065817695_en-us_topic_0057973086_p2491185485110"></a><a name="en-us_topic_0065817695_en-us_topic_0057973086_p2491185485110"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0065817695_en-us_topic_0057973086_p1449165411514"><a name="en-us_topic_0065817695_en-us_topic_0057973086_p1449165411514"></a><a name="en-us_topic_0065817695_en-us_topic_0057973086_p1449165411514"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0065817695_en-us_topic_0057973086_p44540131181624"><a name="en-us_topic_0065817695_en-us_topic_0057973086_p44540131181624"></a><a name="en-us_topic_0065817695_en-us_topic_0057973086_p44540131181624"></a>The value can be:</p>
<a name="en-us_topic_0065817695_en-us_topic_0057973086_ul50320171175059"></a><a name="en-us_topic_0065817695_en-us_topic_0057973086_ul50320171175059"></a><ul id="en-us_topic_0065817695_en-us_topic_0057973086_ul50320171175059"><li><strong id="en-us_topic_0065817695_b11003816175111"><a name="en-us_topic_0065817695_b11003816175111"></a><a name="en-us_topic_0065817695_b11003816175111"></a>self</strong>: A self link contains a version link to the resource. Use these links when the link is followed immediately.</li><li><strong id="en-us_topic_0065817695_b60630642175154"><a name="en-us_topic_0065817695_b60630642175154"></a><a name="en-us_topic_0065817695_b60630642175154"></a>bookmark</strong>: A bookmark link provides a permanent link to a resource, which is suitable for long term storage.</li><li><strong id="en-us_topic_0065817695_b28772520175321"><a name="en-us_topic_0065817695_b28772520175321"></a><a name="en-us_topic_0065817695_b28772520175321"></a>alternate</strong>: An alternate link can contain an alternate representation of the resource. For example, an OpenStack Compute image may have an alternate representation in the OpenStack image service.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0065817695_en-us_topic_0057973086_row15491195465112"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0065817695_en-us_topic_0057973086_p149145411510"><a name="en-us_topic_0065817695_en-us_topic_0057973086_p149145411510"></a><a name="en-us_topic_0065817695_en-us_topic_0057973086_p149145411510"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0065817695_en-us_topic_0057973086_p1949195405118"><a name="en-us_topic_0065817695_en-us_topic_0057973086_p1949195405118"></a><a name="en-us_topic_0065817695_en-us_topic_0057973086_p1949195405118"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0065817695_en-us_topic_0057973086_p649155425114"><a name="en-us_topic_0065817695_en-us_topic_0057973086_p649155425114"></a><a name="en-us_topic_0065817695_en-us_topic_0057973086_p649155425114"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0065817695_en-us_topic_0057973086_p1671811201581"><a name="en-us_topic_0065817695_en-us_topic_0057973086_p1671811201581"></a><a name="en-us_topic_0065817695_en-us_topic_0057973086_p1671811201581"></a>The type attribute provides a hint as to the type of representation to expect when following the link.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="section8647424112917"></a>

```
GET https://{endpoint}/v2/9c53a566cb3443ab910cf0daebca90c4/images/detail
GET https://{endpoint}/v2.1/9c53a566cb3443ab910cf0daebca90c4/images/detail
```

## Example Response<a name="section1315616273226"></a>

```
{
    "image": {
        "OS-EXT-IMG-SIZE:size": 20578304,
        "created": "2014-02-10T17:05:01Z",
        "id": "ee10f19c-503c-44af-af2f-73d5e42f7a17",
        "links": [
            {
                "href": "http://172.25.150.84:8774/v2/d9ebe43510414ef590a4aa158605329e/images/ee10f19c-503c-44af-af2f-73d5e42f7a17",
                "rel": "self"
            },
            {
                "href": "http://172.25.150.84:8774/d9ebe43510414ef590a4aa158605329e/images/ee10f19c-503c-44af-af2f-73d5e42f7a17",
                "rel": "bookmark"
            },
            {
                "href": "http://172.25.150.84:9292/d9ebe43510414ef590a4aa158605329e/images/ee10f19c-503c-44af-af2f-73d5e42f7a17",
                "rel": "alternate",
                "type": "application/vnd.openstack.image"
            }
        ],
        "metadata": {
            "clean_attempts": "3",
            "image_location": "snapshot",
            "image_state": "available",
            "image_type": "snapshot",
            "instance_type_ephemeral_gb": "0",
            "instance_type_flavorid": "6",
            "instance_type_id": "7",
            "instance_type_memory_mb": "256",
            "instance_type_name": "wj.ssd",
            "instance_type_root_gb": "2",
            "instance_type_rxtx_factor": "1.0",
            "instance_type_swap": "0",
            "instance_type_vcpus": "1",
            "instance_uuid": "b600b5b1-ed8c-4814-aefa-8b903c894c20",
            "os_type": "None",
            "owner_id": "d9ebe43510414ef590a4aa158605329e",
            "user_id": "74fe4ff0674b434b8a274077d8106c5b"
        },
        "minDisk": 2,
        "minRam": 0,
        "name": "image1",
        "progress": 100,
        "server": {
            "id": "b600b5b1-ed8c-4814-aefa-8b903c894c20",
            "links": [
                {
                    "href": "http://172.25.150.84:8774/v2/d9ebe43510414ef590a4aa158605329e/servers/b600b5b1-ed8c-4814-aefa-8b903c894c20",
                    "rel": "self"
                },
                {
                    "href": "http://172.25.150.84:8774/d9ebe43510414ef590a4aa158605329e/servers/b600b5b1-ed8c-4814-aefa-8b903c894c20",
                    "rel": "bookmark"
                }
            ]
        },
        "status": "ACTIVE",
        "updated": "2014-02-10T17:05:07Z"
    }
}
```

## Returned Values<a name="en-us_topic_0057973097_section41491842"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).


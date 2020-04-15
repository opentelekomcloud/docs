# Querying Images \(Discarded\)<a name="EN-US_TOPIC_0065817695"></a>

## Function<a name="en-us_topic_0057973086_section36920527"></a>

This API is used to query all images.

## Constraints<a name="en-us_topic_0057973086_section37772735"></a>

-   This API will be discarded. You are advised to use the IMS API "Querying Images \(Native OpenStack API\)".

## URI<a name="en-us_topic_0057973086_section63849294"></a>

GET /v2/\{project\_id\}/images\{?name,status,changes-since,minRam,minDisk\}

GET /v2.1/\{project\_id\}/images\{?name,status,changes-since,minRam,minDisk\}

[Table 1](#en-us_topic_0057973086_en-us_topic_0020212650_table62669527)  describes the parameters in the URI.

**Table  1**  Path parameters

<a name="en-us_topic_0057973086_en-us_topic_0020212650_table62669527"></a>
<table><thead align="left"><tr id="en-us_topic_0057973086_en-us_topic_0020212650_row33894570"><th class="cellrowborder" valign="top" width="20.74%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.05%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="60.209999999999994%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973086_en-us_topic_0020212650_row8419032"><td class="cellrowborder" valign="top" width="20.74%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973086_en-us_topic_0020212650_p10852974"><a name="en-us_topic_0057973086_en-us_topic_0020212650_p10852974"></a><a name="en-us_topic_0057973086_en-us_topic_0020212650_p10852974"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973086_en-us_topic_0020212650_p6675738"><a name="en-us_topic_0057973086_en-us_topic_0020212650_p6675738"></a><a name="en-us_topic_0057973086_en-us_topic_0020212650_p6675738"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="60.209999999999994%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

Parameters in the following table can be used as URI parameters to filter query results. Usage: /v2/\{project\_id\}/images? name =\{name\}&status=\{status\}

[Table 2](#en-us_topic_0057973086_table37477597)  describes the query parameters.

**Table  2**  Query parameters

<a name="en-us_topic_0057973086_table37477597"></a>
<table><thead align="left"><tr id="en-us_topic_0057973086_row35810771"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.1"><p id="en-us_topic_0057973086_p14991335"><a name="en-us_topic_0057973086_p14991335"></a><a name="en-us_topic_0057973086_p14991335"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.2.5.1.2"><p id="p3628114112311"><a name="p3628114112311"></a><a name="p3628114112311"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="en-us_topic_0057973086_p6338652"><a name="en-us_topic_0057973086_p6338652"></a><a name="en-us_topic_0057973086_p6338652"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="47%" id="mcps1.2.5.1.4"><p id="en-us_topic_0057973086_p47513992"><a name="en-us_topic_0057973086_p47513992"></a><a name="en-us_topic_0057973086_p47513992"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973086_row23428110"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973086_p18628757"><a name="en-us_topic_0057973086_p18628757"></a><a name="en-us_topic_0057973086_p18628757"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.2 "><p id="p662819147233"><a name="p662819147233"></a><a name="p662819147233"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973086_p32534340"><a name="en-us_topic_0057973086_p32534340"></a><a name="en-us_topic_0057973086_p32534340"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973086_p51622461"><a name="en-us_topic_0057973086_p51622461"></a><a name="en-us_topic_0057973086_p51622461"></a>Specifies the image name.</p>
</td>
</tr>
<tr id="en-us_topic_0057973086_row61948966"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973086_p51810310"><a name="en-us_topic_0057973086_p51810310"></a><a name="en-us_topic_0057973086_p51810310"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.2 "><p id="p86282141231"><a name="p86282141231"></a><a name="p86282141231"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973086_p35885554"><a name="en-us_topic_0057973086_p35885554"></a><a name="en-us_topic_0057973086_p35885554"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973086_p2209424143317"><a name="en-us_topic_0057973086_p2209424143317"></a><a name="en-us_topic_0057973086_p2209424143317"></a>Specifies the image status.</p>
<p id="en-us_topic_0057973086_p27230225"><a name="en-us_topic_0057973086_p27230225"></a><a name="en-us_topic_0057973086_p27230225"></a>You cannot query images when the value is set to <strong id="en-us_topic_0057973086_b121112552364"><a name="en-us_topic_0057973086_b121112552364"></a><a name="en-us_topic_0057973086_b121112552364"></a>deleted</strong>. The value varies depending on the status in Glance. <a href="#en-us_topic_0057973086_table8522092203758">Table 3</a> shows the mapping of image statuses in Nova and Glance.</p>
</td>
</tr>
<tr id="en-us_topic_0057973086_row53719602"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973086_p56320469"><a name="en-us_topic_0057973086_p56320469"></a><a name="en-us_topic_0057973086_p56320469"></a>changes-since</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.2 "><p id="p762813147233"><a name="p762813147233"></a><a name="p762813147233"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973086_p65664178"><a name="en-us_topic_0057973086_p65664178"></a><a name="en-us_topic_0057973086_p65664178"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973086_p50876212"><a name="en-us_topic_0057973086_p50876212"></a><a name="en-us_topic_0057973086_p50876212"></a>Specifies the images modified after the <strong id="en-us_topic_0057973086_b42863276"><a name="en-us_topic_0057973086_b42863276"></a><a name="en-us_topic_0057973086_b42863276"></a>changes-since</strong> time point. The parameter is in ISO 8601 time format, for example, 2013-06-09T06:42:18Z.</p>
</td>
</tr>
<tr id="en-us_topic_0057973086_row55232730"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973086_p44666111"><a name="en-us_topic_0057973086_p44666111"></a><a name="en-us_topic_0057973086_p44666111"></a>minRam</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.2 "><p id="p12628161412238"><a name="p12628161412238"></a><a name="p12628161412238"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973086_p61185216"><a name="en-us_topic_0057973086_p61185216"></a><a name="en-us_topic_0057973086_p61185216"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973086_p58092345"><a name="en-us_topic_0057973086_p58092345"></a><a name="en-us_topic_0057973086_p58092345"></a>Specifies the minimum memory size in MB required by the image.</p>
</td>
</tr>
<tr id="en-us_topic_0057973086_row53069063"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973086_p3626823"><a name="en-us_topic_0057973086_p3626823"></a><a name="en-us_topic_0057973086_p3626823"></a>minDisk</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.5.1.2 "><p id="p0629201415236"><a name="p0629201415236"></a><a name="p0629201415236"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973086_p25337256"><a name="en-us_topic_0057973086_p25337256"></a><a name="en-us_topic_0057973086_p25337256"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973086_p9083883"><a name="en-us_topic_0057973086_p9083883"></a><a name="en-us_topic_0057973086_p9083883"></a>Specifies the minimum disk size in GB required by the image.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Mapping relationship of image status in Nova and Glance

<a name="en-us_topic_0057973086_table8522092203758"></a>
<table><thead align="left"><tr id="en-us_topic_0057973086_row13340309203758"><th class="cellrowborder" valign="top" width="41.54%" id="mcps1.2.3.1.1"><p id="en-us_topic_0057973086_p46945536203839"><a name="en-us_topic_0057973086_p46945536203839"></a><a name="en-us_topic_0057973086_p46945536203839"></a>Image Status in Glance</p>
</th>
<th class="cellrowborder" valign="top" width="58.46%" id="mcps1.2.3.1.2"><p id="en-us_topic_0057973086_p44492049203839"><a name="en-us_topic_0057973086_p44492049203839"></a><a name="en-us_topic_0057973086_p44492049203839"></a>Image Status in Nova</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973086_row5835335203758"><td class="cellrowborder" valign="top" width="41.54%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0057973086_p21123048203839"><a name="en-us_topic_0057973086_p21123048203839"></a><a name="en-us_topic_0057973086_p21123048203839"></a>queued</p>
</td>
<td class="cellrowborder" valign="top" width="58.46%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0057973086_p33245312203839"><a name="en-us_topic_0057973086_p33245312203839"></a><a name="en-us_topic_0057973086_p33245312203839"></a>saving</p>
</td>
</tr>
<tr id="en-us_topic_0057973086_row33831195203758"><td class="cellrowborder" valign="top" width="41.54%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0057973086_p9532693203839"><a name="en-us_topic_0057973086_p9532693203839"></a><a name="en-us_topic_0057973086_p9532693203839"></a>saving</p>
</td>
<td class="cellrowborder" valign="top" width="58.46%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0057973086_p33950669203839"><a name="en-us_topic_0057973086_p33950669203839"></a><a name="en-us_topic_0057973086_p33950669203839"></a>saving</p>
</td>
</tr>
<tr id="en-us_topic_0057973086_row1617173203758"><td class="cellrowborder" valign="top" width="41.54%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0057973086_p53976228203839"><a name="en-us_topic_0057973086_p53976228203839"></a><a name="en-us_topic_0057973086_p53976228203839"></a>active</p>
</td>
<td class="cellrowborder" valign="top" width="58.46%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0057973086_p9998375203839"><a name="en-us_topic_0057973086_p9998375203839"></a><a name="en-us_topic_0057973086_p9998375203839"></a>active</p>
</td>
</tr>
<tr id="en-us_topic_0057973086_row63643984203758"><td class="cellrowborder" valign="top" width="41.54%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0057973086_p41058235203839"><a name="en-us_topic_0057973086_p41058235203839"></a><a name="en-us_topic_0057973086_p41058235203839"></a>deleted</p>
</td>
<td class="cellrowborder" valign="top" width="58.46%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0057973086_p37382721203839"><a name="en-us_topic_0057973086_p37382721203839"></a><a name="en-us_topic_0057973086_p37382721203839"></a>deleted</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section333218375418"></a>

None

## Response<a name="en-us_topic_0057973086_section21690089"></a>

[Table 4](#en-us_topic_0057973086_table45482640)  describes the response parameters.

**Table  4**  Response parameters

<a name="en-us_topic_0057973086_table45482640"></a>
<table><thead align="left"><tr id="en-us_topic_0057973086_row18065916"><th class="cellrowborder" valign="top" width="19.191919191919194%" id="mcps1.2.5.1.1"><p id="en-us_topic_0057973086_p54053121"><a name="en-us_topic_0057973086_p54053121"></a><a name="en-us_topic_0057973086_p54053121"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.191919191919194%" id="mcps1.2.5.1.2"><p id="en-us_topic_0057973086_p39294541"><a name="en-us_topic_0057973086_p39294541"></a><a name="en-us_topic_0057973086_p39294541"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="22.222222222222225%" id="mcps1.2.5.1.3"><p id="en-us_topic_0057973086_p16226703"><a name="en-us_topic_0057973086_p16226703"></a><a name="en-us_topic_0057973086_p16226703"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="39.3939393939394%" id="mcps1.2.5.1.4"><p id="en-us_topic_0057973086_p28741219"><a name="en-us_topic_0057973086_p28741219"></a><a name="en-us_topic_0057973086_p28741219"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973086_row46337402"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973086_p62342073"><a name="en-us_topic_0057973086_p62342073"></a><a name="en-us_topic_0057973086_p62342073"></a>images</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057973086_p64928978"><a name="en-us_topic_0057973086_p64928978"></a><a name="en-us_topic_0057973086_p64928978"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973086_p16543177"><a name="en-us_topic_0057973086_p16543177"></a><a name="en-us_topic_0057973086_p16543177"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="39.3939393939394%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973086_p24755835"><a name="en-us_topic_0057973086_p24755835"></a><a name="en-us_topic_0057973086_p24755835"></a>Specifies the image information.</p>
</td>
</tr>
<tr id="en-us_topic_0057973086_row21475923"><td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973086_p61828175"><a name="en-us_topic_0057973086_p61828175"></a><a name="en-us_topic_0057973086_p61828175"></a>images_links</p>
</td>
<td class="cellrowborder" valign="top" width="19.191919191919194%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057973086_p48687502"><a name="en-us_topic_0057973086_p48687502"></a><a name="en-us_topic_0057973086_p48687502"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="22.222222222222225%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972661_p11990221102658"><a name="en-us_topic_0057972661_p11990221102658"></a><a name="en-us_topic_0057972661_p11990221102658"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="39.3939393939394%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973086_p51373600"><a name="en-us_topic_0057973086_p51373600"></a><a name="en-us_topic_0057973086_p51373600"></a>Specifies the information about the next page when you query images in pages.</p>
</td>
</tr>
</tbody>
</table>

**Table  5** **images**  information

<a name="en-us_topic_0057973086_table512095"></a>
<table><thead align="left"><tr id="en-us_topic_0057973086_row64402537"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.1"><p id="p54273401584"><a name="p54273401584"></a><a name="p54273401584"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.5.1.2"><p id="p74271940125814"><a name="p74271940125814"></a><a name="p74271940125814"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="22%" id="mcps1.2.5.1.3"><p id="p144271405585"><a name="p144271405585"></a><a name="p144271405585"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="39%" id="mcps1.2.5.1.4"><p id="p17427174011580"><a name="p17427174011580"></a><a name="p17427174011580"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973086_row60927756"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973086_p36201180"><a name="en-us_topic_0057973086_p36201180"></a><a name="en-us_topic_0057973086_p36201180"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057973086_p17676294"><a name="en-us_topic_0057973086_p17676294"></a><a name="en-us_topic_0057973086_p17676294"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973086_p46614477"><a name="en-us_topic_0057973086_p46614477"></a><a name="en-us_topic_0057973086_p46614477"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973086_p22493744"><a name="en-us_topic_0057973086_p22493744"></a><a name="en-us_topic_0057973086_p22493744"></a>Specifies the image ID in UUID format.</p>
</td>
</tr>
<tr id="en-us_topic_0057973086_row1117111"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973086_p23377165"><a name="en-us_topic_0057973086_p23377165"></a><a name="en-us_topic_0057973086_p23377165"></a>links</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057973086_p33826157"><a name="en-us_topic_0057973086_p33826157"></a><a name="en-us_topic_0057973086_p33826157"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973086_p14502183"><a name="en-us_topic_0057973086_p14502183"></a><a name="en-us_topic_0057973086_p14502183"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="39%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973086_p55564233"><a name="en-us_topic_0057973086_p55564233"></a><a name="en-us_topic_0057973086_p55564233"></a>Specifies the shortcut link of the image.</p>
</td>
</tr>
<tr id="en-us_topic_0057973086_row30316049"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973086_p39680934"><a name="en-us_topic_0057973086_p39680934"></a><a name="en-us_topic_0057973086_p39680934"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057973086_p31329554"><a name="en-us_topic_0057973086_p31329554"></a><a name="en-us_topic_0057973086_p31329554"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973086_p60039108"><a name="en-us_topic_0057973086_p60039108"></a><a name="en-us_topic_0057973086_p60039108"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973086_p54665912"><a name="en-us_topic_0057973086_p54665912"></a><a name="en-us_topic_0057973086_p54665912"></a>Specifies the image name.</p>
</td>
</tr>
</tbody>
</table>

**Table  6** **images\_links**  parameters

<a name="en-us_topic_0057973086_table65862751"></a>
<table><thead align="left"><tr id="en-us_topic_0057973086_row21566624"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.1"><p id="p12843114319589"><a name="p12843114319589"></a><a name="p12843114319589"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.2"><p id="p14859114355811"><a name="p14859114355811"></a><a name="p14859114355811"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.3"><p id="p0859343135810"><a name="p0859343135810"></a><a name="p0859343135810"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="44%" id="mcps1.2.5.1.4"><p id="p10859164395813"><a name="p10859164395813"></a><a name="p10859164395813"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973086_row7960749"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973086_p40840956"><a name="en-us_topic_0057973086_p40840956"></a><a name="en-us_topic_0057973086_p40840956"></a>href</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057973086_p58930111"><a name="en-us_topic_0057973086_p58930111"></a><a name="en-us_topic_0057973086_p58930111"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973086_p19783135"><a name="en-us_topic_0057973086_p19783135"></a><a name="en-us_topic_0057973086_p19783135"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973086_p8609667"><a name="en-us_topic_0057973086_p8609667"></a><a name="en-us_topic_0057973086_p8609667"></a>Specifies the URL of the next page when you query images in pages.</p>
</td>
</tr>
<tr id="en-us_topic_0057973086_row10378142"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973086_p35323188"><a name="en-us_topic_0057973086_p35323188"></a><a name="en-us_topic_0057973086_p35323188"></a>rel</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057973086_p28532881"><a name="en-us_topic_0057973086_p28532881"></a><a name="en-us_topic_0057973086_p28532881"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973086_p42605986"><a name="en-us_topic_0057973086_p42605986"></a><a name="en-us_topic_0057973086_p42605986"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973086_p29462057"><a name="en-us_topic_0057973086_p29462057"></a><a name="en-us_topic_0057973086_p29462057"></a>Specifies the query direction when you query images in pages.</p>
</td>
</tr>
</tbody>
</table>

**Table  7** **links**  parameter description

<a name="en-us_topic_0057973086_table1949017543515"></a>
<table><thead align="left"><tr id="en-us_topic_0057973086_row54901254195115"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.1"><p id="p131661047125817"><a name="p131661047125817"></a><a name="p131661047125817"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.5.1.2"><p id="p15166194715818"><a name="p15166194715818"></a><a name="p15166194715818"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.3"><p id="p10166194719587"><a name="p10166194719587"></a><a name="p10166194719587"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="44%" id="mcps1.2.5.1.4"><p id="p91661478589"><a name="p91661478589"></a><a name="p91661478589"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973086_row1549185415113"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973086_p1449195414513"><a name="en-us_topic_0057973086_p1449195414513"></a><a name="en-us_topic_0057973086_p1449195414513"></a>href</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057973086_p1449195455118"><a name="en-us_topic_0057973086_p1449195455118"></a><a name="en-us_topic_0057973086_p1449195455118"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973086_p449195425114"><a name="en-us_topic_0057973086_p449195425114"></a><a name="en-us_topic_0057973086_p449195425114"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973086_p18491754135111"><a name="en-us_topic_0057973086_p18491754135111"></a><a name="en-us_topic_0057973086_p18491754135111"></a>Specifies the link of the corresponding resource.</p>
</td>
</tr>
<tr id="en-us_topic_0057973086_row16491145435118"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973086_p4491155415518"><a name="en-us_topic_0057973086_p4491155415518"></a><a name="en-us_topic_0057973086_p4491155415518"></a>rel</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057973086_p2491185485110"><a name="en-us_topic_0057973086_p2491185485110"></a><a name="en-us_topic_0057973086_p2491185485110"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973086_p1449165411514"><a name="en-us_topic_0057973086_p1449165411514"></a><a name="en-us_topic_0057973086_p1449165411514"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973086_p44540131181624"><a name="en-us_topic_0057973086_p44540131181624"></a><a name="en-us_topic_0057973086_p44540131181624"></a>The value can be:</p>
<a name="en-us_topic_0057973086_ul50320171175059"></a><a name="en-us_topic_0057973086_ul50320171175059"></a><ul id="en-us_topic_0057973086_ul50320171175059"><li><strong id="b11003816175111"><a name="b11003816175111"></a><a name="b11003816175111"></a>self</strong>: A self link contains a version link to the resource. Use these links when the link is followed immediately.</li><li><strong id="b60630642175154"><a name="b60630642175154"></a><a name="b60630642175154"></a>bookmark</strong>: A bookmark link provides a permanent link to a resource, which is suitable for long term storage.</li><li><strong id="b28772520175321"><a name="b28772520175321"></a><a name="b28772520175321"></a>alternate</strong>: An alternate link can contain an alternate representation of the resource. For example, an OpenStack Compute image may have an alternate representation in the OpenStack image service.</li></ul>
</td>
</tr>
<tr id="en-us_topic_0057973086_row15491195465112"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057973086_p149145411510"><a name="en-us_topic_0057973086_p149145411510"></a><a name="en-us_topic_0057973086_p149145411510"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057973086_p1949195405118"><a name="en-us_topic_0057973086_p1949195405118"></a><a name="en-us_topic_0057973086_p1949195405118"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057973086_p649155425114"><a name="en-us_topic_0057973086_p649155425114"></a><a name="en-us_topic_0057973086_p649155425114"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057973086_p1671811201581"><a name="en-us_topic_0057973086_p1671811201581"></a><a name="en-us_topic_0057973086_p1671811201581"></a>The type attribute provides a hint as to the type of representation to expect when following the link.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="en-us_topic_0057973086_section60993073"></a>

```
GET https://{endpoint}/v2/9c53a566cb3443ab910cf0daebca90c4/images
GET https://{endpoint}/v2.1/9c53a566cb3443ab910cf0daebca90c4/images
```

## Example Response<a name="section1857017201151"></a>

```
{
    "images": [
        {
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
            "name": "image1"
        }
    ]
}
```

## Returned Values<a name="en-us_topic_0057973086_section41491842"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).


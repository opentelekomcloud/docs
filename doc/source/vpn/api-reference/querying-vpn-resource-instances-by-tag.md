# Querying VPN Resource Instances by Tag<a name="en_topic_0093011484"></a>

## **Function**<a name="section25709437"></a>

This interface is used to query VPN resource instances by tag.

Tag Management Service \(TMS\) uses this API to filter out service resources and display them in a list. These services must have the query capabilities.

## URI<a name="section30058349"></a>

POST /v2.0/\{project\_id\}/ipsec-site-connections/resource\_instances/action

## Request Message<a name="section23101291384"></a>

[Table 1](#table45111823181914)  describes the request parameters.

**Table  1**  Request parameters

<a name="table45111823181914"></a>
<table><thead align="left"><tr id="row88521623101920"><th class="cellrowborder" valign="top" width="13.861386138613863%" id="mcps1.2.5.1.1"><p id="p168521123141913"><a name="p168521123141913"></a><a name="p168521123141913"></a><strong id="b842352706172115"><a name="b842352706172115"></a><a name="b842352706172115"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="10.891089108910892%" id="mcps1.2.5.1.2"><p id="p68525234198"><a name="p68525234198"></a><a name="p68525234198"></a><strong id="b84235270610412"><a name="b84235270610412"></a><a name="b84235270610412"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.82178217821782%" id="mcps1.2.5.1.3"><p id="p68524237196"><a name="p68524237196"></a><a name="p68524237196"></a><strong id="b8423527061798"><a name="b8423527061798"></a><a name="b8423527061798"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="57.42574257425742%" id="mcps1.2.5.1.4"><p id="p1785232391916"><a name="p1785232391916"></a><a name="p1785232391916"></a><strong id="b842352706151625"><a name="b842352706151625"></a><a name="b842352706151625"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row9852172316195"><td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.1 "><p id="p38521123191911"><a name="p38521123191911"></a><a name="p38521123191911"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.2.5.1.2 "><p id="p198521723191910"><a name="p198521723191910"></a><a name="p198521723191910"></a>List&lt;tag&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.5.1.3 "><p id="p15852102341915"><a name="p15852102341915"></a><a name="p15852102341915"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="57.42574257425742%" headers="mcps1.2.5.1.4 "><p id="p1885242381910"><a name="p1885242381910"></a><a name="p1885242381910"></a>Specifies the included tags. Each tag contains a maximum of 10 keys, and each key contains a maximum of 10 values. The structure body cannot be missing, and the key cannot be left blank or set to an empty string. Each tag key must be unique, and each tag value in a tag must be unique.</p>
</td>
</tr>
<tr id="row485202331911"><td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.1 "><p id="p08523237195"><a name="p08523237195"></a><a name="p08523237195"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.2.5.1.2 "><p id="p1285218232197"><a name="p1285218232197"></a><a name="p1285218232197"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.5.1.3 "><p id="p1985292314197"><a name="p1985292314197"></a><a name="p1985292314197"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="57.42574257425742%" headers="mcps1.2.5.1.4 "><p id="p13852152341914"><a name="p13852152341914"></a><a name="p13852152341914"></a>Sets the page size. This parameter is not available when <strong id="b842352706112419"><a name="b842352706112419"></a><a name="b842352706112419"></a>action</strong> is set to <strong id="b842352706112428"><a name="b842352706112428"></a><a name="b842352706112428"></a>count</strong>. The default value is <strong id="b842352706112654"><a name="b842352706112654"></a><a name="b842352706112654"></a>1000</strong> when <strong id="b39236199214364"><a name="b39236199214364"></a><a name="b39236199214364"></a>action</strong> is set to <strong id="b132640505514364"><a name="b132640505514364"></a><a name="b132640505514364"></a>filter</strong>. The maximum value is <strong id="b842352706112658"><a name="b842352706112658"></a><a name="b842352706112658"></a>1000</strong>, and the minimum value is <strong id="b842352706112710"><a name="b842352706112710"></a><a name="b842352706112710"></a>1</strong>. The value cannot be a negative number.</p>
</td>
</tr>
<tr id="row14852423111914"><td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.1 "><p id="p885219237198"><a name="p885219237198"></a><a name="p885219237198"></a>offset</p>
</td>
<td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.2.5.1.2 "><p id="p1985218237191"><a name="p1985218237191"></a><a name="p1985218237191"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.5.1.3 "><p id="p5852132317199"><a name="p5852132317199"></a><a name="p5852132317199"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="57.42574257425742%" headers="mcps1.2.5.1.4 "><p id="p1785342311917"><a name="p1785342311917"></a><a name="p1785342311917"></a>Specifies the index position. The query starts from the next piece of data indexed by this parameter. This parameter is not required when you query data on the first page. The value in the response returned for querying data on the previous page will be included in this parameter for querying data on subsequent pages. This parameter is not available when <strong id="b84235270621521"><a name="b84235270621521"></a><a name="b84235270621521"></a>action</strong> is set to <strong id="b84235270621525"><a name="b84235270621525"></a><a name="b84235270621525"></a>count</strong>. If <strong id="b84235270621528"><a name="b84235270621528"></a><a name="b84235270621528"></a>action</strong> is set to <strong id="b84235270621532"><a name="b84235270621532"></a><a name="b84235270621532"></a>filter</strong>, the value must be a number, and the default value is <strong id="b84235270621539"><a name="b84235270621539"></a><a name="b84235270621539"></a>0</strong>. The value cannot be a negative number.</p>
</td>
</tr>
<tr id="row28531123181913"><td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.1 "><p id="p1853123121912"><a name="p1853123121912"></a><a name="p1853123121912"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.2.5.1.2 "><p id="p14853122371914"><a name="p14853122371914"></a><a name="p14853122371914"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.5.1.3 "><p id="p17853152331919"><a name="p17853152331919"></a><a name="p17853152331919"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="57.42574257425742%" headers="mcps1.2.5.1.4 "><p id="p6853182320190"><a name="p6853182320190"></a><a name="p6853182320190"></a>Specifies the operation to perform. The value can only be <strong id="b842352706145527"><a name="b842352706145527"></a><a name="b842352706145527"></a>filter</strong> (filtering) or <strong id="b842352706145557"><a name="b842352706145557"></a><a name="b842352706145557"></a>count</strong> (querying the total number).</p>
<p id="p1185332315194"><a name="p1185332315194"></a><a name="p1185332315194"></a>The value <strong id="b842352706112921"><a name="b842352706112921"></a><a name="b842352706112921"></a>filter</strong> indicates pagination query. The value <strong id="b84235270611312"><a name="b84235270611312"></a><a name="b84235270611312"></a>count</strong> indicates that the total number of query results meeting the search criteria will be returned.</p>
</td>
</tr>
<tr id="row1885318232195"><td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.1 "><p id="p085315232194"><a name="p085315232194"></a><a name="p085315232194"></a>matches</p>
</td>
<td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.2.5.1.2 "><p id="p16853023111917"><a name="p16853023111917"></a><a name="p16853023111917"></a>List&lt;match&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.5.1.3 "><p id="p18853102313197"><a name="p18853102313197"></a><a name="p18853102313197"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="57.42574257425742%" headers="mcps1.2.5.1.4 "><p id="p128537230197"><a name="p128537230197"></a><a name="p128537230197"></a>Specifies the search criteria. The tag key is the field to match. Currently, only <strong id="b84235270615351"><a name="b84235270615351"></a><a name="b84235270615351"></a>resource_name</strong> is supported. The tag value indicates the value to be matched. The <strong id="b10991315962239"><a name="b10991315962239"></a><a name="b10991315962239"></a>key</strong> field is a fixed dictionary value.</p>
</td>
</tr>
</tbody>
</table>

-   Description of field  **tag**

<a name="table1548032316199"></a>
<table><thead align="left"><tr id="row1785310237196"><th class="cellrowborder" valign="top" width="31.626837316268368%" id="mcps1.1.5.1.1"><p id="p185312312192"><a name="p185312312192"></a><a name="p185312312192"></a><strong id="b84235270617246"><a name="b84235270617246"></a><a name="b84235270617246"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885708%" id="mcps1.1.5.1.2"><p id="p208531923101913"><a name="p208531923101913"></a><a name="p208531923101913"></a><strong id="b638771301"><a name="b638771301"></a><a name="b638771301"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885708%" id="mcps1.1.5.1.3"><p id="p685312311196"><a name="p685312311196"></a><a name="p685312311196"></a><strong id="b1014822031"><a name="b1014822031"></a><a name="b1014822031"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.1.5.1.4"><p id="p4853122311199"><a name="p4853122311199"></a><a name="p4853122311199"></a><strong id="b852492472"><a name="b852492472"></a><a name="b852492472"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row08532238197"><td class="cellrowborder" valign="top" width="31.626837316268368%" headers="mcps1.1.5.1.1 "><p id="p16854122312191"><a name="p16854122312191"></a><a name="p16854122312191"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885708%" headers="mcps1.1.5.1.2 "><p id="p167509961911"><a name="p167509961911"></a><a name="p167509961911"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885708%" headers="mcps1.1.5.1.3 "><p id="p5854122371919"><a name="p5854122371919"></a><a name="p5854122371919"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.1.5.1.4 "><p id="p085432316193"><a name="p085432316193"></a><a name="p085432316193"></a>Specifies the tag key. It contains a maximum of 127 Unicode characters. It cannot be left blank. (This parameter is not verified in the search process.)</p>
</td>
</tr>
<tr id="row15854623141911"><td class="cellrowborder" valign="top" width="31.626837316268368%" headers="mcps1.1.5.1.1 "><p id="p68541223141919"><a name="p68541223141919"></a><a name="p68541223141919"></a>values</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885708%" headers="mcps1.1.5.1.2 "><p id="p838119133192"><a name="p838119133192"></a><a name="p838119133192"></a>List&lt;String&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885708%" headers="mcps1.1.5.1.3 "><p id="p188541423181914"><a name="p188541423181914"></a><a name="p188541423181914"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.1.5.1.4 "><p id="p198541623121914"><a name="p198541623121914"></a><a name="p198541623121914"></a>Specifies the tag value list. Each value can contain a maximum of 255 Unicode characters. An empty list for <strong id="b842352706151018"><a name="b842352706151018"></a><a name="b842352706151018"></a>values</strong> indicates any value. The resources containing one or more values listed in <strong id="b84235270619578"><a name="b84235270619578"></a><a name="b84235270619578"></a>values</strong> will be found and displayed.</p>
</td>
</tr>
</tbody>
</table>

-   Description of field  **match**

<a name="table13731215298"></a>
<table><thead align="left"><tr id="row1836752192916"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.5.1.1"><p id="p836712211290"><a name="p836712211290"></a><a name="p836712211290"></a><strong id="b1600468818"><a name="b1600468818"></a><a name="b1600468818"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="13.13131313131313%" id="mcps1.1.5.1.2"><p id="p185201217172010"><a name="p185201217172010"></a><a name="p185201217172010"></a><strong>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.14141414141414%" id="mcps1.1.5.1.3"><p id="p8367424292"><a name="p8367424292"></a><a name="p8367424292"></a><strong id="b2122021134"><a name="b2122021134"></a><a name="b2122021134"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.39393939393939%" id="mcps1.1.5.1.4"><p id="p103671626297"><a name="p103671626297"></a><a name="p103671626297"></a><strong id="b114777541"><a name="b114777541"></a><a name="b114777541"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row123691521298"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.5.1.1 "><p id="p1136914292918"><a name="p1136914292918"></a><a name="p1136914292918"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.5.1.2 "><p id="p132326387201"><a name="p132326387201"></a><a name="p132326387201"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.1.5.1.3 "><p id="p13692242912"><a name="p13692242912"></a><a name="p13692242912"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="39.39393939393939%" headers="mcps1.1.5.1.4 "><p id="p936962102919"><a name="p936962102919"></a><a name="p936962102919"></a>Specifies the tag key. Currently, the tag key can only be the resource name.</p>
</td>
</tr>
<tr id="row18373132182918"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.5.1.1 "><p id="p16369329291"><a name="p16369329291"></a><a name="p16369329291"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.1.5.1.2 "><p id="p1213719405202"><a name="p1213719405202"></a><a name="p1213719405202"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.1.5.1.3 "><p id="p1137312212917"><a name="p1137312212917"></a><a name="p1137312212917"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="39.39393939393939%" headers="mcps1.1.5.1.4 "><p id="p11373102182916"><a name="p11373102182916"></a><a name="p11373102182916"></a>Specifies the tag value. Each value can contain a maximum of 255 Unicode characters.</p>
</td>
</tr>
</tbody>
</table>

## Response Parameter<a name="section95436234191"></a>

[Table 2](#table1135702419184)  describes the response parameters.

**Table  2**  Response Parameter

<a name="table1135702419184"></a>
<table><thead align="left"></thead>
<tbody></tbody>
</table>

<a name="table669961372515"></a>
<table><thead align="left"><tr id="row689311382512"><th class="cellrowborder" valign="top" width="28.000000000000004%" id="mcps1.1.4.1.1"><p id="p11893151312516"><a name="p11893151312516"></a><a name="p11893151312516"></a><strong id="b525762354"><a name="b525762354"></a><a name="b525762354"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="37.330000000000005%" id="mcps1.1.4.1.2"><p id="p1789361319251"><a name="p1789361319251"></a><a name="p1789361319251"></a><strong id="b1923039965"><a name="b1923039965"></a><a name="b1923039965"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="34.67%" id="mcps1.1.4.1.3"><p id="p19893131310258"><a name="p19893131310258"></a><a name="p19893131310258"></a><strong id="b1263216195"><a name="b1263216195"></a><a name="b1263216195"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row7893201315255"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.1.4.1.1 "><p id="p889311310255"><a name="p889311310255"></a><a name="p889311310255"></a>resources</p>
</td>
<td class="cellrowborder" valign="top" width="37.330000000000005%" headers="mcps1.1.4.1.2 "><p id="p989313131254"><a name="p989313131254"></a><a name="p989313131254"></a>List&lt;resource&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="34.67%" headers="mcps1.1.4.1.3 "><p id="p1893111313258"><a name="p1893111313258"></a><a name="p1893111313258"></a>N/A</p>
</td>
</tr>
<tr id="row1989331314259"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.1.4.1.1 "><p id="p158931313152513"><a name="p158931313152513"></a><a name="p158931313152513"></a>total_count</p>
</td>
<td class="cellrowborder" valign="top" width="37.330000000000005%" headers="mcps1.1.4.1.2 "><p id="p58931113112511"><a name="p58931113112511"></a><a name="p58931113112511"></a>int</p>
</td>
<td class="cellrowborder" valign="top" width="34.67%" headers="mcps1.1.4.1.3 "><p id="p10893121312258"><a name="p10893121312258"></a><a name="p10893121312258"></a>Specifies the total number of records.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Description of field  **resource**

<a name="table15678313132518"></a>
<table><thead align="left"><tr id="row14893181314253"><th class="cellrowborder" valign="top" width="28.000000000000004%" id="mcps1.2.4.1.1"><p id="p1889361320250"><a name="p1889361320250"></a><a name="p1889361320250"></a><strong id="b1772434113716"><a name="b1772434113716"></a><a name="b1772434113716"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="37.330000000000005%" id="mcps1.2.4.1.2"><p id="p8893161342512"><a name="p8893161342512"></a><a name="p8893161342512"></a><strong id="b1667894219717"><a name="b1667894219717"></a><a name="b1667894219717"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="34.67%" id="mcps1.2.4.1.3"><p id="p3894151362514"><a name="p3894151362514"></a><a name="p3894151362514"></a><strong id="b664217431575"><a name="b664217431575"></a><a name="b664217431575"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row389421332512"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p1289461362516"><a name="p1289461362516"></a><a name="p1289461362516"></a>resource_id</p>
</td>
<td class="cellrowborder" valign="top" width="37.330000000000005%" headers="mcps1.2.4.1.2 "><p id="p13894111322519"><a name="p13894111322519"></a><a name="p13894111322519"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="34.67%" headers="mcps1.2.4.1.3 "><p id="p589451313259"><a name="p589451313259"></a><a name="p589451313259"></a>Specifies the resource ID.</p>
</td>
</tr>
<tr id="row12894213172511"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p11894181312514"><a name="p11894181312514"></a><a name="p11894181312514"></a>resouce_detail</p>
</td>
<td class="cellrowborder" valign="top" width="37.330000000000005%" headers="mcps1.2.4.1.2 "><p id="p6894121314259"><a name="p6894121314259"></a><a name="p6894121314259"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="34.67%" headers="mcps1.2.4.1.3 "><p id="p14894181315254"><a name="p14894181315254"></a><a name="p14894181315254"></a>Specifies the resource details. The value is a resource object, used for extension. This parameter is left blank by default.</p>
</td>
</tr>
<tr id="row1189431342514"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p58945135256"><a name="p58945135256"></a><a name="p58945135256"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="37.330000000000005%" headers="mcps1.2.4.1.2 "><p id="p8894813142516"><a name="p8894813142516"></a><a name="p8894813142516"></a>List&lt;resource_tag&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="34.67%" headers="mcps1.2.4.1.3 "><p id="p188941913122519"><a name="p188941913122519"></a><a name="p188941913122519"></a>Specifies the tag list. This parameter is an empty array by default if there is no tag.</p>
</td>
</tr>
<tr id="row889451315256"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p188943136256"><a name="p188943136256"></a><a name="p188943136256"></a>resource_name</p>
</td>
<td class="cellrowborder" valign="top" width="37.330000000000005%" headers="mcps1.2.4.1.2 "><p id="p2894191372516"><a name="p2894191372516"></a><a name="p2894191372516"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="34.67%" headers="mcps1.2.4.1.3 "><p id="p3894141342514"><a name="p3894141342514"></a><a name="p3894141342514"></a>Specifies the resource name. This parameter is an empty string by default if there is no resource name.</p>
</td>
</tr>
</tbody>
</table>

## Example<a name="section107702427334"></a>

-   Request Example

    ```
    POST /v2.0/{project_id}/ipsec-site-connections/resource_instances/action
    ```

-   Request Body

    -   Request body when  **action**  is set to  **filter**

    ```
    {
        "offset": "0",
        "limit": "100",
        "action": "filter",
        "matches": [
            {
                "key": "resource_name",
                "value": "resource1"
            }
        ],
        "tags": [
            {
                "key": "key1",
                "values": [
                    "*value1",
                    "value2"
                ]
            }
        ]
    }
    ```

    -   Request body when  **action**  is set to  **count**

    ```
    {
        "action": "count",
        "tags": [
            {
                "key": "key1",
                "values": [
                    "value1",
                    "value2"
                ]
            },
            {
                "key": "key2",
                "values": [
                    "value1",
                    "value2"
                ]
            }
        ],
        "matches": [
            {
                "key": "resource_name",
                "value": "resource1"
            }
        ]
    }
    ```

-   Example Response

    -   Response body when  **action**  is set to  **filter**

    ```
    { 
          "resources": [
             {
                "resource_detail": null, 
                "resource_id": "cdfs_cefs_wesas_12_dsad", 
                "resource_name": "resouece1", 
                "tags": [
                    {
                       "key": "key1",
                       "value": "value1"
                    },
                    {
                       "key": "key2",
                       "value": "value1"
                    }
                 ]
             }
           ], 
          "total_count": 1000
    }
     
    ```

    -   Response body when  **action**  is set to  **count**

    ```
    {
           "total_count": 1000
    }
    ```



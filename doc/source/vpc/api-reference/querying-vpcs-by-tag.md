# Querying VPCs by Tag<a name="vpc_tag_0005"></a>

## Function<a name="section046482318191"></a>

This API is used to query VPCs by tag.

## URI<a name="section204655230197"></a>

POST /v2.0/\{project\_id\}/vpcs/resource\_instances/action

[Table 1](#table27380479)  describes the parameters.

**Table  1**  Parameter description

<a name="table27380479"></a>
<table><thead align="left"><tr id="row28751554"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p47174532"><a name="p47174532"></a><a name="p47174532"></a><strong id="b2817144585920"><a name="b2817144585920"></a><a name="b2817144585920"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p63040734"><a name="p63040734"></a><a name="p63040734"></a><strong id="b2071411517598"><a name="b2071411517598"></a><a name="b2071411517598"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p6025849"><a name="p6025849"></a><a name="p6025849"></a><strong id="b74161954205918"><a name="b74161954205918"></a><a name="b74161954205918"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row18331773"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p8478608"><a name="p8478608"></a><a name="p8478608"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p15678685"><a name="p15678685"></a><a name="p15678685"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section747562331920"></a>

Request parameter

**Table  2**  Request parameter

<a name="table45111823181914"></a>
<table><thead align="left"><tr id="row88521623101920"><th class="cellrowborder" valign="top" width="13.861386138613863%" id="mcps1.2.5.1.1"><p id="p168521123141913"><a name="p168521123141913"></a><a name="p168521123141913"></a><strong id="b842352706193648"><a name="b842352706193648"></a><a name="b842352706193648"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="10.891089108910892%" id="mcps1.2.5.1.2"><p id="p68525234198"><a name="p68525234198"></a><a name="p68525234198"></a><strong id="b842352706193653"><a name="b842352706193653"></a><a name="b842352706193653"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="17.82178217821782%" id="mcps1.2.5.1.3"><p id="p68524237196"><a name="p68524237196"></a><a name="p68524237196"></a><strong id="b125816211302"><a name="b125816211302"></a><a name="b125816211302"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="57.42574257425742%" id="mcps1.2.5.1.4"><p id="p1785232391916"><a name="p1785232391916"></a><a name="p1785232391916"></a><strong id="b8423527061645"><a name="b8423527061645"></a><a name="b8423527061645"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row9852172316195"><td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.1 "><p id="p38521123191911"><a name="p38521123191911"></a><a name="p38521123191911"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.2.5.1.2 "><p id="p10424324181820"><a name="p10424324181820"></a><a name="p10424324181820"></a>Array of <a href="#table1548032316199">tag</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.5.1.3 "><p id="p15852102341915"><a name="p15852102341915"></a><a name="p15852102341915"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="57.42574257425742%" headers="mcps1.2.5.1.4 "><p id="p1885242381910"><a name="p1885242381910"></a><a name="p1885242381910"></a>Specifies the included tags. A maximum of 10 tag keys are allowed for each query operation. Each tag key can have up to 10 tag values. The structure body must be included. The tag key cannot be left blank or set to an empty string. Each tag key must be unique, and each tag value in a tag must be unique.</p>
</td>
</tr>
<tr id="row485202331911"><td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.1 "><p id="p08523237195"><a name="p08523237195"></a><a name="p08523237195"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.2.5.1.2 "><p id="p1285218232197"><a name="p1285218232197"></a><a name="p1285218232197"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.5.1.3 "><p id="p1985292314197"><a name="p1985292314197"></a><a name="p1985292314197"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="57.42574257425742%" headers="mcps1.2.5.1.4 "><p id="p13852152341914"><a name="p13852152341914"></a><a name="p13852152341914"></a>Sets the page size. This parameter is not available when <strong id="b842352706112419"><a name="b842352706112419"></a><a name="b842352706112419"></a>action</strong> is set to <strong id="b842352706112428"><a name="b842352706112428"></a><a name="b842352706112428"></a>count</strong>. The default value is <strong id="b842352706112654"><a name="b842352706112654"></a><a name="b842352706112654"></a>1000</strong> when <strong id="b39236199214364"><a name="b39236199214364"></a><a name="b39236199214364"></a>action</strong> is set to <strong id="b132640505514364"><a name="b132640505514364"></a><a name="b132640505514364"></a>filter</strong>. The maximum value is <strong id="b842352706112658"><a name="b842352706112658"></a><a name="b842352706112658"></a>1000</strong>, and the minimum value is <strong id="b842352706112710"><a name="b842352706112710"></a><a name="b842352706112710"></a>1</strong>. The value cannot be a negative number.</p>
</td>
</tr>
<tr id="row14852423111914"><td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.1 "><p id="p885219237198"><a name="p885219237198"></a><a name="p885219237198"></a>offset</p>
</td>
<td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.2.5.1.2 "><p id="p1985218237191"><a name="p1985218237191"></a><a name="p1985218237191"></a>String</p>
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
<td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.2.5.1.2 "><p id="p12177957181019"><a name="p12177957181019"></a><a name="p12177957181019"></a>Array of <a href="#table104959232192">match</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="17.82178217821782%" headers="mcps1.2.5.1.3 "><p id="p18853102313197"><a name="p18853102313197"></a><a name="p18853102313197"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="57.42574257425742%" headers="mcps1.2.5.1.4 "><p id="p128537230197"><a name="p128537230197"></a><a name="p128537230197"></a>Specifies the search criteria. The tag key is the field to match. Currently, only <strong id="b84235270615351"><a name="b84235270615351"></a><a name="b84235270615351"></a>resource_name</strong> is supported. The tag value indicates the matched value. This field is a fixed dictionary value.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Description of the  **tag**  field

<a name="table1548032316199"></a>
<table><thead align="left"><tr id="row1785310237196"><th class="cellrowborder" valign="top" width="31.626837316268368%" id="mcps1.2.5.1.1"><p id="p185312312192"><a name="p185312312192"></a><a name="p185312312192"></a><strong id="b842352706195711"><a name="b842352706195711"></a><a name="b842352706195711"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885708%" id="mcps1.2.5.1.2"><p id="p208531923101913"><a name="p208531923101913"></a><a name="p208531923101913"></a><strong id="b84235270615219"><a name="b84235270615219"></a><a name="b84235270615219"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885708%" id="mcps1.2.5.1.3"><p id="p685312311196"><a name="p685312311196"></a><a name="p685312311196"></a><strong id="b842352706145623"><a name="b842352706145623"></a><a name="b842352706145623"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.5.1.4"><p id="p4853122311199"><a name="p4853122311199"></a><a name="p4853122311199"></a><strong id="b978043569"><a name="b978043569"></a><a name="b978043569"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row08532238197"><td class="cellrowborder" valign="top" width="31.626837316268368%" headers="mcps1.2.5.1.1 "><p id="p16854122312191"><a name="p16854122312191"></a><a name="p16854122312191"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885708%" headers="mcps1.2.5.1.2 "><p id="p10854102317195"><a name="p10854102317195"></a><a name="p10854102317195"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885708%" headers="mcps1.2.5.1.3 "><p id="p5854122371919"><a name="p5854122371919"></a><a name="p5854122371919"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.5.1.4 "><p id="p085432316193"><a name="p085432316193"></a><a name="p085432316193"></a>Specifies the tag key. The value can contain a maximum of 127 Unicode characters. The tag key cannot be left blank. (This parameter is not verified during the search process.)</p>
</td>
</tr>
<tr id="row15854623141911"><td class="cellrowborder" valign="top" width="31.626837316268368%" headers="mcps1.2.5.1.1 "><p id="p68541223141919"><a name="p68541223141919"></a><a name="p68541223141919"></a>values</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885708%" headers="mcps1.2.5.1.2 "><p id="p17854223161918"><a name="p17854223161918"></a><a name="p17854223161918"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885708%" headers="mcps1.2.5.1.3 "><p id="p188541423181914"><a name="p188541423181914"></a><a name="p188541423181914"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.5.1.4 "><p id="p198541623121914"><a name="p198541623121914"></a><a name="p198541623121914"></a>Specifies the tag value list. Each value can contain a maximum of 255 Unicode characters. An empty list for <strong id="b842352706151018"><a name="b842352706151018"></a><a name="b842352706151018"></a>values</strong> indicates any value. The values are in the OR relationship.</p>
</td>
</tr>
</tbody>
</table>

**Table  4**  Description of the  **match**  field

<a name="table104959232192"></a>
<table><thead align="left"><tr id="row208541423191917"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.5.1.1"><p id="p1385417236194"><a name="p1385417236194"></a><a name="p1385417236194"></a><strong id="b1907360570"><a name="b1907360570"></a><a name="b1907360570"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="13.13131313131313%" id="mcps1.2.5.1.2"><p id="p1485442313195"><a name="p1485442313195"></a><a name="p1485442313195"></a><strong id="b2120779538"><a name="b2120779538"></a><a name="b2120779538"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.14141414141414%" id="mcps1.2.5.1.3"><p id="p4854182361910"><a name="p4854182361910"></a><a name="p4854182361910"></a><strong id="b2134292635"><a name="b2134292635"></a><a name="b2134292635"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.39393939393939%" id="mcps1.2.5.1.4"><p id="p685472317197"><a name="p685472317197"></a><a name="p685472317197"></a><strong id="b50997534"><a name="b50997534"></a><a name="b50997534"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row12854323201911"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.5.1.1 "><p id="p285482316198"><a name="p285482316198"></a><a name="p285482316198"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.2.5.1.2 "><p id="p4854723121918"><a name="p4854723121918"></a><a name="p4854723121918"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.3 "><p id="p385422301919"><a name="p385422301919"></a><a name="p385422301919"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.39393939393939%" headers="mcps1.2.5.1.4 "><p id="p185514232197"><a name="p185514232197"></a><a name="p185514232197"></a>Specifies the tag key. Currently, the tag key can only be the resource name.</p>
</td>
</tr>
<tr id="row28552023131919"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.5.1.1 "><p id="p485514231195"><a name="p485514231195"></a><a name="p485514231195"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.2.5.1.2 "><p id="p58551523191914"><a name="p58551523191914"></a><a name="p58551523191914"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.3 "><p id="p128551235194"><a name="p128551235194"></a><a name="p128551235194"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.39393939393939%" headers="mcps1.2.5.1.4 "><p id="p128551023151916"><a name="p128551023151916"></a><a name="p128551023151916"></a>Specifies the tag value. A value contains a maximum of 255 Unicode characters.</p>
</td>
</tr>
</tbody>
</table>

Example request 1: Setting  **action**  to  **filter**

```
POST https://{Endpoint}/v2.0/{project_id}/vpcs/resource_instances/action

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

Example request 2: Setting  **action**  to  **count**

```
POST https://{Endpoint}/v2.0/{project_id}/vpcs/resource_instances/action

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

## Response Message<a name="section95436234191"></a>

Response parameter

**Table  5**  Response parameter

<a name="table25631238196"></a>
<table><thead align="left"><tr id="row285515239199"><th class="cellrowborder" valign="top" width="28.000000000000004%" id="mcps1.2.4.1.1"><p id="p1385512317198"><a name="p1385512317198"></a><a name="p1385512317198"></a><strong id="b210713367"><a name="b210713367"></a><a name="b210713367"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="37.330000000000005%" id="mcps1.2.4.1.2"><p id="p158555239198"><a name="p158555239198"></a><a name="p158555239198"></a><strong id="b2133405966"><a name="b2133405966"></a><a name="b2133405966"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="34.67%" id="mcps1.2.4.1.3"><p id="p2855102313199"><a name="p2855102313199"></a><a name="p2855102313199"></a><strong id="b1628686066"><a name="b1628686066"></a><a name="b1628686066"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row2855172320193"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p685502321914"><a name="p685502321914"></a><a name="p685502321914"></a>resources</p>
</td>
<td class="cellrowborder" valign="top" width="37.330000000000005%" headers="mcps1.2.4.1.2 "><p id="p8347412111010"><a name="p8347412111010"></a><a name="p8347412111010"></a>Array of <a href="#table1454542331912">resource</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="34.67%" headers="mcps1.2.4.1.3 "><p id="p68562235195"><a name="p68562235195"></a><a name="p68562235195"></a>Specifies the <strong id="b466955017110"><a name="b466955017110"></a><a name="b466955017110"></a>resource</strong> object list. For details, see <a href="#table1454542331912">Table 6</a>.</p>
</td>
</tr>
<tr id="row16856223111912"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p285620239197"><a name="p285620239197"></a><a name="p285620239197"></a>total_count</p>
</td>
<td class="cellrowborder" valign="top" width="37.330000000000005%" headers="mcps1.2.4.1.2 "><p id="p168562234194"><a name="p168562234194"></a><a name="p168562234194"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="34.67%" headers="mcps1.2.4.1.3 "><p id="p58561323181910"><a name="p58561323181910"></a><a name="p58561323181910"></a>Specifies the total number of query records.</p>
</td>
</tr>
</tbody>
</table>

**Table  6** **resource**  objects

<a name="table1454542331912"></a>
<table><thead align="left"><tr id="row385622315195"><th class="cellrowborder" valign="top" width="28.000000000000004%" id="mcps1.2.4.1.1"><p id="p1785610232193"><a name="p1785610232193"></a><a name="p1785610232193"></a><strong id="b1888374591"><a name="b1888374591"></a><a name="b1888374591"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="37.330000000000005%" id="mcps1.2.4.1.2"><p id="p16856132351913"><a name="p16856132351913"></a><a name="p16856132351913"></a><strong id="b1972642856"><a name="b1972642856"></a><a name="b1972642856"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="34.67%" id="mcps1.2.4.1.3"><p id="p1285622318195"><a name="p1285622318195"></a><a name="p1285622318195"></a><strong id="b471326749"><a name="b471326749"></a><a name="b471326749"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row185662311194"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p1385611238195"><a name="p1385611238195"></a><a name="p1385611238195"></a>resource_id</p>
</td>
<td class="cellrowborder" valign="top" width="37.330000000000005%" headers="mcps1.2.4.1.2 "><p id="p6856152314195"><a name="p6856152314195"></a><a name="p6856152314195"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="34.67%" headers="mcps1.2.4.1.3 "><p id="p128561823141910"><a name="p128561823141910"></a><a name="p128561823141910"></a>Specifies the resource ID.</p>
</td>
</tr>
<tr id="row5856162316198"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p985642311196"><a name="p985642311196"></a><a name="p985642311196"></a>resouce_detail</p>
</td>
<td class="cellrowborder" valign="top" width="37.330000000000005%" headers="mcps1.2.4.1.2 "><p id="p1285742310190"><a name="p1285742310190"></a><a name="p1285742310190"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="34.67%" headers="mcps1.2.4.1.3 "><p id="p8857523191910"><a name="p8857523191910"></a><a name="p8857523191910"></a>Specifies the resource details. Resource details are used for extension. This parameter is left blank by default.</p>
</td>
</tr>
<tr id="row1859132311911"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p0859423151913"><a name="p0859423151913"></a><a name="p0859423151913"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="37.330000000000005%" headers="mcps1.2.4.1.2 "><p id="p18794152718455"><a name="p18794152718455"></a><a name="p18794152718455"></a>Array of <a href="#table1353515016272">tag</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="34.67%" headers="mcps1.2.4.1.3 "><p id="p1985922316199"><a name="p1985922316199"></a><a name="p1985922316199"></a>Specifies the tag list. This parameter is an empty array by default if there is no tag. For details, see <a href="#table1353515016272">Table 7</a>. </p>
</td>
</tr>
<tr id="row13859102317194"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p1785919234197"><a name="p1785919234197"></a><a name="p1785919234197"></a>resource_name</p>
</td>
<td class="cellrowborder" valign="top" width="37.330000000000005%" headers="mcps1.2.4.1.2 "><p id="p138591823191919"><a name="p138591823191919"></a><a name="p138591823191919"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="34.67%" headers="mcps1.2.4.1.3 "><p id="p68591823131919"><a name="p68591823131919"></a><a name="p68591823131919"></a>Specifies the resource name. This parameter is an empty string by default if there is no resource name.</p>
</td>
</tr>
</tbody>
</table>

**Table  7**  Description of the  **tag**  field

<a name="table1353515016272"></a>
<table><thead align="left"><tr id="row12536145015270"><th class="cellrowborder" valign="top" width="31.626837316268368%" id="mcps1.2.5.1.1"><p id="p153615010278"><a name="p153615010278"></a><a name="p153615010278"></a><strong id="b2121733614"><a name="b2121733614"></a><a name="b2121733614"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885708%" id="mcps1.2.5.1.2"><p id="p205361850152712"><a name="p205361850152712"></a><a name="p205361850152712"></a><strong id="b752729083"><a name="b752729083"></a><a name="b752729083"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885708%" id="mcps1.2.5.1.3"><p id="p155361850162716"><a name="p155361850162716"></a><a name="p155361850162716"></a><strong id="b640540825"><a name="b640540825"></a><a name="b640540825"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.5.1.4"><p id="p105361150132714"><a name="p105361150132714"></a><a name="p105361150132714"></a><strong id="b1903550304"><a name="b1903550304"></a><a name="b1903550304"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row653695012712"><td class="cellrowborder" valign="top" width="31.626837316268368%" headers="mcps1.2.5.1.1 "><p id="p155361650192714"><a name="p155361650192714"></a><a name="p155361650192714"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885708%" headers="mcps1.2.5.1.2 "><p id="p1853675017273"><a name="p1853675017273"></a><a name="p1853675017273"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885708%" headers="mcps1.2.5.1.3 "><p id="p3536250152718"><a name="p3536250152718"></a><a name="p3536250152718"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.5.1.4 "><p id="p4536105010277"><a name="p4536105010277"></a><a name="p4536105010277"></a>Specifies the tag key. The value can contain a maximum of 127 Unicode characters. The tag key cannot be left blank. (This parameter is not verified during the search process.)</p>
</td>
</tr>
<tr id="row11536165042716"><td class="cellrowborder" valign="top" width="31.626837316268368%" headers="mcps1.2.5.1.1 "><p id="p175361650142718"><a name="p175361650142718"></a><a name="p175361650142718"></a>values</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885708%" headers="mcps1.2.5.1.2 "><p id="p9536175042714"><a name="p9536175042714"></a><a name="p9536175042714"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885708%" headers="mcps1.2.5.1.3 "><p id="p13536155052713"><a name="p13536155052713"></a><a name="p13536155052713"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.5.1.4 "><p id="p153645062719"><a name="p153645062719"></a><a name="p153645062719"></a>Specifies the tag value list. Each value can contain a maximum of 255 Unicode characters. An empty list for <strong id="b387346785"><a name="b387346785"></a><a name="b387346785"></a>values</strong> indicates any value. The values are in the OR relationship.</p>
</td>
</tr>
</tbody>
</table>

Example response 1: Setting  **action**  to  **filter**

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

Example response 2: Setting  **action**  to  **count**

```
{
       "total_count": 1000
}
```

## Status Code<a name="section31981619"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).


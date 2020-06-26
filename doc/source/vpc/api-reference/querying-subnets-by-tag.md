# Querying Subnets by Tag<a name="subnet_tag_0005"></a>

## Function<a name="section7606194272212"></a>

This API is used to query subnets by tag.

## URI<a name="section19608204210223"></a>

POST /v2.0/\{project\_id\}/subnets/resource\_instances/action

[Table 1](#table27380479)  describes the parameters.

**Table  1**  Parameter description

<a name="table27380479"></a>
<table><thead align="left"><tr id="row28751554"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p47174532"><a name="p47174532"></a><a name="p47174532"></a><strong id="b10905175310133"><a name="b10905175310133"></a><a name="b10905175310133"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p63040734"><a name="p63040734"></a><a name="p63040734"></a><strong id="b8558155681315"><a name="b8558155681315"></a><a name="b8558155681315"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p6025849"><a name="p6025849"></a><a name="p6025849"></a><strong id="b49594582139"><a name="b49594582139"></a><a name="b49594582139"></a>Description</strong></p>
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

## Request Message<a name="section761212428221"></a>

Request parameter

**Table  2**  Request parameter

<a name="table6638104211226"></a>
<table><thead align="left"><tr id="row1858154232212"><th class="cellrowborder" valign="top" width="14.14%" id="mcps1.2.5.1.1"><p id="p385874214220"><a name="p385874214220"></a><a name="p385874214220"></a><strong id="b842352706193648"><a name="b842352706193648"></a><a name="b842352706193648"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="8.08%" id="mcps1.2.5.1.2"><p id="p10858144210224"><a name="p10858144210224"></a><a name="p10858144210224"></a><strong id="b842352706193653"><a name="b842352706193653"></a><a name="b842352706193653"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="20.200000000000003%" id="mcps1.2.5.1.3"><p id="p785864211222"><a name="p785864211222"></a><a name="p785864211222"></a><strong id="b770198191415"><a name="b770198191415"></a><a name="b770198191415"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="57.58%" id="mcps1.2.5.1.4"><p id="p1285816420221"><a name="p1285816420221"></a><a name="p1285816420221"></a><strong id="b8423527061645"><a name="b8423527061645"></a><a name="b8423527061645"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row28583422229"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.5.1.1 "><p id="p17858164212222"><a name="p17858164212222"></a><a name="p17858164212222"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="8.08%" headers="mcps1.2.5.1.2 "><p id="p5189719172218"><a name="p5189719172218"></a><a name="p5189719172218"></a>Array of <a href="#table1361524272219">tag</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.2.5.1.3 "><p id="p11858154272217"><a name="p11858154272217"></a><a name="p11858154272217"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.5.1.4 "><p id="p48581942142220"><a name="p48581942142220"></a><a name="p48581942142220"></a>Specifies the included tags. A maximum of 10 tag keys are allowed for each query operation. Each tag key can have up to 10 tag values. The structure body must be included. The tag key cannot be left blank or set to an empty string. Each tag key must be unique, and each tag value in a tag must be unique.</p>
</td>
</tr>
<tr id="row2085884262212"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.5.1.1 "><p id="p0858204272215"><a name="p0858204272215"></a><a name="p0858204272215"></a>limit</p>
</td>
<td class="cellrowborder" valign="top" width="8.08%" headers="mcps1.2.5.1.2 "><p id="p19858134217221"><a name="p19858134217221"></a><a name="p19858134217221"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.2.5.1.3 "><p id="p2858342202215"><a name="p2858342202215"></a><a name="p2858342202215"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.5.1.4 "><p id="p17858124232220"><a name="p17858124232220"></a><a name="p17858124232220"></a>Sets the page size. This parameter is not available when <strong id="b842352706112419"><a name="b842352706112419"></a><a name="b842352706112419"></a>action</strong> is set to <strong id="b842352706112428"><a name="b842352706112428"></a><a name="b842352706112428"></a>count</strong>. The default value is <strong id="b842352706112654"><a name="b842352706112654"></a><a name="b842352706112654"></a>1000</strong> when <strong id="b39236199214364"><a name="b39236199214364"></a><a name="b39236199214364"></a>action</strong> is set to <strong id="b132640505514364"><a name="b132640505514364"></a><a name="b132640505514364"></a>filter</strong>. The maximum value is <strong id="b842352706112658"><a name="b842352706112658"></a><a name="b842352706112658"></a>1000</strong>, and the minimum value is <strong id="b842352706112710"><a name="b842352706112710"></a><a name="b842352706112710"></a>1</strong>. The value cannot be a negative number.</p>
</td>
</tr>
<tr id="row1985854215222"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.5.1.1 "><p id="p1085864242216"><a name="p1085864242216"></a><a name="p1085864242216"></a>offset</p>
</td>
<td class="cellrowborder" valign="top" width="8.08%" headers="mcps1.2.5.1.2 "><p id="p885814427225"><a name="p885814427225"></a><a name="p885814427225"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.2.5.1.3 "><p id="p14859042182210"><a name="p14859042182210"></a><a name="p14859042182210"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.5.1.4 "><p id="p1185974217224"><a name="p1185974217224"></a><a name="p1185974217224"></a>Specifies the index position. The query starts from the next piece of data indexed by this parameter. This parameter is not required when you query data on the first page. The value in the response returned for querying data on the previous page will be included in this parameter for querying data on subsequent pages. This parameter is not available when <strong id="b1124678678165222"><a name="b1124678678165222"></a><a name="b1124678678165222"></a>action</strong> is set to <strong id="b492491814165222"><a name="b492491814165222"></a><a name="b492491814165222"></a>count</strong>. If <strong id="b1521445588165222"><a name="b1521445588165222"></a><a name="b1521445588165222"></a>action</strong> is set to <strong id="b1990372348165222"><a name="b1990372348165222"></a><a name="b1990372348165222"></a>filter</strong>, the value must be a number, and the default value is <strong id="b1833821991165222"><a name="b1833821991165222"></a><a name="b1833821991165222"></a>0</strong>. The value cannot be a negative number.</p>
</td>
</tr>
<tr id="row1385954242215"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.5.1.1 "><p id="p785915427229"><a name="p785915427229"></a><a name="p785915427229"></a>action</p>
</td>
<td class="cellrowborder" valign="top" width="8.08%" headers="mcps1.2.5.1.2 "><p id="p10859114217222"><a name="p10859114217222"></a><a name="p10859114217222"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.2.5.1.3 "><p id="p4859154212215"><a name="p4859154212215"></a><a name="p4859154212215"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.5.1.4 "><p id="p138591142192220"><a name="p138591142192220"></a><a name="p138591142192220"></a>Specifies the operation to perform. The value can only be <strong id="b842352706145527"><a name="b842352706145527"></a><a name="b842352706145527"></a>filter</strong> (filtering) or <strong id="b842352706145557"><a name="b842352706145557"></a><a name="b842352706145557"></a>count</strong> (querying the total number).</p>
<p id="p12859154242216"><a name="p12859154242216"></a><a name="p12859154242216"></a>The value <strong id="b842352706112921"><a name="b842352706112921"></a><a name="b842352706112921"></a>filter</strong> indicates pagination query. The value <strong id="b84235270611312"><a name="b84235270611312"></a><a name="b84235270611312"></a>count</strong> indicates that the total number of query results meeting the search criteria will be returned.</p>
</td>
</tr>
<tr id="row20859642142214"><td class="cellrowborder" valign="top" width="14.14%" headers="mcps1.2.5.1.1 "><p id="p178599423224"><a name="p178599423224"></a><a name="p178599423224"></a>matches</p>
</td>
<td class="cellrowborder" valign="top" width="8.08%" headers="mcps1.2.5.1.2 "><p id="p116883215184"><a name="p116883215184"></a><a name="p116883215184"></a>Array of <a href="#table46291842142217">match</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.2.5.1.3 "><p id="p485974211225"><a name="p485974211225"></a><a name="p485974211225"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.2.5.1.4 "><p id="p12859164211224"><a name="p12859164211224"></a><a name="p12859164211224"></a>Specifies the search criteria. The tag key is the field to match. Currently, only <strong id="b84235270615351"><a name="b84235270615351"></a><a name="b84235270615351"></a>resource_name</strong> is supported. The tag value indicates the matched value. This field is a fixed dictionary value.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Description of the  **tag**  field

<a name="table1361524272219"></a>
<table><thead align="left"><tr id="row158592424224"><th class="cellrowborder" valign="top" width="31.626837316268368%" id="mcps1.2.5.1.1"><p id="p2085912422223"><a name="p2085912422223"></a><a name="p2085912422223"></a><strong id="b842352706195711"><a name="b842352706195711"></a><a name="b842352706195711"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885708%" id="mcps1.2.5.1.2"><p id="p4859124292219"><a name="p4859124292219"></a><a name="p4859124292219"></a><strong id="b84235270615219"><a name="b84235270615219"></a><a name="b84235270615219"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885708%" id="mcps1.2.5.1.3"><p id="p16859154210228"><a name="p16859154210228"></a><a name="p16859154210228"></a><strong id="b842352706145623"><a name="b842352706145623"></a><a name="b842352706145623"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.5.1.4"><p id="p5859642112216"><a name="p5859642112216"></a><a name="p5859642112216"></a><strong id="b1283252198"><a name="b1283252198"></a><a name="b1283252198"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row19860104214223"><td class="cellrowborder" valign="top" width="31.626837316268368%" headers="mcps1.2.5.1.1 "><p id="p38601942172210"><a name="p38601942172210"></a><a name="p38601942172210"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885708%" headers="mcps1.2.5.1.2 "><p id="p1886054262219"><a name="p1886054262219"></a><a name="p1886054262219"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885708%" headers="mcps1.2.5.1.3 "><p id="p1986024219225"><a name="p1986024219225"></a><a name="p1986024219225"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.5.1.4 "><p id="p198601742112218"><a name="p198601742112218"></a><a name="p198601742112218"></a>Specifies the tag key. The value can contain a maximum of 127 Unicode characters. The tag key cannot be left blank. (This parameter is not verified during the search process.)</p>
</td>
</tr>
<tr id="row6860242192212"><td class="cellrowborder" valign="top" width="31.626837316268368%" headers="mcps1.2.5.1.1 "><p id="p1486054262219"><a name="p1486054262219"></a><a name="p1486054262219"></a>values</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885708%" headers="mcps1.2.5.1.2 "><p id="p986024211229"><a name="p986024211229"></a><a name="p986024211229"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.288571142885708%" headers="mcps1.2.5.1.3 "><p id="p386064216224"><a name="p386064216224"></a><a name="p386064216224"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.5.1.4 "><p id="p9860184215226"><a name="p9860184215226"></a><a name="p9860184215226"></a>Specifies the tag value list. Each value can contain a maximum of 255 Unicode characters. An empty list for <strong id="b842352706151018"><a name="b842352706151018"></a><a name="b842352706151018"></a>values</strong> indicates any value. The values are in the OR relationship.</p>
</td>
</tr>
</tbody>
</table>

**Table  4**  Description of the  **match**  field

<a name="table46291842142217"></a>
<table><thead align="left"><tr id="row486010427223"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.5.1.1"><p id="p486094222215"><a name="p486094222215"></a><a name="p486094222215"></a><strong id="b1382837491"><a name="b1382837491"></a><a name="b1382837491"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="13.13131313131313%" id="mcps1.2.5.1.2"><p id="p086044214225"><a name="p086044214225"></a><a name="p086044214225"></a><strong id="b2076925252"><a name="b2076925252"></a><a name="b2076925252"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.14141414141414%" id="mcps1.2.5.1.3"><p id="p18860124272213"><a name="p18860124272213"></a><a name="p18860124272213"></a><strong id="b635335264"><a name="b635335264"></a><a name="b635335264"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.39393939393939%" id="mcps1.2.5.1.4"><p id="p7860114202215"><a name="p7860114202215"></a><a name="p7860114202215"></a><strong id="b787297204"><a name="b787297204"></a><a name="b787297204"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1586014213229"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.5.1.1 "><p id="p186016421221"><a name="p186016421221"></a><a name="p186016421221"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.2.5.1.2 "><p id="p1486013420224"><a name="p1486013420224"></a><a name="p1486013420224"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.3 "><p id="p108601842102212"><a name="p108601842102212"></a><a name="p108601842102212"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.39393939393939%" headers="mcps1.2.5.1.4 "><p id="p18621042172215"><a name="p18621042172215"></a><a name="p18621042172215"></a>Specifies the tag key. Currently, the tag key can only be the resource name.</p>
</td>
</tr>
<tr id="row1486224219229"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.5.1.1 "><p id="p18862242162213"><a name="p18862242162213"></a><a name="p18862242162213"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.2.5.1.2 "><p id="p1862114220227"><a name="p1862114220227"></a><a name="p1862114220227"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.3 "><p id="p4862174232214"><a name="p4862174232214"></a><a name="p4862174232214"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="39.39393939393939%" headers="mcps1.2.5.1.4 "><p id="p1862204212220"><a name="p1862204212220"></a><a name="p1862204212220"></a>Specifies the tag value. A value contains a maximum of 255 Unicode characters.</p>
</td>
</tr>
</tbody>
</table>

Example request 1: Setting  **action**  to  **filter**

```
POST https://{Endpoint}/v2.0/{project_id}/subnets/resource_instances/action

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
POST https://{Endpoint}/v2.0/{project_id}/subnets/resource_instances/action

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

## Response Message<a name="section1666134232215"></a>

Response parameter

**Table  5**  Response parameter

<a name="table1968114210222"></a>
<table><thead align="left"><tr id="row19862142132214"><th class="cellrowborder" valign="top" width="28.000000000000004%" id="mcps1.2.4.1.1"><p id="p78624429220"><a name="p78624429220"></a><a name="p78624429220"></a><strong id="b1137174195"><a name="b1137174195"></a><a name="b1137174195"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="37.330000000000005%" id="mcps1.2.4.1.2"><p id="p386264220228"><a name="p386264220228"></a><a name="p386264220228"></a><strong id="b1634295792"><a name="b1634295792"></a><a name="b1634295792"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="34.67%" id="mcps1.2.4.1.3"><p id="p186234211222"><a name="p186234211222"></a><a name="p186234211222"></a><strong id="b543543269"><a name="b543543269"></a><a name="b543543269"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row108621942132212"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p1286294212219"><a name="p1286294212219"></a><a name="p1286294212219"></a>resources</p>
</td>
<td class="cellrowborder" valign="top" width="37.330000000000005%" headers="mcps1.2.4.1.2 "><p id="p3561814101915"><a name="p3561814101915"></a><a name="p3561814101915"></a>Array of <a href="#table186631042162216">resource</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="34.67%" headers="mcps1.2.4.1.3 "><p id="p188621142132214"><a name="p188621142132214"></a><a name="p188621142132214"></a>Specifies the <strong id="b819471411152"><a name="b819471411152"></a><a name="b819471411152"></a>resource</strong> object list. For details, see <a href="#table186631042162216">Table 6</a>.</p>
</td>
</tr>
<tr id="row08626422222"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p19862144220226"><a name="p19862144220226"></a><a name="p19862144220226"></a>total_count</p>
</td>
<td class="cellrowborder" valign="top" width="37.330000000000005%" headers="mcps1.2.4.1.2 "><p id="p5862124212224"><a name="p5862124212224"></a><a name="p5862124212224"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="34.67%" headers="mcps1.2.4.1.3 "><p id="p11862144210222"><a name="p11862144210222"></a><a name="p11862144210222"></a>Specifies the total number of query records.</p>
</td>
</tr>
</tbody>
</table>

**Table  6** **resource**  objects

<a name="table186631042162216"></a>
<table><thead align="left"><tr id="row11862124215223"><th class="cellrowborder" valign="top" width="28.000000000000004%" id="mcps1.2.4.1.1"><p id="p1586284222215"><a name="p1586284222215"></a><a name="p1586284222215"></a><strong id="b794220443"><a name="b794220443"></a><a name="b794220443"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="37.330000000000005%" id="mcps1.2.4.1.2"><p id="p1186214282220"><a name="p1186214282220"></a><a name="p1186214282220"></a><strong id="b1744117550"><a name="b1744117550"></a><a name="b1744117550"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="34.67%" id="mcps1.2.4.1.3"><p id="p1086284220228"><a name="p1086284220228"></a><a name="p1086284220228"></a><strong id="b1640116283"><a name="b1640116283"></a><a name="b1640116283"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row88627424229"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p2862174202215"><a name="p2862174202215"></a><a name="p2862174202215"></a>resource_id</p>
</td>
<td class="cellrowborder" valign="top" width="37.330000000000005%" headers="mcps1.2.4.1.2 "><p id="p138624421228"><a name="p138624421228"></a><a name="p138624421228"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="34.67%" headers="mcps1.2.4.1.3 "><p id="p28621442162217"><a name="p28621442162217"></a><a name="p28621442162217"></a>Specifies the resource ID.</p>
</td>
</tr>
<tr id="row086214222219"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p78624423224"><a name="p78624423224"></a><a name="p78624423224"></a>resouce_detail</p>
</td>
<td class="cellrowborder" valign="top" width="37.330000000000005%" headers="mcps1.2.4.1.2 "><p id="p1862204215222"><a name="p1862204215222"></a><a name="p1862204215222"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="34.67%" headers="mcps1.2.4.1.3 "><p id="p118631542172218"><a name="p118631542172218"></a><a name="p118631542172218"></a>Specifies the resource details. Resource details are used for extension. This parameter is left blank by default.</p>
</td>
</tr>
<tr id="row118631842162213"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p1386304272220"><a name="p1386304272220"></a><a name="p1386304272220"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="37.330000000000005%" headers="mcps1.2.4.1.2 "><p id="p13241163520245"><a name="p13241163520245"></a><a name="p13241163520245"></a>Array of <a href="#table1548032316199">tag</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="34.67%" headers="mcps1.2.4.1.3 "><p id="p128636423223"><a name="p128636423223"></a><a name="p128636423223"></a>Specifies the tag list. This parameter is an empty array by default if there is no tag. For details, see <a href="#table1548032316199">Table 7</a>.</p>
</td>
</tr>
<tr id="row13863442112217"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p8863104212220"><a name="p8863104212220"></a><a name="p8863104212220"></a>resource_name</p>
</td>
<td class="cellrowborder" valign="top" width="37.330000000000005%" headers="mcps1.2.4.1.2 "><p id="p6863742192220"><a name="p6863742192220"></a><a name="p6863742192220"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="34.67%" headers="mcps1.2.4.1.3 "><p id="p1186364242215"><a name="p1186364242215"></a><a name="p1186364242215"></a>Specifies the resource name. This parameter is an empty string by default if there is no resource name.</p>
</td>
</tr>
</tbody>
</table>

**Table  7**  Description of the  **tag**  field

<a name="table1548032316199"></a>
<table><thead align="left"><tr id="row1785310237196"><th class="cellrowborder" valign="top" width="31.626837316268368%" id="mcps1.2.5.1.1"><p id="p185312312192"><a name="p185312312192"></a><a name="p185312312192"></a><strong id="b1048986058"><a name="b1048986058"></a><a name="b1048986058"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885708%" id="mcps1.2.5.1.2"><p id="p208531923101913"><a name="p208531923101913"></a><a name="p208531923101913"></a><strong id="b369807922"><a name="b369807922"></a><a name="b369807922"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="14.288571142885708%" id="mcps1.2.5.1.3"><p id="p685312311196"><a name="p685312311196"></a><a name="p685312311196"></a><strong id="b1932041254"><a name="b1932041254"></a><a name="b1932041254"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.5.1.4"><p id="p4853122311199"><a name="p4853122311199"></a><a name="p4853122311199"></a><strong id="b567224647"><a name="b567224647"></a><a name="b567224647"></a>Description</strong></p>
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
<td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.5.1.4 "><p id="p198541623121914"><a name="p198541623121914"></a><a name="p198541623121914"></a>Specifies the tag value list. Each value can contain a maximum of 255 Unicode characters. An empty list for <strong id="b705778802"><a name="b705778802"></a><a name="b705778802"></a>values</strong> indicates any value. The values are in the OR relationship.</p>
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


# Querying EIPs by Tag<a name="eip_tag_0005"></a>

## Function<a name="section1962411310253"></a>

This API is used to query EIPs by tag.

## URI<a name="section11624171382513"></a>

POST /v2.0/\{project\_id\}/publicips/resource\_instances/action

[Table 1](#table27380479)  describes the parameters.

**Table  1**  Parameter description

<a name="table27380479"></a>
<table><thead align="left"><tr id="row28751554"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p47174532"><a name="p47174532"></a><a name="p47174532"></a><strong id="b1036194315358"><a name="b1036194315358"></a><a name="b1036194315358"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p63040734"><a name="p63040734"></a><a name="p63040734"></a><strong id="b2041734433512"><a name="b2041734433512"></a><a name="b2041734433512"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p6025849"><a name="p6025849"></a><a name="p6025849"></a><strong id="b1378119458359"><a name="b1378119458359"></a><a name="b1378119458359"></a>Description</strong></p>
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

## Request Message<a name="section9629111372520"></a>

-   Request parameter

    **Table  2**  Request parameter

    <a name="table6653101362518"></a>
    <table><thead align="left"><tr id="row10890201372517"><th class="cellrowborder" valign="top" width="13.861386138613863%" id="mcps1.2.5.1.1"><p id="p178901213172513"><a name="p178901213172513"></a><a name="p178901213172513"></a><strong id="b842352706193648"><a name="b842352706193648"></a><a name="b842352706193648"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.831683168316832%" id="mcps1.2.5.1.2"><p id="p38902139259"><a name="p38902139259"></a><a name="p38902139259"></a><strong id="b842352706193653"><a name="b842352706193653"></a><a name="b842352706193653"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="11.881188118811881%" id="mcps1.2.5.1.3"><p id="p5890151372511"><a name="p5890151372511"></a><a name="p5890151372511"></a><strong id="b64445104367"><a name="b64445104367"></a><a name="b64445104367"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.42574257425742%" id="mcps1.2.5.1.4"><p id="p3890181342518"><a name="p3890181342518"></a><a name="p3890181342518"></a><strong id="b8423527061645"><a name="b8423527061645"></a><a name="b8423527061645"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row11890161322518"><td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.1 "><p id="p10890111318251"><a name="p10890111318251"></a><a name="p10890111318251"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.2 "><p id="p1239241812243"><a name="p1239241812243"></a><a name="p1239241812243"></a>Array of <a href="#table16632111318253">tag</a> objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.2.5.1.3 "><p id="p1889041312253"><a name="p1889041312253"></a><a name="p1889041312253"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.42574257425742%" headers="mcps1.2.5.1.4 "><p id="p48900130251"><a name="p48900130251"></a><a name="p48900130251"></a>Specifies the included tags. A maximum of 10 tag keys are allowed for each query operation. Each tag key can have up to 10 tag values. The structure body must be included. The tag key cannot be left blank or set to an empty string. Each tag key must be unique, and each tag value in a tag must be unique.</p>
    </td>
    </tr>
    <tr id="row1389091382511"><td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.1 "><p id="p389021352513"><a name="p389021352513"></a><a name="p389021352513"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.2 "><p id="p168901813172511"><a name="p168901813172511"></a><a name="p168901813172511"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.2.5.1.3 "><p id="p168906139251"><a name="p168906139251"></a><a name="p168906139251"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.42574257425742%" headers="mcps1.2.5.1.4 "><p id="p1589091312258"><a name="p1589091312258"></a><a name="p1589091312258"></a>Sets the page size. This parameter is not available when <strong id="b842352706112419"><a name="b842352706112419"></a><a name="b842352706112419"></a>action</strong> is set to <strong id="b842352706112428"><a name="b842352706112428"></a><a name="b842352706112428"></a>count</strong>. The default value is <strong id="b842352706112654"><a name="b842352706112654"></a><a name="b842352706112654"></a>1000</strong> when <strong id="b39236199214364"><a name="b39236199214364"></a><a name="b39236199214364"></a>action</strong> is set to <strong id="b132640505514364"><a name="b132640505514364"></a><a name="b132640505514364"></a>filter</strong>. The maximum value is <strong id="b842352706112658"><a name="b842352706112658"></a><a name="b842352706112658"></a>1000</strong>, and the minimum value is <strong id="b842352706112710"><a name="b842352706112710"></a><a name="b842352706112710"></a>1</strong>. The value cannot be a negative number.</p>
    </td>
    </tr>
    <tr id="row5890313172513"><td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.1 "><p id="p138901013132519"><a name="p138901013132519"></a><a name="p138901013132519"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.2 "><p id="p1889020133259"><a name="p1889020133259"></a><a name="p1889020133259"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.2.5.1.3 "><p id="p12890131372510"><a name="p12890131372510"></a><a name="p12890131372510"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.42574257425742%" headers="mcps1.2.5.1.4 "><p id="p18901613132519"><a name="p18901613132519"></a><a name="p18901613132519"></a>Specifies the index position. The query starts from the next piece of data indexed by this parameter. This parameter is not required when you query data on the first page. The value in the response returned for querying data on the previous page will be included in this parameter for querying data on subsequent pages. This parameter is not available when <strong id="b84235270621521"><a name="b84235270621521"></a><a name="b84235270621521"></a>action</strong> is set to <strong id="b84235270621525"><a name="b84235270621525"></a><a name="b84235270621525"></a>count</strong>. If <strong id="b84235270621528"><a name="b84235270621528"></a><a name="b84235270621528"></a>action</strong> is set to <strong id="b84235270621532"><a name="b84235270621532"></a><a name="b84235270621532"></a>filter</strong>, the value must be a number, and the default value is <strong id="b84235270621539"><a name="b84235270621539"></a><a name="b84235270621539"></a>0</strong>. The value cannot be a negative number.</p>
    </td>
    </tr>
    <tr id="row19890191382520"><td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.1 "><p id="p2891161314258"><a name="p2891161314258"></a><a name="p2891161314258"></a>action</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.2 "><p id="p14891161312512"><a name="p14891161312512"></a><a name="p14891161312512"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.2.5.1.3 "><p id="p1389115138251"><a name="p1389115138251"></a><a name="p1389115138251"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.42574257425742%" headers="mcps1.2.5.1.4 "><p id="p10891413192514"><a name="p10891413192514"></a><a name="p10891413192514"></a>Specifies the operation to perform. The value can only be <strong id="b842352706145527"><a name="b842352706145527"></a><a name="b842352706145527"></a>filter</strong> (filtering) or <strong id="b842352706145557"><a name="b842352706145557"></a><a name="b842352706145557"></a>count</strong> (querying the total number).</p>
    <p id="p1889191322516"><a name="p1889191322516"></a><a name="p1889191322516"></a>The value <strong id="b842352706112921"><a name="b842352706112921"></a><a name="b842352706112921"></a>filter</strong> indicates pagination query. The value <strong id="b84235270611312"><a name="b84235270611312"></a><a name="b84235270611312"></a>count</strong> indicates that the total number of query results meeting the search criteria will be returned.</p>
    </td>
    </tr>
    <tr id="row118911113102515"><td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.1 "><p id="p208913138258"><a name="p208913138258"></a><a name="p208913138258"></a>matches</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.2 "><p id="p163372262315"><a name="p163372262315"></a><a name="p163372262315"></a>Array of <a href="#table18642101315254">match</a> objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.2.5.1.3 "><p id="p6891111312256"><a name="p6891111312256"></a><a name="p6891111312256"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.42574257425742%" headers="mcps1.2.5.1.4 "><p id="p18891613102512"><a name="p18891613102512"></a><a name="p18891613102512"></a>Specifies the search criteria. The tag key is the field to match. Currently, only <strong id="b84235270615351"><a name="b84235270615351"></a><a name="b84235270615351"></a>resource_name</strong> is supported. The tag value indicates the matched value. This field is a fixed dictionary value.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Description of the  **tag**  field

    <a name="table16632111318253"></a>
    <table><thead align="left"><tr id="row1789113139250"><th class="cellrowborder" valign="top" width="31.626837316268368%" id="mcps1.2.5.1.1"><p id="p78915138256"><a name="p78915138256"></a><a name="p78915138256"></a><strong id="b842352706195711"><a name="b842352706195711"></a><a name="b842352706195711"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885708%" id="mcps1.2.5.1.2"><p id="p158911913112510"><a name="p158911913112510"></a><a name="p158911913112510"></a><strong id="b84235270615219"><a name="b84235270615219"></a><a name="b84235270615219"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885708%" id="mcps1.2.5.1.3"><p id="p0891613152515"><a name="p0891613152515"></a><a name="p0891613152515"></a><strong id="b842352706145623"><a name="b842352706145623"></a><a name="b842352706145623"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.5.1.4"><p id="p1489151317257"><a name="p1489151317257"></a><a name="p1489151317257"></a><strong id="b649887733"><a name="b649887733"></a><a name="b649887733"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row17891131332517"><td class="cellrowborder" valign="top" width="31.626837316268368%" headers="mcps1.2.5.1.1 "><p id="p0891151372514"><a name="p0891151372514"></a><a name="p0891151372514"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885708%" headers="mcps1.2.5.1.2 "><p id="p6891181362517"><a name="p6891181362517"></a><a name="p6891181362517"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885708%" headers="mcps1.2.5.1.3 "><p id="p11891121320254"><a name="p11891121320254"></a><a name="p11891121320254"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.5.1.4 "><p id="p2891131311252"><a name="p2891131311252"></a><a name="p2891131311252"></a>Specifies the tag key. The value can contain a maximum of 127 Unicode characters. The tag key cannot be left blank. (This parameter is not verified during the search process.)</p>
    </td>
    </tr>
    <tr id="row08913131253"><td class="cellrowborder" valign="top" width="31.626837316268368%" headers="mcps1.2.5.1.1 "><p id="p9891171316250"><a name="p9891171316250"></a><a name="p9891171316250"></a>values</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885708%" headers="mcps1.2.5.1.2 "><p id="p2891191311251"><a name="p2891191311251"></a><a name="p2891191311251"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885708%" headers="mcps1.2.5.1.3 "><p id="p1289191392518"><a name="p1289191392518"></a><a name="p1289191392518"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.5.1.4 "><p id="p108915133258"><a name="p108915133258"></a><a name="p108915133258"></a>Specifies the tag value list. Each value can contain a maximum of 255 Unicode characters. An empty list for <strong id="b842352706151018"><a name="b842352706151018"></a><a name="b842352706151018"></a>values</strong> indicates any value. The values are in the OR relationship.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  Description of the  **match**  field

    <a name="table18642101315254"></a>
    <table><thead align="left"><tr id="row7891101302515"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.5.1.1"><p id="p689117135251"><a name="p689117135251"></a><a name="p689117135251"></a><strong id="b2068385150"><a name="b2068385150"></a><a name="b2068385150"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="13.13131313131313%" id="mcps1.2.5.1.2"><p id="p188911413192519"><a name="p188911413192519"></a><a name="p188911413192519"></a><strong id="b2019041834"><a name="b2019041834"></a><a name="b2019041834"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.14141414141414%" id="mcps1.2.5.1.3"><p id="p5891121362511"><a name="p5891121362511"></a><a name="p5891121362511"></a><strong id="b1716312749"><a name="b1716312749"></a><a name="b1716312749"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.39393939393939%" id="mcps1.2.5.1.4"><p id="p1089371313256"><a name="p1089371313256"></a><a name="p1089371313256"></a><strong id="b361793441"><a name="b361793441"></a><a name="b361793441"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row58931413202516"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.5.1.1 "><p id="p989314135254"><a name="p989314135254"></a><a name="p989314135254"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.2.5.1.2 "><p id="p1789319133253"><a name="p1789319133253"></a><a name="p1789319133253"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.3 "><p id="p1889320134251"><a name="p1889320134251"></a><a name="p1889320134251"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.39393939393939%" headers="mcps1.2.5.1.4 "><p id="p188931913182514"><a name="p188931913182514"></a><a name="p188931913182514"></a>Specifies the tag key. Currently, the tag key can only be the resource name.</p>
    </td>
    </tr>
    <tr id="row108933135254"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.5.1.1 "><p id="p7893201310254"><a name="p7893201310254"></a><a name="p7893201310254"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.2.5.1.2 "><p id="p15893113102518"><a name="p15893113102518"></a><a name="p15893113102518"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.3 "><p id="p15893161332520"><a name="p15893161332520"></a><a name="p15893161332520"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.39393939393939%" headers="mcps1.2.5.1.4 "><p id="p3893181332515"><a name="p3893181332515"></a><a name="p3893181332515"></a>Specifies the tag value. A value contains a maximum of 255 Unicode characters.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request 1: Setting  **action**  to  **filter**

    ```
    POST https://{Endpoint}/v2.0/{project_id}/publicips/resource_instances/action
    
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

-   Example request 2: Setting  **action**  to  **count**

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


## Response Message<a name="section3676613112519"></a>

-   Response parameter

    **Table  5**  Response parameter

    <a name="table669961372515"></a>
    <table><thead align="left"><tr id="row689311382512"><th class="cellrowborder" valign="top" width="28.000000000000004%" id="mcps1.2.4.1.1"><p id="p11893151312516"><a name="p11893151312516"></a><a name="p11893151312516"></a><strong id="b556530135"><a name="b556530135"></a><a name="b556530135"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="37.330000000000005%" id="mcps1.2.4.1.2"><p id="p1789361319251"><a name="p1789361319251"></a><a name="p1789361319251"></a><strong id="b887643639"><a name="b887643639"></a><a name="b887643639"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="34.67%" id="mcps1.2.4.1.3"><p id="p19893131310258"><a name="p19893131310258"></a><a name="p19893131310258"></a><strong id="b832303684"><a name="b832303684"></a><a name="b832303684"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row7893201315255"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p889311310255"><a name="p889311310255"></a><a name="p889311310255"></a>resources</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.330000000000005%" headers="mcps1.2.4.1.2 "><p id="p658617115246"><a name="p658617115246"></a><a name="p658617115246"></a>Array of <a href="#table15678313132518">resource</a> objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.67%" headers="mcps1.2.4.1.3 "><p id="p1893111313258"><a name="p1893111313258"></a><a name="p1893111313258"></a>Specifies the <strong id="b17627033133616"><a name="b17627033133616"></a><a name="b17627033133616"></a>resource</strong> object list. For details, see <a href="#table15678313132518">Table 6</a>.</p>
    </td>
    </tr>
    <tr id="row1989331314259"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p158931313152513"><a name="p158931313152513"></a><a name="p158931313152513"></a>total_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.330000000000005%" headers="mcps1.2.4.1.2 "><p id="p58931113112511"><a name="p58931113112511"></a><a name="p58931113112511"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.67%" headers="mcps1.2.4.1.3 "><p id="p10893121312258"><a name="p10893121312258"></a><a name="p10893121312258"></a>Specifies the total number of query records.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6** **resource**  objects

    <a name="table15678313132518"></a>
    <table><thead align="left"><tr id="row14893181314253"><th class="cellrowborder" valign="top" width="28.000000000000004%" id="mcps1.2.4.1.1"><p id="p1889361320250"><a name="p1889361320250"></a><a name="p1889361320250"></a><strong id="b1755613501"><a name="b1755613501"></a><a name="b1755613501"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="37.330000000000005%" id="mcps1.2.4.1.2"><p id="p8893161342512"><a name="p8893161342512"></a><a name="p8893161342512"></a><strong id="b1865005939"><a name="b1865005939"></a><a name="b1865005939"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="34.67%" id="mcps1.2.4.1.3"><p id="p3894151362514"><a name="p3894151362514"></a><a name="p3894151362514"></a><strong id="b1816164348"><a name="b1816164348"></a><a name="b1816164348"></a>Description</strong></p>
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
    <td class="cellrowborder" valign="top" width="34.67%" headers="mcps1.2.4.1.3 "><p id="p14894181315254"><a name="p14894181315254"></a><a name="p14894181315254"></a>Specifies the resource details. Resource details are used for extension. This parameter is left blank by default.</p>
    </td>
    </tr>
    <tr id="row1189431342514"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="p58945135256"><a name="p58945135256"></a><a name="p58945135256"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.330000000000005%" headers="mcps1.2.4.1.2 "><p id="p752144512478"><a name="p752144512478"></a><a name="p752144512478"></a>Array of <a href="#table1548032316199">tag</a> objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.67%" headers="mcps1.2.4.1.3 "><p id="p188941913122519"><a name="p188941913122519"></a><a name="p188941913122519"></a>Specifies the tag list. This parameter is an empty array by default if there is no tag. For details, see <a href="#table1548032316199">Table 7</a>.</p>
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

    **Table  7**  Description of the  **tag**  field

    <a name="table1548032316199"></a>
    <table><thead align="left"><tr id="row1785310237196"><th class="cellrowborder" valign="top" width="31.626837316268368%" id="mcps1.2.5.1.1"><p id="p185312312192"><a name="p185312312192"></a><a name="p185312312192"></a><strong id="b1866897138"><a name="b1866897138"></a><a name="b1866897138"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885708%" id="mcps1.2.5.1.2"><p id="p208531923101913"><a name="p208531923101913"></a><a name="p208531923101913"></a><strong id="b640938415"><a name="b640938415"></a><a name="b640938415"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885708%" id="mcps1.2.5.1.3"><p id="p685312311196"><a name="p685312311196"></a><a name="p685312311196"></a><strong id="b1080233722"><a name="b1080233722"></a><a name="b1080233722"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.5.1.4"><p id="p4853122311199"><a name="p4853122311199"></a><a name="p4853122311199"></a><strong id="b245188100"><a name="b245188100"></a><a name="b245188100"></a>Description</strong></p>
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
    <td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.5.1.4 "><p id="p198541623121914"><a name="p198541623121914"></a><a name="p198541623121914"></a>Specifies the tag value list. Each value can contain a maximum of 255 Unicode characters. An empty list for <strong id="b1957000225"><a name="b1957000225"></a><a name="b1957000225"></a>values</strong> indicates any value. The values are in the OR relationship.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response 1: Setting  **action**  to  **filter**

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

-   Example response 2: Setting  **action**  to  **count**

    ```
    {
           "total_count": 1000
    }
    ```


## Status Code<a name="section31981619"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).


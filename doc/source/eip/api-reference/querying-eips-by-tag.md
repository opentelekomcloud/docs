# Querying EIPs by Tag<a name="eip_apitag_0005"></a>

## Function<a name="en-us_topic_0201534190_section1962411310253"></a>

This API is used to query EIPs by tag.

## URI<a name="en-us_topic_0201534190_section11624171382513"></a>

POST /v2.0/\{project\_id\}/publicips/resource\_instances/action

[Table 1](#en-us_topic_0201534190_table27380479)  describes the parameters.

**Table  1**  Parameter description

<a name="en-us_topic_0201534190_table27380479"></a>
<table><thead align="left"><tr id="en-us_topic_0201534190_row28751554"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534190_p47174532"><a name="en-us_topic_0201534190_p47174532"></a><a name="en-us_topic_0201534190_p47174532"></a><strong id="en-us_topic_0201534190_b1036194315358"><a name="en-us_topic_0201534190_b1036194315358"></a><a name="en-us_topic_0201534190_b1036194315358"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534190_p63040734"><a name="en-us_topic_0201534190_p63040734"></a><a name="en-us_topic_0201534190_p63040734"></a><strong id="en-us_topic_0201534190_b2041734433512"><a name="en-us_topic_0201534190_b2041734433512"></a><a name="en-us_topic_0201534190_b2041734433512"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534190_p6025849"><a name="en-us_topic_0201534190_p6025849"></a><a name="en-us_topic_0201534190_p6025849"></a><strong id="en-us_topic_0201534190_b1378119458359"><a name="en-us_topic_0201534190_b1378119458359"></a><a name="en-us_topic_0201534190_b1378119458359"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0201534190_row18331773"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534190_p8478608"><a name="en-us_topic_0201534190_p8478608"></a><a name="en-us_topic_0201534190_p8478608"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534190_p15678685"><a name="en-us_topic_0201534190_p15678685"></a><a name="en-us_topic_0201534190_p15678685"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534190_p10487112"><a name="en-us_topic_0201534190_p10487112"></a><a name="en-us_topic_0201534190_p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="en-us_topic_0201534190_section9629111372520"></a>

-   Request parameter

    **Table  2**  Request parameter

    <a name="en-us_topic_0201534190_table6653101362518"></a>
    <table><thead align="left"><tr id="en-us_topic_0201534190_row10890201372517"><th class="cellrowborder" valign="top" width="13.861386138613863%" id="mcps1.2.5.1.1"><p id="en-us_topic_0201534190_p178901213172513"><a name="en-us_topic_0201534190_p178901213172513"></a><a name="en-us_topic_0201534190_p178901213172513"></a><strong id="en-us_topic_0201534190_b842352706193648"><a name="en-us_topic_0201534190_b842352706193648"></a><a name="en-us_topic_0201534190_b842352706193648"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.831683168316832%" id="mcps1.2.5.1.2"><p id="en-us_topic_0201534190_p38902139259"><a name="en-us_topic_0201534190_p38902139259"></a><a name="en-us_topic_0201534190_p38902139259"></a><strong id="en-us_topic_0201534190_b842352706193653"><a name="en-us_topic_0201534190_b842352706193653"></a><a name="en-us_topic_0201534190_b842352706193653"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="11.881188118811881%" id="mcps1.2.5.1.3"><p id="en-us_topic_0201534190_p5890151372511"><a name="en-us_topic_0201534190_p5890151372511"></a><a name="en-us_topic_0201534190_p5890151372511"></a><strong id="en-us_topic_0201534190_b64445104367"><a name="en-us_topic_0201534190_b64445104367"></a><a name="en-us_topic_0201534190_b64445104367"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.42574257425742%" id="mcps1.2.5.1.4"><p id="en-us_topic_0201534190_p3890181342518"><a name="en-us_topic_0201534190_p3890181342518"></a><a name="en-us_topic_0201534190_p3890181342518"></a><strong id="en-us_topic_0201534190_b8423527061645"><a name="en-us_topic_0201534190_b8423527061645"></a><a name="en-us_topic_0201534190_b8423527061645"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0201534190_row11890161322518"><td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534190_p10890111318251"><a name="en-us_topic_0201534190_p10890111318251"></a><a name="en-us_topic_0201534190_p10890111318251"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534190_p1239241812243"><a name="en-us_topic_0201534190_p1239241812243"></a><a name="en-us_topic_0201534190_p1239241812243"></a>Array of <a href="#en-us_topic_0201534190_table16632111318253">tag</a> objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534190_p1889041312253"><a name="en-us_topic_0201534190_p1889041312253"></a><a name="en-us_topic_0201534190_p1889041312253"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.42574257425742%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0201534190_p48900130251"><a name="en-us_topic_0201534190_p48900130251"></a><a name="en-us_topic_0201534190_p48900130251"></a>Specifies the included tags. A maximum of 10 tag keys are allowed for each query operation. Each tag key can have up to 10 tag values. The structure body must be included. The tag key cannot be left blank or set to an empty string. Each tag key must be unique, and each tag value in a tag must be unique.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0201534190_row1389091382511"><td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534190_p389021352513"><a name="en-us_topic_0201534190_p389021352513"></a><a name="en-us_topic_0201534190_p389021352513"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534190_p168901813172511"><a name="en-us_topic_0201534190_p168901813172511"></a><a name="en-us_topic_0201534190_p168901813172511"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534190_p168906139251"><a name="en-us_topic_0201534190_p168906139251"></a><a name="en-us_topic_0201534190_p168906139251"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.42574257425742%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0201534190_p1589091312258"><a name="en-us_topic_0201534190_p1589091312258"></a><a name="en-us_topic_0201534190_p1589091312258"></a>Sets the page size. This parameter is not available when <strong id="en-us_topic_0201534190_b842352706112419"><a name="en-us_topic_0201534190_b842352706112419"></a><a name="en-us_topic_0201534190_b842352706112419"></a>action</strong> is set to <strong id="en-us_topic_0201534190_b842352706112428"><a name="en-us_topic_0201534190_b842352706112428"></a><a name="en-us_topic_0201534190_b842352706112428"></a>count</strong>. The default value is <strong id="en-us_topic_0201534190_b842352706112654"><a name="en-us_topic_0201534190_b842352706112654"></a><a name="en-us_topic_0201534190_b842352706112654"></a>1000</strong> when <strong id="en-us_topic_0201534190_b39236199214364"><a name="en-us_topic_0201534190_b39236199214364"></a><a name="en-us_topic_0201534190_b39236199214364"></a>action</strong> is set to <strong id="en-us_topic_0201534190_b132640505514364"><a name="en-us_topic_0201534190_b132640505514364"></a><a name="en-us_topic_0201534190_b132640505514364"></a>filter</strong>. The maximum value is <strong id="en-us_topic_0201534190_b842352706112658"><a name="en-us_topic_0201534190_b842352706112658"></a><a name="en-us_topic_0201534190_b842352706112658"></a>1000</strong>, and the minimum value is <strong id="en-us_topic_0201534190_b842352706112710"><a name="en-us_topic_0201534190_b842352706112710"></a><a name="en-us_topic_0201534190_b842352706112710"></a>1</strong>. The value cannot be a negative number.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0201534190_row5890313172513"><td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534190_p138901013132519"><a name="en-us_topic_0201534190_p138901013132519"></a><a name="en-us_topic_0201534190_p138901013132519"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534190_p1889020133259"><a name="en-us_topic_0201534190_p1889020133259"></a><a name="en-us_topic_0201534190_p1889020133259"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534190_p12890131372510"><a name="en-us_topic_0201534190_p12890131372510"></a><a name="en-us_topic_0201534190_p12890131372510"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.42574257425742%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0201534190_p18901613132519"><a name="en-us_topic_0201534190_p18901613132519"></a><a name="en-us_topic_0201534190_p18901613132519"></a>Specifies the index position. The query starts from the next piece of data indexed by this parameter. This parameter is not required when you query data on the first page. The value in the response returned for querying data on the previous page will be included in this parameter for querying data on subsequent pages. This parameter is not available when <strong id="en-us_topic_0201534190_b84235270621521"><a name="en-us_topic_0201534190_b84235270621521"></a><a name="en-us_topic_0201534190_b84235270621521"></a>action</strong> is set to <strong id="en-us_topic_0201534190_b84235270621525"><a name="en-us_topic_0201534190_b84235270621525"></a><a name="en-us_topic_0201534190_b84235270621525"></a>count</strong>. If <strong id="en-us_topic_0201534190_b84235270621528"><a name="en-us_topic_0201534190_b84235270621528"></a><a name="en-us_topic_0201534190_b84235270621528"></a>action</strong> is set to <strong id="en-us_topic_0201534190_b84235270621532"><a name="en-us_topic_0201534190_b84235270621532"></a><a name="en-us_topic_0201534190_b84235270621532"></a>filter</strong>, the value must be a number, and the default value is <strong id="en-us_topic_0201534190_b84235270621539"><a name="en-us_topic_0201534190_b84235270621539"></a><a name="en-us_topic_0201534190_b84235270621539"></a>0</strong>. The value cannot be a negative number.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0201534190_row19890191382520"><td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534190_p2891161314258"><a name="en-us_topic_0201534190_p2891161314258"></a><a name="en-us_topic_0201534190_p2891161314258"></a>action</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534190_p14891161312512"><a name="en-us_topic_0201534190_p14891161312512"></a><a name="en-us_topic_0201534190_p14891161312512"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534190_p1389115138251"><a name="en-us_topic_0201534190_p1389115138251"></a><a name="en-us_topic_0201534190_p1389115138251"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.42574257425742%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0201534190_p10891413192514"><a name="en-us_topic_0201534190_p10891413192514"></a><a name="en-us_topic_0201534190_p10891413192514"></a>Specifies the operation to perform. The value can only be <strong id="en-us_topic_0201534190_b842352706145527"><a name="en-us_topic_0201534190_b842352706145527"></a><a name="en-us_topic_0201534190_b842352706145527"></a>filter</strong> (filtering) or <strong id="en-us_topic_0201534190_b842352706145557"><a name="en-us_topic_0201534190_b842352706145557"></a><a name="en-us_topic_0201534190_b842352706145557"></a>count</strong> (querying the total number).</p>
    <p id="en-us_topic_0201534190_p1889191322516"><a name="en-us_topic_0201534190_p1889191322516"></a><a name="en-us_topic_0201534190_p1889191322516"></a>The value <strong id="en-us_topic_0201534190_b842352706112921"><a name="en-us_topic_0201534190_b842352706112921"></a><a name="en-us_topic_0201534190_b842352706112921"></a>filter</strong> indicates pagination query. The value <strong id="en-us_topic_0201534190_b84235270611312"><a name="en-us_topic_0201534190_b84235270611312"></a><a name="en-us_topic_0201534190_b84235270611312"></a>count</strong> indicates that the total number of query results meeting the search criteria will be returned.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0201534190_row118911113102515"><td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534190_p208913138258"><a name="en-us_topic_0201534190_p208913138258"></a><a name="en-us_topic_0201534190_p208913138258"></a>matches</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534190_p163372262315"><a name="en-us_topic_0201534190_p163372262315"></a><a name="en-us_topic_0201534190_p163372262315"></a>Array of <a href="#en-us_topic_0201534190_table18642101315254">match</a> objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.881188118811881%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534190_p6891111312256"><a name="en-us_topic_0201534190_p6891111312256"></a><a name="en-us_topic_0201534190_p6891111312256"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.42574257425742%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0201534190_p18891613102512"><a name="en-us_topic_0201534190_p18891613102512"></a><a name="en-us_topic_0201534190_p18891613102512"></a>Specifies the search criteria. The tag key is the field to match. Currently, only <strong id="en-us_topic_0201534190_b84235270615351"><a name="en-us_topic_0201534190_b84235270615351"></a><a name="en-us_topic_0201534190_b84235270615351"></a>resource_name</strong> is supported. The tag value indicates the matched value. This field is a fixed dictionary value.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Description of the  **tag**  field

    <a name="en-us_topic_0201534190_table16632111318253"></a>
    <table><thead align="left"><tr id="en-us_topic_0201534190_row1789113139250"><th class="cellrowborder" valign="top" width="31.626837316268368%" id="mcps1.2.5.1.1"><p id="en-us_topic_0201534190_p78915138256"><a name="en-us_topic_0201534190_p78915138256"></a><a name="en-us_topic_0201534190_p78915138256"></a><strong id="en-us_topic_0201534190_b842352706195711"><a name="en-us_topic_0201534190_b842352706195711"></a><a name="en-us_topic_0201534190_b842352706195711"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885708%" id="mcps1.2.5.1.2"><p id="en-us_topic_0201534190_p158911913112510"><a name="en-us_topic_0201534190_p158911913112510"></a><a name="en-us_topic_0201534190_p158911913112510"></a><strong id="en-us_topic_0201534190_b84235270615219"><a name="en-us_topic_0201534190_b84235270615219"></a><a name="en-us_topic_0201534190_b84235270615219"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885708%" id="mcps1.2.5.1.3"><p id="en-us_topic_0201534190_p0891613152515"><a name="en-us_topic_0201534190_p0891613152515"></a><a name="en-us_topic_0201534190_p0891613152515"></a><strong id="en-us_topic_0201534190_b842352706145623"><a name="en-us_topic_0201534190_b842352706145623"></a><a name="en-us_topic_0201534190_b842352706145623"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.5.1.4"><p id="en-us_topic_0201534190_p1489151317257"><a name="en-us_topic_0201534190_p1489151317257"></a><a name="en-us_topic_0201534190_p1489151317257"></a><strong id="en-us_topic_0201534190_b649887733"><a name="en-us_topic_0201534190_b649887733"></a><a name="en-us_topic_0201534190_b649887733"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0201534190_row17891131332517"><td class="cellrowborder" valign="top" width="31.626837316268368%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534190_p0891151372514"><a name="en-us_topic_0201534190_p0891151372514"></a><a name="en-us_topic_0201534190_p0891151372514"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885708%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534190_p6891181362517"><a name="en-us_topic_0201534190_p6891181362517"></a><a name="en-us_topic_0201534190_p6891181362517"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885708%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534190_p11891121320254"><a name="en-us_topic_0201534190_p11891121320254"></a><a name="en-us_topic_0201534190_p11891121320254"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0201534190_p2891131311252"><a name="en-us_topic_0201534190_p2891131311252"></a><a name="en-us_topic_0201534190_p2891131311252"></a>Specifies the tag key. The value can contain a maximum of 127 Unicode characters. The tag key cannot be left blank. (This parameter is not verified during the search process.)</p>
    </td>
    </tr>
    <tr id="en-us_topic_0201534190_row08913131253"><td class="cellrowborder" valign="top" width="31.626837316268368%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534190_p9891171316250"><a name="en-us_topic_0201534190_p9891171316250"></a><a name="en-us_topic_0201534190_p9891171316250"></a>values</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885708%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534190_p2891191311251"><a name="en-us_topic_0201534190_p2891191311251"></a><a name="en-us_topic_0201534190_p2891191311251"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885708%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534190_p1289191392518"><a name="en-us_topic_0201534190_p1289191392518"></a><a name="en-us_topic_0201534190_p1289191392518"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0201534190_p108915133258"><a name="en-us_topic_0201534190_p108915133258"></a><a name="en-us_topic_0201534190_p108915133258"></a>Specifies the tag value list. Each value can contain a maximum of 255 Unicode characters. An empty list for <strong id="en-us_topic_0201534190_b842352706151018"><a name="en-us_topic_0201534190_b842352706151018"></a><a name="en-us_topic_0201534190_b842352706151018"></a>values</strong> indicates any value. The values are in the OR relationship.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  Description of the  **match**  field

    <a name="en-us_topic_0201534190_table18642101315254"></a>
    <table><thead align="left"><tr id="en-us_topic_0201534190_row7891101302515"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.5.1.1"><p id="en-us_topic_0201534190_p689117135251"><a name="en-us_topic_0201534190_p689117135251"></a><a name="en-us_topic_0201534190_p689117135251"></a><strong id="en-us_topic_0201534190_b2068385150"><a name="en-us_topic_0201534190_b2068385150"></a><a name="en-us_topic_0201534190_b2068385150"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="13.13131313131313%" id="mcps1.2.5.1.2"><p id="en-us_topic_0201534190_p188911413192519"><a name="en-us_topic_0201534190_p188911413192519"></a><a name="en-us_topic_0201534190_p188911413192519"></a><strong id="en-us_topic_0201534190_b2019041834"><a name="en-us_topic_0201534190_b2019041834"></a><a name="en-us_topic_0201534190_b2019041834"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.14141414141414%" id="mcps1.2.5.1.3"><p id="en-us_topic_0201534190_p5891121362511"><a name="en-us_topic_0201534190_p5891121362511"></a><a name="en-us_topic_0201534190_p5891121362511"></a><strong id="en-us_topic_0201534190_b1716312749"><a name="en-us_topic_0201534190_b1716312749"></a><a name="en-us_topic_0201534190_b1716312749"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.39393939393939%" id="mcps1.2.5.1.4"><p id="en-us_topic_0201534190_p1089371313256"><a name="en-us_topic_0201534190_p1089371313256"></a><a name="en-us_topic_0201534190_p1089371313256"></a><strong id="en-us_topic_0201534190_b361793441"><a name="en-us_topic_0201534190_b361793441"></a><a name="en-us_topic_0201534190_b361793441"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0201534190_row58931413202516"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534190_p989314135254"><a name="en-us_topic_0201534190_p989314135254"></a><a name="en-us_topic_0201534190_p989314135254"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534190_p1789319133253"><a name="en-us_topic_0201534190_p1789319133253"></a><a name="en-us_topic_0201534190_p1789319133253"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534190_p1889320134251"><a name="en-us_topic_0201534190_p1889320134251"></a><a name="en-us_topic_0201534190_p1889320134251"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.39393939393939%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0201534190_p188931913182514"><a name="en-us_topic_0201534190_p188931913182514"></a><a name="en-us_topic_0201534190_p188931913182514"></a>Specifies the tag key. Currently, the tag key can only be the resource name.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0201534190_row108933135254"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534190_p7893201310254"><a name="en-us_topic_0201534190_p7893201310254"></a><a name="en-us_topic_0201534190_p7893201310254"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.13131313131313%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534190_p15893113102518"><a name="en-us_topic_0201534190_p15893113102518"></a><a name="en-us_topic_0201534190_p15893113102518"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.14141414141414%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534190_p15893161332520"><a name="en-us_topic_0201534190_p15893161332520"></a><a name="en-us_topic_0201534190_p15893161332520"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.39393939393939%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0201534190_p3893181332515"><a name="en-us_topic_0201534190_p3893181332515"></a><a name="en-us_topic_0201534190_p3893181332515"></a>Specifies the tag value. A value contains a maximum of 255 Unicode characters.</p>
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


## Response Message<a name="en-us_topic_0201534190_section3676613112519"></a>

-   Response parameter

    **Table  5**  Response parameter

    <a name="en-us_topic_0201534190_table669961372515"></a>
    <table><thead align="left"><tr id="en-us_topic_0201534190_row689311382512"><th class="cellrowborder" valign="top" width="28.000000000000004%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534190_p11893151312516"><a name="en-us_topic_0201534190_p11893151312516"></a><a name="en-us_topic_0201534190_p11893151312516"></a><strong id="en-us_topic_0201534190_b556530135"><a name="en-us_topic_0201534190_b556530135"></a><a name="en-us_topic_0201534190_b556530135"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="37.330000000000005%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534190_p1789361319251"><a name="en-us_topic_0201534190_p1789361319251"></a><a name="en-us_topic_0201534190_p1789361319251"></a><strong id="en-us_topic_0201534190_b887643639"><a name="en-us_topic_0201534190_b887643639"></a><a name="en-us_topic_0201534190_b887643639"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="34.67%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534190_p19893131310258"><a name="en-us_topic_0201534190_p19893131310258"></a><a name="en-us_topic_0201534190_p19893131310258"></a><strong id="en-us_topic_0201534190_b832303684"><a name="en-us_topic_0201534190_b832303684"></a><a name="en-us_topic_0201534190_b832303684"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0201534190_row7893201315255"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534190_p889311310255"><a name="en-us_topic_0201534190_p889311310255"></a><a name="en-us_topic_0201534190_p889311310255"></a>resources</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.330000000000005%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534190_p658617115246"><a name="en-us_topic_0201534190_p658617115246"></a><a name="en-us_topic_0201534190_p658617115246"></a>Array of <a href="#en-us_topic_0201534190_table15678313132518">resource</a> objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.67%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534190_p1893111313258"><a name="en-us_topic_0201534190_p1893111313258"></a><a name="en-us_topic_0201534190_p1893111313258"></a>Specifies the <strong id="en-us_topic_0201534190_b17627033133616"><a name="en-us_topic_0201534190_b17627033133616"></a><a name="en-us_topic_0201534190_b17627033133616"></a>resource</strong> object list. For details, see <a href="#en-us_topic_0201534190_table15678313132518">Table 6</a>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0201534190_row1989331314259"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534190_p158931313152513"><a name="en-us_topic_0201534190_p158931313152513"></a><a name="en-us_topic_0201534190_p158931313152513"></a>total_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.330000000000005%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534190_p58931113112511"><a name="en-us_topic_0201534190_p58931113112511"></a><a name="en-us_topic_0201534190_p58931113112511"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.67%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534190_p10893121312258"><a name="en-us_topic_0201534190_p10893121312258"></a><a name="en-us_topic_0201534190_p10893121312258"></a>Specifies the total number of query records.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6** **resource**  objects

    <a name="en-us_topic_0201534190_table15678313132518"></a>
    <table><thead align="left"><tr id="en-us_topic_0201534190_row14893181314253"><th class="cellrowborder" valign="top" width="28.000000000000004%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534190_p1889361320250"><a name="en-us_topic_0201534190_p1889361320250"></a><a name="en-us_topic_0201534190_p1889361320250"></a><strong id="en-us_topic_0201534190_b1755613501"><a name="en-us_topic_0201534190_b1755613501"></a><a name="en-us_topic_0201534190_b1755613501"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="37.330000000000005%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534190_p8893161342512"><a name="en-us_topic_0201534190_p8893161342512"></a><a name="en-us_topic_0201534190_p8893161342512"></a><strong id="en-us_topic_0201534190_b1865005939"><a name="en-us_topic_0201534190_b1865005939"></a><a name="en-us_topic_0201534190_b1865005939"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="34.67%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534190_p3894151362514"><a name="en-us_topic_0201534190_p3894151362514"></a><a name="en-us_topic_0201534190_p3894151362514"></a><strong id="en-us_topic_0201534190_b1816164348"><a name="en-us_topic_0201534190_b1816164348"></a><a name="en-us_topic_0201534190_b1816164348"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0201534190_row389421332512"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534190_p1289461362516"><a name="en-us_topic_0201534190_p1289461362516"></a><a name="en-us_topic_0201534190_p1289461362516"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.330000000000005%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534190_p13894111322519"><a name="en-us_topic_0201534190_p13894111322519"></a><a name="en-us_topic_0201534190_p13894111322519"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.67%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534190_p589451313259"><a name="en-us_topic_0201534190_p589451313259"></a><a name="en-us_topic_0201534190_p589451313259"></a>Specifies the resource ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0201534190_row12894213172511"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534190_p11894181312514"><a name="en-us_topic_0201534190_p11894181312514"></a><a name="en-us_topic_0201534190_p11894181312514"></a>resouce_detail</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.330000000000005%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534190_p6894121314259"><a name="en-us_topic_0201534190_p6894121314259"></a><a name="en-us_topic_0201534190_p6894121314259"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.67%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534190_p14894181315254"><a name="en-us_topic_0201534190_p14894181315254"></a><a name="en-us_topic_0201534190_p14894181315254"></a>Specifies the resource details. Resource details are used for extension. This parameter is left blank by default.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0201534190_row1189431342514"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534190_p58945135256"><a name="en-us_topic_0201534190_p58945135256"></a><a name="en-us_topic_0201534190_p58945135256"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.330000000000005%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534190_p752144512478"><a name="en-us_topic_0201534190_p752144512478"></a><a name="en-us_topic_0201534190_p752144512478"></a>Array of <a href="#en-us_topic_0201534190_table1548032316199">tag</a> objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.67%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534190_p188941913122519"><a name="en-us_topic_0201534190_p188941913122519"></a><a name="en-us_topic_0201534190_p188941913122519"></a>Specifies the tag list. This parameter is an empty array by default if there is no tag. For details, see <a href="#en-us_topic_0201534190_table1548032316199">Table 7</a>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0201534190_row889451315256"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534190_p188943136256"><a name="en-us_topic_0201534190_p188943136256"></a><a name="en-us_topic_0201534190_p188943136256"></a>resource_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="37.330000000000005%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534190_p2894191372516"><a name="en-us_topic_0201534190_p2894191372516"></a><a name="en-us_topic_0201534190_p2894191372516"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="34.67%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534190_p3894141342514"><a name="en-us_topic_0201534190_p3894141342514"></a><a name="en-us_topic_0201534190_p3894141342514"></a>Specifies the resource name. This parameter is an empty string by default if there is no resource name.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  7**  Description of the  **tag**  field

    <a name="en-us_topic_0201534190_table1548032316199"></a>
    <table><thead align="left"><tr id="en-us_topic_0201534190_row1785310237196"><th class="cellrowborder" valign="top" width="31.626837316268368%" id="mcps1.2.5.1.1"><p id="en-us_topic_0201534190_p185312312192"><a name="en-us_topic_0201534190_p185312312192"></a><a name="en-us_topic_0201534190_p185312312192"></a><strong id="en-us_topic_0201534190_b1866897138"><a name="en-us_topic_0201534190_b1866897138"></a><a name="en-us_topic_0201534190_b1866897138"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885708%" id="mcps1.2.5.1.2"><p id="en-us_topic_0201534190_p208531923101913"><a name="en-us_topic_0201534190_p208531923101913"></a><a name="en-us_topic_0201534190_p208531923101913"></a><strong id="en-us_topic_0201534190_b640938415"><a name="en-us_topic_0201534190_b640938415"></a><a name="en-us_topic_0201534190_b640938415"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885708%" id="mcps1.2.5.1.3"><p id="en-us_topic_0201534190_p685312311196"><a name="en-us_topic_0201534190_p685312311196"></a><a name="en-us_topic_0201534190_p685312311196"></a><strong id="en-us_topic_0201534190_b1080233722"><a name="en-us_topic_0201534190_b1080233722"></a><a name="en-us_topic_0201534190_b1080233722"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="39.7960203979602%" id="mcps1.2.5.1.4"><p id="en-us_topic_0201534190_p4853122311199"><a name="en-us_topic_0201534190_p4853122311199"></a><a name="en-us_topic_0201534190_p4853122311199"></a><strong id="en-us_topic_0201534190_b245188100"><a name="en-us_topic_0201534190_b245188100"></a><a name="en-us_topic_0201534190_b245188100"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0201534190_row08532238197"><td class="cellrowborder" valign="top" width="31.626837316268368%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534190_p16854122312191"><a name="en-us_topic_0201534190_p16854122312191"></a><a name="en-us_topic_0201534190_p16854122312191"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885708%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534190_p10854102317195"><a name="en-us_topic_0201534190_p10854102317195"></a><a name="en-us_topic_0201534190_p10854102317195"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885708%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534190_p5854122371919"><a name="en-us_topic_0201534190_p5854122371919"></a><a name="en-us_topic_0201534190_p5854122371919"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0201534190_p085432316193"><a name="en-us_topic_0201534190_p085432316193"></a><a name="en-us_topic_0201534190_p085432316193"></a>Specifies the tag key. The value can contain a maximum of 127 Unicode characters. The tag key cannot be left blank. (This parameter is not verified during the search process.)</p>
    </td>
    </tr>
    <tr id="en-us_topic_0201534190_row15854623141911"><td class="cellrowborder" valign="top" width="31.626837316268368%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534190_p68541223141919"><a name="en-us_topic_0201534190_p68541223141919"></a><a name="en-us_topic_0201534190_p68541223141919"></a>values</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885708%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534190_p17854223161918"><a name="en-us_topic_0201534190_p17854223161918"></a><a name="en-us_topic_0201534190_p17854223161918"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885708%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534190_p188541423181914"><a name="en-us_topic_0201534190_p188541423181914"></a><a name="en-us_topic_0201534190_p188541423181914"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="39.7960203979602%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0201534190_p198541623121914"><a name="en-us_topic_0201534190_p198541623121914"></a><a name="en-us_topic_0201534190_p198541623121914"></a>Specifies the tag value list. Each value can contain a maximum of 255 Unicode characters. An empty list for <strong id="en-us_topic_0201534190_b1957000225"><a name="en-us_topic_0201534190_b1957000225"></a><a name="en-us_topic_0201534190_b1957000225"></a>values</strong> indicates any value. The values are in the OR relationship.</p>
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


## Status Code<a name="en-us_topic_0201534190_section31981619"></a>

See  [Status Codes](status-codes.md#eip_api05_0001).

## Error Code<a name="en-us_topic_0201534190_section85821649202813"></a>

See  [Error Codes](error-codes.md#eip_api05_0002).


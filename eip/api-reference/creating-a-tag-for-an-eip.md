# Creating a Tag for an EIP<a name="eip_apitag_0001"></a>

## Function<a name="en-us_topic_0201534118_section2090011408236"></a>

This API is used to create a tag for an EIP.

## URI<a name="en-us_topic_0201534118_section1690074011233"></a>

POST /v2.0/\{project\_id\}/publicips/\{publicip\_id\}/tags

[Table 1](#en-us_topic_0201534118_table27380479)  describes the parameters.

**Table  1**  Parameter description

<a name="en-us_topic_0201534118_table27380479"></a>
<table><thead align="left"><tr id="en-us_topic_0201534118_row28751554"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534118_p47174532"><a name="en-us_topic_0201534118_p47174532"></a><a name="en-us_topic_0201534118_p47174532"></a><strong id="en-us_topic_0201534118_b1599610319225"><a name="en-us_topic_0201534118_b1599610319225"></a><a name="en-us_topic_0201534118_b1599610319225"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534118_p63040734"><a name="en-us_topic_0201534118_p63040734"></a><a name="en-us_topic_0201534118_p63040734"></a><strong id="en-us_topic_0201534118_b17323135102210"><a name="en-us_topic_0201534118_b17323135102210"></a><a name="en-us_topic_0201534118_b17323135102210"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534118_p6025849"><a name="en-us_topic_0201534118_p6025849"></a><a name="en-us_topic_0201534118_p6025849"></a><strong id="en-us_topic_0201534118_b29655622216"><a name="en-us_topic_0201534118_b29655622216"></a><a name="en-us_topic_0201534118_b29655622216"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0201534118_row18331773"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534118_p8478608"><a name="en-us_topic_0201534118_p8478608"></a><a name="en-us_topic_0201534118_p8478608"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534118_p15678685"><a name="en-us_topic_0201534118_p15678685"></a><a name="en-us_topic_0201534118_p15678685"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534118_p10487112"><a name="en-us_topic_0201534118_p10487112"></a><a name="en-us_topic_0201534118_p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="en-us_topic_0201534118_row21254748"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534118_p43913021"><a name="en-us_topic_0201534118_p43913021"></a><a name="en-us_topic_0201534118_p43913021"></a>publicip_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534118_p184914"><a name="en-us_topic_0201534118_p184914"></a><a name="en-us_topic_0201534118_p184914"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534118_p14978051"><a name="en-us_topic_0201534118_p14978051"></a><a name="en-us_topic_0201534118_p14978051"></a>Specifies the unique identifier of an EIP.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="en-us_topic_0201534118_section1990974032314"></a>

-   Request parameter

    **Table  2**  Request parameter

    <a name="en-us_topic_0201534118_table9909164018236"></a>
    <table><thead align="left"><tr id="en-us_topic_0201534118_row6974154010238"><th class="cellrowborder" valign="top" width="19.6%" id="mcps1.2.5.1.1"><p id="en-us_topic_0201534118_p89741140152312"><a name="en-us_topic_0201534118_p89741140152312"></a><a name="en-us_topic_0201534118_p89741140152312"></a><strong id="en-us_topic_0201534118_b842352706193648"><a name="en-us_topic_0201534118_b842352706193648"></a><a name="en-us_topic_0201534118_b842352706193648"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="13.530000000000001%" id="mcps1.2.5.1.2"><p id="en-us_topic_0201534118_p2974164013235"><a name="en-us_topic_0201534118_p2974164013235"></a><a name="en-us_topic_0201534118_p2974164013235"></a><strong id="en-us_topic_0201534118_b842352706193653"><a name="en-us_topic_0201534118_b842352706193653"></a><a name="en-us_topic_0201534118_b842352706193653"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.36%" id="mcps1.2.5.1.3"><p id="en-us_topic_0201534118_p997410409235"><a name="en-us_topic_0201534118_p997410409235"></a><a name="en-us_topic_0201534118_p997410409235"></a><strong id="en-us_topic_0201534118_b7448114015235"><a name="en-us_topic_0201534118_b7448114015235"></a><a name="en-us_topic_0201534118_b7448114015235"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="47.510000000000005%" id="mcps1.2.5.1.4"><p id="en-us_topic_0201534118_p13974144018230"><a name="en-us_topic_0201534118_p13974144018230"></a><a name="en-us_topic_0201534118_p13974144018230"></a><strong id="en-us_topic_0201534118_b8423527061645"><a name="en-us_topic_0201534118_b8423527061645"></a><a name="en-us_topic_0201534118_b8423527061645"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0201534118_row11974194022315"><td class="cellrowborder" valign="top" width="19.6%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534118_p16974134022320"><a name="en-us_topic_0201534118_p16974134022320"></a><a name="en-us_topic_0201534118_p16974134022320"></a>tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534118_p49755402238"><a name="en-us_topic_0201534118_p49755402238"></a><a name="en-us_topic_0201534118_p49755402238"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.36%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534118_p497516406238"><a name="en-us_topic_0201534118_p497516406238"></a><a name="en-us_topic_0201534118_p497516406238"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.510000000000005%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0201534118_p69751040202314"><a name="en-us_topic_0201534118_p69751040202314"></a><a name="en-us_topic_0201534118_p69751040202314"></a>Specifies the <strong id="en-us_topic_0201534118_b1148724462315"><a name="en-us_topic_0201534118_b1148724462315"></a><a name="en-us_topic_0201534118_b1148724462315"></a>tag</strong> objects. For details, see <a href="#en-us_topic_0201534118_table13242848193719">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **tag**  objects

    <a name="en-us_topic_0201534118_table13242848193719"></a>
    <table><thead align="left"><tr id="en-us_topic_0201534118_row13343144812379"><th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.1"><p id="en-us_topic_0201534118_p15343174853715"><a name="en-us_topic_0201534118_p15343174853715"></a><a name="en-us_topic_0201534118_p15343174853715"></a><strong id="en-us_topic_0201534118_b031616483233"><a name="en-us_topic_0201534118_b031616483233"></a><a name="en-us_topic_0201534118_b031616483233"></a>Attribute</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="18.060000000000002%" id="mcps1.2.5.1.2"><p id="en-us_topic_0201534118_p13431648163716"><a name="en-us_topic_0201534118_p13431648163716"></a><a name="en-us_topic_0201534118_p13431648163716"></a><strong id="en-us_topic_0201534118_b142361349172320"><a name="en-us_topic_0201534118_b142361349172320"></a><a name="en-us_topic_0201534118_b142361349172320"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="12.24%" id="mcps1.2.5.1.3"><p id="en-us_topic_0201534118_p169809965412"><a name="en-us_topic_0201534118_p169809965412"></a><a name="en-us_topic_0201534118_p169809965412"></a><strong id="en-us_topic_0201534118_b1480175017233"><a name="en-us_topic_0201534118_b1480175017233"></a><a name="en-us_topic_0201534118_b1480175017233"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="56.699999999999996%" id="mcps1.2.5.1.4"><p id="en-us_topic_0201534118_p11344748183719"><a name="en-us_topic_0201534118_p11344748183719"></a><a name="en-us_topic_0201534118_p11344748183719"></a><strong id="en-us_topic_0201534118_b79305119235"><a name="en-us_topic_0201534118_b79305119235"></a><a name="en-us_topic_0201534118_b79305119235"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0201534118_row103449487379"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534118_p183469482373"><a name="en-us_topic_0201534118_p183469482373"></a><a name="en-us_topic_0201534118_p183469482373"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.060000000000002%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534118_p1434684863710"><a name="en-us_topic_0201534118_p1434684863710"></a><a name="en-us_topic_0201534118_p1434684863710"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.24%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534118_p298018911544"><a name="en-us_topic_0201534118_p298018911544"></a><a name="en-us_topic_0201534118_p298018911544"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.699999999999996%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0201534118_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul2321196023222"></a><a name="en-us_topic_0201534118_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul2321196023222"></a><ul id="en-us_topic_0201534118_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul2321196023222"><li>Specifies the tag key.</li><li>Cannot be left blank.</li><li>Can contain a maximum of 36 characters.</li><li>Can contain only the following character types:<a name="en-us_topic_0201534118_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul11049850105418"></a><a name="en-us_topic_0201534118_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul11049850105418"></a><ul id="en-us_topic_0201534118_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul11049850105418"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
    </li><li>The tag key of a VPC must be unique.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0201534118_row2346548163714"><td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534118_p1134624816377"><a name="en-us_topic_0201534118_p1134624816377"></a><a name="en-us_topic_0201534118_p1134624816377"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.060000000000002%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534118_p234619483371"><a name="en-us_topic_0201534118_p234619483371"></a><a name="en-us_topic_0201534118_p234619483371"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.24%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534118_p209805915417"><a name="en-us_topic_0201534118_p209805915417"></a><a name="en-us_topic_0201534118_p209805915417"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.699999999999996%" headers="mcps1.2.5.1.4 "><a name="en-us_topic_0201534118_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul6706750105539"></a><a name="en-us_topic_0201534118_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul6706750105539"></a><ul id="en-us_topic_0201534118_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul6706750105539"><li>Specifies the tag value.</li><li>Can contain a maximum of 43 characters.</li><li>Can contain only the following character types:<a name="en-us_topic_0201534118_ul7895160105919"></a><a name="en-us_topic_0201534118_ul7895160105919"></a><ul id="en-us_topic_0201534118_ul7895160105919"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
    </li></ul>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    POST https://{Endpoint}/v2.0/{project_id}/publicips/{publicip_id}/tags
    
    {
        "tag": {
            "key": "key1",
            "value": "value1"
        }
    }
    ```


## Response Message<a name="en-us_topic_0201534118_section691614409232"></a>

-   Response parameter

    None

-   Example response

    None


## Status Code<a name="en-us_topic_0201534118_section31981619"></a>

See  [Status Codes](status-codes.md#eip_api05_0001).

## Error Code<a name="en-us_topic_0201534118_section85821649202813"></a>

See  [Error Codes](error-codes.md#eip_api05_0002).


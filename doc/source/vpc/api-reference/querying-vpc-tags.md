# Querying VPC Tags<a name="vpc_tag_0002"></a>

## Function<a name="section5346624101819"></a>

This API is used to query tags of a specified VPC.

## URI<a name="section7346122401818"></a>

GET /v2.0/\{project\_id\}/vpcs/\{vpc\_id\}/tags

[Table 1](#table27380479)  describes the parameters.

**Table  1**  Parameter description

<a name="table27380479"></a>
<table><thead align="left"><tr id="row28751554"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p47174532"><a name="p47174532"></a><a name="p47174532"></a><strong id="b1056101219361"><a name="b1056101219361"></a><a name="b1056101219361"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p63040734"><a name="p63040734"></a><a name="p63040734"></a><strong id="b2775103313618"><a name="b2775103313618"></a><a name="b2775103313618"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p6025849"><a name="p6025849"></a><a name="p6025849"></a><strong id="b62489370361"><a name="b62489370361"></a><a name="b62489370361"></a>Description</strong></p>
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
<tr id="row21254748"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p43913021"><a name="p43913021"></a><a name="p43913021"></a>vpc_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p184914"><a name="p184914"></a><a name="p184914"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p14978051"><a name="p14978051"></a><a name="p14978051"></a>Specifies the VPC ID, which uniquely identifies the VPC.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section13185925275"></a>

-   Request parameter

    None

-   Example request

    ```
    GET https://{Endpoint}/v2.0/{project_id}/vpcs/{vpc_id}/tags
    ```


## Response Message<a name="section1635502415182"></a>

-   Response parameter

    **Table  2**  Response parameter

    <a name="table1135702419184"></a>
    <table><thead align="left"><tr id="row7424152414187"><th class="cellrowborder" valign="top" width="12.36%" id="mcps1.2.4.1.1"><p id="p14424202481810"><a name="p14424202481810"></a><a name="p14424202481810"></a><strong id="b842352706193648"><a name="b842352706193648"></a><a name="b842352706193648"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="23.51%" id="mcps1.2.4.1.2"><p id="p1442492451817"><a name="p1442492451817"></a><a name="p1442492451817"></a><strong id="b842352706193653"><a name="b842352706193653"></a><a name="b842352706193653"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="64.13%" id="mcps1.2.4.1.3"><p id="p18424202481819"><a name="p18424202481819"></a><a name="p18424202481819"></a><strong id="b8423527061645"><a name="b8423527061645"></a><a name="b8423527061645"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row14424192461816"><td class="cellrowborder" valign="top" width="12.36%" headers="mcps1.2.4.1.1 "><p id="p1942472411816"><a name="p1942472411816"></a><a name="p1942472411816"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.51%" headers="mcps1.2.4.1.2 "><p id="p10424324181820"><a name="p10424324181820"></a><a name="p10424324181820"></a>Array of <a href="#table13242848193719">tag</a> objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.13%" headers="mcps1.2.4.1.3 "><p id="p742482418183"><a name="p742482418183"></a><a name="p742482418183"></a>Specifies the <strong id="b12935194017396"><a name="b12935194017396"></a><a name="b12935194017396"></a>tag</strong> object list. For details, see <a href="#table13242848193719">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **tag**  objects

    <a name="table13242848193719"></a>
    <table><thead align="left"><tr id="row13343144812379"><th class="cellrowborder" valign="top" width="21.33%" id="mcps1.2.4.1.1"><p id="p15343174853715"><a name="p15343174853715"></a><a name="p15343174853715"></a><strong id="b1267574410393"><a name="b1267574410393"></a><a name="b1267574410393"></a>Attribute</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="20%" id="mcps1.2.4.1.2"><p id="p13431648163716"><a name="p13431648163716"></a><a name="p13431648163716"></a><strong id="b1285114453390"><a name="b1285114453390"></a><a name="b1285114453390"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="58.67%" id="mcps1.2.4.1.3"><p id="p11344748183719"><a name="p11344748183719"></a><a name="p11344748183719"></a><strong id="b0938194653911"><a name="b0938194653911"></a><a name="b0938194653911"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row103449487379"><td class="cellrowborder" valign="top" width="21.33%" headers="mcps1.2.4.1.1 "><p id="p183469482373"><a name="p183469482373"></a><a name="p183469482373"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p1434684863710"><a name="p1434684863710"></a><a name="p1434684863710"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.67%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul2321196023222"></a><a name="en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul2321196023222"></a><ul id="en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul2321196023222"><li>Specifies the tag key.</li><li>Cannot be left blank.</li><li>Can contain a maximum of 36 characters.</li><li>Can contain only the following character types:<a name="en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul11049850105418"></a><a name="en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul11049850105418"></a><ul id="en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul11049850105418"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
    </li><li>The tag key of a VPC must be unique.</li></ul>
    </td>
    </tr>
    <tr id="row2346548163714"><td class="cellrowborder" valign="top" width="21.33%" headers="mcps1.2.4.1.1 "><p id="p1134624816377"><a name="p1134624816377"></a><a name="p1134624816377"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.4.1.2 "><p id="p234619483371"><a name="p234619483371"></a><a name="p234619483371"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.67%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul6706750105539"></a><a name="en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul6706750105539"></a><ul id="en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul6706750105539"><li>Specifies the tag value.</li><li>Can contain a maximum of 43 characters.</li><li>Can contain only the following character types:<a name="ul7895160105919"></a><a name="ul7895160105919"></a><ul id="ul7895160105919"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
    </li></ul>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "tags": [
            {
                "key": "key1",
                "value": "value1"
            },
            {
                "key": "key2",
                "value": "value3"
            }
        ]
    }
    ```


## Status Code<a name="section31981619"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).


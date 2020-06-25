# Querying EIP Tags<a name="eip_apitag_0002"></a>

## Function<a name="en-us_topic_0201534160_section131671842412"></a>

This API is used to query tags of a specified EIP.

## URI<a name="en-us_topic_0201534160_section731781892418"></a>

GET /v2.0/\{project\_id\}/publicips/\{publicip\_id\}/tags

[Table 1](#en-us_topic_0201534160_table27380479)  describes the parameters.

**Table  1**  Parameter description

<a name="en-us_topic_0201534160_table27380479"></a>
<table><thead align="left"><tr id="en-us_topic_0201534160_row28751554"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534160_p47174532"><a name="en-us_topic_0201534160_p47174532"></a><a name="en-us_topic_0201534160_p47174532"></a><strong id="en-us_topic_0201534160_b1438819662510"><a name="en-us_topic_0201534160_b1438819662510"></a><a name="en-us_topic_0201534160_b1438819662510"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534160_p63040734"><a name="en-us_topic_0201534160_p63040734"></a><a name="en-us_topic_0201534160_p63040734"></a><strong id="en-us_topic_0201534160_b35652079253"><a name="en-us_topic_0201534160_b35652079253"></a><a name="en-us_topic_0201534160_b35652079253"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534160_p6025849"><a name="en-us_topic_0201534160_p6025849"></a><a name="en-us_topic_0201534160_p6025849"></a><strong id="en-us_topic_0201534160_b65041080254"><a name="en-us_topic_0201534160_b65041080254"></a><a name="en-us_topic_0201534160_b65041080254"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0201534160_row18331773"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534160_p8478608"><a name="en-us_topic_0201534160_p8478608"></a><a name="en-us_topic_0201534160_p8478608"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534160_p15678685"><a name="en-us_topic_0201534160_p15678685"></a><a name="en-us_topic_0201534160_p15678685"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534160_p10487112"><a name="en-us_topic_0201534160_p10487112"></a><a name="en-us_topic_0201534160_p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="en-us_topic_0201534160_row21254748"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534160_p725824594416"><a name="en-us_topic_0201534160_p725824594416"></a><a name="en-us_topic_0201534160_p725824594416"></a>publicip_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534160_p184914"><a name="en-us_topic_0201534160_p184914"></a><a name="en-us_topic_0201534160_p184914"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534160_p14978051"><a name="en-us_topic_0201534160_p14978051"></a><a name="en-us_topic_0201534160_p14978051"></a>Specifies the unique identifier of an EIP.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="en-us_topic_0201534160_section12330418152420"></a>

-   Request parameter

    None

-   Example request

    ```
    GET https://{Endpoint}/v2.0/{project_id}/publicips/{publicip_id}/tags
    ```


## Response Message<a name="en-us_topic_0201534160_section83301318102415"></a>

-   Response parameter

    **Table  2**  Response parameter

    <a name="en-us_topic_0201534160_table2033011815242"></a>
    <table><thead align="left"><tr id="en-us_topic_0201534160_row4392171813241"><th class="cellrowborder" valign="top" width="13.33%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534160_p10392181872410"><a name="en-us_topic_0201534160_p10392181872410"></a><a name="en-us_topic_0201534160_p10392181872410"></a><strong id="en-us_topic_0201534160_b842352706193648"><a name="en-us_topic_0201534160_b842352706193648"></a><a name="en-us_topic_0201534160_b842352706193648"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.11%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534160_p939231813249"><a name="en-us_topic_0201534160_p939231813249"></a><a name="en-us_topic_0201534160_p939231813249"></a><strong id="en-us_topic_0201534160_b842352706193653"><a name="en-us_topic_0201534160_b842352706193653"></a><a name="en-us_topic_0201534160_b842352706193653"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="65.56%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534160_p93927180241"><a name="en-us_topic_0201534160_p93927180241"></a><a name="en-us_topic_0201534160_p93927180241"></a><strong id="en-us_topic_0201534160_b8423527061645"><a name="en-us_topic_0201534160_b8423527061645"></a><a name="en-us_topic_0201534160_b8423527061645"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0201534160_row163921181243"><td class="cellrowborder" valign="top" width="13.33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534160_p1739281812410"><a name="en-us_topic_0201534160_p1739281812410"></a><a name="en-us_topic_0201534160_p1739281812410"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.11%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534160_p1239241812243"><a name="en-us_topic_0201534160_p1239241812243"></a><a name="en-us_topic_0201534160_p1239241812243"></a>Array of <a href="#en-us_topic_0201534160_table13242848193719">tag</a> objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="65.56%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534160_p143926189247"><a name="en-us_topic_0201534160_p143926189247"></a><a name="en-us_topic_0201534160_p143926189247"></a>Specifies the <strong id="en-us_topic_0201534160_b1045416303254"><a name="en-us_topic_0201534160_b1045416303254"></a><a name="en-us_topic_0201534160_b1045416303254"></a>tag</strong> object list. For details, see <a href="#en-us_topic_0201534160_table13242848193719">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **tag**  objects

    <a name="en-us_topic_0201534160_table13242848193719"></a>
    <table><thead align="left"><tr id="en-us_topic_0201534160_row13343144812379"><th class="cellrowborder" valign="top" width="14.78%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534160_p15343174853715"><a name="en-us_topic_0201534160_p15343174853715"></a><a name="en-us_topic_0201534160_p15343174853715"></a><strong id="en-us_topic_0201534160_b124881333122519"><a name="en-us_topic_0201534160_b124881333122519"></a><a name="en-us_topic_0201534160_b124881333122519"></a>Attribute</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.67%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534160_p13431648163716"><a name="en-us_topic_0201534160_p13431648163716"></a><a name="en-us_topic_0201534160_p13431648163716"></a><strong id="en-us_topic_0201534160_b5892038162520"><a name="en-us_topic_0201534160_b5892038162520"></a><a name="en-us_topic_0201534160_b5892038162520"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="65.55%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534160_p11344748183719"><a name="en-us_topic_0201534160_p11344748183719"></a><a name="en-us_topic_0201534160_p11344748183719"></a><strong id="en-us_topic_0201534160_b1355143912513"><a name="en-us_topic_0201534160_b1355143912513"></a><a name="en-us_topic_0201534160_b1355143912513"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0201534160_row103449487379"><td class="cellrowborder" valign="top" width="14.78%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534160_p183469482373"><a name="en-us_topic_0201534160_p183469482373"></a><a name="en-us_topic_0201534160_p183469482373"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.67%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534160_p1434684863710"><a name="en-us_topic_0201534160_p1434684863710"></a><a name="en-us_topic_0201534160_p1434684863710"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65.55%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0201534160_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul2321196023222"></a><a name="en-us_topic_0201534160_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul2321196023222"></a><ul id="en-us_topic_0201534160_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul2321196023222"><li>Specifies the tag key.</li><li>Cannot be left blank.</li><li>Can contain a maximum of 36 characters.</li><li>Can contain only the following character types:<a name="en-us_topic_0201534160_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul11049850105418"></a><a name="en-us_topic_0201534160_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul11049850105418"></a><ul id="en-us_topic_0201534160_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul11049850105418"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
    </li><li>The tag key of a VPC must be unique.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0201534160_row2346548163714"><td class="cellrowborder" valign="top" width="14.78%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534160_p1134624816377"><a name="en-us_topic_0201534160_p1134624816377"></a><a name="en-us_topic_0201534160_p1134624816377"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.67%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534160_p234619483371"><a name="en-us_topic_0201534160_p234619483371"></a><a name="en-us_topic_0201534160_p234619483371"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="65.55%" headers="mcps1.2.4.1.3 "><a name="en-us_topic_0201534160_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul6706750105539"></a><a name="en-us_topic_0201534160_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul6706750105539"></a><ul id="en-us_topic_0201534160_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul6706750105539"><li>Specifies the tag value.</li><li>Can contain a maximum of 43 characters.</li><li>Can contain only the following character types:<a name="en-us_topic_0201534160_ul7895160105919"></a><a name="en-us_topic_0201534160_ul7895160105919"></a><ul id="en-us_topic_0201534160_ul7895160105919"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
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


## Status Code<a name="en-us_topic_0201534160_section31981619"></a>

See  [Status Codes](status-codes.md#eip_api05_0001).

## Error Code<a name="en-us_topic_0201534160_section85821649202813"></a>

See  [Error Codes](error-codes.md#eip_api05_0002).


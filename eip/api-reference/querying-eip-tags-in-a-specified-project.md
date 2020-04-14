# Querying EIP Tags in a Specified Project<a name="eip_apitag_0006"></a>

## Function<a name="en-us_topic_0201534134_section5413192818251"></a>

This API is used to query all EIP tags of a tenant in a specified region.

## URI<a name="en-us_topic_0201534134_section1414182816254"></a>

GET /v2.0/\{project\_id\}/publicips/tags

[Table 1](#en-us_topic_0201534134_table27380479)  describes the parameters.

**Table  1**  Parameter description

<a name="en-us_topic_0201534134_table27380479"></a>
<table><thead align="left"><tr id="en-us_topic_0201534134_row28751554"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534134_p47174532"><a name="en-us_topic_0201534134_p47174532"></a><a name="en-us_topic_0201534134_p47174532"></a><strong id="en-us_topic_0201534134_b9454114443811"><a name="en-us_topic_0201534134_b9454114443811"></a><a name="en-us_topic_0201534134_b9454114443811"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534134_p63040734"><a name="en-us_topic_0201534134_p63040734"></a><a name="en-us_topic_0201534134_p63040734"></a><strong id="en-us_topic_0201534134_b14594114816383"><a name="en-us_topic_0201534134_b14594114816383"></a><a name="en-us_topic_0201534134_b14594114816383"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534134_p6025849"><a name="en-us_topic_0201534134_p6025849"></a><a name="en-us_topic_0201534134_p6025849"></a><strong id="en-us_topic_0201534134_b96221749193811"><a name="en-us_topic_0201534134_b96221749193811"></a><a name="en-us_topic_0201534134_b96221749193811"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0201534134_row18331773"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534134_p8478608"><a name="en-us_topic_0201534134_p8478608"></a><a name="en-us_topic_0201534134_p8478608"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534134_p15678685"><a name="en-us_topic_0201534134_p15678685"></a><a name="en-us_topic_0201534134_p15678685"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534134_p10487112"><a name="en-us_topic_0201534134_p10487112"></a><a name="en-us_topic_0201534134_p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="en-us_topic_0201534134_section1342142882511"></a>

-   Request parameter

    None

-   Example request

    ```
    GET /v2.0/{project_id}/publicips/tags
    ```


## Response Message<a name="en-us_topic_0201534134_section242122862514"></a>

-   Response parameter

    **Table  2**  Response parameter

    <a name="en-us_topic_0201534134_table242418284253"></a>
    <table><thead align="left"><tr id="en-us_topic_0201534134_row155362282252"><th class="cellrowborder" valign="top" width="21.349999999999998%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534134_p65362028192517"><a name="en-us_topic_0201534134_p65362028192517"></a><a name="en-us_topic_0201534134_p65362028192517"></a><strong id="en-us_topic_0201534134_b842352706193648"><a name="en-us_topic_0201534134_b842352706193648"></a><a name="en-us_topic_0201534134_b842352706193648"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="13.48%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534134_p155361728192510"><a name="en-us_topic_0201534134_p155361728192510"></a><a name="en-us_topic_0201534134_p155361728192510"></a><strong id="en-us_topic_0201534134_b842352706193653"><a name="en-us_topic_0201534134_b842352706193653"></a><a name="en-us_topic_0201534134_b842352706193653"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="65.16999999999999%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534134_p1253616288258"><a name="en-us_topic_0201534134_p1253616288258"></a><a name="en-us_topic_0201534134_p1253616288258"></a><strong id="en-us_topic_0201534134_b8423527061645"><a name="en-us_topic_0201534134_b8423527061645"></a><a name="en-us_topic_0201534134_b8423527061645"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0201534134_row65365287254"><td class="cellrowborder" valign="top" width="21.349999999999998%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534134_p553612832513"><a name="en-us_topic_0201534134_p553612832513"></a><a name="en-us_topic_0201534134_p553612832513"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.48%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534134_p1453619282257"><a name="en-us_topic_0201534134_p1453619282257"></a><a name="en-us_topic_0201534134_p1453619282257"></a>Array of <a href="#en-us_topic_0201534134_table043062842515">tag</a> objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="65.16999999999999%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534134_p155364285253"><a name="en-us_topic_0201534134_p155364285253"></a><a name="en-us_topic_0201534134_p155364285253"></a>Specifies the <strong id="en-us_topic_0201534134_b10420185710389"><a name="en-us_topic_0201534134_b10420185710389"></a><a name="en-us_topic_0201534134_b10420185710389"></a>tag</strong> object list. For details, see <a href="#en-us_topic_0201534134_table043062842515">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  Description of the  **tag**  field

    <a name="en-us_topic_0201534134_table043062842515"></a>
    <table><thead align="left"><tr id="en-us_topic_0201534134_en-us_topic_0201534104_row16625112015"><th class="cellrowborder" valign="top" width="25.332533253325334%" id="mcps1.2.4.1.1"><p id="en-us_topic_0201534134_en-us_topic_0201534104_p156216117208"><a name="en-us_topic_0201534134_en-us_topic_0201534104_p156216117208"></a><a name="en-us_topic_0201534134_en-us_topic_0201534104_p156216117208"></a><strong id="en-us_topic_0201534134_en-us_topic_0201534104_b842352706195711"><a name="en-us_topic_0201534134_en-us_topic_0201534104_b842352706195711"></a><a name="en-us_topic_0201534134_en-us_topic_0201534104_b842352706195711"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25.332533253325334%" id="mcps1.2.4.1.2"><p id="en-us_topic_0201534134_en-us_topic_0201534104_p8622172014"><a name="en-us_topic_0201534134_en-us_topic_0201534104_p8622172014"></a><a name="en-us_topic_0201534134_en-us_topic_0201534104_p8622172014"></a><strong id="en-us_topic_0201534134_en-us_topic_0201534104_b842352706145623"><a name="en-us_topic_0201534134_en-us_topic_0201534104_b842352706145623"></a><a name="en-us_topic_0201534134_en-us_topic_0201534104_b842352706145623"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="49.33493349334934%" id="mcps1.2.4.1.3"><p id="en-us_topic_0201534134_en-us_topic_0201534104_p1262101182018"><a name="en-us_topic_0201534134_en-us_topic_0201534104_p1262101182018"></a><a name="en-us_topic_0201534134_en-us_topic_0201534104_p1262101182018"></a><strong id="en-us_topic_0201534134_en-us_topic_0201534104_b937632204"><a name="en-us_topic_0201534134_en-us_topic_0201534104_b937632204"></a><a name="en-us_topic_0201534134_en-us_topic_0201534104_b937632204"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0201534134_en-us_topic_0201534104_row166216192017"><td class="cellrowborder" valign="top" width="25.332533253325334%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534134_en-us_topic_0201534104_p562013203"><a name="en-us_topic_0201534134_en-us_topic_0201534104_p562013203"></a><a name="en-us_topic_0201534134_en-us_topic_0201534104_p562013203"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.332533253325334%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534134_en-us_topic_0201534104_p4621132014"><a name="en-us_topic_0201534134_en-us_topic_0201534104_p4621132014"></a><a name="en-us_topic_0201534134_en-us_topic_0201534104_p4621132014"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.33493349334934%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534134_en-us_topic_0201534104_p3622162019"><a name="en-us_topic_0201534134_en-us_topic_0201534104_p3622162019"></a><a name="en-us_topic_0201534134_en-us_topic_0201534104_p3622162019"></a>Specifies the tag key.</p>
    <a name="en-us_topic_0201534134_en-us_topic_0201534104_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul2321196023222"></a><a name="en-us_topic_0201534134_en-us_topic_0201534104_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul2321196023222"></a><ul id="en-us_topic_0201534134_en-us_topic_0201534104_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul2321196023222"><li>Cannot be left blank.</li><li>Can contain a maximum of 36 characters.</li><li>Can contain only the following character types:<a name="en-us_topic_0201534134_en-us_topic_0201534104_ul17859881507"></a><a name="en-us_topic_0201534134_en-us_topic_0201534104_ul17859881507"></a><ul id="en-us_topic_0201534134_en-us_topic_0201534104_ul17859881507"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
    </li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0201534134_en-us_topic_0201534104_row862171152012"><td class="cellrowborder" valign="top" width="25.332533253325334%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0201534134_en-us_topic_0201534104_p2062312201"><a name="en-us_topic_0201534134_en-us_topic_0201534104_p2062312201"></a><a name="en-us_topic_0201534134_en-us_topic_0201534104_p2062312201"></a>values</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.332533253325334%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0201534134_en-us_topic_0201534104_p7282112319144"><a name="en-us_topic_0201534134_en-us_topic_0201534104_p7282112319144"></a><a name="en-us_topic_0201534134_en-us_topic_0201534104_p7282112319144"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.33493349334934%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0201534134_en-us_topic_0201534104_p166210162014"><a name="en-us_topic_0201534134_en-us_topic_0201534104_p166210162014"></a><a name="en-us_topic_0201534134_en-us_topic_0201534104_p166210162014"></a>Specifies the tag value list.</p>
    <a name="en-us_topic_0201534134_en-us_topic_0201534104_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul6706750105539"></a><a name="en-us_topic_0201534134_en-us_topic_0201534104_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul6706750105539"></a><ul id="en-us_topic_0201534134_en-us_topic_0201534104_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul6706750105539"><li>Can contain a maximum of 43 characters.</li><li>Can contain only the following character types:<a name="en-us_topic_0201534134_en-us_topic_0201534104_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul11049850105418"></a><a name="en-us_topic_0201534134_en-us_topic_0201534104_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul11049850105418"></a><ul id="en-us_topic_0201534134_en-us_topic_0201534104_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul11049850105418"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
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
        ]
    }
    ```


## Status Code<a name="en-us_topic_0201534134_section31981619"></a>

See  [Status Codes](status-codes.md#eip_api05_0001).

## Error Code<a name="en-us_topic_0201534134_section85821649202813"></a>

See  [Error Codes](error-codes.md#eip_api05_0002).


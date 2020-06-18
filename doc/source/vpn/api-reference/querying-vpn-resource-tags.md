# Querying VPN Resource Tags<a name="en_topic_0093011487"></a>

## **Function**<a name="en-us_topic_0103470567_section5346624101819"></a>

This interface is used to query tags of a specified VPN resource.

## URI<a name="en-us_topic_0103470567_section7346122401818"></a>

GET /v2.0/\{project\_id\}/ipsec-site-connections/\{resource\_id\}/tags

>![](/images/icon-note.gif) **NOTE:**   
>In the URI,  **project\_id** indicates the project ID, and **resource\_id**  indicates the target resource ID.  

## Request Message<a name="en-us_topic_0103470567_section113551624161816"></a>

None

## Response Message<a name="en-us_topic_0103470567_section1635502415182"></a>

[Table 1](#en-us_topic_0103470567_table1135702419184)  describes the response parameters.

**Table  1**  Response parameter

<a name="en-us_topic_0103470567_table1135702419184"></a>
<table><thead align="left"><tr id="en-us_topic_0103470567_row7424152414187"><th class="cellrowborder" valign="top" width="22.097790220977902%" id="mcps1.2.4.1.1"><p id="en-us_topic_0103470567_p14424202481810"><a name="en-us_topic_0103470567_p14424202481810"></a><a name="en-us_topic_0103470567_p14424202481810"></a><strong id="b842352706172115"><a name="b842352706172115"></a><a name="b842352706172115"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="28.417158284171585%" id="mcps1.2.4.1.2"><p id="en-us_topic_0103470567_p1442492451817"><a name="en-us_topic_0103470567_p1442492451817"></a><a name="en-us_topic_0103470567_p1442492451817"></a><strong id="b84235270610412"><a name="b84235270610412"></a><a name="b84235270610412"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="49.48505149485052%" id="mcps1.2.4.1.3"><p id="en-us_topic_0103470567_p18424202481819"><a name="en-us_topic_0103470567_p18424202481819"></a><a name="en-us_topic_0103470567_p18424202481819"></a><strong id="b842352706151625"><a name="b842352706151625"></a><a name="b842352706151625"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0103470567_row14424192461816"><td class="cellrowborder" valign="top" width="22.097790220977902%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0103470567_p1942472411816"><a name="en-us_topic_0103470567_p1942472411816"></a><a name="en-us_topic_0103470567_p1942472411816"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="28.417158284171585%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0103470567_p10424324181820"><a name="en-us_topic_0103470567_p10424324181820"></a><a name="en-us_topic_0103470567_p10424324181820"></a>List&lt;resource_tag&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="49.48505149485052%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0103470567_p742482418183"><a name="en-us_topic_0103470567_p742482418183"></a><a name="en-us_topic_0103470567_p742482418183"></a>Specifies the tag list.</p>
</td>
</tr>
</tbody>
</table>

Description of field  **resource\_tag**

<a name="table13242848193719"></a>
<table><thead align="left"><tr id="row13343144812379"><th class="cellrowborder" valign="top" width="25.82%" id="mcps1.1.4.1.1"><p id="p15343174853715"><a name="p15343174853715"></a><a name="p15343174853715"></a><strong id="b84235270617246"><a name="b84235270617246"></a><a name="b84235270617246"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25.28%" id="mcps1.1.4.1.2"><p id="p15643121154020"><a name="p15643121154020"></a><a name="p15643121154020"></a><strong id="b84235270610412_1"><a name="b84235270610412_1"></a><a name="b84235270610412_1"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="48.9%" id="mcps1.1.4.1.3"><p id="p11344748183719"><a name="p11344748183719"></a><a name="p11344748183719"></a><strong id="b842352706151625_1"><a name="b842352706151625_1"></a><a name="b842352706151625_1"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row103449487379"><td class="cellrowborder" valign="top" width="25.82%" headers="mcps1.1.4.1.1 "><p id="p183469482373"><a name="p183469482373"></a><a name="p183469482373"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="25.28%" headers="mcps1.1.4.1.2 "><p id="p18712165919401"><a name="p18712165919401"></a><a name="p18712165919401"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.9%" headers="mcps1.1.4.1.3 "><p id="p11346184819376"><a name="p11346184819376"></a><a name="p11346184819376"></a>Specifies the tag key.</p>
<p id="p166179282045"><a name="p166179282045"></a><a name="p166179282045"></a>The parameter constraints are as follows:</p>
<a name="ul1419712461348"></a><a name="ul1419712461348"></a><ul id="ul1419712461348"><li>Must be unique for a resource.</li><li>Cannot be left blank.</li><li>Can contain a maximum of 36 characters.</li><li>Can contain only the following character types:<a name="ul14203124611419"></a><a name="ul14203124611419"></a><ul id="ul14203124611419"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
</li></ul>
</td>
</tr>
<tr id="row2346548163714"><td class="cellrowborder" valign="top" width="25.82%" headers="mcps1.1.4.1.1 "><p id="p1134624816377"><a name="p1134624816377"></a><a name="p1134624816377"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="25.28%" headers="mcps1.1.4.1.2 "><p id="p81671306414"><a name="p81671306414"></a><a name="p81671306414"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.9%" headers="mcps1.1.4.1.3 "><p id="p534634813374"><a name="p534634813374"></a><a name="p534634813374"></a>Specifies the tag value.</p>
<p id="p9993105613416"><a name="p9993105613416"></a><a name="p9993105613416"></a>The parameter constraints are as follows:</p>
<a name="ul1692049519"></a><a name="ul1692049519"></a><ul id="ul1692049519"><li>Can contain a maximum of 43 characters.</li><li>Can contain only the following character types:<a name="ul5918412520"></a><a name="ul5918412520"></a><ul id="ul5918412520"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
</li></ul>
</td>
</tr>
</tbody>
</table>

## Example<a name="en-us_topic_0103470567_section1836772481820"></a>

-   Example Request

    ```
    GET /v2.0/{project_id}/ipsec-site-connections/{resource_id}/tags
    ```


-   Example Response

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


## Returned Values<a name="section14121248103610"></a>

For details, see section  [Common Returned Values](common-returned-values.md).


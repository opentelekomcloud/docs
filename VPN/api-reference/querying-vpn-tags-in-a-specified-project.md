# Querying VPN Tags in a Specified Project<a name="en_topic_0093011489"></a>

## **Function**<a name="en-us_topic_0103470571_section159501022015"></a>

This interface is used to query all tags of a VPN in a specified region.

## URI<a name="en-us_topic_0103470571_section13950150202019"></a>

GET /v2.0/\{project\_id\}/ipsec-site-connections/tags

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>In the URI,  **project\_id**  indicates the project ID.  

## Request Message<a name="en-us_topic_0103470571_section159561804206"></a>

None

## Response Message<a name="en-us_topic_0103470571_section4956302200"></a>

[Table 1](#en-us_topic_0103470571_table18958160152014)  describes the response parameters.

**Table  1**  Response parameter

<a name="en-us_topic_0103470571_table18958160152014"></a>
<table><thead align="left"><tr id="en-us_topic_0103470571_row106121102012"><th class="cellrowborder" valign="top" width="25.369999999999997%" id="mcps1.2.4.1.1"><p id="en-us_topic_0103470571_p14611716203"><a name="en-us_topic_0103470571_p14611716203"></a><a name="en-us_topic_0103470571_p14611716203"></a><strong id="b842352706172115"><a name="b842352706172115"></a><a name="b842352706172115"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="24.66%" id="mcps1.2.4.1.2"><p id="en-us_topic_0103470571_p8613112202"><a name="en-us_topic_0103470571_p8613112202"></a><a name="en-us_topic_0103470571_p8613112202"></a><strong id="b84235270610412"><a name="b84235270610412"></a><a name="b84235270610412"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="49.97%" id="mcps1.2.4.1.3"><p id="en-us_topic_0103470571_p062121192014"><a name="en-us_topic_0103470571_p062121192014"></a><a name="en-us_topic_0103470571_p062121192014"></a><strong id="b842352706151625"><a name="b842352706151625"></a><a name="b842352706151625"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0103470571_row96219162018"><td class="cellrowborder" valign="top" width="25.369999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0103470571_p16624112203"><a name="en-us_topic_0103470571_p16624112203"></a><a name="en-us_topic_0103470571_p16624112203"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="24.66%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0103470571_p146212172016"><a name="en-us_topic_0103470571_p146212172016"></a><a name="en-us_topic_0103470571_p146212172016"></a>List&lt;tag&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="49.97%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0103470571_p46214112203"><a name="en-us_topic_0103470571_p46214112203"></a><a name="en-us_topic_0103470571_p46214112203"></a>Specifies the tag list.</p>
</td>
</tr>
</tbody>
</table>

-   Description of field  **tag**

<a name="en-us_topic_0103470571_table1696410062019"></a>
<table><thead align="left"><tr id="en-us_topic_0103470571_row16625112015"><th class="cellrowborder" valign="top" width="25.332533253325334%" id="mcps1.1.4.1.1"><p id="en-us_topic_0103470571_p156216117208"><a name="en-us_topic_0103470571_p156216117208"></a><a name="en-us_topic_0103470571_p156216117208"></a><strong id="b84235270617246"><a name="b84235270617246"></a><a name="b84235270617246"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25.332533253325334%" id="mcps1.1.4.1.2"><p id="en-us_topic_0103470571_p8622172014"><a name="en-us_topic_0103470571_p8622172014"></a><a name="en-us_topic_0103470571_p8622172014"></a><strong>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="49.33493349334934%" id="mcps1.1.4.1.3"><p id="en-us_topic_0103470571_p1262101182018"><a name="en-us_topic_0103470571_p1262101182018"></a><a name="en-us_topic_0103470571_p1262101182018"></a><strong id="b842352706151625_1"><a name="b842352706151625_1"></a><a name="b842352706151625_1"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0103470571_row166216192017"><td class="cellrowborder" valign="top" width="25.332533253325334%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0103470571_p562013203"><a name="en-us_topic_0103470571_p562013203"></a><a name="en-us_topic_0103470571_p562013203"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="25.332533253325334%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0103470571_p4621132014"><a name="en-us_topic_0103470571_p4621132014"></a><a name="en-us_topic_0103470571_p4621132014"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.33493349334934%" headers="mcps1.1.4.1.3 "><p id="p3622162019"><a name="p3622162019"></a><a name="p3622162019"></a>Specifies the tag key.</p>
<p id="p10244191781016"><a name="p10244191781016"></a><a name="p10244191781016"></a>The parameter constraints are as follows:</p>
<a name="en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul2321196023222"></a><a name="en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul2321196023222"></a><ul id="en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul2321196023222"><li>Cannot be left blank.</li><li>Can contain a maximum of 36 characters.</li><li>Can contain only the following character types:<a name="en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul11049850105418"></a><a name="en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul11049850105418"></a><ul id="en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul11049850105418"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
</li></ul>
</td>
</tr>
<tr id="en-us_topic_0103470571_row862171152012"><td class="cellrowborder" valign="top" width="25.332533253325334%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0103470571_p2062312201"><a name="en-us_topic_0103470571_p2062312201"></a><a name="en-us_topic_0103470571_p2062312201"></a>values</p>
</td>
<td class="cellrowborder" valign="top" width="25.332533253325334%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0103470571_p10628182012"><a name="en-us_topic_0103470571_p10628182012"></a><a name="en-us_topic_0103470571_p10628182012"></a>List&lt;String&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="49.33493349334934%" headers="mcps1.1.4.1.3 "><p id="p166210162014"><a name="p166210162014"></a><a name="p166210162014"></a>Specifies the tag value list.</p>
<p id="p12611163291010"><a name="p12611163291010"></a><a name="p12611163291010"></a>The parameter constraints are as follows:</p>
<a name="en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul6706750105539"></a><a name="en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul6706750105539"></a><ul id="en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul6706750105539"><li>Can contain a maximum of 43 characters.</li><li>Can contain only the following character types:<a name="en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul4359364711615"></a><a name="en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul4359364711615"></a><ul id="en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul4359364711615"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
</li></ul>
</td>
</tr>
</tbody>
</table>

## Example<a name="en-us_topic_0103470571_section1897413016206"></a>

-   Example Request

    ```
    GET /v2.0/{project_id}/ipsec-site-connections/tags
    ```


-   Example Response

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


## Returned Values<a name="section14121248103610"></a>

For details, see section  [Common Returned Values](common-returned-values.md).


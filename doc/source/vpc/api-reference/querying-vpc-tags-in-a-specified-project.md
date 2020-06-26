# Querying VPC Tags in a Specified Project<a name="vpc_tag_0006"></a>

## Function<a name="section159501022015"></a>

This API is used to query all VPC tags of a tenant in a specified region.

## URI<a name="section13950150202019"></a>

GET /v2.0/\{project\_id\}/vpcs/tags

[Table 1](#table27380479)  describes the parameters.

**Table  1**  Parameter description

<a name="table27380479"></a>
<table><thead align="left"><tr id="row28751554"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p47174532"><a name="p47174532"></a><a name="p47174532"></a><strong id="b17453571447"><a name="b17453571447"></a><a name="b17453571447"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p63040734"><a name="p63040734"></a><a name="p63040734"></a><strong id="b17999101312415"><a name="b17999101312415"></a><a name="b17999101312415"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p6025849"><a name="p6025849"></a><a name="p6025849"></a><strong id="b197686175413"><a name="b197686175413"></a><a name="b197686175413"></a>Description</strong></p>
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

## Request Message<a name="section159561804206"></a>

Request parameter

None

Example request

```
GET https://{Endpoint}/v2.0/{project_id}/vpcs/tags
```

## Response Message<a name="section4956302200"></a>

Response parameter

**Table  2**  Response parameter

<a name="table18958160152014"></a>
<table><thead align="left"><tr id="row106121102012"><th class="cellrowborder" valign="top" width="21.349999999999998%" id="mcps1.2.4.1.1"><p id="p14611716203"><a name="p14611716203"></a><a name="p14611716203"></a><strong id="b842352706193648"><a name="b842352706193648"></a><a name="b842352706193648"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="13.48%" id="mcps1.2.4.1.2"><p id="p8613112202"><a name="p8613112202"></a><a name="p8613112202"></a><strong id="b842352706193653"><a name="b842352706193653"></a><a name="b842352706193653"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="65.16999999999999%" id="mcps1.2.4.1.3"><p id="p062121192014"><a name="p062121192014"></a><a name="p062121192014"></a><strong id="b8423527061645"><a name="b8423527061645"></a><a name="b8423527061645"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row96219162018"><td class="cellrowborder" valign="top" width="21.349999999999998%" headers="mcps1.2.4.1.1 "><p id="p16624112203"><a name="p16624112203"></a><a name="p16624112203"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="13.48%" headers="mcps1.2.4.1.2 "><p id="p146212172016"><a name="p146212172016"></a><a name="p146212172016"></a>Array of <a href="#table1696410062019">tag</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="65.16999999999999%" headers="mcps1.2.4.1.3 "><p id="p46214112203"><a name="p46214112203"></a><a name="p46214112203"></a>Specifies the tag list.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Description of the  **tag**  field

<a name="table1696410062019"></a>
<table><thead align="left"><tr id="row16625112015"><th class="cellrowborder" valign="top" width="25.332533253325334%" id="mcps1.2.4.1.1"><p id="p156216117208"><a name="p156216117208"></a><a name="p156216117208"></a><strong id="b842352706195711"><a name="b842352706195711"></a><a name="b842352706195711"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25.332533253325334%" id="mcps1.2.4.1.2"><p id="p8622172014"><a name="p8622172014"></a><a name="p8622172014"></a><strong id="b842352706145623"><a name="b842352706145623"></a><a name="b842352706145623"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="49.33493349334934%" id="mcps1.2.4.1.3"><p id="p1262101182018"><a name="p1262101182018"></a><a name="p1262101182018"></a><strong id="b937632204"><a name="b937632204"></a><a name="b937632204"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row166216192017"><td class="cellrowborder" valign="top" width="25.332533253325334%" headers="mcps1.2.4.1.1 "><p id="p562013203"><a name="p562013203"></a><a name="p562013203"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="25.332533253325334%" headers="mcps1.2.4.1.2 "><p id="p4621132014"><a name="p4621132014"></a><a name="p4621132014"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.33493349334934%" headers="mcps1.2.4.1.3 "><p id="p3622162019"><a name="p3622162019"></a><a name="p3622162019"></a>Specifies the tag key.</p>
<a name="en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul2321196023222"></a><a name="en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul2321196023222"></a><ul id="en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul2321196023222"><li>Cannot be left blank.</li><li>Can contain a maximum of 36 characters.</li><li>Can contain only the following character types:<a name="ul17859881507"></a><a name="ul17859881507"></a><ul id="ul17859881507"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
</li></ul>
</td>
</tr>
<tr id="row862171152012"><td class="cellrowborder" valign="top" width="25.332533253325334%" headers="mcps1.2.4.1.1 "><p id="p2062312201"><a name="p2062312201"></a><a name="p2062312201"></a>values</p>
</td>
<td class="cellrowborder" valign="top" width="25.332533253325334%" headers="mcps1.2.4.1.2 "><p id="p7282112319144"><a name="p7282112319144"></a><a name="p7282112319144"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="49.33493349334934%" headers="mcps1.2.4.1.3 "><p id="p166210162014"><a name="p166210162014"></a><a name="p166210162014"></a>Specifies the tag value list.</p>
<a name="en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul6706750105539"></a><a name="en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul6706750105539"></a><ul id="en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul6706750105539"><li>Can contain a maximum of 43 characters.</li><li>Can contain only the following character types:<a name="en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul11049850105418"></a><a name="en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul11049850105418"></a><ul id="en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul11049850105418"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
</li></ul>
</td>
</tr>
</tbody>
</table>

Example response

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

## Status Code<a name="section31981619"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).


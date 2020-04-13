# Querying Subnet Tags in a Specified Project<a name="subnet_tag_0006"></a>

## Function<a name="section188355782213"></a>

This API is used to query all subnet tags of a tenant in a specified region.

## URI<a name="section12884125719224"></a>

GET /v2.0/\{project\_id\}/subnets/tags

[Table 1](#table27380479)  describes the parameters.

**Table  1**  Parameter description

<a name="table27380479"></a>
<table><thead align="left"><tr id="row28751554"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p47174532"><a name="p47174532"></a><a name="p47174532"></a><strong id="b514011585194"><a name="b514011585194"></a><a name="b514011585194"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p63040734"><a name="p63040734"></a><a name="p63040734"></a><strong id="b353515411189"><a name="b353515411189"></a><a name="b353515411189"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p6025849"><a name="p6025849"></a><a name="p6025849"></a><strong id="b1312110114208"><a name="b1312110114208"></a><a name="b1312110114208"></a>Description</strong></p>
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

## Request Message<a name="section0889135742214"></a>

Request parameter

None

Example request

```
GET https://{Endpoint}/v2.0/{project_id}/subnets/tags
```

## Response Message<a name="section3890155792217"></a>

Response parameter

**Table  2**  Response parameter

<a name="table6892185716224"></a>
<table><thead align="left"><tr id="row1999955717227"><th class="cellrowborder" valign="top" width="21.349999999999998%" id="mcps1.2.4.1.1"><p id="p1299917572228"><a name="p1299917572228"></a><a name="p1299917572228"></a><strong id="b842352706193648"><a name="b842352706193648"></a><a name="b842352706193648"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="13.48%" id="mcps1.2.4.1.2"><p id="p1299975702210"><a name="p1299975702210"></a><a name="p1299975702210"></a><strong id="b842352706193653"><a name="b842352706193653"></a><a name="b842352706193653"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="65.16999999999999%" id="mcps1.2.4.1.3"><p id="p1499945718227"><a name="p1499945718227"></a><a name="p1499945718227"></a><strong id="b8423527061645"><a name="b8423527061645"></a><a name="b8423527061645"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row59996579220"><td class="cellrowborder" valign="top" width="21.349999999999998%" headers="mcps1.2.4.1.1 "><p id="p5999457172219"><a name="p5999457172219"></a><a name="p5999457172219"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="13.48%" headers="mcps1.2.4.1.2 "><p id="p799918579221"><a name="p799918579221"></a><a name="p799918579221"></a>Array of <a href="#table98981570229">tag</a> objects</p>
</td>
<td class="cellrowborder" valign="top" width="65.16999999999999%" headers="mcps1.2.4.1.3 "><p id="p139998570229"><a name="p139998570229"></a><a name="p139998570229"></a>Specifies the <strong id="b1315215214206"><a name="b1315215214206"></a><a name="b1315215214206"></a>tag</strong> object list. For details, see <a href="#table98981570229">Table 3</a>.</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Description of the  **tag**  field

<a name="table98981570229"></a>
<table><thead align="left"><tr id="vpc_tag_0006_row16625112015"><th class="cellrowborder" valign="top" width="25.332533253325334%" id="mcps1.2.4.1.1"><p id="vpc_tag_0006_p156216117208"><a name="vpc_tag_0006_p156216117208"></a><a name="vpc_tag_0006_p156216117208"></a><strong id="vpc_tag_0006_b842352706195711"><a name="vpc_tag_0006_b842352706195711"></a><a name="vpc_tag_0006_b842352706195711"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25.332533253325334%" id="mcps1.2.4.1.2"><p id="vpc_tag_0006_p8622172014"><a name="vpc_tag_0006_p8622172014"></a><a name="vpc_tag_0006_p8622172014"></a><strong id="vpc_tag_0006_b842352706145623"><a name="vpc_tag_0006_b842352706145623"></a><a name="vpc_tag_0006_b842352706145623"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="49.33493349334934%" id="mcps1.2.4.1.3"><p id="vpc_tag_0006_p1262101182018"><a name="vpc_tag_0006_p1262101182018"></a><a name="vpc_tag_0006_p1262101182018"></a><strong id="vpc_tag_0006_b937632204"><a name="vpc_tag_0006_b937632204"></a><a name="vpc_tag_0006_b937632204"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="vpc_tag_0006_row166216192017"><td class="cellrowborder" valign="top" width="25.332533253325334%" headers="mcps1.2.4.1.1 "><p id="vpc_tag_0006_p562013203"><a name="vpc_tag_0006_p562013203"></a><a name="vpc_tag_0006_p562013203"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="25.332533253325334%" headers="mcps1.2.4.1.2 "><p id="vpc_tag_0006_p4621132014"><a name="vpc_tag_0006_p4621132014"></a><a name="vpc_tag_0006_p4621132014"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="49.33493349334934%" headers="mcps1.2.4.1.3 "><p id="vpc_tag_0006_p3622162019"><a name="vpc_tag_0006_p3622162019"></a><a name="vpc_tag_0006_p3622162019"></a>Specifies the tag key.</p>
<a name="vpc_tag_0006_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul2321196023222"></a><a name="vpc_tag_0006_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul2321196023222"></a><ul id="vpc_tag_0006_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul2321196023222"><li>Cannot be left blank.</li><li>Can contain a maximum of 36 characters.</li><li>Can contain only the following character types:<a name="vpc_tag_0006_ul17859881507"></a><a name="vpc_tag_0006_ul17859881507"></a><ul id="vpc_tag_0006_ul17859881507"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
</li></ul>
</td>
</tr>
<tr id="vpc_tag_0006_row862171152012"><td class="cellrowborder" valign="top" width="25.332533253325334%" headers="mcps1.2.4.1.1 "><p id="vpc_tag_0006_p2062312201"><a name="vpc_tag_0006_p2062312201"></a><a name="vpc_tag_0006_p2062312201"></a>values</p>
</td>
<td class="cellrowborder" valign="top" width="25.332533253325334%" headers="mcps1.2.4.1.2 "><p id="vpc_tag_0006_p7282112319144"><a name="vpc_tag_0006_p7282112319144"></a><a name="vpc_tag_0006_p7282112319144"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="49.33493349334934%" headers="mcps1.2.4.1.3 "><p id="vpc_tag_0006_p166210162014"><a name="vpc_tag_0006_p166210162014"></a><a name="vpc_tag_0006_p166210162014"></a>Specifies the tag value list.</p>
<a name="vpc_tag_0006_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul6706750105539"></a><a name="vpc_tag_0006_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul6706750105539"></a><ul id="vpc_tag_0006_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul6706750105539"><li>Can contain a maximum of 43 characters.</li><li>Can contain only the following character types:<a name="vpc_tag_0006_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul11049850105418"></a><a name="vpc_tag_0006_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul11049850105418"></a><ul id="vpc_tag_0006_en-us_topic_0013935842_en-us_topic_0067805752_en-us_topic_0013859511_ul11049850105418"><li>Uppercase letters</li><li>Lowercase letters</li><li>Digits</li><li>Special characters, including hyphens (-) and underscores (_)</li></ul>
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


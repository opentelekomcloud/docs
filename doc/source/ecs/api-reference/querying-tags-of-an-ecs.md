# Querying Tags of an ECS<a name="EN-US_TOPIC_0167811967"></a>

## Function<a name="en-us_topic_0096282703_section192222559445"></a>

-   This API is used to query the tags of a specified ECS.
-   The Tag Management Service \(TMS\) uses this API to query all tags of an ECS.

## URI<a name="en-us_topic_0096282703_section222245513448"></a>

GET /v1/\{project\_id\}/cloudservers/\{server\_id\}/tags

[Table 1](#en-us_topic_0096282703_table431622145919)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="en-us_topic_0096282703_table431622145919"></a>
<table><thead align="left"><tr id="en-us_topic_0096282703_row1331652135919"><th class="cellrowborder" valign="top" width="16.96%" id="mcps1.2.4.1.1"><p id="en-us_topic_0096282703_p7707213"><a name="en-us_topic_0096282703_p7707213"></a><a name="en-us_topic_0096282703_p7707213"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.11%" id="mcps1.2.4.1.2"><p id="en-us_topic_0096282703_p20304554"><a name="en-us_topic_0096282703_p20304554"></a><a name="en-us_topic_0096282703_p20304554"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.93%" id="mcps1.2.4.1.3"><p id="en-us_topic_0096282703_p34056167"><a name="en-us_topic_0096282703_p34056167"></a><a name="en-us_topic_0096282703_p34056167"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0096282703_row19316172118595"><td class="cellrowborder" valign="top" width="16.96%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096282703_p1531602118592"><a name="en-us_topic_0096282703_p1531602118592"></a><a name="en-us_topic_0096282703_p1531602118592"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096282703_p0316521195914"><a name="en-us_topic_0096282703_p0316521195914"></a><a name="en-us_topic_0096282703_p0316521195914"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.93%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096282703_p37593705"><a name="en-us_topic_0096282703_p37593705"></a><a name="en-us_topic_0096282703_p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0096282703_row333372112590"><td class="cellrowborder" valign="top" width="16.96%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096282703_p2333142117596"><a name="en-us_topic_0096282703_p2333142117596"></a><a name="en-us_topic_0096282703_p2333142117596"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096282703_p13333152110598"><a name="en-us_topic_0096282703_p13333152110598"></a><a name="en-us_topic_0096282703_p13333152110598"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.93%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096282703_p16333021165919"><a name="en-us_topic_0096282703_p16333021165919"></a><a name="en-us_topic_0096282703_p16333021165919"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0096282703_section625475584419"></a>

None

## Response<a name="en-us_topic_0096282703_section1825415515447"></a>

[Table 2](#en-us_topic_0096282703_table725495518449)  describes the response parameters.

**Table  2**  Response parameters

<a name="en-us_topic_0096282703_table725495518449"></a>
<table><thead align="left"><tr id="en-us_topic_0096282703_row3363185511442"><th class="cellrowborder" valign="top" width="16.650000000000002%" id="mcps1.2.4.1.1"><p id="en-us_topic_0096282703_p15806308"><a name="en-us_topic_0096282703_p15806308"></a><a name="en-us_topic_0096282703_p15806308"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.040000000000003%" id="mcps1.2.4.1.2"><p id="en-us_topic_0096282703_p21995508"><a name="en-us_topic_0096282703_p21995508"></a><a name="en-us_topic_0096282703_p21995508"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="64.31%" id="mcps1.2.4.1.3"><p id="en-us_topic_0096282703_p36805753"><a name="en-us_topic_0096282703_p36805753"></a><a name="en-us_topic_0096282703_p36805753"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0096282703_row4363105574411"><td class="cellrowborder" valign="top" width="16.650000000000002%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096282703_p73639556446"><a name="en-us_topic_0096282703_p73639556446"></a><a name="en-us_topic_0096282703_p73639556446"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="19.040000000000003%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096282703_p103634552442"><a name="en-us_topic_0096282703_p103634552442"></a><a name="en-us_topic_0096282703_p103634552442"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="64.31%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096282703_p53631955194415"><a name="en-us_topic_0096282703_p53631955194415"></a><a name="en-us_topic_0096282703_p53631955194415"></a>Specifies tags.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **resource\_tag**  field description

<a name="en-us_topic_0096282703_table109271241135919"></a>
<table><thead align="left"><tr id="en-us_topic_0096282703_row14941114111598"><th class="cellrowborder" valign="top" width="16.72%" id="mcps1.2.4.1.1"><p id="en-us_topic_0096282703_p1729465314372"><a name="en-us_topic_0096282703_p1729465314372"></a><a name="en-us_topic_0096282703_p1729465314372"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19%" id="mcps1.2.4.1.2"><p id="en-us_topic_0096282703_p14294105313378"><a name="en-us_topic_0096282703_p14294105313378"></a><a name="en-us_topic_0096282703_p14294105313378"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="64.28%" id="mcps1.2.4.1.3"><p id="en-us_topic_0096282703_p6294105323712"><a name="en-us_topic_0096282703_p6294105323712"></a><a name="en-us_topic_0096282703_p6294105323712"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0096282703_row39411541145917"><td class="cellrowborder" valign="top" width="16.72%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096282703_p69411241145914"><a name="en-us_topic_0096282703_p69411241145914"></a><a name="en-us_topic_0096282703_p69411241145914"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096282703_p19419419593"><a name="en-us_topic_0096282703_p19419419593"></a><a name="en-us_topic_0096282703_p19419419593"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.28%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096282703_p39411241195914"><a name="en-us_topic_0096282703_p39411241195914"></a><a name="en-us_topic_0096282703_p39411241195914"></a>Specifies the tag key.</p>
</td>
</tr>
<tr id="en-us_topic_0096282703_row3941204116599"><td class="cellrowborder" valign="top" width="16.72%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0096282703_p69412416595"><a name="en-us_topic_0096282703_p69412416595"></a><a name="en-us_topic_0096282703_p69412416595"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="19%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0096282703_p119411341165912"><a name="en-us_topic_0096282703_p119411341165912"></a><a name="en-us_topic_0096282703_p119411341165912"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.28%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0096282703_p6941104116591"><a name="en-us_topic_0096282703_p6941104116591"></a><a name="en-us_topic_0096282703_p6941104116591"></a>Specifies the tag value.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="en-us_topic_0096282703_section869483985113"></a>

```
GET https://{endpoint}/v1/{project_id}/cloudservers/{server_id}/tags
```

## Example Response<a name="section11189250192212"></a>

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

## Returned Values<a name="en-us_topic_0096282703_en-us_topic_0092803065_en-us_topic_0020212692_section22960139"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

## Error Codes<a name="en-us_topic_0096282703_en-us_topic_0092803065_en-us_topic_0067161469_en-us_topic_0057973179_section23611955"></a>

See  [Error Code Description](error-code-description.md).


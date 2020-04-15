# Querying ECS Tags \(Discarded\)<a name="EN-US_TOPIC_0096282703"></a>

## Function<a name="section192222559445"></a>

-   This API is used to query the tags of a specified ECS.
-   The Tag Management Service \(TMS\) uses this API to query all tags of an ECS.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>You are suggested to use the API described in  [Querying Tags of an ECS](querying-tags-of-an-ecs.md).  

## URI<a name="section222245513448"></a>

GET /v1/\{project\_id\}/servers/\{server\_id\}/tags

[Table 1](#table431622145919)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table431622145919"></a>
<table><thead align="left"><tr id="row1331652135919"><th class="cellrowborder" valign="top" width="16.400000000000002%" id="mcps1.2.4.1.1"><p id="p7707213"><a name="p7707213"></a><a name="p7707213"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.119999999999997%" id="mcps1.2.4.1.2"><p id="p20304554"><a name="p20304554"></a><a name="p20304554"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="66.47999999999999%" id="mcps1.2.4.1.3"><p id="p34056167"><a name="p34056167"></a><a name="p34056167"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row19316172118595"><td class="cellrowborder" valign="top" width="16.400000000000002%" headers="mcps1.2.4.1.1 "><p id="p1531602118592"><a name="p1531602118592"></a><a name="p1531602118592"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.119999999999997%" headers="mcps1.2.4.1.2 "><p id="p0316521195914"><a name="p0316521195914"></a><a name="p0316521195914"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.47999999999999%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row333372112590"><td class="cellrowborder" valign="top" width="16.400000000000002%" headers="mcps1.2.4.1.1 "><p id="p2333142117596"><a name="p2333142117596"></a><a name="p2333142117596"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.119999999999997%" headers="mcps1.2.4.1.2 "><p id="p13333152110598"><a name="p13333152110598"></a><a name="p13333152110598"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.47999999999999%" headers="mcps1.2.4.1.3 "><p id="p16333021165919"><a name="p16333021165919"></a><a name="p16333021165919"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section625475584419"></a>

None

## Response<a name="section1825415515447"></a>

[Table 2](#table725495518449)  describes the response parameters.

**Table  2**  Response parameters

<a name="table725495518449"></a>
<table><thead align="left"><tr id="row3363185511442"><th class="cellrowborder" valign="top" width="21.529999999999998%" id="mcps1.2.4.1.1"><p id="p15806308"><a name="p15806308"></a><a name="p15806308"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.2.4.1.2"><p id="p21995508"><a name="p21995508"></a><a name="p21995508"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="52.470000000000006%" id="mcps1.2.4.1.3"><p id="p36805753"><a name="p36805753"></a><a name="p36805753"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row4363105574411"><td class="cellrowborder" valign="top" width="21.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p73639556446"><a name="p73639556446"></a><a name="p73639556446"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.2.4.1.2 "><p id="p103634552442"><a name="p103634552442"></a><a name="p103634552442"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="52.470000000000006%" headers="mcps1.2.4.1.3 "><p id="p53631955194415"><a name="p53631955194415"></a><a name="p53631955194415"></a>Specifies the tag list.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **resource\_tag**  field description

<a name="table109271241135919"></a>
<table><thead align="left"><tr id="row14941114111598"><th class="cellrowborder" valign="top" width="21.61%" id="mcps1.2.4.1.1"><p id="p1729465314372"><a name="p1729465314372"></a><a name="p1729465314372"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25.96%" id="mcps1.2.4.1.2"><p id="p14294105313378"><a name="p14294105313378"></a><a name="p14294105313378"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="52.43%" id="mcps1.2.4.1.3"><p id="p6294105323712"><a name="p6294105323712"></a><a name="p6294105323712"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row39411541145917"><td class="cellrowborder" valign="top" width="21.61%" headers="mcps1.2.4.1.1 "><p id="p69411241145914"><a name="p69411241145914"></a><a name="p69411241145914"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="25.96%" headers="mcps1.2.4.1.2 "><p id="p19419419593"><a name="p19419419593"></a><a name="p19419419593"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.43%" headers="mcps1.2.4.1.3 "><p id="p39411241195914"><a name="p39411241195914"></a><a name="p39411241195914"></a>Specifies the tag key.</p>
</td>
</tr>
<tr id="row3941204116599"><td class="cellrowborder" valign="top" width="21.61%" headers="mcps1.2.4.1.1 "><p id="p69412416595"><a name="p69412416595"></a><a name="p69412416595"></a>value</p>
</td>
<td class="cellrowborder" valign="top" width="25.96%" headers="mcps1.2.4.1.2 "><p id="p119411341165912"><a name="p119411341165912"></a><a name="p119411341165912"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="52.43%" headers="mcps1.2.4.1.3 "><p id="p6941104116591"><a name="p6941104116591"></a><a name="p6941104116591"></a>Specifies the tag value.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="section869483985113"></a>

```
GET https://{endpoint}/v1/{project_id}/servers/{server_id}/tags
```

## Example Response<a name="section3731945154014"></a>

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

## Returned Values<a name="en-us_topic_0092803065_en-us_topic_0020212692_section22960139"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

## Error Codes<a name="en-us_topic_0092803065_en-us_topic_0067161469_en-us_topic_0057973179_section23611955"></a>

See  [Error Code Description](error-code-description.md).


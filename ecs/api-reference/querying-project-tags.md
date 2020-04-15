# Querying Project Tags<a name="EN-US_TOPIC_0167811966"></a>

## Function<a name="en-us_topic_0102606094_section192222559445"></a>

Projects are used to group and isolate OpenStack resources, which include computing, storage, and network resources. A project can be a department or a team. Multiple projects can be created under one account.

This API is used to query all tags used by a user in a specified project.

## URI<a name="en-us_topic_0102606094_section222245513448"></a>

GET /v1/\{project\_id\}/cloudservers/tags

[Table 1](#en-us_topic_0102606094_table144382516421)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="en-us_topic_0102606094_table144382516421"></a>
<table><thead align="left"><tr id="en-us_topic_0102606094_row134312517423"><th class="cellrowborder" valign="top" width="16.85%" id="mcps1.2.4.1.1"><p id="en-us_topic_0102606094_p7707213"><a name="en-us_topic_0102606094_p7707213"></a><a name="en-us_topic_0102606094_p7707213"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.68%" id="mcps1.2.4.1.2"><p id="en-us_topic_0102606094_p20304554"><a name="en-us_topic_0102606094_p20304554"></a><a name="en-us_topic_0102606094_p20304554"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.47%" id="mcps1.2.4.1.3"><p id="en-us_topic_0102606094_p34056167"><a name="en-us_topic_0102606094_p34056167"></a><a name="en-us_topic_0102606094_p34056167"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0102606094_row259142515428"><td class="cellrowborder" valign="top" width="16.85%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0102606094_p1859102519426"><a name="en-us_topic_0102606094_p1859102519426"></a><a name="en-us_topic_0102606094_p1859102519426"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.68%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0102606094_p135962520420"><a name="en-us_topic_0102606094_p135962520420"></a><a name="en-us_topic_0102606094_p135962520420"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.47%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0102606094_p37593705"><a name="en-us_topic_0102606094_p37593705"></a><a name="en-us_topic_0102606094_p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0102606094_section625475584419"></a>

None

## Response<a name="en-us_topic_0102606094_section1825415515447"></a>

[Table 2](#en-us_topic_0102606094_table725495518449)  describes the response parameters.

**Table  2**  Response parameters

<a name="en-us_topic_0102606094_table725495518449"></a>
<table><thead align="left"><tr id="en-us_topic_0102606094_row3363185511442"><th class="cellrowborder" valign="top" width="16.93%" id="mcps1.2.4.1.1"><p id="en-us_topic_0102606094_p15806308"><a name="en-us_topic_0102606094_p15806308"></a><a name="en-us_topic_0102606094_p15806308"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.57%" id="mcps1.2.4.1.2"><p id="en-us_topic_0102606094_p21995508"><a name="en-us_topic_0102606094_p21995508"></a><a name="en-us_topic_0102606094_p21995508"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="65.5%" id="mcps1.2.4.1.3"><p id="en-us_topic_0102606094_p36805753"><a name="en-us_topic_0102606094_p36805753"></a><a name="en-us_topic_0102606094_p36805753"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0102606094_row4363105574411"><td class="cellrowborder" valign="top" width="16.93%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0102606094_p73639556446"><a name="en-us_topic_0102606094_p73639556446"></a><a name="en-us_topic_0102606094_p73639556446"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="17.57%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0102606094_p103634552442"><a name="en-us_topic_0102606094_p103634552442"></a><a name="en-us_topic_0102606094_p103634552442"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="65.5%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0102606094_p53631955194415"><a name="en-us_topic_0102606094_p53631955194415"></a><a name="en-us_topic_0102606094_p53631955194415"></a>Specifies tags.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **tag**  field description

<a name="en-us_topic_0102606094_table207611141174713"></a>
<table><thead align="left"><tr id="en-us_topic_0102606094_row157616415478"><th class="cellrowborder" valign="top" width="17.04%" id="mcps1.2.4.1.1"><p id="en-us_topic_0102606094_p1990563433715"><a name="en-us_topic_0102606094_p1990563433715"></a><a name="en-us_topic_0102606094_p1990563433715"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.53%" id="mcps1.2.4.1.2"><p id="en-us_topic_0102606094_p11905734183715"><a name="en-us_topic_0102606094_p11905734183715"></a><a name="en-us_topic_0102606094_p11905734183715"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="65.42999999999999%" id="mcps1.2.4.1.3"><p id="en-us_topic_0102606094_p169051234153715"><a name="en-us_topic_0102606094_p169051234153715"></a><a name="en-us_topic_0102606094_p169051234153715"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0102606094_row1476124114474"><td class="cellrowborder" valign="top" width="17.04%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0102606094_p1048131744810"><a name="en-us_topic_0102606094_p1048131744810"></a><a name="en-us_topic_0102606094_p1048131744810"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="17.53%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0102606094_p5481171719487"><a name="en-us_topic_0102606094_p5481171719487"></a><a name="en-us_topic_0102606094_p5481171719487"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="65.42999999999999%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0102606094_p6894311152216"><a name="en-us_topic_0102606094_p6894311152216"></a><a name="en-us_topic_0102606094_p6894311152216"></a>Specifies the tag key.</p>
<a name="en-us_topic_0102606094_ul16669204222215"></a><a name="en-us_topic_0102606094_ul16669204222215"></a><ul id="en-us_topic_0102606094_ul16669204222215"><li>Contains a maximum of 36 Unicode characters.</li><li>Can only consist of digits, letters, hyphens (-), and underscores (_).</li></ul>
</td>
</tr>
<tr id="en-us_topic_0102606094_row4761184174717"><td class="cellrowborder" valign="top" width="17.04%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0102606094_p048151716488"><a name="en-us_topic_0102606094_p048151716488"></a><a name="en-us_topic_0102606094_p048151716488"></a>values</p>
</td>
<td class="cellrowborder" valign="top" width="17.53%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0102606094_p1156632102520"><a name="en-us_topic_0102606094_p1156632102520"></a><a name="en-us_topic_0102606094_p1156632102520"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="65.42999999999999%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0102606094_p1662531514220"><a name="en-us_topic_0102606094_p1662531514220"></a><a name="en-us_topic_0102606094_p1662531514220"></a>Specifies the tag value.</p>
<a name="en-us_topic_0102606094_ul18894121619234"></a><a name="en-us_topic_0102606094_ul18894121619234"></a><ul id="en-us_topic_0102606094_ul18894121619234"><li>Contains a maximum of 43 Unicode characters.</li><li>Can be left blank.</li><li>Can only consist of digits, letters, hyphens (-), and underscores (_).</li></ul>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="en-us_topic_0102606094_section73711311115217"></a>

```
GET https://{endpoint}/v1/{project_id}/cloudservers/tags
```

## Example Response<a name="section1828712235221"></a>

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

## Returned Values<a name="en-us_topic_0102606094_en-us_topic_0092803065_en-us_topic_0020212692_section22960139"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

## Error Codes<a name="en-us_topic_0102606094_en-us_topic_0092803065_en-us_topic_0067161469_en-us_topic_0057973179_section23611955"></a>

See  [Error Code Description](error-code-description.md).


# Deleting a Floating IP Address<a name="eip_openstackapi_0010"></a>

## Function<a name="en-us_topic_0201534157_section1285101621658"></a>

This API is used to delete a floating IP address.

## URI<a name="en-us_topic_0201534157_section4025916121658"></a>

DELETE /v2.0/floatingips/\{floatingip\_id\}

[Table 1](#en-us_topic_0201534157_table49321613135118)  describes the parameters.

**Table  1**  Parameter description

<a name="en-us_topic_0201534157_table49321613135118"></a>
<table><thead align="left"><tr id="en-us_topic_0201534157_row89331813135112"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="en-us_topic_0201534157_p116676362558"><a name="en-us_topic_0201534157_p116676362558"></a><a name="en-us_topic_0201534157_p116676362558"></a><strong id="en-us_topic_0201534157_b17651848105713"><a name="en-us_topic_0201534157_b17651848105713"></a><a name="en-us_topic_0201534157_b17651848105713"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="en-us_topic_0201534157_p16671836175513"><a name="en-us_topic_0201534157_p16671836175513"></a><a name="en-us_topic_0201534157_p16671836175513"></a><strong id="en-us_topic_0201534157_b3655164915717"><a name="en-us_topic_0201534157_b3655164915717"></a><a name="en-us_topic_0201534157_b3655164915717"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="en-us_topic_0201534157_p1766716366555"><a name="en-us_topic_0201534157_p1766716366555"></a><a name="en-us_topic_0201534157_p1766716366555"></a><strong id="en-us_topic_0201534157_b1980395018576"><a name="en-us_topic_0201534157_b1980395018576"></a><a name="en-us_topic_0201534157_b1980395018576"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="en-us_topic_0201534157_p116679360559"><a name="en-us_topic_0201534157_p116679360559"></a><a name="en-us_topic_0201534157_p116679360559"></a><strong id="en-us_topic_0201534157_b138701551205713"><a name="en-us_topic_0201534157_b138701551205713"></a><a name="en-us_topic_0201534157_b138701551205713"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0201534157_row4934113125120"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0201534157_p1036313125105"><a name="en-us_topic_0201534157_p1036313125105"></a><a name="en-us_topic_0201534157_p1036313125105"></a>floatingip_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0201534157_p11667113619558"><a name="en-us_topic_0201534157_p11667113619558"></a><a name="en-us_topic_0201534157_p11667113619558"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0201534157_p26672036175513"><a name="en-us_topic_0201534157_p26672036175513"></a><a name="en-us_topic_0201534157_p26672036175513"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0201534157_p566713367557"><a name="en-us_topic_0201534157_p566713367557"></a><a name="en-us_topic_0201534157_p566713367557"></a>Specifies the floating IP address ID.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="en-us_topic_0201534157_section5856898621658"></a>

None

## Response Message<a name="en-us_topic_0201534157_section1555365521658"></a>

None

## Example:<a name="en-us_topic_0201534157_section6432601621658"></a>

Example request

```
DELETE https://{Endpoint}/v2.0/floatingips/a95ec431-8473-463b-aede-34fb048ee3a7
```

Example response

None

## Status Code<a name="en-us_topic_0201534157_section10470352390"></a>

See  [Status Codes](status-codes.md#eip_api05_0001).

## Error Code<a name="en-us_topic_0201534157_section85821649202813"></a>

See  [Error Codes](error-codes.md#eip_api05_0002).


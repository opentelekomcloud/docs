# Managing Automatic Recovery of an ECS<a name="EN-US_TOPIC_0067600284"></a>

## Function<a name="en-us_topic_0057973216_section42686800"></a>

This API is used to configure or delete automatic recovery of an ECS.

## URI<a name="en-us_topic_0057972837_section48648066"></a>

PUT /v1/\{project\_id\}/cloudservers/\{server\_id\}/autorecovery

[Table 1](#table32475667)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table32475667"></a>
<table><thead align="left"><tr id="row44937496"><th class="cellrowborder" valign="top" width="16.96%" id="mcps1.2.4.1.1"><p id="p16058544"><a name="p16058544"></a><a name="p16058544"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.44%" id="mcps1.2.4.1.2"><p id="p25673664"><a name="p25673664"></a><a name="p25673664"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.60000000000001%" id="mcps1.2.4.1.3"><p id="p66300913"><a name="p66300913"></a><a name="p66300913"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1664874"><td class="cellrowborder" valign="top" width="16.96%" headers="mcps1.2.4.1.1 "><p id="p637140"><a name="p637140"></a><a name="p637140"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p51608407"><a name="p51608407"></a><a name="p51608407"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.60000000000001%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row41565035"><td class="cellrowborder" valign="top" width="16.96%" headers="mcps1.2.4.1.1 "><p id="p11324657"><a name="p11324657"></a><a name="p11324657"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p44882061"><a name="p44882061"></a><a name="p44882061"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.60000000000001%" headers="mcps1.2.4.1.3 "><p id="p11568292"><a name="p11568292"></a><a name="p11568292"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0057972837_section35179415"></a>

[Table 2](#table10194370103926)  describes the request parameters.

**Table  2**  Request parameters

<a name="table10194370103926"></a>
<table><thead align="left"><tr id="row2464269103926"><th class="cellrowborder" valign="top" width="16.90830916908309%" id="mcps1.2.5.1.1"><p id="p65388140103926"><a name="p65388140103926"></a><a name="p65388140103926"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.428257174282567%" id="mcps1.2.5.1.2"><p id="p2158837123413"><a name="p2158837123413"></a><a name="p2158837123413"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="13.698630136986301%" id="mcps1.2.5.1.3"><p id="p61948020103926"><a name="p61948020103926"></a><a name="p61948020103926"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.96480351964803%" id="mcps1.2.5.1.4"><p id="p29680796103926"><a name="p29680796103926"></a><a name="p29680796103926"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row55334285103926"><td class="cellrowborder" valign="top" width="16.90830916908309%" headers="mcps1.2.5.1.1 "><p id="p52892102103926"><a name="p52892102103926"></a><a name="p52892102103926"></a>support_auto_recovery</p>
</td>
<td class="cellrowborder" valign="top" width="17.428257174282567%" headers="mcps1.2.5.1.2 "><p id="p15158337163413"><a name="p15158337163413"></a><a name="p15158337163413"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="13.698630136986301%" headers="mcps1.2.5.1.3 "><p id="p56401904103926"><a name="p56401904103926"></a><a name="p56401904103926"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.96480351964803%" headers="mcps1.2.5.1.4 "><p id="p4477201211456"><a name="p4477201211456"></a><a name="p4477201211456"></a>Configures or deletes automatic recovery of an ECS.</p>
<a name="ul1796286911458"></a><a name="ul1796286911458"></a><ul id="ul1796286911458"><li><strong id="b842352706133929"><a name="b842352706133929"></a><a name="b842352706133929"></a>true</strong>: indicates configuring automatic recovery for an ECS.</li><li><strong id="b842352706134346"><a name="b842352706134346"></a><a name="b842352706134346"></a>false</strong>: indicates deleting automatic recovery of an ECS.</li></ul>
</td>
</tr>
</tbody>
</table>

## Response<a name="section46887454104452"></a>

None

## Example Request<a name="section23010434414"></a>

```
PUT https://{endpoint}/v1/{project_id}/cloudservers/{server_id}/autorecovery
```

```
{
    "support_auto_recovery": "true"
}
```

## Example Response<a name="section1579918291477"></a>

None

## Returned Values<a name="section38423777104228"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

## Error Codes<a name="section85821649202813"></a>

See  [Error Code Description](error-code-description.md).


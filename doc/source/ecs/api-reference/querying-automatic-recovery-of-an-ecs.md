# Querying Automatic Recovery of an ECS<a name="EN-US_TOPIC_0067600148"></a>

## Function<a name="en-us_topic_0057973216_section42686800"></a>

This API is used to query automatic recovery configured for an ECS.

## URI<a name="en-us_topic_0057972837_section48648066"></a>

GET /v1/\{project\_id\}/cloudservers/\{server\_id\}/autorecovery

[Table 1](#table32475667)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table32475667"></a>
<table><thead align="left"><tr id="row44937496"><th class="cellrowborder" valign="top" width="16.6%" id="mcps1.2.4.1.1"><p id="p16058544"><a name="p16058544"></a><a name="p16058544"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.349999999999998%" id="mcps1.2.4.1.2"><p id="p25673664"><a name="p25673664"></a><a name="p25673664"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="66.05%" id="mcps1.2.4.1.3"><p id="p66300913"><a name="p66300913"></a><a name="p66300913"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1664874"><td class="cellrowborder" valign="top" width="16.6%" headers="mcps1.2.4.1.1 "><p id="p637140"><a name="p637140"></a><a name="p637140"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p51608407"><a name="p51608407"></a><a name="p51608407"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.05%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row41565035"><td class="cellrowborder" valign="top" width="16.6%" headers="mcps1.2.4.1.1 "><p id="p11324657"><a name="p11324657"></a><a name="p11324657"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p44882061"><a name="p44882061"></a><a name="p44882061"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.05%" headers="mcps1.2.4.1.3 "><p id="p11568292"><a name="p11568292"></a><a name="p11568292"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0057972837_section35179415"></a>

None

## Response<a name="en-us_topic_0057973216_section22805648"></a>

[Table 2](#en-us_topic_0057973216_table30138413)  describes the response parameters.

**Table  2**  Response parameters

<a name="en-us_topic_0057973216_table30138413"></a>
<table><thead align="left"><tr id="en-us_topic_0057973216_row48088059"><th class="cellrowborder" valign="top" width="18.029999999999998%" id="mcps1.2.4.1.1"><p id="en-us_topic_0057973216_p2818710"><a name="en-us_topic_0057973216_p2818710"></a><a name="en-us_topic_0057973216_p2818710"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15.939999999999998%" id="mcps1.2.4.1.2"><p id="en-us_topic_0057973216_p26988933"><a name="en-us_topic_0057973216_p26988933"></a><a name="en-us_topic_0057973216_p26988933"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="66.03%" id="mcps1.2.4.1.3"><p id="en-us_topic_0057973216_p41208449"><a name="en-us_topic_0057973216_p41208449"></a><a name="en-us_topic_0057973216_p41208449"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973216_row35331722"><td class="cellrowborder" valign="top" width="18.029999999999998%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973216_p43297228"><a name="en-us_topic_0057973216_p43297228"></a><a name="en-us_topic_0057973216_p43297228"></a>support_auto_recovery</p>
</td>
<td class="cellrowborder" valign="top" width="15.939999999999998%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973216_p17414566"><a name="en-us_topic_0057973216_p17414566"></a><a name="en-us_topic_0057973216_p17414566"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="66.03%" headers="mcps1.2.4.1.3 "><p id="p1949458111338"><a name="p1949458111338"></a><a name="p1949458111338"></a>Queries automatic recovery configured for an ECS.</p>
<a name="ul3145269711341"></a><a name="ul3145269711341"></a><ul id="ul3145269711341"><li><strong id="b842352706133929"><a name="b842352706133929"></a><a name="b842352706133929"></a>true</strong>: indicates that automatic recovery is configured for an ECS.</li><li><strong id="b842352706133948"><a name="b842352706133948"></a><a name="b842352706133948"></a>false</strong>: indicates that automatic recovery is not configured for an ECS.</li></ul>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="section1586317916474"></a>

None

## Example Response<a name="en-us_topic_0057972837_section48179284"></a>

```
GET https://{endpoint}/v1/{project_id}/cloudservers/{server_id}/autorecovery
```

```
{ 
   "support_auto_recovery": "true"
}
```

## Returned Values<a name="section38423777104228"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

## Error Codes<a name="section85821649202813"></a>

See  [Error Code Description](error-code-description.md).


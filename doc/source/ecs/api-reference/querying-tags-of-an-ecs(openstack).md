# Querying Tags of an ECS<a name="EN-US_TOPIC_0065820822"></a>

This API is used to query all tags of an ECS.

You are required to use the HTTP header  **X-OpenStack-Nova-API-Version: 2.26**  to specify the microversion on the client.

## URI<a name="en-us_topic_0057972837_section48648066"></a>

GET /v2.1/\{project\_id\}/servers/\{server\_id\}/tags

[Table 1](#en-us_topic_0057972837_table32475667)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="en-us_topic_0057972837_table32475667"></a>
<table><thead align="left"><tr id="en-us_topic_0057972837_row44937496"><th class="cellrowborder" valign="top" width="16.98%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.73%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.29%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972837_row1664874"><td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972837_p637140"><a name="en-us_topic_0057972837_p637140"></a><a name="en-us_topic_0057972837_p637140"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.73%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972837_p51608407"><a name="en-us_topic_0057972837_p51608407"></a><a name="en-us_topic_0057972837_p51608407"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.29%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0057972837_row41565035"><td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972837_p11324657"><a name="en-us_topic_0057972837_p11324657"></a><a name="en-us_topic_0057972837_p11324657"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.73%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972837_p44882061"><a name="en-us_topic_0057972837_p44882061"></a><a name="en-us_topic_0057972837_p44882061"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.29%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972837_p11568292"><a name="en-us_topic_0057972837_p11568292"></a><a name="en-us_topic_0057972837_p11568292"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0057972837_section35179415"></a>

None

## Response<a name="en-us_topic_0057972837_section1485113257556"></a>

[Table 2](#en-us_topic_0057972838_table28387752)  describes the response parameters.

**Table  2**  Response parameters

<a name="en-us_topic_0057972838_table28387752"></a>
<table><thead align="left"><tr id="en-us_topic_0057972838_row66802302"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.4.1.1"><p id="en-us_topic_0057972838_p42277343"><a name="en-us_topic_0057972838_p42277343"></a><a name="en-us_topic_0057972838_p42277343"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.810000000000002%" id="mcps1.2.4.1.2"><p id="en-us_topic_0057972838_p1912753"><a name="en-us_topic_0057972838_p1912753"></a><a name="en-us_topic_0057972838_p1912753"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="65.19%" id="mcps1.2.4.1.3"><p id="en-us_topic_0057972838_p217030"><a name="en-us_topic_0057972838_p217030"></a><a name="en-us_topic_0057972838_p217030"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972838_row17579482"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972838_p14651901"><a name="en-us_topic_0057972838_p14651901"></a><a name="en-us_topic_0057972838_p14651901"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="17.810000000000002%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972838_p45953370"><a name="en-us_topic_0057972838_p45953370"></a><a name="en-us_topic_0057972838_p45953370"></a>Array of strings</p>
</td>
<td class="cellrowborder" valign="top" width="65.19%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972838_p47045852"><a name="en-us_topic_0057972838_p47045852"></a><a name="en-us_topic_0057972838_p47045852"></a>Specifies ECS tags.</p>
<p id="p7300949059"><a name="p7300949059"></a><a name="p7300949059"></a>Tag functions have been upgraded on the public cloud. After the upgrade, the tag values returned by the system comply with the following rules:</p>
<a name="ul871515496611"></a><a name="ul871515496611"></a><ul id="ul871515496611"><li>The key and value of a tag are connected using an equal sign (=), for example, key=value.</li><li>If the value is empty, only the key is returned.</li></ul>
<p id="p141334271371"><a name="p141334271371"></a><a name="p141334271371"></a>For more details about upgraded tag functions, see <a href="tag-types(openstack).md">Tag Types</a>.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="section14532216125819"></a>

```
GET https://{endpoint}/v2.1/{project_id}/servers/{server_id}/tags
```

## Example Response<a name="section1956815525910"></a>

Example response

```
{ 
    "tags": ["baz=xyy", "foo", "qux"]
}
```

## Returned Values<a name="en-us_topic_0057972837_en-us_topic_0020212692_section22960139"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).


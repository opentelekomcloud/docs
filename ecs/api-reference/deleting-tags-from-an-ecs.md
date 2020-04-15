# Deleting Tags from an ECS<a name="EN-US_TOPIC_0065820824"></a>

This API is used to delete all tags of an ECS.

You are required to use the HTTP header  **X-OpenStack-Nova-API-Version: 2.26**  to specify the microversion on the client.

## URI<a name="en-us_topic_0057972839_section28406254"></a>

DELETE /v2.1/\{project\_id\}/servers/\{server\_id\}/tags

[Table 1](#en-us_topic_0057972839_table32475667)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="en-us_topic_0057972839_table32475667"></a>
<table><thead align="left"><tr id="en-us_topic_0057972839_row44937496"><th class="cellrowborder" valign="top" width="16.98%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="18.3%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="64.72%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972839_row1664874"><td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972839_p637140"><a name="en-us_topic_0057972839_p637140"></a><a name="en-us_topic_0057972839_p637140"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="18.3%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972839_p51608407"><a name="en-us_topic_0057972839_p51608407"></a><a name="en-us_topic_0057972839_p51608407"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="64.72%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0057972839_row41565035"><td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972839_p11324657"><a name="en-us_topic_0057972839_p11324657"></a><a name="en-us_topic_0057972839_p11324657"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="18.3%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972839_p44882061"><a name="en-us_topic_0057972839_p44882061"></a><a name="en-us_topic_0057972839_p44882061"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="64.72%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972839_p11568292"><a name="en-us_topic_0057972839_p11568292"></a><a name="en-us_topic_0057972839_p11568292"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0057972839_section54329699"></a>

None

## Response<a name="en-us_topic_0057972839_section19205251"></a>

None

## Example Request<a name="section4139939155912"></a>

```
DELETE https://{endpoint}/v2.1/{project_id}/servers/{server_id}/tags
```

## Example Response<a name="section11729204775916"></a>

None

## Returned Values<a name="en-us_topic_0057972839_en-us_topic_0020212692_section22960139"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).


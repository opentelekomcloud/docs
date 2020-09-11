# Querying a Specified Tag for an ECS<a name="EN-US_TOPIC_0065820826"></a>

This API is used to query whether an ECS has a specified tag.

You are required to use the HTTP header  **X-OpenStack-Nova-API-Version: 2.26**  to specify the microversion on the client.

## URI<a name="en-us_topic_0057972841_section26207892"></a>

GET /v2.1/\{project\_id\}/servers/\{server\_id\}/tags/\{tag\}

[Table 1](#en-us_topic_0057972841_table32475667)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="en-us_topic_0057972841_table32475667"></a>
<table><thead align="left"><tr id="en-us_topic_0057972841_row44937496"><th class="cellrowborder" valign="top" width="17.11%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.88%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.01%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972841_row1664874"><td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972841_p637140"><a name="en-us_topic_0057972841_p637140"></a><a name="en-us_topic_0057972841_p637140"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.88%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972841_p51608407"><a name="en-us_topic_0057972841_p51608407"></a><a name="en-us_topic_0057972841_p51608407"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.01%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0057972841_row41565035"><td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972841_p11324657"><a name="en-us_topic_0057972841_p11324657"></a><a name="en-us_topic_0057972841_p11324657"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.88%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972841_p44882061"><a name="en-us_topic_0057972841_p44882061"></a><a name="en-us_topic_0057972841_p44882061"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.01%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972841_p11568292"><a name="en-us_topic_0057972841_p11568292"></a><a name="en-us_topic_0057972841_p11568292"></a>Specifies the ECS ID.</p>
</td>
</tr>
<tr id="en-us_topic_0057972841_row7149154519295"><td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972841_p21503455299"><a name="en-us_topic_0057972841_p21503455299"></a><a name="en-us_topic_0057972841_p21503455299"></a>tag</p>
</td>
<td class="cellrowborder" valign="top" width="17.88%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972841_p415074512298"><a name="en-us_topic_0057972841_p415074512298"></a><a name="en-us_topic_0057972841_p415074512298"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.01%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972841_p1415044592918"><a name="en-us_topic_0057972841_p1415044592918"></a><a name="en-us_topic_0057972841_p1415044592918"></a>Specifies the key of the tag to be queried. If no key is specified, all tags of the ECS are displayed.</p>
<p id="p141334271371"><a name="p141334271371"></a><a name="p141334271371"></a>For details about key rules, see <a href="tag-types(openstack).md">Tag Types</a>.</p>
<div class="note" id="note124521913175616"><a name="note124521913175616"></a><a name="note124521913175616"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1745221311560"><a name="p1745221311560"></a><a name="p1745221311560"></a>Tag functions have been upgraded on the public cloud. If the tags added before the function upgrade are in the format of "Key.Value", query tags using "Key".</p>
<p id="p213418685710"><a name="p213418685710"></a><a name="p213418685710"></a>For example, an existing tag is "a.b". The tag can be queried in the format of "tag=a.b" before and in the format of "tag=a" now according to the new tag rules.</p>
</div></div>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0057972841_section34544438"></a>

None

## Response<a name="en-us_topic_0057972841_section42464494"></a>

None

## Example Request<a name="section274565913012"></a>

```
GET https://{endpoint}/v2.1/{project_id}/servers/{server_id}/tags/{tag}
```

## Example Response<a name="section163001561818"></a>

None

## Returned Values<a name="en-us_topic_0057972841_en-us_topic_0020212692_section22960139"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).


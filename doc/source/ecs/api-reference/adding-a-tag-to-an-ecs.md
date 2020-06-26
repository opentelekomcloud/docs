# Adding a Tag to an ECS<a name="EN-US_TOPIC_0065820825"></a>

This API is used to add a tag to an ECS.

You are required to use the HTTP header  **X-OpenStack-Nova-API-Version: 2.26**  to specify the microversion on the client.

## Constraints<a name="en-us_topic_0057972840_section31378522222725"></a>

-   The tag contains a maximum of 80 characters.
-   A tag can only consist of digits, letters, hyphens \(-\), and underscores \(\_\).
-   A maximum of 50 tags can be added.
-   An empty tag cannot be created.

## URI<a name="en-us_topic_0057972840_section37794916"></a>

PUT /v2.1/\{project\_id\}/servers/\{server\_id\}/tags/\{tag\}

[Table 1](#en-us_topic_0057972840_table32475667)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="en-us_topic_0057972840_table32475667"></a>
<table><thead align="left"><tr id="en-us_topic_0057972840_row44937496"><th class="cellrowborder" valign="top" width="16.79%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.169999999999998%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="66.03999999999999%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972840_row1664874"><td class="cellrowborder" valign="top" width="16.79%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972840_p637140"><a name="en-us_topic_0057972840_p637140"></a><a name="en-us_topic_0057972840_p637140"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972840_p51608407"><a name="en-us_topic_0057972840_p51608407"></a><a name="en-us_topic_0057972840_p51608407"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.03999999999999%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0057972840_row41565035"><td class="cellrowborder" valign="top" width="16.79%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972840_p11324657"><a name="en-us_topic_0057972840_p11324657"></a><a name="en-us_topic_0057972840_p11324657"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972840_p44882061"><a name="en-us_topic_0057972840_p44882061"></a><a name="en-us_topic_0057972840_p44882061"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.03999999999999%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972840_p11568292"><a name="en-us_topic_0057972840_p11568292"></a><a name="en-us_topic_0057972840_p11568292"></a>Specifies the ECS ID.</p>
</td>
</tr>
<tr id="row074891417316"><td class="cellrowborder" valign="top" width="16.79%" headers="mcps1.2.4.1.1 "><p id="p874919141739"><a name="p874919141739"></a><a name="p874919141739"></a>tag</p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p137495141317"><a name="p137495141317"></a><a name="p137495141317"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.03999999999999%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972841_p1415044592918"><a name="en-us_topic_0057972841_p1415044592918"></a><a name="en-us_topic_0057972841_p1415044592918"></a>Specifies the key of the tag to be added.</p>
<p id="p141334271371"><a name="p141334271371"></a><a name="p141334271371"></a>For details about key rules, see <a href="tag-types(openstack).md">Tag Types</a>.</p>
<div class="note" id="note124521913175616"><a name="note124521913175616"></a><a name="note124521913175616"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1745221311560"><a name="p1745221311560"></a><a name="p1745221311560"></a>Tag functions have been upgraded on the public cloud. If the tags added before the function upgrade are in the format of "Key.Value", query tags using "Key".</p>
<p id="p213418685710"><a name="p213418685710"></a><a name="p213418685710"></a>For example, an existing tag is "a.b". The tag can be queried in the format of "tag=a.b" before and in the format of "tag=a" now according to the new tag rules.</p>
</div></div>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0057972840_section9861165814212"></a>

None

## Response<a name="section488222312016"></a>

None

## Example Request<a name="section204251290013"></a>

```
PUT https://{endpoint}/v2.1/{project_id}/servers/{server_id}/tags/{tag}
```

## Example Response<a name="section38861442507"></a>

None

## Returned Values<a name="en-us_topic_0057972840_en-us_topic_0020212692_section22960139"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).


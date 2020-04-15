# Deleting a Specified Tag from an ECS<a name="EN-US_TOPIC_0065820827"></a>

This API is used to delete a specified tag from an ECS.

You are required to use the HTTP header  **X-OpenStack-Nova-API-Version: 2.26**  to specify the microversion on the client.

## Constraints<a name="en-us_topic_0057972842_section47071996222837"></a>

-   The tag contains a maximum of 80 characters.
-   If a tag contains non-URL-safe characters, perform URL encoding.

## URI<a name="en-us_topic_0057972842_section49330940"></a>

DELETE /v2.1/\{project\_id\}/servers/\{server\_id\}/tags/\{tag\}

[Table 1](#en-us_topic_0057972842_table536172734712)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="en-us_topic_0057972842_table536172734712"></a>
<table><thead align="left"><tr id="en-us_topic_0057972842_row103712714716"><th class="cellrowborder" valign="top" width="16.98%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.919999999999998%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.10000000000001%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972842_row0411327194717"><td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972842_p942327144718"><a name="en-us_topic_0057972842_p942327144718"></a><a name="en-us_topic_0057972842_p942327144718"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.919999999999998%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972842_p164222714475"><a name="en-us_topic_0057972842_p164222714475"></a><a name="en-us_topic_0057972842_p164222714475"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.10000000000001%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0057972842_row17438272471"><td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972842_p14448270471"><a name="en-us_topic_0057972842_p14448270471"></a><a name="en-us_topic_0057972842_p14448270471"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.919999999999998%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972842_p11458272478"><a name="en-us_topic_0057972842_p11458272478"></a><a name="en-us_topic_0057972842_p11458272478"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.10000000000001%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972842_p845102714478"><a name="en-us_topic_0057972842_p845102714478"></a><a name="en-us_topic_0057972842_p845102714478"></a>Specifies the ECS ID.</p>
</td>
</tr>
<tr id="en-us_topic_0057972842_row255344913344"><td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972842_p8553134913345"><a name="en-us_topic_0057972842_p8553134913345"></a><a name="en-us_topic_0057972842_p8553134913345"></a>tag</p>
</td>
<td class="cellrowborder" valign="top" width="17.919999999999998%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972842_p05531249143414"><a name="en-us_topic_0057972842_p05531249143414"></a><a name="en-us_topic_0057972842_p05531249143414"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.10000000000001%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972842_p04316297356"><a name="en-us_topic_0057972842_p04316297356"></a><a name="en-us_topic_0057972842_p04316297356"></a>Specifies the key of the tag to be deleted. If no key is specified, all tags of the ECS are deleted.</p>
<p id="p141334271371"><a name="p141334271371"></a><a name="p141334271371"></a>For details about key rules, see <a href="tag-types(openstack).md">Tag Types</a>.</p>
<div class="note" id="note124521913175616"><a name="note124521913175616"></a><a name="note124521913175616"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1745221311560"><a name="p1745221311560"></a><a name="p1745221311560"></a>Tag functions have been upgraded on the public cloud. If the tags added before the function upgrade are in the format of "Key.Value", delete tags using "Key".</p>
<p id="p213418685710"><a name="p213418685710"></a><a name="p213418685710"></a>For example, an existing tag is <strong id="b84235270610509"><a name="b84235270610509"></a><a name="b84235270610509"></a>a.b</strong>. After the tag function upgrade, delete the tag using "a".</p>
</div></div>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0057972842_section41325284"></a>

None

## Response<a name="en-us_topic_0057972842_section36383236"></a>

None

## Example Request<a name="section28931627710"></a>

```
DELETE https://{endpoint}/v2.1/{project_id}/servers/{server_id}/tags/{tag}
```

## Example Response<a name="section179263403114"></a>

None

## Returned Values<a name="en-us_topic_0057972842_en-us_topic_0020212692_section22960139"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).


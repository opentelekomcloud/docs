# Deleting an ECS Group<a name="EN-US_TOPIC_0065817723"></a>

## Function<a name="en-us_topic_0057973160_section59750848"></a>

This API is used to delete an ECS group.

## URI<a name="en-us_topic_0057973160_section886720"></a>

DELETE /v2/\{project\_id\}/os-server-groups/\{server\_group\_id\}

DELETE /v2.1/\{project\_id\}/os-server-groups/\{server\_group\_id\}

[Table 1](#en-us_topic_0057973160_en-us_topic_0020212650_table62669527)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="en-us_topic_0057973160_en-us_topic_0020212650_table62669527"></a>
<table><thead align="left"><tr id="en-us_topic_0057973160_en-us_topic_0020212650_row33894570"><th class="cellrowborder" valign="top" width="17.358264173582644%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.548245175482453%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.09349065093491%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057973160_en-us_topic_0020212650_row8419032"><td class="cellrowborder" valign="top" width="17.358264173582644%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973160_en-us_topic_0020212650_p10852974"><a name="en-us_topic_0057973160_en-us_topic_0020212650_p10852974"></a><a name="en-us_topic_0057973160_en-us_topic_0020212650_p10852974"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.548245175482453%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973160_en-us_topic_0020212650_p6675738"><a name="en-us_topic_0057973160_en-us_topic_0020212650_p6675738"></a><a name="en-us_topic_0057973160_en-us_topic_0020212650_p6675738"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.09349065093491%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0057973160_row1856062192319"><td class="cellrowborder" valign="top" width="17.358264173582644%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057973160_p16560926238"><a name="en-us_topic_0057973160_p16560926238"></a><a name="en-us_topic_0057973160_p16560926238"></a>server_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.548245175482453%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057973160_p5560326232"><a name="en-us_topic_0057973160_p5560326232"></a><a name="en-us_topic_0057973160_p5560326232"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.09349065093491%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057973160_p94577242237"><a name="en-us_topic_0057973160_p94577242237"></a><a name="en-us_topic_0057973160_p94577242237"></a>Specifies the ECS group UUID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section8486123205213"></a>

None

## Response<a name="section164423895218"></a>

None

## Example Request<a name="en-us_topic_0057973160_section15049613"></a>

```
DELETE https://{endpoint}/v2/9c53a566cb3443ab910cf0daebca90c4/os-server-groups/5bbcc3c4-1da2-4437-a48a-66f15b1b13f9
DELETE https://{endpoint}/v2.1/9c53a566cb3443ab910cf0daebca90c4/os-server-groups/5bbcc3c4-1da2-4437-a48a-66f15b1b13f9
```

## Returned Values<a name="en-us_topic_0057973160_section11059103"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).


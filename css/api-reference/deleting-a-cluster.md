# Deleting a Cluster<a name="css_03_0020"></a>

## Function<a name="section13509138115714"></a>

This API is used to delete a cluster. All resources, including customer data, of the deleted cluster will be released. For data security reasons, create a snapshot for the cluster that you want to delete.

## URI<a name="section156291613195618"></a>

```
DELETE /v1.0/{project_id}/clusters/{cluster_id}
```

**Table  1**  Parameter description

<a name="table26299133563"></a>
<table><thead align="left"><tr id="row1511414148567"><th class="cellrowborder" valign="top" width="20.419999999999998%" id="mcps1.2.5.1.1"><p id="p201141114115617"><a name="p201141114115617"></a><a name="p201141114115617"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15.1%" id="mcps1.2.5.1.2"><p id="p611491415563"><a name="p611491415563"></a><a name="p611491415563"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="15.67%" id="mcps1.2.5.1.3"><p id="p13114714165613"><a name="p13114714165613"></a><a name="p13114714165613"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="48.809999999999995%" id="mcps1.2.5.1.4"><p id="p81148146567"><a name="p81148146567"></a><a name="p81148146567"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row7114141416564"><td class="cellrowborder" valign="top" width="20.419999999999998%" headers="mcps1.2.5.1.1 "><p id="p6114111455616"><a name="p6114111455616"></a><a name="p6114111455616"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="15.1%" headers="mcps1.2.5.1.2 "><p id="p91143149562"><a name="p91143149562"></a><a name="p91143149562"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.67%" headers="mcps1.2.5.1.3 "><p id="p111451435614"><a name="p111451435614"></a><a name="p111451435614"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.809999999999995%" headers="mcps1.2.5.1.4 "><p id="p16114201416568"><a name="p16114201416568"></a><a name="p16114201416568"></a>Project ID.</p>
</td>
</tr>
<tr id="row1911421445610"><td class="cellrowborder" valign="top" width="20.419999999999998%" headers="mcps1.2.5.1.1 "><p id="p12114214115615"><a name="p12114214115615"></a><a name="p12114214115615"></a>cluster_id</p>
</td>
<td class="cellrowborder" valign="top" width="15.1%" headers="mcps1.2.5.1.2 "><p id="p31141614165612"><a name="p31141614165612"></a><a name="p31141614165612"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="15.67%" headers="mcps1.2.5.1.3 "><p id="p111142014165613"><a name="p111142014165613"></a><a name="p111142014165613"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="48.809999999999995%" headers="mcps1.2.5.1.4 "><p id="p7114191425620"><a name="p7114191425620"></a><a name="p7114191425620"></a>ID of the cluster to be deleted.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section264581355617"></a>

None

## Response<a name="section5645161395611"></a>

None

## Examples<a name="section11872121315298"></a>

Delete the cluster whose ID is  **2a197c4d-5467-4003-931d-83ec49939cf**.

Example request

```
DELETE /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/2a197c4d-5467-4003-931d-83ec49939cf
```

Example response

The returned value is empty.

## Status Code<a name="section87962546391"></a>

[Table 2](#table12321369178)  describes the status code.

**Table  2**  Status code

<a name="table12321369178"></a>
<table><thead align="left"><tr id="css_03_0018_row1972183521418"><th class="cellrowborder" valign="top" width="15.939999999999998%" id="mcps1.2.4.1.1"><p id="css_03_0018_p14560134151414"><a name="css_03_0018_p14560134151414"></a><a name="css_03_0018_p14560134151414"></a>Status Code</p>
</th>
<th class="cellrowborder" valign="top" width="31.04%" id="mcps1.2.4.1.2"><p id="css_03_0018_p5563194141411"><a name="css_03_0018_p5563194141411"></a><a name="css_03_0018_p5563194141411"></a>Code</p>
</th>
<th class="cellrowborder" valign="top" width="53.02%" id="mcps1.2.4.1.3"><p id="css_03_0018_p256616411143"><a name="css_03_0018_p256616411143"></a><a name="css_03_0018_p256616411143"></a>Status Code Description</p>
</th>
</tr>
</thead>
<tbody><tr id="css_03_0018_row129720356144"><td class="cellrowborder" valign="top" width="15.939999999999998%" headers="mcps1.2.4.1.1 "><p id="css_03_0018_p1957004131410"><a name="css_03_0018_p1957004131410"></a><a name="css_03_0018_p1957004131410"></a>400</p>
</td>
<td class="cellrowborder" valign="top" width="31.04%" headers="mcps1.2.4.1.2 "><p id="css_03_0018_p165731141171419"><a name="css_03_0018_p165731141171419"></a><a name="css_03_0018_p165731141171419"></a>BadRequest</p>
</td>
<td class="cellrowborder" valign="top" width="53.02%" headers="mcps1.2.4.1.3 "><p id="css_03_0018_p65778413148"><a name="css_03_0018_p65778413148"></a><a name="css_03_0018_p65778413148"></a>Invalid request.</p>
<p id="css_03_0018_p1557974171415"><a name="css_03_0018_p1557974171415"></a><a name="css_03_0018_p1557974171415"></a>The client should not repeat the request without modifications.</p>
</td>
</tr>
<tr id="css_03_0018_row8972103517147"><td class="cellrowborder" valign="top" width="15.939999999999998%" headers="mcps1.2.4.1.1 "><p id="css_03_0018_p75841441191410"><a name="css_03_0018_p75841441191410"></a><a name="css_03_0018_p75841441191410"></a>404</p>
</td>
<td class="cellrowborder" valign="top" width="31.04%" headers="mcps1.2.4.1.2 "><p id="css_03_0018_p258716416142"><a name="css_03_0018_p258716416142"></a><a name="css_03_0018_p258716416142"></a>NotFound</p>
</td>
<td class="cellrowborder" valign="top" width="53.02%" headers="mcps1.2.4.1.3 "><p id="css_03_0018_p15589154118141"><a name="css_03_0018_p15589154118141"></a><a name="css_03_0018_p15589154118141"></a>The requested resource cannot be found.</p>
<p id="css_03_0018_p14590164151410"><a name="css_03_0018_p14590164151410"></a><a name="css_03_0018_p14590164151410"></a>The client should not repeat the request without modifications.</p>
</td>
</tr>
<tr id="css_03_0018_row297223511416"><td class="cellrowborder" valign="top" width="15.939999999999998%" headers="mcps1.2.4.1.1 "><p id="css_03_0018_p13595164131416"><a name="css_03_0018_p13595164131416"></a><a name="css_03_0018_p13595164131416"></a>200</p>
</td>
<td class="cellrowborder" valign="top" width="31.04%" headers="mcps1.2.4.1.2 "><p id="css_03_0018_p9598741131416"><a name="css_03_0018_p9598741131416"></a><a name="css_03_0018_p9598741131416"></a>OK</p>
</td>
<td class="cellrowborder" valign="top" width="53.02%" headers="mcps1.2.4.1.3 "><p id="css_03_0018_p659994115146"><a name="css_03_0018_p659994115146"></a><a name="css_03_0018_p659994115146"></a>The request is processed successfully.</p>
</td>
</tr>
</tbody>
</table>


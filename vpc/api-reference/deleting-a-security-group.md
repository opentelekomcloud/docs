# Deleting a Security Group<a name="vpc_sg01_0004"></a>

## Function<a name="section4195542395259"></a>

This API is used to delete a security group.

## URI<a name="section5844660495259"></a>

DELETE /v1/\{project\_id\}/security-groups/\{security\_group\_id\}

[Table 1](#table1939240195259)  describes the parameters.

**Table  1**  Parameter description

<a name="table1939240195259"></a>
<table><thead align="left"><tr id="row1961474195259"><th class="cellrowborder" valign="top" width="28.232823282328233%" id="mcps1.2.4.1.1"><p id="p1035476495259"><a name="p1035476495259"></a><a name="p1035476495259"></a><strong id="b842352706195711"><a name="b842352706195711"></a><a name="b842352706195711"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="30.273027302730277%" id="mcps1.2.4.1.2"><p id="p1553041195259"><a name="p1553041195259"></a><a name="p1553041195259"></a><strong id="b842352706145619"><a name="b842352706145619"></a><a name="b842352706145619"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="41.494149414941496%" id="mcps1.2.4.1.3"><p id="p2600047695259"><a name="p2600047695259"></a><a name="p2600047695259"></a><strong id="b372029376201138"><a name="b372029376201138"></a><a name="b372029376201138"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1253681595259"><td class="cellrowborder" valign="top" width="28.232823282328233%" headers="mcps1.2.4.1.1 "><p id="p2796266695259"><a name="p2796266695259"></a><a name="p2796266695259"></a>security_group_id</p>
</td>
<td class="cellrowborder" valign="top" width="30.273027302730277%" headers="mcps1.2.4.1.2 "><p id="p3612906795259"><a name="p3612906795259"></a><a name="p3612906795259"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="41.494149414941496%" headers="mcps1.2.4.1.3 "><p id="p1165773195259"><a name="p1165773195259"></a><a name="p1165773195259"></a>Specifies the security group ID, which uniquely identifies the security group.</p>
</td>
</tr>
<tr id="row4225519995259"><td class="cellrowborder" valign="top" width="28.232823282328233%" headers="mcps1.2.4.1.1 "><p id="p137426195259"><a name="p137426195259"></a><a name="p137426195259"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="30.273027302730277%" headers="mcps1.2.4.1.2 "><p id="p3252720195259"><a name="p3252720195259"></a><a name="p3252720195259"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="41.494149414941496%" headers="mcps1.2.4.1.3 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section3936161695259"></a>

-   Request parameter

    None

-   Example request

    ```
    DELETE https://{Endpoint}/v1/{project_id}/security-groups/0c4a2336-b036-4fa2-bc3c-1a291ed4c431
    ```


## Response Message<a name="section3532656695259"></a>

-   Response parameter

    None

-   Example response

    None


## Status Code<a name="section31981619"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).


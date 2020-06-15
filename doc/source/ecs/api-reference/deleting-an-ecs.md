# Deleting an ECS<a name="EN-US_TOPIC_0025560296"></a>

## Function<a name="section4329148591032"></a>

This API is used to delete an ECS.

## Constraints<a name="section14125473229"></a>

When an ECS is deleted, all NICs attached to the ECS through the OpenStack Nova API will be deleted.

## URI<a name="section1832690791032"></a>

DELETE /v2/\{project\_id\}/servers/\{server\_id\}

DELETE /v2.1/\{project\_id\}/servers/\{server\_id\}

[Table 1](#table2659898791032)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table2659898791032"></a>
<table><thead align="left"><tr id="row4869561291032"><th class="cellrowborder" valign="top" width="16.41%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.549999999999997%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="66.03999999999999%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row6666852391032"><td class="cellrowborder" valign="top" width="16.41%" headers="mcps1.2.4.1.1 "><p id="p3144131991032"><a name="p3144131991032"></a><a name="p3144131991032"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.549999999999997%" headers="mcps1.2.4.1.2 "><p id="p6371887891032"><a name="p6371887891032"></a><a name="p6371887891032"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.03999999999999%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row5885541191134"><td class="cellrowborder" valign="top" width="16.41%" headers="mcps1.2.4.1.1 "><p id="p255895491134"><a name="p255895491134"></a><a name="p255895491134"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.549999999999997%" headers="mcps1.2.4.1.2 "><p id="p594874291134"><a name="p594874291134"></a><a name="p594874291134"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66.03999999999999%" headers="mcps1.2.4.1.3 "><p id="p1208612791134"><a name="p1208612791134"></a><a name="p1208612791134"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section1172872291032"></a>

None

## Response<a name="section6619360391225"></a>

None

## Example Request<a name="section1399410202536"></a>

```
DELETE https://{endpoint}/v2/{project_id}/servers/{server_id}
DELETE https://{endpoint}/v2.1/{project_id}/servers/{server_id}
```

## Example Response<a name="section975263145318"></a>

None

## Returned Values<a name="section3477250491225"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).


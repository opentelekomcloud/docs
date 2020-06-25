# Deleting Specified ECS Metadata<a name="EN-US_TOPIC_0025560299"></a>

## Function<a name="section5520708185439"></a>

This API is used to delete specified ECS metadata.

## Constraints<a name="section4794112412015"></a>

An ECS must be in active, stopped, paused, or suspended state, which is specified by  **OS-EXT-STS:vm\_state**.

## URI<a name="section65173692185439"></a>

DELETE /v2/\{project\_id\}/servers/\{server\_id\}/metadata/\{key\}

DELETE /v2.1/\{project\_id\}/servers/\{server\_id\}/metadata/\{key\}

[Table 1](#table14014174185439)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table14014174185439"></a>
<table><thead align="left"><tr id="row32160776185439"><th class="cellrowborder" valign="top" width="16.98%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.36%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.66%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row26570121185439"><td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.1 "><p id="p4696221185439"><a name="p4696221185439"></a><a name="p4696221185439"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.2 "><p id="p44849621185439"><a name="p44849621185439"></a><a name="p44849621185439"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.66%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row13357420185439"><td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.1 "><p id="p8209263185439"><a name="p8209263185439"></a><a name="p8209263185439"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.2 "><p id="p60970546185439"><a name="p60970546185439"></a><a name="p60970546185439"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.66%" headers="mcps1.2.4.1.3 "><p id="p39667165185439"><a name="p39667165185439"></a><a name="p39667165185439"></a>Specifies the ECS ID.</p>
</td>
</tr>
<tr id="row32078344185622"><td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.1 "><p id="p48209085185622"><a name="p48209085185622"></a><a name="p48209085185622"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="17.36%" headers="mcps1.2.4.1.2 "><p id="p12621798185622"><a name="p12621798185622"></a><a name="p12621798185622"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.66%" headers="mcps1.2.4.1.3 "><p id="p15732716185622"><a name="p15732716185622"></a><a name="p15732716185622"></a>Specifies the ECS metadata key value to be deleted.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section21460169185439"></a>

None

## Response<a name="section31286738185439"></a>

None

## Example Request<a name="section43661451124217"></a>

```
DELETE https://{endpoint}/v2/{project_id}/servers/{server_id}/metadata/{key}
DELETE https://{endpoint}/v2.1/{project_id}/servers/{server_id}/metadata/{key}
```

## Example Response<a name="section105131358154219"></a>

None

## Returned Values<a name="section4253667185439"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).


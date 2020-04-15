# Deleting an SSH Key Pair<a name="EN-US_TOPIC_0020212680"></a>

## Function<a name="section33132068"></a>

This API is used to delete a specified SSH key pair based on the SSH key pair name.

## URI<a name="section29753161"></a>

DELETE /v2/\{project\_id\}/os-keypairs/\{keypair\_name\}

DELETE /v2.1/\{project\_id\}/os-keypairs/\{keypair\_name\}

[Table 1](#table48776445)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table48776445"></a>
<table><thead align="left"><tr id="row64721603"><th class="cellrowborder" valign="top" width="20.18%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.169999999999998%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="62.64999999999999%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row8464456"><td class="cellrowborder" valign="top" width="20.18%" headers="mcps1.2.4.1.1 "><p id="p14532322"><a name="p14532322"></a><a name="p14532322"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p36267453"><a name="p36267453"></a><a name="p36267453"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="62.64999999999999%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row65190153"><td class="cellrowborder" valign="top" width="20.18%" headers="mcps1.2.4.1.1 "><p id="p45911036"><a name="p45911036"></a><a name="p45911036"></a>keypair_name</p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.2.4.1.2 "><p id="p27806444"><a name="p27806444"></a><a name="p27806444"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="62.64999999999999%" headers="mcps1.2.4.1.3 "><p id="p37729472"><a name="p37729472"></a><a name="p37729472"></a>Specifies the key pair name.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section66451858"></a>

None

## Response<a name="section61195818"></a>

None

## Example Request<a name="section118665219435"></a>

```
DELETE https://{endpoint}/v2/{project_id}/os-keypairs/{keypair_name}
DELETE https://{endpoint}/v2.1/{project_id}/os-keypairs/{keypair_name}
```

## Example Response<a name="section19716123044320"></a>

None

## Returned Values<a name="section13891457"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).


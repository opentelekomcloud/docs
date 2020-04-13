# Deleting an SNAT Rule<a name="nat_api_0009"></a>

## Function<a name="section20675657"></a>

This API is used to delete an SNAT rule.

## URI<a name="section51863185"></a>

DELETE /v2.0/snat\_rules/\{snat\_rule\_id\}

**Table  1**  Parameter description

<a name="table1910716134591"></a>
<table><thead align="left"><tr id="row3169413135915"><th class="cellrowborder" valign="top" width="25.26252625262526%" id="mcps1.2.5.1.1"><p id="p16169131375910"><a name="p16169131375910"></a><a name="p16169131375910"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13.431343134313432%" id="mcps1.2.5.1.2"><p id="p151699135593"><a name="p151699135593"></a><a name="p151699135593"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="19.2019201920192%" id="mcps1.2.5.1.3"><p id="p1716915133591"><a name="p1716915133591"></a><a name="p1716915133591"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="42.104210421042104%" id="mcps1.2.5.1.4"><p id="p016991320594"><a name="p016991320594"></a><a name="p016991320594"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row131691913145916"><td class="cellrowborder" valign="top" width="25.26252625262526%" headers="mcps1.2.5.1.1 "><p id="p116919133595"><a name="p116919133595"></a><a name="p116919133595"></a>snat_rule_id</p>
</td>
<td class="cellrowborder" valign="top" width="13.431343134313432%" headers="mcps1.2.5.1.2 "><p id="p6169171310597"><a name="p6169171310597"></a><a name="p6169171310597"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="19.2019201920192%" headers="mcps1.2.5.1.3 "><p id="p101695138597"><a name="p101695138597"></a><a name="p101695138597"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="42.104210421042104%" headers="mcps1.2.5.1.4 "><p id="p31691313145913"><a name="p31691313145913"></a><a name="p31691313145913"></a>Specifies the SNAT rule ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section40168441"></a>

None

## Response<a name="section25971650"></a>

None

## Examples<a name="section32418265"></a>

-   Example request

    ```
    DELETE https://{Endpoint}/v2.0/snat_rules/a78fb3eb-1654-4710-8742-3fc49d5f04f8
    ```


-   Example response

    ```
    None (STATUS CODE 204)
    ```


## Status Code<a name="section8633818"></a>

See  [Status Codes](status-codes.md).


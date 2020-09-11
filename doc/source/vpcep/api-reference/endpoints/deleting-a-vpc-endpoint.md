# Deleting a VPC Endpoint<a name="vpcep_06_0305"></a>

## Function<a name="section23326136"></a>

This API is used to delete a VPC endpoint.

## URI<a name="section8608636"></a>

DELETE /v1/\{project\_id\}/vpc-endpoints/\{vpc\_endpoint\_id\}

For detailed about the parameters, see  [Table 1](#table2452701).

**Table  1**  Parameters

<a name="table2452701"></a>
<table><thead align="left"><tr id="row24297719"><th class="cellrowborder" valign="top" width="32.65%" id="mcps1.2.4.1.1"><p id="p21958222"><a name="p21958222"></a><a name="p21958222"></a><strong id="b9157810591"><a name="b9157810591"></a><a name="b9157810591"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26.529999999999998%" id="mcps1.2.4.1.2"><p id="p33785549"><a name="p33785549"></a><a name="p33785549"></a><strong id="b1966812480581"><a name="b1966812480581"></a><a name="b1966812480581"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="40.82%" id="mcps1.2.4.1.3"><p id="p52274973"><a name="p52274973"></a><a name="p52274973"></a><strong id="b3452650145819"><a name="b3452650145819"></a><a name="b3452650145819"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row6414438"><td class="cellrowborder" valign="top" width="32.65%" headers="mcps1.2.4.1.1 "><p id="p49807439"><a name="p49807439"></a><a name="p49807439"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.2 "><p id="p7870720"><a name="p7870720"></a><a name="p7870720"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="40.82%" headers="mcps1.2.4.1.3 "><p id="p33548578"><a name="p33548578"></a><a name="p33548578"></a>Specifies the project ID. For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
</td>
</tr>
<tr id="row33501748"><td class="cellrowborder" valign="top" width="32.65%" headers="mcps1.2.4.1.1 "><p id="p29287106"><a name="p29287106"></a><a name="p29287106"></a>vpc_endpoint_id</p>
</td>
<td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.2 "><p id="p23445396"><a name="p23445396"></a><a name="p23445396"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="40.82%" headers="mcps1.2.4.1.3 "><p id="p20028947"><a name="p20028947"></a><a name="p20028947"></a>Specifies the ID of the VPC endpoint.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section10368864"></a>

-   Parameter description

    None

-   Example request

    This request is to delete the VPC endpoint whose ID is  **4189d3c2-8882-4871-a3c2-d380272eed83**.

    ```
    DELETE https://{endpoint}/v1/{project_id}/vpc-endpoints/4189d3c2-8882-4871-a3c2-d380272eed83
    ```


## Response<a name="section34571669"></a>

None

## Status Code<a name="section48841790"></a>

For details about status codes, see  [Status Code](/vpcep/api-reference/common/status-code.md).


# Deleting a VPC Endpoint Service<a name="vpcep_06_0204"></a>

## Function<a name="section17315029"></a>

This API is used to delete a VPC endpoint service.

## URI<a name="section21617533"></a>

DELETE /v1/\{project\_id\}/vpc-endpoint-services/\{vpc\_endpoint\_service\_id\}

[Table 1](#table35049127)  describes the required parameters.

**Table  1**  Parameters

<a name="table35049127"></a>
<table><thead align="left"><tr id="row6237533"><th class="cellrowborder" valign="top" width="32.65%" id="mcps1.2.4.1.1"><p id="p35478198"><a name="p35478198"></a><a name="p35478198"></a><strong id="b151561431185516"><a name="b151561431185516"></a><a name="b151561431185516"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26.529999999999998%" id="mcps1.2.4.1.2"><p id="p55161795"><a name="p55161795"></a><a name="p55161795"></a><strong id="b12208143912552"><a name="b12208143912552"></a><a name="b12208143912552"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="40.82%" id="mcps1.2.4.1.3"><p id="p38920429"><a name="p38920429"></a><a name="p38920429"></a><strong id="b17240340135510"><a name="b17240340135510"></a><a name="b17240340135510"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row65547035"><td class="cellrowborder" valign="top" width="32.65%" headers="mcps1.2.4.1.1 "><p id="p7709622"><a name="p7709622"></a><a name="p7709622"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.2 "><p id="p20499621"><a name="p20499621"></a><a name="p20499621"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="40.82%" headers="mcps1.2.4.1.3 "><p id="p49856593"><a name="p49856593"></a><a name="p49856593"></a>Specifies the project ID. For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
</td>
</tr>
<tr id="row46056153"><td class="cellrowborder" valign="top" width="32.65%" headers="mcps1.2.4.1.1 "><p id="p39560874"><a name="p39560874"></a><a name="p39560874"></a>vpc_endpoint_service_id</p>
</td>
<td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.2.4.1.2 "><p id="p50314220"><a name="p50314220"></a><a name="p50314220"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="40.82%" headers="mcps1.2.4.1.3 "><p id="p48920006"><a name="p48920006"></a><a name="p48920006"></a>Specifies the ID of the VPC endpoint service.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section60340071"></a>

-   Parameter description

    None

-   Example request

    This request is to delete the VPC endpoint service whose ID is  **4189d3c2-8882-4871-a3c2-d380272eed88**.

    ```
    DELETE https://{endpoint}/v1/{project_id}/vpc-endpoint-services/4189d3c2-8882-4871-a3c2-d380272eed88
    ```


## Response<a name="section4368746203313"></a>

None

## Status Code<a name="section9976838"></a>

For details about status codes, see  [Status Code](/vpcep/api-reference/common/status-code.md).


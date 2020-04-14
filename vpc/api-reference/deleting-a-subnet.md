# Deleting a Subnet<a name="vpc_subnet01_0005"></a>

## Function<a name="section36031167"></a>

This API is used to delete a subnet.

## URI<a name="section55845053"></a>

DELETE /v1/\{project\_id\}/vpcs/\{vpc\_id\}/subnets/\{subnet\_id\}

[Table 1](#table23279683)  describes the parameters.

**Table  1**  Parameter description

<a name="table23279683"></a>
<table><thead align="left"><tr id="row57883273"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p58033516"><a name="p58033516"></a><a name="p58033516"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p3094327"><a name="p3094327"></a><a name="p3094327"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p49313939"><a name="p49313939"></a><a name="p49313939"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row35006119"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p16923420"><a name="p16923420"></a><a name="p16923420"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p28619802"><a name="p28619802"></a><a name="p28619802"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row29689498122133"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p37198247122136"><a name="p37198247122136"></a><a name="p37198247122136"></a>vpc_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p60268063122136"><a name="p60268063122136"></a><a name="p60268063122136"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p49874919122136"><a name="p49874919122136"></a><a name="p49874919122136"></a>Specifies the ID of the subnet VPC.</p>
</td>
</tr>
<tr id="row60087944"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p35285314"><a name="p35285314"></a><a name="p35285314"></a>subnet_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p39538176"><a name="p39538176"></a><a name="p39538176"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p48475691"><a name="p48475691"></a><a name="p48475691"></a>Specifies the subnet ID, which uniquely identifies the subnet.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section32843429"></a>

-   Request parameter

    None

-   Example request

    ```
    DELETE https://{Endpoint}/v1/{project_id}/vpcs/{vpc_id}/subnets/4779ab1c-7c1a-44b1-a02e-93dfc361b32d
    ```


## Response Message<a name="section27155410"></a>

-   Response parameter

    None

-   Example response

    None


## Status Code<a name="section31981619"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).


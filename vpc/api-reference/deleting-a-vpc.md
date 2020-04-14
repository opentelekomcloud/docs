# Deleting a VPC<a name="vpc_api01_0005"></a>

## Function<a name="section15422169"></a>

This API is used to delete a VPC.

## URI<a name="section4581796"></a>

DELETE /v1/\{project\_id\}/vpcs/\{vpc\_id\}

[Table 1](#table47834478)  describes the parameters.

**Table  1**  Parameter description

<a name="table47834478"></a>
<table><thead align="left"><tr id="row29612923"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p49836563"><a name="p49836563"></a><a name="p49836563"></a>Name</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p10229816"><a name="p10229816"></a><a name="p10229816"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p23308753"><a name="p23308753"></a><a name="p23308753"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row8960839"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p54739329"><a name="p54739329"></a><a name="p54739329"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p4700647"><a name="p4700647"></a><a name="p4700647"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID. </p>
</td>
</tr>
<tr id="row4220283"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p6298672"><a name="p6298672"></a><a name="p6298672"></a>vpc_id</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p40430446"><a name="p40430446"></a><a name="p40430446"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p53640668"><a name="p53640668"></a><a name="p53640668"></a>Specifies the VPC ID, which uniquely identifies the VPC.</p>
</td>
</tr>
</tbody>
</table>

## Request Message<a name="section41236172"></a>

-   Request parameter

    None

-   Example request

    ```
    DELETE https://{Endpoint}/v1/{project_id}/vpcs/13551d6b-755d-4757-b956-536f674975c0
    ```


## Response Message<a name="section35581233"></a>

-   Response parameter

    None


-   Example response

    None


## Status Code<a name="section31981619"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).


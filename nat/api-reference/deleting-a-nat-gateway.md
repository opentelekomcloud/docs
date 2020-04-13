# Deleting a NAT Gateway<a name="nat_api_0004"></a>

## Function<a name="section23460301"></a>

This API is used to delete a NAT gateway.

## URI<a name="section9816121"></a>

DELETE /v2.0/nat\_gateways/\{nat\_gateway\_id\}

**Table  1**  Parameter description

<a name="table285161395713"></a>
<table><thead align="left"><tr id="row12912101317577"><th class="cellrowborder" valign="top" width="22.57%" id="mcps1.2.5.1.1"><p id="p791271313579"><a name="p791271313579"></a><a name="p791271313579"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="8.649999999999999%" id="mcps1.2.5.1.2"><p id="p1391221355716"><a name="p1391221355716"></a><a name="p1391221355716"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="12.9%" id="mcps1.2.5.1.3"><p id="p7912013105718"><a name="p7912013105718"></a><a name="p7912013105718"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="55.879999999999995%" id="mcps1.2.5.1.4"><p id="p1191216131572"><a name="p1191216131572"></a><a name="p1191216131572"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1591281345717"><td class="cellrowborder" valign="top" width="22.57%" headers="mcps1.2.5.1.1 "><p id="p69121213115717"><a name="p69121213115717"></a><a name="p69121213115717"></a>nat_gateway_id</p>
</td>
<td class="cellrowborder" valign="top" width="8.649999999999999%" headers="mcps1.2.5.1.2 "><p id="p1291281325710"><a name="p1291281325710"></a><a name="p1291281325710"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="12.9%" headers="mcps1.2.5.1.3 "><p id="p179129138573"><a name="p179129138573"></a><a name="p179129138573"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="55.879999999999995%" headers="mcps1.2.5.1.4 "><p id="p20912111395719"><a name="p20912111395719"></a><a name="p20912111395719"></a>Specifies the NAT gateway ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section56908304"></a>

None

## Response<a name="section42412694"></a>

None

## Examples<a name="section46169932"></a>

-   Example request

    ```
    DELETE https://{Endpoint}/v2.0/nat_gateways/a78fb3eb-1654-4710-8742-3fc49d5f04f8
    ```


-   Example response

    ```
    None (STATUS CODE 204)
    ```


## Status Code<a name="section48777045"></a>

See  [Status Codes](status-codes.md).


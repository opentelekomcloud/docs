# Deleting a Virtual Interface<a name="en-dc_topic_0055025331"></a>

## Function<a name="section235045714306"></a>

This API is used to delete a virtual interface.

## URI<a name="section4104188114306"></a>

DELETE /v2.0/dcaas/virtual-interfaces/\{virtual\_interface\_id\}

**Table  1**  Parameter description

<a name="table640636113810"></a>
<table><thead align="left"><tr id="row1546856113814"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p12468664381"><a name="p12468664381"></a><a name="p12468664381"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p346866153810"><a name="p346866153810"></a><a name="p346866153810"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p04683613389"><a name="p04683613389"></a><a name="p04683613389"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p13468206123813"><a name="p13468206123813"></a><a name="p13468206123813"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row12468166143815"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p24687693816"><a name="p24687693816"></a><a name="p24687693816"></a>virtual_interface_id</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p8468136203815"><a name="p8468136203815"></a><a name="p8468136203815"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p44681561384"><a name="p44681561384"></a><a name="p44681561384"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p246813663813"><a name="p246813663813"></a><a name="p246813663813"></a>Indicates the virtual interface ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section3850154614306"></a>

[Table 2](#table5224055914306)  lists the request parameter.

**Table  2**  Request parameter

<a name="table5224055914306"></a>
<table><thead align="left"><tr id="row6052323214306"><th class="cellrowborder" valign="top" width="24.84%" id="mcps1.2.5.1.1"><p id="p1875992714306"><a name="p1875992714306"></a><a name="p1875992714306"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="12.22%" id="mcps1.2.5.1.2"><p id="p523663814306"><a name="p523663814306"></a><a name="p523663814306"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="16.509999999999998%" id="mcps1.2.5.1.3"><p id="p99311514306"><a name="p99311514306"></a><a name="p99311514306"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="46.43%" id="mcps1.2.5.1.4"><p id="p6490218014306"><a name="p6490218014306"></a><a name="p6490218014306"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row2775932614306"><td class="cellrowborder" valign="top" width="24.84%" headers="mcps1.2.5.1.1 "><p id="p4251721614306"><a name="p4251721614306"></a><a name="p4251721614306"></a>virtual_interface_id</p>
</td>
<td class="cellrowborder" valign="top" width="12.22%" headers="mcps1.2.5.1.2 "><p id="p6380017614306"><a name="p6380017614306"></a><a name="p6380017614306"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="16.509999999999998%" headers="mcps1.2.5.1.3 "><p id="p1079430814306"><a name="p1079430814306"></a><a name="p1079430814306"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="46.43%" headers="mcps1.2.5.1.4 "><p id="p4809318514306"><a name="p4809318514306"></a><a name="p4809318514306"></a>Indicates the virtual interface ID.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section1670969814306"></a>

None

## Examples<a name="section3828902514306"></a>

-   Example request

```
DELETE /v2.0/dcaas/virtual-interfaces/{virtual_interface_id}
```

-   Response example

    None


## Returned Value<a name="section6289309617342"></a>

For details, see section  [Common Returned Values](common-returned-values.md).


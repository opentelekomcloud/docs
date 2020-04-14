# Adding an Interface to a Router<a name="vpc_router_0006"></a>

## Function<a name="section57792052205835"></a>

This API is used to add an interface to a router.

Restrictions

-   When a port is used, the port can have only one IP address.
-   When a subnet is used, the gateway IP address must be configured for the subnet.
-   A router cannot be added to networks whose  **provider:network\_type**  is  **geneve**.
-   Only one router can be added to a subnet.

## URI<a name="section53148261205835"></a>

PUT /v2.0/routers/\{router\_id\}/add\_router\_interface

## Request Message<a name="section46335438205835"></a>

**Table  1**  Request parameter

<a name="table62182974205835"></a>
<table><thead align="left"><tr id="row2403081205835"><th class="cellrowborder" valign="top" width="17.349999999999998%" id="mcps1.2.5.1.1"><p id="p60431871205835"><a name="p60431871205835"></a><a name="p60431871205835"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.29%" id="mcps1.2.5.1.2"><p id="p63143353205835"><a name="p63143353205835"></a><a name="p63143353205835"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="18.279999999999998%" id="mcps1.2.5.1.3"><p id="p14337951205835"><a name="p14337951205835"></a><a name="p14337951205835"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="50.080000000000005%" id="mcps1.2.5.1.4"><p id="p20523419205835"><a name="p20523419205835"></a><a name="p20523419205835"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row51784210205835"><td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.5.1.1 "><p id="p33771502205835"><a name="p33771502205835"></a><a name="p33771502205835"></a>subnet_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.2.5.1.2 "><p id="p51137175205835"><a name="p51137175205835"></a><a name="p51137175205835"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="18.279999999999998%" headers="mcps1.2.5.1.3 "><p id="p48470516205835"><a name="p48470516205835"></a><a name="p48470516205835"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="50.080000000000005%" headers="mcps1.2.5.1.4 "><p id="p33797742205835"><a name="p33797742205835"></a><a name="p33797742205835"></a>Specifies the subnet ID. Either <strong id="b842352706191715"><a name="b842352706191715"></a><a name="b842352706191715"></a>subnet_id</strong> or <strong id="b842352706191719"><a name="b842352706191719"></a><a name="b842352706191719"></a>port_id</strong> is used.</p>
<p id="p35744225205835"><a name="p35744225205835"></a><a name="p35744225205835"></a>Use the gateway IP address of the subnet to create a router interface.</p>
</td>
</tr>
<tr id="row53262572205835"><td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.5.1.1 "><p id="p19301079205835"><a name="p19301079205835"></a><a name="p19301079205835"></a>port_id</p>
</td>
<td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.2.5.1.2 "><p id="p19883542205835"><a name="p19883542205835"></a><a name="p19883542205835"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="18.279999999999998%" headers="mcps1.2.5.1.3 "><p id="p67063058205835"><a name="p67063058205835"></a><a name="p67063058205835"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="50.080000000000005%" headers="mcps1.2.5.1.4 "><p id="p63398578205835"><a name="p63398578205835"></a><a name="p63398578205835"></a>Specifies the port ID. Either <strong id="b1556928203191732"><a name="b1556928203191732"></a><a name="b1556928203191732"></a>subnet_id</strong> or <strong id="b2095602666191732"><a name="b2095602666191732"></a><a name="b2095602666191732"></a>port_id</strong> is used. Use the port IP address to create a router interface.</p>
</td>
</tr>
</tbody>
</table>

## Response Message<a name="section33716291205835"></a>

**Table  2**  Response parameter

<a name="table46665045205835"></a>
<table><thead align="left"><tr id="row27310894205835"><th class="cellrowborder" valign="top" width="19.32%" id="mcps1.2.4.1.1"><p id="p64698801205835"><a name="p64698801205835"></a><a name="p64698801205835"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15.909999999999998%" id="mcps1.2.4.1.2"><p id="p6111537205835"><a name="p6111537205835"></a><a name="p6111537205835"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="64.77000000000001%" id="mcps1.2.4.1.3"><p id="p33804102205835"><a name="p33804102205835"></a><a name="p33804102205835"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row53777707205835"><td class="cellrowborder" valign="top" width="19.32%" headers="mcps1.2.4.1.1 "><p id="p61026988205835"><a name="p61026988205835"></a><a name="p61026988205835"></a>subnet_id</p>
</td>
<td class="cellrowborder" valign="top" width="15.909999999999998%" headers="mcps1.2.4.1.2 "><p id="p44239027205835"><a name="p44239027205835"></a><a name="p44239027205835"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.77000000000001%" headers="mcps1.2.4.1.3 "><p id="p6419564205835"><a name="p6419564205835"></a><a name="p6419564205835"></a>Specifies the subnet ID.</p>
</td>
</tr>
<tr id="row57776083205835"><td class="cellrowborder" valign="top" width="19.32%" headers="mcps1.2.4.1.1 "><p id="p49351156205835"><a name="p49351156205835"></a><a name="p49351156205835"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="15.909999999999998%" headers="mcps1.2.4.1.2 "><p id="p38020701205835"><a name="p38020701205835"></a><a name="p38020701205835"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.77000000000001%" headers="mcps1.2.4.1.3 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row24491644205835"><td class="cellrowborder" valign="top" width="19.32%" headers="mcps1.2.4.1.1 "><p id="p37666118205835"><a name="p37666118205835"></a><a name="p37666118205835"></a>port_id</p>
</td>
<td class="cellrowborder" valign="top" width="15.909999999999998%" headers="mcps1.2.4.1.2 "><p id="p31056700205835"><a name="p31056700205835"></a><a name="p31056700205835"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.77000000000001%" headers="mcps1.2.4.1.3 "><p id="p20503759205835"><a name="p20503759205835"></a><a name="p20503759205835"></a>Specifies the port ID.</p>
</td>
</tr>
<tr id="row50316109205835"><td class="cellrowborder" valign="top" width="19.32%" headers="mcps1.2.4.1.1 "><p id="p49073051205835"><a name="p49073051205835"></a><a name="p49073051205835"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="15.909999999999998%" headers="mcps1.2.4.1.2 "><p id="p15494169205835"><a name="p15494169205835"></a><a name="p15494169205835"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.77000000000001%" headers="mcps1.2.4.1.3 "><p id="p54423238205835"><a name="p54423238205835"></a><a name="p54423238205835"></a>Specifies the router ID.</p>
</td>
</tr>
</tbody>
</table>

## Example:<a name="section20047097205835"></a>

Example request

```
PUT https://{Endpoint}/v2.0/routers/5b8e885c-1347-4ac2-baf9-2249c8ed1270/add_router_interface

{"subnet_id": "ab78be2d-782f-42a5-aa72-35879f6890ff"}
```

Example response

```
{
  "subnet_id": "ab78be2d-782f-42a5-aa72-35879f6890ff",
  "tenant_id": "6fbe9263116a4b68818cf1edce16bc4f",
  "port_id": "40e86635-b2a3-45de-a7c8-3cced5b7e755",
  "id": "5b8e885c-1347-4ac2-baf9-2249c8ed1270"
}
```

## Status Code<a name="section10470352390"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).


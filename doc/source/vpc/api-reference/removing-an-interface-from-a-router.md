# Removing an Interface from a Router<a name="vpc_router_0007"></a>

## Function<a name="section30197552205849"></a>

This API is used to remove an interface from a router.

Restrictions

You are not allowed to remove an interface from a router if the subnet contains load balancer objects.

## URI<a name="section2308632205849"></a>

PUT /v2.0/routers/\{router\_id\}/remove\_router\_interface

## Request Message<a name="section55215913205849"></a>

**Table  1**  Request parameter

<a name="table43303993205849"></a>
<table><thead align="left"><tr id="row15734591205849"><th class="cellrowborder" valign="top" width="18.099999999999998%" id="mcps1.2.5.1.1"><p id="p66542384205849"><a name="p66542384205849"></a><a name="p66542384205849"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13.54%" id="mcps1.2.5.1.2"><p id="p21224062205849"><a name="p21224062205849"></a><a name="p21224062205849"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="18.09%" id="mcps1.2.5.1.3"><p id="p41427472205849"><a name="p41427472205849"></a><a name="p41427472205849"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="50.27%" id="mcps1.2.5.1.4"><p id="p182095205849"><a name="p182095205849"></a><a name="p182095205849"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row14749730205849"><td class="cellrowborder" valign="top" width="18.099999999999998%" headers="mcps1.2.5.1.1 "><p id="p53877490205849"><a name="p53877490205849"></a><a name="p53877490205849"></a>subnet_id</p>
</td>
<td class="cellrowborder" valign="top" width="13.54%" headers="mcps1.2.5.1.2 "><p id="p2000550205849"><a name="p2000550205849"></a><a name="p2000550205849"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="18.09%" headers="mcps1.2.5.1.3 "><p id="p27826855205849"><a name="p27826855205849"></a><a name="p27826855205849"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="50.27%" headers="mcps1.2.5.1.4 "><p id="p39382748205849"><a name="p39382748205849"></a><a name="p39382748205849"></a>Specifies the subnet ID. Either <strong id="b3115262052"><a name="b3115262052"></a><a name="b3115262052"></a>subnet_id</strong> or <strong id="b91215269520"><a name="b91215269520"></a><a name="b91215269520"></a>port_id</strong> must be specified.</p>
<p id="p18900413205849"><a name="p18900413205849"></a><a name="p18900413205849"></a>Use the gateway IP address of the subnet to create a router interface.</p>
</td>
</tr>
<tr id="row35885997205849"><td class="cellrowborder" valign="top" width="18.099999999999998%" headers="mcps1.2.5.1.1 "><p id="p21084676205849"><a name="p21084676205849"></a><a name="p21084676205849"></a>port_id</p>
</td>
<td class="cellrowborder" valign="top" width="13.54%" headers="mcps1.2.5.1.2 "><p id="p30137158205849"><a name="p30137158205849"></a><a name="p30137158205849"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="18.09%" headers="mcps1.2.5.1.3 "><p id="p25190749205849"><a name="p25190749205849"></a><a name="p25190749205849"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="50.27%" headers="mcps1.2.5.1.4 "><p id="p27184817205849"><a name="p27184817205849"></a><a name="p27184817205849"></a>Specifies the port ID. Either <strong id="b1556928203191732"><a name="b1556928203191732"></a><a name="b1556928203191732"></a>subnet_id</strong> or <strong id="b2095602666191732"><a name="b2095602666191732"></a><a name="b2095602666191732"></a>port_id</strong> is used. Use the port IP address to create a router interface.</p>
</td>
</tr>
</tbody>
</table>

## Response Message<a name="section43336765205849"></a>

**Table  2**  Response parameter

<a name="table20617078205849"></a>
<table><thead align="left"><tr id="row10859799205849"><th class="cellrowborder" valign="top" width="19.32%" id="mcps1.2.4.1.1"><p id="p7228509205849"><a name="p7228509205849"></a><a name="p7228509205849"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15.909999999999998%" id="mcps1.2.4.1.2"><p id="p48638393205849"><a name="p48638393205849"></a><a name="p48638393205849"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="64.77000000000001%" id="mcps1.2.4.1.3"><p id="p13848780205849"><a name="p13848780205849"></a><a name="p13848780205849"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row48009429205849"><td class="cellrowborder" valign="top" width="19.32%" headers="mcps1.2.4.1.1 "><p id="p63558546205849"><a name="p63558546205849"></a><a name="p63558546205849"></a>subnet_id</p>
</td>
<td class="cellrowborder" valign="top" width="15.909999999999998%" headers="mcps1.2.4.1.2 "><p id="p47968620205849"><a name="p47968620205849"></a><a name="p47968620205849"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.77000000000001%" headers="mcps1.2.4.1.3 "><p id="p48654997205849"><a name="p48654997205849"></a><a name="p48654997205849"></a>Specifies the subnet ID.</p>
</td>
</tr>
<tr id="row35241790205849"><td class="cellrowborder" valign="top" width="19.32%" headers="mcps1.2.4.1.1 "><p id="p36012759205849"><a name="p36012759205849"></a><a name="p36012759205849"></a>tenant_id</p>
</td>
<td class="cellrowborder" valign="top" width="15.909999999999998%" headers="mcps1.2.4.1.2 "><p id="p31352336205849"><a name="p31352336205849"></a><a name="p31352336205849"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.77000000000001%" headers="mcps1.2.4.1.3 "><p id="p10487112"><a name="p10487112"></a><a name="p10487112"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row58967197205849"><td class="cellrowborder" valign="top" width="19.32%" headers="mcps1.2.4.1.1 "><p id="p11613691205849"><a name="p11613691205849"></a><a name="p11613691205849"></a>port_id</p>
</td>
<td class="cellrowborder" valign="top" width="15.909999999999998%" headers="mcps1.2.4.1.2 "><p id="p1184925205849"><a name="p1184925205849"></a><a name="p1184925205849"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.77000000000001%" headers="mcps1.2.4.1.3 "><p id="p56778703205849"><a name="p56778703205849"></a><a name="p56778703205849"></a>Specifies the port ID.</p>
</td>
</tr>
<tr id="row41246284205849"><td class="cellrowborder" valign="top" width="19.32%" headers="mcps1.2.4.1.1 "><p id="p52614697205849"><a name="p52614697205849"></a><a name="p52614697205849"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="15.909999999999998%" headers="mcps1.2.4.1.2 "><p id="p33932046205849"><a name="p33932046205849"></a><a name="p33932046205849"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="64.77000000000001%" headers="mcps1.2.4.1.3 "><p id="p28056338205849"><a name="p28056338205849"></a><a name="p28056338205849"></a>Specifies the router ID.</p>
</td>
</tr>
</tbody>
</table>

## Example:<a name="section51180458205849"></a>

Example request

```
PUT https://{Endpoint}/v2.0/routers/b625c58c-0cfe-49e0-acc8-f2374f8187ff/remove_router_interface

{"subnet_id": "4b910a10-0860-428b-b463-d84dbc5e288e"}
```

Example response

```
{
  "subnet_id": "4b910a10-0860-428b-b463-d84dbc5e288e",
  "tenant_id": "3d72597871904daeb6887f75f848b531",
  "port_id": "34d7d063-8f40-4958-b420-096db40d4067",
  "id": "b625c58c-0cfe-49e0-acc8-f2374f8187ff"
}
```

## Status Code<a name="section10470352390"></a>

See  [Status Codes](status-codes.md).

## Error Code<a name="section85821649202813"></a>

See  [Error Codes](error-codes.md).


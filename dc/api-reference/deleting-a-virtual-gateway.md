# Deleting a Virtual Gateway<a name="en-dc_topic_0055025324"></a>

## Function<a name="section43031324205035"></a>

This API is used to delete a virtual gateway.

## URI<a name="section29996404205035"></a>

DELETE /v2.0/dcaas/virtual-gateways/\{virtual\_gateway\_id\}

**Table  1**  Parameter description

<a name="table2653155192017"></a>
<table><thead align="left"><tr id="row165355510201"><th class="cellrowborder" valign="top" width="19.388061193880613%" id="mcps1.2.5.1.1"><p id="p1865314551207"><a name="p1865314551207"></a><a name="p1865314551207"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="21.42785721427857%" id="mcps1.2.5.1.2"><p id="p965345514201"><a name="p965345514201"></a><a name="p965345514201"></a><strong id="b842352706165439"><a name="b842352706165439"></a><a name="b842352706165439"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="16.328367163283673%" id="mcps1.2.5.1.3"><p id="p136531556208"><a name="p136531556208"></a><a name="p136531556208"></a><strong id="b842352706192549"><a name="b842352706192549"></a><a name="b842352706192549"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="42.85571442855714%" id="mcps1.2.5.1.4"><p id="p14660155542013"><a name="p14660155542013"></a><a name="p14660155542013"></a><strong id="b84235270615331"><a name="b84235270615331"></a><a name="b84235270615331"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row13660145572012"><td class="cellrowborder" valign="top" width="19.388061193880613%" headers="mcps1.2.5.1.1 "><p id="p866020558209"><a name="p866020558209"></a><a name="p866020558209"></a>virtual_gateway_id</p>
</td>
<td class="cellrowborder" valign="top" width="21.42785721427857%" headers="mcps1.2.5.1.2 "><p id="p9660145552017"><a name="p9660145552017"></a><a name="p9660145552017"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="16.328367163283673%" headers="mcps1.2.5.1.3 "><p id="p12660195532019"><a name="p12660195532019"></a><a name="p12660195532019"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="42.85571442855714%" headers="mcps1.2.5.1.4 "><p id="p866065522015"><a name="p866065522015"></a><a name="p866065522015"></a>Indicates the virtual gateway ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section54655929205035"></a>

[Table 2](#table2198437322244)  lists the request parameter.

**Table  2**  Request parameter

<a name="table2198437322244"></a>
<table><thead align="left"><tr id="row4304807922244"><th class="cellrowborder" valign="top" width="25.217478252174786%" id="mcps1.2.5.1.1"><p id="p6505580022244"><a name="p6505580022244"></a><a name="p6505580022244"></a><strong id="b8423527069918"><a name="b8423527069918"></a><a name="b8423527069918"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="13.528647135286477%" id="mcps1.2.5.1.2"><p id="p329696222244"><a name="p329696222244"></a><a name="p329696222244"></a><strong id="b842352706165439_1"><a name="b842352706165439_1"></a><a name="b842352706165439_1"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="18.398160183981606%" id="mcps1.2.5.1.3"><p id="p3257067222244"><a name="p3257067222244"></a><a name="p3257067222244"></a><strong id="b842352706192549_1"><a name="b842352706192549_1"></a><a name="b842352706192549_1"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="42.85571442855715%" id="mcps1.2.5.1.4"><p id="p5470821922244"><a name="p5470821922244"></a><a name="p5470821922244"></a><strong id="b84235270615331_1"><a name="b84235270615331_1"></a><a name="b84235270615331_1"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row5451891922244"><td class="cellrowborder" valign="top" width="25.217478252174786%" headers="mcps1.2.5.1.1 "><p id="p3187982384832"><a name="p3187982384832"></a><a name="p3187982384832"></a>virtual_gateway_id</p>
</td>
<td class="cellrowborder" valign="top" width="13.528647135286477%" headers="mcps1.2.5.1.2 "><p id="p757920222316"><a name="p757920222316"></a><a name="p757920222316"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="18.398160183981606%" headers="mcps1.2.5.1.3 "><p id="p4706384922316"><a name="p4706384922316"></a><a name="p4706384922316"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="42.85571442855715%" headers="mcps1.2.5.1.4 "><p id="p970883222316"><a name="p970883222316"></a><a name="p970883222316"></a>Indicates the virtual gateway ID.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section48616095205035"></a>

None

## Examples<a name="section7653394205035"></a>

-   Example request

```
DELETE /v2.0/dcaas/virtual-gateways/{virtual_gateway_id}
```

-   Response example

    None


## Returned Value<a name="section5604023173234"></a>

For details, see section  [Common Returned Values](common-returned-values.md).


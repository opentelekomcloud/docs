# Disassociating an FPGA Image from an ECS Image<a name="EN-US_TOPIC_0081950549"></a>

## Function<a name="section43795230211632"></a>

This API is used to delete a mapping between an FPGA image and an ECS image.

## URI<a name="section28033540211632"></a>

DELETE /v1/\{project\_id\}/cloudservers/fpga\_image/\{fpga\_image\_id\}/association

[Table 1](#table28107133211632)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table28107133211632"></a>
<table><thead align="left"><tr id="row19177941211632"><th class="cellrowborder" valign="top" width="19.96%" id="mcps1.2.4.1.1"><p id="p7707213"><a name="p7707213"></a><a name="p7707213"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.16%" id="mcps1.2.4.1.2"><p id="p20304554"><a name="p20304554"></a><a name="p20304554"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="62.88%" id="mcps1.2.4.1.3"><p id="p34056167"><a name="p34056167"></a><a name="p34056167"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row33377558211632"><td class="cellrowborder" valign="top" width="19.96%" headers="mcps1.2.4.1.1 "><p id="p53863828211632"><a name="p53863828211632"></a><a name="p53863828211632"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.16%" headers="mcps1.2.4.1.2 "><p id="p47645557211632"><a name="p47645557211632"></a><a name="p47645557211632"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="62.88%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row176964211632"><td class="cellrowborder" valign="top" width="19.96%" headers="mcps1.2.4.1.1 "><p id="p48913232211632"><a name="p48913232211632"></a><a name="p48913232211632"></a>fpga_image_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.16%" headers="mcps1.2.4.1.2 "><p id="p66905560211632"><a name="p66905560211632"></a><a name="p66905560211632"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="62.88%" headers="mcps1.2.4.1.3 "><p id="p5594788211632"><a name="p5594788211632"></a><a name="p5594788211632"></a>Specifies the FPGA image ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section3313651211632"></a>

[Table 2](#table41782128362)  describes the request parameters.

**Table  2**  Request parameters

<a name="table41782128362"></a>
<table><thead align="left"><tr id="row17178181253615"><th class="cellrowborder" valign="top" width="19.919999999999998%" id="mcps1.2.5.1.1"><p id="p3178612173615"><a name="p3178612173615"></a><a name="p3178612173615"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.23%" id="mcps1.2.5.1.2"><p id="p2017861210364"><a name="p2017861210364"></a><a name="p2017861210364"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="17.49%" id="mcps1.2.5.1.3"><p id="p1775122317363"><a name="p1775122317363"></a><a name="p1775122317363"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="48.36%" id="mcps1.2.5.1.4"><p id="p71791812113610"><a name="p71791812113610"></a><a name="p71791812113610"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row817971293614"><td class="cellrowborder" valign="top" width="19.919999999999998%" headers="mcps1.2.5.1.1 "><p id="p54426520364"><a name="p54426520364"></a><a name="p54426520364"></a>image</p>
</td>
<td class="cellrowborder" valign="top" width="14.23%" headers="mcps1.2.5.1.2 "><p id="p12442185213364"><a name="p12442185213364"></a><a name="p12442185213364"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="17.49%" headers="mcps1.2.5.1.3 "><p id="p16442195218369"><a name="p16442195218369"></a><a name="p16442195218369"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="48.36%" headers="mcps1.2.5.1.4 "><p id="p15444145213368"><a name="p15444145213368"></a><a name="p15444145213368"></a>Specifies the ECS image.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **image**  field description

<a name="table9461983324"></a>
<table><thead align="left"><tr id="row1546112813212"><th class="cellrowborder" valign="top" width="19.92%" id="mcps1.2.5.1.1"><p id="p14613820329"><a name="p14613820329"></a><a name="p14613820329"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.290000000000003%" id="mcps1.2.5.1.2"><p id="p946168183217"><a name="p946168183217"></a><a name="p946168183217"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="17.480000000000004%" id="mcps1.2.5.1.3"><p id="p47957996211632"><a name="p47957996211632"></a><a name="p47957996211632"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="48.31%" id="mcps1.2.5.1.4"><p id="p184616815328"><a name="p184616815328"></a><a name="p184616815328"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row346158143218"><td class="cellrowborder" valign="top" width="19.92%" headers="mcps1.2.5.1.1 "><p id="p8461188173210"><a name="p8461188173210"></a><a name="p8461188173210"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="14.290000000000003%" headers="mcps1.2.5.1.2 "><p id="p946220803218"><a name="p946220803218"></a><a name="p946220803218"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.480000000000004%" headers="mcps1.2.5.1.3 "><p id="p27767370211632"><a name="p27767370211632"></a><a name="p27767370211632"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="48.31%" headers="mcps1.2.5.1.4 "><p id="p046218183218"><a name="p046218183218"></a><a name="p046218183218"></a>Specifies the ECS image ID.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section727655211632"></a>

None

## Example Request<a name="section47627159211632"></a>

```
DELETE https://{endpoint}/v1/{project_id}/cloudservers/fpga_image/{fpga_image_id}/association
```

```
{
  "image": {
    "id": "18efee75-e058-4c52-a49c-9e3ba4d1c8de"
  }
}
```

## Example Response<a name="section15218105142815"></a>

None

## Returned Values<a name="section3477250491225"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

## Error Codes<a name="section85821649202813"></a>

See  [Error Code Description](error-code-description.md).


# Associating an FPGA Image with an ECS Image<a name="EN-US_TOPIC_0065962598"></a>

## Function<a name="section43795230211632"></a>

This API is used to create a mapping between an FPGA image and an ECS image.

## URI<a name="section28033540211632"></a>

POST /v1/\{project\_id\}/cloudservers/fpga\_image/\{fpga\_image\_id\}/association

[Table 1](#table28107133211632)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table28107133211632"></a>
<table><thead align="left"><tr id="row19177941211632"><th class="cellrowborder" valign="top" width="19.42%" id="mcps1.2.4.1.1"><p id="p7707213"><a name="p7707213"></a><a name="p7707213"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.349999999999998%" id="mcps1.2.4.1.2"><p id="p20304554"><a name="p20304554"></a><a name="p20304554"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="63.23%" id="mcps1.2.4.1.3"><p id="p34056167"><a name="p34056167"></a><a name="p34056167"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row33377558211632"><td class="cellrowborder" valign="top" width="19.42%" headers="mcps1.2.4.1.1 "><p id="p53863828211632"><a name="p53863828211632"></a><a name="p53863828211632"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p47645557211632"><a name="p47645557211632"></a><a name="p47645557211632"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="63.23%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row176964211632"><td class="cellrowborder" valign="top" width="19.42%" headers="mcps1.2.4.1.1 "><p id="p48913232211632"><a name="p48913232211632"></a><a name="p48913232211632"></a>fpga_image_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.349999999999998%" headers="mcps1.2.4.1.2 "><p id="p66905560211632"><a name="p66905560211632"></a><a name="p66905560211632"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="63.23%" headers="mcps1.2.4.1.3 "><p id="p5594788211632"><a name="p5594788211632"></a><a name="p5594788211632"></a>Specifies the FPGA image ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section3313651211632"></a>

[Table 2](#table41782128362)  describes the request parameters.

**Table  2**  Request parameters

<a name="table41782128362"></a>
<table><thead align="left"><tr id="row17178181253615"><th class="cellrowborder" valign="top" width="19.36%" id="mcps1.2.5.1.1"><p id="p3178612173615"><a name="p3178612173615"></a><a name="p3178612173615"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13.469999999999999%" id="mcps1.2.5.1.2"><p id="p2017861210364"><a name="p2017861210364"></a><a name="p2017861210364"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="17.68%" id="mcps1.2.5.1.3"><p id="p1775122317363"><a name="p1775122317363"></a><a name="p1775122317363"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="49.49%" id="mcps1.2.5.1.4"><p id="p71791812113610"><a name="p71791812113610"></a><a name="p71791812113610"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row817971293614"><td class="cellrowborder" valign="top" width="19.36%" headers="mcps1.2.5.1.1 "><p id="p54426520364"><a name="p54426520364"></a><a name="p54426520364"></a>image</p>
</td>
<td class="cellrowborder" valign="top" width="13.469999999999999%" headers="mcps1.2.5.1.2 "><p id="p12442185213364"><a name="p12442185213364"></a><a name="p12442185213364"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="17.68%" headers="mcps1.2.5.1.3 "><p id="p16442195218369"><a name="p16442195218369"></a><a name="p16442195218369"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="49.49%" headers="mcps1.2.5.1.4 "><p id="p15444145213368"><a name="p15444145213368"></a><a name="p15444145213368"></a>Specifies the ECS image.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **image**  field description

<a name="table39016918211632"></a>
<table><thead align="left"><tr id="row31417811211632"><th class="cellrowborder" valign="top" width="19.36%" id="mcps1.2.5.1.1"><p id="p13501148211632"><a name="p13501148211632"></a><a name="p13501148211632"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13.530000000000001%" id="mcps1.2.5.1.2"><p id="p32752343211632"><a name="p32752343211632"></a><a name="p32752343211632"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="17.11%" id="mcps1.2.5.1.3"><p id="p47957996211632"><a name="p47957996211632"></a><a name="p47957996211632"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.5.1.4"><p id="p51666370211632"><a name="p51666370211632"></a><a name="p51666370211632"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row22126978211632"><td class="cellrowborder" valign="top" width="19.36%" headers="mcps1.2.5.1.1 "><p id="p24226259211632"><a name="p24226259211632"></a><a name="p24226259211632"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="13.530000000000001%" headers="mcps1.2.5.1.2 "><p id="p42610398211632"><a name="p42610398211632"></a><a name="p42610398211632"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.11%" headers="mcps1.2.5.1.3 "><p id="p27767370211632"><a name="p27767370211632"></a><a name="p27767370211632"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.5.1.4 "><p id="p57026368211632"><a name="p57026368211632"></a><a name="p57026368211632"></a>Specifies the ECS image ID.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section727655211632"></a>

None

## Example Request<a name="section47627159211632"></a>

```
POST https://{endpoint}/v1/{project_id}/cloudservers/fpga_image/{fpga_image_id}/association
```

```
{
  "image": {
    "id": "18efee75-e058-4c52-a49c-9e3ba4d1c8de"
  }
}
```

## Example Response<a name="section186865517285"></a>

None

## Returned Values<a name="section3477250491225"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

## Error Codes<a name="section85821649202813"></a>

See  [Error Code Description](error-code-description.md).


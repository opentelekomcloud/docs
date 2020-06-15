# Registering an FPGA Image<a name="EN-US_TOPIC_0065962597"></a>

## Function<a name="section6847204211311"></a>

This API is used to register an FPGA image.

An FPGA image, which is also called accelerated engine image \(AEI\), is a logic FPGA file developed by a user. During FPGA image registration, the logic file must be stored in the Object Storage Service \(OBS\) bucket of the user.

## URI<a name="section62251638211311"></a>

POST /v1/\{project\_id\}/cloudservers/fpga\_image

[Table 1](#table10080802211311)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table10080802211311"></a>
<table><thead align="left"><tr id="row23258692211311"><th class="cellrowborder" valign="top" width="16.97%" id="mcps1.2.4.1.1"><p id="p7707213"><a name="p7707213"></a><a name="p7707213"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.28%" id="mcps1.2.4.1.2"><p id="p20304554"><a name="p20304554"></a><a name="p20304554"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.75%" id="mcps1.2.4.1.3"><p id="p34056167"><a name="p34056167"></a><a name="p34056167"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row37402583211311"><td class="cellrowborder" valign="top" width="16.97%" headers="mcps1.2.4.1.1 "><p id="p54826436211311"><a name="p54826436211311"></a><a name="p54826436211311"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.28%" headers="mcps1.2.4.1.2 "><p id="p54905009211311"><a name="p54905009211311"></a><a name="p54905009211311"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.75%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section20272402211311"></a>

[Table 2](#table5698154011375)  describes the request parameters.

**Table  2**  Request parameters

<a name="table5698154011375"></a>
<table><thead align="left"><tr id="row18698940103719"><th class="cellrowborder" valign="top" width="16.848315168483154%" id="mcps1.2.5.1.1"><p id="p1569884093712"><a name="p1569884093712"></a><a name="p1569884093712"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13.138686131386859%" id="mcps1.2.5.1.2"><p id="p9699184073710"><a name="p9699184073710"></a><a name="p9699184073710"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="17.358264173582644%" id="mcps1.2.5.1.3"><p id="p1769974053715"><a name="p1769974053715"></a><a name="p1769974053715"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="52.654734526547344%" id="mcps1.2.5.1.4"><p id="p469974003711"><a name="p469974003711"></a><a name="p469974003711"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row769974019371"><td class="cellrowborder" valign="top" width="16.848315168483154%" headers="mcps1.2.5.1.1 "><p id="p1378615433718"><a name="p1378615433718"></a><a name="p1378615433718"></a>fpga_image</p>
</td>
<td class="cellrowborder" valign="top" width="13.138686131386859%" headers="mcps1.2.5.1.2 "><p id="p769911401374"><a name="p769911401374"></a><a name="p769911401374"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="17.358264173582644%" headers="mcps1.2.5.1.3 "><p id="p18699104011370"><a name="p18699104011370"></a><a name="p18699104011370"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="52.654734526547344%" headers="mcps1.2.5.1.4 "><p id="p19699134073719"><a name="p19699134073719"></a><a name="p19699134073719"></a>Indicates details about an FPGA image.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **fpga\_image**  field description

<a name="table36632723211311"></a>
<table><thead align="left"><tr id="row6485675211311"><th class="cellrowborder" valign="top" width="16.91%" id="mcps1.2.5.1.1"><p id="p22916806211311"><a name="p22916806211311"></a><a name="p22916806211311"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13.16%" id="mcps1.2.5.1.2"><p id="p58378163211311"><a name="p58378163211311"></a><a name="p58378163211311"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="17.29%" id="mcps1.2.5.1.3"><p id="p36640154211311"><a name="p36640154211311"></a><a name="p36640154211311"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="52.64%" id="mcps1.2.5.1.4"><p id="p58095138211311"><a name="p58095138211311"></a><a name="p58095138211311"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row55081076211311"><td class="cellrowborder" valign="top" width="16.91%" headers="mcps1.2.5.1.1 "><p id="p30311735211311"><a name="p30311735211311"></a><a name="p30311735211311"></a>location</p>
</td>
<td class="cellrowborder" valign="top" width="13.16%" headers="mcps1.2.5.1.2 "><p id="p25396884211311"><a name="p25396884211311"></a><a name="p25396884211311"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.2.5.1.3 "><p id="p65343538211311"><a name="p65343538211311"></a><a name="p65343538211311"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="52.64%" headers="mcps1.2.5.1.4 "><p id="p161527536573"><a name="p161527536573"></a><a name="p161527536573"></a>Specifies the OBS bucket path in which the logic FPGA file is stored. The format of the path is "Bucket name:File name", for example, "obs-fpga:fpga.bin".</p>
<p id="p1315225312576"><a name="p1315225312576"></a><a name="p1315225312576"></a>Bucket naming rules comply with the following OBS requirements:</p>
<a name="ul43426540194839"></a><a name="ul43426540194839"></a><ul id="ul43426540194839"><li>Consists of lowercase letters, digits, and special characters <span class="parmvalue" id="parmvalue492036462113233"><a name="parmvalue492036462113233"></a><a name="parmvalue492036462113233"></a><b>.</b></span> and <span class="parmvalue" id="parmvalue282040979113233"><a name="parmvalue282040979113233"></a><a name="parmvalue282040979113233"></a><b>-</b></span>.</li><li>Must start and end with a digit or letter.</li><li>Contains 3 to 63 characters.</li><li>Cannot be an IP address.</li><li>Cannot contain <span class="parmvalue" id="parmvalue634589654113359"><a name="parmvalue634589654113359"></a><a name="parmvalue634589654113359"></a><b>..</b></span>, <span class="parmvalue" id="parmvalue449462891113359"><a name="parmvalue449462891113359"></a><a name="parmvalue449462891113359"></a><b>.-</b></span>, or <span class="parmvalue" id="parmvalue229886553113359"><a name="parmvalue229886553113359"></a><a name="parmvalue229886553113359"></a><b>-.</b></span>.</li></ul>
<p id="p13624699194711"><a name="p13624699194711"></a><a name="p13624699194711"></a>A file name must conform to the following rules:</p>
<a name="ul40992670194757"></a><a name="ul40992670194757"></a><ul id="ul40992670194757"><li>Consists of uppercase and lowercase letters, digits, hyphens (-), underscores (_), slashes (/), and periods (.).</li><li>Must end with <span class="parmvalue" id="parmvalue47163054611124"><a name="parmvalue47163054611124"></a><a name="parmvalue47163054611124"></a><b>.bin</b></span> or <span class="parmvalue" id="parmvalue153878766711127"><a name="parmvalue153878766711127"></a><a name="parmvalue153878766711127"></a><b>xclbin</b></span>.</li><li>Contains 4 to 64 characters.</li></ul>
</td>
</tr>
<tr id="row43174483211311"><td class="cellrowborder" valign="top" width="16.91%" headers="mcps1.2.5.1.1 "><p id="p11983269211311"><a name="p11983269211311"></a><a name="p11983269211311"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="13.16%" headers="mcps1.2.5.1.2 "><p id="p1310425211311"><a name="p1310425211311"></a><a name="p1310425211311"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.2.5.1.3 "><p id="p7009559211311"><a name="p7009559211311"></a><a name="p7009559211311"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="52.64%" headers="mcps1.2.5.1.4 "><p id="p5607686211311"><a name="p5607686211311"></a><a name="p5607686211311"></a>Specifies the name of the FPGA image.</p>
<p id="p52669702211311"><a name="p52669702211311"></a><a name="p52669702211311"></a>Value range:</p>
<a name="ul64450334162249"></a><a name="ul64450334162249"></a><ul id="ul64450334162249"><li>Contains only letters, digits, underscores, and hyphens.</li><li>Contains 1 to 64 characters.</li></ul>
</td>
</tr>
<tr id="row49437453114111"><td class="cellrowborder" valign="top" width="16.91%" headers="mcps1.2.5.1.1 "><p id="p32309183114120"><a name="p32309183114120"></a><a name="p32309183114120"></a>metadata</p>
</td>
<td class="cellrowborder" valign="top" width="13.16%" headers="mcps1.2.5.1.2 "><p id="p45454409114125"><a name="p45454409114125"></a><a name="p45454409114125"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.2.5.1.3 "><p id="p36703951114111"><a name="p36703951114111"></a><a name="p36703951114111"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="52.64%" headers="mcps1.2.5.1.4 "><p id="p37045433589"><a name="p37045433589"></a><a name="p37045433589"></a>Specifies the FPGA image metadata, which must be a valid JavaScript Object Notation (JSON) object.</p>
<p id="p770494355817"><a name="p770494355817"></a><a name="p770494355817"></a>The number of characters in metadata after JSON serialization cannot exceed 1024.</p>
</td>
</tr>
<tr id="row21013490211311"><td class="cellrowborder" valign="top" width="16.91%" headers="mcps1.2.5.1.1 "><p id="p63941444211311"><a name="p63941444211311"></a><a name="p63941444211311"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="13.16%" headers="mcps1.2.5.1.2 "><p id="p9176036211311"><a name="p9176036211311"></a><a name="p9176036211311"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="17.29%" headers="mcps1.2.5.1.3 "><p id="p53464121211311"><a name="p53464121211311"></a><a name="p53464121211311"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="52.64%" headers="mcps1.2.5.1.4 "><p id="p28403755211311"><a name="p28403755211311"></a><a name="p28403755211311"></a>Describes an FPGA image. The value consists of uppercase and lowercase letters, digits, hyphens (-), underscores (_), periods (.), commas, and spaces. The value consists of 0 to 255 characters.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="section55994659211311"></a>

[Table 4](#table551653634018)  describes the response parameters.

**Table  4**  Response parameters

<a name="table551653634018"></a>
<table><thead align="left"><tr id="row17516036104012"><th class="cellrowborder" valign="top" width="17.03%" id="mcps1.2.4.1.1"><p id="p75161336124015"><a name="p75161336124015"></a><a name="p75161336124015"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13.100000000000001%" id="mcps1.2.4.1.2"><p id="p14517136124013"><a name="p14517136124013"></a><a name="p14517136124013"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="69.87%" id="mcps1.2.4.1.3"><p id="p751711364402"><a name="p751711364402"></a><a name="p751711364402"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1551763664016"><td class="cellrowborder" valign="top" width="17.03%" headers="mcps1.2.4.1.1 "><p id="p8517103634019"><a name="p8517103634019"></a><a name="p8517103634019"></a>fpga_image</p>
</td>
<td class="cellrowborder" valign="top" width="13.100000000000001%" headers="mcps1.2.4.1.2 "><p id="p6517173604019"><a name="p6517173604019"></a><a name="p6517173604019"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="69.87%" headers="mcps1.2.4.1.3 "><p id="p1451793612400"><a name="p1451793612400"></a><a name="p1451793612400"></a>Indicates details about an FPGA image.</p>
</td>
</tr>
</tbody>
</table>

**Table  5** **fpga\_image**  field description

<a name="table8648200211311"></a>
<table><thead align="left"><tr id="row47349056211311"><th class="cellrowborder" valign="top" width="16.919999999999998%" id="mcps1.2.4.1.1"><p id="p15806308"><a name="p15806308"></a><a name="p15806308"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="13.16%" id="mcps1.2.4.1.2"><p id="p21995508"><a name="p21995508"></a><a name="p21995508"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="69.92%" id="mcps1.2.4.1.3"><p id="p36805753"><a name="p36805753"></a><a name="p36805753"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row64340933211311"><td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.4.1.1 "><p id="p32671333211311"><a name="p32671333211311"></a><a name="p32671333211311"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="13.16%" headers="mcps1.2.4.1.2 "><p id="p30640904211311"><a name="p30640904211311"></a><a name="p30640904211311"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="69.92%" headers="mcps1.2.4.1.3 "><p id="p51329136211311"><a name="p51329136211311"></a><a name="p51329136211311"></a>ID of an FPGA image</p>
</td>
</tr>
<tr id="row1620851211311"><td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.4.1.1 "><p id="p26004605211311"><a name="p26004605211311"></a><a name="p26004605211311"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="13.16%" headers="mcps1.2.4.1.2 "><p id="p64423181211311"><a name="p64423181211311"></a><a name="p64423181211311"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="69.92%" headers="mcps1.2.4.1.3 "><p id="p63235550211311"><a name="p63235550211311"></a><a name="p63235550211311"></a>Specifies the FPGA image status. Options:</p>
<a name="ul10437195973916"></a><a name="ul10437195973916"></a><ul id="ul10437195973916"><li><strong>saving</strong>: indicates that the FPGA image file is being uploaded to the backend storage.</li><li><strong id="b84235270615561"><a name="b84235270615561"></a><a name="b84235270615561"></a>deleting</strong>: indicates that the FPGA image is being deleted.</li><li><strong id="b842352706155622"><a name="b842352706155622"></a><a name="b842352706155622"></a>error</strong>: indicates that creating the FPGA image failed.</li><li><strong>active</strong>: indicates that the FPGA image is available for use.</li></ul>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="section11362753211311"></a>

```
POST https://{endpoint}/v1/{project_id}/cloudservers/fpga_image
```

```
{ 
  "fpga_image": { 
    "location": "obs-fpga:fpga.bin", 
    "name": "fpga-image-test", 
    "description": "fpga description", 
    "metadata": { 
      "shell_type": "OCL", 
      "shell_version": "1.0" 
    } 
  } 
}
```

## Example Response<a name="section7937164492610"></a>

```
{
  "fpga_image": {
    "status": "saving",
    "id": "4010a32c5c62bad9015c62dc2290002b"
  }
}
```

## Returned Values<a name="section3477250491225"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

## Error Codes<a name="section85821649202813"></a>

See  [Error Code Description](error-code-description.md).


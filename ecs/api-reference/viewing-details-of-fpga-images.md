# Viewing Details of FPGA Images<a name="EN-US_TOPIC_0065962600"></a>

## Function<a name="section48834480211756"></a>

This API is used to view the details of the FPGA images of a tenant.

## URI<a name="section30048492211756"></a>

GET /v1/\{project\_id\}/cloudservers/fpga\_image/detail\{?fpga\_image\_id,page,size\}

[Table 1](#table972014396283)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table972014396283"></a>
<table><thead align="left"><tr id="row18736639162810"><th class="cellrowborder" valign="top" width="16.98%" id="mcps1.2.4.1.1"><p id="p1873611398284"><a name="p1873611398284"></a><a name="p1873611398284"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.32%" id="mcps1.2.4.1.2"><p id="p13736113918287"><a name="p13736113918287"></a><a name="p13736113918287"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="65.7%" id="mcps1.2.4.1.3"><p id="p1736123982813"><a name="p1736123982813"></a><a name="p1736123982813"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row873613910283"><td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.1 "><p id="p127363398282"><a name="p127363398282"></a><a name="p127363398282"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.32%" headers="mcps1.2.4.1.2 "><p id="p1573653913281"><a name="p1573653913281"></a><a name="p1573653913281"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="65.7%" headers="mcps1.2.4.1.3 "><p id="p573610392287"><a name="p573610392287"></a><a name="p573610392287"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="row104351048202211"><td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.1 "><p id="p20435134810224"><a name="p20435134810224"></a><a name="p20435134810224"></a>fpga_image_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.32%" headers="mcps1.2.4.1.2 "><p id="p114361048162214"><a name="p114361048162214"></a><a name="p114361048162214"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="65.7%" headers="mcps1.2.4.1.3 "><p id="p134361248182213"><a name="p134361248182213"></a><a name="p134361248182213"></a>Specifies the FPGA image ID.</p>
</td>
</tr>
<tr id="row1273633912816"><td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.1 "><p id="p075111399287"><a name="p075111399287"></a><a name="p075111399287"></a>page</p>
</td>
<td class="cellrowborder" valign="top" width="17.32%" headers="mcps1.2.4.1.2 "><p id="p575113399286"><a name="p575113399286"></a><a name="p575113399286"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="65.7%" headers="mcps1.2.4.1.3 "><p id="p11751839102813"><a name="p11751839102813"></a><a name="p11751839102813"></a>Specifies the number of pages in a pagination query.</p>
<p id="p375133982819"><a name="p375133982819"></a><a name="p375133982819"></a>The value of this parameter must meet the following requirements:</p>
<a name="ul5751239142816"></a><a name="ul5751239142816"></a><ul id="ul5751239142816"><li>Must be a decimal integer.</li><li>Ranges from 1 (inclusive) to 65,535 (exclusive).</li><li>Cannot contain <span class="parmvalue" id="parmvalue1012157220123616"><a name="parmvalue1012157220123616"></a><a name="parmvalue1012157220123616"></a><b>+</b></span>.</li></ul>
</td>
</tr>
<tr id="row4751539122812"><td class="cellrowborder" valign="top" width="16.98%" headers="mcps1.2.4.1.1 "><p id="p375115393284"><a name="p375115393284"></a><a name="p375115393284"></a>size</p>
</td>
<td class="cellrowborder" valign="top" width="17.32%" headers="mcps1.2.4.1.2 "><p id="p2751639162811"><a name="p2751639162811"></a><a name="p2751639162811"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="65.7%" headers="mcps1.2.4.1.3 "><p id="p10751193912280"><a name="p10751193912280"></a><a name="p10751193912280"></a>Specifies the maximum records displayed on a page in a pagination query.</p>
<a name="ul137519397282"></a><a name="ul137519397282"></a><ul id="ul137519397282"><li>Must be a decimal integer.</li><li>Ranges from 1 (inclusive) to 100 (inclusive).</li><li>Cannot contain <span class="parmvalue" id="parmvalue1012157220123616_1"><a name="parmvalue1012157220123616_1"></a><a name="parmvalue1012157220123616_1"></a><b>+</b></span>.</li></ul>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>-   Pagination query takes effect only if parameters  **page**  and  **size**  both have a value. If only one of them has a value, an error message indicating invalid parameter will be displayed.  
>-   If  **fpga\_image\_id**  is used, pagination query specified by  **page**  and  **size**  does not take effect.  

## Request<a name="section8276847211756"></a>

None

## Response<a name="section1847981211756"></a>

[Table 2](#table41782128362)  describes the response parameters.

**Table  2**  Response parameters

<a name="table41782128362"></a>
<table><thead align="left"><tr id="row17178181253615"><th class="cellrowborder" valign="top" width="17.86%" id="mcps1.2.4.1.1"><p id="p3178612173615"><a name="p3178612173615"></a><a name="p3178612173615"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.899999999999999%" id="mcps1.2.4.1.2"><p id="p2017861210364"><a name="p2017861210364"></a><a name="p2017861210364"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="67.24%" id="mcps1.2.4.1.3"><p id="p71791812113610"><a name="p71791812113610"></a><a name="p71791812113610"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row19882155510223"><td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.2.4.1.1 "><p id="p17883135513226"><a name="p17883135513226"></a><a name="p17883135513226"></a>count</p>
</td>
<td class="cellrowborder" valign="top" width="14.899999999999999%" headers="mcps1.2.4.1.2 "><p id="p14248122614238"><a name="p14248122614238"></a><a name="p14248122614238"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="67.24%" headers="mcps1.2.4.1.3 "><p id="p1388355518227"><a name="p1388355518227"></a><a name="p1388355518227"></a>Specifies the number of FPGA images to be queried.</p>
</td>
</tr>
<tr id="row124863092316"><td class="cellrowborder" valign="top" width="17.86%" headers="mcps1.2.4.1.1 "><p id="p14435168240"><a name="p14435168240"></a><a name="p14435168240"></a>fpgaimages</p>
</td>
<td class="cellrowborder" valign="top" width="14.899999999999999%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972909_p28080649"><a name="en-us_topic_0057972909_p28080649"></a><a name="en-us_topic_0057972909_p28080649"></a>Array of objects</p>
</td>
<td class="cellrowborder" valign="top" width="67.24%" headers="mcps1.2.4.1.3 "><p id="p748690112311"><a name="p748690112311"></a><a name="p748690112311"></a>Specifies details of FPGA images.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **fpgaimages**  field description

<a name="table41296006211756"></a>
<table><thead align="left"><tr id="row1990984211756"><th class="cellrowborder" valign="top" width="17.919999999999998%" id="mcps1.2.4.1.1"><p id="p15806308"><a name="p15806308"></a><a name="p15806308"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="14.719999999999999%" id="mcps1.2.4.1.2"><p id="p21995508"><a name="p21995508"></a><a name="p21995508"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="67.36%" id="mcps1.2.4.1.3"><p id="p36805753"><a name="p36805753"></a><a name="p36805753"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row43619055211756"><td class="cellrowborder" valign="top" width="17.919999999999998%" headers="mcps1.2.4.1.1 "><p id="p17102613211756"><a name="p17102613211756"></a><a name="p17102613211756"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="14.719999999999999%" headers="mcps1.2.4.1.2 "><p id="p50695788211756"><a name="p50695788211756"></a><a name="p50695788211756"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67.36%" headers="mcps1.2.4.1.3 "><p id="p49395919211756"><a name="p49395919211756"></a><a name="p49395919211756"></a>Specifies the FPGA image ID.</p>
</td>
</tr>
<tr id="row41382846211756"><td class="cellrowborder" valign="top" width="17.919999999999998%" headers="mcps1.2.4.1.1 "><p id="p14594565211756"><a name="p14594565211756"></a><a name="p14594565211756"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="14.719999999999999%" headers="mcps1.2.4.1.2 "><p id="p60068226211756"><a name="p60068226211756"></a><a name="p60068226211756"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67.36%" headers="mcps1.2.4.1.3 "><p id="p24580412211756"><a name="p24580412211756"></a><a name="p24580412211756"></a>Specifies the FPGA image name.</p>
</td>
</tr>
<tr id="row2706776211756"><td class="cellrowborder" valign="top" width="17.919999999999998%" headers="mcps1.2.4.1.1 "><p id="p12159451211756"><a name="p12159451211756"></a><a name="p12159451211756"></a>description</p>
</td>
<td class="cellrowborder" valign="top" width="14.719999999999999%" headers="mcps1.2.4.1.2 "><p id="p31907576211756"><a name="p31907576211756"></a><a name="p31907576211756"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67.36%" headers="mcps1.2.4.1.3 "><p id="p30372637211756"><a name="p30372637211756"></a><a name="p30372637211756"></a>Describes the FPGA image.</p>
</td>
</tr>
<tr id="row16501990211756"><td class="cellrowborder" valign="top" width="17.919999999999998%" headers="mcps1.2.4.1.1 "><p id="p16482479211756"><a name="p16482479211756"></a><a name="p16482479211756"></a>status</p>
</td>
<td class="cellrowborder" valign="top" width="14.719999999999999%" headers="mcps1.2.4.1.2 "><p id="p29509334211756"><a name="p29509334211756"></a><a name="p29509334211756"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67.36%" headers="mcps1.2.4.1.3 "><p id="p63235550211311"><a name="p63235550211311"></a><a name="p63235550211311"></a>Specifies the FPGA image status. Options:</p>
<a name="ul10437195973916"></a><a name="ul10437195973916"></a><ul id="ul10437195973916"><li><strong id="b842352706155750"><a name="b842352706155750"></a><a name="b842352706155750"></a>initialling</strong>: indicates that the task of creating an FPGA image is being initialized.</li><li><strong id="b84235270615593"><a name="b84235270615593"></a><a name="b84235270615593"></a>scheduling</strong>: indicates that the task of creating an FPGA image is waiting for scheduling.</li><li><strong id="b84235270615561"><a name="b84235270615561"></a><a name="b84235270615561"></a>creating</strong>: indicates that the FPGA image is being created.</li><li><strong>saving</strong>: indicates that the FPGA image file is being uploaded to the backend storage.</li><li><strong id="b84235270615561_1"><a name="b84235270615561_1"></a><a name="b84235270615561_1"></a>deleting</strong>: indicates that the FPGA image is being deleted.</li><li><strong id="b842352706155622"><a name="b842352706155622"></a><a name="b842352706155622"></a>error</strong>: indicates that creating the FPGA image failed.</li><li><strong>active</strong>: indicates that the FPGA image is available for use.</li></ul>
</td>
</tr>
<tr id="row23208874211756"><td class="cellrowborder" valign="top" width="17.919999999999998%" headers="mcps1.2.4.1.1 "><p id="p50294579211756"><a name="p50294579211756"></a><a name="p50294579211756"></a>size</p>
</td>
<td class="cellrowborder" valign="top" width="14.719999999999999%" headers="mcps1.2.4.1.2 "><p id="p55007805211756"><a name="p55007805211756"></a><a name="p55007805211756"></a>Integer</p>
</td>
<td class="cellrowborder" valign="top" width="67.36%" headers="mcps1.2.4.1.3 "><p id="p40832246211756"><a name="p40832246211756"></a><a name="p40832246211756"></a>Specifies the size (MB) of the FPGA image file.</p>
</td>
</tr>
<tr id="row6209341211756"><td class="cellrowborder" valign="top" width="17.919999999999998%" headers="mcps1.2.4.1.1 "><p id="p63772911211756"><a name="p63772911211756"></a><a name="p63772911211756"></a>createdAt</p>
</td>
<td class="cellrowborder" valign="top" width="14.719999999999999%" headers="mcps1.2.4.1.2 "><p id="p23403431211756"><a name="p23403431211756"></a><a name="p23403431211756"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67.36%" headers="mcps1.2.4.1.3 "><p id="p7571123314012"><a name="p7571123314012"></a><a name="p7571123314012"></a>Specifies the time when the FPGA image was created.</p>
<p id="p48706887211756"><a name="p48706887211756"></a><a name="p48706887211756"></a>Coordinated Universal Time (UTC) time is used.</p>
</td>
</tr>
<tr id="row3069902211756"><td class="cellrowborder" valign="top" width="17.919999999999998%" headers="mcps1.2.4.1.1 "><p id="p56866436211756"><a name="p56866436211756"></a><a name="p56866436211756"></a>protected</p>
</td>
<td class="cellrowborder" valign="top" width="14.719999999999999%" headers="mcps1.2.4.1.2 "><p id="p14992676211756"><a name="p14992676211756"></a><a name="p14992676211756"></a>Boolean</p>
</td>
<td class="cellrowborder" valign="top" width="67.36%" headers="mcps1.2.4.1.3 "><p id="p10022464211756"><a name="p10022464211756"></a><a name="p10022464211756"></a>Specifies whether an FPGA image is protected.</p>
<p id="p11704713203339"><a name="p11704713203339"></a><a name="p11704713203339"></a>If an FPGA image is protected, it is associated with an image used to create ECSs and cannot be deleted.</p>
</td>
</tr>
<tr id="row57042024211756"><td class="cellrowborder" valign="top" width="17.919999999999998%" headers="mcps1.2.4.1.1 "><p id="p31688172211756"><a name="p31688172211756"></a><a name="p31688172211756"></a>message</p>
</td>
<td class="cellrowborder" valign="top" width="14.719999999999999%" headers="mcps1.2.4.1.2 "><p id="p34157725211756"><a name="p34157725211756"></a><a name="p34157725211756"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67.36%" headers="mcps1.2.4.1.3 "><p id="p12786151213735"><a name="p12786151213735"></a><a name="p12786151213735"></a>Specifies the FPGA image supplementation.</p>
</td>
</tr>
<tr id="row9124165114747"><td class="cellrowborder" valign="top" width="17.919999999999998%" headers="mcps1.2.4.1.1 "><p id="p859913114747"><a name="p859913114747"></a><a name="p859913114747"></a>metadata</p>
</td>
<td class="cellrowborder" valign="top" width="14.719999999999999%" headers="mcps1.2.4.1.2 "><p id="p17931171520319"><a name="p17931171520319"></a><a name="p17931171520319"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="67.36%" headers="mcps1.2.4.1.3 "><p id="p29151897114957"><a name="p29151897114957"></a><a name="p29151897114957"></a>Specifies the FPGA image metadata.</p>
</td>
</tr>
<tr id="row1599674922420"><td class="cellrowborder" valign="top" width="17.919999999999998%" headers="mcps1.2.4.1.1 "><p id="p179961449132417"><a name="p179961449132417"></a><a name="p179961449132417"></a>log_directory</p>
</td>
<td class="cellrowborder" valign="top" width="14.719999999999999%" headers="mcps1.2.4.1.2 "><p id="p0996649122411"><a name="p0996649122411"></a><a name="p0996649122411"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="67.36%" headers="mcps1.2.4.1.3 "><p id="p59961849152415"><a name="p59961849152415"></a><a name="p59961849152415"></a>Specifies the directory, in the format of "Bucket name:Directory", in which the log file for constructing the FPGA image is stored in OBS, for example, "obs-fpga:vu9p/log".</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="section10567103352712"></a>

```
GET https://{endpoint}/v1/{project_id}/cloudservers/fpga_image/detail
```

## Example Response<a name="section31303547211756"></a>

```
{ 
  "count": 2, 
  "fpgaimages": [ 
    { 
      "id": "4010a32c5c7d7711015c81ac714c009d", 
      "name": "FPGA001", 
      "description": "fpga test", 
      "status": "active", 
      "size": 40, 
      "createdAt": "2017-06-07 08:29:41", 
      "protected": false, 
      "message": null, 
      "metadata": { 
        "shell_type": "OCL", 
        "shell_version": "1.0" 
      },
      "log_directory": "obs-fpga:vu9p/log"
    }, 
    { 
      "id": "4010a32c5c7d7711015c813e69bd002c", 
      "name": "FPGA002", 
      "description": "fpga test", 
      "status": "active", 
      "size": 43, 
      "createdAt": "2017-06-07 16:29:30", 
      "protected": true, 
      "message": null,
      "metadata": { 
        "shell_type": "OCL", 
        "shell_version": "1.0" 
      },
      "log_directory": "obs-fpga:vu9p/log"
    } 
  ] 
}
```

## Returned Values<a name="section3477250491225"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).

## Error Codes<a name="section85821649202813"></a>

See  [Error Code Description](error-code-description.md).


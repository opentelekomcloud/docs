# Creating an Image Using an ECS<a name="EN-US_TOPIC_0065817694"></a>

## Function<a name="en-us_topic_0057972976_section52906670"></a>

This API is used to create an image using an ECS. After the creation, you can use this image to create ECSs.

Images created using ECSs are stored on storage nodes as snapshots.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>This API is a native OpenStack API that is not applicable to the images on the public cloud platform.  
>-   To create a system disk image or data disk image, use the IMS API \(**POST /v2/cloudimages/action**\). For details, see "Creating an Image" in  _Image Management Service API Reference_.  
>-   To create a full-ECS image, use the IMS API \(**POST /v1/cloudimages/wholeimages/action**\). For details, see "Creating a Full-ECS Image" in  _Image Management Service API Reference_.  

## Constraints<a name="en-us_topic_0057972976_section57581898"></a>

1.  ECSs in error state cannot be used to create images.
2.  If an image created using an ECS is used to create a new ECS, the new ECS must be located in the same AZ as the original ECS.
3.  After an ECS is deleted, the images and snapshots created using this ECS will not be automatically deleted. You must manually delete them.
4.  After an image created using an ECS is deleted, the associated snapshots will not be automatically deleted \(this function is implemented by native OpenStack\). You must manually delete such snapshots.
5.  The image created using an ECS cannot be used to create data disks.
6.  The images created using the API described in this section \(URI: POST /v2/\{project\_id\}/servers/\{server\_id\}/action or POST /v2.1/\{project\_id\}/servers/\{server\_id\}/action\) cannot be exported to OBS buckets. If such images must be exported, use the IMS API \(**POST  /v2/cloudimages/action**\). For details, see "Creating an Image" in  _Image Management Service API Reference_.

## URI<a name="en-us_topic_0057972976_section6397988"></a>

POST /v2/\{project\_id\}/servers/\{server\_id\}/action

POST /v2.1/\{project\_id\}/servers/\{server\_id\}/action

[Table 1](#en-us_topic_0057972976_en-us_topic_0020212650_table62669527)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="en-us_topic_0057972976_en-us_topic_0020212650_table62669527"></a>
<table><thead align="left"><tr id="en-us_topic_0057972976_en-us_topic_0020212650_row33894570"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.4.1.1"><p id="p5187119"><a name="p5187119"></a><a name="p5187119"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.4.1.2"><p id="p17503500"><a name="p17503500"></a><a name="p17503500"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="66%" id="mcps1.2.4.1.3"><p id="p8497414"><a name="p8497414"></a><a name="p8497414"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972976_en-us_topic_0020212650_row8419032"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972976_en-us_topic_0020212650_p10852974"><a name="en-us_topic_0057972976_en-us_topic_0020212650_p10852974"></a><a name="en-us_topic_0057972976_en-us_topic_0020212650_p10852974"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972976_en-us_topic_0020212650_p6675738"><a name="en-us_topic_0057972976_en-us_topic_0020212650_p6675738"></a><a name="en-us_topic_0057972976_en-us_topic_0020212650_p6675738"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.4.1.3 "><p id="p37593705"><a name="p37593705"></a><a name="p37593705"></a>Specifies the project ID.</p>
</td>
</tr>
<tr id="en-us_topic_0057972976_en-us_topic_0020212650_row34774863"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0057972976_en-us_topic_0020212650_p65300541"><a name="en-us_topic_0057972976_en-us_topic_0020212650_p65300541"></a><a name="en-us_topic_0057972976_en-us_topic_0020212650_p65300541"></a>server_id</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0057972976_en-us_topic_0020212650_p54852443"><a name="en-us_topic_0057972976_en-us_topic_0020212650_p54852443"></a><a name="en-us_topic_0057972976_en-us_topic_0020212650_p54852443"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0057972976_en-us_topic_0020212650_p13862865"><a name="en-us_topic_0057972976_en-us_topic_0020212650_p13862865"></a><a name="en-us_topic_0057972976_en-us_topic_0020212650_p13862865"></a>Specifies the ECS ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="en-us_topic_0057972976_section33622195"></a>

[Table 2](#en-us_topic_0057972976_table26141647)  describes the request parameters.

**Table  2**  Request parameter

<a name="en-us_topic_0057972976_table26141647"></a>
<table><thead align="left"><tr id="en-us_topic_0057972976_row26305715"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="en-us_topic_0057972976_p50388198"><a name="en-us_topic_0057972976_p50388198"></a><a name="en-us_topic_0057972976_p50388198"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.2"><p id="p984417238195"><a name="p984417238195"></a><a name="p984417238195"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="en-us_topic_0057972976_p54912217"><a name="en-us_topic_0057972976_p54912217"></a><a name="en-us_topic_0057972976_p54912217"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="52%" id="mcps1.2.5.1.4"><p id="en-us_topic_0057972976_p38674720"><a name="en-us_topic_0057972976_p38674720"></a><a name="en-us_topic_0057972976_p38674720"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972976_row45644612"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972976_p6226121"><a name="en-us_topic_0057972976_p6226121"></a><a name="en-us_topic_0057972976_p6226121"></a>createImage</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p168443237193"><a name="p168443237193"></a><a name="p168443237193"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972976_p34553815"><a name="en-us_topic_0057972976_p34553815"></a><a name="en-us_topic_0057972976_p34553815"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972976_p13838763"><a name="en-us_topic_0057972976_p13838763"></a><a name="en-us_topic_0057972976_p13838763"></a>Creates an image using an ECS.</p>
</td>
</tr>
</tbody>
</table>

**Table  3** **createImage**  field description

<a name="en-us_topic_0057972976_table47198018"></a>
<table><thead align="left"><tr id="en-us_topic_0057972976_row23638763"><th class="cellrowborder" valign="top" width="17.171717171717173%" id="mcps1.2.5.1.1"><p id="en-us_topic_0057972976_p35691611"><a name="en-us_topic_0057972976_p35691611"></a><a name="en-us_topic_0057972976_p35691611"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.171717171717173%" id="mcps1.2.5.1.2"><p id="en-us_topic_0057972976_p29834312"><a name="en-us_topic_0057972976_p29834312"></a><a name="en-us_topic_0057972976_p29834312"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.141414141414144%" id="mcps1.2.5.1.3"><p id="en-us_topic_0057972976_p5339351"><a name="en-us_topic_0057972976_p5339351"></a><a name="en-us_topic_0057972976_p5339351"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.515151515151516%" id="mcps1.2.5.1.4"><p id="en-us_topic_0057972976_p660246"><a name="en-us_topic_0057972976_p660246"></a><a name="en-us_topic_0057972976_p660246"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0057972976_row53479976"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972976_p36910823"><a name="en-us_topic_0057972976_p36910823"></a><a name="en-us_topic_0057972976_p36910823"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057972976_p43131274"><a name="en-us_topic_0057972976_p43131274"></a><a name="en-us_topic_0057972976_p43131274"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972976_p36986682"><a name="en-us_topic_0057972976_p36986682"></a><a name="en-us_topic_0057972976_p36986682"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972976_p3972286"><a name="en-us_topic_0057972976_p3972286"></a><a name="en-us_topic_0057972976_p3972286"></a>Specifies the image name with a length greater than 0 bytes and less than 243 bytes.</p>
</td>
</tr>
<tr id="en-us_topic_0057972976_row35750577"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0057972976_p10115639"><a name="en-us_topic_0057972976_p10115639"></a><a name="en-us_topic_0057972976_p10115639"></a>metadata</p>
</td>
<td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0057972976_p65153652"><a name="en-us_topic_0057972976_p65153652"></a><a name="en-us_topic_0057972976_p65153652"></a>No</p>
</td>
<td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0057972976_p14060437"><a name="en-us_topic_0057972976_p14060437"></a><a name="en-us_topic_0057972976_p14060437"></a>Object</p>
</td>
<td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0057972976_p42954492"><a name="en-us_topic_0057972976_p42954492"></a><a name="en-us_topic_0057972976_p42954492"></a>Specifies the image attribute with a length greater than 0 bytes and less than 255 bytes.</p>
</td>
</tr>
</tbody>
</table>

## Response<a name="en-us_topic_0057972976_section34164304"></a>

<a name="table194321619184818"></a>
<table><thead align="left"><tr id="row944991954814"><th class="cellrowborder" valign="top" width="17.171717171717173%" id="mcps1.1.5.1.1"><p id="p19449719184818"><a name="p19449719184818"></a><a name="p19449719184818"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="17.171717171717173%" id="mcps1.1.5.1.2"><p id="p544961994813"><a name="p544961994813"></a><a name="p544961994813"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="14.141414141414144%" id="mcps1.1.5.1.3"><p id="p1144918191483"><a name="p1144918191483"></a><a name="p1144918191483"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="51.515151515151516%" id="mcps1.1.5.1.4"><p id="p15449161954819"><a name="p15449161954819"></a><a name="p15449161954819"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row2449141911489"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.1.5.1.1 "><p id="p54499190480"><a name="p54499190480"></a><a name="p54499190480"></a>Location</p>
</td>
<td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.1.5.1.2 "><p id="p144491919134811"><a name="p144491919134811"></a><a name="p144491919134811"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.1.5.1.3 "><p id="p1644961924815"><a name="p1644961924815"></a><a name="p1644961924815"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.1.5.1.4 "><p id="p4449819124813"><a name="p4449819124813"></a><a name="p4449819124813"></a>Specifies the local URL of the image, which is returned in the request header.</p>
<p id="p179991156134920"><a name="p179991156134920"></a><a name="p179991156134920"></a>This field is not supported in microversions later than 2.44.</p>
</td>
</tr>
<tr id="row244981920485"><td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.1.5.1.1 "><p id="p2464141924819"><a name="p2464141924819"></a><a name="p2464141924819"></a>image_id</p>
</td>
<td class="cellrowborder" valign="top" width="17.171717171717173%" headers="mcps1.1.5.1.2 "><p id="p104641819174818"><a name="p104641819174818"></a><a name="p104641819174818"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.1.5.1.3 "><p id="p194647198489"><a name="p194647198489"></a><a name="p194647198489"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="51.515151515151516%" headers="mcps1.1.5.1.4 "><p id="p746418198488"><a name="p746418198488"></a><a name="p746418198488"></a>Specifies the image UUID.</p>
<p id="p1353146174918"><a name="p1353146174918"></a><a name="p1353146174918"></a>This field is supported in microversion 2.45.</p>
</td>
</tr>
</tbody>
</table>

## Example Request<a name="en-us_topic_0057972976_section39043280"></a>

```
POST https://{endpoint}/v2/{project_id}/servers/{server_id}/action
POST https://{endpoint}/v2.1/{project_id}/servers/{server_id}/action
```

```
{
   "createImage" : {
        "name" : "new-image-name",
        "metadata": {
            "ImageType": "Gold",
            "ImageVersion": "2.0"
        }
    }
}
```

## Example Response<a name="section10810185715811"></a>

None

## Returned Values<a name="en-us_topic_0057972976_section128741313191616"></a>

See  [Returned Values for General Requests](returned-values-for-general-requests.md).


# Uploading an Image \(Native OpenStack API\)<a name="EN-US_TOPIC_0031615566"></a>

## Function<a name="section11046056154747"></a>

This API is used to upload a local image to the cloud platform. The image to be uploaded must be smaller than 128 GB.

For more information about how to use external files to create images, see sections "Creating a Private Windows Image Using an External Image File" and "Creating a Private Linux Image Using an External Image File" in  _Image Management Service User Guide_.

The following describes how to use this API:

1.  Prepare the image to be uploaded. The image can be in QCOW2, VMDK, VHD, RAW, VHDX, QED, VDI, QCOW, ZVHD2, or ZVHD format.
2.  <a name="li57474254155728"></a>Create metadata for the image by performing the operations in  [Creating Image Metadata \(Native OpenStack API\)](creating-image-metadata-(native-openstack-api).md). After the API is invoked successfully, save the image ID.
3.  Upload the image file with the image ID obtained in  [2](#li57474254155728).

## URI<a name="section66620681154747"></a>

PUT /v2/images/\{image\_id\}/file

[Table 1](#table23910047154747)  lists the parameters in the URI.

**Table  1**  Parameter description

<a name="table23910047154747"></a>
<table><thead align="left"><tr id="row24965460154747"><th class="cellrowborder" valign="top" width="19.919999999999998%" id="mcps1.2.5.1.1"><p id="p8936346154747"><a name="p8936346154747"></a><a name="p8936346154747"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="19.919999999999998%" id="mcps1.2.5.1.2"><p id="p4072498116916"><a name="p4072498116916"></a><a name="p4072498116916"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="18.98%" id="mcps1.2.5.1.3"><p id="p52755425154747"><a name="p52755425154747"></a><a name="p52755425154747"></a><strong id="b5086748204848"><a name="b5086748204848"></a><a name="b5086748204848"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="41.18%" id="mcps1.2.5.1.4"><p id="p57477321154747"><a name="p57477321154747"></a><a name="p57477321154747"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row25151394154747"><td class="cellrowborder" valign="top" width="19.919999999999998%" headers="mcps1.2.5.1.1 "><p id="p23996995154747"><a name="p23996995154747"></a><a name="p23996995154747"></a>image_id</p>
</td>
<td class="cellrowborder" valign="top" width="19.919999999999998%" headers="mcps1.2.5.1.2 "><p id="p1038913616916"><a name="p1038913616916"></a><a name="p1038913616916"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.98%" headers="mcps1.2.5.1.3 "><p id="p64708437154747"><a name="p64708437154747"></a><a name="p64708437154747"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="41.18%" headers="mcps1.2.5.1.4 "><p id="p54354750154747"><a name="p54354750154747"></a><a name="p54354750154747"></a>Specifies the image ID.</p>
<a name="ul2091361694"></a><a name="ul2091361694"></a><ul id="ul2091361694"><li><strong id="b842352706151612"><a name="b842352706151612"></a><a name="b842352706151612"></a>image_id</strong> is the ID of the image you created by invoking the API for creating image metadata. Image upload may fail if you use other image IDs.</li><li>After this API is invoked, you can check the image status with the image ID. When the image status changes to <strong id="b842352706152426"><a name="b842352706152426"></a><a name="b842352706152426"></a>active</strong>, the image is uploaded successfully.</li></ul>
</td>
</tr>
</tbody>
</table>

## Request<a name="section29704853154747"></a>

-   Request parameters

    None

-   Example request

    ```
    PUT https://{Endpoint}/v2/images/84ac7f2b-bf19-4efb-86a0-b5be8771b476/file
    ```

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If you use the curl command to call the API, the example request is as follows:  
    >```  
    >curl -i --insecure 'https://IP/v2/images/84ac7f2b-bf19-4efb-86a0-b5be8771b476/file' -X PUT -H "X-Auth-Token: $mytoken" -H "Content-Type:application/octet-stream" -T /mnt/userdisk/images/suse.zvhd  
    >```  


## Response<a name="section42338041154747"></a>

-   Response parameters

    None

-   Example response

    ```
    HTTP/1.1 204
    ```


## Returned Values<a name="section61463701154747"></a>

-   Normal

    204

-   Abnormal

    <a name="table61689654164325"></a>
    <table><thead align="left"><tr id="row43263384164325"><th class="cellrowborder" valign="top" width="38.080000000000005%" id="mcps1.1.3.1.1"><p id="p14673233164325"><a name="p14673233164325"></a><a name="p14673233164325"></a><strong id="b52350906161544"><a name="b52350906161544"></a><a name="b52350906161544"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="61.919999999999995%" id="mcps1.1.3.1.2"><p id="p47681194164325"><a name="p47681194164325"></a><a name="p47681194164325"></a><strong id="b53324949161548"><a name="b53324949161548"></a><a name="b53324949161548"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row36971467164325"><td class="cellrowborder" valign="top" width="38.080000000000005%" headers="mcps1.1.3.1.1 "><p id="p41898845164325"><a name="p41898845164325"></a><a name="p41898845164325"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.919999999999995%" headers="mcps1.1.3.1.2 "><p id="p38363271164325"><a name="p38363271164325"></a><a name="p38363271164325"></a>Request error. For details, see <a href="error-codes.md">Error Codes</a>.</p>
    </td>
    </tr>
    <tr id="row20417266164325"><td class="cellrowborder" valign="top" width="38.080000000000005%" headers="mcps1.1.3.1.1 "><p id="p43185862164325"><a name="p43185862164325"></a><a name="p43185862164325"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.919999999999995%" headers="mcps1.1.3.1.2 "><p id="p8393897164325"><a name="p8393897164325"></a><a name="p8393897164325"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row8436217164325"><td class="cellrowborder" valign="top" width="38.080000000000005%" headers="mcps1.1.3.1.1 "><p id="p12244985164325"><a name="p12244985164325"></a><a name="p12244985164325"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.919999999999995%" headers="mcps1.1.3.1.2 "><p id="p52319709164325"><a name="p52319709164325"></a><a name="p52319709164325"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="row1115336164325"><td class="cellrowborder" valign="top" width="38.080000000000005%" headers="mcps1.1.3.1.1 "><p id="p23233406164325"><a name="p23233406164325"></a><a name="p23233406164325"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.919999999999995%" headers="mcps1.1.3.1.2 "><p id="p2857740164325"><a name="p2857740164325"></a><a name="p2857740164325"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="row33911260174644"><td class="cellrowborder" valign="top" width="38.080000000000005%" headers="mcps1.1.3.1.1 "><p id="p33585825174654"><a name="p33585825174654"></a><a name="p33585825174654"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.919999999999995%" headers="mcps1.1.3.1.2 "><p id="p36097324174654"><a name="p36097324174654"></a><a name="p36097324174654"></a>Request conflict.</p>
    </td>
    </tr>
    <tr id="row60371567174640"><td class="cellrowborder" valign="top" width="38.080000000000005%" headers="mcps1.1.3.1.1 "><p id="p8274976174654"><a name="p8274976174654"></a><a name="p8274976174654"></a>500 System Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.919999999999995%" headers="mcps1.1.3.1.2 "><p id="p66293315174654"><a name="p66293315174654"></a><a name="p66293315174654"></a>System error.</p>
    </td>
    </tr>
    </tbody>
    </table>



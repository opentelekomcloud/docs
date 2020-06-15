# Registering an Image<a name="EN-US_TOPIC_0037131984"></a>

## Function<a name="section11046056154747"></a>

This API is used to register an image file as an uninitialized private image on the cloud platform.

The following describes how to use this API:

1.  Upload the image file to an OBS bucket. For details, see "Object Storage Service User Guide".
2.  <a name="li40093194"></a>Use the image metadata creation API to create image metadata. After the API is invoked successfully, save the image ID. For how to create image metadata, see  [Creating Image Metadata \(Native OpenStack API\)](creating-image-metadata-(native-openstack-api).md).
3.  Use the API for registering images and the image ID obtained in  [2](#li40093194)  to register the image file as a private image.
4.  After the API is successfully invoked as an asynchronous one, the cloud service system receives a request. Query the image status using the image ID and check whether the image file is successfully registered. When the image status changes to  **active**, the image file is successfully registered as a private image.

    For details about how to query the status of an asynchronous task, see  [Asynchronous Job Query](asynchronous-job-query.md).


>![](/images/icon-note.gif) **NOTE:**   
>Before registering an image file, ensure that you have the Tenant Administrator permission of OBS.  

## URI<a name="section66620681154747"></a>

PUT /v1/cloudimages/\{image\_id\}/upload

[Table 1](#table23910047154747)  lists the parameters in the URI.

**Table  1**  Parameter description

<a name="table23910047154747"></a>
<table><thead align="left"><tr id="row24965460154747"><th class="cellrowborder" valign="top" width="19.168083191680832%" id="mcps1.2.5.1.1"><p id="p8936346154747"><a name="p8936346154747"></a><a name="p8936346154747"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="22.17778222177782%" id="mcps1.2.5.1.2"><p id="p4072498116916"><a name="p4072498116916"></a><a name="p4072498116916"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="18.228177182281772%" id="mcps1.2.5.1.3"><p id="p52755425154747"><a name="p52755425154747"></a><a name="p52755425154747"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="40.42595740425957%" id="mcps1.2.5.1.4"><p id="p57477321154747"><a name="p57477321154747"></a><a name="p57477321154747"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row25151394154747"><td class="cellrowborder" valign="top" width="19.168083191680832%" headers="mcps1.2.5.1.1 "><p id="p23996995154747"><a name="p23996995154747"></a><a name="p23996995154747"></a>image_id</p>
</td>
<td class="cellrowborder" valign="top" width="22.17778222177782%" headers="mcps1.2.5.1.2 "><p id="p1038913616916"><a name="p1038913616916"></a><a name="p1038913616916"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="18.228177182281772%" headers="mcps1.2.5.1.3 "><p id="p64708437154747"><a name="p64708437154747"></a><a name="p64708437154747"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="40.42595740425957%" headers="mcps1.2.5.1.4 "><p id="p54354750154747"><a name="p54354750154747"></a><a name="p54354750154747"></a>Specifies the image ID.</p>
<a name="ul2091361694"></a><a name="ul2091361694"></a><ul id="ul2091361694"><li><strong id="b842352706151612"><a name="b842352706151612"></a><a name="b842352706151612"></a>image_id</strong> is the ID of the image you created by invoking the API for creating image metadata. Registration may fail if you use other image IDs.</li><li>After this API is invoked, you can check the image status with the image ID. When the image status changes to <strong id="b2087357550"><a name="b2087357550"></a><a name="b2087357550"></a>active</strong>, the image file is successfully registered. For details, see <a href="querying-image-details-(native-openstack-api).md">Querying Image Details (Native OpenStack API)</a>.</li></ul>
</td>
</tr>
</tbody>
</table>

## Request<a name="section29704853154747"></a>

-   Request parameters

    <a name="table57282886154747"></a>
    <table><thead align="left"><tr id="row33194661154747"><th class="cellrowborder" valign="top" width="20.95%" id="mcps1.1.5.1.1"><p id="p4413036154747"><a name="p4413036154747"></a><a name="p4413036154747"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.75%" id="mcps1.1.5.1.2"><p id="p15244109154747"><a name="p15244109154747"></a><a name="p15244109154747"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.830000000000002%" id="mcps1.1.5.1.3"><p id="p4364817210345"><a name="p4364817210345"></a><a name="p4364817210345"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="41.47%" id="mcps1.1.5.1.4"><p id="p26813302154747"><a name="p26813302154747"></a><a name="p26813302154747"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row24393852154747"><td class="cellrowborder" valign="top" width="20.95%" headers="mcps1.1.5.1.1 "><p id="p29744966154747"><a name="p29744966154747"></a><a name="p29744966154747"></a>image_url</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.75%" headers="mcps1.1.5.1.2 "><p id="p384719154747"><a name="p384719154747"></a><a name="p384719154747"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.830000000000002%" headers="mcps1.1.5.1.3 "><p id="p2213925010345"><a name="p2213925010345"></a><a name="p2213925010345"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.47%" headers="mcps1.1.5.1.4 "><p id="p31162299154747"><a name="p31162299154747"></a><a name="p31162299154747"></a>Specifies the URL of the image file in the format of <em id="i84235269795423"><a name="i84235269795423"></a><a name="i84235269795423"></a>Bucket name</em>:<em id="i84235269795427"><a name="i84235269795427"></a><a name="i84235269795427"></a>File name</em>.</p>
    <p id="p129047121673"><a name="p129047121673"></a><a name="p129047121673"></a>Image files in the bucket can be in ZVHD, QCOW2, VHD, RAW, VHDX, QED, VDI, QCOW, ZVHD2, or VMDK format.</p>
    <div class="notice" id="note24311794102659"><a name="note24311794102659"></a><a name="note24311794102659"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><p id="p17479562102659"><a name="p17479562102659"></a><a name="p17479562102659"></a>The storage class of the OBS bucket must be <strong id="b84235270610044"><a name="b84235270610044"></a><a name="b84235270610044"></a>Standard</strong>. </p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    PUT https://{Endpoint}/v1/cloudimages/4ca46bf1-5c61-48ff-b4f3-0ad4e5e3ba86/upload
    ```

    ```
    {
       "image_url": "bucketname:Centos6.5-disk1.vmdk" 
    }
    ```


## Response<a name="section42338041154747"></a>

-   Response parameters

    <a name="table1337332211159"></a>
    <table><thead align="left"><tr id="row1133156911159"><th class="cellrowborder" valign="top" width="23.84%" id="mcps1.1.4.1.1"><p id="p4544189211159"><a name="p4544189211159"></a><a name="p4544189211159"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.97%" id="mcps1.1.4.1.2"><p id="p556206921988"><a name="p556206921988"></a><a name="p556206921988"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.19%" id="mcps1.1.4.1.3"><p id="p5691464411159"><a name="p5691464411159"></a><a name="p5691464411159"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4668343211159"><td class="cellrowborder" valign="top" width="23.84%" headers="mcps1.1.4.1.1 "><p id="p2326164111159"><a name="p2326164111159"></a><a name="p2326164111159"></a>job_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.97%" headers="mcps1.1.4.1.2 "><p id="p89821791988"><a name="p89821791988"></a><a name="p89821791988"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.19%" headers="mcps1.1.4.1.3 "><p id="p514473411159"><a name="p514473411159"></a><a name="p514473411159"></a>Specifies the asynchronous task ID.</p>
    <p id="p99354261311"><a name="p99354261311"></a><a name="p99354261311"></a>For details, see <a href="asynchronous-job-query.md">Asynchronous Job Query</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    HTTP/1.1 200
    ```

    ```
    {
       "job_id":" b912fb4a4c464b568ecfca1071b21b10"
    }
    ```


## Returned Value<a name="section61463701154747"></a>

-   Normal

    200

-   Abnormal

<a name="table61689654164325"></a>
<table><thead align="left"><tr id="row43263384164325"><th class="cellrowborder" valign="top" width="38.080000000000005%" id="mcps1.1.3.1.1"><p id="p14673233164325"><a name="p14673233164325"></a><a name="p14673233164325"></a>Returned Value</p>
</th>
<th class="cellrowborder" valign="top" width="61.919999999999995%" id="mcps1.1.3.1.2"><p id="p47681194164325"><a name="p47681194164325"></a><a name="p47681194164325"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row36971467164325"><td class="cellrowborder" valign="top" width="38.080000000000005%" headers="mcps1.1.3.1.1 "><p id="p41898845164325"><a name="p41898845164325"></a><a name="p41898845164325"></a>400 Bad Request</p>
</td>
<td class="cellrowborder" valign="top" width="61.919999999999995%" headers="mcps1.1.3.1.2 "><p id="p38363271164325"><a name="p38363271164325"></a><a name="p38363271164325"></a>Request error. For details about the returned error code, see <a href="error-codes.md">Error Codes</a>.</p>
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
</tbody>
</table>


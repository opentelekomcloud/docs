# Querying Image Metadata \(Native OpenStack API v1 - Abandoned and Not Recommended\)<a name="EN-US_TOPIC_0066978721"></a>

## Function<a name="section6658307515228"></a>

This API is used to query image metadata.

This API has been discarded. The API for querying image details \([Querying Image Details \(Native OpenStack API\)](querying-image-details-(native-openstack-api).md)\) is recommended.

## URI<a name="section1935356215228"></a>

HEAD /v1/images/\{image\_id\}

[Table 1](#table27262282)  lists the parameters in the URI.

**Table  1**  Parameter description

<a name="table27262282"></a>
<table><thead align="left"><tr id="row27551015"><th class="cellrowborder" valign="top" width="22.720000000000002%" id="mcps1.2.5.1.1"><p id="p17039762"><a name="p17039762"></a><a name="p17039762"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="20.71%" id="mcps1.2.5.1.2"><p id="p38043494"><a name="p38043494"></a><a name="p38043494"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="20.49%" id="mcps1.2.5.1.3"><p id="p1119157921331"><a name="p1119157921331"></a><a name="p1119157921331"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="36.08%" id="mcps1.2.5.1.4"><p id="p61624137"><a name="p61624137"></a><a name="p61624137"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row25499238"><td class="cellrowborder" valign="top" width="22.720000000000002%" headers="mcps1.2.5.1.1 "><p id="p52172387"><a name="p52172387"></a><a name="p52172387"></a>image_id</p>
</td>
<td class="cellrowborder" valign="top" width="20.71%" headers="mcps1.2.5.1.2 "><p id="p65213800"><a name="p65213800"></a><a name="p65213800"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="20.49%" headers="mcps1.2.5.1.3 "><p id="p3410274521331"><a name="p3410274521331"></a><a name="p3410274521331"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="36.08%" headers="mcps1.2.5.1.4 "><p id="p47826462"><a name="p47826462"></a><a name="p47826462"></a>Specifies the image ID.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section6467246815228"></a>

-   Request parameters

    None

-   Example request

    ```
    HEAD https://{Endpoint}/v1/images/3c3d1d01-b48a-4639-8a88-08be3b9b5d78
    ```


## Response<a name="section1674295515228"></a>

-   Response parameters

    <a name="table1400212915228"></a>
    <table><thead align="left"><tr id="row5823351215228"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="p1929404715228"><a name="p1929404715228"></a><a name="p1929404715228"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="p1931400315228"><a name="p1931400315228"></a><a name="p1931400315228"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="p1764174415228"><a name="p1764174415228"></a><a name="p1764174415228"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1969514515228"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p5180291115228"><a name="p5180291115228"></a><a name="p5180291115228"></a>Status</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p3528623315228"><a name="p3528623315228"></a><a name="p3528623315228"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p5450463515228"><a name="p5450463515228"></a><a name="p5450463515228"></a>Image status</p>
    </td>
    </tr>
    <tr id="row2077966715228"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p543149615228"><a name="p543149615228"></a><a name="p543149615228"></a>Virtual_size</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p3729805415228"><a name="p3729805415228"></a><a name="p3729805415228"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p3361529015228"><a name="p3361529015228"></a><a name="p3361529015228"></a>Virtual size of an image</p>
    </td>
    </tr>
    <tr id="row3410215815228"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p1081140415228"><a name="p1081140415228"></a><a name="p1081140415228"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p330853515228"><a name="p330853515228"></a><a name="p330853515228"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p3113630615228"><a name="p3113630615228"></a><a name="p3113630615228"></a>Image name</p>
    </td>
    </tr>
    <tr id="row1179129815228"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p1557104315228"><a name="p1557104315228"></a><a name="p1557104315228"></a>Deleted</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p5329496515228"><a name="p5329496515228"></a><a name="p5329496515228"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p3108609015228"><a name="p3108609015228"></a><a name="p3108609015228"></a>Whether an image has been deleted</p>
    </td>
    </tr>
    <tr id="row1133935915228"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p4607291015228"><a name="p4607291015228"></a><a name="p4607291015228"></a>Container_format</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p4091822515228"><a name="p4091822515228"></a><a name="p4091822515228"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p2902213315228"><a name="p2902213315228"></a><a name="p2902213315228"></a>Image container type</p>
    </td>
    </tr>
    <tr id="row5987260815228"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p1784309415228"><a name="p1784309415228"></a><a name="p1784309415228"></a>Created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p3600451615228"><a name="p3600451615228"></a><a name="p3600451615228"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p243466715228"><a name="p243466715228"></a><a name="p243466715228"></a>Time when an image was created</p>
    </td>
    </tr>
    <tr id="row2191200515228"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p3004199615228"><a name="p3004199615228"></a><a name="p3004199615228"></a>Disk_format</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p1748264015228"><a name="p1748264015228"></a><a name="p1748264015228"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p1455575715228"><a name="p1455575715228"></a><a name="p1455575715228"></a>Image file type</p>
    </td>
    </tr>
    <tr id="row6389295115228"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p794657015228"><a name="p794657015228"></a><a name="p794657015228"></a>Updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p3969241315228"><a name="p3969241315228"></a><a name="p3969241315228"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p3953030815228"><a name="p3953030815228"></a><a name="p3953030815228"></a>Time when an image was updated</p>
    </td>
    </tr>
    <tr id="row2022845615228"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p2789220715228"><a name="p2789220715228"></a><a name="p2789220715228"></a>Property</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p4467631515228"><a name="p4467631515228"></a><a name="p4467631515228"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p5689958515228"><a name="p5689958515228"></a><a name="p5689958515228"></a>Image attribute</p>
    </td>
    </tr>
    <tr id="row4233422315228"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p652003815228"><a name="p652003815228"></a><a name="p652003815228"></a>Owner</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p5836106115228"><a name="p5836106115228"></a><a name="p5836106115228"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p5085734215228"><a name="p5085734215228"></a><a name="p5085734215228"></a>Tenant to which an image belongs</p>
    </td>
    </tr>
    <tr id="row5506289515228"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p3090947115228"><a name="p3090947115228"></a><a name="p3090947115228"></a>Protected</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p2063919515228"><a name="p2063919515228"></a><a name="p2063919515228"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p5518505015228"><a name="p5518505015228"></a><a name="p5518505015228"></a>Whether an image is protected</p>
    </td>
    </tr>
    <tr id="row2690340715228"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p3169237115228"><a name="p3169237115228"></a><a name="p3169237115228"></a>Min_ram</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p1694522215228"><a name="p1694522215228"></a><a name="p1694522215228"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p4532902415228"><a name="p4532902415228"></a><a name="p4532902415228"></a>Minimum memory (MB) required for running an image</p>
    </td>
    </tr>
    <tr id="row530803415228"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p2729760315228"><a name="p2729760315228"></a><a name="p2729760315228"></a>Checksum</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p6362220015228"><a name="p6362220015228"></a><a name="p6362220015228"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p812156815228"><a name="p812156815228"></a><a name="p812156815228"></a>Image verification sum. This parameter is available after an image file is uploaded.</p>
    </td>
    </tr>
    <tr id="row598524815228"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p1504306415228"><a name="p1504306415228"></a><a name="p1504306415228"></a>Min_disk</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p1052864815228"><a name="p1052864815228"></a><a name="p1052864815228"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p2344248215228"><a name="p2344248215228"></a><a name="p2344248215228"></a>Minimum disk capacity (GB) required for running the image</p>
    </td>
    </tr>
    <tr id="row965575415228"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p4391859515228"><a name="p4391859515228"></a><a name="p4391859515228"></a>Is_public</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p63644115228"><a name="p63644115228"></a><a name="p63644115228"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p1494066515228"><a name="p1494066515228"></a><a name="p1494066515228"></a>Whether an image is a public one</p>
    </td>
    </tr>
    <tr id="row24826515228"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p2010950115228"><a name="p2010950115228"></a><a name="p2010950115228"></a>Deleted_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p1825691415228"><a name="p1825691415228"></a><a name="p1825691415228"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p6140441415228"><a name="p6140441415228"></a><a name="p6140441415228"></a>Time when an image was deleted</p>
    </td>
    </tr>
    <tr id="row1576881415228"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p220557615228"><a name="p220557615228"></a><a name="p220557615228"></a>Id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p4443395815228"><a name="p4443395815228"></a><a name="p4443395815228"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p1029672015228"><a name="p1029672015228"></a><a name="p1029672015228"></a>Image UUID</p>
    </td>
    </tr>
    <tr id="row2556161915228"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="p5722522815228"><a name="p5722522815228"></a><a name="p5722522815228"></a>Size</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="p473185315228"><a name="p473185315228"></a><a name="p473185315228"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="p4139514515228"><a name="p4139514515228"></a><a name="p4139514515228"></a>Image size. This parameter is available after an image file is uploaded.</p>
    </td>
    </tr>
    </tbody>
    </table>

    These parameters are contained in the header of the HTTP response message.

-   Example response

    ```
    HTTP/1.1 200 OK
    ```

    ```
    Content-Type: text/html; charset=UTF-8
    Content-Length: 0
    X-Image-Meta-Id: 3c3d1d01-b48a-4639-8a88-08be3b9b5d78
    X-Image-Meta-Deleted: False
    X-Image-Meta-Container_format: bare
    X-Image-Meta-Checksum: 64d7c1cd2b6f60c92c14662941cb7913
    X-Image-Meta-Protected: False
    X-Image-Meta-Min_disk: 0
    X-Image-Meta-Created_at: 2016-05-22T06:04:20.425843
    X-Image-Meta-Size: 13167616
    X-Image-Meta-Status: active
    X-Image-Meta-Is_public: True
    X-Image-Meta-Min_ram: 0
    X-Image-Meta-Owner: 23f4cb75768d4febb39542ef6fe169f3
    X-Image-Meta-Updated_at: 2016-05-22T06:04:22.719791
    X-Image-Meta-Disk_format: qcow2
    X-Image-Meta-Name: cirros
    Etag: 64d7c1cd2b6f60c92c14662941cb7913
    X-Openstack-Request-Id: req-7123ca83-da23-4f4e-9ed6-accd3707d333
    Date: Mon, 23 May 2016 02:29:54 GMT
    ```


## Returned Values<a name="section6571722315228"></a>

-   Normal

    200

-   Abnormal

    <a name="table262968317230"></a>
    <table><thead align="left"><tr id="row5740081817230"><th class="cellrowborder" valign="top" width="46.54%" id="mcps1.1.3.1.1"><p id="p1895465817230"><a name="p1895465817230"></a><a name="p1895465817230"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.459999999999994%" id="mcps1.1.3.1.2"><p id="p5893233917230"><a name="p5893233917230"></a><a name="p5893233917230"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row879015617230"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p4091407017230"><a name="p4091407017230"></a><a name="p4091407017230"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p2570540117230"><a name="p2570540117230"></a><a name="p2570540117230"></a>Request error.</p>
    </td>
    </tr>
    <tr id="row176271617230"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p856227917230"><a name="p856227917230"></a><a name="p856227917230"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p2245600317230"><a name="p2245600317230"></a><a name="p2245600317230"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row77743917230"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p6297256617230"><a name="p6297256617230"></a><a name="p6297256617230"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p50424217230"><a name="p50424217230"></a><a name="p50424217230"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="row56011270191147"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p40619053191147"><a name="p40619053191147"></a><a name="p40619053191147"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p1808959191147"><a name="p1808959191147"></a><a name="p1808959191147"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="row453818617230"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p3204876017230"><a name="p3204876017230"></a><a name="p3204876017230"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p4581273417230"><a name="p4581273417230"></a><a name="p4581273417230"></a>Internal service error.</p>
    </td>
    </tr>
    <tr id="row966142617230"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p4437803217230"><a name="p4437803217230"></a><a name="p4437803217230"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p3785084317230"><a name="p3785084317230"></a><a name="p3785084317230"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>



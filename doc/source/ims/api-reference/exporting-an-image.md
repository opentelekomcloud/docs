# Exporting an Image<a name="EN-US_TOPIC_0036994315"></a>

## Function<a name="section11046056154747"></a>

This is an extension API and used to export a private image to an OBS bucket.

>![](/images/icon-note.gif) **NOTE:**   
>Before exporting an image, ensure that you have the Tenant Administrator permission of OBS.  

## Constraints<a name="section921963105411"></a>

-   Images can only be exported to standard OBS buckets.
-   You can export private images in the  **Normal**  or  **Normal \(Uninitialized\)**  status.
-   You cannot export Windows or SUSE public images or private images created from these public images.
-   Full-ECS images cannot be exported.
-   You can only export images smaller than 128 GB.
-   You can export images only in the format of VMDK, VHD, QCOW2, or ZVHD.
-   You cannot export images created using CSBS backups.
-   If a market image is used to create an ECS and then the ECS is used to create a private image, this private image cannot be exported.

## URI<a name="section66620681154747"></a>

POST /v1/cloudimages/\{image\_id\}/file

[Table 1](#table23910047154747)  lists the parameters in the URI.

**Table  1**  Parameter description

<a name="table23910047154747"></a>
<table><thead align="left"><tr id="row24965460154747"><th class="cellrowborder" valign="top" width="19.918008199180083%" id="mcps1.2.5.1.1"><p id="p8936346154747"><a name="p8936346154747"></a><a name="p8936346154747"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="22.17778222177782%" id="mcps1.2.5.1.2"><p id="p4072498116916"><a name="p4072498116916"></a><a name="p4072498116916"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="16.348365163483653%" id="mcps1.2.5.1.3"><p id="p52755425154747"><a name="p52755425154747"></a><a name="p52755425154747"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="41.55584441555845%" id="mcps1.2.5.1.4"><p id="p57477321154747"><a name="p57477321154747"></a><a name="p57477321154747"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row25151394154747"><td class="cellrowborder" valign="top" width="19.918008199180083%" headers="mcps1.2.5.1.1 "><p id="p23996995154747"><a name="p23996995154747"></a><a name="p23996995154747"></a>image_id</p>
</td>
<td class="cellrowborder" valign="top" width="22.17778222177782%" headers="mcps1.2.5.1.2 "><p id="p1038913616916"><a name="p1038913616916"></a><a name="p1038913616916"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="16.348365163483653%" headers="mcps1.2.5.1.3 "><p id="p64708437154747"><a name="p64708437154747"></a><a name="p64708437154747"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="41.55584441555845%" headers="mcps1.2.5.1.4 "><p id="p54354750154747"><a name="p54354750154747"></a><a name="p54354750154747"></a>Specifies the image ID.</p>
<p id="p127065072116"><a name="p127065072116"></a><a name="p127065072116"></a>For details about how to obtain the image ID, see <a href="querying-images.md">Querying Images</a>.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section29704853154747"></a>

-   Request parameters

    <a name="table57282886154747"></a>
    <table><thead align="left"><tr id="row33194661154747"><th class="cellrowborder" valign="top" width="20.200000000000003%" id="mcps1.1.5.1.1"><p id="p4413036154747"><a name="p4413036154747"></a><a name="p4413036154747"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.32%" id="mcps1.1.5.1.2"><p id="p15244109154747"><a name="p15244109154747"></a><a name="p15244109154747"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.01%" id="mcps1.1.5.1.3"><p id="p4364817210345"><a name="p4364817210345"></a><a name="p4364817210345"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="41.47%" id="mcps1.1.5.1.4"><p id="p26813302154747"><a name="p26813302154747"></a><a name="p26813302154747"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row24393852154747"><td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.1.5.1.1 "><p id="p5109612910120"><a name="p5109612910120"></a><a name="p5109612910120"></a>bucket_url</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.32%" headers="mcps1.1.5.1.2 "><p id="p4514577610120"><a name="p4514577610120"></a><a name="p4514577610120"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.01%" headers="mcps1.1.5.1.3 "><p id="p3292926410120"><a name="p3292926410120"></a><a name="p3292926410120"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.47%" headers="mcps1.1.5.1.4 "><p id="p5002474510120"><a name="p5002474510120"></a><a name="p5002474510120"></a>Specifies the URL of the image file in the format of <em id="i84235269795256"><a name="i84235269795256"></a><a name="i84235269795256"></a>Bucket name</em>:<em id="i84235269795259"><a name="i84235269795259"></a><a name="i84235269795259"></a>File name</em>.</p>
    <div class="note" id="note5552125083518"><a name="note5552125083518"></a><a name="note5552125083518"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1555325043517"><a name="p1555325043517"></a><a name="p1555325043517"></a>The storage class of the OBS bucket must be <strong id="b19684172820416"><a name="b19684172820416"></a><a name="b19684172820416"></a>Standard</strong>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row835962711950"><td class="cellrowborder" valign="top" width="20.200000000000003%" headers="mcps1.1.5.1.1 "><p id="p604120411950"><a name="p604120411950"></a><a name="p604120411950"></a>file_format</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.32%" headers="mcps1.1.5.1.2 "><p id="p1957548511950"><a name="p1957548511950"></a><a name="p1957548511950"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.01%" headers="mcps1.1.5.1.3 "><p id="p4211041411950"><a name="p4211041411950"></a><a name="p4211041411950"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.47%" headers="mcps1.1.5.1.4 "><p id="p5550036811950"><a name="p5550036811950"></a><a name="p5550036811950"></a>Specifies the file format. The value can be <strong id="b842352706101048"><a name="b842352706101048"></a><a name="b842352706101048"></a>qcow2</strong>, <strong id="b842352706101053"><a name="b842352706101053"></a><a name="b842352706101053"></a>vhd</strong>, <strong id="b842352706101056"><a name="b842352706101056"></a><a name="b842352706101056"></a>zvhd</strong>, or <strong id="b84235270610111"><a name="b84235270610111"></a><a name="b84235270610111"></a>vmdk</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    POST https://{Endpoint}/v1/cloudimages/d164b5df-1bc3-4c3f-893e-3e471fd16e64/file
    ```

    ```
    {
       "bucket_url": "ims-image:centos7_5.qcow2",
       "file_format": "qcow2"
    }
    ```


## Response<a name="section42338041154747"></a>

-   Response parameters

    <a name="table142317910447"></a>
    <table><thead align="left"><tr id="row3520294810447"><th class="cellrowborder" valign="top" width="30.486951304869514%" id="mcps1.1.4.1.1"><p id="p3286650610447"><a name="p3286650610447"></a><a name="p3286650610447"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.078292170782923%" id="mcps1.1.4.1.2"><p id="p1636902410447"><a name="p1636902410447"></a><a name="p1636902410447"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="52.434756524347556%" id="mcps1.1.4.1.3"><p id="p5082259210447"><a name="p5082259210447"></a><a name="p5082259210447"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2298930510447"><td class="cellrowborder" valign="top" width="30.486951304869514%" headers="mcps1.1.4.1.1 "><p id="p5019438610447"><a name="p5019438610447"></a><a name="p5019438610447"></a>job_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.078292170782923%" headers="mcps1.1.4.1.2 "><p id="p2217101310447"><a name="p2217101310447"></a><a name="p2217101310447"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.434756524347556%" headers="mcps1.1.4.1.3 "><p id="p5102161510447"><a name="p5102161510447"></a><a name="p5102161510447"></a>Specifies the asynchronous job ID.</p>
    <p id="p19968122117312"><a name="p19968122117312"></a><a name="p19968122117312"></a>For details, see <a href="asynchronous-job-query.md">Asynchronous Job Query</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    STATUS CODE 200
    ```

    ```
    {
        "job_id": "edc89b490d7d4392898e19b2deb34797"
    }
    ```


## Returned Value<a name="section40084941"></a>

-   Normal

    200

-   Abnormal

    <a name="table1069408417333"></a>
    <table><thead align="left"><tr id="row4772021317333"><th class="cellrowborder" valign="top" width="46.54%" id="mcps1.1.3.1.1"><p id="p4013206717333"><a name="p4013206717333"></a><a name="p4013206717333"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.459999999999994%" id="mcps1.1.3.1.2"><p id="p2947196917333"><a name="p2947196917333"></a><a name="p2947196917333"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3841925517333"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p2495195017333"><a name="p2495195017333"></a><a name="p2495195017333"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p784206117333"><a name="p784206117333"></a><a name="p784206117333"></a>Request error. For details about the returned error code, see <a href="error-codes.md">Error Codes</a>.</p>
    </td>
    </tr>
    <tr id="row3122722917333"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p4637763817333"><a name="p4637763817333"></a><a name="p4637763817333"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p6560116717333"><a name="p6560116717333"></a><a name="p6560116717333"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row5353959117333"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p4173958717333"><a name="p4173958717333"></a><a name="p4173958717333"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p2546341217333"><a name="p2546341217333"></a><a name="p2546341217333"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="row5197513192250"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p21898657192252"><a name="p21898657192252"></a><a name="p21898657192252"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p28960832192252"><a name="p28960832192252"></a><a name="p28960832192252"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="row2784412417333"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p4078159117333"><a name="p4078159117333"></a><a name="p4078159117333"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p1497458717333"><a name="p1497458717333"></a><a name="p1497458717333"></a>Internal service error.</p>
    </td>
    </tr>
    <tr id="row55355517333"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p4483799017333"><a name="p4483799017333"></a><a name="p4483799017333"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p799858217333"><a name="p799858217333"></a><a name="p799858217333"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>



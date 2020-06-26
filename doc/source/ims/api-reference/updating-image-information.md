# Updating Image Information<a name="EN-US_TOPIC_0020091567"></a>

## Function<a name="section16095919"></a>

This API is used to modify image attributes and update image information.

>![](/images/icon-note.gif) **NOTE:**   
>Only information of images in  **active**  status can be changed.  

## URI<a name="section10645546"></a>

PATCH /v2/cloudimages/\{image\_id\}

[Table 1](#table30282311)  describes the parameters in the URI.

**Table  1**  Parameter description

<a name="table30282311"></a>
<table><thead align="left"><tr id="row19672999"><th class="cellrowborder" valign="top" width="25.75%" id="mcps1.2.5.1.1"><p id="p50009058"><a name="p50009058"></a><a name="p50009058"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="22.37%" id="mcps1.2.5.1.2"><p id="p24201902"><a name="p24201902"></a><a name="p24201902"></a>Mandatory</p>
</th>
<th class="cellrowborder" valign="top" width="21.05%" id="mcps1.2.5.1.3"><p id="p265296612135"><a name="p265296612135"></a><a name="p265296612135"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="30.830000000000002%" id="mcps1.2.5.1.4"><p id="p14197042"><a name="p14197042"></a><a name="p14197042"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row41227749"><td class="cellrowborder" valign="top" width="25.75%" headers="mcps1.2.5.1.1 "><p id="p51113363"><a name="p51113363"></a><a name="p51113363"></a>image_id</p>
</td>
<td class="cellrowborder" valign="top" width="22.37%" headers="mcps1.2.5.1.2 "><p id="p46541742"><a name="p46541742"></a><a name="p46541742"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="21.05%" headers="mcps1.2.5.1.3 "><p id="p14189122135"><a name="p14189122135"></a><a name="p14189122135"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="30.830000000000002%" headers="mcps1.2.5.1.4 "><p id="p11784733"><a name="p11784733"></a><a name="p11784733"></a>Specifies the image ID.</p>
<p id="p127065072116"><a name="p127065072116"></a><a name="p127065072116"></a>For details about how to obtain the image ID, see <a href="querying-images.md">Querying Images</a>.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section28701056"></a>

-   Request parameters

    <a name="table5455656611030"></a>
    <table><thead align="left"><tr id="row1943767711030"><th class="cellrowborder" valign="top" width="19.36%" id="mcps1.1.5.1.1"><p id="p3094801411030"><a name="p3094801411030"></a><a name="p3094801411030"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.11%" id="mcps1.1.5.1.2"><p id="p2376120711030"><a name="p2376120711030"></a><a name="p2376120711030"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.669999999999998%" id="mcps1.1.5.1.3"><p id="p4560964911030"><a name="p4560964911030"></a><a name="p4560964911030"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="42.86%" id="mcps1.1.5.1.4"><p id="p339411611030"><a name="p339411611030"></a><a name="p339411611030"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row648795911030"><td class="cellrowborder" valign="top" width="19.36%" headers="mcps1.1.5.1.1 "><p id="p5576264211030"><a name="p5576264211030"></a><a name="p5576264211030"></a>op</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.11%" headers="mcps1.1.5.1.2 "><p id="p2048015811030"><a name="p2048015811030"></a><a name="p2048015811030"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.669999999999998%" headers="mcps1.1.5.1.3 "><p id="p4828009811030"><a name="p4828009811030"></a><a name="p4828009811030"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.86%" headers="mcps1.1.5.1.4 "><p id="p1837389511030"><a name="p1837389511030"></a><a name="p1837389511030"></a>Specifies the operation. The value can be <strong id="b1028539183915"><a name="b1028539183915"></a><a name="b1028539183915"></a>add</strong>, <strong id="b6291539113919"><a name="b6291539113919"></a><a name="b6291539113919"></a>replace</strong>, or <strong id="b529439103913"><a name="b529439103913"></a><a name="b529439103913"></a>remove</strong>.</p>
    </td>
    </tr>
    <tr id="row3114733311030"><td class="cellrowborder" valign="top" width="19.36%" headers="mcps1.1.5.1.1 "><p id="p3990607811030"><a name="p3990607811030"></a><a name="p3990607811030"></a>path</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.11%" headers="mcps1.1.5.1.2 "><p id="p1116689111030"><a name="p1116689111030"></a><a name="p1116689111030"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.669999999999998%" headers="mcps1.1.5.1.3 "><p id="p3210299711030"><a name="p3210299711030"></a><a name="p3210299711030"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.86%" headers="mcps1.1.5.1.4 "><p id="p6308567716410"><a name="p6308567716410"></a><a name="p6308567716410"></a>Specifies the name of the attribute to be modified. <strong id="b14174132152513"><a name="b14174132152513"></a><a name="b14174132152513"></a>/</strong> needs to be added in front of it.</p>
    <p id="p219111881645"><a name="p219111881645"></a><a name="p219111881645"></a>You can modify the following attributes:</p>
    <a name="ul3977269316441"></a><a name="ul3977269316441"></a><ul id="ul3977269316441"><li><strong id="b86681055111517"><a name="b86681055111517"></a><a name="b86681055111517"></a>name</strong>: specifies the image name.</li><li><strong id="b177221118153"><a name="b177221118153"></a><a name="b177221118153"></a>__description</strong>: specifies the image description.</li><li><strong id="b27131414152013"><a name="b27131414152013"></a><a name="b27131414152013"></a>__support_xen</strong>: Xen is supported.</li><li><strong id="b1383418378208"><a name="b1383418378208"></a><a name="b1383418378208"></a>__support_largememory</strong>: Ultra-large memory is supported.</li><li><strong id="b4998457152018"><a name="b4998457152018"></a><a name="b4998457152018"></a>__support_diskintensive</strong>: Intensive storage is supported.</li><li><strong id="b1210411203211"><a name="b1210411203211"></a><a name="b1210411203211"></a>__support_highperformance</strong>: High-performance computing (HPC) is supported.</li><li><strong id="b613885132115"><a name="b613885132115"></a><a name="b613885132115"></a>__support_xen_gpu_type</strong>: GPU-optimized ECSs that use Xen for virtualization are supported.</li><li><strong id="b17744048142915"><a name="b17744048142915"></a><a name="b17744048142915"></a>__support_xen_hana</strong>: HANA ECSs that use Xen for virtualization are supported.</li><li><strong id="b1768883173119"><a name="b1768883173119"></a><a name="b1768883173119"></a>min_ram</strong>: specifies the minimum memory.</li><li><strong id="b589565412318"><a name="b589565412318"></a><a name="b589565412318"></a>hw_vif_multiqueue_enabled</strong>: The NIC multi-queue feature is supported.</li><li><strong id="b569465518329"><a name="b569465518329"></a><a name="b569465518329"></a>hw_firmware_uefi</strong>: The UEFU boot mode is supported.</li></ul>
    <p id="p5020595511030"><a name="p5020595511030"></a><a name="p5020595511030"></a>You can add or delete extension attributes.</p>
    </td>
    </tr>
    <tr id="row4920041511030"><td class="cellrowborder" valign="top" width="19.36%" headers="mcps1.1.5.1.1 "><p id="p2581070311030"><a name="p2581070311030"></a><a name="p2581070311030"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.11%" headers="mcps1.1.5.1.2 "><p id="p1029221611030"><a name="p1029221611030"></a><a name="p1029221611030"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.669999999999998%" headers="mcps1.1.5.1.3 "><p id="p4031814520459"><a name="p4031814520459"></a><a name="p4031814520459"></a>Determined by the attribute value.</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.86%" headers="mcps1.1.5.1.4 "><p id="p1571272211030"><a name="p1571272211030"></a><a name="p1571272211030"></a>Specifies the new value of the attribute. For detailed description, see <a href="image-attributes.md#section61598810155254">Image Attributes</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    PATCH  https://{Endpoint}/v2/cloudimages/33ad552d-1149-471c-8190-ff6776174a00
    ```

    ```
    [
        {
            "op": "replace",
            "path": "/name",
            "value": "ims_test"
        }
    ]
    ```


## Response<a name="section56982912"></a>

-   Response parameters

    <a name="table16258230194835"></a>
    <table><thead align="left"><tr id="row23919935194835"><th class="cellrowborder" valign="top" width="28.57%" id="mcps1.1.4.1.1"><p id="p58466603194835"><a name="p58466603194835"></a><a name="p58466603194835"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.29%" id="mcps1.1.4.1.2"><p id="p38174436194835"><a name="p38174436194835"></a><a name="p38174436194835"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.14%" id="mcps1.1.4.1.3"><p id="p5121617194835"><a name="p5121617194835"></a><a name="p5121617194835"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row12197851194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p48501865194835"><a name="p48501865194835"></a><a name="p48501865194835"></a>file</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="p36336996194835"><a name="p36336996194835"></a><a name="p36336996194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p57615539194835"><a name="p57615539194835"></a><a name="p57615539194835"></a>Specifies the URL for uploading and downloading the image file.</p>
    </td>
    </tr>
    <tr id="row48777806194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p58688183194835"><a name="p58688183194835"></a><a name="p58688183194835"></a>owner</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="p56122344194835"><a name="p56122344194835"></a><a name="p56122344194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p49616010194835"><a name="p49616010194835"></a><a name="p49616010194835"></a>Specifies the image owner.</p>
    </td>
    </tr>
    <tr id="row43890908194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p65502698194835"><a name="p65502698194835"></a><a name="p65502698194835"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="p4118332194835"><a name="p4118332194835"></a><a name="p4118332194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p65149499194835"><a name="p65149499194835"></a><a name="p65149499194835"></a>Specifies the image ID.</p>
    </td>
    </tr>
    <tr id="row49474582194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p48018243194835"><a name="p48018243194835"></a><a name="p48018243194835"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="p64272464194835"><a name="p64272464194835"></a><a name="p64272464194835"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p38687077194835"><a name="p38687077194835"></a><a name="p38687077194835"></a>This parameter is unavailable currently.</p>
    </td>
    </tr>
    <tr id="row12639379194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p17156744194835"><a name="p17156744194835"></a><a name="p17156744194835"></a>self</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="p47519001194835"><a name="p47519001194835"></a><a name="p47519001194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p23833904194835"><a name="p23833904194835"></a><a name="p23833904194835"></a>Specifies the image URL.</p>
    </td>
    </tr>
    <tr id="row13178544194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p60829128194835"><a name="p60829128194835"></a><a name="p60829128194835"></a>schema</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="p28212312194835"><a name="p28212312194835"></a><a name="p28212312194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p3495945194835"><a name="p3495945194835"></a><a name="p3495945194835"></a>Specifies the image schema.</p>
    </td>
    </tr>
    <tr id="row31463509194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p65516314194835"><a name="p65516314194835"></a><a name="p65516314194835"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="p5221203194835"><a name="p5221203194835"></a><a name="p5221203194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p29539523155411"><a name="p29539523155411"></a><a name="p29539523155411"></a>Specifies the image status. The value can be one of the following:</p>
    <a name="ul64671162155411"></a><a name="ul64671162155411"></a><ul id="ul64671162155411"><li><strong id="b842352706103333"><a name="b842352706103333"></a><a name="b842352706103333"></a>queued</strong>: indicates that the image metadata has already been created, and it is ready for the image file to upload. </li><li><strong id="b842352706104325"><a name="b842352706104325"></a><a name="b842352706104325"></a>saving</strong>: indicates that the image file is being uploaded to the backend storage. </li><li><strong id="b842352706104450"><a name="b842352706104450"></a><a name="b842352706104450"></a>deleted</strong>: indicates that the image has been deleted. </li><li><strong id="b842352706104518"><a name="b842352706104518"></a><a name="b842352706104518"></a>killed</strong>: indicates that an error occurs on the image uploading. </li><li><strong id="b842352706104558"><a name="b842352706104558"></a><a name="b842352706104558"></a>active</strong>: indicates that the image is available for use. </li></ul>
    </td>
    </tr>
    <tr id="row48160946194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p8722525194835"><a name="p8722525194835"></a><a name="p8722525194835"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="p35435929194835"><a name="p35435929194835"></a><a name="p35435929194835"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p51737997194835"><a name="p51737997194835"></a><a name="p51737997194835"></a>Lists the image tags, through which you can manage private images in your own way. You can use the image tag API to add different tags to each image and filter images by tag.</p>
    </td>
    </tr>
    <tr id="row62988796194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p1818872194835"><a name="p1818872194835"></a><a name="p1818872194835"></a>visibility</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="p13110977194835"><a name="p13110977194835"></a><a name="p13110977194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p13296112271017"><a name="p13296112271017"></a><a name="p13296112271017"></a>Specifies whether the image is available to other tenants. The value can be one of the following:</p>
    <a name="ul5644164418103"></a><a name="ul5644164418103"></a><ul id="ul5644164418103"><li><strong id="b183535353418"><a name="b183535353418"></a><a name="b183535353418"></a>private</strong>: private image</li><li><strong id="b96231055203419"><a name="b96231055203419"></a><a name="b96231055203419"></a>public</strong>: public image</li><li><strong id="b1527335713413"><a name="b1527335713413"></a><a name="b1527335713413"></a>shared</strong>: shared image</li></ul>
    </td>
    </tr>
    <tr id="row28443956194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p22259099194835"><a name="p22259099194835"></a><a name="p22259099194835"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="p58156586194835"><a name="p58156586194835"></a><a name="p58156586194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p13063050194835"><a name="p13063050194835"></a><a name="p13063050194835"></a>Specifies the image name. For detailed description, see <a href="image-attributes.md#section61598810155254">Image Attributes</a>.</p>
    </td>
    </tr>
    <tr id="row50458592194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p60614140194835"><a name="p60614140194835"></a><a name="p60614140194835"></a>checksum</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="p10798268194835"><a name="p10798268194835"></a><a name="p10798268194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p2244488194835"><a name="p2244488194835"></a><a name="p2244488194835"></a>This parameter is unavailable currently.</p>
    </td>
    </tr>
    <tr id="row20200399194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p25619609194835"><a name="p25619609194835"></a><a name="p25619609194835"></a>deleted</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="p61922468194835"><a name="p61922468194835"></a><a name="p61922468194835"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p49664024194835"><a name="p49664024194835"></a><a name="p49664024194835"></a>Specifies whether the image has been deleted. The value can be <strong id="b178851538203618"><a name="b178851538203618"></a><a name="b178851538203618"></a>true</strong> or <strong id="b1289711387361"><a name="b1289711387361"></a><a name="b1289711387361"></a>false</strong>.</p>
    </td>
    </tr>
    <tr id="row44323032194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p33395835194835"><a name="p33395835194835"></a><a name="p33395835194835"></a>protected</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="p20708123194835"><a name="p20708123194835"></a><a name="p20708123194835"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p66745247194835"><a name="p66745247194835"></a><a name="p66745247194835"></a>Specifies whether the image is protected. A protected image cannot be deleted. The value can be <strong id="b149531447103618"><a name="b149531447103618"></a><a name="b149531447103618"></a>true</strong> or <strong id="b169534478363"><a name="b169534478363"></a><a name="b169534478363"></a>false</strong>.</p>
    </td>
    </tr>
    <tr id="row63836314194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p3358960194835"><a name="p3358960194835"></a><a name="p3358960194835"></a>container_format</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="p3640350194835"><a name="p3640350194835"></a><a name="p3640350194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p26432973194835"><a name="p26432973194835"></a><a name="p26432973194835"></a>Specifies the container type.</p>
    </td>
    </tr>
    <tr id="row36570173194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p9393999194835"><a name="p9393999194835"></a><a name="p9393999194835"></a>min_ram</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="p22716470194835"><a name="p22716470194835"></a><a name="p22716470194835"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p28094810194835"><a name="p28094810194835"></a><a name="p28094810194835"></a>Specifies the minimum memory size (MB) required for running the image. The parameter value depends on the <span id="text134961814105612"><a name="text134961814105612"></a><a name="text134961814105612"></a></span><span id="text5497131475612"><a name="text5497131475612"></a><a name="text5497131475612"></a>ECS</span> specifications. The default value is <strong id="b174975148566"><a name="b174975148566"></a><a name="b174975148566"></a>0</strong>.</p>
    </td>
    </tr>
    <tr id="row51176839416"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p118791549416"><a name="p118791549416"></a><a name="p118791549416"></a>max_ram</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="p257405589416"><a name="p257405589416"></a><a name="p257405589416"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p46104269416"><a name="p46104269416"></a><a name="p46104269416"></a>Specifies the maximum memory of the image in the unit of MB. The parameter value depends on the ECS flavor and is not configured by default.</p>
    </td>
    </tr>
    <tr id="row51526702194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p12913335194835"><a name="p12913335194835"></a><a name="p12913335194835"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="p39347249194835"><a name="p39347249194835"></a><a name="p39347249194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p33010628194835"><a name="p33010628194835"></a><a name="p33010628194835"></a>Specifies the time when the image was updated. The value is in UTC format. </p>
    </td>
    </tr>
    <tr id="row28660198194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p39774672194835"><a name="p39774672194835"></a><a name="p39774672194835"></a>__os_bit</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="p522982194835"><a name="p522982194835"></a><a name="p522982194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p42361618194835"><a name="p42361618194835"></a><a name="p42361618194835"></a>Specifies the OS architecture, 32 bit or 64 bit.</p>
    </td>
    </tr>
    <tr id="row45710242194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p11542151194835"><a name="p11542151194835"></a><a name="p11542151194835"></a>__os_version</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="p62499061194835"><a name="p62499061194835"></a><a name="p62499061194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p29259155194835"><a name="p29259155194835"></a><a name="p29259155194835"></a>Specifies the OS version.</p>
    </td>
    </tr>
    <tr id="row62005803194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p56414165194835"><a name="p56414165194835"></a><a name="p56414165194835"></a>__description</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="p6144643194835"><a name="p6144643194835"></a><a name="p6144643194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p27954078194835"><a name="p27954078194835"></a><a name="p27954078194835"></a>Provides supplementary information about the image. For detailed description, see <a href="image-attributes.md#section61598810155254">Image Attributes</a>.</p>
    </td>
    </tr>
    <tr id="row50260111194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p44537208194835"><a name="p44537208194835"></a><a name="p44537208194835"></a>disk_format</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="p50744065194835"><a name="p50744065194835"></a><a name="p50744065194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p16628562194835"><a name="p16628562194835"></a><a name="p16628562194835"></a>Specifies the image format. The value can be <strong id="b667911865611"><a name="b667911865611"></a><a name="b667911865611"></a>vhd</strong>, <strong id="b867919181567"><a name="b867919181567"></a><a name="b867919181567"></a>raw</strong>, <strong id="b17680121815617"><a name="b17680121815617"></a><a name="b17680121815617"></a>zvhd</strong>, or <strong id="b136811818105613"><a name="b136811818105613"></a><a name="b136811818105613"></a>qcow2</strong>. The default value is <strong id="b842352706165234"><a name="b842352706165234"></a><a name="b842352706165234"></a>vhd</strong>.</p>
    </td>
    </tr>
    <tr id="row15439333194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p42626486194835"><a name="p42626486194835"></a><a name="p42626486194835"></a>__isregistered</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="p30193380194835"><a name="p30193380194835"></a><a name="p30193380194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p29744726194835"><a name="p29744726194835"></a><a name="p29744726194835"></a>Specifies whether the image has been registered. The value can be <strong id="b1378193283816"><a name="b1378193283816"></a><a name="b1378193283816"></a>true</strong> or <strong id="b178243211384"><a name="b178243211384"></a><a name="b178243211384"></a>false</strong>.</p>
    </td>
    </tr>
    <tr id="row66375949194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p7742752194835"><a name="p7742752194835"></a><a name="p7742752194835"></a>__platform</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="p23183213194835"><a name="p23183213194835"></a><a name="p23183213194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p16267923202620"><a name="p16267923202620"></a><a name="p16267923202620"></a>Specifies the image platform type. The value can be <strong id="b128190224020"><a name="b128190224020"></a><a name="b128190224020"></a>Windows</strong>, <strong id="b682015218401"><a name="b682015218401"></a><a name="b682015218401"></a>Ubuntu</strong>, <strong id="b582011210401"><a name="b582011210401"></a><a name="b582011210401"></a>RedHat</strong>, <strong id="b198217210406"><a name="b198217210406"></a><a name="b198217210406"></a>SUSE</strong>, <strong id="b118211725408"><a name="b118211725408"></a><a name="b118211725408"></a>CentOS</strong>, <strong id="b1382219244016"><a name="b1382219244016"></a><a name="b1382219244016"></a>Debian</strong>, <strong id="b38228215405"><a name="b38228215405"></a><a name="b38228215405"></a>OpenSUSE</strong>, <strong id="b1682318234014"><a name="b1682318234014"></a><a name="b1682318234014"></a>Oracle Linux</strong>, <strong id="b982313213407"><a name="b982313213407"></a><a name="b982313213407"></a>Fedora</strong>, <strong id="b1982315212402"><a name="b1982315212402"></a><a name="b1982315212402"></a>Other</strong>, <strong id="b128241625407"><a name="b128241625407"></a><a name="b128241625407"></a>CoreOS</strong>, or <strong id="b38246217405"><a name="b38246217405"></a><a name="b38246217405"></a>EulerOS</strong>.</p>
    </td>
    </tr>
    <tr id="row56237676194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p58957901194835"><a name="p58957901194835"></a><a name="p58957901194835"></a>__os_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="p10860642194835"><a name="p10860642194835"></a><a name="p10860642194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p7296787194835"><a name="p7296787194835"></a><a name="p7296787194835"></a>Specifies the OS type. The value can be <strong id="b111902564014"><a name="b111902564014"></a><a name="b111902564014"></a>Linux</strong>, <strong id="b2191258406"><a name="b2191258406"></a><a name="b2191258406"></a>Windows</strong>, or <strong id="b1219115564017"><a name="b1219115564017"></a><a name="b1219115564017"></a>Other</strong>.</p>
    </td>
    </tr>
    <tr id="row65671090194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p17758106194835"><a name="p17758106194835"></a><a name="p17758106194835"></a>min_disk</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="p29120466194835"><a name="p29120466194835"></a><a name="p29120466194835"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p9947522194835"><a name="p9947522194835"></a><a name="p9947522194835"></a>Specifies the minimum disk space (GB) required for running the image. The value ranges from 1 GB to 1024 GB.</p>
    </td>
    </tr>
    <tr id="row22418839194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p3986671194835"><a name="p3986671194835"></a><a name="p3986671194835"></a>virtual_env_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="p54484948194835"><a name="p54484948194835"></a><a name="p54484948194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p125611053153413"><a name="p125611053153413"></a><a name="p125611053153413"></a>Specifies the environment where the image is used. The value can be <strong id="b1331907114015"><a name="b1331907114015"></a><a name="b1331907114015"></a>FusionCompute</strong>, <strong id="b4320573403"><a name="b4320573403"></a><a name="b4320573403"></a>Ironic</strong>, or <strong id="b63201371402"><a name="b63201371402"></a><a name="b63201371402"></a>DataImage</strong>.</p>
    <a name="ul20526189153516"></a><a name="ul20526189153516"></a><ul id="ul20526189153516"><li>For an <span id="text1175125161018"><a name="text1175125161018"></a><a name="text1175125161018"></a></span><span id="text576145111017"><a name="text576145111017"></a><a name="text576145111017"></a>ECS</span> image (system disk image), the value is <strong id="b376175112109"><a name="b376175112109"></a><a name="b376175112109"></a>FusionCompute</strong>.</li><li>For a data disk image, set the value to <strong id="b166310339511"><a name="b166310339511"></a><a name="b166310339511"></a>DataImage</strong>.</li><li>For a <span id="text1839145751012"><a name="text1839145751012"></a><a name="text1839145751012"></a></span><span id="text539117577103"><a name="text539117577103"></a><a name="text539117577103"></a>BMS</span> image, the value is <strong id="b2392115721014"><a name="b2392115721014"></a><a name="b2392115721014"></a>Ironic</strong>.</li></ul>
    </td>
    </tr>
    <tr id="row58188697194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p15663996194835"><a name="p15663996194835"></a><a name="p15663996194835"></a>__image_source_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="p60824135194835"><a name="p60824135194835"></a><a name="p60824135194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p27807907194835"><a name="p27807907194835"></a><a name="p27807907194835"></a>Specifies the image backend storage type. Only UDS is supported currently. </p>
    </td>
    </tr>
    <tr id="row48944575194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p5087606194835"><a name="p5087606194835"></a><a name="p5087606194835"></a>__imagetype</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="p9442962194835"><a name="p9442962194835"></a><a name="p9442962194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p2572734285718"><a name="p2572734285718"></a><a name="p2572734285718"></a>Specifies the image type. The following types are supported:</p>
    <a name="ul6291210685828"></a><a name="ul6291210685828"></a><ul id="ul6291210685828"><li>Public image: The value is <strong id="b842352706163515"><a name="b842352706163515"></a><a name="b842352706163515"></a>gold</strong>.</li><li>Private image: The value is <strong id="b1762610292163524"><a name="b1762610292163524"></a><a name="b1762610292163524"></a>private</strong>.</li><li>Shared image: The value is <strong id="b298092137163545"><a name="b298092137163545"></a><a name="b298092137163545"></a>shared</strong>.</li></ul>
    </td>
    </tr>
    <tr id="row38815832194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p57074654194835"><a name="p57074654194835"></a><a name="p57074654194835"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="p59644261194835"><a name="p59644261194835"></a><a name="p59644261194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p66455828194835"><a name="p66455828194835"></a><a name="p66455828194835"></a>Specifies the time when the image was created. The value is in UTC format. </p>
    </td>
    </tr>
    <tr id="row61231547194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p60808250194835"><a name="p60808250194835"></a><a name="p60808250194835"></a>virtual_size</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="p26521206194835"><a name="p26521206194835"></a><a name="p26521206194835"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p734038194835"><a name="p734038194835"></a><a name="p734038194835"></a>This parameter is unavailable currently.</p>
    </td>
    </tr>
    <tr id="row6606343194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p65351769194835"><a name="p65351769194835"></a><a name="p65351769194835"></a>deleted_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="p59001923194835"><a name="p59001923194835"></a><a name="p59001923194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p14426478194835"><a name="p14426478194835"></a><a name="p14426478194835"></a>Specifies the time when the image was deleted. The value is in UTC format. </p>
    </td>
    </tr>
    <tr id="row62729443194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p47920146194835"><a name="p47920146194835"></a><a name="p47920146194835"></a>__originalimagename</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="p56326613194835"><a name="p56326613194835"></a><a name="p56326613194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p66161813194835"><a name="p66161813194835"></a><a name="p66161813194835"></a>Specifies the parent image ID.</p>
    <p id="p58585407194835"><a name="p58585407194835"></a><a name="p58585407194835"></a>If the image is a public image or created from an image file, this value is left empty.</p>
    </td>
    </tr>
    <tr id="row57506617194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p27524394194835"><a name="p27524394194835"></a><a name="p27524394194835"></a>__backup_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="p14883407194835"><a name="p14883407194835"></a><a name="p14883407194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p64705296194835"><a name="p64705296194835"></a><a name="p64705296194835"></a>Specifies the backup ID. To create an image using a backup, set the value to the backup ID. Otherwise, this value is left empty.</p>
    </td>
    </tr>
    <tr id="row45476759194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p59738895194835"><a name="p59738895194835"></a><a name="p59738895194835"></a>__productcode</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="p7012311194835"><a name="p7012311194835"></a><a name="p7012311194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p31126295194835"><a name="p31126295194835"></a><a name="p31126295194835"></a>Specifies the ID of the market image product.</p>
    </td>
    </tr>
    <tr id="row54629742194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p62932961194835"><a name="p62932961194835"></a><a name="p62932961194835"></a>__image_size</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="p64405052194835"><a name="p64405052194835"></a><a name="p64405052194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p49426728194835"><a name="p49426728194835"></a><a name="p49426728194835"></a>Specifies the size (bytes) of the image file. Value: an integer greater than 0</p>
    </td>
    </tr>
    <tr id="row42187372194835"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p61733939194835"><a name="p61733939194835"></a><a name="p61733939194835"></a>__data_origin</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="p34393183194835"><a name="p34393183194835"></a><a name="p34393183194835"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p34384472194835"><a name="p34384472194835"></a><a name="p34384472194835"></a>Specifies the image resource.</p>
    <p id="p41024797194835"><a name="p41024797194835"></a><a name="p41024797194835"></a>If the image is a public image, this parameter is left empty.</p>
    </td>
    </tr>
    <tr id="row241695482710"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p3417155412277"><a name="p3417155412277"></a><a name="p3417155412277"></a>hw_firmware_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="p94173546271"><a name="p94173546271"></a><a name="p94173546271"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p1841725410273"><a name="p1841725410273"></a><a name="p1841725410273"></a>Specifies the <span id="text517213819114"><a name="text517213819114"></a><a name="text517213819114"></a></span><span id="text617310871112"><a name="text617310871112"></a><a name="text617310871112"></a>ECS</span> boot mode. The following values are supported:</p>
    <a name="ul149852572301"></a><a name="ul149852572301"></a><ul id="ul149852572301"><li><strong id="b21976546489"><a name="b21976546489"></a><a name="b21976546489"></a>bios</strong> indicates the BIOS boot mode.</li><li><strong id="b131713934914"><a name="b131713934914"></a><a name="b131713934914"></a>uefi</strong> indicates the UEFI boot mode.</li></ul>
    </td>
    </tr>
    <tr id="row1922712020747"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p1688848719937"><a name="p1688848719937"></a><a name="p1688848719937"></a>__support_kvm</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="p1314210319937"><a name="p1314210319937"></a><a name="p1314210319937"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p6435151319937"><a name="p6435151319937"></a><a name="p6435151319937"></a>Specifies whether the image supports KVM. If yes, the value is <strong id="b842352706174145"><a name="b842352706174145"></a><a name="b842352706174145"></a>true</strong>. Otherwise, this attribute is not required.</p>
    </td>
    </tr>
    <tr id="row2176677820925"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p4682508419937"><a name="p4682508419937"></a><a name="p4682508419937"></a>__support_xen</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="p2922074219937"><a name="p2922074219937"></a><a name="p2922074219937"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p5999426419937"><a name="p5999426419937"></a><a name="p5999426419937"></a>Specifies whether the image supports Xen. If yes, the value is <strong id="b40128715692258"><a name="b40128715692258"></a><a name="b40128715692258"></a>true</strong>. Otherwise, this attribute is not required.</p>
    </td>
    </tr>
    <tr id="row40128591201933"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p5564125819937"><a name="p5564125819937"></a><a name="p5564125819937"></a>__support_largememory</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="p3285048619937"><a name="p3285048619937"></a><a name="p3285048619937"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p14775155391313"><a name="p14775155391313"></a><a name="p14775155391313"></a>Specifies whether the image can be used to create large-memory ECSs. If the image supports large-memory ECSs, the value is <strong id="b4112171915415"><a name="b4112171915415"></a><a name="b4112171915415"></a>true</strong>. Otherwise, this attribute is not required.</p>
    <p id="p3197171053216"><a name="p3197171053216"></a><a name="p3197171053216"></a>For the supported OSs, see <a href="values-of-related-parameters.md#table48545918250">Table 3</a>.</p>
    <p id="p86725554217"><a name="p86725554217"></a><a name="p86725554217"></a></p>
    </td>
    </tr>
    <tr id="row27314678185940"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p5257634319937"><a name="p5257634319937"></a><a name="p5257634319937"></a>__support_diskintensive</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="p4365124719937"><a name="p4365124719937"></a><a name="p4365124719937"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p3727279719937"><a name="p3727279719937"></a><a name="p3727279719937"></a>Specifies whether the image can be used to create disk-intensive ECSs. If the image supports disk-intensive ECSs, the value is <strong id="b2025511543"><a name="b2025511543"></a><a name="b2025511543"></a>true</strong>. Otherwise, this attribute is not required.</p>
    </td>
    </tr>
    <tr id="row55915043185940"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p6005168719937"><a name="p6005168719937"></a><a name="p6005168719937"></a>__support_highperformance</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="p6702872519937"><a name="p6702872519937"></a><a name="p6702872519937"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p3306819319937"><a name="p3306819319937"></a><a name="p3306819319937"></a>Specifies whether the image can be used to create high-performance ECSs. If the image supports high-performance ECSs, the value is <strong id="b1321410424"><a name="b1321410424"></a><a name="b1321410424"></a>true</strong>. Otherwise, this attribute is not required.</p>
    </td>
    </tr>
    <tr id="row32822185940"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p1241378919937"><a name="p1241378919937"></a><a name="p1241378919937"></a>__support_xen_gpu_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="p3786179019937"><a name="p3786179019937"></a><a name="p3786179019937"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p5825807419937"><a name="p5825807419937"></a><a name="p5825807419937"></a>Specifies whether the image can be used to create GPU-optimized ECSs on the Xen platform. See <a href="values-of-related-parameters.md#table65768383152758">Table 2</a> for its value. If the image does not support GPU-optimized ECSs on the Xen platform, this attribute is not required. This attribute cannot co-exist with <strong id="b842352706175423"><a name="b842352706175423"></a><a name="b842352706175423"></a>__support_xen</strong> and <strong id="b842352706175430"><a name="b842352706175430"></a><a name="b842352706175430"></a>__support_kvm</strong>.</p>
    </td>
    </tr>
    <tr id="row11388758185940"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p4869692419937"><a name="p4869692419937"></a><a name="p4869692419937"></a>__support_kvm_gpu_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="p2602039619937"><a name="p2602039619937"></a><a name="p2602039619937"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p1297699219937"><a name="p1297699219937"></a><a name="p1297699219937"></a>Specifies whether the image supports GPU-optimized ECSs on the KVM platform. See <a href="values-of-related-parameters.md#table65768383152758">Table 2</a> for its value.</p>
    <p id="p1103263019937"><a name="p1103263019937"></a><a name="p1103263019937"></a>If the image does not support GPU-optimized ECSs on the KVM platform, this attribute is not required. This attribute cannot co-exist with <strong id="b2090041441"><a name="b2090041441"></a><a name="b2090041441"></a>__support_xen</strong> and <strong id="b147119975"><a name="b147119975"></a><a name="b147119975"></a>__support_kvm</strong>.</p>
    </td>
    </tr>
    <tr id="row1461958185940"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p6196955419937"><a name="p6196955419937"></a><a name="p6196955419937"></a>__support_xen_hana</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="p2663872719937"><a name="p2663872719937"></a><a name="p2663872719937"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p2469264919937"><a name="p2469264919937"></a><a name="p2469264919937"></a>Specifies whether the image supports HANA ECSs on the Xen platform. If yes, the value is <strong id="b1066553282174316"><a name="b1066553282174316"></a><a name="b1066553282174316"></a>true</strong>. Otherwise, this attribute is not required.</p>
    <p id="p1546130419937"><a name="p1546130419937"></a><a name="p1546130419937"></a>This attribute cannot co-exist with <strong id="b839921310"><a name="b839921310"></a><a name="b839921310"></a>__support_xen</strong> and <strong id="b345297505"><a name="b345297505"></a><a name="b345297505"></a>__support_kvm</strong>.</p>
    </td>
    </tr>
    <tr id="row1957610919416"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p3308936119937"><a name="p3308936119937"></a><a name="p3308936119937"></a>__support_kvm_infiniband</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.29%" headers="mcps1.1.4.1.2 "><p id="p1490599719937"><a name="p1490599719937"></a><a name="p1490599719937"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p3836423719937"><a name="p3836423719937"></a><a name="p3836423719937"></a>Specifies whether the image supports ECSs with the InfiniBand NIC on the KVM platform. If yes, the value is <strong id="b2040161919154726"><a name="b2040161919154726"></a><a name="b2040161919154726"></a>true</strong>. Otherwise, this attribute is not required.</p>
    <p id="p2430059519937"><a name="p2430059519937"></a><a name="p2430059519937"></a>This attribute cannot co-exist with <strong id="b1655636019"><a name="b1655636019"></a><a name="b1655636019"></a>__support_xen</strong>.</p>
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
        "file": "/v2/images/33ad552d-1149-471c-8190-ff6776174a00/file",
        "owner": "0b1e494e2660441a957313163095fe5c",
        "id": "33ad552d-1149-471c-8190-ff6776174a00",
        "size": 2,
        "self": "/v2/images/33ad552d-1149-471c-8190-ff6776174a00",
        "schema": "/v2/schemas/image",
        "status": "active",
        "tags": [],
        "visibility": "private",
        "name": "ims_test",
        "checksum": "99914b932bd37a50b983c5e7c90ae93b",
        "deleted": false,
        "protected": false,
        "container_format": "bare",
        "min_ram": 0,
        "updated_at": "2015-12-08T02:30:49Z",
        "__os_bit": "64",
        "__os_version": "Ubuntu 14.04 server 64bit",
        "__description": "ims test",
        "disk_format": "vhd",
        "__isregistered": "true",
        "__platform": "Ubuntu",
        "__os_type": "Linux",
        "min_disk": 40,
        "virtual_env_type": "FusionCompute",
        "__image_source_type": "uds",
        "__imagetype": "private",
        "created_at": "2015-12-04T09:45:33Z",
        "virtual_size": 0,
        "deleted_at": null,
        "__originalimagename": "33ad552d-1149-471c-8190-ff6776174a00",
        "__backup_id": "",
        "__productcode": "",
        "__image_size": "449261568",
        "__data_origin": null,
        "hw_firmware_type":"bios"
    }
    ```


## Returned Value<a name="section43084165"></a>

-   Normal

    200

-   Abnormal

    <a name="table2933833017254"></a>
    <table><thead align="left"><tr id="row5083298917254"><th class="cellrowborder" valign="top" width="46.54%" id="mcps1.1.3.1.1"><p id="p2383143117254"><a name="p2383143117254"></a><a name="p2383143117254"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.459999999999994%" id="mcps1.1.3.1.2"><p id="p5129777817254"><a name="p5129777817254"></a><a name="p5129777817254"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6147936617254"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p1377271317254"><a name="p1377271317254"></a><a name="p1377271317254"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p4184800617254"><a name="p4184800617254"></a><a name="p4184800617254"></a>Request error. For details about the returned error code, see <a href="error-codes.md">Error Codes</a>.</p>
    </td>
    </tr>
    <tr id="row3424531517254"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p2240711217254"><a name="p2240711217254"></a><a name="p2240711217254"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p303679817254"><a name="p303679817254"></a><a name="p303679817254"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row2733118717254"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p6634251617254"><a name="p6634251617254"></a><a name="p6634251617254"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p503474717254"><a name="p503474717254"></a><a name="p503474717254"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="row48054866192311"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p47142447192313"><a name="p47142447192313"></a><a name="p47142447192313"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p60441878192313"><a name="p60441878192313"></a><a name="p60441878192313"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="row4531272317254"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p4645193117254"><a name="p4645193117254"></a><a name="p4645193117254"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p451004317254"><a name="p451004317254"></a><a name="p451004317254"></a>Internal service error.</p>
    </td>
    </tr>
    <tr id="row4059039217254"><td class="cellrowborder" valign="top" width="46.54%" headers="mcps1.1.3.1.1 "><p id="p6659632017254"><a name="p6659632017254"></a><a name="p6659632017254"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.459999999999994%" headers="mcps1.1.3.1.2 "><p id="p2559285317254"><a name="p2559285317254"></a><a name="p2559285317254"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>



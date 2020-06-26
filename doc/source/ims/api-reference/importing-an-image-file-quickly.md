# Importing an Image File Quickly<a name="EN-US_TOPIC_0133188204"></a>

## Function<a name="section1194520316464"></a>

This API is used to quickly create a private image from an oversized external image file that has uploaded to the OBS bucket. Currently, only ZVHD2 and RAW image files are supported, and the size of image files cannot exceed 1 TB.

The fast image creation function is only available for image files in RAW or ZVHD2 format. For other formats of image files that are smaller than 128 GB, you are advised to import these files with the common method.

The API is an asynchronous one. If it is successfully called, the cloud service system receives the request. However, you need to use the asynchronous job query API to query the image creation status. For details, see  [Asynchronous Job Query](asynchronous-job-query.md).

## Constraints<a name="section244817584484"></a>

Before importing image files, ensure that the file format is RAW or ZVHD2 and the following have been done:

-   RAW image files have been optimized, and bitmap files have been generated.
-   ZVHD2 image files have been optimized as required.

>![](/images/icon-note.gif) **NOTE:**   
>For how to convert image file formats and generate a bitmap file, see section "Quickly Importing an Image File" in the  _Image Management Service User Guide_.  

## URI<a name="section1594513117469"></a>

POST /v2/cloudimages/quickimport/action

## Request<a name="section1394517316467"></a>

-   Parameters in the request body when an image file is used to create a system disk image

    <a name="table1996117311464"></a>
    <table><thead align="left"><tr id="row230533204615"><th class="cellrowborder" valign="top" width="23.23232323232323%" id="mcps1.1.5.1.1"><p id="p13051332144610"><a name="p13051332144610"></a><a name="p13051332144610"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.16161616161616%" id="mcps1.1.5.1.2"><p id="p1630520329462"><a name="p1630520329462"></a><a name="p1630520329462"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.2020202020202%" id="mcps1.1.5.1.3"><p id="p5305332184616"><a name="p5305332184616"></a><a name="p5305332184616"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="40.4040404040404%" id="mcps1.1.5.1.4"><p id="p73056327467"><a name="p73056327467"></a><a name="p73056327467"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row430593218463"><td class="cellrowborder" valign="top" width="23.23232323232323%" headers="mcps1.1.5.1.1 "><p id="p330543210463"><a name="p330543210463"></a><a name="p330543210463"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.2 "><p id="p1630553264617"><a name="p1630553264617"></a><a name="p1630553264617"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.2020202020202%" headers="mcps1.1.5.1.3 "><p id="p3305932144610"><a name="p3305932144610"></a><a name="p3305932144610"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.4040404040404%" headers="mcps1.1.5.1.4 "><p id="p1551018218225"><a name="p1551018218225"></a><a name="p1551018218225"></a>Specifies the image name.</p>
    <p id="p630510326467"><a name="p630510326467"></a><a name="p630510326467"></a>For detailed description, see <a href="image-attributes.md">Image Attributes</a>.</p>
    </td>
    </tr>
    <tr id="row130503284613"><td class="cellrowborder" valign="top" width="23.23232323232323%" headers="mcps1.1.5.1.1 "><p id="p73051932154620"><a name="p73051932154620"></a><a name="p73051932154620"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.2 "><p id="p1430513324463"><a name="p1430513324463"></a><a name="p1430513324463"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.2020202020202%" headers="mcps1.1.5.1.3 "><p id="p6305732154618"><a name="p6305732154618"></a><a name="p6305732154618"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.4040404040404%" headers="mcps1.1.5.1.4 "><p id="p16554109232"><a name="p16554109232"></a><a name="p16554109232"></a>Provides supplementary information about the image.</p>
    <p id="p14983181319239"><a name="p14983181319239"></a><a name="p14983181319239"></a>For detailed description, see <a href="image-attributes.md">Image Attributes</a>.</p>
    <p id="p1230533224616"><a name="p1230533224616"></a><a name="p1230533224616"></a>The value contains a maximum of 1024 characters and consists of only letters and digits. Carriage returns and angle brackets (&lt; &gt;) are not allowed. This parameter is left blank by default.</p>
    </td>
    </tr>
    <tr id="row143051632144610"><td class="cellrowborder" valign="top" width="23.23232323232323%" headers="mcps1.1.5.1.1 "><p id="p18305432174611"><a name="p18305432174611"></a><a name="p18305432174611"></a>os_version</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.2 "><p id="p123051332104613"><a name="p123051332104613"></a><a name="p123051332104613"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.2020202020202%" headers="mcps1.1.5.1.3 "><p id="p14305183244611"><a name="p14305183244611"></a><a name="p14305183244611"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.4040404040404%" headers="mcps1.1.5.1.4 "><p id="p5305203217468"><a name="p5305203217468"></a><a name="p5305203217468"></a>Specifies the OS version.</p>
    <p id="p430583213464"><a name="p430583213464"></a><a name="p430583213464"></a>This parameter is valid if an external image file uploaded to the OBS bucket is used to create an image. For its value, see <a href="values-of-related-parameters.md">Values of Related Parameters</a>.</p>
    </td>
    </tr>
    <tr id="row93058325464"><td class="cellrowborder" valign="top" width="23.23232323232323%" headers="mcps1.1.5.1.1 "><p id="p103058329463"><a name="p103058329463"></a><a name="p103058329463"></a>image_url</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.2 "><p id="p630533211465"><a name="p630533211465"></a><a name="p630533211465"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.2020202020202%" headers="mcps1.1.5.1.3 "><p id="p1630593294615"><a name="p1630593294615"></a><a name="p1630593294615"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.4040404040404%" headers="mcps1.1.5.1.4 "><p id="p1230517327465"><a name="p1230517327465"></a><a name="p1230517327465"></a>Specifies the URL of the external image file in the OBS bucket.</p>
    <p id="p03051832114620"><a name="p03051832114620"></a><a name="p03051832114620"></a>This parameter is mandatory if an external image file in the OBS bucket is used to create an image. The format is <em id="i84235269710218"><a name="i84235269710218"></a><a name="i84235269710218"></a>OBS bucket name</em>:<em id="i84235269710226"><a name="i84235269710226"></a><a name="i84235269710226"></a>Image file name</em>.</p>
    <div class="notice" id="note3992231124619"><a name="note3992231124619"></a><a name="note3992231124619"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><p id="p030515329463"><a name="p030515329463"></a><a name="p030515329463"></a>The storage class of the OBS bucket must be <strong id="b84235270695634"><a name="b84235270695634"></a><a name="b84235270695634"></a>Standard</strong>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row730573215467"><td class="cellrowborder" valign="top" width="23.23232323232323%" headers="mcps1.1.5.1.1 "><p id="p1430593274613"><a name="p1430593274613"></a><a name="p1430593274613"></a>min_disk</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.2 "><p id="p4305193224619"><a name="p4305193224619"></a><a name="p4305193224619"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.2020202020202%" headers="mcps1.1.5.1.3 "><p id="p2305632134614"><a name="p2305632134614"></a><a name="p2305632134614"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.4040404040404%" headers="mcps1.1.5.1.4 "><p id="p143051632104617"><a name="p143051632104617"></a><a name="p143051632104617"></a>Specifies the minimum size (GB) of the system disk.</p>
    <a name="ul2568215149"></a><a name="ul2568215149"></a><ul id="ul2568215149"><li>This parameter is mandatory if an external image file in the OBS bucket is used to create an image.</li><li>The value ranges from 1 to 1024 and must be greater than the size of the selected image file.</li></ul>
    </td>
    </tr>
    <tr id="row16305113220466"><td class="cellrowborder" valign="top" width="23.23232323232323%" headers="mcps1.1.5.1.1 "><p id="p1730583214460"><a name="p1730583214460"></a><a name="p1730583214460"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.2 "><p id="p1230510329468"><a name="p1230510329468"></a><a name="p1230510329468"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.2020202020202%" headers="mcps1.1.5.1.3 "><p id="p13058328463"><a name="p13058328463"></a><a name="p13058328463"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.4040404040404%" headers="mcps1.1.5.1.4 "><p id="p10305732164620"><a name="p10305732164620"></a><a name="p10305732164620"></a>Lists the image tags. This parameter is left blank by default.</p>
    <p id="p3106162222815"><a name="p3106162222815"></a><a name="p3106162222815"></a>Set either <strong id="b68022071419"><a name="b68022071419"></a><a name="b68022071419"></a>tags</strong> or <strong id="b17807204145"><a name="b17807204145"></a><a name="b17807204145"></a>image_tags</strong>.</p>
    </td>
    </tr>
    <tr id="row1259121152812"><td class="cellrowborder" valign="top" width="23.23232323232323%" headers="mcps1.1.5.1.1 "><p id="p21354848113521"><a name="p21354848113521"></a><a name="p21354848113521"></a>image_tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.2 "><p id="p29922489113521"><a name="p29922489113521"></a><a name="p29922489113521"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.2020202020202%" headers="mcps1.1.5.1.3 "><p id="p56528150113521"><a name="p56528150113521"></a><a name="p56528150113521"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.4040404040404%" headers="mcps1.1.5.1.4 "><p id="p58098807113521"><a name="p58098807113521"></a><a name="p58098807113521"></a>Lists the image tags. The value is left blank by default.</p>
    <p id="p19190125113278"><a name="p19190125113278"></a><a name="p19190125113278"></a>Set either <strong id="b64491227181417"><a name="b64491227181417"></a><a name="b64491227181417"></a>tags</strong> or <strong id="b5450172718146"><a name="b5450172718146"></a><a name="b5450172718146"></a>image_tags</strong>.</p>
    </td>
    </tr>
    <tr id="row1330510320467"><td class="cellrowborder" valign="top" width="23.23232323232323%" headers="mcps1.1.5.1.1 "><p id="p12305193254612"><a name="p12305193254612"></a><a name="p12305193254612"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.2 "><p id="p430514323464"><a name="p430514323464"></a><a name="p430514323464"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.2020202020202%" headers="mcps1.1.5.1.3 "><p id="p13305183212463"><a name="p13305183212463"></a><a name="p13305183212463"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.4040404040404%" headers="mcps1.1.5.1.4 "><p id="p14305832164616"><a name="p14305832164616"></a><a name="p14305832164616"></a>Specifies the image type. The parameter value is ECS/BMS for system disk images. The default value is <strong id="b842352706161934"><a name="b842352706161934"></a><a name="b842352706161934"></a>ECS</strong>.</p>
    </td>
    </tr>
    <tr id="row134361944974"><td class="cellrowborder" valign="top" width="23.23232323232323%" headers="mcps1.1.5.1.1 "><p id="p1531631810"><a name="p1531631810"></a><a name="p1531631810"></a>architecture</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.2 "><p id="p35316311810"><a name="p35316311810"></a><a name="p35316311810"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.2020202020202%" headers="mcps1.1.5.1.3 "><p id="p15318311813"><a name="p15318311813"></a><a name="p15318311813"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.4040404040404%" headers="mcps1.1.5.1.4 "><p id="p1710991214517"><a name="p1710991214517"></a><a name="p1710991214517"></a>Specifies the image architecture type. Available values include:</p>
    <a name="ul12299918656"></a><a name="ul12299918656"></a><ul id="ul12299918656"><li>x86</li><li>arm</li></ul>
    <p id="p186813286510"><a name="p186813286510"></a><a name="p186813286510"></a>The default value is <strong id="b1460217264193"><a name="b1460217264193"></a><a name="b1460217264193"></a>x86</strong>.</p>
    <div class="note" id="note4599194110418"><a name="note4599194110418"></a><a name="note4599194110418"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p892691311810"><a name="p892691311810"></a><a name="p892691311810"></a>If the image architecture is ARM, the boot mode is automatically changed to UEFI.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameters description when an image file uploaded to the OBS bucket is used to create an image

    <a name="table399233124619"></a>
    <table><thead align="left"><tr id="row163059328462"><th class="cellrowborder" valign="top" width="23.23232323232323%" id="mcps1.1.5.1.1"><p id="p13058328466"><a name="p13058328466"></a><a name="p13058328466"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.16161616161616%" id="mcps1.1.5.1.2"><p id="p130523214617"><a name="p130523214617"></a><a name="p130523214617"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.2020202020202%" id="mcps1.1.5.1.3"><p id="p8305103212461"><a name="p8305103212461"></a><a name="p8305103212461"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="40.4040404040404%" id="mcps1.1.5.1.4"><p id="p1830563214461"><a name="p1830563214461"></a><a name="p1830563214461"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row83058326463"><td class="cellrowborder" valign="top" width="23.23232323232323%" headers="mcps1.1.5.1.1 "><p id="p3305173214616"><a name="p3305173214616"></a><a name="p3305173214616"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.2 "><p id="p53052032114616"><a name="p53052032114616"></a><a name="p53052032114616"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.2020202020202%" headers="mcps1.1.5.1.3 "><p id="p630543214610"><a name="p630543214610"></a><a name="p630543214610"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.4040404040404%" headers="mcps1.1.5.1.4 "><p id="p3305203234614"><a name="p3305203234614"></a><a name="p3305203234614"></a>Specifies the image name. For detailed description, see <a href="image-attributes.md">Image Attributes</a>.</p>
    </td>
    </tr>
    <tr id="row73051332174618"><td class="cellrowborder" valign="top" width="23.23232323232323%" headers="mcps1.1.5.1.1 "><p id="p1230503213462"><a name="p1230503213462"></a><a name="p1230503213462"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.2 "><p id="p1230513211468"><a name="p1230513211468"></a><a name="p1230513211468"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.2020202020202%" headers="mcps1.1.5.1.3 "><p id="p18305532154612"><a name="p18305532154612"></a><a name="p18305532154612"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.4040404040404%" headers="mcps1.1.5.1.4 "><p id="p1630515328463"><a name="p1630515328463"></a><a name="p1630515328463"></a>Provides supplementary information about the image. For detailed description, see <a href="image-attributes.md">Image Attributes</a>. The value contains a maximum of 1024 characters and consists of only letters and digits. Carriage returns and angle brackets (&lt; &gt;) are not allowed. This parameter is left blank by default.</p>
    </td>
    </tr>
    <tr id="row830510326469"><td class="cellrowborder" valign="top" width="23.23232323232323%" headers="mcps1.1.5.1.1 "><p id="p113057324467"><a name="p113057324467"></a><a name="p113057324467"></a>os_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.2 "><p id="p1130553284618"><a name="p1130553284618"></a><a name="p1130553284618"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.2020202020202%" headers="mcps1.1.5.1.3 "><p id="p143052324463"><a name="p143052324463"></a><a name="p143052324463"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.4040404040404%" headers="mcps1.1.5.1.4 "><p id="p183051732184612"><a name="p183051732184612"></a><a name="p183051732184612"></a>Specifies the OS version.</p>
    <p id="p1230518329464"><a name="p1230518329464"></a><a name="p1230518329464"></a>This parameter is used when a data disk image is to be created. The value can be <strong id="b84235270691525"><a name="b84235270691525"></a><a name="b84235270691525"></a>Linux</strong> or <strong id="b84235270691528"><a name="b84235270691528"></a><a name="b84235270691528"></a>Windows</strong>.</p>
    </td>
    </tr>
    <tr id="row1330519329465"><td class="cellrowborder" valign="top" width="23.23232323232323%" headers="mcps1.1.5.1.1 "><p id="p630533264610"><a name="p630533264610"></a><a name="p630533264610"></a>image_url</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.2 "><p id="p1130553244617"><a name="p1130553244617"></a><a name="p1130553244617"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.2020202020202%" headers="mcps1.1.5.1.3 "><p id="p14305123218469"><a name="p14305123218469"></a><a name="p14305123218469"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.4040404040404%" headers="mcps1.1.5.1.4 "><p id="p1830573213469"><a name="p1830573213469"></a><a name="p1830573213469"></a>Specifies the URL of the external image file in the OBS bucket.</p>
    <p id="p73051322460"><a name="p73051322460"></a><a name="p73051322460"></a>This parameter is mandatory if an external image file in the OBS bucket is used to create an image. The format is <em id="i84235269710445"><a name="i84235269710445"></a><a name="i84235269710445"></a>OBS bucket name</em>:<em id="i84235269710449"><a name="i84235269710449"></a><a name="i84235269710449"></a>Image file name</em>.</p>
    <div class="notice" id="note12812320467"><a name="note12812320467"></a><a name="note12812320467"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><p id="p7305173294619"><a name="p7305173294619"></a><a name="p7305173294619"></a>The storage class of the OBS bucket must be <strong id="b1576401798"><a name="b1576401798"></a><a name="b1576401798"></a>Standard</strong>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row73059326469"><td class="cellrowborder" valign="top" width="23.23232323232323%" headers="mcps1.1.5.1.1 "><p id="p2030533214463"><a name="p2030533214463"></a><a name="p2030533214463"></a>min_disk</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.2 "><p id="p19305123212467"><a name="p19305123212467"></a><a name="p19305123212467"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.2020202020202%" headers="mcps1.1.5.1.3 "><p id="p193051332114620"><a name="p193051332114620"></a><a name="p193051332114620"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.4040404040404%" headers="mcps1.1.5.1.4 "><p id="p130513264618"><a name="p130513264618"></a><a name="p130513264618"></a>Specifies the minimum size of the system disk in the unit of GB.</p>
    <p id="p15305173217466"><a name="p15305173217466"></a><a name="p15305173217466"></a>This parameter is mandatory if an external image file in the OBS bucket is used to create an image. The value ranges from 1 to 1024.</p>
    </td>
    </tr>
    <tr id="row430516321463"><td class="cellrowborder" valign="top" width="23.23232323232323%" headers="mcps1.1.5.1.1 "><p id="p130523212468"><a name="p130523212468"></a><a name="p130523212468"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.2 "><p id="p830512325469"><a name="p830512325469"></a><a name="p830512325469"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.2020202020202%" headers="mcps1.1.5.1.3 "><p id="p1430514322463"><a name="p1430514322463"></a><a name="p1430514322463"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.4040404040404%" headers="mcps1.1.5.1.4 "><p id="p1830518323464"><a name="p1830518323464"></a><a name="p1830518323464"></a>Lists the image tags. This parameter is left blank by default.</p>
    <p id="p1879112459285"><a name="p1879112459285"></a><a name="p1879112459285"></a>Set either <strong id="b8662228161411"><a name="b8662228161411"></a><a name="b8662228161411"></a>tags</strong> or <strong id="b5663328171414"><a name="b5663328171414"></a><a name="b5663328171414"></a>image_tags</strong>.</p>
    </td>
    </tr>
    <tr id="row1874183652819"><td class="cellrowborder" valign="top" width="23.23232323232323%" headers="mcps1.1.5.1.1 "><p id="p182233972817"><a name="p182233972817"></a><a name="p182233972817"></a>image_tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.2 "><p id="p52233962817"><a name="p52233962817"></a><a name="p52233962817"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.2020202020202%" headers="mcps1.1.5.1.3 "><p id="p72273910288"><a name="p72273910288"></a><a name="p72273910288"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.4040404040404%" headers="mcps1.1.5.1.4 "><p id="p622153910286"><a name="p622153910286"></a><a name="p622153910286"></a>Lists the image tags. The value is left blank by default.</p>
    <p id="p1222113913288"><a name="p1222113913288"></a><a name="p1222113913288"></a>Set either <strong id="b21235334146"><a name="b21235334146"></a><a name="b21235334146"></a>tags</strong> or <strong id="b17123833111414"><a name="b17123833111414"></a><a name="b17123833111414"></a>image_tags</strong>.</p>
    </td>
    </tr>
    <tr id="row173051332174611"><td class="cellrowborder" valign="top" width="23.23232323232323%" headers="mcps1.1.5.1.1 "><p id="p630519326463"><a name="p630519326463"></a><a name="p630519326463"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.16161616161616%" headers="mcps1.1.5.1.2 "><p id="p1430523210469"><a name="p1430523210469"></a><a name="p1430523210469"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.2020202020202%" headers="mcps1.1.5.1.3 "><p id="p13305132164618"><a name="p13305132164618"></a><a name="p13305132164618"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="40.4040404040404%" headers="mcps1.1.5.1.4 "><p id="p830513320465"><a name="p830513320465"></a><a name="p830513320465"></a>Specifies the image type. The parameter value is DataImage for data disk images.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example requests
    -   Creating a system disk image using an external image file

        ```
        POST https://{Endpoint}/v2/cloudimages/quickimport/action
        ```

        If parameter  **tags**  is used:

        ```
        {  
            "name": "ims_test_file",  
           "description": "Create an image using a file in the OBS bucket.", 
            "image_url": "ims-image:centos70.zvhd2",  
            "os_version": "CentOS 7.0 64bit",  
            "min_disk": 40,  
            "type": "ECS", 
            "tags":
                [
                    "aaa.111",    
                    "bbb.333",    
                    "ccc.444"    
                ]
        }
        ```

        If parameter  **image\_tags**  is used:

        ```
        {  
            "name": "ims_test_file",  
           "description": "Create an image using a file in the OBS bucket.", 
            "image_url": "ims-image:centos70.zvhd2",  
            "os_version": "CentOS 7.0 64bit",  
            "min_disk": 40,  
            "type": "ECS", 
            "image_tags": [{"key":"key2","value":"value2"},{"key":"key1","value":"value1"}]  
        }
        ```

    -   Creating a data disk image using an external image file

        ```
        POST https://{Endpoint}/v2/cloudimages/quickimport/action
        ```

        If parameter  **tags**  is used:

        ```
        {  
            "name": "ims_test_file",  
           "description": "Create an image using a file in the OBS bucket.", 
            "image_url": "ims-image:centos70.qcow2",  
            "os_type": "Linux",  
            "min_disk": 40,  
            "type": "DataImage",  
            "tags": [    
                "aaa.111",    
                "bbb.333",    
                "ccc.444"    
            ]
        }
        ```

        If parameter  **image\_tags**  is used:

        ```
        {  
            "name": "ims_test_file",  
           "description": "Create an image using a file in the OBS bucket.", 
            "image_url": "ims-image:centos70.qcow2",  
            "os_type": "Linux",  
            "min_disk": 40,  
            "type": "DataImage",
            "image_tags": [{"key":"key2","value":"value2"},{"key":"key1","value":"value1"}]
        }
        ```



## Response<a name="section639632154617"></a>

-   Response parameters

    <a name="table139163294618"></a>
    <table><thead align="left"><tr id="row103054322469"><th class="cellrowborder" valign="top" width="23.68%" id="mcps1.1.4.1.1"><p id="p43051732184618"><a name="p43051732184618"></a><a name="p43051732184618"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.74%" id="mcps1.1.4.1.2"><p id="p113051332184618"><a name="p113051332184618"></a><a name="p113051332184618"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.58%" id="mcps1.1.4.1.3"><p id="p23051732124619"><a name="p23051732124619"></a><a name="p23051732124619"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row83051832144620"><td class="cellrowborder" valign="top" width="23.68%" headers="mcps1.1.4.1.1 "><p id="p730511328463"><a name="p730511328463"></a><a name="p730511328463"></a>job_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.1.4.1.2 "><p id="p15305163211465"><a name="p15305163211465"></a><a name="p15305163211465"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.4.1.3 "><p id="p130583216466"><a name="p130583216466"></a><a name="p130583216466"></a>Specifies the asynchronous job ID.</p>
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
         "job_id": "8a12fc664fb4daa3014fb4e581380005"
    }
    ```


## Returned Values<a name="section539103214611"></a>

-   Normal

    200

-   Abnormal

    <a name="table53911327463"></a>
    <table><thead align="left"><tr id="row11305143214468"><th class="cellrowborder" valign="top" width="46.46%" id="mcps1.1.3.1.1"><p id="p63051132164612"><a name="p63051132164612"></a><a name="p63051132164612"></a>Return Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.54%" id="mcps1.1.3.1.2"><p id="p133051932194617"><a name="p133051932194617"></a><a name="p133051932194617"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row11305133204615"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p13305143220466"><a name="p13305143220466"></a><a name="p13305143220466"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p17305203244617"><a name="p17305203244617"></a><a name="p17305203244617"></a>Request error. For details about the returned error code, see <a href="error-codes.md">Error Codes</a>.</p>
    </td>
    </tr>
    <tr id="row1130593211466"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p16305183274616"><a name="p16305183274616"></a><a name="p16305183274616"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p19305532164619"><a name="p19305532164619"></a><a name="p19305532164619"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row43051832104610"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p113057325469"><a name="p113057325469"></a><a name="p113057325469"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p12305153214469"><a name="p12305153214469"></a><a name="p12305153214469"></a>You do not have the rights to perform the operation.</p>
    </td>
    </tr>
    <tr id="row23051532194620"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p1230553210462"><a name="p1230553210462"></a><a name="p1230553210462"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p9305432184614"><a name="p9305432184614"></a><a name="p9305432184614"></a>The requested resource was not found.</p>
    </td>
    </tr>
    <tr id="row1305132104618"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p183056324469"><a name="p183056324469"></a><a name="p183056324469"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p730533294620"><a name="p730533294620"></a><a name="p730533294620"></a>Internal service error.</p>
    </td>
    </tr>
    <tr id="row1730513326464"><td class="cellrowborder" valign="top" width="46.46%" headers="mcps1.1.3.1.1 "><p id="p6305153284615"><a name="p6305153284615"></a><a name="p6305153284615"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.54%" headers="mcps1.1.3.1.2 "><p id="p6305133284616"><a name="p6305133284616"></a><a name="p6305133284616"></a>The service is unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>



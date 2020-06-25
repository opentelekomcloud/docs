# Registering an External Image File as a Private Image<a name="EN-US_TOPIC_0030713184"></a>

## Scenarios<a name="section717820315503"></a>

This section describes how to register an image file uploaded to the OBS bucket as a private image.

## Procedure<a name="section1753510552356"></a>

1.  Log in to the management console.
2.  Under  **Computing**, click  **Image Management Service**.

    The IMS console is displayed.

3.  In the upper right corner, click** Create Image**  and set the following parameters:

    [Table 1](#table050019474117)  and  [Table 2](#table6978715749)  list the parameters in the  **Image Type and Source**  and  **Image Information**  areas, respectively.

    **Table  1**  Image Type and Source

    <a name="table050019474117"></a>
    <table><thead align="left"><tr id="row1350164712110"><th class="cellrowborder" valign="top" width="25.96%" id="mcps1.2.3.1.1"><p id="p12501447314"><a name="p12501447314"></a><a name="p12501447314"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="74.03999999999999%" id="mcps1.2.3.1.2"><p id="p1350114720117"><a name="p1350114720117"></a><a name="p1350114720117"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row350214713113"><td class="cellrowborder" valign="top" width="25.96%" headers="mcps1.2.3.1.1 "><p id="p650294716116"><a name="p650294716116"></a><a name="p650294716116"></a>Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="74.03999999999999%" headers="mcps1.2.3.1.2 "><p id="p75021947615"><a name="p75021947615"></a><a name="p75021947615"></a>Select <strong id="b126662048155215"><a name="b126662048155215"></a><a name="b126662048155215"></a>System disk image</strong>.</p>
    </td>
    </tr>
    <tr id="row1650284720113"><td class="cellrowborder" valign="top" width="25.96%" headers="mcps1.2.3.1.1 "><p id="p125022471113"><a name="p125022471113"></a><a name="p125022471113"></a>Source</p>
    </td>
    <td class="cellrowborder" valign="top" width="74.03999999999999%" headers="mcps1.2.3.1.2 "><p id="p850214712118"><a name="p850214712118"></a><a name="p850214712118"></a>Select <strong id="b842352706205833"><a name="b842352706205833"></a><a name="b842352706205833"></a>Image File</strong> for <strong id="b842352706205830"><a name="b842352706205830"></a><a name="b842352706205830"></a>Source</strong>. Select the bucket storing the image file from the list and then select the image file.</p>
    </td>
    </tr>
    <tr id="row19047191220"><td class="cellrowborder" valign="top" width="25.96%" headers="mcps1.2.3.1.1 "><p id="p690516194212"><a name="p690516194212"></a><a name="p690516194212"></a>Fast Create</p>
    </td>
    <td class="cellrowborder" valign="top" width="74.03999999999999%" headers="mcps1.2.3.1.2 "><p id="p1139533015529"><a name="p1139533015529"></a><a name="p1139533015529"></a>This parameter is available only when you upload a ZVHD2 or RAW image file.</p>
    <p id="p690516196213"><a name="p690516196213"></a><a name="p690516196213"></a>This function enables fast image creation and supports import of files as large as 1 TB on condition that the files to be uploaded must be converted to the ZVHD2 or RAW format and optimized. If you have a file that meets the requirements, select <strong id="b25354261597"><a name="b25354261597"></a><a name="b25354261597"></a>Enable Fast Create</strong> and select the confirmation information following <strong id="b7626371717"><a name="b7626371717"></a><a name="b7626371717"></a>Image File Preparation</strong>.</p>
    <div class="note" id="note189513537562"><a name="note189513537562"></a><a name="note189513537562"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p9951353185614"><a name="p9951353185614"></a><a name="p9951353185614"></a>For how to convert image file formats and generate bitmap files, see <a href="quickly-importing-an-image-file.md">Quickly Importing an Image File</a>.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  Image Information

    <a name="table6978715749"></a>
    <table><thead align="left"><tr id="row1597918159415"><th class="cellrowborder" valign="top" width="25.91%" id="mcps1.2.3.1.1"><p id="p597916152418"><a name="p597916152418"></a><a name="p597916152418"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="74.09%" id="mcps1.2.3.1.2"><p id="p99796151642"><a name="p99796151642"></a><a name="p99796151642"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2979615646"><td class="cellrowborder" valign="top" width="25.91%" headers="mcps1.2.3.1.1 "><p id="p119791415146"><a name="p119791415146"></a><a name="p119791415146"></a>Enable automatic configuration</p>
    </td>
    <td class="cellrowborder" valign="top" width="74.09%" headers="mcps1.2.3.1.2 "><p id="p159799151641"><a name="p159799151641"></a><a name="p159799151641"></a>If you select this option, the system will automatically check and optimize the image file. For details, see <a href="what-changes-will-be-made-to-an-image-file-used-for-registering-a-private-image.md">What Changes Will Be Made to an Image File Used for Registering a Private Image?</a></p>
    </td>
    </tr>
    <tr id="row1597941514412"><td class="cellrowborder" valign="top" width="25.91%" headers="mcps1.2.3.1.1 "><p id="p49796159415"><a name="p49796159415"></a><a name="p49796159415"></a>Function</p>
    </td>
    <td class="cellrowborder" valign="top" width="74.09%" headers="mcps1.2.3.1.2 "><p id="p19791151244"><a name="p19791151244"></a><a name="p19791151244"></a>Specifies whether the image is used to create ECSs or BMSs. The value can be <strong id="b8112182221317"><a name="b8112182221317"></a><a name="b8112182221317"></a>ECS system disk image</strong> or <strong id="b1374314358135"><a name="b1374314358135"></a><a name="b1374314358135"></a>BMS system disk image</strong>. This section uses <strong id="b16721555131317"><a name="b16721555131317"></a><a name="b16721555131317"></a>ECS system disk image</strong> as an example.</p>
    </td>
    </tr>
    <tr id="row5979161520418"><td class="cellrowborder" valign="top" width="25.91%" headers="mcps1.2.3.1.1 "><p id="p397920159413"><a name="p397920159413"></a><a name="p397920159413"></a>OS</p>
    </td>
    <td class="cellrowborder" valign="top" width="74.09%" headers="mcps1.2.3.1.2 "><p id="p13980151519417"><a name="p13980151519417"></a><a name="p13980151519417"></a>To ensure that the image can be created and used properly, select an OS consistent with that in the image file. If you do not select an OS, the system automatically identifies the OS in the image file.</p>
    <div class="note" id="note1083205331415"><a name="note1083205331415"></a><a name="note1083205331415"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul183081759171412"></a><a name="ul183081759171412"></a><ul id="ul183081759171412"><li>If the system detects that the image file OS is different from the one you selected, the OS detected by the system will prevail.</li><li>If the system cannot detect the OS in the image file, the OS you selected will prevail.</li><li>If the OS you selected or identified by the system is inconsistent with the actual one, <span id="text94741046125720"><a name="text94741046125720"></a><a name="text94741046125720"></a>ECS</span><span id="text941354825714"><a name="text941354825714"></a><a name="text941354825714"></a></span>s created from the image file may be affected.</li></ul>
    </div></div>
    </td>
    </tr>
    <tr id="row186599521354"><td class="cellrowborder" valign="top" width="25.91%" headers="mcps1.2.3.1.1 "><p id="p5659125219510"><a name="p5659125219510"></a><a name="p5659125219510"></a>System Disk (GB)</p>
    </td>
    <td class="cellrowborder" valign="top" width="74.09%" headers="mcps1.2.3.1.2 "><p id="p165912527520"><a name="p165912527520"></a><a name="p165912527520"></a>Specifies the system disk capacity. Ensure that the value is greater than or equal to the system disk size in the source image file.</p>
    <div class="note" id="note106387506495"><a name="note106387506495"></a><a name="note106387506495"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p263819508495"><a name="p263819508495"></a><a name="p263819508495"></a>If the uploaded VHD image is generated using qemu-img or similar tools, check the system disk size based on <a href="why-does-the-error-message-displayed-on-task-center-indicates-that-the-system-disk-size-of-the-exter.md">Why Does the Error Message Displayed on Task Center Indicates That the System Disk Size of the External Image File Exceeds the Maximum System Disk Size When a VHD Image File Failed to Be Uploaded?</a></p>
    </div></div>
    </td>
    </tr>
    <tr id="row36593522511"><td class="cellrowborder" valign="top" width="25.91%" headers="mcps1.2.3.1.1 "><p id="p19659452051"><a name="p19659452051"></a><a name="p19659452051"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="74.09%" headers="mcps1.2.3.1.2 "><p id="p126597521359"><a name="p126597521359"></a><a name="p126597521359"></a>Set a name for the image.</p>
    </td>
    </tr>
    <tr id="row66596520512"><td class="cellrowborder" valign="top" width="25.91%" headers="mcps1.2.3.1.1 "><p id="p156591952159"><a name="p156591952159"></a><a name="p156591952159"></a>Encryption</p>
    </td>
    <td class="cellrowborder" valign="top" width="74.09%" headers="mcps1.2.3.1.2 "><p id="p936015584547"><a name="p936015584547"></a><a name="p936015584547"></a>(Optional) If you want to encrypt the image, select <strong id="b842352706112959"><a name="b842352706112959"></a><a name="b842352706112959"></a>KMS encryption</strong> and select the key to be used from the key list. After you select <strong id="b1731175645101245"><a name="b1731175645101245"></a><a name="b1731175645101245"></a>KMS encryption</strong>, the system will create a default master private key <strong id="b84235270610140"><a name="b84235270610140"></a><a name="b84235270610140"></a>ims/default</strong> for you. You can also select a private key from the private key list.</p>
    <p id="p96591652653"><a name="p96591652653"></a><a name="p96591652653"></a>For how to encrypt an image, see <a href="creating-encrypted-images.md">Creating Encrypted Images</a>.</p>
    </td>
    </tr>
    <tr id="row142057141619"><td class="cellrowborder" valign="top" width="25.91%" headers="mcps1.2.3.1.1 "><p id="p1420612141267"><a name="p1420612141267"></a><a name="p1420612141267"></a>Tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="74.09%" headers="mcps1.2.3.1.2 "><p id="p820611415612"><a name="p820611415612"></a><a name="p820611415612"></a>(Optional) Set a tag key and a tag value for the image to easily identify and manage it.</p>
    </td>
    </tr>
    <tr id="row720613141962"><td class="cellrowborder" valign="top" width="25.91%" headers="mcps1.2.3.1.1 "><p id="p7206111416617"><a name="p7206111416617"></a><a name="p7206111416617"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="74.09%" headers="mcps1.2.3.1.2 "><p id="p420631410613"><a name="p420631410613"></a><a name="p420631410613"></a>(Optional) Enter the description of the image.</p>
    </td>
    </tr>
    </tbody>
    </table>

4.  Click  **Next**, confirm the configurations, and click  **Submit**.
5.  Go back to the  **Private Images**  page. The image is successfully registered when its status becomes  **Normal**.

    >![](/images/icon-note.gif) **NOTE:**   
    >The time required for image registration is determined by the image file size. You may need to wait a long period of time for the image file to be successfully registered as a private image.  



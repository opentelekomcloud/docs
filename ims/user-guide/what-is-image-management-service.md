# What Is Image Management Service?<a name="EN-US_TOPIC_0013901609"></a>

## Overview<a name="section1848290795755"></a>

An image is an Elastic Cloud Server \(ECS\) or a Bare Metal Server \(BMS\) template that contains an operating system \(OS\) or service data and necessary application software, such as database software. Images are categorized into public, private, Marketplace, and shared images.

Image Management Service \(IMS\) allows you to manage the lifecycle of images. You can create ECSs or BMSs from a public, private, or shared image. You can also create a private image from an ECS or external image file.

## Image Types<a name="section2445683595836"></a>

Images are classified as public, private, Marketplace images, and shared images according to their visibility. Public images are provided by the cloud platform, private images are those you created, and shared images are private images that other tenants shared with you.

<a name="en-us_topic_0029124570_en-us_topic_0029124523_table5687699412614"></a>
<table><thead align="left"><tr id="en-us_topic_0029124570_en-us_topic_0029124523_row6204106512614"><th class="cellrowborder" valign="top" width="18.990000000000002%" id="mcps1.1.3.1.1"><p id="en-us_topic_0029124570_en-us_topic_0029124523_p5927036212614"><a name="en-us_topic_0029124570_en-us_topic_0029124523_p5927036212614"></a><a name="en-us_topic_0029124570_en-us_topic_0029124523_p5927036212614"></a><strong id="b84235270695930"><a name="b84235270695930"></a><a name="b84235270695930"></a>Image Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="81.01%" id="mcps1.1.3.1.2"><p id="en-us_topic_0029124570_en-us_topic_0029124523_p3616998312614"><a name="en-us_topic_0029124570_en-us_topic_0029124523_p3616998312614"></a><a name="en-us_topic_0029124570_en-us_topic_0029124523_p3616998312614"></a><strong id="b84235270695939"><a name="b84235270695939"></a><a name="b84235270695939"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0029124570_en-us_topic_0029124523_row4408748812614"><td class="cellrowborder" valign="top" width="18.990000000000002%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0029124570_en-us_topic_0029124523_p1431680712614"><a name="en-us_topic_0029124570_en-us_topic_0029124523_p1431680712614"></a><a name="en-us_topic_0029124570_en-us_topic_0029124523_p1431680712614"></a><span class="keyword" id="keyword1411468221151522"><a name="keyword1411468221151522"></a><a name="keyword1411468221151522"></a>Public image</span></p>
</td>
<td class="cellrowborder" valign="top" width="81.01%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0029124570_en-us_topic_0029124523_p1881068112614"><a name="en-us_topic_0029124570_en-us_topic_0029124523_p1881068112614"></a><a name="en-us_topic_0029124570_en-us_topic_0029124523_p1881068112614"></a>A public image is a standard, widely used image. It contains an OS and preinstalled public applications and is available to all users. Public images are highly stable and authorized. You can configure the application environment or related software as required.</p>
</td>
</tr>
<tr id="en-us_topic_0029124570_en-us_topic_0029124523_row3507840712614"><td class="cellrowborder" valign="top" width="18.990000000000002%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0029124570_en-us_topic_0029124523_p2277869512614"><a name="en-us_topic_0029124570_en-us_topic_0029124523_p2277869512614"></a><a name="en-us_topic_0029124570_en-us_topic_0029124523_p2277869512614"></a><span class="keyword" id="keyword1056511395151512"><a name="keyword1056511395151512"></a><a name="keyword1056511395151512"></a>Private image</span></p>
</td>
<td class="cellrowborder" valign="top" width="81.01%" headers="mcps1.1.3.1.2 "><p id="p6239130142016"><a name="p6239130142016"></a><a name="p6239130142016"></a>A private image is an image that contains an OS or service data, pre-installed public applications, and the owner's private applications. It is visible only to the user who creates it.</p>
<p id="p978715419106"><a name="p978715419106"></a><a name="p978715419106"></a>A private image can be a system disk image, full-ECS image, or data disk image.</p>
<a name="ul28904698175326"></a><a name="ul28904698175326"></a><ul id="ul28904698175326"><li>System disk image: contains an OS and pre-installed application software for running services. You can use a system disk image to create ECSs and migrate your services to the cloud.</li><li>Data disk image: contains only the owner's service data. You can also use a data disk image to create EVS disks and migrate your service data to the cloud.</li><li>Full-ECS image: contains an OS, pre-installed application software, and service data.</li></ul>
</td>
</tr>
<tr id="row22261334165248"><td class="cellrowborder" valign="top" width="18.990000000000002%" headers="mcps1.1.3.1.1 "><p id="p66134282165248"><a name="p66134282165248"></a><a name="p66134282165248"></a><span class="keyword" id="keyword290210687151536"><a name="keyword290210687151536"></a><a name="keyword290210687151536"></a>Shared image</span></p>
</td>
<td class="cellrowborder" valign="top" width="81.01%" headers="mcps1.1.3.1.2 "><p id="p7991323165259"><a name="p7991323165259"></a><a name="p7991323165259"></a>A shared image is an image shared by another tenant with you. </p>
</td>
</tr>
<tr id="row187861916172017"><td class="cellrowborder" valign="top" width="18.990000000000002%" headers="mcps1.1.3.1.1 "><p id="p578781642013"><a name="p578781642013"></a><a name="p578781642013"></a>Marketplace image</p>
</td>
<td class="cellrowborder" valign="top" width="81.01%" headers="mcps1.1.3.1.2 "><p id="p1878711169202"><a name="p1878711169202"></a><a name="p1878711169202"></a>The Marketplace is a store where you can purchase third-party images that have the OS, application environment, and software pre-installed. You can use the images to deploy websites and application development environments with a few clicks, and no additional configuration operation is required.</p>
</td>
</tr>
</tbody>
</table>

## IMS Functions<a name="section4762417995855"></a>

IMS provides:

-   Public images that use common OSs
-   Creation of a private image from an ECS or an external image file
-   Public image management, such as searching images by OS type, name, or ID, and viewing the image ID, system disk size, and features \(such as user data injection and disk hot swap\) supported by the image
-   Private image management, such as modifying image attributes, sharing images, and replicating images
-   Creation of ECSs using an image

## Access Mode<a name="section124941284376"></a>

The public cloud provides a web-based service management platform \(management console\). You can access ECSs through HTTPS-compliant application programming interfaces \(APIs\) or the management console. These two access modes differ as follows:

-   API

    If you need to integrate IMS into a third-party system for secondary development, use APIs to access the IMS service. For details, see  _Image Management Service API Reference_.

-   Management console

    You can perform other operations provided by IMS on the management console. 



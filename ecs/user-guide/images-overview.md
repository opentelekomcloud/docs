# Overview<a name="EN-US_TOPIC_0177457773"></a>

## Image<a name="section2063511219582"></a>

An image is an ECS template that contains an OS or service data and may also contain proprietary software and application software, such as database software. Images can be public, private, Marketplace, or shared.

Image Management Service \(IMS\) allows you to easily create and manage images. You can create an ECS using a public image, private image, or shared image. You can also use an existing ECS or external image file to create a private image.

## Public Image<a name="section1685231310443"></a>

A standard, widely used image. A public image contains an OS, such as Windows, Ubuntu, CentOS, or Debian, and preinstalled public applications. This image will be available to all users. Select your desired public image. Alternatively, create a private image based on a public image to copy an existing ECS or rapidly create ECSs in a batch. You can customize a public image by configuring the application environment and software.

## Private Image<a name="section46132514116"></a>

A private image contains an OS or service data, preinstalled public applications, and private applications. It is available only to the user who created it.

**Table  1**  Private image types

<a name="table1567919914154"></a>
<table><thead align="left"><tr id="row6679109141518"><th class="cellrowborder" valign="top" width="18.43%" id="mcps1.2.3.1.1"><p id="p568010912154"><a name="p568010912154"></a><a name="p568010912154"></a>Image Type</p>
</th>
<th class="cellrowborder" valign="top" width="81.57%" id="mcps1.2.3.1.2"><p id="p36801897151"><a name="p36801897151"></a><a name="p36801897151"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row7680149111517"><td class="cellrowborder" valign="top" width="18.43%" headers="mcps1.2.3.1.1 "><p id="p2068029161516"><a name="p2068029161516"></a><a name="p2068029161516"></a>System disk image</p>
</td>
<td class="cellrowborder" valign="top" width="81.57%" headers="mcps1.2.3.1.2 "><p id="p1268009201516"><a name="p1268009201516"></a><a name="p1268009201516"></a>Contains an OS and application software for running services. You can use a system disk image to create ECSs and migrate your services to the cloud.</p>
</td>
</tr>
<tr id="row146805951513"><td class="cellrowborder" valign="top" width="18.43%" headers="mcps1.2.3.1.1 "><p id="p868089111518"><a name="p868089111518"></a><a name="p868089111518"></a>Data disk image</p>
</td>
<td class="cellrowborder" valign="top" width="81.57%" headers="mcps1.2.3.1.2 "><p id="p18680189131517"><a name="p18680189131517"></a><a name="p18680189131517"></a>Contains only service data. You can use a data disk image to create EVS disks and migrate your service data to the cloud.</p>
</td>
</tr>
<tr id="row1768014915151"><td class="cellrowborder" valign="top" width="18.43%" headers="mcps1.2.3.1.1 "><p id="p2068014913158"><a name="p2068014913158"></a><a name="p2068014913158"></a>Full-ECS image</p>
</td>
<td class="cellrowborder" valign="top" width="81.57%" headers="mcps1.2.3.1.2 "><p id="p10680189161520"><a name="p10680189161520"></a><a name="p10680189161520"></a>Contains an OS, application software, and data for running services. A full-ECS image contains the system disk and all data disks attached to it.</p>
</td>
</tr>
</tbody>
</table>

If you plan to use a private image to change the OS, ensure that the private image is available. For instructions about how to create a private image, see  _Image Management Service User Guide_.

-   If the image of a specified ECS is required, make sure that a private image has been created using this ECS.
-   If a local image file is required, make sure that the image file has been imported to the cloud platform and registered as a private image.
-   If a private image from another region is required, make sure that the image has been copied.
-   If a private image from another user account is required, make sure that the image has been shared with you.

## Shared Image<a name="section6342194217116"></a>

A shared image is a private image shared by another user and can be used as your own private image. 

-   Images can be shared within a region only. 
-   Each image can be shared to a maximum of 128 tenants.
-   You can stop sharing images anytime without notifying the recipient.
-   You can delete shared image anytime without notifying the recipient.
-   Encrypted images cannot be shared.
-   Full-ECS images cannot be shared.

## Marketplace Image<a name="section6597649181118"></a>

A third-party image that has the OS, application environment, and software preinstalled. You can use the images to deploy websites and application development environments with a few clicks. No additional configuration is required.

A Marketplace image can be free of charge or paid, based on image service providers. When you use a paid image to create an ECS, you need to pay for the Marketplace image and ECS.


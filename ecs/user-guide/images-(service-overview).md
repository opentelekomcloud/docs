# Images<a name="EN-US_TOPIC_0030828254"></a>

## What Is Image?<a name="en-us_topic_0027498836_section6105436615564"></a>

An image is an ECS template that contains an OS and may also contain proprietary software and application software, such as database software. You can use images to create ECSs.

Images can be public, private, or shared. Public images are provided by the system by default, private images are manually created, and shared images are private images that are shared by another user. You can use any type of image to create an ECS. You can also create a private image using an existing ECS or external image. This provides you with a simple way to create ECSs that comply with your service requirements. For example, if you use web services, your image can contain web server configurations, static configurations, and dynamic page code. After you use this image to create an ECS, the web server will run.

## Image Types<a name="en-us_topic_0027498836_section31040989164158"></a>

**Table  1**  Image types

<a name="en-us_topic_0027498836_table25967296164224"></a>
<table><thead align="left"><tr id="en-us_topic_0027498836_row54255308164224"><th class="cellrowborder" valign="top" width="16.73%" id="mcps1.2.3.1.1"><p id="en-us_topic_0027498836_p24998728164224"><a name="en-us_topic_0027498836_p24998728164224"></a><a name="en-us_topic_0027498836_p24998728164224"></a>Image Type</p>
</th>
<th class="cellrowborder" valign="top" width="83.27%" id="mcps1.2.3.1.2"><p id="en-us_topic_0027498836_p11631092164224"><a name="en-us_topic_0027498836_p11631092164224"></a><a name="en-us_topic_0027498836_p11631092164224"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0027498836_row12264203164224"><td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0027498836_p38049136164319"><a name="en-us_topic_0027498836_p38049136164319"></a><a name="en-us_topic_0027498836_p38049136164319"></a>Public image</p>
</td>
<td class="cellrowborder" valign="top" width="83.27%" headers="mcps1.2.3.1.2 "><p id="p027755191815"><a name="p027755191815"></a><a name="p027755191815"></a>A standard, widely used image. It contains an OS and preinstalled public applications and is available to all users.</p>
</td>
</tr>
<tr id="en-us_topic_0027498836_row2891925164224"><td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0027498836_p32919397164224"><a name="en-us_topic_0027498836_p32919397164224"></a><a name="en-us_topic_0027498836_p32919397164224"></a>Private image</p>
</td>
<td class="cellrowborder" valign="top" width="83.27%" headers="mcps1.2.3.1.2 "><p id="p56421362113357"><a name="p56421362113357"></a><a name="p56421362113357"></a>An image available only to the user who created it. It contains an OS, preinstalled public applications, and the user's private applications. Using a private image to create ECSs removes the need to configure multiple ECSs repeatedly. A private image can be created using:</p>
<a name="en-us_topic_0029124570_ul3646220717511"></a><a name="en-us_topic_0029124570_ul3646220717511"></a><ul id="en-us_topic_0029124570_ul3646220717511"><li>An ECS</li><li>An external image file<p id="p6578515517525"><a name="p6578515517525"></a><a name="p6578515517525"></a>You can upload external image files and register the images on the public cloud platform to make them function as private images. External image files can be in VMDK, VHD, QCOW2, or ZVHD format.</p>
</li></ul>
</td>
</tr>
<tr id="row2112651116412"><td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.3.1.1 "><p id="p2852802316412"><a name="p2852802316412"></a><a name="p2852802316412"></a>Shared image</p>
</td>
<td class="cellrowborder" valign="top" width="83.27%" headers="mcps1.2.3.1.2 "><p id="p2057387616412"><a name="p2057387616412"></a><a name="p2057387616412"></a>A private image shared by another user.</p>
</td>
</tr>
<tr id="row919965415438"><td class="cellrowborder" valign="top" width="16.73%" headers="mcps1.2.3.1.1 "><p id="p3505959715438"><a name="p3505959715438"></a><a name="p3505959715438"></a>Marketplace image</p>
</td>
<td class="cellrowborder" valign="top" width="83.27%" headers="mcps1.2.3.1.2 "><p id="p2318436915438"><a name="p2318436915438"></a><a name="p2318436915438"></a>A third-party image that has the OS, application environment, and software preinstalled. You can use the images to deploy websites and application development environments with a few clicks. No additional configuration operation is required.</p>
</td>
</tr>
</tbody>
</table>


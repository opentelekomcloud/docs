##IMS
### Introduction

Image Management Service (IMS) allows you to create ECSs using images. An image is an ECS template that contains an OS and may also contain proprietary software and application software, such as database software.

Images can be public, private, or shared. Public images are provided by the
system by default, private images are manually created, and shared images are private images that are shared by another user. You can use any type of image to create an ECS. You can also create a private image using an existing ECS or external image. This provides you with a simple way to create ECSs that comply with your service requirements. For example, if you use web services, your image can contain a web server, static configurations, and dynamic page code. When you use this image to create an ECS, your web server and applications will be available for use immediately.

###Image Types
Table 1-1 Image types

<table>
    <tr>
        <th>Image Type</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>Public image</td>
        <td>A standard, widely used image. It contains an OS, comes with preinstalled public applications, and is available to all users.</td>
          </tr>
           <tr>
        <td>Private image</td>
        <td>An image available only to the user who created it. It contains an OS, preinstalled public applications, and the user’s private applications. Using a private image to create ECSs removes the need to configure multiple ECSs repeatedly. A private image can be created using: 1, An ECS 2, An external image file: You can upload external image files and register the images on the public cloud platform to make them function as private images. External image files can be in VMDK, VHD, QCOW2, or ZVHD format.</td>
          </tr>
           <tr>
        <td>Shared image</td>
        <td>A private image shared by another user.</td>
          </tr>
                     <tr>
        <td>Marketplace image</td>
        <td>	A third-party image that has the OS, application environment, and software pre-installed. You can use the images to deploy websites and application development environments with a few clicks. No additional configuration operation is required.</td>
          </tr>
</table>

### Conversion Between Images and ECSs

You can use images to create ECSs and you can convert  ECS configurations into images.

# Image<a name="EN-US_TOPIC_0083745257"></a>

## What Is an Image?<a name="section7588141665317"></a>

An image is a template of the BMS running environment. It contains an OS and runtime environment, and also some pre-installed applications. An image file is equivalent to a copy file that contains all data in the system disk.

## Image Types<a name="section737511513552"></a>

Images can be classified into public images, private images, and shared images based on the image source.

**Table  1**  Image types

<a name="table72052065610"></a>
<table><thead align="left"><tr id="row32132055613"><th class="cellrowborder" valign="top" width="28.000000000000004%" id="mcps1.2.3.1.1"><p id="p18211820195618"><a name="p18211820195618"></a><a name="p18211820195618"></a>Image Type</p>
</th>
<th class="cellrowborder" valign="top" width="72%" id="mcps1.2.3.1.2"><p id="p16211120115618"><a name="p16211120115618"></a><a name="p16211120115618"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row22172025611"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.3.1.1 "><p id="p62152065614"><a name="p62152065614"></a><a name="p62152065614"></a>Public image</p>
</td>
<td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.3.1.2 "><p id="p20211209564"><a name="p20211209564"></a><a name="p20211209564"></a>A public image is a standard, widely used image. It contains an OS and preinstalled public applications or services and is available to all users.</p>
</td>
</tr>
<tr id="row1521320115616"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.3.1.1 "><p id="p2211320105619"><a name="p2211320105619"></a><a name="p2211320105619"></a>Private image</p>
</td>
<td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.3.1.2 "><p id="p1921112014561"><a name="p1921112014561"></a><a name="p1921112014561"></a>A private image contains an OS, pre-installed public applications, and a user's private applications. It is visible only to the user who creates it. Using a private image to create BMSs frees you from configuring BMSs repeatedly.</p>
</td>
</tr>
<tr id="row8211520195616"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.3.1.1 "><p id="p162102035616"><a name="p162102035616"></a><a name="p162102035616"></a>Shared image</p>
</td>
<td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.3.1.2 "><p id="p321620115619"><a name="p321620115619"></a><a name="p321620115619"></a>This is a private image shared by another user.</p>
</td>
</tr>
</tbody>
</table>

## Public Image<a name="section2087195810593"></a>

Public images are provided by the system. These images are adaptable to BMS compatibility with necessary initial plug-ins and are available to all users. Most mainstream OSs are included. Available public images vary depending on the BMS flavor.

**Characteristics**

-   OS types: Linux and Windows OSs that are updated and maintained periodically
-   Supported software: Public images integrate some plug-ins on which BMS storage, networks, and basic functions depend.

    >![](/images/icon-notice.gif) **NOTICE:**   
    >These plug-ins are necessary for BMSs to run properly. Do not delete or modify any of them. Otherwise, your BMS basic functions will be affected.  

    **Table  2**  Supported software

    <a name="table1717118165381"></a>
    <table><thead align="left"><tr id="row2172131612381"><th class="cellrowborder" valign="top" width="23.189999999999998%" id="mcps1.2.3.1.1"><p id="p71720169384"><a name="p71720169384"></a><a name="p71720169384"></a>Software</p>
    </th>
    <th class="cellrowborder" valign="top" width="76.81%" id="mcps1.2.3.1.2"><p id="p817217161388"><a name="p817217161388"></a><a name="p817217161388"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row161728161386"><td class="cellrowborder" valign="top" width="23.189999999999998%" headers="mcps1.2.3.1.1 "><p id="p1172181610384"><a name="p1172181610384"></a><a name="p1172181610384"></a>Cloud-init</p>
    </td>
    <td class="cellrowborder" valign="top" width="76.81%" headers="mcps1.2.3.1.2 "><p id="p575323613818"><a name="p575323613818"></a><a name="p575323613818"></a>Cloud-Init is an open-source cloud initialization program, which initializes specified customized configurations, such as the host name, key, and user data, of a newly created BMS.</p>
    </td>
    </tr>
    <tr id="row10172121617385"><td class="cellrowborder" valign="top" width="23.189999999999998%" headers="mcps1.2.3.1.1 "><p id="p3172111618386"><a name="p3172111618386"></a><a name="p3172111618386"></a>bms-network-config network configuration plug-in</p>
    </td>
    <td class="cellrowborder" valign="top" width="76.81%" headers="mcps1.2.3.1.2 "><p id="p2172616183818"><a name="p2172616183818"></a><a name="p2172616183818"></a>This plug-in is used to automatically configure BMS networks during BMS provisioning and restore the BMS network when the network is interrupted due to misoperations.</p>
    </td>
    </tr>
    <tr id="row1017231612382"><td class="cellrowborder" valign="top" width="23.189999999999998%" headers="mcps1.2.3.1.1 "><p id="p51721116173819"><a name="p51721116173819"></a><a name="p51721116173819"></a>SDI iNIC frontend driver plug-in</p>
    </td>
    <td class="cellrowborder" valign="top" width="76.81%" headers="mcps1.2.3.1.2 "><p id="p111720168381"><a name="p111720168381"></a><a name="p111720168381"></a>This plug-in is installed on the image so that BMSs can have EVS disks attached and can start from EVS disks, which enables quick BMS provisioning.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Compatibility: Public images are compatible with server hardware.
-   Security: Public images are highly stable and licensed.
-   Restrictions: There are no restrictions on using public images.

## Private Image<a name="section1736332313512"></a>

A private image contains an OS, preinstalled public applications, and a user's private applications. Using a private image to create BMSs frees you from configuring BMSs repeatedly.

**Characteristics**

-   Compatibility: Private images only adapt to servers of the same model as the private images and may fail to deploy BMSs of other models.
-   Supported functions: You can create and delete private images, as well as create BMSs and reinstall the BMS OS using private images. 
-   Restrictions: You can create a maximum of 50 private images.

**Shared Images**

Private images refer to images shared by other tenants with you.

## Application Scenarios<a name="section985836152820"></a>

-   Deploying software environments in a batch

    Use a BMS with an OS, partitions, and software to create a private image, and then use the image to create BMSs in a batch. The created BMSs have the same configuration as the source BMS.

-   Backing up a BMS

    Create an image from a BMS to back up the BMS. If the software of the BMS becomes faulty, you can use the image to restore the BMS.



# Creating a System Disk Image from a Linux ECS<a name="EN-US_TOPIC_0030713180"></a>

## Scenarios<a name="section1583993012317"></a>

If you have created a Linux ECS and configured it \(such as software installation and application environment deployment\) based on your business requirements, you can create a system disk image from the configured ECS. Then, the configurations will be applied to all the new ECSs created from this image.

## Prerequisites<a name="en-us_topic_0029124558_section14824313152247"></a>

Before creating a private image from an ECS:

-   Delete sensitive data in the ECS to prevent data security risks.
-   Ensure that the ECS is in the  **Running**  or  **Stopped**  state.
-   Check network configuration of the ECS and ensure that DHCP is configured for the NICs. For details, see  [Setting the NIC to DHCP \(Linux\)](setting-the-nic-to-dhcp-(linux).md).
-   Install special drivers. The normal running and advanced functions of some ECSs depend on certain drivers. For example, P1 ECSs depend on the NVIDIA driver. For details, see  [Installing Special Linux Drivers](installing-special-linux-drivers.md).
-   Check whether Cloud-Init has been installed in the ECS. The user data injection function on the management console is available for the new ECSs created from the image only after the tool is installed. For example, you can use the data injection function to set the login password for a new ECS. For details, see  [Installing Cloud-Init](installing-cloud-init.md)  and  [Configuring Cloud-Init](configuring-cloud-init.md).
-   Delete network rule files to prevent NIC name drift on the ECSs created from the image. For details, see  [Deleting Files in the Network Rule Directory](deleting-files-in-the-network-rule-directory.md).
-   To ensure that the ECSs created from the image support both Xen and KVM virtualization, optimize the Linux ECS used to create the image, such as changing the disk ID in the GRUB and fstab files to UUID and installing native Xen and KVM drivers.

    For details, see steps 2 to 6 in  [Optimization Process](optimization-process-(linux).md).

-   If multiple data disks are attached to the ECS used to create the private image, the ECSs created from the image may be unavailable. Therefore, you need to detach all data disks from the ECS before using it to create the image. For details, see  [Detaching Data Disks from an ECS](detaching-data-disks-from-an-ecs.md).
-   To ensure that  **Console Log**  is available for the newly created ECSs on the console, set related parameters in the ECS that is used to create the image. For details, see  [Configuring Console Logging](configuring-console-logging.md).

>![](/images/icon-note.gif) **NOTE:**   
>If the ECS is created from a public image, Cloud-Init has been installed by default. You can follow the guide to verify the installation.  

## Procedure<a name="section56420413328"></a>

1.  Log in to the management console.
2.  Under  **Computing**, click  **Image Management Service**.

    The IMS console is displayed.

3.  In the upper right corner, click  **Create Image**  and set the following parameters:

    [Table 1](#en-us_topic_0030713149_table050019474117)  and  [Table 2](#en-us_topic_0030713149_table6978715749)  list the parameters in the  **Image Type and Source**  and  **Image Information**  areas, respectively.

    **Table  1**  Image type and source

    <a name="en-us_topic_0030713149_table050019474117"></a>
    <table><thead align="left"><tr id="en-us_topic_0030713149_row1350164712110"><th class="cellrowborder" valign="top" width="25.96%" id="mcps1.2.3.1.1"><p id="en-us_topic_0030713149_p12501447314"><a name="en-us_topic_0030713149_p12501447314"></a><a name="en-us_topic_0030713149_p12501447314"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="74.03999999999999%" id="mcps1.2.3.1.2"><p id="en-us_topic_0030713149_p1350114720117"><a name="en-us_topic_0030713149_p1350114720117"></a><a name="en-us_topic_0030713149_p1350114720117"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0030713149_row350214713113"><td class="cellrowborder" valign="top" width="25.96%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0030713149_p650294716116"><a name="en-us_topic_0030713149_p650294716116"></a><a name="en-us_topic_0030713149_p650294716116"></a>Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="74.03999999999999%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0030713149_p75021947615"><a name="en-us_topic_0030713149_p75021947615"></a><a name="en-us_topic_0030713149_p75021947615"></a>Select <strong id="en-us_topic_0030713149_b9800161192315"><a name="en-us_topic_0030713149_b9800161192315"></a><a name="en-us_topic_0030713149_b9800161192315"></a>System disk image</strong>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0030713149_row1650284720113"><td class="cellrowborder" valign="top" width="25.96%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0030713149_p125022471113"><a name="en-us_topic_0030713149_p125022471113"></a><a name="en-us_topic_0030713149_p125022471113"></a>Source</p>
    </td>
    <td class="cellrowborder" valign="top" width="74.03999999999999%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0030713149_p850214712118"><a name="en-us_topic_0030713149_p850214712118"></a><a name="en-us_topic_0030713149_p850214712118"></a>Select <strong id="en-us_topic_0030713149_b1429910143237"><a name="en-us_topic_0030713149_b1429910143237"></a><a name="en-us_topic_0030713149_b1429910143237"></a>ECS</strong> and select an ECS on which required configurations have been performed from the ECS list.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  Image information

    <a name="en-us_topic_0030713149_table6978715749"></a>
    <table><thead align="left"><tr id="en-us_topic_0030713149_row1597918159415"><th class="cellrowborder" valign="top" width="25.91%" id="mcps1.2.3.1.1"><p id="en-us_topic_0030713149_p597916152418"><a name="en-us_topic_0030713149_p597916152418"></a><a name="en-us_topic_0030713149_p597916152418"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="74.09%" id="mcps1.2.3.1.2"><p id="en-us_topic_0030713149_p99796151642"><a name="en-us_topic_0030713149_p99796151642"></a><a name="en-us_topic_0030713149_p99796151642"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0030713149_row190153318123"><td class="cellrowborder" valign="top" width="25.91%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0030713149_p156591952159"><a name="en-us_topic_0030713149_p156591952159"></a><a name="en-us_topic_0030713149_p156591952159"></a>Encryption</p>
    </td>
    <td class="cellrowborder" valign="top" width="74.09%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0030713149_p96591652653"><a name="en-us_topic_0030713149_p96591652653"></a><a name="en-us_topic_0030713149_p96591652653"></a>This parameter specifies the encryption attribute of the image. The value cannot be changed.</p>
    <a name="en-us_topic_0030713149_ul94161232191418"></a><a name="en-us_topic_0030713149_ul94161232191418"></a><ul id="en-us_topic_0030713149_ul94161232191418"><li>Only an unencrypted private image can be created from an unencrypted <span id="en-us_topic_0030713149_text9398194114266"><a name="en-us_topic_0030713149_text9398194114266"></a><a name="en-us_topic_0030713149_text9398194114266"></a>ECS</span><span id="en-us_topic_0030713149_text1839914412264"><a name="en-us_topic_0030713149_text1839914412264"></a><a name="en-us_topic_0030713149_text1839914412264"></a></span>.</li><li>Only an encrypted private image can be created from an encrypted <span id="en-us_topic_0030713149_text1730719615276"><a name="en-us_topic_0030713149_text1730719615276"></a><a name="en-us_topic_0030713149_text1730719615276"></a>ECS</span><span id="en-us_topic_0030713149_text43081663272"><a name="en-us_topic_0030713149_text43081663272"></a><a name="en-us_topic_0030713149_text43081663272"></a></span>.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0030713149_row36593522511"><td class="cellrowborder" valign="top" width="25.91%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0030713149_p19659452051"><a name="en-us_topic_0030713149_p19659452051"></a><a name="en-us_topic_0030713149_p19659452051"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="74.09%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0030713149_p126597521359"><a name="en-us_topic_0030713149_p126597521359"></a><a name="en-us_topic_0030713149_p126597521359"></a>Set a name for the image.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0030713149_row142057141619"><td class="cellrowborder" valign="top" width="25.91%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0030713149_p1420612141267"><a name="en-us_topic_0030713149_p1420612141267"></a><a name="en-us_topic_0030713149_p1420612141267"></a>Tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="74.09%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0030713149_p820611415612"><a name="en-us_topic_0030713149_p820611415612"></a><a name="en-us_topic_0030713149_p820611415612"></a>(Optional) Set a tag key and a tag value for the image to easily identify and manage it.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0030713149_row720613141962"><td class="cellrowborder" valign="top" width="25.91%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0030713149_p7206111416617"><a name="en-us_topic_0030713149_p7206111416617"></a><a name="en-us_topic_0030713149_p7206111416617"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="74.09%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0030713149_p420631410613"><a name="en-us_topic_0030713149_p420631410613"></a><a name="en-us_topic_0030713149_p420631410613"></a>(Optional) Enter the description of the image.</p>
    </td>
    </tr>
    </tbody>
    </table>

4.  Click  **Next**.
5.  Confirm the parameters and click  **Submit**.
6.  Switch back to the  **Image Management Service**  page to view the image status. 

    The time required for creating an image depends on the image file size, network status, and number of concurrent tasks. When the image status changes to  **Normal**, the image is created successfully.

    >![](/images/icon-note.gif) **NOTE:**   
    >-   Do not perform any operation on the selected ECS or its associated resources during image creation.  
    >-   An ECS created from an encrypted image is also encrypted. The key used for encrypting the ECS is the same as that used for encrypting the image.  
    >-   An image created from an encrypted ECS is also encrypted. The key used for encrypting the image is the same as that used for encrypting the ECS.  



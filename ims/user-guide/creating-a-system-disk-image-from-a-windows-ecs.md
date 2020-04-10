# Creating a System Disk Image from a Windows ECS<a name="EN-US_TOPIC_0030713149"></a>

## Scenarios<a name="section1787117288167"></a>

If you have created a Windows ECS and configured it \(such as software installation and application environment deployment\) based on your business requirements, you can create a system disk image from the configured ECS. Then, the configurations will be applied to all the new ECSs created from this image.

## Prerequisites<a name="section943045519380"></a>

Before creating a private image from an ECS:

-   Delete sensitive data in the ECS to prevent data security risks.
-   Ensure that the ECS is in the  **Running**  or  **Stopped**  state.
-   Check network configuration of the ECS and ensure that DHCP is configured for the NICs. Enable remote desktop connection as needed. For details, see  [Setting the NIC to DHCP \(Windows\)](setting-the-nic-to-dhcp-(windows).md)  and  [Enabling Remote Desktop Connection](enabling-remote-desktop-connection.md).
-   Install special drivers. The normal running and advanced functions of some ECSs depend on certain drivers. For example, GPU-accelerated ECSs depend on the Tesla and GRID/vGPU drivers. For details, see  [Installing Special Windows Drivers](installing-special-windows-drivers.md).
-   Check whether Cloudbase-Init has been installed in the ECS. The user data injection function on the management console is available for the new ECSs created from the image only after the tool is installed. For example, you can use the data injection function to set the login password for a new ECS. For details, see  [Installing and Configuring Cloudbase-Init](installing-and-configuring-cloudbase-init.md).
-   Check and install the PV driver and UVP VMTools driver to ensure that the new ECSs created from the image support both KVM and XEN virtualization and to improve network performance.

    For details, see steps 2 to 5 in  [Optimization Process](optimization-process-(windows).md).

-   Run Sysprep to ensure that the SIDs of the new ECSs created from the image are unique in a domain. In a cluster deployment scenario, the SIDs must be unique. For details, see  [Running Sysprep](running-sysprep.md).

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>If the ECS is created from a public image, Cloudbase-Init has been installed by default. You can follow the guide in the prerequisites to verify the installation.  

## Procedure<a name="section146023151537"></a>

1.  Log in to the management console.
2.  Under  **Computing**, click  **Image Management Service**.

    The IMS console is displayed.

3.  In the upper right corner, click  **Create Image**  and set the following parameters:

    [Table 1](#table050019474117)  and  [Table 2](#table6978715749)  list the parameters in the  **Image Type and Source**  and  **Image Information**  areas, respectively.

    **Table  1**  Image type and source

    <a name="table050019474117"></a>
    <table><thead align="left"><tr id="row1350164712110"><th class="cellrowborder" valign="top" width="25.96%" id="mcps1.2.3.1.1"><p id="p12501447314"><a name="p12501447314"></a><a name="p12501447314"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="74.03999999999999%" id="mcps1.2.3.1.2"><p id="p1350114720117"><a name="p1350114720117"></a><a name="p1350114720117"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row350214713113"><td class="cellrowborder" valign="top" width="25.96%" headers="mcps1.2.3.1.1 "><p id="p650294716116"><a name="p650294716116"></a><a name="p650294716116"></a>Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="74.03999999999999%" headers="mcps1.2.3.1.2 "><p id="p75021947615"><a name="p75021947615"></a><a name="p75021947615"></a>Select <strong id="b9800161192315"><a name="b9800161192315"></a><a name="b9800161192315"></a>System disk image</strong>.</p>
    </td>
    </tr>
    <tr id="row1650284720113"><td class="cellrowborder" valign="top" width="25.96%" headers="mcps1.2.3.1.1 "><p id="p125022471113"><a name="p125022471113"></a><a name="p125022471113"></a>Source</p>
    </td>
    <td class="cellrowborder" valign="top" width="74.03999999999999%" headers="mcps1.2.3.1.2 "><p id="p850214712118"><a name="p850214712118"></a><a name="p850214712118"></a>Select <strong id="b1429910143237"><a name="b1429910143237"></a><a name="b1429910143237"></a>ECS</strong> and select an ECS on which required configurations have been performed from the ECS list.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  Image information

    <a name="table6978715749"></a>
    <table><thead align="left"><tr id="row1597918159415"><th class="cellrowborder" valign="top" width="25.91%" id="mcps1.2.3.1.1"><p id="p597916152418"><a name="p597916152418"></a><a name="p597916152418"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="74.09%" id="mcps1.2.3.1.2"><p id="p99796151642"><a name="p99796151642"></a><a name="p99796151642"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row190153318123"><td class="cellrowborder" valign="top" width="25.91%" headers="mcps1.2.3.1.1 "><p id="p156591952159"><a name="p156591952159"></a><a name="p156591952159"></a>Encryption</p>
    </td>
    <td class="cellrowborder" valign="top" width="74.09%" headers="mcps1.2.3.1.2 "><p id="p96591652653"><a name="p96591652653"></a><a name="p96591652653"></a>This parameter specifies the encryption attribute of the image. The value cannot be changed.</p>
    <a name="ul94161232191418"></a><a name="ul94161232191418"></a><ul id="ul94161232191418"><li>Only an unencrypted private image can be created from an unencrypted <span id="text9398194114266"><a name="text9398194114266"></a><a name="text9398194114266"></a>ECS</span><span id="text1839914412264"><a name="text1839914412264"></a><a name="text1839914412264"></a></span>.</li><li>Only an encrypted private image can be created from an encrypted <span id="text1730719615276"><a name="text1730719615276"></a><a name="text1730719615276"></a>ECS</span><span id="text43081663272"><a name="text43081663272"></a><a name="text43081663272"></a></span>.</li></ul>
    </td>
    </tr>
    <tr id="row36593522511"><td class="cellrowborder" valign="top" width="25.91%" headers="mcps1.2.3.1.1 "><p id="p19659452051"><a name="p19659452051"></a><a name="p19659452051"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="74.09%" headers="mcps1.2.3.1.2 "><p id="p126597521359"><a name="p126597521359"></a><a name="p126597521359"></a>Set a name for the image.</p>
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

4.  Click  **Next**.
5.  Confirm the parameters and click  **Submit**.
6.  Switch back to the  **Image Management Service**  page to view the image status. 

    The time required for creating an image depends on the image file size, network status, and number of concurrent tasks. When the image status changes to  **Normal**, the image is created successfully.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   Do not perform any operation on the selected ECS or its associated resources during image creation.  
    >-   An ECS created from an encrypted image is also encrypted. The key used for encrypting the ECS is the same as that used for encrypting the image.  
    >-   An image created from an encrypted ECS is also encrypted. The key used for encrypting the image is the same as that used for encrypting the ECS.  



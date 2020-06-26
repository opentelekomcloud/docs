# What Do I Do If the Initial Configurations of a Windows External Image File Are Not Completed Before the File Is Exported?<a name="EN-US_TOPIC_0030713185"></a>

The ECS where the external image file is located is not configured as instructed in  [Table 1](preparing-an-image-file-(windows).md#table85212269215)  before the image file is exported. You are advised to follow the process in  [Figure 1](#fig18196115421120)  to configure the ECS.

**Figure  1**  Image creation process<a name="fig18196115421120"></a>  
![](figures/image-creation-process.png "image-creation-process")

## Step 1: Upload the Image File<a name="section1049514242043"></a>

Upload the external image file to the OBS bucket. For details, see  [Uploading an External Image File](uploading-an-external-image-file-(windows).md).

## Step 2 Register the External Image File as a Private Image<a name="section4198749842"></a>

On the management console, select the uploaded image file and register it as an uninitialized private image. For details, see  [Registering an External Image File as a Private Image](registering-an-external-image-file-as-a-private-image-(windows).md).

## Step 3: Create an ECS<a name="en-us_topic_0029124475_s3524cdcb025c4c3aa892d8c644fc677e"></a>

1.  Log in to the management console.
2.  Under  **Computing**, click  **Image Management Service**.

    The IMS console is displayed.

3.  Click the  **Private Images**  tab to display the image list.
4.  Locate the row that contains the uninitialized private image and click  **Apply for Server**  in the  **Operation**  column.
5.  Set parameters as promoted to create the ECS. Pay attention to the following:

    -   Bind an EIP to the ECS so that you can upload the Guest OS driver installation package to the ECS or download the Guest OS driver installation package from the ECS.
    -   You must add inbound rules for the security group of the ECS to ensure that the ECS can be accessed.
    -   If the image file has Cloudbase-Init installed and configured, set a password and log in to the ECS using the password as prompted. If Cloudbase-Init is not installed, use the password or certificate contained in the image file to log in the ECS.

    For details, see  _Elastic Cloud Server User Guide_.

6.  Perform the following steps to check whether the private image is available:

    1.  Check whether the ECS can start successfully. If yes, the Guest OS driver required by the ECS has been automatically installed on the cloud platform. If no, install the Guest OS driver by referring to  [4](#li32851343163416)  in  [Step 4: Configure the ECS](#section1170711344016).
    2.  Check whether you can log in to the ECS using your configured password or key. If yes, Cloudbase-Init has been installed. If no, use the password or key contained in the image file to log in the ECS and install Cloudbase-Init as instructed in  [Installing and Configuring Cloudbase-Init](installing-and-configuring-cloudbase-init.md).
    3.  Check whether the NIC is set to DHCP by referring to  [2](#li19785161610328)  in  [Step 4: Configure the ECS](#section1170711344016).
    4.  Use MSTSC to log in to the ECS. If the login is successful, remote desktop connection is enabled on the ECS. If the login fails, enable remote desktop connection by referring to  [3](#li174414479612)  in  [Step 4: Configure the ECS](#section1170711344016).

    If the ECS meets the preceding requirements, the private image is available. You can clear the environment as instructed in  [\(Optional\) Clear the Environment](#section69472817511).


## Step 4: Configure the ECS<a name="section1170711344016"></a>

Remotely log in to the ECS created in  [Step 3: Create an ECS](#en-us_topic_0029124475_s3524cdcb025c4c3aa892d8c644fc677e)  to configure the network and install drivers.

1.  Log in to the ECS.
2.  <a name="li19785161610328"></a>Check whether the NIC is set to DHCP. If the ECS is configured with a static IP address, change its IP address assignment mode to DHCP as instructed in  [Setting the NIC to DHCP \(Windows\)](setting-the-nic-to-dhcp-(windows).md).
3.  <a name="li174414479612"></a>Enable remote desktop connection for the ECS as needed. For details about how to enable this function, see  [Enabling Remote Desktop Connection](enabling-remote-desktop-connection.md).
4.  <a name="li32851343163416"></a>Install drivers.

    The proper running of ECSs depends on the XEN Guest OS driver \(PV driver\) and KVM Guest OS driver \(UVP VMTools\). If the drivers are not installed, the performance of ECSs will be affected and some functions will be unavailable. Therefore, you must install the Guest OS driver when using an external image file to create a private image.

    >![](/images/icon-note.gif) **NOTE:**   
    >To avoid an installation failure, perform the following operations before starting the installation:  
    >-   Uninstall third-party virtualization platform tools, such as Citrix Xen Tools and VMware Tools. For how to uninstall the tools provided by a third-party virtualization platform, see the corresponding documents of the cloud platform.  
    >-   Disable your antivirus and intrusion detection software. You can enable the software after the Guest OS driver is installed.  

    -   For details about how to install the PV driver, see  [Installing the PV Driver](installing-the-pv-driver.md).
    -   For details about how to install UVP VMTools, see  [Installing UVP VMTools](installing-uvp-vmtools.md).

    After the drivers are installed, you need to  clear system logs. For details, see  [Clearing System Logs](clearing-system-logs-(windows).md).

5.  \(Optional\) Configure value-added functions.
    -   Install and configure Cloudbase-Init. For details, see  [Installing and Configuring Cloudbase-Init](installing-and-configuring-cloudbase-init.md).
    -   Enable NIC multi-queue. For details, see  [How Do I Set NIC Multi-Queue Feature of an Image?](how-do-i-set-nic-multi-queue-feature-of-an-image.md).


## Step 5: Create an Image from the ECS<a name="section10407615356"></a>

Create a private image from the ECS. For details, see  [Creating a System Disk Image from a Windows ECS](creating-a-system-disk-image-from-a-windows-ecs.md).

## \(Optional\) Clear the Environment<a name="section69472817511"></a>

In the preceding steps, the uninitialized image file and created ECS occupy storage and computing resources. Therefore, you are advised to clear the environment after the image is registered.

-   Delete the uninitialized image registered in  [Step 2 Register the External Image File as a Private Image](#section4198749842).
-   Delete the ECS created in  [Step 3: Create an ECS](#en-us_topic_0029124475_s3524cdcb025c4c3aa892d8c644fc677e).
-   Delete the image files stored in the OBS bucket.


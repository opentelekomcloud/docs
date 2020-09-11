# Installing the PV Driver<a name="EN-US_TOPIC_0037352182"></a>

## Scenarios<a name="section854616214319"></a>

Before using an ECS or external image file to create a private image, ensure that the  PV driver  has been installed in the OS to enable Xen virtualization for subsequently created ECSs, improve the I/O processing performance of the ECSs, and implement advanced functions such as monitoring hardware of the ECSs.

>![](/images/icon-notice.gif) **NOTICE:**   
>If you do not install the PV driver, the ECS network performance will be poor, and the security group and firewall configured for the ECS will not take effect.  

The PV driver has been installed by default when you use a public image to create ECSs. You can perform the following operations to verify the installation:

Open the  **version**  configuration file to check whether the PV driver is the latest:

**C:\\Program Files \(x86\)\\Xen PV Drivers\\bin\\version**

-   If the PV driver version is later than 2.5, you do not need to install the PV driver.
-   If the PV driver version is not displayed or the version is 2.5 or earlier, perform operations in  [Installing the PV Driver](#en-us_topic_0036684067_section46181951).

## Prerequisites<a name="en-us_topic_0036684067_section34957489"></a>

-   An OS has been installed for the ECS, and an EIP has been bound to the ECS.
-   The remaining capacity of the ECS system disk must be greater than 32 MB.
-   If the ECS uses Windows 2008, you must install the PV driver using the administrator account.
-   The PV driver software package has been downloaded on the ECS. For how to obtain the software package, see  [Obtaining Required Software Packages](obtaining-required-software-packages.md).
-   To avoid an installation failure, perform the following operations before starting the installation:
    -   Uninstall third-party virtualization platform tools, such as Citrix Xen Tools and VMware Tools. For how to uninstall the tools provided by a third-party virtualization platform, see the corresponding documents of the cloud platform.
    -   Disable your antivirus and intrusion detection software. You can enable the software after the PV driver is installed.


## Installing the PV Driver<a name="en-us_topic_0036684067_section46181951"></a>

1.  Log in to the Windows ECS using VNC.

    For details about how to log in to the ECS, see  _Elastic Cloud Server User Guide_.

    >![](/images/icon-note.gif) **NOTE:**   
    >You must log in to the ECS using VNC. Remote desktop connection is not allowed because the NIC driver needs to be updated during the installation but the NIC is in use for the remote desktop connection. As a result, the installation will fail.  

2.  On the ECS, choose  **Start**  \>  **Control Panel**.
3.  Click  **Uninstall a program**.
4.  Uninstall  **GPL PV drivers for Windows** _x.x.x.xx_  as prompted.
5.  Download the required PV driver based on the ECS OS and  [Obtaining Required Software Packages](obtaining-required-software-packages.md).
6.  Decompress the PV driver software package.
7.  Right-click  **GPL PV Drivers for Windows** _x.x.x.xx_, select  **Run as administrator**, and complete the installation as prompted.
8.  Restart the ECS as prompted to make the PV driver take effect.

    ECSs running Windows Server 2008 must be restarted twice.

    >![](/images/icon-note.gif) **NOTE:**   
    >After the PV driver is installed, the ECS NIC configuration will be lost. If you have configured NICs before, you need to configure them again.  


## Verifying the Installation<a name="en-us_topic_0036684065_section42271171"></a>

Perform the following steps to verify the installation of the PV driver:

1.  Click  **Start**. Choose  **Control Panel**  \>  **Programs and Features**.
2.  Locate the PV driver for Windows.

    If the PV driver for Windows exists, the installation is successful, as shown in  [Figure 1](#fig16926124855714).

    **Figure  1**  Verifying the installation<a name="fig16926124855714"></a>  
    ![](figures/verifying-the-installation.png "verifying-the-installation")



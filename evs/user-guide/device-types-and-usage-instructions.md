# Device Types and Usage Instructions<a name="en-us_topic_0052554220"></a>

## What Are Device Types?<a name="section4216899312115"></a>

EVS device types are classified as Virtual Block Device \(VBD\) and Small Computer System Interface \(SCSI\) based on whether advanced SCSI commands are supported.

-   VBD is the default EVS disk device type. VBD EVS disks support only basic SCSI read/write commands.
-   SCSI EVS disks support transparent SCSI command transmission and allow the server OS to directly access the underlying storage media. Besides basic read/write SCSI commands, such EVS disks also support advanced SCSI commands.

## Common Application Scenarios and Usage Instructions of SCSI EVS Disks<a name="section5554506411"></a>

-   SCSI EVS disks: BMSs support only SCSI EVS disks, which can be used as either system disks or data disks.
-   Shared SCSI EVS disks: Shared SCSI EVS disks must be used together with a distributed file system or cluster software. Because most cluster applications, such as Windows MSCS, Veritas VCS, and Veritas CFS, require the usage of SCSI reservations, you are advised to use shared EVS disks with SCSI.

    SCSI reservations take effect only when shared SCSI EVS disks are attached to ECSs in the same ECS group. For more information about shared EVS disks, see  [Shared EVS Disks and Usage Instructions](shared-evs-disks-and-usage-instructions.md).


## Do I Need to Install a Driver for SCSI EVS Disks?<a name="section1071245115370"></a>

To use SCSI EVS disks, you need to install a driver for certain server OSs. The details are as follows:

-   BMS

    Both the Windows and Linux images for BMSs are preinstalled with the required driver, that is, the SDI card driver. Therefore, no driver needs to be installed.

-   KVM ECS

    When using SCSI EVS disks, you are advised to use them with KVM ECSs. Linux images for KVM ECSs already have the required driver built in the Linux kernel, and Windows images for KVM ECSs are also included with the driver. Therefore, no driver needs to be installed for KVM ECSs.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >ECS virtualization types are categorized into KVM and Xen. For details, see  [ECS Types](https://docs.otc.t-systems.com/en-us/usermanual/ecs/en-us_topic_0035470096.html).  

-   XEN ECS

    Due to limitations in the driver support, you are advised not to use SCSI EVS disk with Xen ECSs.

    However, there are a few images available that support SCSI EVS disks on Xen ECSs. For the supported images, see  [Table 1](#table36381951181116).

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >After confirming that the OS images of Xen ECSs support SCSI EVS disks, determine whether the driver needs to be installed based on the following conditions:  
    >-   Public Windows images are preinstalled with the Paravirtual SCSI \(PVSCSI\) driver. Therefore, no driver needs to be installed.  
    >-   Private Windows images are not preinstalled with the PVSCSI driver so that you need to download and install it explicitly.  
    >    For details, see  **\(Optional\) Optimizing Windows Private Images**  in the  _Image Management Service User Guide_.  
    >-   Linux images are not preinstalled with the PVSCSI driver. You need to obtain the source code of the open source Linux driver at  [https://github.com/UVP-Tools/SAP-HANA-Tools](https://github.com/UVP-Tools/SAP-HANA-Tools).  
    >    Note that this driver is different from the PVSCSI drivers attached to some Linux distributions.  

    **Table  1**  OSs supporting SCSI EVS disks

    <a name="table36381951181116"></a>
    <table><thead align="left"><tr id="row763875110110"><th class="cellrowborder" valign="top" id="mcps1.2.4.1.1"><p id="p563819518115"><a name="p563819518115"></a><a name="p563819518115"></a>Virtualization Type</p>
    </th>
    <th class="cellrowborder" colspan="2" valign="top" id="mcps1.2.4.1.2"><p id="p1063875115119"><a name="p1063875115119"></a><a name="p1063875115119"></a>OS</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row11638105113112"><td class="cellrowborder" rowspan="2" valign="top" width="19.89%" headers="mcps1.2.4.1.1 "><p id="p7638195161116"><a name="p7638195161116"></a><a name="p7638195161116"></a>XEN</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.129999999999999%" headers="mcps1.2.4.1.2 "><p id="p263835113111"><a name="p263835113111"></a><a name="p263835113111"></a>Windows</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.98%" headers="mcps1.2.4.1.2 "><p id="p18638165141112"><a name="p18638165141112"></a><a name="p18638165141112"></a>See the Windows images listed on the <strong id="b842352706163839"><a name="b842352706163839"></a><a name="b842352706163839"></a>Public Images</strong> page.</p>
    <p id="p3638145181116"><a name="p3638145181116"></a><a name="p3638145181116"></a>For details about how to view the information: Log in to the management console, choose <strong id="b842352706114953"><a name="b842352706114953"></a><a name="b842352706114953"></a>Image Mgmt Service</strong>, click the <strong id="b84235270611508"><a name="b84235270611508"></a><a name="b84235270611508"></a>Public Images</strong> tab, and select <strong id="b842352706164154"><a name="b842352706164154"></a><a name="b842352706164154"></a>ECS system disk image</strong> and <strong id="b842352706164159"><a name="b842352706164159"></a><a name="b842352706164159"></a>Windows</strong> from the drop-down lists, respectively.</p>
    </td>
    </tr>
    <tr id="row16638165131113"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p1163845116114"><a name="p1163845116114"></a><a name="p1163845116114"></a>Linux</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><a name="ul18638135151113"></a><a name="ul18638135151113"></a><ul id="ul18638135151113"><li>SUSE Linux Enterprise Server 11 SP4 64bit (The kernel version is 3.0.101-68-default or 3.0.101-80-default.)</li><li>SUSE Linux Enterprise Server 12 64bit (The kernel version is 3.12.51-52.31-default.)</li><li>SUSE Linux Enterprise Server 12 SP1 64bit (The kernel version is 3.12.67-60.64.24-default.)</li><li>SUSE Linux Enterprise Server 12 SP2 64bit (The kernel version is 4.4.74-92.35.1-default.)</li></ul>
    </td>
    </tr>
    </tbody>
    </table>



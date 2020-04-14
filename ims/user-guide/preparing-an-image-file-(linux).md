# Preparing an Image File<a name="EN-US_TOPIC_0030713198"></a>

You need to prepare an image file that meets the platform requirements.

**Table  1**  Linux image file requirements

<a name="table85212269215"></a>
<table><thead align="left"><tr id="row853426172112"><th class="cellrowborder" valign="top" width="23.51%" id="mcps1.2.3.1.1"><p id="p12530269215"><a name="p12530269215"></a><a name="p12530269215"></a>Image File Property</p>
</th>
<th class="cellrowborder" valign="top" width="76.49000000000001%" id="mcps1.2.3.1.2"><p id="p1753152611212"><a name="p1753152611212"></a><a name="p1753152611212"></a>Requirement</p>
</th>
</tr>
</thead>
<tbody><tr id="row1453162692112"><td class="cellrowborder" valign="top" width="23.51%" headers="mcps1.2.3.1.1 "><p id="p1253182672119"><a name="p1253182672119"></a><a name="p1253182672119"></a>OS</p>
</td>
<td class="cellrowborder" valign="top" width="76.49000000000001%" headers="mcps1.2.3.1.2 "><a name="ul889991962516"></a><a name="ul889991962516"></a><ul id="ul889991962516"><li>SUSE, Oracle Linux, Red Hat, Ubuntu, OpenSUSE, CentOS, Debian, Fedora, EulerOS, and NeoKylin</li><li>32-bit and 64-bit</li><li>The OS cannot be bound to hardware.</li><li>The OS must support full virtualization.</li></ul>
<p id="p1787815142817"><a name="p1787815142817"></a><a name="p1787815142817"></a>For details about the supported OS versions, see <a href="formats-and-oss-supported-for-external-image-files.md">Formats and OSs Supported for External Image Files</a>. These OSs support automatic configuration. For details, see <a href="what-changes-will-be-made-to-an-image-file-used-for-registering-a-private-image.md">What Changes Will Be Made to an Image File Used for Registering a Private Image?</a> For other OSs, check and install the Guest OS driver. On the image registration page, select <strong id="b103120441069"><a name="b103120441069"></a><a name="b103120441069"></a>Other Linux.</strong> After the image is imported, whether the system is started depends on the driver integrity.</p>
</td>
</tr>
<tr id="row1653182610212"><td class="cellrowborder" valign="top" width="23.51%" headers="mcps1.2.3.1.1 "><p id="p4532026152119"><a name="p4532026152119"></a><a name="p4532026152119"></a>Image format</p>
</td>
<td class="cellrowborder" valign="top" width="76.49000000000001%" headers="mcps1.2.3.1.2 "><p id="p17531426152112"><a name="p17531426152112"></a><a name="p17531426152112"></a>VMDK, VHD, QCOW2, RAW, VHDX, QED, VDI, QCOW, ZVHD2, and ZVHD</p>
</td>
</tr>
<tr id="row15536261217"><td class="cellrowborder" valign="top" width="23.51%" headers="mcps1.2.3.1.1 "><p id="p353142692117"><a name="p353142692117"></a><a name="p353142692117"></a>Image size</p>
</td>
<td class="cellrowborder" valign="top" width="76.49000000000001%" headers="mcps1.2.3.1.2 "><p id="p1498992571314"><a name="p1498992571314"></a><a name="p1498992571314"></a>The image size cannot exceed 128 GB.</p>
<div class="p" id="p14410175834710"><a name="p14410175834710"></a><a name="p14410175834710"></a>If the image size is between 128 GB and 1 TB, convert the image file into the RAW or ZVHD2 format and import the image through fast import.<a name="ul16854182355610"></a><a name="ul16854182355610"></a><ul id="ul16854182355610"><li>For details about how to convert the image file format, see <a href="quickly-importing-an-image-file-(linux).md#li2635823142815">image format conversion</a>.</li><li>For details about fast import, see <a href="quickly-importing-an-image-file-overview.md">fast image file import</a>.</li></ul>
</div>
</td>
</tr>
<tr id="row3531626162117"><td class="cellrowborder" valign="top" width="23.51%" headers="mcps1.2.3.1.1 "><p id="p35313261219"><a name="p35313261219"></a><a name="p35313261219"></a>Network capability</p>
</td>
<td class="cellrowborder" valign="top" width="76.49000000000001%" headers="mcps1.2.3.1.2 "><p id="p197299113553"><a name="p197299113553"></a><a name="p197299113553"></a>The following operation is mandatory. If the operation is not performed, the startup or network capability will be abnormal.</p>
<a name="ul10942125439"></a><a name="ul10942125439"></a><ul id="ul10942125439"><li><a href="deleting-files-in-the-network-rule-directory.md">Deleting files in the network rule directory</a></li><li><a href="setting-the-nic-to-dhcp-(linux).md">Setting the NIC to DHCP</a></li></ul>
<p id="p1256214156553"><a name="p1256214156553"></a><a name="p1256214156553"></a>The following value-added operations are optional:</p>
<a name="ul1454250115714"></a><a name="ul1454250115714"></a><ul id="ul1454250115714"><li>Enabling NIC multi-queue<p id="p733615559471"><a name="p733615559471"></a><a name="p733615559471"></a>NIC multi-queue routes NIC interruptions among multiple CPUs to balance load and increase network PPS and bandwidth. For details, see <a href="how-do-i-set-nic-multi-queue-feature-of-an-image.md">How Do I Set NIC Multi-Queue Feature of an Image?</a></p>
</li></ul>
</td>
</tr>
<tr id="row1558028151811"><td class="cellrowborder" valign="top" width="23.51%" headers="mcps1.2.3.1.1 "><p id="p558018891810"><a name="p558018891810"></a><a name="p558018891810"></a>Tool</p>
</td>
<td class="cellrowborder" valign="top" width="76.49000000000001%" headers="mcps1.2.3.1.2 "><p id="p1657443219185"><a name="p1657443219185"></a><a name="p1657443219185"></a>You are advised to install Cloud-Init.</p>
<p id="p3276725102112"><a name="p3276725102112"></a><a name="p3276725102112"></a>Cloud-Init is an open-source cloud initialization tool. When creating an <span id="text1019113652116"><a name="text1019113652116"></a><a name="text1019113652116"></a>ECS</span><span id="text101922036142115"><a name="text101922036142115"></a><a name="text101922036142115"></a></span> from an image with Cloud-Init, you can use the user data injection function to inject customized initialization information (for example, setting the <span id="text10193113618218"><a name="text10193113618218"></a><a name="text10193113618218"></a>ECS</span><span id="text919323642112"><a name="text919323642112"></a><a name="text919323642112"></a></span> login password). You can also configure and manage a running <span id="text6194936132114"><a name="text6194936132114"></a><a name="text6194936132114"></a>ECS</span><span id="text12195036202113"><a name="text12195036202113"></a><a name="text12195036202113"></a></span> by querying and using metadata. If Cloud-Init is not installed, you cannot configure an <span id="text19766405228"><a name="text19766405228"></a><a name="text19766405228"></a>ECS</span><span id="text897719408224"><a name="text897719408224"></a><a name="text897719408224"></a></span>. As a result, you can only use the password in the image file to log in to the <span id="text297884042211"><a name="text297884042211"></a><a name="text297884042211"></a>ECS</span><span id="text179791540112213"><a name="text179791540112213"></a><a name="text179791540112213"></a></span>.</p>
<p id="p142251129111720"><a name="p142251129111720"></a><a name="p142251129111720"></a>For details, see <a href="installing-cloud-init.md">Installing Cloud-Init</a>.</p>
</td>
</tr>
<tr id="row20361842182918"><td class="cellrowborder" valign="top" width="23.51%" headers="mcps1.2.3.1.1 "><p id="p113644216291"><a name="p113644216291"></a><a name="p113644216291"></a>Driver</p>
</td>
<td class="cellrowborder" valign="top" width="76.49000000000001%" headers="mcps1.2.3.1.2 "><p id="p857214531434"><a name="p857214531434"></a><a name="p857214531434"></a><a href="installing-native-xen-and-kvm-drivers.md">Installing native Xen and KVM drivers</a></p>
</td>
</tr>
<tr id="row7637883311"><td class="cellrowborder" valign="top" width="23.51%" headers="mcps1.2.3.1.1 "><p id="p56591949191514"><a name="p56591949191514"></a><a name="p56591949191514"></a>File system</p>
</td>
<td class="cellrowborder" valign="top" width="76.49000000000001%" headers="mcps1.2.3.1.2 "><a name="ul6303717181618"></a><a name="ul6303717181618"></a><ul id="ul6303717181618"><li><a href="changing-the-disk-identifier-in-the-grub-configuration-file-to-uuid.md">Changing the disk identifier in the GRUB configuration file to UUID</a></li><li><a href="changing-the-disk-identifier-in-the-fstab-file-to-uuid.md">Changing the disk identifier in the fstab file to UUID</a></li></ul>
</td>
</tr>
<tr id="row1661924212312"><td class="cellrowborder" valign="top" width="23.51%" headers="mcps1.2.3.1.1 "><p id="p196201042152313"><a name="p196201042152313"></a><a name="p196201042152313"></a>Other requirements</p>
</td>
<td class="cellrowborder" valign="top" width="76.49000000000001%" headers="mcps1.2.3.1.2 "><a name="ul3863205042313"></a><a name="ul3863205042313"></a><ul id="ul3863205042313"><li>Currently, images with data disks cannot be created. The image file must contain only the system disk, and the system disk size must be [40GB, 1024GB].</li><li>The initial password in the image file contains at least uppercase letters, lowercase letters, digits, and special characters (!@$%^-_=+[{}]:,./?).</li><li>The boot partition and system partition of external image files must be on the same disk.</li><li>Generally, the image boot mode is BIOS. Some OS images support the UEFI boot mode. For details, see "OSs Supporting UEFI Boot Mode" in <em id="i14866344124018"><a name="i14866344124018"></a><a name="i14866344124018"></a>Image Service Management User Guide</em>.</li><li>The image file cannot be encrypted. Otherwise, ECSs created from the registered image may not work properly.</li><li>The <strong id="b1358135519411"><a name="b1358135519411"></a><a name="b1358135519411"></a>/etc/fstab</strong> file cannot contain automatic mounting information of non-system disks. Otherwise, the login to the created <span id="text419153562410"><a name="text419153562410"></a><a name="text419153562410"></a>ECS</span><span id="text141912358241"><a name="text141912358241"></a><a name="text141912358241"></a></span> may fail.</li><li>If the external image file uses the LVM as the system disk and the private image is registered from the external image file, ECSs created from the private image do not support file injection.</li><li>If the VM where the external image file is located has been shut down, it must be a graceful shutdown. Otherwise, a blue screen may occur when the <span id="text17974041924"><a name="text17974041924"></a><a name="text17974041924"></a></span><span id="text169748419214"><a name="text169748419214"></a><a name="text169748419214"></a>ECS</span> created from the private image is started.</li></ul>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>-   You are advised to complete the file system, network, and driver configurations in  [Table 1](#table85212269215)  on the VM and then export the image file. You can also complete the configurations on ECSs. For details, see  [What Do I Do If the Initial Configurations of a Linux External Image File Are Not Completed Before the File Is Exported?](what-do-i-do-if-the-initial-configurations-of-a-linux-external-image-file-are-not-completed-before-t.md)  
>-   Currently, only RAW and ZVHD2 files can be imported \(not larger than 1 TB\). In addition to the requirements described in  [Table 1](#table85212269215), a bitmap file needs to be generated for the RAW image file. The bitmap file is uploaded together with the image file. For details, see  [Quickly Importing an Image File](quickly-importing-an-image-file.md).  


# Automatically Changing a Xen ECS to a KVM ECS \(Linux\)<a name="EN-US_TOPIC_0120890833"></a>

## Scenarios<a name="section9265624184119"></a>

Before changing a Xen ECS running Linux to a KVM ECS, make sure that the desired drivers have been installed on the ECS and that the ECS has been configured.

This section describes how to use a script to automatically install drivers on the ECS, configure the device name, and change Xen to KVM.

>![](/images/icon-note.gif) **NOTE:**   
>-   Xen ECSs include S1, C1, C2, and M1 ECSs.  
>-   To obtain KVM ECSs, see the  **Virtualization Type**  column in  [ECSs](ecs-specifications.md).  
>-   To support both Xen and KVM, Linux ECSs require the xen-pv and Virtio drivers. Before changing a Xen ECS to a KVM ECS, make sure that the Linux ECS has been configured, including installing drivers and configuring automatic disk attachment.  

## Constraints<a name="section32289014501"></a>

-   If a Linux ECS is attached with a logical LVM disk or a RAID disk array consisting of multiple physical disks, the ECS specifications cannot be modified. Otherwise, data may be lost.
-   A Xen ECS with more than 24 VBD disks attached cannot be changed to a KVM ECS.
-   A Xen ECS can be changed to a KVM ECS, but a KVM ECS cannot be changed to a Xen ECS.

## Procedure<a name="section117911026122211"></a>

[Figure 1](#fig1685151934912)  shows the flowchart for automatically changing a Xen ECS to a KVM ECS.

**Figure  1**  Flowchart for automatically changing a Xen ECS to a KVM ECS<a name="fig1685151934912"></a>  
![](figures/flowchart-for-automatically-changing-a-xen-ecs-to-a-kvm-ecs.png "flowchart-for-automatically-changing-a-xen-ecs-to-a-kvm-ecs")

**Table  1**  OSs that support automatic configuration using a script

<a name="table134451651171116"></a>
<table><thead align="left"><tr id="row1446115171116"><th class="cellrowborder" valign="top" width="41.21%" id="mcps1.2.3.1.1"><p id="p325218580119"><a name="p325218580119"></a><a name="p325218580119"></a>OS</p>
</th>
<th class="cellrowborder" valign="top" width="58.79%" id="mcps1.2.3.1.2"><p id="p1644071133213"><a name="p1644071133213"></a><a name="p1644071133213"></a>Version</p>
</th>
</tr>
</thead>
<tbody><tr id="row3446155111113"><td class="cellrowborder" valign="top" width="41.21%" headers="mcps1.2.3.1.1 "><p id="p444615141119"><a name="p444615141119"></a><a name="p444615141119"></a>CentOS</p>
</td>
<td class="cellrowborder" valign="top" width="58.79%" headers="mcps1.2.3.1.2 "><a name="ul1571531819322"></a><a name="ul1571531819322"></a><ul id="ul1571531819322"><li>CentOS 7</li><li>CentOS 6</li></ul>
</td>
</tr>
<tr id="row04461351201115"><td class="cellrowborder" valign="top" width="41.21%" headers="mcps1.2.3.1.1 "><p id="p15446165119112"><a name="p15446165119112"></a><a name="p15446165119112"></a>Debian</p>
</td>
<td class="cellrowborder" valign="top" width="58.79%" headers="mcps1.2.3.1.2 "><a name="ul1975518595322"></a><a name="ul1975518595322"></a><ul id="ul1975518595322"><li>Debian 9</li><li>Debian 8</li></ul>
</td>
</tr>
<tr id="row044655111114"><td class="cellrowborder" valign="top" width="41.21%" headers="mcps1.2.3.1.1 "><p id="p64467513111"><a name="p64467513111"></a><a name="p64467513111"></a>EulerOS</p>
</td>
<td class="cellrowborder" valign="top" width="58.79%" headers="mcps1.2.3.1.2 "><a name="ul55051414343"></a><a name="ul55051414343"></a><ul id="ul55051414343"><li>EulerOS 2</li></ul>
</td>
</tr>
<tr id="row11446151131118"><td class="cellrowborder" valign="top" width="41.21%" headers="mcps1.2.3.1.1 "><p id="p12446651101120"><a name="p12446651101120"></a><a name="p12446651101120"></a>OpenSUSE</p>
</td>
<td class="cellrowborder" valign="top" width="58.79%" headers="mcps1.2.3.1.2 "><a name="ul1088512663414"></a><a name="ul1088512663414"></a><ul id="ul1088512663414"><li>OpenSUSE 42</li><li>OpenSUSE 15</li></ul>
</td>
</tr>
<tr id="row64474513111"><td class="cellrowborder" valign="top" width="41.21%" headers="mcps1.2.3.1.1 "><p id="p0447205141114"><a name="p0447205141114"></a><a name="p0447205141114"></a>SUSE</p>
</td>
<td class="cellrowborder" valign="top" width="58.79%" headers="mcps1.2.3.1.2 "><a name="ul237783293420"></a><a name="ul237783293420"></a><ul id="ul237783293420"><li>SUSE 15</li><li>SUSE 12</li><li>SUSE 11</li></ul>
</td>
</tr>
<tr id="row37671195362"><td class="cellrowborder" valign="top" width="41.21%" headers="mcps1.2.3.1.1 "><p id="p576861915364"><a name="p576861915364"></a><a name="p576861915364"></a>SUSE-SAP</p>
</td>
<td class="cellrowborder" valign="top" width="58.79%" headers="mcps1.2.3.1.2 "><a name="ul28601351153411"></a><a name="ul28601351153411"></a><ul id="ul28601351153411"><li>SUSE-SAP 12</li></ul>
</td>
</tr>
<tr id="row167687194367"><td class="cellrowborder" valign="top" width="41.21%" headers="mcps1.2.3.1.1 "><p id="p117681419193614"><a name="p117681419193614"></a><a name="p117681419193614"></a>Ubuntu</p>
</td>
<td class="cellrowborder" valign="top" width="58.79%" headers="mcps1.2.3.1.2 "><a name="ul8168132620357"></a><a name="ul8168132620357"></a><ul id="ul8168132620357"><li>Ubuntu 18.04</li><li>Ubuntu 16.04</li><li>Ubuntu 14.04</li></ul>
</td>
</tr>
<tr id="row1276871910366"><td class="cellrowborder" valign="top" width="41.21%" headers="mcps1.2.3.1.1 "><p id="p19768121915361"><a name="p19768121915361"></a><a name="p19768121915361"></a>Red Hat</p>
</td>
<td class="cellrowborder" valign="top" width="58.79%" headers="mcps1.2.3.1.2 "><a name="ul747716398357"></a><a name="ul747716398357"></a><ul id="ul747716398357"><li>Red Hat 7</li><li>Red Hat 6</li></ul>
</td>
</tr>
<tr id="row1293153833611"><td class="cellrowborder" valign="top" width="41.21%" headers="mcps1.2.3.1.1 "><p id="p39317386368"><a name="p39317386368"></a><a name="p39317386368"></a>Fedora</p>
</td>
<td class="cellrowborder" valign="top" width="58.79%" headers="mcps1.2.3.1.2 "><a name="ul78139293613"></a><a name="ul78139293613"></a><ul id="ul78139293613"><li>Fedora 29</li><li>Fedora 28</li><li>Fedora 27</li><li>Fedora 26</li></ul>
</td>
</tr>
<tr id="row19400164913364"><td class="cellrowborder" valign="top" width="41.21%" headers="mcps1.2.3.1.1 "><p id="p1400154915369"><a name="p1400154915369"></a><a name="p1400154915369"></a>Oracle Linux</p>
</td>
<td class="cellrowborder" valign="top" width="58.79%" headers="mcps1.2.3.1.2 "><a name="ul6707122793617"></a><a name="ul6707122793617"></a><ul id="ul6707122793617"><li>Oracle Linux 7</li></ul>
</td>
</tr>
</tbody>
</table>

[Table 2](#table128603262223)  describes the operations.

**Table  2**  Procedure for automatically changing a Xen ECS to a KVM ECS using a script

<a name="table128603262223"></a>
<table><thead align="left"><tr id="row198591826152211"><th class="cellrowborder" valign="top" width="35.4%" id="mcps1.2.3.1.1"><p id="p485942616225"><a name="p485942616225"></a><a name="p485942616225"></a>Step</p>
</th>
<th class="cellrowborder" valign="top" width="64.60000000000001%" id="mcps1.2.3.1.2"><p id="p2859142615221"><a name="p2859142615221"></a><a name="p2859142615221"></a>Operation</p>
</th>
</tr>
</thead>
<tbody><tr id="row108591226182214"><td class="cellrowborder" valign="top" width="35.4%" headers="mcps1.2.3.1.1 "><p id="p1859122642211"><a name="p1859122642211"></a><a name="p1859122642211"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="64.60000000000001%" headers="mcps1.2.3.1.2 "><p id="p1985962611223"><a name="p1985962611223"></a><a name="p1985962611223"></a><a href="#section125278281411">(Optional) Step 1: Back Up System Disk Data</a></p>
</td>
</tr>
<tr id="row18859122662211"><td class="cellrowborder" valign="top" width="35.4%" headers="mcps1.2.3.1.1 "><p id="p16859122620224"><a name="p16859122620224"></a><a name="p16859122620224"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="64.60000000000001%" headers="mcps1.2.3.1.2 "><p id="p5859126132217"><a name="p5859126132217"></a><a name="p5859126132217"></a><a href="#section2599649145513">Step 2: Using a Script to Automatically Install Drivers</a></p>
</td>
</tr>
<tr id="row19859122619222"><td class="cellrowborder" valign="top" width="35.4%" headers="mcps1.2.3.1.1 "><p id="p1859162610226"><a name="p1859162610226"></a><a name="p1859162610226"></a>3</p>
</td>
<td class="cellrowborder" valign="top" width="64.60000000000001%" headers="mcps1.2.3.1.2 "><p id="p38591626152216"><a name="p38591626152216"></a><a name="p38591626152216"></a><a href="#section1815152131917">Step 3: Modify Specifications</a></p>
</td>
</tr>
<tr id="row1186042632210"><td class="cellrowborder" valign="top" width="35.4%" headers="mcps1.2.3.1.1 "><p id="p585916261226"><a name="p585916261226"></a><a name="p585916261226"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="64.60000000000001%" headers="mcps1.2.3.1.2 "><p id="p685922613229"><a name="p685922613229"></a><a name="p685922613229"></a><a href="#section2625525131519">(Optional) Step 4: Check Disk Attachment</a></p>
</td>
</tr>
</tbody>
</table>

## \(Optional\) Step 1: Back Up System Disk Data<a name="section125278281411"></a>

Before modifying the specifications, back up the system disk and install the driver on the ECS. Otherwise, the ECS will be unavailable after the modification is performed. If the ECS becomes unavailable, the fault can be rectified by reinstalling the OS, which may cause data loss in your system disk.

For instructions about how to back up the system disk, see "Getting Started \>  [Creating a VBS Backup](https://docs.otc.t-systems.com/en-us/usermanual/vbs/en-us_topic_0015667820.html)" in  _Volume Backup Service User Guide_.

## Step 2: Using a Script to Automatically Install Drivers<a name="section2599649145513"></a>

Perform the operations described in this section if your ECS supports the configuration using a script. If your ECS does not support this mode, manually configure it. For details, see  [Manually Changing a Xen ECS to a KVM ECS \(Linux\)](manually-changing-a-xen-ecs-to-a-kvm-ecs-(linux).md).

>![](/images/icon-note.gif) **NOTE:**   
>For details about the ECSs supporting the configuration using a script, see  [Procedure](#section117911026122211).  

1.  Log in to the ECS.
2.  Run the following command to download the driver installation script to the  **root**  directory:

    **curl** _URL_ **\> \~/resize\_ecs\_modify\_linux.sh**

    In the preceding command,  _URL_  is the address for downloading the specifications modification script.

    URL:  [http://ecs-instance-driver.obs.eu-de.otc.t-systems.com/resize\_ecs\_modify\_linux.sh](http://ecs-instance-driver.obs.eu-de.otc.t-systems.com/resize_ecs_modify_linux.sh)

3.  Run the following command to execute the script which automatically checks and installs the native Xen PV driver and virtio driver:

    **bash resize\_ecs\_modify\_linux.sh**

    **Figure  2**  Executing the script<a name="fig1527312381829"></a>  
    ![](figures/executing-the-script.png "executing-the-script")

4.  Wait until the script execution is complete. If the message "\{_Image name_\} already contain xen and virtio driver" is displayed, the driver has been installed.

    Perform the operations described in  [Step 3: Modify Specifications](#section1815152131917). Otherwise, execute the script again or contact customer service for technical support.

    **Figure  3**  Successful script execution<a name="fig12201134171014"></a>  
    ![](figures/successful-script-execution.png "successful-script-execution")

    >![](/images/icon-note.gif) **NOTE:**   
    >-   Make sure that the ECS has been configured successfully. Otherwise, the ECS will be unavailable after the modification is performed. If the operation failed, follow the instructions provided in  [Manually Changing a Xen ECS to a KVM ECS \(Linux\)](manually-changing-a-xen-ecs-to-a-kvm-ecs-(linux).md)  for manual operations.  
    >-   FAQs related to a script installation failure:  
    >    -   [What Should I Do If Executing a Driver Installation Script Failed on an ECS Running CentOS 5?](what-should-i-do-if-executing-a-driver-installation-script-failed-on-an-ecs-running-centos-5.md)  
    >    -   [What Should I Do If Executing a Driver Installation Script Failed When I Attempted to Modify the Specifications of a Linux ECS?](what-should-i-do-if-executing-a-driver-installation-script-failed-when-i-attempted-to-modify-the-spe.md)  


## Step 3: Modify Specifications<a name="section1815152131917"></a>

1.  Log in to management console.
2.  Click  ![](figures/icon-region-0.png)  in the upper left corner and select the desired region and project.
3.  Under  **Computing**, click  **Elastic Cloud Server**.
4.  On the  **Elastic Cloud Server**  page, view the status of the target ECS.

    If the ECS is not in  **Stopped**  state, click  **More**  in the  **Operation**  column and select  **Stop**.

5.  Click  **More**  in the  **Operation**  column and select  **Modify Specifications**.

    The  **Modify ECS Specifications**  page is displayed.

6.  Select the new ECS type, vCPUs, and memory as prompted.
7.  \(Optional\) Set  **DeH**.

    If the ECS is created on a DeH, the system allows you to change the DeH.

    To do so, select the target DeH from the drop-down list. If no DeH is available in the drop-down list, remaining DeH resources are insufficient and cannot be used to create the ECS with specifications modified.

8.  Select the check box to confirm the ECS configuration.
9.  Click  **OK**.

## \(Optional\) Step 4: Check Disk Attachment<a name="section2625525131519"></a>

After a Xen ECS is changed to a KVM ECS, disk attachment may fail. Therefore, check disk attachment after specifications modification. If disks are properly attached, the specifications modification is successful.

-   Linux

    For details, see  [What Should I Do If the Disk of a Linux ECS Becomes Offline After the ECS Specifications Are Modified?](what-should-i-do-if-the-disk-of-a-linux-ecs-becomes-offline-after-the-ecs-specifications-are-modifie.md)


## Follow-up Procedure<a name="section7460163511720"></a>

If the ECS with specifications modified is displayed in the ECS list but its OS cannot be started after the ECS is remotely logged in, reinstall the ECS OS to rectify this fault. For details, see  [Reinstalling the OS](reinstalling-the-os.md).


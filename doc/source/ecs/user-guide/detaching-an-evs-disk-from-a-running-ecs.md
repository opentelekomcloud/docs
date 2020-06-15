# Detaching an EVS Disk from a Running ECS<a name="EN-US_TOPIC_0036046828"></a>

## Scenarios<a name="section15787511144344"></a>

An EVS disk attached to an ECS can function as a system disk or data disk.

-   EVS disks mounted to  **/dev/sda**  or  **/dev/vda**  function as system disks. You can only detach system disks offline. Before detaching a system disk from an ECS, you must stop the ECS.
-   EVS disks mounted to other locations function as data disks. In addition to offline detachment, data disks can be detached online if the OS running on the ECS supports this feature.

This section describes how to detach a disk from a running ECS.

## Constraints<a name="section34475334143121"></a>

-   The EVS disk to be detached must be mounted at a location other than  **/dev/sda**  or  **/dev/vda**.

    EVS disks mounted to  **/dev/sda**  or  **/dev/vda**  are system disks and cannot be detached from running ECSs.

-   Before detaching an EVS disk from a running Windows ECS, make sure that OTC tools have been installed on the ECS and that the tools are running properly.
-   Before detaching an EVS disk from a running Windows ECS, ensure that no program is reading data from or writing data to the disk. Otherwise, data will be lost.
-   SCSI EVS disks cannot be detached from running Windows ECSs.

-   Before detaching an EVS disk from a running Linux ECS, you must log in to the ECS and run the  **umount**  command to cancel the association between the disk and the file system. In addition, ensure that no program is reading data from or writing data to the disk. Otherwise, detaching the disk will fail.

## Notes<a name="section58087347152725"></a>

-   On a Windows ECS, if the disk is in non-offline state, the system forcibly detaches the EVS disk. If this occurs, the system may generate a xenvbd alarm. You can ignore this alarm.

    >![](/images/icon-note.gif) **NOTE:**   
    >To view the status of an EVS disk, perform the following operations:  
    >1.  Click  **Start**  in the task bar. In the displayed  **Start**  menu, right-click  **Computer**  and choose  **Manage**  from the shortcut menu.  
    >    The  **Server Manager**  page is displayed.  
    >2.  In the navigation pane on the left, choose  **Storage**  \>  **Disk Management**.  
    >    The EVS disk list is displayed in the right pane.  
    >3.  View the status of each EVS disk.  

-   Do not detach an EVS disk from an ECS that is being started, stopped, or restarted.
-   Do not detach an EVS disk from a running ECS whose OS does not support this feature. OSs supporting EVS disk detachment from a running ECS are listed in  [OSs Supporting EVS Disk Detachment from a Running ECS](#section21417196143518).
-   For a running Linux ECS, the drive letter may be changed after an EVS disk is detached from it and then attached to it again. This is a normal case due to the drive letter allocation mechanism of the Linux system.
-   For a running Linux ECS, the drive letter may be changed after an EVS disk is detached from it and the ECS is restarted. This is a normal case due to the drive letter allocation mechanism of the Linux system.

## OSs Supporting EVS Disk Detachment from a Running ECS<a name="section21417196143518"></a>

OSs supporting EVS disk detachment from a running ECS include two parts:

-   For the first part, see  [External Image Files and Supported OSs](https://docs.otc.t-systems.com/en-us/usermanual/ims/en-us_topic_0030713143.html).
-   [Table 1](#table9271324195455)  lists the second part of supported OSs.

    **Table  1**  OSs supporting EVS disk detachment from a running ECS

    <a name="table9271324195455"></a>
    <table><thead align="left"><tr id="row29095028195455"><th class="cellrowborder" valign="top" width="35.709999999999994%" id="mcps1.2.3.1.1"><p id="p3874810195455"><a name="p3874810195455"></a><a name="p3874810195455"></a>OS</p>
    </th>
    <th class="cellrowborder" valign="top" width="64.29%" id="mcps1.2.3.1.2"><p id="p45424225195455"><a name="p45424225195455"></a><a name="p45424225195455"></a>Version</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6164841195455"><td class="cellrowborder" rowspan="4" valign="top" width="35.709999999999994%" headers="mcps1.2.3.1.1 "><p id="p29590097195455"><a name="p29590097195455"></a><a name="p29590097195455"></a>CentOS</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.29%" headers="mcps1.2.3.1.2 "><p id="p47987633195455"><a name="p47987633195455"></a><a name="p47987633195455"></a>7.3 64bit</p>
    </td>
    </tr>
    <tr id="row29235518195455"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p17103579195455"><a name="p17103579195455"></a><a name="p17103579195455"></a>7.2 64bit</p>
    </td>
    </tr>
    <tr id="row19714485195455"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p27960603195455"><a name="p27960603195455"></a><a name="p27960603195455"></a>6.8 64bit</p>
    </td>
    </tr>
    <tr id="row50318836195455"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p33382838195455"><a name="p33382838195455"></a><a name="p33382838195455"></a>6.7 64bit</p>
    </td>
    </tr>
    <tr id="row32010086195455"><td class="cellrowborder" rowspan="2" valign="top" width="35.709999999999994%" headers="mcps1.2.3.1.1 "><p id="p42680203195455"><a name="p42680203195455"></a><a name="p42680203195455"></a>Debian</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.29%" headers="mcps1.2.3.1.2 "><p id="p34544441195455"><a name="p34544441195455"></a><a name="p34544441195455"></a>8.6.0 64bit</p>
    </td>
    </tr>
    <tr id="row42464514195455"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p40785593195455"><a name="p40785593195455"></a><a name="p40785593195455"></a>8.5.0 64bit</p>
    </td>
    </tr>
    <tr id="row31526020195455"><td class="cellrowborder" rowspan="2" valign="top" width="35.709999999999994%" headers="mcps1.2.3.1.1 "><p id="p3470819195455"><a name="p3470819195455"></a><a name="p3470819195455"></a>Fedora</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.29%" headers="mcps1.2.3.1.2 "><p id="p12700947195455"><a name="p12700947195455"></a><a name="p12700947195455"></a>25 64bit</p>
    </td>
    </tr>
    <tr id="row7771181195618"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p28046932195618"><a name="p28046932195618"></a><a name="p28046932195618"></a>24 64bit</p>
    </td>
    </tr>
    <tr id="row48634140195618"><td class="cellrowborder" rowspan="4" valign="top" width="35.709999999999994%" headers="mcps1.2.3.1.1 "><p id="p35054084195618"><a name="p35054084195618"></a><a name="p35054084195618"></a>SUSE</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.29%" headers="mcps1.2.3.1.2 "><p id="p20808552195618"><a name="p20808552195618"></a><a name="p20808552195618"></a>SUSE Linux Enterprise Server 12 SP2 64bit</p>
    </td>
    </tr>
    <tr id="row56745994195618"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p28769574195618"><a name="p28769574195618"></a><a name="p28769574195618"></a>SUSE Linux Enterprise Server 12 SP1 64bit</p>
    </td>
    </tr>
    <tr id="row53117304195618"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p700567195618"><a name="p700567195618"></a><a name="p700567195618"></a>SUSE Linux Enterprise Server 11 SP4 64bit</p>
    </td>
    </tr>
    <tr id="row1719114311319"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p5009498811319"><a name="p5009498811319"></a><a name="p5009498811319"></a>SUSE Linux Enterprise Server 12 64bit</p>
    </td>
    </tr>
    <tr id="row588467195618"><td class="cellrowborder" rowspan="2" valign="top" width="35.709999999999994%" headers="mcps1.2.3.1.1 "><p id="p5296204195618"><a name="p5296204195618"></a><a name="p5296204195618"></a>OpenSUSE</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.29%" headers="mcps1.2.3.1.2 "><p id="p26339408195618"><a name="p26339408195618"></a><a name="p26339408195618"></a>42.2 64bit</p>
    </td>
    </tr>
    <tr id="row14494860195618"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p30661931195618"><a name="p30661931195618"></a><a name="p30661931195618"></a>42.1 64bit</p>
    </td>
    </tr>
    <tr id="row48454688195618"><td class="cellrowborder" rowspan="4" valign="top" width="35.709999999999994%" headers="mcps1.2.3.1.1 "><p id="p33439014195618"><a name="p33439014195618"></a><a name="p33439014195618"></a>Oracle Linux Server release</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.29%" headers="mcps1.2.3.1.2 "><p id="p24205579195618"><a name="p24205579195618"></a><a name="p24205579195618"></a>7.3 64bit</p>
    </td>
    </tr>
    <tr id="row44683344195810"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p26359341195810"><a name="p26359341195810"></a><a name="p26359341195810"></a>7.2 64bit</p>
    </td>
    </tr>
    <tr id="row6869729195810"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p41976870195810"><a name="p41976870195810"></a><a name="p41976870195810"></a>6.8 64bit</p>
    </td>
    </tr>
    <tr id="row49642196195810"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p17483405195810"><a name="p17483405195810"></a><a name="p17483405195810"></a>6.7 64bit</p>
    </td>
    </tr>
    <tr id="row28948492195810"><td class="cellrowborder" rowspan="3" valign="top" width="35.709999999999994%" headers="mcps1.2.3.1.1 "><p id="p59209837195810"><a name="p59209837195810"></a><a name="p59209837195810"></a>Ubuntu Server</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.29%" headers="mcps1.2.3.1.2 "><p id="p31267532195810"><a name="p31267532195810"></a><a name="p31267532195810"></a>16.04 64bit</p>
    </td>
    </tr>
    <tr id="row66691124195810"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p31012055195810"><a name="p31012055195810"></a><a name="p31012055195810"></a>14.04 64bit</p>
    </td>
    </tr>
    <tr id="row29984127195810"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p48048103195810"><a name="p48048103195810"></a><a name="p48048103195810"></a>14.04.4 64bit</p>
    </td>
    </tr>
    <tr id="row58019688195810"><td class="cellrowborder" rowspan="3" valign="top" width="35.709999999999994%" headers="mcps1.2.3.1.1 "><p id="p52415150195810"><a name="p52415150195810"></a><a name="p52415150195810"></a>Windows (SCSI EVS disks cannot be detached from a running ECS.)</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.29%" headers="mcps1.2.3.1.2 "><p id="p17768768195810"><a name="p17768768195810"></a><a name="p17768768195810"></a>Windows Server 2008 R2 Enterprise 64bit</p>
    </td>
    </tr>
    <tr id="row17974643195810"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p17286382195810"><a name="p17286382195810"></a><a name="p17286382195810"></a>Windows Server 2012 R2 Standard 64bit</p>
    </td>
    </tr>
    <tr id="row5831657195810"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p23420035195810"><a name="p23420035195810"></a><a name="p23420035195810"></a>Windows Server 2016 R2 Standard 64bit</p>
    </td>
    </tr>
    <tr id="row24482463195810"><td class="cellrowborder" rowspan="2" valign="top" width="35.709999999999994%" headers="mcps1.2.3.1.1 "><p id="p19015578195810"><a name="p19015578195810"></a><a name="p19015578195810"></a>Red Hat Linux Enterprise</p>
    </td>
    <td class="cellrowborder" valign="top" width="64.29%" headers="mcps1.2.3.1.2 "><p id="p63866841195810"><a name="p63866841195810"></a><a name="p63866841195810"></a>7.3 64bit</p>
    </td>
    </tr>
    <tr id="row39384495195810"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p55812053195810"><a name="p55812053195810"></a><a name="p55812053195810"></a>6.8 64bit</p>
    </td>
    </tr>
    </tbody>
    </table>


>![](/images/icon-note.gif) **NOTE:**   
>Online detachment is not supported by the ECSs running OSs not listed in the preceding table. For such ECSs, stop the ECSs before detaching disks from them to prevent any possible problems from occurring.  

## Procedure<a name="section4606494215457"></a>

1.  On the  **Elastic Cloud Server**  page, click the name of the ECS from which the EVS disk is to be detached. The page providing details about the ECS is displayed.
2.  Click the  **Disks**  tab. Locate the row containing the EVS disk to be detached and click  **Detach**.


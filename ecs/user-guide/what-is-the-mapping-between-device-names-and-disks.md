# What Is the Mapping Between Device Names and Disks?<a name="EN-US_TOPIC_0103285575"></a>

## Scenarios<a name="section1021919499213"></a>

After users logged in to a Linux ECS and viewed disk information, they found that the disk device names were different from those displayed on the management console and could not identify the ECS to which a specified disk was attached. This section describes how to obtain the device name used on an ECS according to the disk information displayed on the management console.

## Background<a name="section764152920234"></a>

Disk information displayed varies according to the ECS virtualization type. For the sake of convenience, KVM ECSs are called KVM instances, and Xen ECSs are called Xen instances.

## Obtaining the Disk Device Name of a KVM Instance<a name="section263542712262"></a>

1.  <a name="li1078411215720"></a>Obtain the disk information displayed on the management console.
    1.  Log in to the management console.
    2.  Under  **Computing**, click  **Elastic Cloud Server**.
    3.  Click the target ECS name in the ECS list.

        The page providing details about the ECS is displayed.

    4.  Click the  **Disks**  tab and then expand the disk information.
    5.  Check the device type and ID of the disk.

        -   If the device type is  **VBD**, go to  [2](#li65954291187).
        -   If the device name is  **SCSI**, go to  [3](#li9432436104811).

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >If  **Device Identifier**  is not displayed on the web page, stop the ECS and restart it.  


2.  <a name="li65954291187"></a>Check the device name of a VBD disk on the ECS.
    1.  Obtain the disk device ID by referring to  [1](#li1078411215720).

        The device ID of the VBD disk shows the PCI address of the disk on the ECS. The address is in the format of "DOMIN:BUS:SLOT.FUNCTION".

    2.  Log in to the ECS as user  **root**.
    3.  In  **/sys/bus/pci/devices/DOMIN:BUS:SLOT.FUNCTION/virtio\*/block**, view the device name.

        For example, if the device ID of the VBD disk is  **0000:00:05.0**, the device name is shown as follows:

        ```
        A90CF6C6-BEC0-0C44-8082-8C8610755B61:/sys/bus/pci/devices/0000:00:05.0/virtiol/block # ll /sys/bus/pci/devices/0000:00:05.0/virtio1/block total 0
        drwxr-xr-x 10 root root 0 May 22 11:01 vda
        ```

        The displayed information is the disk device name,  **/dev/vda**  in the preceding figure.

3.  <a name="li9432436104811"></a>Check the device name of a SCSI disk on the ECS.
    1.  Obtain the disk device ID by referring to  [1](#li1078411215720).

        The device ID of the SCSI disk displays the disk WWN on the ECS.

    2.  Log in to the ECS as user  **root**.
    3.  Run the following command to view the disk device name:

        **ll /dev/disk/by-id |grep** _**WWN**_**|grep scsi-3**

        ```
        [root@host-192-168-133-148 block]# ll /dev/disk/by-id/ |grep 6888603000008b32fa16688d09368506 |grep scsi-3
        lrwxrwxrwx 1 root root  9 May 21 20:22 scsi-36888603000008b32fa16688d09368506 -> ../../sda
        ```



## Obtaining the Disk Device Name of a Xen Instance<a name="section17916409263"></a>

1.  Obtain the disk information displayed on the management console.
    1.  Log in to the management console.
    2.  Under  **Computing**, click  **Elastic Cloud Server**.
    3.  Click the target ECS name in the ECS list.

        The page providing details about the ECS is displayed.

    4.  Click the  **Disks**  tab and then  ![](figures/icon-unfold.png)  to expand the disk information.
    5.  Check the device name, type, and ID of the disk.

        -   If the device type is  **VBD**, go to  [2](#li205963711149).
        -   If the device name is  **SCSI**, go to  [3](#li2253121473315).

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >If  **Device Identifier**  is not displayed on the web page, stop the ECS and restart it.  


2.  <a name="li205963711149"></a>Check the device name of a VBD disk on the ECS.

    For a VBD disk, the device name displayed on the management console corresponds to the disk device name viewed on the ECS. For details, see  [Table 1](#table050473316173).

    **Table  1**  Mapping between disk device names displayed on the management console and those obtained on the ECS

    <a name="table050473316173"></a>
    <table><thead align="left"><tr id="row105042033171717"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p750443301712"><a name="p750443301712"></a><a name="p750443301712"></a>Device Name (Management Console)</p>
    </th>
    <th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p750453319178"><a name="p750453319178"></a><a name="p750453319178"></a>Device Name (ECS)</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row950453313179"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p155054337177"><a name="p155054337177"></a><a name="p155054337177"></a>/dev/sd***</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p550520336178"><a name="p550520336178"></a><a name="p550520336178"></a>/dev/xvd***</p>
    </td>
    </tr>
    <tr id="row250523316173"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p450553318172"><a name="p450553318172"></a><a name="p450553318172"></a>/dev/vd***</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p8505133161717"><a name="p8505133161717"></a><a name="p8505133161717"></a>/dev/xvd***</p>
    </td>
    </tr>
    <tr id="row35051633151715"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p10505163314170"><a name="p10505163314170"></a><a name="p10505163314170"></a>/dev/xvd***</p>
    </td>
    <td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p195051333101715"><a name="p195051333101715"></a><a name="p195051333101715"></a>/dev/xvd***</p>
    </td>
    </tr>
    </tbody>
    </table>

    An example is provided as follows:

    If the device name displayed on the management console is  **/dev/sdb**, the device name of the device attached to the ECS is  **/dev/xvdb**.

3.  <a name="li2253121473315"></a>Check the device name of a SCSI disk on the ECS.
    1.  Obtain the disk device ID.

        The device ID of the SCSI disk displays the disk WWN on the ECS.

    2.  Log in to the ECS as user  **root**.
    3.  Run the following command to view the disk device name:

        **ll /dev/disk/by-id |grep** **_WWN_|grep scsi-3**

        ```
        [root@host-192-168-133-148 block]# ll /dev/disk/by-id/ |grep 6888603000008b32fa16688d09368506 |grep scsi-3
        lrwxrwxrwx 1 root root  9 May 21 20:22 scsi-36888603000008b32fa16688d09368506 -> ../../sda
        ```




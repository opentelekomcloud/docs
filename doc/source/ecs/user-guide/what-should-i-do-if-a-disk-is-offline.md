# What Should I Do If a Disk Is Offline?<a name="EN-US_TOPIC_0114225937"></a>

## Symptom<a name="section19665528155311"></a>

A disk attached to a Windows ECS is offline, and the system displays the message "The disk is offline because of policy set by an administrator."

**Figure  1**  Offline disk<a name="fig1167510561578"></a>  
![](figures/offline-disk.png "offline-disk")

## Possible Causes<a name="section16231817217"></a>

Windows has three types of SAN policies:  **OnlineAll**,  **OfflineShared**, and  **OfflineInternal**.

**Table  1**  SAN policies

<a name="table28191141038"></a>
<table><thead align="left"><tr id="row1581912410311"><th class="cellrowborder" valign="top" width="28.000000000000004%" id="mcps1.2.3.1.1"><p id="p18192049310"><a name="p18192049310"></a><a name="p18192049310"></a>SAN Policy</p>
</th>
<th class="cellrowborder" valign="top" width="72%" id="mcps1.2.3.1.2"><p id="p9819641738"><a name="p9819641738"></a><a name="p9819641738"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row178191347320"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.3.1.1 "><p id="p9819134231"><a name="p9819134231"></a><a name="p9819134231"></a>OnlineAll</p>
</td>
<td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.3.1.2 "><p id="p4819943310"><a name="p4819943310"></a><a name="p4819943310"></a>Indicates that all newly detected disks are automatically brought online.</p>
</td>
</tr>
<tr id="row581924937"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.3.1.1 "><p id="p1632122130"><a name="p1632122130"></a><a name="p1632122130"></a>OfflineShared</p>
</td>
<td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.3.1.2 "><p id="p183217225319"><a name="p183217225319"></a><a name="p183217225319"></a>Indicates that all newly detected disks on sharable buses, such as FC or iSCSI, are left offline by default, while disks on non-sharable buses are kept online.</p>
</td>
</tr>
<tr id="row981914132"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.3.1.1 "><p id="p198191441431"><a name="p198191441431"></a><a name="p198191441431"></a>OfflineInternal</p>
</td>
<td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.3.1.2 "><p id="p68199412320"><a name="p68199412320"></a><a name="p68199412320"></a>Indicates that all newly detected disks are left offline.</p>
</td>
</tr>
</tbody>
</table>

The SAN policy of certain Windows OSs, such as Windows Server 2008/2012 Enterprise Edition and Data Center Edition, is  **OfflineShared**  by default.

## Solution<a name="section65994290513"></a>

Use the disk partition management tool DiskPart to obtain and set the SAN policy on the ECS to  **OnlineAll**.

1.  Log in to the Windows ECS.
2.  Press  **Win+R**  to run  **cmd.exe**.
3.  Run the following command to access DiskPart:

    **diskpart**

4.  Run the following command to view the SAN policy on the ECS:

    **san**

    -   If the SAN policy is  **OnlineAll**, run the  **exit**  command to exit DiskPart.

    -   If the SAN policy is not  **OnlineAll**, go to step  [5](#li5934113914122).

5.  <a name="li5934113914122"></a>Run the following command to change the SAN policy to  **OnlineAll**:

    **san policy=onlineall**

6.  \(Optional\) Use the ECS with the SAN policy changed to create a private image for the configuration to take effect permanently. After an ECS is created using this private image, the disks attached to the ECS are online by default. You only need to initialize them.


# Changing a Xen ECS to a KVM ECS \(Windows\)<a name="EN-US_TOPIC_0100593628"></a>

## Scenarios<a name="section9265624184119"></a>

Before changing a Xen ECS running Windows to a KVM ECS, make sure that PV driver and UVP VMTools have been installed on the Windows ECS.

This section describes how to install the PV driver and UVP VMTools and change Xen to KVM.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>-   Xen ECSs include S1, C1, C2, and M1 ECSs.  
>-   To obtain KVM ECSs, see the  **Virtualization Type**  column in  [ECS Specifications](ecs-specifications.md).  
>-   Before changing a Xen ECS to a KVM ECS, install the desired driver on the ECS. Otherwise, the ECS will be unavailable after the modification is performed. For example, starting the OS will fail.  

## Constraints<a name="section1969981316489"></a>

-   If a Windows ECS is attached with a cross-region disk, the ECS specifications cannot be modified. Otherwise, ECS data may be lost.
-   A Xen ECS with more than 24 VBD disks attached cannot be changed to a KVM ECS.
-   A Xen ECS can be changed to a KVM ECS, but a KVM ECS cannot be changed to a Xen ECS.

## Procedure<a name="section1551105985918"></a>

[Figure 1](#fig10268287430)  shows the flowchart for changing a Xen ECS to a KVM ECS.

**Figure  1**  Flowchart for changing a Xen ECS to a KVM ECS<a name="fig10268287430"></a>  
![](figures/flowchart-for-changing-a-xen-ecs-to-a-kvm-ecs.png "flowchart-for-changing-a-xen-ecs-to-a-kvm-ecs")

[Table 1](#table1746813564213)  describes the operations.

**Table  1**  Procedure for changing a Xen ECS to a KVM ECS

<a name="table1746813564213"></a>
<table><thead align="left"><tr id="row1546910563218"><th class="cellrowborder" valign="top" width="33.22%" id="mcps1.2.3.1.1"><p id="p1446910561120"><a name="p1446910561120"></a><a name="p1446910561120"></a>Step</p>
</th>
<th class="cellrowborder" valign="top" width="66.78%" id="mcps1.2.3.1.2"><p id="p1646916561627"><a name="p1646916561627"></a><a name="p1646916561627"></a>Operation</p>
</th>
</tr>
</thead>
<tbody><tr id="row34697562212"><td class="cellrowborder" valign="top" width="33.22%" headers="mcps1.2.3.1.1 "><p id="p124699560210"><a name="p124699560210"></a><a name="p124699560210"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="66.78%" headers="mcps1.2.3.1.2 "><p id="p194695561523"><a name="p194695561523"></a><a name="p194695561523"></a><a href="#section8632184717500">(Optional) Step 1: Back Up the System Disk</a></p>
</td>
</tr>
<tr id="row946915561427"><td class="cellrowborder" valign="top" width="33.22%" headers="mcps1.2.3.1.1 "><p id="p164691456326"><a name="p164691456326"></a><a name="p164691456326"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="66.78%" headers="mcps1.2.3.1.2 "><p id="p1946914561820"><a name="p1946914561820"></a><a name="p1946914561820"></a><a href="#section1424018509446">Step 2: Check the UVP VMTools Version</a></p>
</td>
</tr>
<tr id="row3469156926"><td class="cellrowborder" valign="top" width="33.22%" headers="mcps1.2.3.1.1 "><p id="p846919562027"><a name="p846919562027"></a><a name="p846919562027"></a>3</p>
</td>
<td class="cellrowborder" valign="top" width="66.78%" headers="mcps1.2.3.1.2 "><p id="p104691256029"><a name="p104691256029"></a><a name="p104691256029"></a><a href="#section884919094417">Step 3: Install or Upgrade UVP VMTools</a></p>
</td>
</tr>
<tr id="row44695565215"><td class="cellrowborder" valign="top" width="33.22%" headers="mcps1.2.3.1.1 "><p id="p146910569217"><a name="p146910569217"></a><a name="p146910569217"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="66.78%" headers="mcps1.2.3.1.2 "><p id="p12469175615215"><a name="p12469175615215"></a><a name="p12469175615215"></a><a href="#section1815152131917">Step 4: Modify Specifications</a></p>
</td>
</tr>
<tr id="row7469135619210"><td class="cellrowborder" valign="top" width="33.22%" headers="mcps1.2.3.1.1 "><p id="p1469145611218"><a name="p1469145611218"></a><a name="p1469145611218"></a>5</p>
</td>
<td class="cellrowborder" valign="top" width="66.78%" headers="mcps1.2.3.1.2 "><p id="p846918566213"><a name="p846918566213"></a><a name="p846918566213"></a><a href="#section2625525131519">(Optional) Step 5: Check Disk Attachment</a></p>
</td>
</tr>
</tbody>
</table>

## \(Optional\) Step 1: Back Up the System Disk<a name="section8632184717500"></a>

Before modifying the specifications, back up the system disk and install the driver on the ECS. Otherwise, the ECS will be unavailable after the modification is performed. If the ECS becomes unavailable, the fault can be rectified by reinstalling the OS, which may cause data loss in your system disk.

For instructions about how to back up the system disk, see "Getting Started \>  [Creating a VBS Backup](https://docs.otc.t-systems.com/en-us/usermanual/vbs/en-us_topic_0015667820.html)" in  _Volume Backup Service User Guide_.

## Step 2: Check the UVP VMTools Version<a name="section1424018509446"></a>

1.  Log in to the ECS.
2.  Check whether UVP VMTools of 2.5 or a later version has been installed.

    Switch to the  **C:\\Program Files \(x86\)\\virtio\\bin**  directory, open the  **version.ini**  file, and view the UVP VMTools version.

    ```
    cur_vmtools_ver=2.5.0.105org_vmtools_ver=0cur_daemon_ver=2.5.0.105-010cur_drivers_ver=2.5.0.105-010
    ```

    -   If the directory is available and the driver version is 2.5 or later, UVP VMTools meeting service requirements has been installed. Then, go to  [Step 4: Modify Specifications](#section1815152131917).
    -   If the directory is unavailable or the driver version is earlier than 2.5, UVP VMTools has not been properly installed or the version does not meet service requirements. In such a case, install or upgrade UVP VMTools by following the instructions provided in  [Step 3: Install or Upgrade UVP VMTools](#section884919094417).


## Step 3: Install or Upgrade UVP VMTools<a name="section884919094417"></a>

When you install or upgrade UVP VMTools, if the PV driver has been installed on the ECS, the system will check the PV driver version. Ensure that the PV driver version meets service requirements. Otherwise, installing UVP VMTools will fail on the ECS. This section describes how to check the installation of the PV driver and UVP VMTools.

>![](public_sys-resources/icon-caution.gif) **CAUTION:**   
>Before installing the PV driver or UVP VMTools, ensure that the ECS meets the following requirements:  
>-   The available system disk size of the ECS is greater than 2 GB.  
>-   To prevent a driver installation failure, uninstall third-party virtualization platform tools, such as Citrix Xen Tools and VMware Tools, before installing the driver. For instructions about how to uninstall the tools, see the official documents of the tools.  
>-   Disable antivirus software or intrusion detection software. Enable them after installing the driver.  

1.  Check whether the PV driver version meets the UVP VMTools dependency requirements.

    Switch to the  **C:\\Program Files \(x86\)\\Xen PV Drivers\\bin**  directory, open the  **version.ini**  file, and view the PV driver version.

    ```
    pvdriverVersion=5.0.104.010
    ```

    -   If the directory is available and the driver version is 5.0 or later, the PV driver meeting service requirements has been installed. In such a case, go to step  [6](#li1950201211120)  to install UVP VMTools.
    -   If the directory is unavailable or the driver version is earlier than 5.0, the PV driver has not been properly installed or the version does not meet service requirements. Then, go to the next step to uninstall the PV driver and install a new one.

2.  <a name="li20502191213114"></a>Record the User Account Control \(UAC\) configuration of the ECS.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If the PV driver version is earlier than 5.0, DisableLUA is added to the registry during PV driver installation to prevent too many pop-up windows during driver upgrade, and EnableLUA is added to the registry during PV driver uninstallation \(this has been resolved in PV driver 5.0 and later versions\). To prevent adverse impact on your services, if the PV driver version is earlier than 5.0, record the UAC configuration before uninstalling the PV driver, and check and restore the EnableLUA configuration in the registry after installing the PV driver of the new version. For details about UAC configurations, see  [official Microsoft documents](https://docs.microsoft.com/en-us/windows/security/identity-protection/user-account-control/user-account-control-overview).  

    1.  In the  **Run**  dialog box, enter  **regedit**  and click  **OK**  to open the registry editor.
    2.  Record the  **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\\EnableLUA**  value.

        **Figure  2**  EnableLUA<a name="fig1757419164344"></a>  
        ![](figures/enablelua.jpg "enablelua")

3.  Uninstall the PV driver of the old version.
    1.  On the ECS OS, choose  **Start**  \>  **Control Panel**.
    2.  Click  **Uninstall a program**.
    3.  Uninstall  **GPL PV Drivers for Windows**_x.x.x.xx_  as prompted.
    4.  Restart the ECS.

4.  Install the PV driver of the new version.
    1.  Download the PV driver installation package.

        To download the installation package for the PV driver, log in at  [https://ecs-instance-driver.obs.eu-de.otc.t-systems.com/pvdriver-windows.zip](https://ecs-instance-driver.obs.eu-de.otc.t-systems.com/pvdriver-windows.zip).

    2.  Decompress the PV driver software package.
    3.  Run  **Setup.exe**  and install the PV driver as prompted.
    4.  Restart the ECS as prompted for the PV driver to take effect.

5.  Check and restore the UAC configuration.
    1.  In the  **Run**  dialog box, enter  **regedit**  and click  **OK**  to open the registry editor.
    2.  Check the  **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\\EnableLUA**  value and compare it with the value recorded before the PV driver is uninstalled. If they are different, change the value to the one recorded in step  [2](#li20502191213114).

6.  <a name="li1950201211120"></a>Install or upgrade UVP VMTools.
    1.  Download the UVP VMTools installation package.

        Download UVP VMTools at  [https://ecs-instance-driver.obs.eu-de.otc.t-systems.com/vmtools-windows.zip](https://ecs-instance-driver.obs.eu-de.otc.t-systems.com/vmtools-windows.zip).

    2.  Decompress the UVP VMTools installation package.
    3.  Run  **Setup.exe**  and install UVP VMTools as prompted.

        The installation program will automatically adapt to the OS version and identify whether UVP VMTools is newly installed or upgraded.

    4.  Restart the ECS as prompted for UVP VMTools to take effect.
    5.  Check whether UVP VMTools has been installed. For details, see  [Step 2: Check the UVP VMTools Version](#section1424018509446).


## Step 4: Modify Specifications<a name="section1815152131917"></a>

1.  Log in to management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  Under  **Computing**, click  **Elastic Cloud Server**.
4.  On the  **Elastic Cloud Server**  page, view the status of the target ECS.

    If the ECS is not in  **Stopped**  state, click  **More**  in the  **Operation**  column and select  **Stop**.

5.  Click  **More**  in the  **Operation**  column and select  **Modify Specifications**.

    The  **Modify ECS Specifications**  page is displayed.

6.  Select the new ECS type, vCPUs, and memory as prompted.
7.  \(Optional\) Set  **DeH**.

    If the ECS is created on a DeH, the system allows you to change the DeH.

    To do so, select the target DeH from the drop-down list. If no DeH is available in the drop-down list, remaining DeH resources are insufficient and cannot be used to create the ECS with specifications modified.

8.  Select the check box to confirm that step  [Step 3: Install or Upgrade UVP VMTools](#section884919094417)  has been performed.
9.  Click  **OK**.

## \(Optional\) Step 5: Check Disk Attachment<a name="section2625525131519"></a>

After a Xen ECS is changed to a KVM ECS, disk attachment may fail. Therefore, check disk attachment after specifications modification. If disks are properly attached, the specifications modification is successful.

-   Windows

    For details, see  [What Should I Do If the Data Disk of a Windows ECS Becomes Offline After the ECS Specifications Are Modified?](what-should-i-do-if-the-data-disk-of-a-windows-ecs-becomes-offline-after-the-ecs-specifications-are.md)


## Follow-up Procedure<a name="section76661826131619"></a>

If the ECS with specifications modified is displayed in the ECS list but its OS cannot be started after the ECS is remotely logged in, reinstall the ECS OS to rectify this fault. For details, see  [Reinstalling the OS](reinstalling-the-os.md).


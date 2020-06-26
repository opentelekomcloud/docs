# What Initial Configuration Needs to Be Performed on the ECS, BMS, or Image File Before It Is Used to Create an Image?<a name="EN-US_TOPIC_0040740508"></a>

## ECS or Image File Configurations<a name="section054335316711"></a>

**Table  1**  ECS configurations

<a name="table1978918558314"></a>
<table><thead align="left"><tr id="row2790165593112"><th class="cellrowborder" valign="top" width="16.8983101689831%" id="mcps1.2.4.1.1"><p id="p1979085563116"><a name="p1979085563116"></a><a name="p1979085563116"></a>OS</p>
</th>
<th class="cellrowborder" valign="top" width="44.995500449955%" id="mcps1.2.4.1.2"><p id="p679382318332"><a name="p679382318332"></a><a name="p679382318332"></a>Configuration Item</p>
</th>
<th class="cellrowborder" valign="top" width="38.106189381061895%" id="mcps1.2.4.1.3"><p id="p497545474216"><a name="p497545474216"></a><a name="p497545474216"></a>Reference</p>
</th>
</tr>
</thead>
<tbody><tr id="row187901655173119"><td class="cellrowborder" valign="top" width="16.8983101689831%" headers="mcps1.2.4.1.1 "><p id="p9790175543113"><a name="p9790175543113"></a><a name="p9790175543113"></a>Windows</p>
</td>
<td class="cellrowborder" valign="top" width="44.995500449955%" headers="mcps1.2.4.1.2 "><a name="ul15947101224316"></a><a name="ul15947101224316"></a><ul id="ul15947101224316"><li>Setting the NIC to DHCP</li><li>Enabling remote desktop connection</li><li>(Optional) installing special Windows drivers</li><li>(Optional) Installing Cloudbase-Init</li><li>Installing the Guest OS drivers, including the PV driver and UVP VMTools</li><li>Running Sysprep</li></ul>
</td>
<td class="cellrowborder" valign="top" width="38.106189381061895%" headers="mcps1.2.4.1.3 "><p id="p1176417812473"><a name="p1176417812473"></a><a name="p1176417812473"></a><a href="creating-a-system-disk-image-from-a-windows-ecs.md">Creating a System Disk Image from a Windows ECS</a></p>
</td>
</tr>
<tr id="row6792115783211"><td class="cellrowborder" valign="top" width="16.8983101689831%" headers="mcps1.2.4.1.1 "><p id="p13792175718323"><a name="p13792175718323"></a><a name="p13792175718323"></a>Linux</p>
</td>
<td class="cellrowborder" valign="top" width="44.995500449955%" headers="mcps1.2.4.1.2 "><a name="ul3979111343"></a><a name="ul3979111343"></a><ul id="ul3979111343"><li>Setting the NIC to DHCP</li><li>(Optional) installing special Linux drivers</li><li>(Optional) Installing Cloud-Init</li><li>Deleting files in the network rule directory</li><li>Changing the disk identifier in the GRUB configuration file to UUID</li><li>Changing the disk identifier in the fstab file to UUID</li><li>Installing native Xen and KVM drivers</li><li>Detaching data disks of an <span id="text12451619132813"><a name="text12451619132813"></a><a name="text12451619132813"></a>ECS</span><span id="text7451192285"><a name="text7451192285"></a><a name="text7451192285"></a></span></li><li>Configuring console logging</li></ul>
</td>
<td class="cellrowborder" valign="top" width="38.106189381061895%" headers="mcps1.2.4.1.3 "><p id="p1621217418716"><a name="p1621217418716"></a><a name="p1621217418716"></a><a href="creating-a-system-disk-image-from-a-linux-ecs.md">Creating a System Disk Image from a Linux ECS</a></p>
</td>
</tr>
</tbody>
</table>

**Table  2**  Image file configurations

<a name="table1182513010515"></a>
<table><thead align="left"><tr id="row28251308512"><th class="cellrowborder" valign="top" width="16.998300169983%" id="mcps1.2.4.1.1"><p id="p38253301850"><a name="p38253301850"></a><a name="p38253301850"></a>OS</p>
</th>
<th class="cellrowborder" valign="top" width="44.89551044895511%" id="mcps1.2.4.1.2"><p id="p1082553011519"><a name="p1082553011519"></a><a name="p1082553011519"></a>Configuration Item</p>
</th>
<th class="cellrowborder" valign="top" width="38.106189381061895%" id="mcps1.2.4.1.3"><p id="p1082533011510"><a name="p1082533011510"></a><a name="p1082533011510"></a>Reference</p>
</th>
</tr>
</thead>
<tbody><tr id="row118261630556"><td class="cellrowborder" valign="top" width="16.998300169983%" headers="mcps1.2.4.1.1 "><p id="p843193818510"><a name="p843193818510"></a><a name="p843193818510"></a>Windows</p>
</td>
<td class="cellrowborder" valign="top" width="44.89551044895511%" headers="mcps1.2.4.1.2 "><a name="ul7826153018518"></a><a name="ul7826153018518"></a><ul id="ul7826153018518"><li>Setting the NIC to DHCP</li><li>Enabling remote desktop connection</li><li>Installing the Guest OS drivers, including the PV driver and UVP VMTools</li><li>(Optional) Installing Cloudbase-Init</li><li>(Optional) Enabling NIC multi-queue</li></ul>
</td>
<td class="cellrowborder" valign="top" width="38.106189381061895%" headers="mcps1.2.4.1.3 "><p id="p1982663013518"><a name="p1982663013518"></a><a name="p1982663013518"></a><a href="preparing-an-image-file-(windows).md">Preparing an Image File</a></p>
</td>
</tr>
<tr id="row78275304510"><td class="cellrowborder" valign="top" width="16.998300169983%" headers="mcps1.2.4.1.1 "><p id="p2043443751"><a name="p2043443751"></a><a name="p2043443751"></a>Linux</p>
</td>
<td class="cellrowborder" valign="top" width="44.89551044895511%" headers="mcps1.2.4.1.2 "><a name="ul58271308513"></a><a name="ul58271308513"></a><ul id="ul58271308513"><li>Deleting files in the network rule directory</li><li>Setting the NIC to DHCP</li><li>Installing native Xen and KVM drivers</li><li>Changing the disk identifier in the GRUB configuration file to UUID</li><li>Changing the disk identifier in the fstab file to UUID</li><li>Deleting the automatic attachment information of non-system disks from the <strong id="b265313126127"><a name="b265313126127"></a><a name="b265313126127"></a>/etc/fstab</strong> file</li><li>(Optional) Installing Cloud-Init</li><li>(Optional) Enabling NIC multi-queue</li></ul>
</td>
<td class="cellrowborder" valign="top" width="38.106189381061895%" headers="mcps1.2.4.1.3 "><p id="p282812301257"><a name="p282812301257"></a><a name="p282812301257"></a><a href="preparing-an-image-file-(linux).md">Preparing an Image File</a></p>
</td>
</tr>
</tbody>
</table>

>![](/images/icon-note.gif) **NOTE:**   
>-   When registering an external image file as a private image, you are advised to perform the preceding operations on the VM where the external image file is located.  
>-   If the Guest OS driver is installed on the ECS, the cloud platform will check the image file after you select  **Enable automatic configuration**. If the GuestOS driver is not installed, the cloud platform will try to install the driver.  

## BMS or Image File Configurations<a name="section034477111115"></a>

**Table  3**  BMS configurations

<a name="table1268144421118"></a>
<table><thead align="left"><tr id="row126974419113"><th class="cellrowborder" valign="top" width="16.8983101689831%" id="mcps1.2.4.1.1"><p id="p1069194491111"><a name="p1069194491111"></a><a name="p1069194491111"></a>OS</p>
</th>
<th class="cellrowborder" valign="top" width="44.995500449955%" id="mcps1.2.4.1.2"><p id="p2069444171118"><a name="p2069444171118"></a><a name="p2069444171118"></a>Configuration Item</p>
</th>
<th class="cellrowborder" valign="top" width="38.106189381061895%" id="mcps1.2.4.1.3"><p id="p2693447112"><a name="p2693447112"></a><a name="p2693447112"></a>Reference</p>
</th>
</tr>
</thead>
<tbody><tr id="row1569194417112"><td class="cellrowborder" valign="top" width="16.8983101689831%" headers="mcps1.2.4.1.1 "><p id="p18699443112"><a name="p18699443112"></a><a name="p18699443112"></a>Windows</p>
</td>
<td class="cellrowborder" valign="top" width="44.995500449955%" headers="mcps1.2.4.1.2 "><a name="ul11701644161114"></a><a name="ul11701644161114"></a><ul id="ul11701644161114"><li>Installing the <strong id="b842352706143312"><a name="b842352706143312"></a><a name="b842352706143312"></a>bms-network-config</strong> software package</li><li>Installing Cloudbase-Init</li><li>Deleting residual files in the OS</li></ul>
</td>
<td class="cellrowborder" valign="top" width="38.106189381061895%" headers="mcps1.2.4.1.3 "><p id="p9712445111"><a name="p9712445111"></a><a name="p9712445111"></a>For details, see "Creating a Private Image from a BMS" in <em id="i790723918182"><a name="i790723918182"></a><a name="i790723918182"></a>Bare Metal Server User Guide</em>.</p>
</td>
</tr>
<tr id="row571194410118"><td class="cellrowborder" valign="top" width="16.8983101689831%" headers="mcps1.2.4.1.1 "><p id="p07144481119"><a name="p07144481119"></a><a name="p07144481119"></a>Linux</p>
</td>
<td class="cellrowborder" valign="top" width="44.995500449955%" headers="mcps1.2.4.1.2 "><a name="ul419561315141"></a><a name="ul419561315141"></a><ul id="ul419561315141"><li>Installing the <strong id="b488611578188"><a name="b488611578188"></a><a name="b488611578188"></a>bms-network-config</strong> software package</li><li>Installing Cloud-Init</li><li>Deleting residual files in the OS</li></ul>
</td>
<td class="cellrowborder" valign="top" width="38.106189381061895%" headers="mcps1.2.4.1.3 "><p id="p750683741819"><a name="p750683741819"></a><a name="p750683741819"></a>For details, see "Creating a Private Image from a BMS" in <em id="i1575211122019"><a name="i1575211122019"></a><a name="i1575211122019"></a>Bare Metal Server User Guide</em>.</p>
</td>
</tr>
</tbody>
</table>

**Table  4**  Image file configurations

<a name="table17827101913125"></a>
<table><thead align="left"><tr id="row1282712195126"><th class="cellrowborder" valign="top" width="16.998300169983%" id="mcps1.2.4.1.1"><p id="p5827319151219"><a name="p5827319151219"></a><a name="p5827319151219"></a>OS</p>
</th>
<th class="cellrowborder" valign="top" width="44.89551044895511%" id="mcps1.2.4.1.2"><p id="p128281019121216"><a name="p128281019121216"></a><a name="p128281019121216"></a>Configuration Item</p>
</th>
<th class="cellrowborder" valign="top" width="38.106189381061895%" id="mcps1.2.4.1.3"><p id="p11828119191220"><a name="p11828119191220"></a><a name="p11828119191220"></a>Reference</p>
</th>
</tr>
</thead>
<tbody><tr id="row882816199124"><td class="cellrowborder" valign="top" width="16.998300169983%" headers="mcps1.2.4.1.1 "><p id="p1182821951212"><a name="p1182821951212"></a><a name="p1182821951212"></a>Windows</p>
</td>
<td class="cellrowborder" valign="top" width="44.89551044895511%" headers="mcps1.2.4.1.2 "><a name="ul18311535111120"></a><a name="ul18311535111120"></a><ul id="ul18311535111120"><li>Installing the V5 server driver</li><li>Installing Cloudbase-Init</li><li>Installing the <strong id="b842352706143312_1"><a name="b842352706143312_1"></a><a name="b842352706143312_1"></a>bms-network-config</strong> software package</li><li>(Optional) Installing the SDI iNIC driver</li><li>Setting the Windows time zone</li><li>Setting the virtual memory</li><li>(Optional) Configuring automatic Windows update</li><li>Configuring the SID</li></ul>
</td>
<td class="cellrowborder" valign="top" width="38.106189381061895%" headers="mcps1.2.4.1.3 "><p id="p12765161316229"><a name="p12765161316229"></a><a name="p12765161316229"></a><em id="i106301718152214"><a name="i106301718152214"></a><a name="i106301718152214"></a>Bare Metal Server Image Creation Guide</em></p>
</td>
</tr>
<tr id="row108281619121214"><td class="cellrowborder" valign="top" width="16.998300169983%" headers="mcps1.2.4.1.1 "><p id="p18828919141213"><a name="p18828919141213"></a><a name="p18828919141213"></a>Linux</p>
</td>
<td class="cellrowborder" valign="top" width="44.89551044895511%" headers="mcps1.2.4.1.2 "><a name="ul16592117124"></a><a name="ul16592117124"></a><ul id="ul16592117124"><li>Installing and configuring Cloud-Init.</li><li>Modifying the hardware device driver that boots the OS</li><li>Installing the <strong id="b842352706143312_2"><a name="b842352706143312_2"></a><a name="b842352706143312_2"></a>bms-network-config</strong> software package</li><li>(Optional) Installing the SDI iNIC driver</li><li>(Optional) Installing the Hi1822 NIC driver</li><li>(Optional) Installing the IB driver</li><li>(Optional) Installing the V5 server driver</li><li>(Optional) Installing the UltraPath software</li><li>Performing security configuration</li><li>Configuring remote login to the BMS</li><li>Configuring automatic root partition expansion</li></ul>
</td>
<td class="cellrowborder" valign="top" width="38.106189381061895%" headers="mcps1.2.4.1.3 "><p id="p6539171152311"><a name="p6539171152311"></a><a name="p6539171152311"></a><em id="i676510392315"><a name="i676510392315"></a><a name="i676510392315"></a>Bare Metal Server Image Creation Guide</em></p>
</td>
</tr>
</tbody>
</table>


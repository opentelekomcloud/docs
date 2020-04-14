# OS::Nova::Server<a name="EN-US_TOPIC_0088407142"></a>

A resource for managing Nova instances.

A Server resource manages the running virtual machine instance within an OpenStack cloud.

## Required Properties<a name="section4892133219411"></a>

<a name="table107871529124018"></a>
<table><thead align="left"><tr id="row1151614441192"><th class="cellrowborder" valign="top" width="33%" id="mcps1.1.3.1.1"><p id="p1078942910403"><a name="p1078942910403"></a><a name="p1078942910403"></a><strong id="b1407102315819"><a name="b1407102315819"></a><a name="b1407102315819"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="67%" id="mcps1.1.3.1.2"><p id="p778912915400"><a name="p778912915400"></a><a name="p778912915400"></a><strong id="b64082023685"><a name="b64082023685"></a><a name="b64082023685"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row55161844999"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p2790192919406"><a name="p2790192919406"></a><a name="p2790192919406"></a>flavor</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p44907963"><a name="p44907963"></a><a name="p44907963"></a>The ID or name of the flavor to boot onto.</p>
<p id="p1518486"><a name="p1518486"></a><a name="p1518486"></a>String value expected.</p>
<p id="p13666380"><a name="p13666380"></a><a name="p13666380"></a>Can be updated without replacement.</p>
<p id="p55888556"><a name="p55888556"></a><a name="p55888556"></a>Value must be of type nova.flavor</p>
<div class="note" id="note5470285514545"><a name="note5470285514545"></a><a name="note5470285514545"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p30679194"><a name="p30679194"></a><a name="p30679194"></a>The Server flavor does not support the <strong id="b18771320135414"><a name="b18771320135414"></a><a name="b18771320135414"></a>replace</strong> parameter (When updating the stack, resources need to be deleted and rebuilt).</p>
</div></div>
</td>
</tr>
<tr id="row6251542195912"><td class="cellrowborder" valign="top" width="33%" headers="mcps1.1.3.1.1 "><p id="p648718302436"><a name="p648718302436"></a><a name="p648718302436"></a>networks</p>
</td>
<td class="cellrowborder" valign="top" width="67%" headers="mcps1.1.3.1.2 "><p id="p61799001"><a name="p61799001"></a><a name="p61799001"></a>An ordered list of NICs to be added to this server, with information about connected networks, fixed IP addresses, port, and others.</p>
<p id="p19320103"><a name="p19320103"></a><a name="p19320103"></a>List value expected.</p>
<p id="p39663204"><a name="p39663204"></a><a name="p39663204"></a>Can be updated without replacement.</p>
<p id="p21424521"><a name="p21424521"></a><a name="p21424521"></a><em id="i25803286"><a name="i25803286"></a><a name="i25803286"></a>List contents:</em></p>
<a name="ul57664664"></a><a name="ul57664664"></a><ul id="ul57664664"><li>*<p id="p40326203"><a name="p40326203"></a><a name="p40326203"></a>Map value expected.</p>
<p id="p27391512"><a name="p27391512"></a><a name="p27391512"></a>Can be updated without replacement.</p>
<p id="p139661234145411"><a name="p139661234145411"></a><a name="p139661234145411"></a><em id="i33379675"><a name="i33379675"></a><a name="i33379675"></a>Map properties:</em></p>
<a name="ul10338204419545"></a><a name="ul10338204419545"></a><ul id="ul10338204419545"><li>fixed_ip<p id="p50682160"><a name="p50682160"></a><a name="p50682160"></a>Fixed IP address to specify for the port created on the requested network.</p>
<p id="p53486256"><a name="p53486256"></a><a name="p53486256"></a>String value expected.</p>
<p id="p11614261"><a name="p11614261"></a><a name="p11614261"></a>Can be updated without replacement.</p>
<p id="p370414165519"><a name="p370414165519"></a><a name="p370414165519"></a>Value must be of type ip_addr</p>
</li><li>port<p id="p32607229"><a name="p32607229"></a><a name="p32607229"></a>ID of an existing port to associate with this server.</p>
<p id="p25029605"><a name="p25029605"></a><a name="p25029605"></a>String value expected.</p>
<p id="p23939855"><a name="p23939855"></a><a name="p23939855"></a>Can be updated without replacement.</p>
<p id="p18611912175518"><a name="p18611912175518"></a><a name="p18611912175518"></a>Value must be of type neutron.port</p>
</li><li>network<p id="p34651418"><a name="p34651418"></a><a name="p34651418"></a>Name or ID of network to create a port on.</p>
<p id="p43427310"><a name="p43427310"></a><a name="p43427310"></a>String value expected.</p>
<p id="p55301474"><a name="p55301474"></a><a name="p55301474"></a>Can be updated without replacement.</p>
<p id="p1247463055511"><a name="p1247463055511"></a><a name="p1247463055511"></a>Value must be of type neutron.network</p>
</li><li>uuid<p id="p42456448"><a name="p42456448"></a><a name="p42456448"></a>ID of network to create a port on.</p>
<p id="p46563716"><a name="p46563716"></a><a name="p46563716"></a>String value expected.</p>
<p id="p1940833811559"><a name="p1940833811559"></a><a name="p1940833811559"></a>Can be updated without replacement.</p>
</li></ul>
</li></ul>
<div class="note" id="note29801019151743"><a name="note29801019151743"></a><a name="note29801019151743"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul34513736"></a><a name="ul34513736"></a><ul id="ul34513736"><li>When creating a VM that has multiple NICs, ensure that all subnets used by the NICs are in the same VPC.</li><li>When changing the subnets of NICs on a VM, ensure that the new subnets must be in the same VPC as the original ones.</li></ul>
</div></div>
</td>
</tr>
</tbody>
</table>

## Optional Properties<a name="section1998916452415"></a>

<a name="table12485123016433"></a>
<table><thead align="left"><tr id="row14195438118"><th class="cellrowborder" valign="top" width="34%" id="mcps1.1.3.1.1"><p id="p124852303439"><a name="p124852303439"></a><a name="p124852303439"></a><strong id="b3275145981115"><a name="b3275145981115"></a><a name="b3275145981115"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="66%" id="mcps1.1.3.1.2"><p id="p14851304439"><a name="p14851304439"></a><a name="p14851304439"></a><strong id="b8276459101116"><a name="b8276459101116"></a><a name="b8276459101116"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row12199438112"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p154856302433"><a name="p154856302433"></a><a name="p154856302433"></a>admin_pass</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p47150815"><a name="p47150815"></a><a name="p47150815"></a>The administrator password for the server.</p>
<p id="p21704158"><a name="p21704158"></a><a name="p21704158"></a>String value expected.</p>
<p id="p61119702"><a name="p61119702"></a><a name="p61119702"></a>Can be updated without replacement.</p>
<div class="note" id="note4291428517483"><a name="note4291428517483"></a><a name="note4291428517483"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p51748792"><a name="p51748792"></a><a name="p51748792"></a>This parameter is invalid in the current version.</p>
<p id="p20696133191713"><a name="p20696133191713"></a><a name="p20696133191713"></a>For Linux ECSs, if you need to inject passwords, you can only use <strong id="b1351294510351"><a name="b1351294510351"></a><a name="b1351294510351"></a>user_data</strong> for injection. For Windows ECSs, if you need to inject passwords, you can only use the metadata <strong id="b194281657173510"><a name="b194281657173510"></a><a name="b194281657173510"></a>admin_pass</strong> to inject.</p>
</div></div>
</td>
</tr>
<tr id="row171916432118"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p648683016431"><a name="p648683016431"></a><a name="p648683016431"></a>availability_zone</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p20085859"><a name="p20085859"></a><a name="p20085859"></a>Name of the availability zone for server placement. Obtain the value from <a href="https://docs.otc.t-systems.com/en-us/endpoint/index.html" target="_blank" rel="noopener noreferrer">Regions and Endpoints</a>.</p>
<p id="p46555007"><a name="p46555007"></a><a name="p46555007"></a>String value expected.</p>
<p id="p16341883"><a name="p16341883"></a><a name="p16341883"></a>Updates cause replacement.</p>
<div class="note" id="note14793173711568"><a name="note14793173711568"></a><a name="note14793173711568"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p9688302"><a name="p9688302"></a><a name="p9688302"></a>Do not update this attribute. Otherwise, the ECS update will fail.</p>
</div></div>
</td>
</tr>
<tr id="row419164315114"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p1486113044313"><a name="p1486113044313"></a><a name="p1486113044313"></a>block_device_mapping</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p13532677"><a name="p13532677"></a><a name="p13532677"></a>Block device mappings for this server.</p>
<p id="p54685231"><a name="p54685231"></a><a name="p54685231"></a>List value expected.</p>
<p id="p22405032"><a name="p22405032"></a><a name="p22405032"></a>Updates cause replacement.</p>
<p id="p318697"><a name="p318697"></a><a name="p318697"></a><em id="i17305987"><a name="i17305987"></a><a name="i17305987"></a>List contents:</em></p>
<a name="ul25814479"></a><a name="ul25814479"></a><ul id="ul25814479"><li>*<p id="p6856192317451"><a name="p6856192317451"></a><a name="p6856192317451"></a>Map value expected.</p>
<p id="p10857323154517"><a name="p10857323154517"></a><a name="p10857323154517"></a>Updates cause replacement.</p>
<p id="p8858182318453"><a name="p8858182318453"></a><a name="p8858182318453"></a><em id="i42927366"><a name="i42927366"></a><a name="i42927366"></a>Map properties:</em></p>
<a name="ul12891729164516"></a><a name="ul12891729164516"></a><ul id="ul12891729164516"><li>delete_on_termination<p id="p138892754618"><a name="p138892754618"></a><a name="p138892754618"></a>Indicate whether the volume should be deleted when the server is terminated.</p>
<p id="p189087154613"><a name="p189087154613"></a><a name="p189087154613"></a>Boolean value expected.</p>
<p id="p9891197164618"><a name="p9891197164618"></a><a name="p9891197164618"></a>Updates cause replacement.</p>
</li><li>device_name<p id="p12607121517465"><a name="p12607121517465"></a><a name="p12607121517465"></a>A device name where the volume will be attached in the system at /dev/device_name. This value is typically vda.</p>
<p id="p6607181511468"><a name="p6607181511468"></a><a name="p6607181511468"></a>String value expected.</p>
<p id="p106082150467"><a name="p106082150467"></a><a name="p106082150467"></a>Updates cause replacement.</p>
</li><li>snapshot_id<p id="p132111248468"><a name="p132111248468"></a><a name="p132111248468"></a>The ID of the snapshot to create a volume from.</p>
<p id="p1322152404612"><a name="p1322152404612"></a><a name="p1322152404612"></a>String value expected.</p>
<p id="p193231248465"><a name="p193231248465"></a><a name="p193231248465"></a>Updates cause replacement.</p>
<p id="p1032492474613"><a name="p1032492474613"></a><a name="p1032492474613"></a>Value must be of type cinder.snapshot</p>
</li><li>volume_id<p id="p13543733174610"><a name="p13543733174610"></a><a name="p13543733174610"></a>The ID of the volume to boot from. Only one of volume_id or snapshot_id should be provided.</p>
<p id="p55431433194619"><a name="p55431433194619"></a><a name="p55431433194619"></a>String value expected.</p>
<p id="p65441433194620"><a name="p65441433194620"></a><a name="p65441433194620"></a>Updates cause replacement.</p>
<p id="p115451133124612"><a name="p115451133124612"></a><a name="p115451133124612"></a>Value must be of type cinder.volume</p>
</li><li>volume_size<p id="p13495124219465"><a name="p13495124219465"></a><a name="p13495124219465"></a>The size of the volume, in GB. It is safe to leave this blank and have the Compute service infer the size.</p>
<p id="p549694215464"><a name="p549694215464"></a><a name="p549694215464"></a>Integer value expected.</p>
<p id="p16496154224612"><a name="p16496154224612"></a><a name="p16496154224612"></a>Updates cause replacement.</p>
</li></ul>
</li></ul>
<div class="note" id="note26822905151922"><a name="note26822905151922"></a><a name="note26822905151922"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p34964258"><a name="p34964258"></a><a name="p34964258"></a>Do not update this attribute. Otherwise, the VM update will fail.</p>
<p id="p46242873"><a name="p46242873"></a><a name="p46242873"></a>If the template contains information about disks attached to Servers, you are not allowed to update the disks. Otherwise, Servers will be rebuilt.</p>
</div></div>
</td>
</tr>
<tr id="row619164301115"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p12486230154311"><a name="p12486230154311"></a><a name="p12486230154311"></a>block_device_mapping_v2</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p12339307"><a name="p12339307"></a><a name="p12339307"></a>Block device mappings v2 for this server.</p>
<p id="p43944901"><a name="p43944901"></a><a name="p43944901"></a>List value expected.</p>
<p id="p59959792"><a name="p59959792"></a><a name="p59959792"></a>Updates cause replacement.</p>
<p id="p2767222"><a name="p2767222"></a><a name="p2767222"></a><em id="i57408296"><a name="i57408296"></a><a name="i57408296"></a>List contents:</em></p>
<a name="ul22818395"></a><a name="ul22818395"></a><ul id="ul22818395"><li>*<p id="p36350684"><a name="p36350684"></a><a name="p36350684"></a>Map value expected.</p>
<p id="p58720707"><a name="p58720707"></a><a name="p58720707"></a>Updates cause replacement.</p>
<p id="p1275612355474"><a name="p1275612355474"></a><a name="p1275612355474"></a><em id="i23541105"><a name="i23541105"></a><a name="i23541105"></a>Map properties:</em></p>
<a name="ul14555204234718"></a><a name="ul14555204234718"></a><ul id="ul14555204234718"><li>boot_index<p id="p18295196"><a name="p18295196"></a><a name="p18295196"></a>Integer used for ordering the boot disks.</p>
<p id="p30439043"><a name="p30439043"></a><a name="p30439043"></a>Integer value expected.</p>
<p id="p84921955124817"><a name="p84921955124817"></a><a name="p84921955124817"></a>Updates cause replacement.</p>
</li><li>delete_on_termination<p id="p61694733"><a name="p61694733"></a><a name="p61694733"></a>Indicate whether the volume should be deleted when the server is terminated.</p>
<p id="p18381693"><a name="p18381693"></a><a name="p18381693"></a>Boolean value expected.</p>
<p id="p091420424911"><a name="p091420424911"></a><a name="p091420424911"></a>Updates cause replacement.</p>
</li><li>device_name<p id="p7661228"><a name="p7661228"></a><a name="p7661228"></a>A device name where the volume will be attached in the system at /dev/device_name. This value is typically vda.</p>
<p id="p1842189"><a name="p1842189"></a><a name="p1842189"></a>String value expected.</p>
<p id="p1220611151494"><a name="p1220611151494"></a><a name="p1220611151494"></a>Updates cause replacement.</p>
</li><li>device_type<p id="p7007444"><a name="p7007444"></a><a name="p7007444"></a>Device type: at the moment we can make distinction only between disk and cdrom.</p>
<p id="p63067000"><a name="p63067000"></a><a name="p63067000"></a>String value expected.</p>
<p id="p30732088"><a name="p30732088"></a><a name="p30732088"></a>Updates cause replacement.</p>
<p id="p15192152520491"><a name="p15192152520491"></a><a name="p15192152520491"></a>Allowed values: cdrom, disk</p>
</li><li>disk_bus<p id="p38207563"><a name="p38207563"></a><a name="p38207563"></a>Bus of the device: hypervisor driver chooses a suitable default if omitted.</p>
<p id="p8323748"><a name="p8323748"></a><a name="p8323748"></a>String value expected.</p>
<p id="p7804873"><a name="p7804873"></a><a name="p7804873"></a>Updates cause replacement.</p>
<p id="p575618346494"><a name="p575618346494"></a><a name="p575618346494"></a>Allowed values: ide, lame_bus, scsi, usb, virtio</p>
</li><li>snapshot_id<p id="p3709046"><a name="p3709046"></a><a name="p3709046"></a>The ID of the snapshot to create a volume from.</p>
<p id="p33381417"><a name="p33381417"></a><a name="p33381417"></a>String value expected.</p>
<p id="p31997301"><a name="p31997301"></a><a name="p31997301"></a>Updates cause replacement.</p>
<p id="p1795864494917"><a name="p1795864494917"></a><a name="p1795864494917"></a>Value must be of type cinder.snapshot</p>
</li><li>swap_size<p id="p17770510"><a name="p17770510"></a><a name="p17770510"></a>The size of the swap, in MB.</p>
<p id="p25716863"><a name="p25716863"></a><a name="p25716863"></a>Integer value expected.</p>
<p id="p1335195494920"><a name="p1335195494920"></a><a name="p1335195494920"></a>Updates cause replacement.</p>
</li><li>volume_id<p id="p16654059"><a name="p16654059"></a><a name="p16654059"></a>The volume_id can be boot or non-boot device to the server.</p>
<p id="p15668810"><a name="p15668810"></a><a name="p15668810"></a>String value expected.</p>
<p id="p6801564"><a name="p6801564"></a><a name="p6801564"></a>Updates cause replacement.</p>
<p id="p1631964155016"><a name="p1631964155016"></a><a name="p1631964155016"></a>Value must be of type cinder.volume</p>
</li><li>volume_size<p id="p64782076"><a name="p64782076"></a><a name="p64782076"></a>Size of the block device in GB. If it is omitted, hypervisor driver calculates size.</p>
<p id="p46167779"><a name="p46167779"></a><a name="p46167779"></a>Integer value expected.</p>
<p id="p966571318508"><a name="p966571318508"></a><a name="p966571318508"></a>Updates cause replacement.</p>
</li><li>image_id<p id="p44495107"><a name="p44495107"></a><a name="p44495107"></a>The ID of the image to create a volume from.</p>
<p id="p64911646"><a name="p64911646"></a><a name="p64911646"></a>String value expected.</p>
<p id="p47333904"><a name="p47333904"></a><a name="p47333904"></a>Updates cause replacement.</p>
<p id="p53971224501"><a name="p53971224501"></a><a name="p53971224501"></a>Value must be of type glance.image</p>
</li></ul>
</li></ul>
<div class="note" id="note30001193151932"><a name="note30001193151932"></a><a name="note30001193151932"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p35778030"><a name="p35778030"></a><a name="p35778030"></a>Do not update this attribute. Otherwise, the VM update will fail.</p>
<p id="p53566817"><a name="p53566817"></a><a name="p53566817"></a>If the template contains information about disks attached to Servers, you are not allowed to update the disks. Otherwise, Servers will be rebuilt.</p>
</div></div>
</td>
</tr>
<tr id="row1219943191116"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p124867305431"><a name="p124867305431"></a><a name="p124867305431"></a>config_drive</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p2636360"><a name="p2636360"></a><a name="p2636360"></a>If True, enable config drive on the server.</p>
<p id="p23727241"><a name="p23727241"></a><a name="p23727241"></a>Boolean value expected.</p>
<p id="p12218585"><a name="p12218585"></a><a name="p12218585"></a>Updates cause replacement.</p>
<div class="note" id="note1952072925715"><a name="note1952072925715"></a><a name="note1952072925715"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p45032171"><a name="p45032171"></a><a name="p45032171"></a>Do not update this attribute. Otherwise, the VM update will fail.</p>
</div></div>
</td>
</tr>
<tr id="row51924341115"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p174861230104318"><a name="p174861230104318"></a><a name="p174861230104318"></a>diskConfig</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p38158322"><a name="p38158322"></a><a name="p38158322"></a>Control how the disk is partitioned when the server is created.</p>
<p id="p7880584"><a name="p7880584"></a><a name="p7880584"></a>String value expected.</p>
<p id="p3816393"><a name="p3816393"></a><a name="p3816393"></a>Updates cause replacement.</p>
<p id="p34347544"><a name="p34347544"></a><a name="p34347544"></a>Allowed values: AUTO, MANUAL</p>
<div class="note" id="note15510143635716"><a name="note15510143635716"></a><a name="note15510143635716"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p48979056"><a name="p48979056"></a><a name="p48979056"></a>Do not update this attribute. Otherwise, the VM update will fail.</p>
</div></div>
</td>
</tr>
<tr id="row1819144311115"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p16486230144312"><a name="p16486230144312"></a><a name="p16486230144312"></a>flavor_update_policy</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p30687689"><a name="p30687689"></a><a name="p30687689"></a>Policy on how to apply a flavor update; either by requesting a server resize or by replacing the entire server.</p>
<p id="p7753749"><a name="p7753749"></a><a name="p7753749"></a>String value expected.</p>
<p id="p2674882"><a name="p2674882"></a><a name="p2674882"></a>Can be updated without replacement.</p>
<p id="p24073946"><a name="p24073946"></a><a name="p24073946"></a>Defaults to "RESIZE".</p>
<p id="p15338924"><a name="p15338924"></a><a name="p15338924"></a>Allowed values: RESIZE</p>
</td>
</tr>
<tr id="row13191943151114"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p11486330174311"><a name="p11486330174311"></a><a name="p11486330174311"></a>image</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p34493359"><a name="p34493359"></a><a name="p34493359"></a>The ID or name of the image to boot with.</p>
<p id="p42004777"><a name="p42004777"></a><a name="p42004777"></a>String value expected.</p>
<p id="p42498674"><a name="p42498674"></a><a name="p42498674"></a>Can be updated without replacement.</p>
<p id="p46943747"><a name="p46943747"></a><a name="p46943747"></a>Value must be of type glance.image</p>
<div class="note" id="note137484320015"><a name="note137484320015"></a><a name="note137484320015"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p17121323571"><a name="p17121323571"></a><a name="p17121323571"></a>If you use the system volume to create an ECS, this parameter is not required. If you do not use a volume to create an ECS, you must set <strong id="en-us_topic_0057972661_b842352706102116"><a name="en-us_topic_0057972661_b842352706102116"></a><a name="en-us_topic_0057972661_b842352706102116"></a>imageRef</strong> to a valid UUID. Otherwise, the API will return error code <strong id="en-us_topic_0057972661_b842352706102125"><a name="en-us_topic_0057972661_b842352706102125"></a><a name="en-us_topic_0057972661_b842352706102125"></a>400</strong>.</p>
</div></div>
</td>
</tr>
<tr id="row1819134320118"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p54865309433"><a name="p54865309433"></a><a name="p54865309433"></a>image_update_policy</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p44347145"><a name="p44347145"></a><a name="p44347145"></a>Policy on how to apply an image-id update; either by requesting a server rebuild or by replacing the entire server.</p>
<p id="p63579993"><a name="p63579993"></a><a name="p63579993"></a>String value expected.</p>
<p id="p35349029"><a name="p35349029"></a><a name="p35349029"></a>Can be updated without replacement.</p>
<p id="p49705805"><a name="p49705805"></a><a name="p49705805"></a>Defaults to "REBUILD".</p>
<p id="p44699068"><a name="p44699068"></a><a name="p44699068"></a>Allowed values: REBUILD</p>
</td>
</tr>
<tr id="row4194433115"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p1648643044320"><a name="p1648643044320"></a><a name="p1648643044320"></a>key_name</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p4854401"><a name="p4854401"></a><a name="p4854401"></a>Name of keypair to inject into the server.</p>
<p id="p43689614"><a name="p43689614"></a><a name="p43689614"></a>String value expected.</p>
<p id="p57662206"><a name="p57662206"></a><a name="p57662206"></a>Updates cause replacement.</p>
<p id="p49197812"><a name="p49197812"></a><a name="p49197812"></a>Value must be of type nova.keypair</p>
<div class="note" id="note34179300174951"><a name="note34179300174951"></a><a name="note34179300174951"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p37822080"><a name="p37822080"></a><a name="p37822080"></a>Do not update this attribute. Otherwise, the VM update will fail.</p>
</div></div>
</td>
</tr>
<tr id="row191924312118"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p2048723017433"><a name="p2048723017433"></a><a name="p2048723017433"></a>metadata</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p60320746"><a name="p60320746"></a><a name="p60320746"></a>Arbitrary key/value metadata to store for this server. Both keys and values must be 255 characters or less. Non-string values will be serialized to JSON (and the serialized string must be 255 characters or less).</p>
<p id="p6015809"><a name="p6015809"></a><a name="p6015809"></a>Map value expected.</p>
<p id="p54142282"><a name="p54142282"></a><a name="p54142282"></a>Can be updated without replacement.</p>
</td>
</tr>
<tr id="row20192437115"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p1748717308439"><a name="p1748717308439"></a><a name="p1748717308439"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p23448739"><a name="p23448739"></a><a name="p23448739"></a>Server name.</p>
<p id="p9712060"><a name="p9712060"></a><a name="p9712060"></a>String value expected.</p>
<p id="p20299676"><a name="p20299676"></a><a name="p20299676"></a>Can be updated without replacement.</p>
</td>
</tr>
<tr id="row9199435113"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p174871301432"><a name="p174871301432"></a><a name="p174871301432"></a>personality</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p23613094"><a name="p23613094"></a><a name="p23613094"></a>A map of files to create/overwrite on the server upon boot. Keys are file names and values are the file contents.</p>
<p id="p11191262"><a name="p11191262"></a><a name="p11191262"></a>Map value expected.</p>
<p id="p33612498"><a name="p33612498"></a><a name="p33612498"></a>Updates cause replacement.</p>
<p id="p34077026"><a name="p34077026"></a><a name="p34077026"></a>Defaults to "{}".</p>
<div class="note" id="note15646748145813"><a name="note15646748145813"></a><a name="note15646748145813"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p24993298"><a name="p24993298"></a><a name="p24993298"></a>Do not update this attribute. Otherwise, the VM update will fail.</p>
</div></div>
</td>
</tr>
<tr id="row319174341114"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p19487930174318"><a name="p19487930174318"></a><a name="p19487930174318"></a>reservation_id</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p39747253"><a name="p39747253"></a><a name="p39747253"></a>A UUID for the set of servers being requested.</p>
<p id="p22180958"><a name="p22180958"></a><a name="p22180958"></a>String value expected.</p>
<p id="p65410899"><a name="p65410899"></a><a name="p65410899"></a>Updates cause replacement.</p>
<div class="note" id="note11204185585815"><a name="note11204185585815"></a><a name="note11204185585815"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p11872901"><a name="p11872901"></a><a name="p11872901"></a>Do not update this attribute. Otherwise, the VM update will fail.</p>
</div></div>
</td>
</tr>
<tr id="row7195439111"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p24871330124316"><a name="p24871330124316"></a><a name="p24871330124316"></a>scheduler_hints</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p66832448"><a name="p66832448"></a><a name="p66832448"></a>Arbitrary key-value pairs specified by the client to help boot a server.</p>
<p id="p64621123"><a name="p64621123"></a><a name="p64621123"></a>Map value expected.</p>
<p id="p44719199"><a name="p44719199"></a><a name="p44719199"></a>Updates cause replacement.</p>
<div class="note" id="note4903603596"><a name="note4903603596"></a><a name="note4903603596"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p37251989"><a name="p37251989"></a><a name="p37251989"></a>Do not update this attribute. Otherwise, the VM update will fail.</p>
</div></div>
</td>
</tr>
<tr id="row15191543121118"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p24871030134312"><a name="p24871030134312"></a><a name="p24871030134312"></a>security_groups</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p2716472"><a name="p2716472"></a><a name="p2716472"></a>List of security group names or IDs. Cannot be used if neutron ports are associated with this server; assign security groups to the ports instead.</p>
<p id="p24448249"><a name="p24448249"></a><a name="p24448249"></a>List value expected.</p>
<p id="p18707649"><a name="p18707649"></a><a name="p18707649"></a>Updates cause replacement.</p>
<p id="p34151113"><a name="p34151113"></a><a name="p34151113"></a>Defaults to "[]".</p>
<div class="note" id="note6011015590"><a name="note6011015590"></a><a name="note6011015590"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p52497613"><a name="p52497613"></a><a name="p52497613"></a>Do not update this attribute. Otherwise, the VM update will fail.</p>
</div></div>
</td>
</tr>
<tr id="row919184318111"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p9487730164319"><a name="p9487730164319"></a><a name="p9487730164319"></a>software_config_transport</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p13656193818589"><a name="p13656193818589"></a><a name="p13656193818589"></a>How the server should receive the metadata required for software configuration.</p>
<p id="p394903415817"><a name="p394903415817"></a><a name="p394903415817"></a>POLL_TEMP_URL will create and populate a Swift TempURL with metadata for polling.</p>
<p id="p65881812"><a name="p65881812"></a><a name="p65881812"></a>String value expected.</p>
<p id="p56065398"><a name="p56065398"></a><a name="p56065398"></a>Can be updated without replacement.</p>
<p id="p34826542"><a name="p34826542"></a><a name="p34826542"></a>Defaults to "POLL_TEMP_URL".</p>
</td>
</tr>
<tr id="row201914317111"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p11487330134320"><a name="p11487330134320"></a><a name="p11487330134320"></a>tags</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p21399062"><a name="p21399062"></a><a name="p21399062"></a>Server tags.</p>
<p id="p58373837"><a name="p58373837"></a><a name="p58373837"></a>List value expected.</p>
<p id="p55602485"><a name="p55602485"></a><a name="p55602485"></a>Can be updated without replacement.</p>
<p id="p30660320"><a name="p30660320"></a><a name="p30660320"></a><em id="i16172705102351"><a name="i16172705102351"></a><a name="i16172705102351"></a>List contents:</em></p>
<a name="ul458029"></a><a name="ul458029"></a><ul id="ul458029"><li>*<p id="p37100378"><a name="p37100378"></a><a name="p37100378"></a>String value expected.</p>
<p id="p55274543581"><a name="p55274543581"></a><a name="p55274543581"></a>Can be updated without replacement.</p>
</li></ul>
</td>
</tr>
<tr id="row620243191114"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p1548814303435"><a name="p1548814303435"></a><a name="p1548814303435"></a>user_data</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p1303565"><a name="p1303565"></a><a name="p1303565"></a>User data script to be executed by cloud-init.</p>
<p id="p11732085"><a name="p11732085"></a><a name="p11732085"></a>String value expected.</p>
<p id="p38479906"><a name="p38479906"></a><a name="p38479906"></a>Can be updated without replacement.</p>
<p id="p10774835"><a name="p10774835"></a><a name="p10774835"></a>Defaults to "".</p>
<div class="note" id="note19752850175121"><a name="note19752850175121"></a><a name="note19752850175121"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p346482"><a name="p346482"></a><a name="p346482"></a>You are not advised to update user_data. Otherwise, VMs may be rebuilt.</p>
</div></div>
</td>
</tr>
<tr id="row920154318117"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p17488133084315"><a name="p17488133084315"></a><a name="p17488133084315"></a>user_data_format</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p18188281632"><a name="p18188281632"></a><a name="p18188281632"></a>How the user_data should be formatted for the server.</p>
<a name="ul17581193117312"></a><a name="ul17581193117312"></a><ul id="ul17581193117312"><li>For HEAT_CFNTOOLS, the user_data is bundled as part of the heat-cfntools cloud-init boot configuration data.</li><li>For RAW the user_data is passed to Nova unmodified.</li><li>For SOFTWARE_CONFIG user_data is bundled as part of the software config data, and metadata is derived from any associated SoftwareDeployment resources.</li></ul>
<p id="p51259436"><a name="p51259436"></a><a name="p51259436"></a>String value expected.</p>
<p id="p58681746"><a name="p58681746"></a><a name="p58681746"></a>Updates cause replacement.</p>
<p id="p58373667"><a name="p58373667"></a><a name="p58373667"></a>Defaults to "HEAT_CFNTOOLS".</p>
<p id="p55600962"><a name="p55600962"></a><a name="p55600962"></a>Allowed values: HEAT_CFNTOOLS, RAW, SOFTWARE_CONFIG</p>
</td>
</tr>
</tbody>
</table>

## Attributes<a name="section1637135416415"></a>

<a name="table515755685910"></a>
<table><thead align="left"><tr id="row3747235182414"><th class="cellrowborder" valign="top" width="34%" id="mcps1.1.3.1.1"><p id="p151571156105910"><a name="p151571156105910"></a><a name="p151571156105910"></a><strong id="b41626692614"><a name="b41626692614"></a><a name="b41626692614"></a>Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="66%" id="mcps1.1.3.1.2"><p id="p20157185695915"><a name="p20157185695915"></a><a name="p20157185695915"></a><strong id="b18163263268"><a name="b18163263268"></a><a name="b18163263268"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row197471335202417"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p8157856165913"><a name="p8157856165913"></a><a name="p8157856165913"></a>accessIPv4</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p1515735611593"><a name="p1515735611593"></a><a name="p1515735611593"></a>The manually assigned alternative public IPv4 address of the server.</p>
</td>
</tr>
<tr id="row57471135152414"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p14157756175910"><a name="p14157756175910"></a><a name="p14157756175910"></a>accessIPv6</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p415715569593"><a name="p415715569593"></a><a name="p415715569593"></a>The manually assigned alternative public IPv6 address of the server.</p>
</td>
</tr>
<tr id="row37471735102415"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p1315715613599"><a name="p1315715613599"></a><a name="p1315715613599"></a>addresses</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p12157145635915"><a name="p12157145635915"></a><a name="p12157145635915"></a>A dict of all network addresses with corresponding port_id. Each network will have two keys in dict, they are network name and network id. The port ID may be obtained through the following expression: "{get_attr: [&lt;server&gt;, addresses, &lt;network name_or_id&gt;, 0, port]}".</p>
</td>
</tr>
<tr id="row1874712358244"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p715795665915"><a name="p715795665915"></a><a name="p715795665915"></a>first_address</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p3157115685911"><a name="p3157115685911"></a><a name="p3157115685911"></a>Convenience attribute to fetch the first assigned network address, or an empty string if nothing has been assigned at this time. Result may not be predictable if the server has addresses from more than one network.</p>
</td>
</tr>
<tr id="row1574763562411"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p161581756155915"><a name="p161581756155915"></a><a name="p161581756155915"></a>instance_name</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p0158185605912"><a name="p0158185605912"></a><a name="p0158185605912"></a>Name of the instance.</p>
</td>
</tr>
<tr id="row574743512242"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p6158456155919"><a name="p6158456155919"></a><a name="p6158456155919"></a>name</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p1415835695913"><a name="p1415835695913"></a><a name="p1415835695913"></a>Name of the server.</p>
</td>
</tr>
<tr id="row47479358245"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p7158756165910"><a name="p7158756165910"></a><a name="p7158756165910"></a>networks</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p1815811561592"><a name="p1815811561592"></a><a name="p1815811561592"></a>A dict of assigned network addresses of the form: {"public": [ip1, ip2...], "private": [ip3, ip4], "public_uuid": [ip1, ip2...], "private_uuid": [ip3, ip4]}. Each network will have two keys in dict, they are network name and network id.</p>
</td>
</tr>
<tr id="row13747183582414"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.1.3.1.1 "><p id="p156336431018"><a name="p156336431018"></a><a name="p156336431018"></a>show</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.1.3.1.2 "><p id="p156331643918"><a name="p156331643918"></a><a name="p156331643918"></a>Detailed information about resource.</p>
</td>
</tr>
</tbody>
</table>

## HOT Syntax<a name="section3552943425"></a>

```
heat_template_version: 2014-10-16
...
resources:
  ...
  the_resource:
    type: OS::Nova::Server
    properties:
      admin_pass: String
      availability_zone: String
      block_device_mapping: [{"snapshot_id": String, "volume_id": String, "delete_on_termination": Boolean, "volume_size": Integer, "device_name": String}, {"snapshot_id": String, "volume_id": String, "delete_on_termination": Boolean, "volume_size": Integer, "device_name": String}, ...]
      block_device_mapping_v2: [{"disk_bus": String, "swap_size": Integer, "device_name": String, "device_type": String, "delete_on_termination": Boolean, "volume_id": String, "snapshot_id": String, "boot_index": Integer, "image_id": String, "volume_size": Integer}, {"disk_bus": String, "swap_size": Integer, "device_name": String, "device_type": String, "delete_on_termination": Boolean, "volume_id": String, "snapshot_id": String, "boot_index": Integer, "image_id": String, "volume_size": Integer}, ...]
      config_drive: Boolean
      diskConfig: String
      flavor: String
      flavor_update_policy: String
      image: String
      image_update_policy: String
      key_name: String
      metadata: {...}
      name: String
      networks: [{"network": String, "uuid": String, "fixed_ip": String, "port": String, "floating_ip": String, "subnet": String, "port_extra_properties": {"qos_policy": String, "mac_address": String, "binding:vnic_type": String, "admin_state_up": Boolean, "port_security_enabled": Boolean, "allowed_address_pairs": [{"mac_address": String, "ip_address": String}, {"mac_address": String, "ip_address": String}, ...], "value_specs": {...}}}, {"network": String, "uuid": String, "fixed_ip": String, "port": String, "floating_ip": String, "subnet": String, "port_extra_properties": {"qos_policy": String, "mac_address": String, "binding:vnic_type": String, "admin_state_up": Boolean, "port_security_enabled": Boolean, "allowed_address_pairs": [{"mac_address": String, "ip_address": String}, {"mac_address": String, "ip_address": String}, ...], "value_specs": {...}}}, ...]
      personality: {...}
      reservation_id: String
      scheduler_hints: {...}
      security_groups: [Value, Value, ...]
      software_config_transport: String
      user_data: String
      user_data_format: String
```


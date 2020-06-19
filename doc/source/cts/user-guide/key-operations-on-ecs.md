# Key Operations on ECS<a name="en-us_topic_0100236046"></a>

Elastic Cloud Server \(ECS\) provides scalable, on-demand cloud servers for secure, flexible, and efficient application environments. An ECS is a computing server that consists of CPUs, memory, images, and EVS disks, and integrates virtual private cloud \(VPC\), virtual firewall, and multi-data-copy functions to ensure reliable, uninterrupted services.

With CTS, you can record operations associated with ECS for future query, audit, and backtrack operations.

**Table  1**  ECS operations that can be recorded by CTS

<a name="table53281160152351"></a>
<table><thead align="left"><tr id="ra44435ac2e584c81a74b5e2c0db0e6ec"><th class="cellrowborder" valign="top" width="47.5%" id="mcps1.2.4.1.1"><p id="a1ec564946d4d471397af5813917c0ee4"><a name="a1ec564946d4d471397af5813917c0ee4"></a><a name="a1ec564946d4d471397af5813917c0ee4"></a><strong id="b842352706103557"><a name="b842352706103557"></a><a name="b842352706103557"></a>Operation</strong></p>
</th>
<th class="cellrowborder" valign="top" width="21.89%" id="mcps1.2.4.1.2"><p id="ad929f7d0e3c04409a4e73636898fa12a"><a name="ad929f7d0e3c04409a4e73636898fa12a"></a><a name="ad929f7d0e3c04409a4e73636898fa12a"></a><strong id="b84235270610360"><a name="b84235270610360"></a><a name="b84235270610360"></a>Resource Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="30.61%" id="mcps1.2.4.1.3"><p id="a274f3171fa8c49dd91180b97be73c99e"><a name="a274f3171fa8c49dd91180b97be73c99e"></a><a name="a274f3171fa8c49dd91180b97be73c99e"></a><strong id="b842352706182955"><a name="b842352706182955"></a><a name="b842352706182955"></a>Trace Name</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="re374057cf5844edfad7375b67f88ce24"><td class="cellrowborder" valign="top" width="47.5%" headers="mcps1.2.4.1.1 "><p id="a587f15d8dc62437499ff8ecee61b64fe"><a name="a587f15d8dc62437499ff8ecee61b64fe"></a><a name="a587f15d8dc62437499ff8ecee61b64fe"></a>Starting an ECS</p>
</td>
<td class="cellrowborder" valign="top" width="21.89%" headers="mcps1.2.4.1.2 "><p id="a063d3aa12f04462d8850ef97b8a0cf7f"><a name="a063d3aa12f04462d8850ef97b8a0cf7f"></a><a name="a063d3aa12f04462d8850ef97b8a0cf7f"></a>ecs</p>
</td>
<td class="cellrowborder" valign="top" width="30.61%" headers="mcps1.2.4.1.3 "><p id="a7a600ad5c0564de4b9a772d9e85ed1ef"><a name="a7a600ad5c0564de4b9a772d9e85ed1ef"></a><a name="a7a600ad5c0564de4b9a772d9e85ed1ef"></a>startServer</p>
</td>
</tr>
<tr id="r335af3eca09e40b69eeee06c4c2d6cd9"><td class="cellrowborder" valign="top" width="47.5%" headers="mcps1.2.4.1.1 "><p id="a3930ae1647db49adb000f7cb3c05df04"><a name="a3930ae1647db49adb000f7cb3c05df04"></a><a name="a3930ae1647db49adb000f7cb3c05df04"></a>Restarting an ECS</p>
</td>
<td class="cellrowborder" valign="top" width="21.89%" headers="mcps1.2.4.1.2 "><p id="ac847e523afa74358ab8479c93513890d"><a name="ac847e523afa74358ab8479c93513890d"></a><a name="ac847e523afa74358ab8479c93513890d"></a>ecs</p>
</td>
<td class="cellrowborder" valign="top" width="30.61%" headers="mcps1.2.4.1.3 "><p id="ab341be9570fe41fe807cf9ba16bd560f"><a name="ab341be9570fe41fe807cf9ba16bd560f"></a><a name="ab341be9570fe41fe807cf9ba16bd560f"></a>rebootServer</p>
</td>
</tr>
<tr id="rbb9dd4a944784e86984d5634e0537f83"><td class="cellrowborder" valign="top" width="47.5%" headers="mcps1.2.4.1.1 "><p id="ac46feb0a16ae475392908aaab7e2b45b"><a name="ac46feb0a16ae475392908aaab7e2b45b"></a><a name="ac46feb0a16ae475392908aaab7e2b45b"></a>Stopping an ECS</p>
</td>
<td class="cellrowborder" valign="top" width="21.89%" headers="mcps1.2.4.1.2 "><p id="a5da7813d1d0f4cdcad82b56212779150"><a name="a5da7813d1d0f4cdcad82b56212779150"></a><a name="a5da7813d1d0f4cdcad82b56212779150"></a>ecs</p>
</td>
<td class="cellrowborder" valign="top" width="30.61%" headers="mcps1.2.4.1.3 "><p id="aef4316bc379a43b3befb03fe08dd45fa"><a name="aef4316bc379a43b3befb03fe08dd45fa"></a><a name="aef4316bc379a43b3befb03fe08dd45fa"></a>stopServer</p>
</td>
</tr>
<tr id="r6339a23c72644f278c08056cae6282b2"><td class="cellrowborder" valign="top" width="47.5%" headers="mcps1.2.4.1.1 "><p id="aee452b4f7885447ba2d809d810a942ed"><a name="aee452b4f7885447ba2d809d810a942ed"></a><a name="aee452b4f7885447ba2d809d810a942ed"></a>Attaching a disk to an ECS (on the ECS console)</p>
</td>
<td class="cellrowborder" valign="top" width="21.89%" headers="mcps1.2.4.1.2 "><p id="a59312799886e45b89db9b1c540745443"><a name="a59312799886e45b89db9b1c540745443"></a><a name="a59312799886e45b89db9b1c540745443"></a>ecs</p>
</td>
<td class="cellrowborder" valign="top" width="30.61%" headers="mcps1.2.4.1.3 "><p id="a12117ddcc6e942c7a7ee1fe308c83636"><a name="a12117ddcc6e942c7a7ee1fe308c83636"></a><a name="a12117ddcc6e942c7a7ee1fe308c83636"></a>attachVolume2</p>
</td>
</tr>
<tr id="re322ad8a67fc48dd9ce0988a19da697b"><td class="cellrowborder" valign="top" width="47.5%" headers="mcps1.2.4.1.1 "><p id="a9b60ec00ff9641509faa259bbcb5fa0c"><a name="a9b60ec00ff9641509faa259bbcb5fa0c"></a><a name="a9b60ec00ff9641509faa259bbcb5fa0c"></a>Reinstalling the OS</p>
</td>
<td class="cellrowborder" valign="top" width="21.89%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240378_p145192709337"><a name="en-us_topic_0100240378_p145192709337"></a><a name="en-us_topic_0100240378_p145192709337"></a>ecs</p>
</td>
<td class="cellrowborder" valign="top" width="30.61%" headers="mcps1.2.4.1.3 "><p id="a36b28b2aec254685b893bae0d2b8ea10"><a name="a36b28b2aec254685b893bae0d2b8ea10"></a><a name="a36b28b2aec254685b893bae0d2b8ea10"></a>reinstallOs</p>
</td>
</tr>
<tr id="r8bb4447758424cceb93e09afaf57a80a"><td class="cellrowborder" valign="top" width="47.5%" headers="mcps1.2.4.1.1 "><p id="a462c3b388f634e4a9649202aaaf730dd"><a name="a462c3b388f634e4a9649202aaaf730dd"></a><a name="a462c3b388f634e4a9649202aaaf730dd"></a>Changing the OS</p>
</td>
<td class="cellrowborder" valign="top" width="21.89%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240378_p484569019337"><a name="en-us_topic_0100240378_p484569019337"></a><a name="en-us_topic_0100240378_p484569019337"></a>ecs</p>
</td>
<td class="cellrowborder" valign="top" width="30.61%" headers="mcps1.2.4.1.3 "><p id="a679b323513e6498cbf3277382adcd9ae"><a name="a679b323513e6498cbf3277382adcd9ae"></a><a name="a679b323513e6498cbf3277382adcd9ae"></a>changeOs</p>
</td>
</tr>
<tr id="r7e9b89d3c24d4b27acbc9265a7e59836"><td class="cellrowborder" valign="top" width="47.5%" headers="mcps1.2.4.1.1 "><p id="a013e7fe430c34fb1b94b910557f359ad"><a name="a013e7fe430c34fb1b94b910557f359ad"></a><a name="a013e7fe430c34fb1b94b910557f359ad"></a>Modifying ECS specifications</p>
</td>
<td class="cellrowborder" valign="top" width="21.89%" headers="mcps1.2.4.1.2 "><p id="a86a1d3bd08a048be841514a942fb0be6"><a name="a86a1d3bd08a048be841514a942fb0be6"></a><a name="a86a1d3bd08a048be841514a942fb0be6"></a>ecs</p>
</td>
<td class="cellrowborder" valign="top" width="30.61%" headers="mcps1.2.4.1.3 "><p id="a21ec8c701af942a293fa7f8445ad0677"><a name="a21ec8c701af942a293fa7f8445ad0677"></a><a name="a21ec8c701af942a293fa7f8445ad0677"></a>resizeServer</p>
</td>
</tr>
<tr id="rf4af1d63a69a40e0b36742772df369c9"><td class="cellrowborder" valign="top" width="47.5%" headers="mcps1.2.4.1.1 "><p id="a7c3b77f69b424151b25f7ed864b744c8"><a name="a7c3b77f69b424151b25f7ed864b744c8"></a><a name="a7c3b77f69b424151b25f7ed864b744c8"></a>Adding the automatic recovery tag to a VM</p>
</td>
<td class="cellrowborder" valign="top" width="21.89%" headers="mcps1.2.4.1.2 "><p id="a0fca81ba631c499d8d2af2db1e71497c"><a name="a0fca81ba631c499d8d2af2db1e71497c"></a><a name="a0fca81ba631c499d8d2af2db1e71497c"></a>ecs</p>
</td>
<td class="cellrowborder" valign="top" width="30.61%" headers="mcps1.2.4.1.3 "><p id="a00bbe05dadf5434680a5ba13b5a8c8d5"><a name="a00bbe05dadf5434680a5ba13b5a8c8d5"></a><a name="a00bbe05dadf5434680a5ba13b5a8c8d5"></a>addAutoRecovery</p>
</td>
</tr>
<tr id="rf615d15303c54e08a7edd695e59294a0"><td class="cellrowborder" valign="top" width="47.5%" headers="mcps1.2.4.1.1 "><p id="a416b47ddbf214618851b0c9d660a6af1"><a name="a416b47ddbf214618851b0c9d660a6af1"></a><a name="a416b47ddbf214618851b0c9d660a6af1"></a>Deleting the automatic recovery tag from a VM</p>
</td>
<td class="cellrowborder" valign="top" width="21.89%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240378_p564335384857"><a name="en-us_topic_0100240378_p564335384857"></a><a name="en-us_topic_0100240378_p564335384857"></a>ecs</p>
</td>
<td class="cellrowborder" valign="top" width="30.61%" headers="mcps1.2.4.1.3 "><p id="af67e816896d84b9bb97a08272908c149"><a name="af67e816896d84b9bb97a08272908c149"></a><a name="af67e816896d84b9bb97a08272908c149"></a>deleteAutoRecovery</p>
</td>
</tr>
<tr id="rc611a358f342468eb1f4f39bff9e1e24"><td class="cellrowborder" valign="top" width="47.5%" headers="mcps1.2.4.1.1 "><p id="ad758444e8bb647bda0bcde2133ac7d04"><a name="ad758444e8bb647bda0bcde2133ac7d04"></a><a name="ad758444e8bb647bda0bcde2133ac7d04"></a>Creating a security group</p>
</td>
<td class="cellrowborder" valign="top" width="21.89%" headers="mcps1.2.4.1.2 "><p id="ac788ca378c064ec684971c2e91978eaa"><a name="ac788ca378c064ec684971c2e91978eaa"></a><a name="ac788ca378c064ec684971c2e91978eaa"></a>ecs</p>
</td>
<td class="cellrowborder" valign="top" width="30.61%" headers="mcps1.2.4.1.3 "><p id="a76225ae6d8724b35a3d05fdf03a177d1"><a name="a76225ae6d8724b35a3d05fdf03a177d1"></a><a name="a76225ae6d8724b35a3d05fdf03a177d1"></a>createSecurityGroup</p>
</td>
</tr>
</tbody>
</table>


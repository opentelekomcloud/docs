# Key Operations on CSBS<a name="en-us_topic_0100273724"></a>

Cloud Server Backup Service \(CSBS\) can back up an entire ECS. It can use the consistent backup data of multiple Elastic Volume Service \(EVS\) disks to restore the service data of an ECS. CSBS ensures data security and service continuity.

With CTS, you can record operations associated with CSBS for future query, audit, and backtrack operations.

**Table  1**  CSBS operations that can be recorded by CTS

<a name="table1997296115354"></a>
<table><thead align="left"><tr id="ra66962a4b95745d28c72254db9e62b18"><th class="cellrowborder" valign="top" width="30.303030303030305%" id="mcps1.2.4.1.1"><p id="a05fe6a7fd2f64b8e8a33220fb5e501f9"><a name="a05fe6a7fd2f64b8e8a33220fb5e501f9"></a><a name="a05fe6a7fd2f64b8e8a33220fb5e501f9"></a><strong id="b842352706103557"><a name="b842352706103557"></a><a name="b842352706103557"></a>Operation</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.27272727272727%" id="mcps1.2.4.1.2"><p id="a2becdf394bc24f0293ebddc3715fe30f"><a name="a2becdf394bc24f0293ebddc3715fe30f"></a><a name="a2becdf394bc24f0293ebddc3715fe30f"></a><strong id="b84235270610360"><a name="b84235270610360"></a><a name="b84235270610360"></a>Resource Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="42.42424242424242%" id="mcps1.2.4.1.3"><p id="aa9bf3b51ca2c422eae144f73c6143446"><a name="aa9bf3b51ca2c422eae144f73c6143446"></a><a name="aa9bf3b51ca2c422eae144f73c6143446"></a><strong id="b842352706182955"><a name="b842352706182955"></a><a name="b842352706182955"></a>Trace Name</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r89493c1ae11544b2bb3f31d11533cbe0"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="aa1a1c60d91db4eedbb3de567109a66d7"><a name="aa1a1c60d91db4eedbb3de567109a66d7"></a><a name="aa1a1c60d91db4eedbb3de567109a66d7"></a>Creating a backup policy</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="a8f5f606271d2487282229290d76ae06c"><a name="a8f5f606271d2487282229290d76ae06c"></a><a name="a8f5f606271d2487282229290d76ae06c"></a>backupPolicy</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="a938d9b503dbe44e6a38f060747ff7c1f"><a name="a938d9b503dbe44e6a38f060747ff7c1f"></a><a name="a938d9b503dbe44e6a38f060747ff7c1f"></a>createBackupPolicy</p>
</td>
</tr>
<tr id="r23c06da62d854ab8820a44124846023a"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="a76a5c1a6c4244386a74cbcce359b0170"><a name="a76a5c1a6c4244386a74cbcce359b0170"></a><a name="a76a5c1a6c4244386a74cbcce359b0170"></a>Updating a backup policy</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="a64fc69619b0d4c5b8837fb99bf37e567"><a name="a64fc69619b0d4c5b8837fb99bf37e567"></a><a name="a64fc69619b0d4c5b8837fb99bf37e567"></a>backupPolicy</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="a97acb3c4f2f549c39e6909f68e3ea8a6"><a name="a97acb3c4f2f549c39e6909f68e3ea8a6"></a><a name="a97acb3c4f2f549c39e6909f68e3ea8a6"></a>updateBackupPolicy</p>
</td>
</tr>
<tr id="r9ccbfda30f0c4bb6a755cce94cb882f3"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="a6489ea2b5d074d4a922d769ae5aafa1a"><a name="a6489ea2b5d074d4a922d769ae5aafa1a"></a><a name="a6489ea2b5d074d4a922d769ae5aafa1a"></a>Deleting a backup policy</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="ac16a1ef334c046bcac3ab183b8e0994f"><a name="ac16a1ef334c046bcac3ab183b8e0994f"></a><a name="ac16a1ef334c046bcac3ab183b8e0994f"></a>backupPolicy</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="a27aa762d42dc416f970bca95642c9e4b"><a name="a27aa762d42dc416f970bca95642c9e4b"></a><a name="a27aa762d42dc416f970bca95642c9e4b"></a>deleteBackupPolicy</p>
</td>
</tr>
<tr id="r8224c5dbc2b94aa5b50fc85b1e059d84"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="af707cd4981d847b193f85c7cd0f20b73"><a name="af707cd4981d847b193f85c7cd0f20b73"></a><a name="af707cd4981d847b193f85c7cd0f20b73"></a>Binding resources</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="a25cd18aa96184989a2a4279092b56f48"><a name="a25cd18aa96184989a2a4279092b56f48"></a><a name="a25cd18aa96184989a2a4279092b56f48"></a>backupPolicy</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="ac765b47482d1401082086482d3eea8b8"><a name="ac765b47482d1401082086482d3eea8b8"></a><a name="ac765b47482d1401082086482d3eea8b8"></a>bindResources</p>
</td>
</tr>
<tr id="re5d41f98eb4c4babbf1979496d6adb05"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="acefe3bf8e3384789b655f58f2584fafc"><a name="acefe3bf8e3384789b655f58f2584fafc"></a><a name="acefe3bf8e3384789b655f58f2584fafc"></a>Executing a backup</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="ab8641751d43f48a4b8d8e6048a4403b6"><a name="ab8641751d43f48a4b8d8e6048a4403b6"></a><a name="ab8641751d43f48a4b8d8e6048a4403b6"></a>checkpointItem</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="a001c3a31a4e448f894f19a20f708f126"><a name="a001c3a31a4e448f894f19a20f708f126"></a><a name="a001c3a31a4e448f894f19a20f708f126"></a>createCheckpoint</p>
</td>
</tr>
<tr id="r9664d5ad489b4dcb8701eae9f2844863"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="a4c770d8757c2408caf9eee06fe2785da"><a name="a4c770d8757c2408caf9eee06fe2785da"></a><a name="a4c770d8757c2408caf9eee06fe2785da"></a>Restoring a backup</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240378_p927949193139"><a name="en-us_topic_0100240378_p927949193139"></a><a name="en-us_topic_0100240378_p927949193139"></a>checkpointItem</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="a5ccacb574b80431298288806e30f9206"><a name="a5ccacb574b80431298288806e30f9206"></a><a name="a5ccacb574b80431298288806e30f9206"></a>restoreCheckpointItem</p>
</td>
</tr>
<tr id="rc48d581c6e7343448dc32d99fb476583"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="a78c328dc787c4053a834686a7cd296d0"><a name="a78c328dc787c4053a834686a7cd296d0"></a><a name="a78c328dc787c4053a834686a7cd296d0"></a>Deleting a backup</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="aac9d2fb852194074a8215ec930c120dc"><a name="aac9d2fb852194074a8215ec930c120dc"></a><a name="aac9d2fb852194074a8215ec930c120dc"></a>checkpointItem</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="ac395cef89a904c5a818520a619eef75a"><a name="ac395cef89a904c5a818520a619eef75a"></a><a name="ac395cef89a904c5a818520a619eef75a"></a>deleteCheckpointItem</p>
</td>
</tr>
<tr id="r23c98ebc3d154101ba96fc3f83e4c028"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="a15971d3abba2446fb1eb039478dfee6f"><a name="a15971d3abba2446fb1eb039478dfee6f"></a><a name="a15971d3abba2446fb1eb039478dfee6f"></a>Backing up an ECS</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240378_p733073093139"><a name="en-us_topic_0100240378_p733073093139"></a><a name="en-us_topic_0100240378_p733073093139"></a>cloudServer</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="ae69e3bbb20004919b8adc729b9c5c6cf"><a name="ae69e3bbb20004919b8adc729b9c5c6cf"></a><a name="ae69e3bbb20004919b8adc729b9c5c6cf"></a>backupCloudServer</p>
</td>
</tr>
<tr id="r449b39b7061f49ab9c81bba6ef515429"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="a74657e8e7348451487cd8b505139d5f9"><a name="a74657e8e7348451487cd8b505139d5f9"></a><a name="a74657e8e7348451487cd8b505139d5f9"></a>Deleting a task</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="a7c68af25209240868bd1ddcc77ff9321"><a name="a7c68af25209240868bd1ddcc77ff9321"></a><a name="a7c68af25209240868bd1ddcc77ff9321"></a>operationLog</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="adb49259719074128b3d3e0472be4b925"><a name="adb49259719074128b3d3e0472be4b925"></a><a name="adb49259719074128b3d3e0472be4b925"></a>deleteOperationLog</p>
</td>
</tr>
<tr id="row14493238141218"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p16383546121217"><a name="p16383546121217"></a><a name="p16383546121217"></a>Batch adding or deleting tags of a backup</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p14649351141210"><a name="p14649351141210"></a><a name="p14649351141210"></a>checkpointItem</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p744616120138"><a name="p744616120138"></a><a name="p744616120138"></a>batchCreateOrDeleteCheckpointItemTags</p>
</td>
</tr>
<tr id="row1649317389122"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p53831346151212"><a name="p53831346151212"></a><a name="p53831346151212"></a>Adding a backup tag</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p1864915112125"><a name="p1864915112125"></a><a name="p1864915112125"></a>checkpointItem</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p13446413137"><a name="p13446413137"></a><a name="p13446413137"></a>createCheckpointItemTag</p>
</td>
</tr>
<tr id="row1749383813128"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p11383194615120"><a name="p11383194615120"></a><a name="p11383194615120"></a>Deleting a backup tag</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p56491151201211"><a name="p56491151201211"></a><a name="p56491151201211"></a>checkpointItem</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p114465101312"><a name="p114465101312"></a><a name="p114465101312"></a>deleteCheckpointItemTag</p>
</td>
</tr>
<tr id="row149317387126"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p1838334612126"><a name="p1838334612126"></a><a name="p1838334612126"></a>Batch adding or deleting tags of a backup policy</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p14649151101210"><a name="p14649151101210"></a><a name="p14649151101210"></a>backupPolicy</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p84466119134"><a name="p84466119134"></a><a name="p84466119134"></a>batchCreateOrDeleteBackupPolicyTags</p>
</td>
</tr>
<tr id="row17493638161212"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p83834467126"><a name="p83834467126"></a><a name="p83834467126"></a>Adding a backup policy tag</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p166491451161218"><a name="p166491451161218"></a><a name="p166491451161218"></a>backupPolicy</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p8446715130"><a name="p8446715130"></a><a name="p8446715130"></a>createBackupPolicyTag</p>
</td>
</tr>
<tr id="row14931038141214"><td class="cellrowborder" valign="top" width="30.303030303030305%" headers="mcps1.2.4.1.1 "><p id="p838317463123"><a name="p838317463123"></a><a name="p838317463123"></a>Deleting a backup policy tag</p>
</td>
<td class="cellrowborder" valign="top" width="27.27272727272727%" headers="mcps1.2.4.1.2 "><p id="p16491051141212"><a name="p16491051141212"></a><a name="p16491051141212"></a>backupPolicy</p>
</td>
<td class="cellrowborder" valign="top" width="42.42424242424242%" headers="mcps1.2.4.1.3 "><p id="p1844616114131"><a name="p1844616114131"></a><a name="p1844616114131"></a>deleteBackupPolicyTag</p>
</td>
</tr>
</tbody>
</table>


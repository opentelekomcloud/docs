# Key Operations on RTS<a name="en-us_topic_0100291676"></a>

Resource Template Service \(RTS\) provides templates for combining cloud resources and allows users to automatically create cloud resources they need using templates.

With CTS, you can record operations associated with RTS for later query, audit, and backtrack operations.

**Table  1**  RTS operations that can be recorded by CTS

<a name="table35840362173850"></a>
<table><thead align="left"><tr id="r4dd07d0416cb4eeb94f4d53a89bb7342"><th class="cellrowborder" valign="top" width="32.300000000000004%" id="mcps1.2.4.1.1"><p id="aa345862d2ff741b790d846cd54712c6d"><a name="aa345862d2ff741b790d846cd54712c6d"></a><a name="aa345862d2ff741b790d846cd54712c6d"></a><strong id="b842352706103557"><a name="b842352706103557"></a><a name="b842352706103557"></a>Operation</strong></p>
</th>
<th class="cellrowborder" valign="top" width="30.620000000000005%" id="mcps1.2.4.1.2"><p id="a1051aae3643747768d47b99f1af1215d"><a name="a1051aae3643747768d47b99f1af1215d"></a><a name="a1051aae3643747768d47b99f1af1215d"></a><strong id="b84235270610360"><a name="b84235270610360"></a><a name="b84235270610360"></a>Resource Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="37.08%" id="mcps1.2.4.1.3"><p id="a75b9cc3ae4c74aa992278c2aa62f78db"><a name="a75b9cc3ae4c74aa992278c2aa62f78db"></a><a name="a75b9cc3ae4c74aa992278c2aa62f78db"></a><strong id="b842352706182955"><a name="b842352706182955"></a><a name="b842352706182955"></a>Trace Name</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r2a4fe15e746140e0b6b9f669c2e7b078"><td class="cellrowborder" valign="top" width="32.300000000000004%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240417_p214355681600"><a name="en-us_topic_0100240417_p214355681600"></a><a name="en-us_topic_0100240417_p214355681600"></a>Creating a configuration</p>
</td>
<td class="cellrowborder" valign="top" width="30.620000000000005%" headers="mcps1.2.4.1.2 "><p id="a5ae1a98c31af4c73be8be5b2da1c8b89"><a name="a5ae1a98c31af4c73be8be5b2da1c8b89"></a><a name="a5ae1a98c31af4c73be8be5b2da1c8b89"></a>software_configs</p>
</td>
<td class="cellrowborder" valign="top" width="37.08%" headers="mcps1.2.4.1.3 "><p id="a78eada9384ea4bad9c7db9698f5dd690"><a name="a78eada9384ea4bad9c7db9698f5dd690"></a><a name="a78eada9384ea4bad9c7db9698f5dd690"></a>createSoftwareConfigs</p>
</td>
</tr>
<tr id="rd611ab99657a4190bd06db1d25d25ac0"><td class="cellrowborder" valign="top" width="32.300000000000004%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240417_p572731381600"><a name="en-us_topic_0100240417_p572731381600"></a><a name="en-us_topic_0100240417_p572731381600"></a>Deleting a configuration</p>
</td>
<td class="cellrowborder" valign="top" width="30.620000000000005%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240417_p700169116024"><a name="en-us_topic_0100240417_p700169116024"></a><a name="en-us_topic_0100240417_p700169116024"></a>software_configs</p>
</td>
<td class="cellrowborder" valign="top" width="37.08%" headers="mcps1.2.4.1.3 "><p id="adae3fc6dcdab41039d1d02182e73b94d"><a name="adae3fc6dcdab41039d1d02182e73b94d"></a><a name="adae3fc6dcdab41039d1d02182e73b94d"></a>deleteSoftwareConfigs</p>
</td>
</tr>
<tr id="r2a2c96aa5aaa4b029c90abcd2532564d"><td class="cellrowborder" valign="top" width="32.300000000000004%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240417_p104041951600"><a name="en-us_topic_0100240417_p104041951600"></a><a name="en-us_topic_0100240417_p104041951600"></a>Creating a deployment</p>
</td>
<td class="cellrowborder" valign="top" width="30.620000000000005%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240417_p395974816024"><a name="en-us_topic_0100240417_p395974816024"></a><a name="en-us_topic_0100240417_p395974816024"></a>software_deployments</p>
</td>
<td class="cellrowborder" valign="top" width="37.08%" headers="mcps1.2.4.1.3 "><p id="a12127bc472af446799c624b374508c92"><a name="a12127bc472af446799c624b374508c92"></a><a name="a12127bc472af446799c624b374508c92"></a>createSoftwareDeployments</p>
</td>
</tr>
<tr id="r93cd68bb7e544e28be9f3dac4e19843e"><td class="cellrowborder" valign="top" width="32.300000000000004%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240417_p13568311600"><a name="en-us_topic_0100240417_p13568311600"></a><a name="en-us_topic_0100240417_p13568311600"></a>Deleting a deployment</p>
</td>
<td class="cellrowborder" valign="top" width="30.620000000000005%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240417_p97548316024"><a name="en-us_topic_0100240417_p97548316024"></a><a name="en-us_topic_0100240417_p97548316024"></a>software_deployments</p>
</td>
<td class="cellrowborder" valign="top" width="37.08%" headers="mcps1.2.4.1.3 "><p id="a638bcf1d78794543a1c556470e5e3f56"><a name="a638bcf1d78794543a1c556470e5e3f56"></a><a name="a638bcf1d78794543a1c556470e5e3f56"></a>deleteSoftwareDeployments</p>
</td>
</tr>
<tr id="r306953837fc44e9b94161463a2ed506f"><td class="cellrowborder" valign="top" width="32.300000000000004%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240417_p496064101600"><a name="en-us_topic_0100240417_p496064101600"></a><a name="en-us_topic_0100240417_p496064101600"></a>Updating a deployment</p>
</td>
<td class="cellrowborder" valign="top" width="30.620000000000005%" headers="mcps1.2.4.1.2 "><p id="a883fcff9190e48489badf8774caee270"><a name="a883fcff9190e48489badf8774caee270"></a><a name="a883fcff9190e48489badf8774caee270"></a>software_deployments</p>
</td>
<td class="cellrowborder" valign="top" width="37.08%" headers="mcps1.2.4.1.3 "><p id="a3bc92d1ab37242c7847198caa039b8d3"><a name="a3bc92d1ab37242c7847198caa039b8d3"></a><a name="a3bc92d1ab37242c7847198caa039b8d3"></a>updateSoftwareDeployments</p>
</td>
</tr>
<tr id="rd3da1d3a3de748a3b846b52a9cb47648"><td class="cellrowborder" valign="top" width="32.300000000000004%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240417_p585045261600"><a name="en-us_topic_0100240417_p585045261600"></a><a name="en-us_topic_0100240417_p585045261600"></a>Stack management actions, such as canceling stack update or checking stack resources</p>
</td>
<td class="cellrowborder" valign="top" width="30.620000000000005%" headers="mcps1.2.4.1.2 "><p id="a35c507c7dc71437da50104fcb77066b8"><a name="a35c507c7dc71437da50104fcb77066b8"></a><a name="a35c507c7dc71437da50104fcb77066b8"></a>stacks</p>
</td>
<td class="cellrowborder" valign="top" width="37.08%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0100240417_p718318116041"><a name="en-us_topic_0100240417_p718318116041"></a><a name="en-us_topic_0100240417_p718318116041"></a>createStacksActions</p>
</td>
</tr>
<tr id="r50dcd1fb711b4bd2bb516c052af475ca"><td class="cellrowborder" valign="top" width="32.300000000000004%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240417_p356711341600"><a name="en-us_topic_0100240417_p356711341600"></a><a name="en-us_topic_0100240417_p356711341600"></a>Sending a signal to resources in a stack</p>
</td>
<td class="cellrowborder" valign="top" width="30.620000000000005%" headers="mcps1.2.4.1.2 "><p id="a0f0dd5bcad11406fa798025c8368691f"><a name="a0f0dd5bcad11406fa798025c8368691f"></a><a name="a0f0dd5bcad11406fa798025c8368691f"></a>stacks</p>
</td>
<td class="cellrowborder" valign="top" width="37.08%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0100240417_p204776316041"><a name="en-us_topic_0100240417_p204776316041"></a><a name="en-us_topic_0100240417_p204776316041"></a>createStacksResourcesSignal</p>
</td>
</tr>
<tr id="r9db0603c99b8445c9df9e88ea96a9dc4"><td class="cellrowborder" valign="top" width="32.300000000000004%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240417_p331265811600"><a name="en-us_topic_0100240417_p331265811600"></a><a name="en-us_topic_0100240417_p331265811600"></a>Creating a stack</p>
</td>
<td class="cellrowborder" valign="top" width="30.620000000000005%" headers="mcps1.2.4.1.2 "><p id="a7653fa1fc28d42a5a33847bf99dfa478"><a name="a7653fa1fc28d42a5a33847bf99dfa478"></a><a name="a7653fa1fc28d42a5a33847bf99dfa478"></a>stacks</p>
</td>
<td class="cellrowborder" valign="top" width="37.08%" headers="mcps1.2.4.1.3 "><p id="afbe07a57bbe04e0f89623445eb66302e"><a name="afbe07a57bbe04e0f89623445eb66302e"></a><a name="afbe07a57bbe04e0f89623445eb66302e"></a>createStacks</p>
</td>
</tr>
<tr id="re6004ca51eb74a54bbac05f5a331eca7"><td class="cellrowborder" valign="top" width="32.300000000000004%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240417_p571956701600"><a name="en-us_topic_0100240417_p571956701600"></a><a name="en-us_topic_0100240417_p571956701600"></a>Deleting a stack</p>
</td>
<td class="cellrowborder" valign="top" width="30.620000000000005%" headers="mcps1.2.4.1.2 "><p id="ab4eca0bbf70b465b9e06006396905a32"><a name="ab4eca0bbf70b465b9e06006396905a32"></a><a name="ab4eca0bbf70b465b9e06006396905a32"></a>stacks</p>
</td>
<td class="cellrowborder" valign="top" width="37.08%" headers="mcps1.2.4.1.3 "><p id="a7afc6f39fd8f4e80a052ee9966bdc766"><a name="a7afc6f39fd8f4e80a052ee9966bdc766"></a><a name="a7afc6f39fd8f4e80a052ee9966bdc766"></a>deleteStacks</p>
</td>
</tr>
<tr id="r7f65f468b76b49f0a1b725d2534f91bf"><td class="cellrowborder" valign="top" width="32.300000000000004%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240417_p210393081600"><a name="en-us_topic_0100240417_p210393081600"></a><a name="en-us_topic_0100240417_p210393081600"></a>Updating a stack</p>
</td>
<td class="cellrowborder" valign="top" width="30.620000000000005%" headers="mcps1.2.4.1.2 "><p id="a749af696045346849688bd8e6374e5e1"><a name="a749af696045346849688bd8e6374e5e1"></a><a name="a749af696045346849688bd8e6374e5e1"></a>stacks</p>
</td>
<td class="cellrowborder" valign="top" width="37.08%" headers="mcps1.2.4.1.3 "><p id="a779638b39d4e45909c159954af137bca"><a name="a779638b39d4e45909c159954af137bca"></a><a name="a779638b39d4e45909c159954af137bca"></a>updateStacks</p>
</td>
</tr>
<tr id="rf883682be37d47258c9b398749baec8a"><td class="cellrowborder" valign="top" width="32.300000000000004%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240417_p368351791600"><a name="en-us_topic_0100240417_p368351791600"></a><a name="en-us_topic_0100240417_p368351791600"></a>Previewing a stack</p>
</td>
<td class="cellrowborder" valign="top" width="30.620000000000005%" headers="mcps1.2.4.1.2 "><p id="af133cc56d41f4fe5810147d4c3726ced"><a name="af133cc56d41f4fe5810147d4c3726ced"></a><a name="af133cc56d41f4fe5810147d4c3726ced"></a>stacks</p>
</td>
<td class="cellrowborder" valign="top" width="37.08%" headers="mcps1.2.4.1.3 "><p id="a1e16b0e0080645db85314f4d48cdd8b7"><a name="a1e16b0e0080645db85314f4d48cdd8b7"></a><a name="a1e16b0e0080645db85314f4d48cdd8b7"></a>createStacksPreview</p>
</td>
</tr>
<tr id="rb0ecf5a503d347adaecc863ad016f2df"><td class="cellrowborder" valign="top" width="32.300000000000004%" headers="mcps1.2.4.1.1 "><p id="a24b4229cd6924fbba7bf5d6be792ce3b"><a name="a24b4229cd6924fbba7bf5d6be792ce3b"></a><a name="a24b4229cd6924fbba7bf5d6be792ce3b"></a>Identifying a resource as unhealthy</p>
</td>
<td class="cellrowborder" valign="top" width="30.620000000000005%" headers="mcps1.2.4.1.2 "><p id="acba2f8edb4b6479da4b3f56b54c3e97b"><a name="acba2f8edb4b6479da4b3f56b54c3e97b"></a><a name="acba2f8edb4b6479da4b3f56b54c3e97b"></a>stacks</p>
</td>
<td class="cellrowborder" valign="top" width="37.08%" headers="mcps1.2.4.1.3 "><p id="a013fb84276da47298030f3e08799e8b4"><a name="a013fb84276da47298030f3e08799e8b4"></a><a name="a013fb84276da47298030f3e08799e8b4"></a>patchStacksResource</p>
</td>
</tr>
<tr id="raa2763cdcac94d2681ac8c5e41f2d012"><td class="cellrowborder" valign="top" width="32.300000000000004%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240417_p17840841600"><a name="en-us_topic_0100240417_p17840841600"></a><a name="en-us_topic_0100240417_p17840841600"></a>Validating a template</p>
</td>
<td class="cellrowborder" valign="top" width="30.620000000000005%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240417_p527223316024"><a name="en-us_topic_0100240417_p527223316024"></a><a name="en-us_topic_0100240417_p527223316024"></a>validate</p>
</td>
<td class="cellrowborder" valign="top" width="37.08%" headers="mcps1.2.4.1.3 "><p id="af5b90282fd7b4496aef06a7ede53a2e0"><a name="af5b90282fd7b4496aef06a7ede53a2e0"></a><a name="af5b90282fd7b4496aef06a7ede53a2e0"></a>createValidate</p>
</td>
</tr>
</tbody>
</table>


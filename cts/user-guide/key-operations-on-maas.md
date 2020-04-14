# Key Operations on MaaS<a name="en-us_topic_0127477881"></a>

Object Storage Migration Service \(MaaS\) enables you to migrate object storage on other cloud platforms to the OBS service. The migration operations are simple. You can create automatic migration tasks or manually perform migration tasks on the console.

With CTS, you can record operations associated with MaaS for future query, audit, and backtrack operations.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>MaaS is a global-level service and MaaS traces are only displayed in the central region of the current site.  

**Table  1**  MaaS operations that can be recorded by CTS

<a name="table58567941183026"></a>
<table><thead align="left"><tr id="r2d9a2de1e1fb4a2ea790fdbd3763f81a"><th class="cellrowborder" valign="top" width="31.069999999999997%" id="mcps1.2.4.1.1"><p id="afbdd240e64b5421db35d77a2cf0e5d20"><a name="afbdd240e64b5421db35d77a2cf0e5d20"></a><a name="afbdd240e64b5421db35d77a2cf0e5d20"></a><strong id="b842352706103557"><a name="b842352706103557"></a><a name="b842352706103557"></a>Operation</strong></p>
</th>
<th class="cellrowborder" valign="top" width="30.15%" id="mcps1.2.4.1.2"><p id="aafc6f0d26d424c51a604df05526cc2f4"><a name="aafc6f0d26d424c51a604df05526cc2f4"></a><a name="aafc6f0d26d424c51a604df05526cc2f4"></a><strong id="b84235270610360"><a name="b84235270610360"></a><a name="b84235270610360"></a>Resource Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="38.78%" id="mcps1.2.4.1.3"><p id="a1588714580ff41eaac3214225091caea"><a name="a1588714580ff41eaac3214225091caea"></a><a name="a1588714580ff41eaac3214225091caea"></a><strong id="b842352706182955"><a name="b842352706182955"></a><a name="b842352706182955"></a>Trace Name</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r8cda2ec30293431b921c74fc6948741d"><td class="cellrowborder" valign="top" width="31.069999999999997%" headers="mcps1.2.4.1.1 "><p id="a2669928ef5c2407a867e739a52d432cf"><a name="a2669928ef5c2407a867e739a52d432cf"></a><a name="a2669928ef5c2407a867e739a52d432cf"></a>Creating a task</p>
</td>
<td class="cellrowborder" valign="top" width="30.15%" headers="mcps1.2.4.1.2 "><p id="ac27f992a63354f148d39828200060f11"><a name="ac27f992a63354f148d39828200060f11"></a><a name="ac27f992a63354f148d39828200060f11"></a>migrationTask</p>
</td>
<td class="cellrowborder" valign="top" width="38.78%" headers="mcps1.2.4.1.3 "><p id="a7e8e62a2d33547e0999f58051ef8bbea"><a name="a7e8e62a2d33547e0999f58051ef8bbea"></a><a name="a7e8e62a2d33547e0999f58051ef8bbea"></a>createTask</p>
</td>
</tr>
<tr id="reb196dca518e44a089ed778f062ec2f2"><td class="cellrowborder" valign="top" width="31.069999999999997%" headers="mcps1.2.4.1.1 "><p id="a0fd1fe7884684af9a8464a562d05c0e4"><a name="a0fd1fe7884684af9a8464a562d05c0e4"></a><a name="a0fd1fe7884684af9a8464a562d05c0e4"></a>Deleting a task</p>
</td>
<td class="cellrowborder" valign="top" width="30.15%" headers="mcps1.2.4.1.2 "><p id="ad6d7c0ebd50b47bbb325fe444729d84c"><a name="ad6d7c0ebd50b47bbb325fe444729d84c"></a><a name="ad6d7c0ebd50b47bbb325fe444729d84c"></a>migrationTask</p>
</td>
<td class="cellrowborder" valign="top" width="38.78%" headers="mcps1.2.4.1.3 "><p id="a073426dc1b524d13ad7f8781960a2149"><a name="a073426dc1b524d13ad7f8781960a2149"></a><a name="a073426dc1b524d13ad7f8781960a2149"></a>deleteTask</p>
</td>
</tr>
<tr id="r4a7f0f8d132e4b1684bc5283edd75015"><td class="cellrowborder" valign="top" width="31.069999999999997%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240354_p229287183252"><a name="en-us_topic_0100240354_p229287183252"></a><a name="en-us_topic_0100240354_p229287183252"></a>Starting a task</p>
</td>
<td class="cellrowborder" valign="top" width="30.15%" headers="mcps1.2.4.1.2 "><p id="a2a55dffc884f4a369d428a60421b1d02"><a name="a2a55dffc884f4a369d428a60421b1d02"></a><a name="a2a55dffc884f4a369d428a60421b1d02"></a>migrationTask</p>
</td>
<td class="cellrowborder" valign="top" width="38.78%" headers="mcps1.2.4.1.3 "><p id="ae03affbe5742402bb3d89aafedcc4916"><a name="ae03affbe5742402bb3d89aafedcc4916"></a><a name="ae03affbe5742402bb3d89aafedcc4916"></a>startTask</p>
</td>
</tr>
<tr id="r45e955b9ebd54b73b5b03291c4b89682"><td class="cellrowborder" valign="top" width="31.069999999999997%" headers="mcps1.2.4.1.1 "><p id="a3148b48637ca484dbff1db6f694b2047"><a name="a3148b48637ca484dbff1db6f694b2047"></a><a name="a3148b48637ca484dbff1db6f694b2047"></a>Stopping or suspending a task</p>
</td>
<td class="cellrowborder" valign="top" width="30.15%" headers="mcps1.2.4.1.2 "><p id="a6bb30a75a67b4f5cb44155aed2f25d99"><a name="a6bb30a75a67b4f5cb44155aed2f25d99"></a><a name="a6bb30a75a67b4f5cb44155aed2f25d99"></a>migrationTask</p>
</td>
<td class="cellrowborder" valign="top" width="38.78%" headers="mcps1.2.4.1.3 "><p id="a5302bbb602344bbf819ea9befc72b48e"><a name="a5302bbb602344bbf819ea9befc72b48e"></a><a name="a5302bbb602344bbf819ea9befc72b48e"></a>stopTask</p>
</td>
</tr>
</tbody>
</table>


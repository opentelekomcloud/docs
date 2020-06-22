# Key Operations on AS<a name="en-us_topic_0100236049"></a>

Auto Scaling \(AS\) is a service that automatically adjusts compute resources based on your service requirements and configured AS policies to ensure proper service running.

With CTS, you can record operations associated with AS for future query, audit, and backtrack operations.

**Table  1**  AS operations that can be recorded by CTS

<a name="table28380359152351"></a>
<table><thead align="left"><tr id="r3634b65116e145e38561c8003864432a"><th class="cellrowborder" valign="top" width="29.967003299670036%" id="mcps1.2.4.1.1"><p id="a7e070630b4364f9096d2acef90d30ed9"><a name="a7e070630b4364f9096d2acef90d30ed9"></a><a name="a7e070630b4364f9096d2acef90d30ed9"></a><strong id="b842352706103557"><a name="b842352706103557"></a><a name="b842352706103557"></a>Operation</strong></p>
</th>
<th class="cellrowborder" valign="top" width="31.986801319868015%" id="mcps1.2.4.1.2"><p id="a02795d1f3b3b48ceb756a3f8222e4291"><a name="a02795d1f3b3b48ceb756a3f8222e4291"></a><a name="a02795d1f3b3b48ceb756a3f8222e4291"></a><strong id="b84235270610360"><a name="b84235270610360"></a><a name="b84235270610360"></a>Resource Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="38.04619538046195%" id="mcps1.2.4.1.3"><p id="a824d959f8f294a7cbdc91ada6f3cdc77"><a name="a824d959f8f294a7cbdc91ada6f3cdc77"></a><a name="a824d959f8f294a7cbdc91ada6f3cdc77"></a><strong id="b842352706182955"><a name="b842352706182955"></a><a name="b842352706182955"></a>Trace Name</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="rdda2231ec12b4db682cc0776319725d3"><td class="cellrowborder" valign="top" width="29.967003299670036%" headers="mcps1.2.4.1.1 "><p id="aa9e1732b35fe4cbf83698b8949ea85ff"><a name="aa9e1732b35fe4cbf83698b8949ea85ff"></a><a name="aa9e1732b35fe4cbf83698b8949ea85ff"></a>Creating an AS group</p>
</td>
<td class="cellrowborder" valign="top" width="31.986801319868015%" headers="mcps1.2.4.1.2 "><p id="a87dc542e104149a18cb43e9db3a60385"><a name="a87dc542e104149a18cb43e9db3a60385"></a><a name="a87dc542e104149a18cb43e9db3a60385"></a>scaling_group</p>
</td>
<td class="cellrowborder" valign="top" width="38.04619538046195%" headers="mcps1.2.4.1.3 "><p id="a95f609e89b8a4296a2fa6853894d94f9"><a name="a95f609e89b8a4296a2fa6853894d94f9"></a><a name="a95f609e89b8a4296a2fa6853894d94f9"></a>createScalingGroup</p>
</td>
</tr>
<tr id="r96c66d19cd5e4c75b7e53d97bf132420"><td class="cellrowborder" valign="top" width="29.967003299670036%" headers="mcps1.2.4.1.1 "><p id="abef73b7c1b5347d1bfeba31876f0d121"><a name="abef73b7c1b5347d1bfeba31876f0d121"></a><a name="abef73b7c1b5347d1bfeba31876f0d121"></a>Modifying an AS group</p>
</td>
<td class="cellrowborder" valign="top" width="31.986801319868015%" headers="mcps1.2.4.1.2 "><p id="a73369f07b4cd4b17885f4212a4692a4e"><a name="a73369f07b4cd4b17885f4212a4692a4e"></a><a name="a73369f07b4cd4b17885f4212a4692a4e"></a>scaling_group</p>
</td>
<td class="cellrowborder" valign="top" width="38.04619538046195%" headers="mcps1.2.4.1.3 "><p id="ab71137bd978a43aa814871c37f237c43"><a name="ab71137bd978a43aa814871c37f237c43"></a><a name="ab71137bd978a43aa814871c37f237c43"></a>modifyScalingGroup</p>
</td>
</tr>
<tr id="r2e90899c457a461fab64c3b65b7b49a5"><td class="cellrowborder" valign="top" width="29.967003299670036%" headers="mcps1.2.4.1.1 "><p id="a7126af14abbc416c8ab25fad6fbab6a2"><a name="a7126af14abbc416c8ab25fad6fbab6a2"></a><a name="a7126af14abbc416c8ab25fad6fbab6a2"></a>Deleting an AS group</p>
</td>
<td class="cellrowborder" valign="top" width="31.986801319868015%" headers="mcps1.2.4.1.2 "><p id="aa2383f0982e54deba291f9ddbb970486"><a name="aa2383f0982e54deba291f9ddbb970486"></a><a name="aa2383f0982e54deba291f9ddbb970486"></a>scaling_group</p>
</td>
<td class="cellrowborder" valign="top" width="38.04619538046195%" headers="mcps1.2.4.1.3 "><p id="a1faacc5608654876bfe3e85117946721"><a name="a1faacc5608654876bfe3e85117946721"></a><a name="a1faacc5608654876bfe3e85117946721"></a>deleteScalingGroup</p>
</td>
</tr>
<tr id="rd9d9dd32ff6648efba77aa6c1d7013b1"><td class="cellrowborder" valign="top" width="29.967003299670036%" headers="mcps1.2.4.1.1 "><p id="aebaa3bebb45844999b03d410daabac49"><a name="aebaa3bebb45844999b03d410daabac49"></a><a name="aebaa3bebb45844999b03d410daabac49"></a>Enabling an AS group</p>
</td>
<td class="cellrowborder" valign="top" width="31.986801319868015%" headers="mcps1.2.4.1.2 "><p id="a4b15085d7494423a852c48da9fb87b79"><a name="a4b15085d7494423a852c48da9fb87b79"></a><a name="a4b15085d7494423a852c48da9fb87b79"></a>scaling_group</p>
</td>
<td class="cellrowborder" valign="top" width="38.04619538046195%" headers="mcps1.2.4.1.3 "><p id="a27413483f5ac47528030cf6475f2c5ce"><a name="a27413483f5ac47528030cf6475f2c5ce"></a><a name="a27413483f5ac47528030cf6475f2c5ce"></a>enableScalingGroup</p>
</td>
</tr>
<tr id="rb83ed9b331e1436d9ca0efab5b472d56"><td class="cellrowborder" valign="top" width="29.967003299670036%" headers="mcps1.2.4.1.1 "><p id="a872503b247e5438cbaf1b9b5f49c6697"><a name="a872503b247e5438cbaf1b9b5f49c6697"></a><a name="a872503b247e5438cbaf1b9b5f49c6697"></a>Disabling an AS group</p>
</td>
<td class="cellrowborder" valign="top" width="31.986801319868015%" headers="mcps1.2.4.1.2 "><p id="a197b7595cfcd40418672eeb02f8acc6e"><a name="a197b7595cfcd40418672eeb02f8acc6e"></a><a name="a197b7595cfcd40418672eeb02f8acc6e"></a>scaling_group</p>
</td>
<td class="cellrowborder" valign="top" width="38.04619538046195%" headers="mcps1.2.4.1.3 "><p id="ac6871173e5f54397b7a6769d28aab07e"><a name="ac6871173e5f54397b7a6769d28aab07e"></a><a name="ac6871173e5f54397b7a6769d28aab07e"></a>disableScalingGroup</p>
</td>
</tr>
<tr id="r928af1ff60914e5498f4edda3ae982cd"><td class="cellrowborder" valign="top" width="29.967003299670036%" headers="mcps1.2.4.1.1 "><p id="a55290ed7cb3640f7b33f0e6c92411f9b"><a name="a55290ed7cb3640f7b33f0e6c92411f9b"></a><a name="a55290ed7cb3640f7b33f0e6c92411f9b"></a>Creating an AS configuration</p>
</td>
<td class="cellrowborder" valign="top" width="31.986801319868015%" headers="mcps1.2.4.1.2 "><p id="af3e2f4714a2e490e8aad24925df96d83"><a name="af3e2f4714a2e490e8aad24925df96d83"></a><a name="af3e2f4714a2e490e8aad24925df96d83"></a>scaling_configuration</p>
</td>
<td class="cellrowborder" valign="top" width="38.04619538046195%" headers="mcps1.2.4.1.3 "><p id="a66c2ec70232a444b8353429267d7710f"><a name="a66c2ec70232a444b8353429267d7710f"></a><a name="a66c2ec70232a444b8353429267d7710f"></a>createScalingConfiguration</p>
</td>
</tr>
<tr id="rf763dd1760af46fcbd8098af6df3a1d9"><td class="cellrowborder" valign="top" width="29.967003299670036%" headers="mcps1.2.4.1.1 "><p id="a76653d308cec479e8fd0f2d4efe36d78"><a name="a76653d308cec479e8fd0f2d4efe36d78"></a><a name="a76653d308cec479e8fd0f2d4efe36d78"></a>Deleting an AS configuration</p>
</td>
<td class="cellrowborder" valign="top" width="31.986801319868015%" headers="mcps1.2.4.1.2 "><p id="aad216184a7d14b2cbf870c9c1e520dc7"><a name="aad216184a7d14b2cbf870c9c1e520dc7"></a><a name="aad216184a7d14b2cbf870c9c1e520dc7"></a>scaling_configuration</p>
</td>
<td class="cellrowborder" valign="top" width="38.04619538046195%" headers="mcps1.2.4.1.3 "><p id="ac8f988cd07d04bd1ac645de83f428958"><a name="ac8f988cd07d04bd1ac645de83f428958"></a><a name="ac8f988cd07d04bd1ac645de83f428958"></a>deleteScalingConfiguration</p>
</td>
</tr>
<tr id="rd42af1fefe5a4563a642fce5df050a05"><td class="cellrowborder" valign="top" width="29.967003299670036%" headers="mcps1.2.4.1.1 "><p id="abc50dff286244d858f660aee158faf65"><a name="abc50dff286244d858f660aee158faf65"></a><a name="abc50dff286244d858f660aee158faf65"></a>Deleting AS configurations in batches</p>
</td>
<td class="cellrowborder" valign="top" width="31.986801319868015%" headers="mcps1.2.4.1.2 "><p id="a4285f703fd3f411a8d8185432f682e5d"><a name="a4285f703fd3f411a8d8185432f682e5d"></a><a name="a4285f703fd3f411a8d8185432f682e5d"></a>scaling_configuration</p>
</td>
<td class="cellrowborder" valign="top" width="38.04619538046195%" headers="mcps1.2.4.1.3 "><p id="ac54686712fab4c98a92a279d549af69b"><a name="ac54686712fab4c98a92a279d549af69b"></a><a name="ac54686712fab4c98a92a279d549af69b"></a>batchDeleteScalingConfiguration</p>
</td>
</tr>
<tr id="rf780fed644774c6f97eaa3a781fe9e15"><td class="cellrowborder" valign="top" width="29.967003299670036%" headers="mcps1.2.4.1.1 "><p id="a3ab83c07ed2b4c8f9c20b5448ec04a89"><a name="a3ab83c07ed2b4c8f9c20b5448ec04a89"></a><a name="a3ab83c07ed2b4c8f9c20b5448ec04a89"></a>Creating an AS policy</p>
</td>
<td class="cellrowborder" valign="top" width="31.986801319868015%" headers="mcps1.2.4.1.2 "><p id="a28066f5efca94d3aa49d4f9b7fad0c50"><a name="a28066f5efca94d3aa49d4f9b7fad0c50"></a><a name="a28066f5efca94d3aa49d4f9b7fad0c50"></a>scaling_policy</p>
</td>
<td class="cellrowborder" valign="top" width="38.04619538046195%" headers="mcps1.2.4.1.3 "><p id="ac07c00be4afb49ba8472b027c604db36"><a name="ac07c00be4afb49ba8472b027c604db36"></a><a name="ac07c00be4afb49ba8472b027c604db36"></a>createScalingPolicy</p>
</td>
</tr>
<tr id="r8a8b74d297254de798f052857c3818ce"><td class="cellrowborder" valign="top" width="29.967003299670036%" headers="mcps1.2.4.1.1 "><p id="a7746111d651c427589e8ac3aa0cbf33d"><a name="a7746111d651c427589e8ac3aa0cbf33d"></a><a name="a7746111d651c427589e8ac3aa0cbf33d"></a>Modifying an AS policy</p>
</td>
<td class="cellrowborder" valign="top" width="31.986801319868015%" headers="mcps1.2.4.1.2 "><p id="ae8953524dd894191afee13d0cad54a07"><a name="ae8953524dd894191afee13d0cad54a07"></a><a name="ae8953524dd894191afee13d0cad54a07"></a>scaling_policy</p>
</td>
<td class="cellrowborder" valign="top" width="38.04619538046195%" headers="mcps1.2.4.1.3 "><p id="a6ddadb1a7d2e41cc86ea4130347f3674"><a name="a6ddadb1a7d2e41cc86ea4130347f3674"></a><a name="a6ddadb1a7d2e41cc86ea4130347f3674"></a>modifyScalingPolicy</p>
</td>
</tr>
<tr id="r072fa42b1af74fbe88a51266f382916a"><td class="cellrowborder" valign="top" width="29.967003299670036%" headers="mcps1.2.4.1.1 "><p id="ac2f270ba8a2f4cf992bcc4926073ff78"><a name="ac2f270ba8a2f4cf992bcc4926073ff78"></a><a name="ac2f270ba8a2f4cf992bcc4926073ff78"></a>Deleting an AS policy</p>
</td>
<td class="cellrowborder" valign="top" width="31.986801319868015%" headers="mcps1.2.4.1.2 "><p id="a0f6868eafd75440990e4a28d6bf48fb9"><a name="a0f6868eafd75440990e4a28d6bf48fb9"></a><a name="a0f6868eafd75440990e4a28d6bf48fb9"></a>scaling_policy</p>
</td>
<td class="cellrowborder" valign="top" width="38.04619538046195%" headers="mcps1.2.4.1.3 "><p id="a2463c1be9bd14c61af0dc85cc0acf895"><a name="a2463c1be9bd14c61af0dc85cc0acf895"></a><a name="a2463c1be9bd14c61af0dc85cc0acf895"></a>deleteScalingPolicy</p>
</td>
</tr>
<tr id="r7b4fdbd96c674a78ab14773d6ff9909d"><td class="cellrowborder" valign="top" width="29.967003299670036%" headers="mcps1.2.4.1.1 "><p id="a47b848f3e4144aeda3262ef5e7ac9f7b"><a name="a47b848f3e4144aeda3262ef5e7ac9f7b"></a><a name="a47b848f3e4144aeda3262ef5e7ac9f7b"></a>Enabling an AS policy</p>
</td>
<td class="cellrowborder" valign="top" width="31.986801319868015%" headers="mcps1.2.4.1.2 "><p id="adeea0c2db9c14363be784c11a5965b04"><a name="adeea0c2db9c14363be784c11a5965b04"></a><a name="adeea0c2db9c14363be784c11a5965b04"></a>scaling_policy</p>
</td>
<td class="cellrowborder" valign="top" width="38.04619538046195%" headers="mcps1.2.4.1.3 "><p id="a6ca18529e2ff4dc78afa173400919a02"><a name="a6ca18529e2ff4dc78afa173400919a02"></a><a name="a6ca18529e2ff4dc78afa173400919a02"></a>enableScalingPolicy</p>
</td>
</tr>
<tr id="r2f33e8227ba04cdd941315eb59dcc21c"><td class="cellrowborder" valign="top" width="29.967003299670036%" headers="mcps1.2.4.1.1 "><p id="a62782f291adf43f8ab2c1d2c07bd609d"><a name="a62782f291adf43f8ab2c1d2c07bd609d"></a><a name="a62782f291adf43f8ab2c1d2c07bd609d"></a>Disabling an AS policy</p>
</td>
<td class="cellrowborder" valign="top" width="31.986801319868015%" headers="mcps1.2.4.1.2 "><p id="a719a077312664ee1b1e0ab71723fbdec"><a name="a719a077312664ee1b1e0ab71723fbdec"></a><a name="a719a077312664ee1b1e0ab71723fbdec"></a>scaling_policy</p>
</td>
<td class="cellrowborder" valign="top" width="38.04619538046195%" headers="mcps1.2.4.1.3 "><p id="a38069f45779b4c5cb1d6e7a930c1b72a"><a name="a38069f45779b4c5cb1d6e7a930c1b72a"></a><a name="a38069f45779b4c5cb1d6e7a930c1b72a"></a>disableScalingPolicy</p>
</td>
</tr>
<tr id="r6997053255cb4821a7feabd7301b5568"><td class="cellrowborder" valign="top" width="29.967003299670036%" headers="mcps1.2.4.1.1 "><p id="aa924b2137c594977a41dbe431e12a8c7"><a name="aa924b2137c594977a41dbe431e12a8c7"></a><a name="aa924b2137c594977a41dbe431e12a8c7"></a>Executing an AS policy</p>
</td>
<td class="cellrowborder" valign="top" width="31.986801319868015%" headers="mcps1.2.4.1.2 "><p id="a6d46c4bd8d6844a08b893c6967f8f10d"><a name="a6d46c4bd8d6844a08b893c6967f8f10d"></a><a name="a6d46c4bd8d6844a08b893c6967f8f10d"></a>scaling_policy</p>
</td>
<td class="cellrowborder" valign="top" width="38.04619538046195%" headers="mcps1.2.4.1.3 "><p id="ab912b8d4c9f748589d2a6d7794413a62"><a name="ab912b8d4c9f748589d2a6d7794413a62"></a><a name="ab912b8d4c9f748589d2a6d7794413a62"></a>executeScalingPolicy</p>
</td>
</tr>
<tr id="r0091ae7c346f48a78a58e9d36d483e51"><td class="cellrowborder" valign="top" width="29.967003299670036%" headers="mcps1.2.4.1.1 "><p id="a90cf7d7140f646b58be8b3c3038c4965"><a name="a90cf7d7140f646b58be8b3c3038c4965"></a><a name="a90cf7d7140f646b58be8b3c3038c4965"></a>Removing an instance from an AS group</p>
</td>
<td class="cellrowborder" valign="top" width="31.986801319868015%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240378_p346375152351"><a name="en-us_topic_0100240378_p346375152351"></a><a name="en-us_topic_0100240378_p346375152351"></a>scaling_instance</p>
</td>
<td class="cellrowborder" valign="top" width="38.04619538046195%" headers="mcps1.2.4.1.3 "><p id="a22144cbe20f14c91917fd3b268c4b06b"><a name="a22144cbe20f14c91917fd3b268c4b06b"></a><a name="a22144cbe20f14c91917fd3b268c4b06b"></a>removeInstance</p>
</td>
</tr>
<tr id="r67ab0d3a670f44d4bda526ec48e9b0f5"><td class="cellrowborder" valign="top" width="29.967003299670036%" headers="mcps1.2.4.1.1 "><p id="a16a8234987b9464dbbd208403b8d027b"><a name="a16a8234987b9464dbbd208403b8d027b"></a><a name="a16a8234987b9464dbbd208403b8d027b"></a>Removing instances from an AS group in batches</p>
</td>
<td class="cellrowborder" valign="top" width="31.986801319868015%" headers="mcps1.2.4.1.2 "><p id="a87683da7b57646e08441dc30a5bad7e0"><a name="a87683da7b57646e08441dc30a5bad7e0"></a><a name="a87683da7b57646e08441dc30a5bad7e0"></a>scaling_instance</p>
</td>
<td class="cellrowborder" valign="top" width="38.04619538046195%" headers="mcps1.2.4.1.3 "><p id="ae94309b59f004c60ac10af9e08384519"><a name="ae94309b59f004c60ac10af9e08384519"></a><a name="ae94309b59f004c60ac10af9e08384519"></a>batchRemoveInstances</p>
</td>
</tr>
<tr id="r02ac0483bdb3435097ed9c185f61d420"><td class="cellrowborder" valign="top" width="29.967003299670036%" headers="mcps1.2.4.1.1 "><p id="a26b871cb90b749aab81a3aff3cb041dc"><a name="a26b871cb90b749aab81a3aff3cb041dc"></a><a name="a26b871cb90b749aab81a3aff3cb041dc"></a>Adding instances to an AS group in batches</p>
</td>
<td class="cellrowborder" valign="top" width="31.986801319868015%" headers="mcps1.2.4.1.2 "><p id="a25df7921efe74d65a21c19497c6eecf4"><a name="a25df7921efe74d65a21c19497c6eecf4"></a><a name="a25df7921efe74d65a21c19497c6eecf4"></a>scaling_instance</p>
</td>
<td class="cellrowborder" valign="top" width="38.04619538046195%" headers="mcps1.2.4.1.3 "><p id="a78e30daa5f284d7ea267144f625103ed"><a name="a78e30daa5f284d7ea267144f625103ed"></a><a name="a78e30daa5f284d7ea267144f625103ed"></a>batchAddInstances</p>
</td>
</tr>
</tbody>
</table>


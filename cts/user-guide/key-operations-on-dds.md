# Key Operations on DDS<a name="en-us_topic_0100363627"></a>

Document Database Service \(DDS\) is compatible with the MongoDB protocol and is secure, highly available, reliable, scalable, and easy to use. It provides DB instance creation, scaling, redundancy, backup, restoration, monitoring, and alarm reporting functions with just a few clicks on the DDS console.

With CTS, you can record operations associated with DDS for future query, audit, and backtrack operations.

**Table  1**  DDS operations that can be recorded by CTS

<a name="table3228948093953"></a>
<table><thead align="left"><tr id="r085db548aa6d460986356e596643a3cc"><th class="cellrowborder" valign="top" width="33.33%" id="mcps1.2.4.1.1"><p id="a2473fad514c945d3a9f021e01ae2880f"><a name="a2473fad514c945d3a9f021e01ae2880f"></a><a name="a2473fad514c945d3a9f021e01ae2880f"></a><strong id="a1d6e8624ec8d48b39793c2b607ad6940"><a name="a1d6e8624ec8d48b39793c2b607ad6940"></a><a name="a1d6e8624ec8d48b39793c2b607ad6940"></a>Operation</strong></p>
</th>
<th class="cellrowborder" valign="top" width="29.39%" id="mcps1.2.4.1.2"><p id="a1962133871ea46a181fbd1114e953548"><a name="a1962133871ea46a181fbd1114e953548"></a><a name="a1962133871ea46a181fbd1114e953548"></a><strong id="ae9f0943a97aa4f30985264bf85683848"><a name="ae9f0943a97aa4f30985264bf85683848"></a><a name="ae9f0943a97aa4f30985264bf85683848"></a>Resource Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="37.28%" id="mcps1.2.4.1.3"><p id="ac509a4a064674906a0ab006efdba9522"><a name="ac509a4a064674906a0ab006efdba9522"></a><a name="ac509a4a064674906a0ab006efdba9522"></a><strong id="ab556dff9de194efa99f4184c2a8dfb7e"><a name="ab556dff9de194efa99f4184c2a8dfb7e"></a><a name="ab556dff9de194efa99f4184c2a8dfb7e"></a>Trace Name</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r2ef4700b1f714ae1aaf03724455f16da"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.1 "><p id="a520938c3acde4ecba11cd42f1f225428"><a name="a520938c3acde4ecba11cd42f1f225428"></a><a name="a520938c3acde4ecba11cd42f1f225428"></a>Restoring data to a new DB instance</p>
</td>
<td class="cellrowborder" valign="top" width="29.39%" headers="mcps1.2.4.1.2 "><p id="a7747c62c7ae04db8b1be94ed4a830227"><a name="a7747c62c7ae04db8b1be94ed4a830227"></a><a name="a7747c62c7ae04db8b1be94ed4a830227"></a>instance</p>
</td>
<td class="cellrowborder" valign="top" width="37.28%" headers="mcps1.2.4.1.3 "><p id="a432c5c5dde4442ac801a522cabcfed8b"><a name="a432c5c5dde4442ac801a522cabcfed8b"></a><a name="a432c5c5dde4442ac801a522cabcfed8b"></a>ddsRestoreToNewInstance</p>
</td>
</tr>
<tr id="r7114f9f21dc04b5fbc196001d312a1a3"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.1 "><p id="ad0a7b28ac1184d57b85f2d4626728ee8"><a name="ad0a7b28ac1184d57b85f2d4626728ee8"></a><a name="ad0a7b28ac1184d57b85f2d4626728ee8"></a>Creating a DB instance</p>
</td>
<td class="cellrowborder" valign="top" width="29.39%" headers="mcps1.2.4.1.2 "><p id="a9621d204bb4f46449a34b539841d85da"><a name="a9621d204bb4f46449a34b539841d85da"></a><a name="a9621d204bb4f46449a34b539841d85da"></a>instance</p>
</td>
<td class="cellrowborder" valign="top" width="37.28%" headers="mcps1.2.4.1.3 "><p id="a44beb57220da4f6b94705a215b411cad"><a name="a44beb57220da4f6b94705a215b411cad"></a><a name="a44beb57220da4f6b94705a215b411cad"></a>ddsCreateInstance</p>
</td>
</tr>
<tr id="ra031904e8b0e4a05ae07a969c3882aab"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.1 "><p id="a43fb9a5a9bd74bca831ab94e32af1a1e"><a name="a43fb9a5a9bd74bca831ab94e32af1a1e"></a><a name="a43fb9a5a9bd74bca831ab94e32af1a1e"></a>Deleting a DB instance</p>
</td>
<td class="cellrowborder" valign="top" width="29.39%" headers="mcps1.2.4.1.2 "><p id="afb6b5455a19046f180d65501c89f2cbc"><a name="afb6b5455a19046f180d65501c89f2cbc"></a><a name="afb6b5455a19046f180d65501c89f2cbc"></a>instance</p>
</td>
<td class="cellrowborder" valign="top" width="37.28%" headers="mcps1.2.4.1.3 "><p id="a91d79e6007864231a77506a89f4f7dcb"><a name="a91d79e6007864231a77506a89f4f7dcb"></a><a name="a91d79e6007864231a77506a89f4f7dcb"></a>ddsDeleteInstance</p>
</td>
</tr>
<tr id="rbde08ed6e0fa42c8b8cc8fac2b7b8257"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.1 "><p id="a55c4919cb1eb4d1bbf42857b96746a77"><a name="a55c4919cb1eb4d1bbf42857b96746a77"></a><a name="a55c4919cb1eb4d1bbf42857b96746a77"></a>Restarting a DB instance</p>
</td>
<td class="cellrowborder" valign="top" width="29.39%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0100240370_p323530182518"><a name="en-us_topic_0100240370_p323530182518"></a><a name="en-us_topic_0100240370_p323530182518"></a>instance</p>
</td>
<td class="cellrowborder" valign="top" width="37.28%" headers="mcps1.2.4.1.3 "><p id="a8cad951df7ab46428889b91b9316b224"><a name="a8cad951df7ab46428889b91b9316b224"></a><a name="a8cad951df7ab46428889b91b9316b224"></a>ddsRestartInstance</p>
</td>
</tr>
<tr id="r2043965193ea492599727b355ab7099c"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.1 "><p id="ae7040a4fc4c4446d9aaae30ed1316681"><a name="ae7040a4fc4c4446d9aaae30ed1316681"></a><a name="ae7040a4fc4c4446d9aaae30ed1316681"></a>Adding nodes</p>
</td>
<td class="cellrowborder" valign="top" width="29.39%" headers="mcps1.2.4.1.2 "><p id="aca0ec36bd7644960afdb58a6869be8fd"><a name="aca0ec36bd7644960afdb58a6869be8fd"></a><a name="aca0ec36bd7644960afdb58a6869be8fd"></a>instance</p>
</td>
<td class="cellrowborder" valign="top" width="37.28%" headers="mcps1.2.4.1.3 "><p id="a01c1091e89b9465bb052c44b22717ce2"><a name="a01c1091e89b9465bb052c44b22717ce2"></a><a name="a01c1091e89b9465bb052c44b22717ce2"></a>ddsGrowInstance</p>
</td>
</tr>
<tr id="r43e5ceb769414ce790aa935274acf52f"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.1 "><p id="ab1a7be8d47a64da9a2943d048deea898"><a name="ab1a7be8d47a64da9a2943d048deea898"></a><a name="ab1a7be8d47a64da9a2943d048deea898"></a>Scaling up storage space</p>
</td>
<td class="cellrowborder" valign="top" width="29.39%" headers="mcps1.2.4.1.2 "><p id="a88617d011b4a49a4969d54a41842a2fc"><a name="a88617d011b4a49a4969d54a41842a2fc"></a><a name="a88617d011b4a49a4969d54a41842a2fc"></a>instance</p>
</td>
<td class="cellrowborder" valign="top" width="37.28%" headers="mcps1.2.4.1.3 "><p id="afca341b94793402591233c29deb95edb"><a name="afca341b94793402591233c29deb95edb"></a><a name="afca341b94793402591233c29deb95edb"></a>ddsExtendInstanceVolume</p>
</td>
</tr>
<tr id="r02edc7b376ec45ada17f0e661be1b2bf"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.1 "><p id="a350c114495f3449ba25c97198a022bab"><a name="a350c114495f3449ba25c97198a022bab"></a><a name="a350c114495f3449ba25c97198a022bab"></a>Resetting the database password</p>
</td>
<td class="cellrowborder" valign="top" width="29.39%" headers="mcps1.2.4.1.2 "><p id="ac5409ca7235b49d2afed16b38e8061d8"><a name="ac5409ca7235b49d2afed16b38e8061d8"></a><a name="ac5409ca7235b49d2afed16b38e8061d8"></a>instance</p>
</td>
<td class="cellrowborder" valign="top" width="37.28%" headers="mcps1.2.4.1.3 "><p id="a0affe07eab644d8bb4c4dc2da955de12"><a name="a0affe07eab644d8bb4c4dc2da955de12"></a><a name="a0affe07eab644d8bb4c4dc2da955de12"></a>ddsResetPassword</p>
</td>
</tr>
<tr id="r59ad9e15f70144d191063eea7a7048e2"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.1 "><p id="a512afd50609842b79db1b4d77500be5c"><a name="a512afd50609842b79db1b4d77500be5c"></a><a name="a512afd50609842b79db1b4d77500be5c"></a>Renaming a DB instance</p>
</td>
<td class="cellrowborder" valign="top" width="29.39%" headers="mcps1.2.4.1.2 "><p id="ad2597117bef448f78dd15406085ab262"><a name="ad2597117bef448f78dd15406085ab262"></a><a name="ad2597117bef448f78dd15406085ab262"></a>instance</p>
</td>
<td class="cellrowborder" valign="top" width="37.28%" headers="mcps1.2.4.1.3 "><p id="a662d0923c3b6478dbe31d1db4d65f11a"><a name="a662d0923c3b6478dbe31d1db4d65f11a"></a><a name="a662d0923c3b6478dbe31d1db4d65f11a"></a>ddsRenameInstance</p>
</td>
</tr>
<tr id="r84603301ebe74dd0b61e17579bb500f9"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.1 "><p id="a345ddad90cc84f969ea1d3de3ce50277"><a name="a345ddad90cc84f969ea1d3de3ce50277"></a><a name="a345ddad90cc84f969ea1d3de3ce50277"></a>Setting the O&amp;M window</p>
</td>
<td class="cellrowborder" valign="top" width="29.39%" headers="mcps1.2.4.1.2 "><p id="a5d1469b0fb854b438d1ade9388a62e08"><a name="a5d1469b0fb854b438d1ade9388a62e08"></a><a name="a5d1469b0fb854b438d1ade9388a62e08"></a>instance</p>
</td>
<td class="cellrowborder" valign="top" width="37.28%" headers="mcps1.2.4.1.3 "><p id="a0a8072ddfb414dca89ca27315bc3eb7c"><a name="a0a8072ddfb414dca89ca27315bc3eb7c"></a><a name="a0a8072ddfb414dca89ca27315bc3eb7c"></a>ddsSetOpsWindow</p>
</td>
</tr>
<tr id="r3863a66dd20d4a10b7522c78d07f6504"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.1 "><p id="a15edaf48f52347b6a59a035bc49aa487"><a name="a15edaf48f52347b6a59a035bc49aa487"></a><a name="a15edaf48f52347b6a59a035bc49aa487"></a>Switching SSL</p>
</td>
<td class="cellrowborder" valign="top" width="29.39%" headers="mcps1.2.4.1.2 "><p id="a4f4b99165f674ba28430f1911c19c08a"><a name="a4f4b99165f674ba28430f1911c19c08a"></a><a name="a4f4b99165f674ba28430f1911c19c08a"></a>instance</p>
</td>
<td class="cellrowborder" valign="top" width="37.28%" headers="mcps1.2.4.1.3 "><p id="ada4c507a4cfe43d1ae7c1747de7b02e3"><a name="ada4c507a4cfe43d1ae7c1747de7b02e3"></a><a name="ada4c507a4cfe43d1ae7c1747de7b02e3"></a>ddsSwitchSsl</p>
</td>
</tr>
<tr id="rf74a8cb10b484352936de98e18fcd869"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.1 "><p id="a894228c3cb754a94a40f25f9e0982b8e"><a name="a894228c3cb754a94a40f25f9e0982b8e"></a><a name="a894228c3cb754a94a40f25f9e0982b8e"></a>Changing a DB instance port</p>
</td>
<td class="cellrowborder" valign="top" width="29.39%" headers="mcps1.2.4.1.2 "><p id="a667a4e5b0245478b94291b18cf200682"><a name="a667a4e5b0245478b94291b18cf200682"></a><a name="a667a4e5b0245478b94291b18cf200682"></a>instance</p>
</td>
<td class="cellrowborder" valign="top" width="37.28%" headers="mcps1.2.4.1.3 "><p id="a470533130a8448ec9af7589bffb62645"><a name="a470533130a8448ec9af7589bffb62645"></a><a name="a470533130a8448ec9af7589bffb62645"></a>ddsModifyInstancePort</p>
</td>
</tr>
<tr id="re362d64ac76a46fcb94933b81e6b90f6"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.1 "><p id="a23174b609ece4b3dafa039e583aa886a"><a name="a23174b609ece4b3dafa039e583aa886a"></a><a name="a23174b609ece4b3dafa039e583aa886a"></a>Creating a backup</p>
</td>
<td class="cellrowborder" valign="top" width="29.39%" headers="mcps1.2.4.1.2 "><p id="ae52e04c452454fec9433ed7e27fef58b"><a name="ae52e04c452454fec9433ed7e27fef58b"></a><a name="ae52e04c452454fec9433ed7e27fef58b"></a>backup</p>
</td>
<td class="cellrowborder" valign="top" width="37.28%" headers="mcps1.2.4.1.3 "><p id="a37f22df5047e487db21db791d14ed9c7"><a name="a37f22df5047e487db21db791d14ed9c7"></a><a name="a37f22df5047e487db21db791d14ed9c7"></a>ddsCreateBackup</p>
</td>
</tr>
<tr id="r8120ad3ddcd746f299315427702e9dc3"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240370_p568515018254"><a name="en-us_topic_0100240370_p568515018254"></a><a name="en-us_topic_0100240370_p568515018254"></a>Deleting a backup</p>
</td>
<td class="cellrowborder" valign="top" width="29.39%" headers="mcps1.2.4.1.2 "><p id="a35a701e5d5fb42cd90aceac15ecba853"><a name="a35a701e5d5fb42cd90aceac15ecba853"></a><a name="a35a701e5d5fb42cd90aceac15ecba853"></a>backup</p>
</td>
<td class="cellrowborder" valign="top" width="37.28%" headers="mcps1.2.4.1.3 "><p id="a0110ed2b704c4294b4ea696b47a76541"><a name="a0110ed2b704c4294b4ea696b47a76541"></a><a name="a0110ed2b704c4294b4ea696b47a76541"></a>ddsDeleteBackup</p>
</td>
</tr>
<tr id="r9b29d1174ed24fa9babc746aa28f4a5e"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.1 "><p id="aca76a4779f0248f09a8d9d32a25d0f6c"><a name="aca76a4779f0248f09a8d9d32a25d0f6c"></a><a name="aca76a4779f0248f09a8d9d32a25d0f6c"></a>Setting a backup policy</p>
</td>
<td class="cellrowborder" valign="top" width="29.39%" headers="mcps1.2.4.1.2 "><p id="p53983344719"><a name="p53983344719"></a><a name="p53983344719"></a>instance</p>
</td>
<td class="cellrowborder" valign="top" width="37.28%" headers="mcps1.2.4.1.3 "><p id="ab5453023e685439aa5c3f287a7a799c2"><a name="ab5453023e685439aa5c3f287a7a799c2"></a><a name="ab5453023e685439aa5c3f287a7a799c2"></a>ddsSetBackupPolicy</p>
</td>
</tr>
<tr id="r129b85a0f07940b5b1e66c60bbbd468d"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.1 "><p id="a62b2ef9f4bd74ca19ed126766c87f4dd"><a name="a62b2ef9f4bd74ca19ed126766c87f4dd"></a><a name="a62b2ef9f4bd74ca19ed126766c87f4dd"></a>Applying a parameter group</p>
</td>
<td class="cellrowborder" valign="top" width="29.39%" headers="mcps1.2.4.1.2 "><p id="a239941e827e447f0b3eb422e7defebd4"><a name="a239941e827e447f0b3eb422e7defebd4"></a><a name="a239941e827e447f0b3eb422e7defebd4"></a>parameterGroup</p>
</td>
<td class="cellrowborder" valign="top" width="37.28%" headers="mcps1.2.4.1.3 "><p id="ab59d81117e0946db826a2514598e6f92"><a name="ab59d81117e0946db826a2514598e6f92"></a><a name="ab59d81117e0946db826a2514598e6f92"></a>ddsApplyConfigurations</p>
</td>
</tr>
<tr id="ra585a875fa7a43dc96cec1c748d0d477"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.1 "><p id="a8c11c37110a54b5bb87ff3a889b077f2"><a name="a8c11c37110a54b5bb87ff3a889b077f2"></a><a name="a8c11c37110a54b5bb87ff3a889b077f2"></a>Copying a parameter group</p>
</td>
<td class="cellrowborder" valign="top" width="29.39%" headers="mcps1.2.4.1.2 "><p id="a05a9889754e64d49bd1043d0727dd2ed"><a name="a05a9889754e64d49bd1043d0727dd2ed"></a><a name="a05a9889754e64d49bd1043d0727dd2ed"></a>parameterGroup</p>
</td>
<td class="cellrowborder" valign="top" width="37.28%" headers="mcps1.2.4.1.3 "><p id="a8f5f6557d83141e89fd1aa2bd231d57d"><a name="a8f5f6557d83141e89fd1aa2bd231d57d"></a><a name="a8f5f6557d83141e89fd1aa2bd231d57d"></a>ddsCopyConfigurations</p>
</td>
</tr>
<tr id="r12c70a4abd4c41ddb4fbadbf99d150ba"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.1 "><p id="a3132c290d4f84040a43bc5cd525e6b83"><a name="a3132c290d4f84040a43bc5cd525e6b83"></a><a name="a3132c290d4f84040a43bc5cd525e6b83"></a>Resetting a parameter group</p>
</td>
<td class="cellrowborder" valign="top" width="29.39%" headers="mcps1.2.4.1.2 "><p id="a1d4138b42ad14b0fafa88b368fa375a8"><a name="a1d4138b42ad14b0fafa88b368fa375a8"></a><a name="a1d4138b42ad14b0fafa88b368fa375a8"></a>parameterGroup</p>
</td>
<td class="cellrowborder" valign="top" width="37.28%" headers="mcps1.2.4.1.3 "><p id="abcfb1a1eb00d4d6ba734756673703a75"><a name="abcfb1a1eb00d4d6ba734756673703a75"></a><a name="abcfb1a1eb00d4d6ba734756673703a75"></a>ddsResetConfigurations</p>
</td>
</tr>
<tr id="r4228e39290d04283bd5faf9b565d41bb"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.1 "><p id="ac3b3a0e166a1403e94e86dd0ca44850b"><a name="ac3b3a0e166a1403e94e86dd0ca44850b"></a><a name="ac3b3a0e166a1403e94e86dd0ca44850b"></a>Creating a parameter group</p>
</td>
<td class="cellrowborder" valign="top" width="29.39%" headers="mcps1.2.4.1.2 "><p id="ad35ec983ef0f4d4e978889a2cfceeecc"><a name="ad35ec983ef0f4d4e978889a2cfceeecc"></a><a name="ad35ec983ef0f4d4e978889a2cfceeecc"></a>parameterGroup</p>
</td>
<td class="cellrowborder" valign="top" width="37.28%" headers="mcps1.2.4.1.3 "><p id="a5a22a6113d2e48e4a21f6d29d511f892"><a name="a5a22a6113d2e48e4a21f6d29d511f892"></a><a name="a5a22a6113d2e48e4a21f6d29d511f892"></a>ddsCreateConfigurations</p>
</td>
</tr>
<tr id="ra15fd8112f0944848a6b6ca9d4051a59"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.1 "><p id="a92250db2e7554683b5f9bc36c0e0f16f"><a name="a92250db2e7554683b5f9bc36c0e0f16f"></a><a name="a92250db2e7554683b5f9bc36c0e0f16f"></a>Deleting a parameter group</p>
</td>
<td class="cellrowborder" valign="top" width="29.39%" headers="mcps1.2.4.1.2 "><p id="a527289d47ec249da84848c3824b701eb"><a name="a527289d47ec249da84848c3824b701eb"></a><a name="a527289d47ec249da84848c3824b701eb"></a>parameterGroup</p>
</td>
<td class="cellrowborder" valign="top" width="37.28%" headers="mcps1.2.4.1.3 "><p id="aa931152ca162478e947938ace33ae4c0"><a name="aa931152ca162478e947938ace33ae4c0"></a><a name="aa931152ca162478e947938ace33ae4c0"></a>ddsDeleteConfigurations</p>
</td>
</tr>
<tr id="r2779c3bcc5a04b229ad341f1a1d88d8a"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.1 "><p id="a7b5f1be8e3ff4a41ac73ecc322544a0a"><a name="a7b5f1be8e3ff4a41ac73ecc322544a0a"></a><a name="a7b5f1be8e3ff4a41ac73ecc322544a0a"></a>Updating a parameter group</p>
</td>
<td class="cellrowborder" valign="top" width="29.39%" headers="mcps1.2.4.1.2 "><p id="ad020405fd10945789a221c6a70317f2c"><a name="ad020405fd10945789a221c6a70317f2c"></a><a name="ad020405fd10945789a221c6a70317f2c"></a>parameterGroup</p>
</td>
<td class="cellrowborder" valign="top" width="37.28%" headers="mcps1.2.4.1.3 "><p id="a81ad151683874853a96d523a4832c321"><a name="a81ad151683874853a96d523a4832c321"></a><a name="a81ad151683874853a96d523a4832c321"></a>ddsUpdateConfigurations</p>
</td>
</tr>
<tr id="row559312613918"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.1 "><p id="p4156193763912"><a name="p4156193763912"></a><a name="p4156193763912"></a>Binding an EIP</p>
</td>
<td class="cellrowborder" valign="top" width="29.39%" headers="mcps1.2.4.1.2 "><p id="p20640124273914"><a name="p20640124273914"></a><a name="p20640124273914"></a>instance</p>
</td>
<td class="cellrowborder" valign="top" width="37.28%" headers="mcps1.2.4.1.3 "><p id="p13607249123915"><a name="p13607249123915"></a><a name="p13607249123915"></a>ddsBindIP</p>
</td>
</tr>
<tr id="row16593182610393"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.1 "><p id="p41561537103914"><a name="p41561537103914"></a><a name="p41561537103914"></a>Unbinding an EIP</p>
</td>
<td class="cellrowborder" valign="top" width="29.39%" headers="mcps1.2.4.1.2 "><p id="p664074243912"><a name="p664074243912"></a><a name="p664074243912"></a>instance</p>
</td>
<td class="cellrowborder" valign="top" width="37.28%" headers="mcps1.2.4.1.3 "><p id="p13607194983914"><a name="p13607194983914"></a><a name="p13607194983914"></a>ddsUnbindIP</p>
</td>
</tr>
<tr id="row155933265398"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.1 "><p id="p915614379397"><a name="p915614379397"></a><a name="p915614379397"></a>Adding a tag</p>
</td>
<td class="cellrowborder" valign="top" width="29.39%" headers="mcps1.2.4.1.2 "><p id="p86401242163918"><a name="p86401242163918"></a><a name="p86401242163918"></a>tag</p>
</td>
<td class="cellrowborder" valign="top" width="37.28%" headers="mcps1.2.4.1.3 "><p id="p760711496395"><a name="p760711496395"></a><a name="p760711496395"></a>ddsAddTag</p>
</td>
</tr>
<tr id="row11593162610390"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.1 "><p id="p91568379398"><a name="p91568379398"></a><a name="p91568379398"></a>Deleting a tag</p>
</td>
<td class="cellrowborder" valign="top" width="29.39%" headers="mcps1.2.4.1.2 "><p id="p17640642133915"><a name="p17640642133915"></a><a name="p17640642133915"></a>tag</p>
</td>
<td class="cellrowborder" valign="top" width="37.28%" headers="mcps1.2.4.1.3 "><p id="p760719494391"><a name="p760719494391"></a><a name="p760719494391"></a>ddsDeleteTag</p>
</td>
</tr>
<tr id="row85931926153916"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.1 "><p id="p8156103713396"><a name="p8156103713396"></a><a name="p8156103713396"></a>Adding a DB instance tag</p>
</td>
<td class="cellrowborder" valign="top" width="29.39%" headers="mcps1.2.4.1.2 "><p id="p5640124233911"><a name="p5640124233911"></a><a name="p5640124233911"></a>tag</p>
</td>
<td class="cellrowborder" valign="top" width="37.28%" headers="mcps1.2.4.1.3 "><p id="p86071449173918"><a name="p86071449173918"></a><a name="p86071449173918"></a>ddsAddInstanceTags</p>
</td>
</tr>
<tr id="row2593426153914"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.1 "><p id="p16156237123915"><a name="p16156237123915"></a><a name="p16156237123915"></a>Reverting nodes that fail to be added</p>
</td>
<td class="cellrowborder" valign="top" width="29.39%" headers="mcps1.2.4.1.2 "><p id="p3640194215396"><a name="p3640194215396"></a><a name="p3640194215396"></a>instance</p>
</td>
<td class="cellrowborder" valign="top" width="37.28%" headers="mcps1.2.4.1.3 "><p id="p86071549153918"><a name="p86071549153918"></a><a name="p86071549153918"></a>ddsDeleteExtendedDdsNode</p>
</td>
</tr>
<tr id="row1059342663910"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.1 "><p id="p10156183716397"><a name="p10156183716397"></a><a name="p10156183716397"></a>Changing node classes</p>
</td>
<td class="cellrowborder" valign="top" width="29.39%" headers="mcps1.2.4.1.2 "><p id="p66401042143915"><a name="p66401042143915"></a><a name="p66401042143915"></a>instance</p>
</td>
<td class="cellrowborder" valign="top" width="37.28%" headers="mcps1.2.4.1.3 "><p id="p136078494392"><a name="p136078494392"></a><a name="p136078494392"></a>ddsResizeInstance</p>
</td>
</tr>
<tr id="row853813478478"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.1 "><p id="p6460185818470"><a name="p6460185818470"></a><a name="p6460185818470"></a>Changing the security group of a DB instance</p>
</td>
<td class="cellrowborder" valign="top" width="29.39%" headers="mcps1.2.4.1.2 "><p id="p128193394814"><a name="p128193394814"></a><a name="p128193394814"></a>instance</p>
</td>
<td class="cellrowborder" valign="top" width="37.28%" headers="mcps1.2.4.1.3 "><p id="p10476181494820"><a name="p10476181494820"></a><a name="p10476181494820"></a>ddsModifySecurityGroup</p>
</td>
</tr>
<tr id="row16367135044715"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.2.4.1.1 "><p id="p646075874711"><a name="p646075874711"></a><a name="p646075874711"></a>Executing a database command</p>
</td>
<td class="cellrowborder" valign="top" width="29.39%" headers="mcps1.2.4.1.2 "><p id="p781919313488"><a name="p781919313488"></a><a name="p781919313488"></a>instance</p>
</td>
<td class="cellrowborder" valign="top" width="37.28%" headers="mcps1.2.4.1.3 "><p id="p16476514194817"><a name="p16476514194817"></a><a name="p16476514194817"></a>ddsExecCommand</p>
</td>
</tr>
</tbody>
</table>


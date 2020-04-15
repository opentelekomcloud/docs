# Destination Link Configurations of Loader Jobs<a name="EN-US_TOPIC_0125375320"></a>

## Overview<a name="s8b89660ef1a9445f81716688666282c0"></a>

When Loader jobs save data to different storage locations, a destination link needs to be selected and the link properties need to be configured.

## obs-connector<a name="s98fb51b91fe04f60a06a4e2f28e36404"></a>

**Table  1**  Destination link properties of  **obs-connector**

<a name="tdb4771fe991f4972bb8e846674b92a3b"></a>
<table><thead align="left"><tr id="rdae16b8d057d42e9bbdd99a752adf0e1"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.3.1.1"><p id="a0616cad469464c469e581b3183ca5756"><a name="a0616cad469464c469e581b3183ca5756"></a><a name="a0616cad469464c469e581b3183ca5756"></a><strong id="ac822abcfc5bf4444ae998157696d3eef"><a name="ac822abcfc5bf4444ae998157696d3eef"></a><a name="ac822abcfc5bf4444ae998157696d3eef"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="75%" id="mcps1.2.3.1.2"><p id="a89f1fb4c5780483a9492f6eef1338029"><a name="a89f1fb4c5780483a9492f6eef1338029"></a><a name="a89f1fb4c5780483a9492f6eef1338029"></a><strong id="ad6cea4a7ebad4a8eaffa068cc11a636d"><a name="ad6cea4a7ebad4a8eaffa068cc11a636d"></a><a name="ad6cea4a7ebad4a8eaffa068cc11a636d"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="ra9a7fb4d69ef4851a8ab470fcc3f758c"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="af1ce4fc26f8649c8b2201e03e4b50da7"><a name="af1ce4fc26f8649c8b2201e03e4b50da7"></a><a name="af1ce4fc26f8649c8b2201e03e4b50da7"></a>Bucket Name</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="adde5010471894bf9a222136ccc876922"><a name="adde5010471894bf9a222136ccc876922"></a><a name="adde5010471894bf9a222136ccc876922"></a>OBS bucket for storing final data</p>
</td>
</tr>
<tr id="ra628f409f9644798b6c8d7c5a380cc78"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="a6db94abc20aa48178b402fa138feea7d"><a name="a6db94abc20aa48178b402fa138feea7d"></a><a name="a6db94abc20aa48178b402fa138feea7d"></a>Output directory</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="a12d319193f20402ba960942d3b393ffe"><a name="a12d319193f20402ba960942d3b393ffe"></a><a name="a12d319193f20402ba960942d3b393ffe"></a>Directory for storing final data in the bucket. A directory must be specified.</p>
</td>
</tr>
<tr id="rc9ea664044354ef3adcc193b38f2494c"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="af713af588f1b43b687b58497c50c548b"><a name="af713af588f1b43b687b58497c50c548b"></a><a name="af713af588f1b43b687b58497c50c548b"></a>File format</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="a2ff48115633d45b8913f3ac5ba621105"><a name="a2ff48115633d45b8913f3ac5ba621105"></a><a name="a2ff48115633d45b8913f3ac5ba621105"></a>Loader supports the following file formats of data stored in OBS:</p>
<a name="u649dbbd9536c41cf9bb4dd04de55ba31"></a><a name="u649dbbd9536c41cf9bb4dd04de55ba31"></a><ul id="u649dbbd9536c41cf9bb4dd04de55ba31"><li><strong id="a1c4f3c75d69b47928992fcabf66365f3"><a name="a1c4f3c75d69b47928992fcabf66365f3"></a><a name="a1c4f3c75d69b47928992fcabf66365f3"></a>CSV_FILE</strong>: Specifies a text file. When the destination link is a database link, only the text file is supported.</li><li><strong id="ad0796e9241b240a696c42edded28a854"><a name="ad0796e9241b240a696c42edded28a854"></a><a name="ad0796e9241b240a696c42edded28a854"></a>BINARY_FILE</strong>: Specifies binary files excluding text files.</li></ul>
</td>
</tr>
<tr id="raf7228798fd449f88d44e09f56a8b0af"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="a4f781f2a546940fa8d1cfc07a0f02729"><a name="a4f781f2a546940fa8d1cfc07a0f02729"></a><a name="a4f781f2a546940fa8d1cfc07a0f02729"></a>Line Separator</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="a1ec380be312a473383aeb4b6d324f8e5"><a name="a1ec380be312a473383aeb4b6d324f8e5"></a><a name="a1ec380be312a473383aeb4b6d324f8e5"></a>Identifier of each line end of final data</p>
</td>
</tr>
<tr id="r98a3854c2a184b63b089f6d44fa4b239"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="acb4bfac970df4316ac55fb1bc4c71078"><a name="acb4bfac970df4316ac55fb1bc4c71078"></a><a name="acb4bfac970df4316ac55fb1bc4c71078"></a>Field Separator</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="a49e14da61a044e72b6825da66b52a84f"><a name="a49e14da61a044e72b6825da66b52a84f"></a><a name="a49e14da61a044e72b6825da66b52a84f"></a>Identifier of each field end of final data</p>
</td>
</tr>
<tr id="r3fddd62fb23745f680a38dd7e2ed98a8"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="ae63f496f0a474af48e96c1c5c57898d1"><a name="ae63f496f0a474af48e96c1c5c57898d1"></a><a name="ae63f496f0a474af48e96c1c5c57898d1"></a>Encode type</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="a18a9924ce1274800a27a46e5717c1237"><a name="a18a9924ce1274800a27a46e5717c1237"></a><a name="a18a9924ce1274800a27a46e5717c1237"></a>Text encoding type of final data. It takes effect for text files only.</p>
</td>
</tr>
</tbody>
</table>

## generic-jdbc-connector<a name="s0912defa989944d6b2c25e2ece5615ac"></a>

**Table  2**  Destination link properties of  **generic-jdbc-connector**

<a name="t3e9e8d753bfb40c6b49d64d9330880cd"></a>
<table><thead align="left"><tr id="rb986b409e22444e7957b845d60a0dfd9"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.3.1.1"><p id="a7e80c1a28ba64565bf8931a99f0d64b0"><a name="a7e80c1a28ba64565bf8931a99f0d64b0"></a><a name="a7e80c1a28ba64565bf8931a99f0d64b0"></a><strong id="aa7423d84197c4f35a457b11e8f5aeb5a"><a name="aa7423d84197c4f35a457b11e8f5aeb5a"></a><a name="aa7423d84197c4f35a457b11e8f5aeb5a"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="75%" id="mcps1.2.3.1.2"><p id="adfeaafb167324d9486c1d9e47600144f"><a name="adfeaafb167324d9486c1d9e47600144f"></a><a name="adfeaafb167324d9486c1d9e47600144f"></a><strong id="af266d51b5c6a457b838e9d5274e9f361"><a name="af266d51b5c6a457b838e9d5274e9f361"></a><a name="af266d51b5c6a457b838e9d5274e9f361"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r741ec1fd4dcf4645957b5c6d031a21ba"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="abe375224cb504719859dfa2448dc0ceb"><a name="abe375224cb504719859dfa2448dc0ceb"></a><a name="abe375224cb504719859dfa2448dc0ceb"></a>Schema name</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="af79709fd13f84cf0981cef09fa5c82e4"><a name="af79709fd13f84cf0981cef09fa5c82e4"></a><a name="af79709fd13f84cf0981cef09fa5c82e4"></a>Name of the database saving final data</p>
</td>
</tr>
<tr id="r0ef2cd2fa3cd479699054c45484496a6"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="a73dac9857adb4b51ace80ccd1870372d"><a name="a73dac9857adb4b51ace80ccd1870372d"></a><a name="a73dac9857adb4b51ace80ccd1870372d"></a>Table name</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="ac19ef9baf1914441bd4ad3a49031f519"><a name="ac19ef9baf1914441bd4ad3a49031f519"></a><a name="ac19ef9baf1914441bd4ad3a49031f519"></a>Name of the table saving final data</p>
</td>
</tr>
</tbody>
</table>

## ftp-connector or sftp-connector<a name="s9cc5e7efa9f44468a2a1792eb476a4e3"></a>

**Table  3**  Destination link properties of  **ftp-connector** or **sftp-connector**

<a name="t3dd3ba8e1e084deca5398dc32dceaddb"></a>
<table><thead align="left"><tr id="r73f1e8dd6e684bf88ad3a7a7a6409358"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.3.1.1"><p id="a377f8b27fac64abe94fcfc8c6f155726"><a name="a377f8b27fac64abe94fcfc8c6f155726"></a><a name="a377f8b27fac64abe94fcfc8c6f155726"></a><strong id="a6fa144f2987d4a9e9a83cb8e60d49121"><a name="a6fa144f2987d4a9e9a83cb8e60d49121"></a><a name="a6fa144f2987d4a9e9a83cb8e60d49121"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="75%" id="mcps1.2.3.1.2"><p id="a61a3cf8cfd00495dbd558875de315285"><a name="a61a3cf8cfd00495dbd558875de315285"></a><a name="a61a3cf8cfd00495dbd558875de315285"></a><strong id="a488b39e2ce9a4be3ae91f8d6feb43583"><a name="a488b39e2ce9a4be3ae91f8d6feb43583"></a><a name="a488b39e2ce9a4be3ae91f8d6feb43583"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r92c8223dfe6b44a184944351c8b09bf2"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="a26a316561323474a973a48d28a6b8052"><a name="a26a316561323474a973a48d28a6b8052"></a><a name="a26a316561323474a973a48d28a6b8052"></a>Output directory</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="a0fa8e17c122b4c63a3602ab30f4d134b"><a name="a0fa8e17c122b4c63a3602ab30f4d134b"></a><a name="a0fa8e17c122b4c63a3602ab30f4d134b"></a>Directory for storing final data in the file server. A directory must be specified.</p>
</td>
</tr>
<tr id="r8cbb910283b7456facfe7adb67e06a48"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="ad4e75ae1e3f6430e9d199ca70e5d25c3"><a name="ad4e75ae1e3f6430e9d199ca70e5d25c3"></a><a name="ad4e75ae1e3f6430e9d199ca70e5d25c3"></a>File format</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="ab064ef1e1b664b898ec96dba23f81cfc"><a name="ab064ef1e1b664b898ec96dba23f81cfc"></a><a name="ab064ef1e1b664b898ec96dba23f81cfc"></a>Loader supports the following file formats of data stored in the file server:</p>
<a name="u2921e5e599c84787a0cbb957dca86060"></a><a name="u2921e5e599c84787a0cbb957dca86060"></a><ul id="u2921e5e599c84787a0cbb957dca86060"><li><strong id="a46bd41d6abce414a8409ec625544572a"><a name="a46bd41d6abce414a8409ec625544572a"></a><a name="a46bd41d6abce414a8409ec625544572a"></a>CSV_FILE</strong>: Specifies a text file. When the destination link is a database link, only the text file is supported.</li><li><strong id="a29bdd002a8b54235981b07a4d34eb6be"><a name="a29bdd002a8b54235981b07a4d34eb6be"></a><a name="a29bdd002a8b54235981b07a4d34eb6be"></a>BINARY_FILE</strong>: Specifies binary files excluding text files.</li></ul>
</td>
</tr>
<tr id="r6611f8b38a994eed88f7d27330da2441"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="a176882b7b90b499eadd1822ff49d3ea9"><a name="a176882b7b90b499eadd1822ff49d3ea9"></a><a name="a176882b7b90b499eadd1822ff49d3ea9"></a>Line Separator</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="a49cc532508854845a183d78367230c8f"><a name="a49cc532508854845a183d78367230c8f"></a><a name="a49cc532508854845a183d78367230c8f"></a>Identifier of each line end of final data</p>
<div class="note" id="ndea6587a75d84f4d8cd3dea01ea7cda6"><a name="ndea6587a75d84f4d8cd3dea01ea7cda6"></a><a name="ndea6587a75d84f4d8cd3dea01ea7cda6"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="a4a23f0db6e034a128ba8dcbec0ee77a7"><a name="a4a23f0db6e034a128ba8dcbec0ee77a7"></a><a name="a4a23f0db6e034a128ba8dcbec0ee77a7"></a>When FTP or SFTP serves as a destination link and <span class="parmname" id="p959e42ab38f34ad184caa46e2ec0e1b9"><a name="p959e42ab38f34ad184caa46e2ec0e1b9"></a><a name="p959e42ab38f34ad184caa46e2ec0e1b9"></a><b>File format</b></span>&nbsp;is set to&nbsp;<span class="parmvalue" id="p69ce4f01ad7e4abf9140a3139dccfc0a"><a name="p69ce4f01ad7e4abf9140a3139dccfc0a"></a><a name="p69ce4f01ad7e4abf9140a3139dccfc0a"></a><b>BINARY_FILE</b></span>, the value of&nbsp;<span class="parmname" id="p6a8642f97a3a49ab95fe1f3267c9ebc6"><a name="p6a8642f97a3a49ab95fe1f3267c9ebc6"></a><a name="p6a8642f97a3a49ab95fe1f3267c9ebc6"></a><b>Line Separator</b></span> in the advanced properties is invalid.</p>
</div></div>
</td>
</tr>
<tr id="re64cb7820009469fb8efd0bf9389f882"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="a2e78dca3aa2f4426a5603eacd210aa09"><a name="a2e78dca3aa2f4426a5603eacd210aa09"></a><a name="a2e78dca3aa2f4426a5603eacd210aa09"></a>Field Separator</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="a2fcf7b0d25834e8d84b48dc475ec82db"><a name="a2fcf7b0d25834e8d84b48dc475ec82db"></a><a name="a2fcf7b0d25834e8d84b48dc475ec82db"></a>Identifier of each field end of final data</p>
<div class="note" id="n65cb1f6f79d348de9dace9a5540534dd"><a name="n65cb1f6f79d348de9dace9a5540534dd"></a><a name="n65cb1f6f79d348de9dace9a5540534dd"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="a6ab92cfe046649bebc010434292e14c5"><a name="a6ab92cfe046649bebc010434292e14c5"></a><a name="a6ab92cfe046649bebc010434292e14c5"></a>When FTP or SFTP serves as a destination link and <span class="parmname" id="p20193c98c1ff44849db64de7577113cd"><a name="p20193c98c1ff44849db64de7577113cd"></a><a name="p20193c98c1ff44849db64de7577113cd"></a><b>File format</b></span>&nbsp;is set to&nbsp;<span class="parmvalue" id="p1fb323d477e6453396927ce2bd735e24"><a name="p1fb323d477e6453396927ce2bd735e24"></a><a name="p1fb323d477e6453396927ce2bd735e24"></a><b>BINARY_FILE</b></span>, the value of&nbsp;<span class="parmname" id="pc3b2d2cf628f452691cfe93fd3f058e6"><a name="pc3b2d2cf628f452691cfe93fd3f058e6"></a><a name="pc3b2d2cf628f452691cfe93fd3f058e6"></a><b>Field Separator</b></span> in the advanced properties is invalid.</p>
</div></div>
</td>
</tr>
<tr id="r950f1dc248af4b2687a8aa918c736428"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="a6d1353f3cfed42bbbacf3e9b55249ad8"><a name="a6d1353f3cfed42bbbacf3e9b55249ad8"></a><a name="a6d1353f3cfed42bbbacf3e9b55249ad8"></a>Encode type</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="ad67e9c7a45374efba191cef9b9a76c68"><a name="ad67e9c7a45374efba191cef9b9a76c68"></a><a name="ad67e9c7a45374efba191cef9b9a76c68"></a>Text encoding type of final data. It takes effect for text files only.</p>
</td>
</tr>
</tbody>
</table>

## hbase-connector<a name="s132f6ec3810b46c3b30336a1a87bff9a"></a>

**Table  4**  Destination link properties of  **hbase-connector**

<a name="t512bd5297d214cb59bd72bdb8d7efc0f"></a>
<table><thead align="left"><tr id="rfa2052d6899c4e57a47011f619dc7b84"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.3.1.1"><p id="a10c7fa2744e94549b0312629da7017f6"><a name="a10c7fa2744e94549b0312629da7017f6"></a><a name="a10c7fa2744e94549b0312629da7017f6"></a><strong id="a64a358c9062643908e029e1f66f26761"><a name="a64a358c9062643908e029e1f66f26761"></a><a name="a64a358c9062643908e029e1f66f26761"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="75%" id="mcps1.2.3.1.2"><p id="abea87d46a17a48be83a43fb81f746873"><a name="abea87d46a17a48be83a43fb81f746873"></a><a name="abea87d46a17a48be83a43fb81f746873"></a><strong id="ab59fe66d86b2445cb9845c591c78c2ae"><a name="ab59fe66d86b2445cb9845c591c78c2ae"></a><a name="ab59fe66d86b2445cb9845c591c78c2ae"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r53adc0b017a64e1f9d3141d4e421324f"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="a006ae05b7d464cf3be441c9be5bdcc8f"><a name="a006ae05b7d464cf3be441c9be5bdcc8f"></a><a name="a006ae05b7d464cf3be441c9be5bdcc8f"></a>Table name</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="a094adb6a85954e01b72e1c069c9456c2"><a name="a094adb6a85954e01b72e1c069c9456c2"></a><a name="a094adb6a85954e01b72e1c069c9456c2"></a>Name of the HBase table saving final data. You can query and select it on the interface.</p>
</td>
</tr>
<tr id="rc31bcdd732c34aa5a9b9dae13b67f006"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="a2472d6f9a5384752817c89a7fdeb4ee5"><a name="a2472d6f9a5384752817c89a7fdeb4ee5"></a><a name="a2472d6f9a5384752817c89a7fdeb4ee5"></a>Method</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="a48f5227440304e089cc36f856ee02b65"><a name="a48f5227440304e089cc36f856ee02b65"></a><a name="a48f5227440304e089cc36f856ee02b65"></a>Data can be imported to an HBase table using either <strong id="a219d07914e92470fbe2d45e5e8bfb6ad"><a name="a219d07914e92470fbe2d45e5e8bfb6ad"></a><a name="a219d07914e92470fbe2d45e5e8bfb6ad"></a>BULKLOAD</strong>&nbsp;or&nbsp;<strong id="a421f41fa01464c6db38f4d4e50f968a3"><a name="a421f41fa01464c6db38f4d4e50f968a3"></a><a name="a421f41fa01464c6db38f4d4e50f968a3"></a>PUTLIST</strong>.</p>
</td>
</tr>
<tr id="rf526c64c085846f48ea40d9d169788b7"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="a2f6e3e982c7f435ba0388e263bc16edb"><a name="a2f6e3e982c7f435ba0388e263bc16edb"></a><a name="a2f6e3e982c7f435ba0388e263bc16edb"></a>Clear data before import</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="a9820f9c6956d4973b38f35b0dca43b56"><a name="a9820f9c6956d4973b38f35b0dca43b56"></a><a name="a9820f9c6956d4973b38f35b0dca43b56"></a>Whether to clear data in the destination HBase table. Options are as follows:</p>
<a name="u0b79879bad784388adc3f87da75903ff"></a><a name="u0b79879bad784388adc3f87da75903ff"></a><ul id="u0b79879bad784388adc3f87da75903ff"><li><strong id="ae85860e9d19142be8b3a7e18d80a0a6a"><a name="ae85860e9d19142be8b3a7e18d80a0a6a"></a><a name="ae85860e9d19142be8b3a7e18d80a0a6a"></a>True</strong>: Clean up data in the table.</li><li><strong id="a2685240e92654f36bb82c4eebd41b1d2"><a name="a2685240e92654f36bb82c4eebd41b1d2"></a><a name="a2685240e92654f36bb82c4eebd41b1d2"></a>False</strong>: Do not clean up data in the table. When you select&nbsp;<strong id="a9bdf9a07fc3342acb14baa0338c24c01"><a name="a9bdf9a07fc3342acb14baa0338c24c01"></a><a name="a9bdf9a07fc3342acb14baa0338c24c01"></a>False</strong>, an error is reported during job running if data exists in the table.</li></ul>
</td>
</tr>
</tbody>
</table>

## hdfs-connector<a name="sd792a34536214e7bbf3cf1806f222a3e"></a>

**Table  5**  Destination link properties of  **hdfs-connector**

<a name="tdaf4dde5df8c47a298cd4b3cd83a72aa"></a>
<table><thead align="left"><tr id="r3956af7321d146f99257926b027a2801"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.3.1.1"><p id="a4609644af1da419b8e2472c109ee5e61"><a name="a4609644af1da419b8e2472c109ee5e61"></a><a name="a4609644af1da419b8e2472c109ee5e61"></a><strong id="a868e1b2f292d4e21ad49ea442b96baaa"><a name="a868e1b2f292d4e21ad49ea442b96baaa"></a><a name="a868e1b2f292d4e21ad49ea442b96baaa"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="75%" id="mcps1.2.3.1.2"><p id="aa41bb80ca0184299acd5c3f4dadf4872"><a name="aa41bb80ca0184299acd5c3f4dadf4872"></a><a name="aa41bb80ca0184299acd5c3f4dadf4872"></a><strong id="a731ae593652a4c0b8f14d466f750745d"><a name="a731ae593652a4c0b8f14d466f750745d"></a><a name="a731ae593652a4c0b8f14d466f750745d"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r83ba1a46277e49dd9e2c565a71b9075a"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0071084973_p385045217275"><a name="en-us_topic_0071084973_p385045217275"></a><a name="en-us_topic_0071084973_p385045217275"></a>Output directory</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="a0321c6cc2b3647beb8f9ab02edbf3e95"><a name="a0321c6cc2b3647beb8f9ab02edbf3e95"></a><a name="a0321c6cc2b3647beb8f9ab02edbf3e95"></a>Directory for storing final data in HDFS. A directory must be specified.</p>
</td>
</tr>
<tr id="r6dfa486333fe43d697f7717570516cf4"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="ae5847bb8197749f1b02d15bebe3ee3fd"><a name="ae5847bb8197749f1b02d15bebe3ee3fd"></a><a name="ae5847bb8197749f1b02d15bebe3ee3fd"></a>File format</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="aaa505671216c41f3b84ac000317351a0"><a name="aaa505671216c41f3b84ac000317351a0"></a><a name="aaa505671216c41f3b84ac000317351a0"></a>Loader supports the following file formats of data stored in HDFS:</p>
<a name="u3622d2dc86e84994aa0dc27359934363"></a><a name="u3622d2dc86e84994aa0dc27359934363"></a><ul id="u3622d2dc86e84994aa0dc27359934363"><li><strong id="ac9eba77d5aab4e6ca6585f9e3d599c26"><a name="ac9eba77d5aab4e6ca6585f9e3d599c26"></a><a name="ac9eba77d5aab4e6ca6585f9e3d599c26"></a>CSV_FILE</strong>: Specifies a text file. When the destination link is a database link, only the text file is supported.</li><li><strong id="aafdf06f1536740b7ba7f2371011ffc77"><a name="aafdf06f1536740b7ba7f2371011ffc77"></a><a name="aafdf06f1536740b7ba7f2371011ffc77"></a>BINARY_FILE</strong>: Specifies binary files excluding text files.</li></ul>
</td>
</tr>
<tr id="r1b4e6a3ae52f4beba1c76a4d8f5753c3"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0071084973_p402135418121"><a name="en-us_topic_0071084973_p402135418121"></a><a name="en-us_topic_0071084973_p402135418121"></a>Compression codec</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="ad19e6606076b43e0b49e34f41f8d8563"><a name="ad19e6606076b43e0b49e34f41f8d8563"></a><a name="ad19e6606076b43e0b49e34f41f8d8563"></a>Compression mode used when a file is saved to HDFS. The following modes are supported: <strong id="a9401b08f55b94962a9122fd4e5b8857a"><a name="a9401b08f55b94962a9122fd4e5b8857a"></a><a name="a9401b08f55b94962a9122fd4e5b8857a"></a>NONE</strong>,&nbsp;<strong id="a91f67275c1944b079d3525063392d472"><a name="a91f67275c1944b079d3525063392d472"></a><a name="a91f67275c1944b079d3525063392d472"></a>DEFLATE</strong>,&nbsp;<strong id="a7030b2b8a39245ceb727893b98036031"><a name="a7030b2b8a39245ceb727893b98036031"></a><a name="a7030b2b8a39245ceb727893b98036031"></a>GZIP</strong>,&nbsp;<strong id="a44a8cad6638049e0a22ba28d729b4fdf"><a name="a44a8cad6638049e0a22ba28d729b4fdf"></a><a name="a44a8cad6638049e0a22ba28d729b4fdf"></a>BZIP2</strong>,&nbsp;<strong id="ae405772388cb453881b6c2631b66876b"><a name="ae405772388cb453881b6c2631b66876b"></a><a name="ae405772388cb453881b6c2631b66876b"></a>LZ4</strong> <strong id="b137058371000"><a name="b137058371000"></a><a name="b137058371000"></a>and</strong>&nbsp;<strong id="a888d3b94268a46e8bd89d74f8d5b6c0e"><a name="a888d3b94268a46e8bd89d74f8d5b6c0e"></a><a name="a888d3b94268a46e8bd89d74f8d5b6c0e"></a>SNAPPY</strong>.</p>
</td>
</tr>
<tr id="r2f631892d3d2474aa12ed68d56b46d25"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="a247d4b519a3543079a318bdf6fd90ada"><a name="a247d4b519a3543079a318bdf6fd90ada"></a><a name="a247d4b519a3543079a318bdf6fd90ada"></a>Overwrite</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="aea347c0b9142479ca061909e472b9b0c"><a name="aea347c0b9142479ca061909e472b9b0c"></a><a name="aea347c0b9142479ca061909e472b9b0c"></a>How to process files in the output directory when files are imported to HDFS. Options are as follows:</p>
<a name="u1409c8e7f4664d518b6146dc8fa1f59a"></a><a name="u1409c8e7f4664d518b6146dc8fa1f59a"></a><ul id="u1409c8e7f4664d518b6146dc8fa1f59a"><li><strong id="a2244cf50960f4737bf712cf0c93dece7"><a name="a2244cf50960f4737bf712cf0c93dece7"></a><a name="a2244cf50960f4737bf712cf0c93dece7"></a>True</strong>: Clean up files in the directory and import new files by default.</li><li><strong id="ada116fdc52504d2496a212b84c948c19"><a name="ada116fdc52504d2496a212b84c948c19"></a><a name="ada116fdc52504d2496a212b84c948c19"></a>False</strong>: Do not clean up files. If files exist in the output directory, job running fails.</li></ul>
</td>
</tr>
<tr id="r5c04848f4e2e421c8b6d3b4ba0fc1b44"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="a4f4e0441b4214a4da2a4edb02b8fac67"><a name="a4f4e0441b4214a4da2a4edb02b8fac67"></a><a name="a4f4e0441b4214a4da2a4edb02b8fac67"></a>Line Separator</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="a88877e937e7b4a4aafc0e7f2cbdd5408"><a name="a88877e937e7b4a4aafc0e7f2cbdd5408"></a><a name="a88877e937e7b4a4aafc0e7f2cbdd5408"></a>Identifier of each line end of final data</p>
<div class="note" id="naafe91b9141a4ebba6de6f4d1b9e38ca"><a name="naafe91b9141a4ebba6de6f4d1b9e38ca"></a><a name="naafe91b9141a4ebba6de6f4d1b9e38ca"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="a021dfa545caa48f58d18a77645539d12"><a name="a021dfa545caa48f58d18a77645539d12"></a><a name="a021dfa545caa48f58d18a77645539d12"></a>When HDFS serves as a destination link and <span class="parmname" id="pbb40d7f9bc744122a2888551225890b6"><a name="pbb40d7f9bc744122a2888551225890b6"></a><a name="pbb40d7f9bc744122a2888551225890b6"></a><b>File format</b></span>&nbsp;is set to&nbsp;<span class="parmvalue" id="pe7f2dc9aac08494cb28b24a79dced172"><a name="pe7f2dc9aac08494cb28b24a79dced172"></a><a name="pe7f2dc9aac08494cb28b24a79dced172"></a><b>BINARY_FILE</b></span>, the value of&nbsp;<span class="parmname" id="peb7dbbc28b7945c88776b0a8a902b6cd"><a name="peb7dbbc28b7945c88776b0a8a902b6cd"></a><a name="peb7dbbc28b7945c88776b0a8a902b6cd"></a><b>Line Separator</b></span> in the advanced properties is invalid.</p>
</div></div>
</td>
</tr>
<tr id="r80723a2a59a347489bea670efc482187"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="acf5f6e3ed97447a9bf249a5a44f2ad7a"><a name="acf5f6e3ed97447a9bf249a5a44f2ad7a"></a><a name="acf5f6e3ed97447a9bf249a5a44f2ad7a"></a>Field Separator</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="a1cb922ecca8c43c8852f2e2a8a8b0700"><a name="a1cb922ecca8c43c8852f2e2a8a8b0700"></a><a name="a1cb922ecca8c43c8852f2e2a8a8b0700"></a>Identifier of each field end of final data</p>
<div class="note" id="nb69b6e9157014659a89572dd579ab97f"><a name="nb69b6e9157014659a89572dd579ab97f"></a><a name="nb69b6e9157014659a89572dd579ab97f"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="acb16f23283da4f40ba09d40fcbdb2372"><a name="acb16f23283da4f40ba09d40fcbdb2372"></a><a name="acb16f23283da4f40ba09d40fcbdb2372"></a>When HDFS serves as a destination link and <span class="parmname" id="p644a90d2123243e8a2054a072ff82098"><a name="p644a90d2123243e8a2054a072ff82098"></a><a name="p644a90d2123243e8a2054a072ff82098"></a><b>File format</b></span>&nbsp;is set to&nbsp;<span class="parmvalue" id="p44fce344771249819c3d1e9e0f1d7f99"><a name="p44fce344771249819c3d1e9e0f1d7f99"></a><a name="p44fce344771249819c3d1e9e0f1d7f99"></a><b>BINARY_FILE</b></span>, the value of&nbsp;<span class="parmname" id="p863375376ac4482eaea6cc70f4f7132b"><a name="p863375376ac4482eaea6cc70f4f7132b"></a><a name="p863375376ac4482eaea6cc70f4f7132b"></a><b>Field Separator</b></span> in the advanced properties is invalid.</p>
</div></div>
</td>
</tr>
</tbody>
</table>

## hive-connector<a name="s087b59d3886c4de5a33e4f6517c7b125"></a>

**Table  6**  Destination link properties of  **hive-connector**

<a name="ta42e0a680a52470797fa4edc758a526e"></a>
<table><thead align="left"><tr id="r25a37b9992af49338c58cef8649c9c65"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.3.1.1"><p id="ac00882261e154fb184c17e37997cd22d"><a name="ac00882261e154fb184c17e37997cd22d"></a><a name="ac00882261e154fb184c17e37997cd22d"></a><strong id="en-us_topic_0071084973_b816290111751"><a name="en-us_topic_0071084973_b816290111751"></a><a name="en-us_topic_0071084973_b816290111751"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="75%" id="mcps1.2.3.1.2"><p id="ad725514d833f44a2a240e8623c891703"><a name="ad725514d833f44a2a240e8623c891703"></a><a name="ad725514d833f44a2a240e8623c891703"></a><strong id="a09dc291dc09340cba7d75161c6151f86"><a name="a09dc291dc09340cba7d75161c6151f86"></a><a name="a09dc291dc09340cba7d75161c6151f86"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="rd5962953bc7143da968820d1f27c2c8b"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="a7d8bb75834bb4e7fad0bedaa40b5f493"><a name="a7d8bb75834bb4e7fad0bedaa40b5f493"></a><a name="a7d8bb75834bb4e7fad0bedaa40b5f493"></a>Database</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="a5dc8afda727c46bca8b34f0c408796eb"><a name="a5dc8afda727c46bca8b34f0c408796eb"></a><a name="a5dc8afda727c46bca8b34f0c408796eb"></a>Name of the Hive database storing final data. You can query and select it on the interface.</p>
</td>
</tr>
<tr id="rb1507d5f07ae4d858fdf59fdb28fc912"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="a0b73c087064440fb9b1cb2692ad50e70"><a name="a0b73c087064440fb9b1cb2692ad50e70"></a><a name="a0b73c087064440fb9b1cb2692ad50e70"></a>Table</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="a2f664480784a49a88a4f193edcf52069"><a name="a2f664480784a49a88a4f193edcf52069"></a><a name="a2f664480784a49a88a4f193edcf52069"></a>Name of the Hive table saving final data. You can query and select it on the interface.</p>
</td>
</tr>
</tbody>
</table>

## voltdb-connector<a name="sc61e82d5ba4540128849e035c7ee93ac"></a>

**Table  7**  Destination link properties of  **voltdb-connector**

<a name="tcc50b5e7921f461cb250c9c3ea4f182e"></a>
<table><thead align="left"><tr id="r7128af4d7e5b411b8d64e1a5f02d3973"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.3.1.1"><p id="a7be86a8494474df88076f42fa9e62a05"><a name="a7be86a8494474df88076f42fa9e62a05"></a><a name="a7be86a8494474df88076f42fa9e62a05"></a><strong id="a56b32fa9064d4301b8ce8871086411b3"><a name="a56b32fa9064d4301b8ce8871086411b3"></a><a name="a56b32fa9064d4301b8ce8871086411b3"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="75%" id="mcps1.2.3.1.2"><p id="a332b6dfb8d6240d4bb596d44c8f4f1df"><a name="a332b6dfb8d6240d4bb596d44c8f4f1df"></a><a name="a332b6dfb8d6240d4bb596d44c8f4f1df"></a><strong id="a8bec7d812f2d48a4975660e92f3e4d78"><a name="a8bec7d812f2d48a4975660e92f3e4d78"></a><a name="a8bec7d812f2d48a4975660e92f3e4d78"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r708a02634f7f438ea444a0397c202a96"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="a47d3a426e2c243a595685e47dc5b1437"><a name="a47d3a426e2c243a595685e47dc5b1437"></a><a name="a47d3a426e2c243a595685e47dc5b1437"></a>Table</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="a83f1623730b9418d94922026bc78e8a7"><a name="a83f1623730b9418d94922026bc78e8a7"></a><a name="a83f1623730b9418d94922026bc78e8a7"></a>Name of the memory database table storing final data. You can query and select it on the interface.</p>
</td>
</tr>
</tbody>
</table>


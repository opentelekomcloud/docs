# List of Open Source Component Ports<a name="EN-US_TOPIC_0125375380"></a>

**Table  1**  Common ports

<a name="t7e0c5eec375d408e82df6b22bbcfaaa6"></a>
<table><thead align="left"><tr id="ra548dd638e46430191ff1aabc11889b8"><th class="cellrowborder" valign="top" width="15%" id="mcps1.2.6.1.1"><p id="a267d8c118aaa4cf78c5f24c95fcde07a"><a name="a267d8c118aaa4cf78c5f24c95fcde07a"></a><a name="a267d8c118aaa4cf78c5f24c95fcde07a"></a>Sub-system Name</p>
</th>
<th class="cellrowborder" valign="top" width="20%" id="mcps1.2.6.1.2"><p id="af895fcf08df246fbadc11bb5b556d7f3"><a name="af895fcf08df246fbadc11bb5b556d7f3"></a><a name="af895fcf08df246fbadc11bb5b556d7f3"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.6.1.3"><p id="aa1151ac275114f4bbb1dd6368bf2e532"><a name="aa1151ac275114f4bbb1dd6368bf2e532"></a><a name="aa1151ac275114f4bbb1dd6368bf2e532"></a>Default Port (MRS 1.6.3 or Earlier)</p>
<p id="ae7459d83639c448792ee80e306e26100"><a name="ae7459d83639c448792ee80e306e26100"></a><a name="ae7459d83639c448792ee80e306e26100"></a></p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.2.6.1.4"><p id="a8f6bea200c494d9fb9ef5dfc25188dcc"><a name="a8f6bea200c494d9fb9ef5dfc25188dcc"></a><a name="a8f6bea200c494d9fb9ef5dfc25188dcc"></a>Default Port (MRS 1.7.2 or Later)</p>
<p id="aa50fa09ae06c4efc8b82cddc99779209"><a name="aa50fa09ae06c4efc8b82cddc99779209"></a><a name="aa50fa09ae06c4efc8b82cddc99779209"></a></p>
</th>
<th class="cellrowborder" valign="top" width="35%" id="mcps1.2.6.1.5"><p id="a1644323c101f4c4789f1f98fbbbbde31"><a name="a1644323c101f4c4789f1f98fbbbbde31"></a><a name="a1644323c101f4c4789f1f98fbbbbde31"></a>Port Description</p>
</th>
</tr>
</thead>
<tbody><tr id="r6cdab69d635b42b59281333e56623157"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.1 "><p id="a373b08e56bf543128eead25d209c6e4e"><a name="a373b08e56bf543128eead25d209c6e4e"></a><a name="a373b08e56bf543128eead25d209c6e4e"></a>HBase</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="ae967854c409f45d3ad3d2f72fc75edd5"><a name="ae967854c409f45d3ad3d2f72fc75edd5"></a><a name="ae967854c409f45d3ad3d2f72fc75edd5"></a>hbase.master.port</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="a857476ea254a480aabffe3671116c455"><a name="a857476ea254a480aabffe3671116c455"></a><a name="a857476ea254a480aabffe3671116c455"></a>21300</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.4 "><p id="a36c4a0060d9c49378d919b985d1112be"><a name="a36c4a0060d9c49378d919b985d1112be"></a><a name="a36c4a0060d9c49378d919b985d1112be"></a>16000</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.6.1.5 "><p id="acb30cea625764387b9f05f7314515cf1"><a name="acb30cea625764387b9f05f7314515cf1"></a><a name="acb30cea625764387b9f05f7314515cf1"></a>HMaster RPC port</p>
<p id="af360cec51d3b4328a9e20ff2c1646ee6"><a name="af360cec51d3b4328a9e20ff2c1646ee6"></a><a name="af360cec51d3b4328a9e20ff2c1646ee6"></a>Used for the HBase client to connect to HMaster.</p>
<div class="note" id="nfc71a6423f2e4a79a8398c1857196c15"><a name="nfc71a6423f2e4a79a8398c1857196c15"></a><a name="nfc71a6423f2e4a79a8398c1857196c15"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="a4708fd4eb21b4f3790f4bcfe4105ff8f"><a name="a4708fd4eb21b4f3790f4bcfe4105ff8f"></a><a name="a4708fd4eb21b4f3790f4bcfe4105ff8f"></a>The value range of the port is just a suggestion and is specified in the product. In addition, the value range of the port is not limited in code.</p>
</div></div>
<a name="u8bfe3f9cc65248f4873eda59bfb99100"></a><a name="u8bfe3f9cc65248f4873eda59bfb99100"></a><ul id="u8bfe3f9cc65248f4873eda59bfb99100"><li>Port enabled by default during the installation: Yes</li><li>Port enabled after security hardening: Yes</li></ul>
</td>
</tr>
<tr id="r8c81409eff63418389a729e9f3402785"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.1 "><p id="ac40bf061a9d34ab496d34160044803e7"><a name="ac40bf061a9d34ab496d34160044803e7"></a><a name="ac40bf061a9d34ab496d34160044803e7"></a>HBase</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="a1e43217b07ee4a7391b15925d3ed3d20"><a name="a1e43217b07ee4a7391b15925d3ed3d20"></a><a name="a1e43217b07ee4a7391b15925d3ed3d20"></a>hbase.master.info.port</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="ae6b80a06ab23472ba378464ec935e22c"><a name="ae6b80a06ab23472ba378464ec935e22c"></a><a name="ae6b80a06ab23472ba378464ec935e22c"></a>21301</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.4 "><p id="ade2b1821ce854417b5ea99eb95a754c0"><a name="ade2b1821ce854417b5ea99eb95a754c0"></a><a name="ade2b1821ce854417b5ea99eb95a754c0"></a>16010</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.6.1.5 "><p id="af77c28b5cd4f4b349331f32180476129"><a name="af77c28b5cd4f4b349331f32180476129"></a><a name="af77c28b5cd4f4b349331f32180476129"></a>HMaster HTTPS port</p>
<p id="afd879911c67b43f383fc8b729552d2e0"><a name="afd879911c67b43f383fc8b729552d2e0"></a><a name="afd879911c67b43f383fc8b729552d2e0"></a>Used for a remote Web client to connect to the HMaster UI.</p>
<div class="note" id="n173efabb972d42d68b6922690f71f8a6"><a name="n173efabb972d42d68b6922690f71f8a6"></a><a name="n173efabb972d42d68b6922690f71f8a6"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="a112ae9c2c8934ef1865bc55407fd4c9e"><a name="a112ae9c2c8934ef1865bc55407fd4c9e"></a><a name="a112ae9c2c8934ef1865bc55407fd4c9e"></a>The value range of the port is just a suggestion and is specified in the product. In addition, the value range of the port is not limited in code.</p>
</div></div>
<a name="ua0198b7e2ecd499a9236032085df331d"></a><a name="ua0198b7e2ecd499a9236032085df331d"></a><ul id="ua0198b7e2ecd499a9236032085df331d"><li>Port enabled by default during the installation: Yes</li><li>Port enabled after security hardening: Yes</li></ul>
</td>
</tr>
<tr id="raf5bd41b964e43d3b87d70208ec730ea"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.1 "><p id="ae2cbea5dec5443a593c75758c08ade63"><a name="ae2cbea5dec5443a593c75758c08ade63"></a><a name="ae2cbea5dec5443a593c75758c08ade63"></a>HBase</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="abe7ad8f3daa04ce3a3894aabbe9e8641"><a name="abe7ad8f3daa04ce3a3894aabbe9e8641"></a><a name="abe7ad8f3daa04ce3a3894aabbe9e8641"></a>hbase.regionserver.port</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="a9bb875c55424442fa0f72033ea06690b"><a name="a9bb875c55424442fa0f72033ea06690b"></a><a name="a9bb875c55424442fa0f72033ea06690b"></a>21302</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.4 "><p id="ad198601801434f78bdaea411d6186730"><a name="ad198601801434f78bdaea411d6186730"></a><a name="ad198601801434f78bdaea411d6186730"></a>16020</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.6.1.5 "><p id="a7a88cd367479431aba5b443a42fc7074"><a name="a7a88cd367479431aba5b443a42fc7074"></a><a name="a7a88cd367479431aba5b443a42fc7074"></a>RegoinServer RPC port</p>
<p id="a9d2e96d88e9d49efa4aafe866085a54b"><a name="a9d2e96d88e9d49efa4aafe866085a54b"></a><a name="a9d2e96d88e9d49efa4aafe866085a54b"></a>Used for the HBase client to connect to RegionServer.</p>
<div class="note" id="n8828ffe6b1994b6db8789ee3154f34a2"><a name="n8828ffe6b1994b6db8789ee3154f34a2"></a><a name="n8828ffe6b1994b6db8789ee3154f34a2"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="a03ee0d35fe324ed387ddad58f00a3525"><a name="a03ee0d35fe324ed387ddad58f00a3525"></a><a name="a03ee0d35fe324ed387ddad58f00a3525"></a>The value range of the port is just a suggestion and is specified in the product. In addition, the value range of the port is not limited in code.</p>
</div></div>
<a name="u879eb924452d482eba6415ea01fc5ed7"></a><a name="u879eb924452d482eba6415ea01fc5ed7"></a><ul id="u879eb924452d482eba6415ea01fc5ed7"><li>Port enabled by default during the installation: Yes</li><li>Port enabled after security hardening: Yes</li></ul>
</td>
</tr>
<tr id="r35a0942c9d3c4451bb6028940d7fb611"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.1 "><p id="aa5b9be5915fc43ec96d2dae1e42416df"><a name="aa5b9be5915fc43ec96d2dae1e42416df"></a><a name="aa5b9be5915fc43ec96d2dae1e42416df"></a>HBase</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="a6e08c118bc3240b5992eb04ffb679d3d"><a name="a6e08c118bc3240b5992eb04ffb679d3d"></a><a name="a6e08c118bc3240b5992eb04ffb679d3d"></a>hbase.regionserver.info.port</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="af0cad23ae38c4523a26c1f58de0186bd"><a name="af0cad23ae38c4523a26c1f58de0186bd"></a><a name="af0cad23ae38c4523a26c1f58de0186bd"></a>21303</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.4 "><p id="ade42c2c0396a4307bc8f4fba44caed7e"><a name="ade42c2c0396a4307bc8f4fba44caed7e"></a><a name="ade42c2c0396a4307bc8f4fba44caed7e"></a>16030</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.6.1.5 "><p id="add9e75bd2f414d8e85ff62bdac32909f"><a name="add9e75bd2f414d8e85ff62bdac32909f"></a><a name="add9e75bd2f414d8e85ff62bdac32909f"></a>RegionServer HTTPS port</p>
<p id="a27cdae90ae654d6c93f834e460958e13"><a name="a27cdae90ae654d6c93f834e460958e13"></a><a name="a27cdae90ae654d6c93f834e460958e13"></a>Used for a remote Web client to connect to the RegionServer UI.</p>
<div class="note" id="nbd0ae0a316564d08a3113e90189fa9d9"><a name="nbd0ae0a316564d08a3113e90189fa9d9"></a><a name="nbd0ae0a316564d08a3113e90189fa9d9"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="ac92a5dca972d482ab7c5765a493879c4"><a name="ac92a5dca972d482ab7c5765a493879c4"></a><a name="ac92a5dca972d482ab7c5765a493879c4"></a>The value range of the port is just a suggestion and is specified in the product. In addition, the value range of the port is not limited in code.</p>
</div></div>
<a name="u2f15e747bc5f4c2ba5ee86d977ea88ba"></a><a name="u2f15e747bc5f4c2ba5ee86d977ea88ba"></a><ul id="u2f15e747bc5f4c2ba5ee86d977ea88ba"><li>Port enabled by default during the installation: Yes</li><li>Port enabled after security hardening: Yes</li></ul>
</td>
</tr>
<tr id="r43641d429a5a4ee796cea96b58cd6bb0"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.1 "><p id="aed7aa0c0767f47a1a3f704c746e109bf"><a name="aed7aa0c0767f47a1a3f704c746e109bf"></a><a name="aed7aa0c0767f47a1a3f704c746e109bf"></a>HBase</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="a77faa724110b44d98ab2721fe3ac62d1"><a name="a77faa724110b44d98ab2721fe3ac62d1"></a><a name="a77faa724110b44d98ab2721fe3ac62d1"></a>hbase.thrift.info.port</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="acc3e90eef1664f62b84efa0d41f04b4b"><a name="acc3e90eef1664f62b84efa0d41f04b4b"></a><a name="acc3e90eef1664f62b84efa0d41f04b4b"></a>21304</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.4 "><p id="a152a500d07874bbb92602a91b926e2d8"><a name="a152a500d07874bbb92602a91b926e2d8"></a><a name="a152a500d07874bbb92602a91b926e2d8"></a>9095</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.6.1.5 "><p id="a0acc17914a414e04bd43fd4ef0e1f46a"><a name="a0acc17914a414e04bd43fd4ef0e1f46a"></a><a name="a0acc17914a414e04bd43fd4ef0e1f46a"></a>ThriftServer monitoring port of ThriftServer</p>
<p id="a1daae0b71ec742a18039af23877a45f3"><a name="a1daae0b71ec742a18039af23877a45f3"></a><a name="a1daae0b71ec742a18039af23877a45f3"></a>Used to monitor client connections.</p>
<div class="note" id="n1777a8b81b32415aa44cb5ae1095a8d4"><a name="n1777a8b81b32415aa44cb5ae1095a8d4"></a><a name="n1777a8b81b32415aa44cb5ae1095a8d4"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="ae31094d6cd964e0a9162a2d7923213f8"><a name="ae31094d6cd964e0a9162a2d7923213f8"></a><a name="ae31094d6cd964e0a9162a2d7923213f8"></a>The value range of the port is just a suggestion and is specified in the product. In addition, the value range of the port is not limited in code.</p>
</div></div>
<a name="u473f3b18badc437aaef3ce8232ca5cf2"></a><a name="u473f3b18badc437aaef3ce8232ca5cf2"></a><ul id="u473f3b18badc437aaef3ce8232ca5cf2"><li>Port enabled by default during the installation: Yes</li><li>Port enabled after security hardening: Yes</li></ul>
</td>
</tr>
<tr id="r0a9ebe9a164040d2ada3300e0c08f897"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.1 "><p id="aec63ecaa85f54e09adc7740c68650beb"><a name="aec63ecaa85f54e09adc7740c68650beb"></a><a name="aec63ecaa85f54e09adc7740c68650beb"></a>HBase</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="aad8a5ec47b3e4276b21c5866865892bc"><a name="aad8a5ec47b3e4276b21c5866865892bc"></a><a name="aad8a5ec47b3e4276b21c5866865892bc"></a>hbase.regionserver.thrift.port</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="a8aff01b3df3644dea45f96763ee7eccb"><a name="a8aff01b3df3644dea45f96763ee7eccb"></a><a name="a8aff01b3df3644dea45f96763ee7eccb"></a>21305</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.4 "><p id="aa700dd022b4b44e48ab186265e363d4e"><a name="aa700dd022b4b44e48ab186265e363d4e"></a><a name="aa700dd022b4b44e48ab186265e363d4e"></a>9090</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.6.1.5 "><p id="aa359f3b48f334ffaadddb6a4ec44f2d7"><a name="aa359f3b48f334ffaadddb6a4ec44f2d7"></a><a name="aa359f3b48f334ffaadddb6a4ec44f2d7"></a>ThriftServer monitoring port of RegionServer</p>
<p id="a914f19415d2e4775b152010ef2ebdf62"><a name="a914f19415d2e4775b152010ef2ebdf62"></a><a name="a914f19415d2e4775b152010ef2ebdf62"></a>Used to monitor connections between the client and RegionServer.</p>
<div class="note" id="n43140b117b1a42a5b9d06e62290b3c9e"><a name="n43140b117b1a42a5b9d06e62290b3c9e"></a><a name="n43140b117b1a42a5b9d06e62290b3c9e"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="a7b9acb570c89427f813d4be55e601e22"><a name="a7b9acb570c89427f813d4be55e601e22"></a><a name="a7b9acb570c89427f813d4be55e601e22"></a>The value range of the port is just a suggestion and is specified in the product. In addition, the value range of the port is not limited in code.</p>
</div></div>
<a name="u7dbc506f42e84afa99216d7bd1bc29aa"></a><a name="u7dbc506f42e84afa99216d7bd1bc29aa"></a><ul id="u7dbc506f42e84afa99216d7bd1bc29aa"><li>Port enabled by default during the installation: Yes</li><li>Port enabled after security hardening: Yes</li></ul>
</td>
</tr>
<tr id="r68faf41c7017469dabda8852cbb84225"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.1 "><p id="acef6837138144c83bc1b8bbd19ae91e7"><a name="acef6837138144c83bc1b8bbd19ae91e7"></a><a name="acef6837138144c83bc1b8bbd19ae91e7"></a>HBase</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="a9af3f3e73166419ea18a74938eb13223"><a name="a9af3f3e73166419ea18a74938eb13223"></a><a name="a9af3f3e73166419ea18a74938eb13223"></a>hbase.rest.info.port</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="a538ce28d60494d949bfcef00a3502c5e"><a name="a538ce28d60494d949bfcef00a3502c5e"></a><a name="a538ce28d60494d949bfcef00a3502c5e"></a>21308</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.4 "><p id="a78bdc8003d8a43148bef09392e12b440"><a name="a78bdc8003d8a43148bef09392e12b440"></a><a name="a78bdc8003d8a43148bef09392e12b440"></a>8085</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.6.1.5 "><p id="af25b426cfac948bc952e7186ec357040"><a name="af25b426cfac948bc952e7186ec357040"></a><a name="af25b426cfac948bc952e7186ec357040"></a>Port of the native web UI of RegionServer RESTServer</p>
</td>
</tr>
<tr id="r5a25758a679e490fbb6318e562858a19"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.1 "><p id="abeab7a6da226451fbfd34c6b461d638a"><a name="abeab7a6da226451fbfd34c6b461d638a"></a><a name="abeab7a6da226451fbfd34c6b461d638a"></a>HBase</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="af6f94576b8124fef93cd5ddc85640293"><a name="af6f94576b8124fef93cd5ddc85640293"></a><a name="af6f94576b8124fef93cd5ddc85640293"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="afde8821708a143c09fed9364b5cc0e28"><a name="afde8821708a143c09fed9364b5cc0e28"></a><a name="afde8821708a143c09fed9364b5cc0e28"></a>21309</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.4 "><p id="a0b6dabba4557485fa7331607691f11ba"><a name="a0b6dabba4557485fa7331607691f11ba"></a><a name="a0b6dabba4557485fa7331607691f11ba"></a>21309</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.6.1.5 "><p id="a4e02123402ce4091bd6b8e2dfc2928fd"><a name="a4e02123402ce4091bd6b8e2dfc2928fd"></a><a name="a4e02123402ce4091bd6b8e2dfc2928fd"></a>REST port of RegionServer RESTServer</p>
</td>
</tr>
<tr id="r97b2fa5c6b3e4ae48ac9c0b6c924d261"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.1 "><p id="aaa230ba2ba534b8081ce20eaf5beb7eb"><a name="aaa230ba2ba534b8081ce20eaf5beb7eb"></a><a name="aaa230ba2ba534b8081ce20eaf5beb7eb"></a>HDFS</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="a1187e9a8090c41e79252b1c58a69f9ec"><a name="a1187e9a8090c41e79252b1c58a69f9ec"></a><a name="a1187e9a8090c41e79252b1c58a69f9ec"></a>dfs.namenode.rpc.port</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="a9cc1c1becf5f45f5870f4513a02826b4"><a name="a9cc1c1becf5f45f5870f4513a02826b4"></a><a name="a9cc1c1becf5f45f5870f4513a02826b4"></a>25000</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.4 "><p id="a76bcb28f615b45bebbeb9f354b04b9f4"><a name="a76bcb28f615b45bebbeb9f354b04b9f4"></a><a name="a76bcb28f615b45bebbeb9f354b04b9f4"></a>9820</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.6.1.5 "><p id="ab77ae0a4681c42c58ba428aa7a1c2d7d"><a name="ab77ae0a4681c42c58ba428aa7a1c2d7d"></a><a name="ab77ae0a4681c42c58ba428aa7a1c2d7d"></a>NameNode RPC port</p>
<p id="a0b36d01bd7d94ad1a82f6ec28642d3ba"><a name="a0b36d01bd7d94ad1a82f6ec28642d3ba"></a><a name="a0b36d01bd7d94ad1a82f6ec28642d3ba"></a>Used for:</p>
<p id="a94bc323562b54c43b0a63cb3f3532575"><a name="a94bc323562b54c43b0a63cb3f3532575"></a><a name="a94bc323562b54c43b0a63cb3f3532575"></a>1. Communications between the HDFS client and NameNode</p>
<p id="a9b25cd1add2a47bba96a9ee912b9bdf5"><a name="a9b25cd1add2a47bba96a9ee912b9bdf5"></a><a name="a9b25cd1add2a47bba96a9ee912b9bdf5"></a>2. Connection between DataNode and NameNode</p>
<div class="note" id="nacd8126b3bae4cbeb651e12987618517"><a name="nacd8126b3bae4cbeb651e12987618517"></a><a name="nacd8126b3bae4cbeb651e12987618517"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="a3009691728b04965a0a881f1c9067de2"><a name="a3009691728b04965a0a881f1c9067de2"></a><a name="a3009691728b04965a0a881f1c9067de2"></a>The value range of the port is just a suggestion and is specified in the product. In addition, the value range of the port is not limited in code.</p>
</div></div>
<a name="u55e9d6dd3fd44416af46beef86b5b365"></a><a name="u55e9d6dd3fd44416af46beef86b5b365"></a><ul id="u55e9d6dd3fd44416af46beef86b5b365"><li>Port enabled by default during the installation: Yes</li><li>Port enabled after security hardening: Yes</li></ul>
</td>
</tr>
<tr id="rdc93e31cfebc4f8aae475064ee58ec6e"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.1 "><p id="aa4b16d030e72422f968aadd3e4ef2f4d"><a name="aa4b16d030e72422f968aadd3e4ef2f4d"></a><a name="aa4b16d030e72422f968aadd3e4ef2f4d"></a>HDFS</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="a9cd63b21ee4b4e388fbba0f3f16484f6"><a name="a9cd63b21ee4b4e388fbba0f3f16484f6"></a><a name="a9cd63b21ee4b4e388fbba0f3f16484f6"></a>dfs.namenode.http.port</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="aa3236004c8204e418874ab379b59571c"><a name="aa3236004c8204e418874ab379b59571c"></a><a name="aa3236004c8204e418874ab379b59571c"></a>25002</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.4 "><p id="ad61d525126f848a39403a49b87beb1cd"><a name="ad61d525126f848a39403a49b87beb1cd"></a><a name="ad61d525126f848a39403a49b87beb1cd"></a>9870</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.6.1.5 "><p id="a8cfa1b79487e4f5ab9324d9bc869a64d"><a name="a8cfa1b79487e4f5ab9324d9bc869a64d"></a><a name="a8cfa1b79487e4f5ab9324d9bc869a64d"></a>HDFS HTTP port (NameNode)</p>
<p id="a669c15c1a99f4d4cb742d3cb85d6f5fb"><a name="a669c15c1a99f4d4cb742d3cb85d6f5fb"></a><a name="a669c15c1a99f4d4cb742d3cb85d6f5fb"></a>Used for:</p>
<p id="a7b6cb10198504e668e13ccef1c088c87"><a name="a7b6cb10198504e668e13ccef1c088c87"></a><a name="a7b6cb10198504e668e13ccef1c088c87"></a>1. Point-to-point NameNode checkpoint operations</p>
<p id="aa25f54eb99f242028eeb9d20c21f1eb3"><a name="aa25f54eb99f242028eeb9d20c21f1eb3"></a><a name="aa25f54eb99f242028eeb9d20c21f1eb3"></a>2. Connection between the remote Web client and the NameNode UI</p>
<div class="note" id="nc9252ed3532b4f44bc21119613823a42"><a name="nc9252ed3532b4f44bc21119613823a42"></a><a name="nc9252ed3532b4f44bc21119613823a42"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="abff274a30b5849238601f0e871f662a0"><a name="abff274a30b5849238601f0e871f662a0"></a><a name="abff274a30b5849238601f0e871f662a0"></a>The value range of the port is just a suggestion and is specified in the product. In addition, the value range of the port is not limited in code.</p>
</div></div>
<a name="u2bd55be8c98c4feeacd60b9189e1ed16"></a><a name="u2bd55be8c98c4feeacd60b9189e1ed16"></a><ul id="u2bd55be8c98c4feeacd60b9189e1ed16"><li>Port enabled by default during the installation: Yes</li><li>Port enabled after security hardening: Yes</li></ul>
</td>
</tr>
<tr id="rcc370463401744f1b97d57672e9c0739"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.1 "><p id="a833870ad12d1441bbec41267e5aba2bb"><a name="a833870ad12d1441bbec41267e5aba2bb"></a><a name="a833870ad12d1441bbec41267e5aba2bb"></a>HDFS</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="af989f16a4f5341aebe43121b4446299e"><a name="af989f16a4f5341aebe43121b4446299e"></a><a name="af989f16a4f5341aebe43121b4446299e"></a>dfs.namenode.https.port</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="a8370053a59ae4b85a00d4a6499fcbb00"><a name="a8370053a59ae4b85a00d4a6499fcbb00"></a><a name="a8370053a59ae4b85a00d4a6499fcbb00"></a>25003</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.4 "><p id="a9a97c3db6d604fad8f795ddfa6dcf872"><a name="a9a97c3db6d604fad8f795ddfa6dcf872"></a><a name="a9a97c3db6d604fad8f795ddfa6dcf872"></a>9871</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.6.1.5 "><p id="a07cd67986cd2444e9bf6b995de273c4b"><a name="a07cd67986cd2444e9bf6b995de273c4b"></a><a name="a07cd67986cd2444e9bf6b995de273c4b"></a>HDFS HTTPS port (NameNode)</p>
<p id="a7991997fe8524634bbe7a9c394d54371"><a name="a7991997fe8524634bbe7a9c394d54371"></a><a name="a7991997fe8524634bbe7a9c394d54371"></a>Used for:</p>
<p id="a5cd8764986af4a4ba48cf229f54974fa"><a name="a5cd8764986af4a4ba48cf229f54974fa"></a><a name="a5cd8764986af4a4ba48cf229f54974fa"></a>1. Point-to-point NameNode checkpoint operations</p>
<p id="ad28c4afabee94fdf9ea2fbb9dd55603c"><a name="ad28c4afabee94fdf9ea2fbb9dd55603c"></a><a name="ad28c4afabee94fdf9ea2fbb9dd55603c"></a>2. Connection between the remote Web client and the NameNode UI</p>
<div class="note" id="nf49e14f66efa4380b5812b601ad09619"><a name="nf49e14f66efa4380b5812b601ad09619"></a><a name="nf49e14f66efa4380b5812b601ad09619"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="a31f9207d9e1347a895f91b26382e679d"><a name="a31f9207d9e1347a895f91b26382e679d"></a><a name="a31f9207d9e1347a895f91b26382e679d"></a>The value range of the port is just a suggestion and is specified in the product. In addition, the value range of the port is not limited in code.</p>
</div></div>
<a name="u1ba48fb410534731b2026daff2b82a7f"></a><a name="u1ba48fb410534731b2026daff2b82a7f"></a><ul id="u1ba48fb410534731b2026daff2b82a7f"><li>Port enabled by default during the installation: Yes</li><li>Port enabled after security hardening: Yes</li></ul>
</td>
</tr>
<tr id="r0f539345ed91477fa65f811fd81733d5"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.1 "><p id="ae4f3bdcb3be34a14804de4c9e8a86c48"><a name="ae4f3bdcb3be34a14804de4c9e8a86c48"></a><a name="ae4f3bdcb3be34a14804de4c9e8a86c48"></a>HDFS</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="a4747468b5b034f6da644a1c5111d82b9"><a name="a4747468b5b034f6da644a1c5111d82b9"></a><a name="a4747468b5b034f6da644a1c5111d82b9"></a>dfs.datanode.ipc.port</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="a48e8f8a2443a41a59819bda8fcc53886"><a name="a48e8f8a2443a41a59819bda8fcc53886"></a><a name="a48e8f8a2443a41a59819bda8fcc53886"></a>25008</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.4 "><p id="aa8d59f56209140899d4c0e5db44499d5"><a name="aa8d59f56209140899d4c0e5db44499d5"></a><a name="aa8d59f56209140899d4c0e5db44499d5"></a>9867</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.6.1.5 "><p id="ae4980caacd0d4293bdf87f59e99fb512"><a name="ae4980caacd0d4293bdf87f59e99fb512"></a><a name="ae4980caacd0d4293bdf87f59e99fb512"></a>DataNode IPC server port</p>
<p id="aa6b2c7b266284b8083be6d56f1def881"><a name="aa6b2c7b266284b8083be6d56f1def881"></a><a name="aa6b2c7b266284b8083be6d56f1def881"></a>Used for the client to connect to DataNode for performing RPC operations.</p>
<div class="note" id="n3a11a17869e84685ad523630e74a84c0"><a name="n3a11a17869e84685ad523630e74a84c0"></a><a name="n3a11a17869e84685ad523630e74a84c0"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="a56b68283f31a48dcb56949413971cb20"><a name="a56b68283f31a48dcb56949413971cb20"></a><a name="a56b68283f31a48dcb56949413971cb20"></a>The value range of the port is just a suggestion and is specified in the product. In addition, the value range of the port is not limited in code.</p>
</div></div>
<a name="u0ae66060b94c405e96ccca5cc1faac6d"></a><a name="u0ae66060b94c405e96ccca5cc1faac6d"></a><ul id="u0ae66060b94c405e96ccca5cc1faac6d"><li>Port enabled by default during the installation: Yes</li><li>Port enabled after security hardening: Yes</li></ul>
</td>
</tr>
<tr id="r012fb33befd742d0ab3676991a36b146"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.1 "><p id="a8f7e123c3f5b4d0bac693b35c5b135d4"><a name="a8f7e123c3f5b4d0bac693b35c5b135d4"></a><a name="a8f7e123c3f5b4d0bac693b35c5b135d4"></a>HDFS</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="ae97b6eb9c05d4ac3984c6c202845f933"><a name="ae97b6eb9c05d4ac3984c6c202845f933"></a><a name="ae97b6eb9c05d4ac3984c6c202845f933"></a>dfs.datanode.port</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="ae84d5979ac8945488edf1eabb450d56a"><a name="ae84d5979ac8945488edf1eabb450d56a"></a><a name="ae84d5979ac8945488edf1eabb450d56a"></a>25009</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.4 "><p id="a0bc73f3768ee496aa3f19254ea6453b1"><a name="a0bc73f3768ee496aa3f19254ea6453b1"></a><a name="a0bc73f3768ee496aa3f19254ea6453b1"></a>9866</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.6.1.5 "><p id="a35b5af4319ce4fa9b32fb8859bd7956a"><a name="a35b5af4319ce4fa9b32fb8859bd7956a"></a><a name="a35b5af4319ce4fa9b32fb8859bd7956a"></a>DataNode data transmission port</p>
<p id="a28601e8304b74d46afbecf78d86d8251"><a name="a28601e8304b74d46afbecf78d86d8251"></a><a name="a28601e8304b74d46afbecf78d86d8251"></a>Used for:</p>
<p id="ab65d9f09e70d4749ae5a0b3625ea6c69"><a name="ab65d9f09e70d4749ae5a0b3625ea6c69"></a><a name="ab65d9f09e70d4749ae5a0b3625ea6c69"></a>1. Communications between the HDFS client and DataNode for data transmission</p>
<p id="a8f6572cb7f5348c69de4724353f1f738"><a name="a8f6572cb7f5348c69de4724353f1f738"></a><a name="a8f6572cb7f5348c69de4724353f1f738"></a>2. Point-to-point data transmission on DataNode</p>
<div class="note" id="n915ae0529b5646768fed33dbf56fb160"><a name="n915ae0529b5646768fed33dbf56fb160"></a><a name="n915ae0529b5646768fed33dbf56fb160"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="a764d8b8c16e9437581086e7f6c881ec0"><a name="a764d8b8c16e9437581086e7f6c881ec0"></a><a name="a764d8b8c16e9437581086e7f6c881ec0"></a>The value range of the port is just a suggestion and is specified in the product. In addition, the value range of the port is not limited in code.</p>
</div></div>
<a name="ue01104231a1040c3859f2e57106c485f"></a><a name="ue01104231a1040c3859f2e57106c485f"></a><ul id="ue01104231a1040c3859f2e57106c485f"><li>Port enabled by default during the installation: Yes</li><li>Port enabled after security hardening: Yes</li></ul>
</td>
</tr>
<tr id="r5e28f55070e444739c206f6d4738700a"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.1 "><p id="a26bf991271444ce8a8c852305c88ca8d"><a name="a26bf991271444ce8a8c852305c88ca8d"></a><a name="a26bf991271444ce8a8c852305c88ca8d"></a>HDFS</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="a0efa007b18004e069b0dd178909d5cfc"><a name="a0efa007b18004e069b0dd178909d5cfc"></a><a name="a0efa007b18004e069b0dd178909d5cfc"></a>dfs.datanode.http.port</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="a33e36ed673004580b00ef96a433a3f85"><a name="a33e36ed673004580b00ef96a433a3f85"></a><a name="a33e36ed673004580b00ef96a433a3f85"></a>25010</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.4 "><p id="a48d52a083214474c8e62c13e3b78e44f"><a name="a48d52a083214474c8e62c13e3b78e44f"></a><a name="a48d52a083214474c8e62c13e3b78e44f"></a>9864</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.6.1.5 "><p id="af8f5fa7ee64246899dd10c0c899578ce"><a name="af8f5fa7ee64246899dd10c0c899578ce"></a><a name="af8f5fa7ee64246899dd10c0c899578ce"></a>DataNode HTTP port</p>
<p id="ac214c5e460ca49f295d6f09bfb77cad3"><a name="ac214c5e460ca49f295d6f09bfb77cad3"></a><a name="ac214c5e460ca49f295d6f09bfb77cad3"></a>Used for a remote Web client to connect to the DataNode UI in security mode.</p>
<div class="note" id="ncd8e29d2d58b4dd19f999f08f3dbe5ab"><a name="ncd8e29d2d58b4dd19f999f08f3dbe5ab"></a><a name="ncd8e29d2d58b4dd19f999f08f3dbe5ab"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="ad5a6f63946354fedb99506d2dbe74522"><a name="ad5a6f63946354fedb99506d2dbe74522"></a><a name="ad5a6f63946354fedb99506d2dbe74522"></a>The value range of the port is just a suggestion and is specified in the product. In addition, the value range of the port is not limited in code.</p>
</div></div>
<a name="ue10360b0a70f4a48a879b8a84a08fea8"></a><a name="ue10360b0a70f4a48a879b8a84a08fea8"></a><ul id="ue10360b0a70f4a48a879b8a84a08fea8"><li>Port enabled by default during the installation: Yes</li><li>Port enabled after security hardening: Yes</li></ul>
</td>
</tr>
<tr id="rbfada51f641c4b55bece9bb325b7dff4"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.1 "><p id="a2fb3ad80e7b74143b2769bdfef0997d1"><a name="a2fb3ad80e7b74143b2769bdfef0997d1"></a><a name="a2fb3ad80e7b74143b2769bdfef0997d1"></a>HDFS</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="a7d8b28db504048bdba56c467e2a44289"><a name="a7d8b28db504048bdba56c467e2a44289"></a><a name="a7d8b28db504048bdba56c467e2a44289"></a>dfs.datanode.https.port</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="af447185276714628881dafa78cac59cb"><a name="af447185276714628881dafa78cac59cb"></a><a name="af447185276714628881dafa78cac59cb"></a>25011</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.4 "><p id="ab17abcc06fe64c42aefeb06445365aac"><a name="ab17abcc06fe64c42aefeb06445365aac"></a><a name="ab17abcc06fe64c42aefeb06445365aac"></a>9865</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.6.1.5 "><p id="a156df626811b44e9a903ee704102759d"><a name="a156df626811b44e9a903ee704102759d"></a><a name="a156df626811b44e9a903ee704102759d"></a>DataNode HTTPS port</p>
<p id="aecfd9be432e14020a788127541908d3b"><a name="aecfd9be432e14020a788127541908d3b"></a><a name="aecfd9be432e14020a788127541908d3b"></a>Used for a remote Web client to connect to the DataNode UI in security mode.</p>
<div class="note" id="n45f091b47fc5449ca29d1477a0757a6b"><a name="n45f091b47fc5449ca29d1477a0757a6b"></a><a name="n45f091b47fc5449ca29d1477a0757a6b"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="a5342e8565bbe411a9ce460667ec45abe"><a name="a5342e8565bbe411a9ce460667ec45abe"></a><a name="a5342e8565bbe411a9ce460667ec45abe"></a>The value range of the port is just a suggestion and is specified in the product. In addition, the value range of the port is not limited in code.</p>
</div></div>
<a name="udf6d67e4e46c4c81a844a9b2d7ed8136"></a><a name="udf6d67e4e46c4c81a844a9b2d7ed8136"></a><ul id="udf6d67e4e46c4c81a844a9b2d7ed8136"><li>Port enabled by default during the installation: Yes</li><li>Port enabled after security hardening: Yes</li></ul>
</td>
</tr>
<tr id="rd4c5970999744ee9bc16a0b9cdf06e44"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.1 "><p id="a9a82b75edeb34943a2d74bf05258ae3b"><a name="a9a82b75edeb34943a2d74bf05258ae3b"></a><a name="a9a82b75edeb34943a2d74bf05258ae3b"></a>HDFS</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="a9d1268182db248df81ae1d692386a38f"><a name="a9d1268182db248df81ae1d692386a38f"></a><a name="a9d1268182db248df81ae1d692386a38f"></a>dfs.journalnode.rpc.port</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="ac866b372aaa9494190384323d64cbaf7"><a name="ac866b372aaa9494190384323d64cbaf7"></a><a name="ac866b372aaa9494190384323d64cbaf7"></a>25012</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.4 "><p id="a027101a258fc4592b3deac522183c3eb"><a name="a027101a258fc4592b3deac522183c3eb"></a><a name="a027101a258fc4592b3deac522183c3eb"></a>8485</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.6.1.5 "><p id="a1be7189df38a4e7c83c9134e2d3db226"><a name="a1be7189df38a4e7c83c9134e2d3db226"></a><a name="a1be7189df38a4e7c83c9134e2d3db226"></a>JournalNode RPC port</p>
<p id="ad7aa084a70e649ec94496da1fa4c9683"><a name="ad7aa084a70e649ec94496da1fa4c9683"></a><a name="ad7aa084a70e649ec94496da1fa4c9683"></a>Used for client communications for accessing various information.</p>
<div class="note" id="n59041e753c694ad9bc465c0ffbc6c228"><a name="n59041e753c694ad9bc465c0ffbc6c228"></a><a name="n59041e753c694ad9bc465c0ffbc6c228"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="a1bc81f144a034ed1add08079c2fcb652"><a name="a1bc81f144a034ed1add08079c2fcb652"></a><a name="a1bc81f144a034ed1add08079c2fcb652"></a>The value range of the port is just a suggestion and is specified in the product. In addition, the value range of the port is not limited in code.</p>
</div></div>
<a name="ue1135fb513d249548c711042d0f1724d"></a><a name="ue1135fb513d249548c711042d0f1724d"></a><ul id="ue1135fb513d249548c711042d0f1724d"><li>Port enabled by default during the installation: Yes</li><li>Port enabled after security hardening: Yes</li></ul>
</td>
</tr>
<tr id="red9ca82aa46f4df4b96545f7782bff5d"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.1 "><p id="a6faf285df596471cbec3cfebc295551c"><a name="a6faf285df596471cbec3cfebc295551c"></a><a name="a6faf285df596471cbec3cfebc295551c"></a>HDFS</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="add2daa68fa834f6693fc36fed646a107"><a name="add2daa68fa834f6693fc36fed646a107"></a><a name="add2daa68fa834f6693fc36fed646a107"></a>dfs.journalnode.http.port</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="a1fac490619f447be84a238875cbe00fd"><a name="a1fac490619f447be84a238875cbe00fd"></a><a name="a1fac490619f447be84a238875cbe00fd"></a>25013</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.4 "><p id="a55322e316d9f49c58eb0a24c5314c026"><a name="a55322e316d9f49c58eb0a24c5314c026"></a><a name="a55322e316d9f49c58eb0a24c5314c026"></a>8480</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.6.1.5 "><p id="a4588d56f3e80476e94f173cf32f96709"><a name="a4588d56f3e80476e94f173cf32f96709"></a><a name="a4588d56f3e80476e94f173cf32f96709"></a>JournalNode HTTP port</p>
<p id="ac4c332b295ee40699d0657d98cc4590d"><a name="ac4c332b295ee40699d0657d98cc4590d"></a><a name="ac4c332b295ee40699d0657d98cc4590d"></a>Used for a remote Web client to connect to JournalNode in security mode.</p>
<div class="note" id="n17e5295a545e422fb3a0728147919171"><a name="n17e5295a545e422fb3a0728147919171"></a><a name="n17e5295a545e422fb3a0728147919171"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="ad05458da6a7045b192c02c60c74f2287"><a name="ad05458da6a7045b192c02c60c74f2287"></a><a name="ad05458da6a7045b192c02c60c74f2287"></a>The value range of the port is just a suggestion and is specified in the product. In addition, the value range of the port is not limited in code.</p>
</div></div>
<a name="uf79bc193f4ed4f41832b959dac596748"></a><a name="uf79bc193f4ed4f41832b959dac596748"></a><ul id="uf79bc193f4ed4f41832b959dac596748"><li>Port enabled by default during the installation: Yes</li><li>Port enabled after security hardening: Yes</li></ul>
</td>
</tr>
<tr id="r022e0729493946d7b47561655527eb9d"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.1 "><p id="af6da93c62f184b499d7d7c41f1a5f5c3"><a name="af6da93c62f184b499d7d7c41f1a5f5c3"></a><a name="af6da93c62f184b499d7d7c41f1a5f5c3"></a>HDFS</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="ad6ab3c04b0b444dfac1c21e3df8bff42"><a name="ad6ab3c04b0b444dfac1c21e3df8bff42"></a><a name="ad6ab3c04b0b444dfac1c21e3df8bff42"></a>dfs.journalnode.https.port</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="a5681f6129a28474483c102403c113b82"><a name="a5681f6129a28474483c102403c113b82"></a><a name="a5681f6129a28474483c102403c113b82"></a>25014</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.4 "><p id="ae95fb02050654c3a8fa4bae3fbff203c"><a name="ae95fb02050654c3a8fa4bae3fbff203c"></a><a name="ae95fb02050654c3a8fa4bae3fbff203c"></a>8481</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.6.1.5 "><p id="a6ae003367fb240459752ee6aae437f10"><a name="a6ae003367fb240459752ee6aae437f10"></a><a name="a6ae003367fb240459752ee6aae437f10"></a>JournalNode HTTPS port</p>
<p id="a5faa46e3832e4fdeb11eacb9ae6c74d1"><a name="a5faa46e3832e4fdeb11eacb9ae6c74d1"></a><a name="a5faa46e3832e4fdeb11eacb9ae6c74d1"></a>Used for a remote Web client to connect to JournalNode in security mode.</p>
<div class="note" id="n2cc1f3ddf4a74197af243bc16310219b"><a name="n2cc1f3ddf4a74197af243bc16310219b"></a><a name="n2cc1f3ddf4a74197af243bc16310219b"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="ab920f03d461c4e539e05ee52c469650c"><a name="ab920f03d461c4e539e05ee52c469650c"></a><a name="ab920f03d461c4e539e05ee52c469650c"></a>The value range of the port is just a suggestion and is specified in the product. In addition, the value range of the port is not limited in code.</p>
</div></div>
<a name="u56be0738fa354dda9ec302e49f852b44"></a><a name="u56be0738fa354dda9ec302e49f852b44"></a><ul id="u56be0738fa354dda9ec302e49f852b44"><li>Port enabled by default during the installation: Yes</li><li>Port enabled after security hardening: Yes</li></ul>
</td>
</tr>
<tr id="r5995a5a59ca742efac6351685fdb608a"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.1 "><p id="a8b5a53b3f01a47f8bbf146bb2a7b5887"><a name="a8b5a53b3f01a47f8bbf146bb2a7b5887"></a><a name="a8b5a53b3f01a47f8bbf146bb2a7b5887"></a>HDFS</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="ae844bc9132244e38afbc506257caf348"><a name="ae844bc9132244e38afbc506257caf348"></a><a name="ae844bc9132244e38afbc506257caf348"></a>HTTPFS_HTTP_PORT</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="ae5497abbfb9847469546900f823abe5a"><a name="ae5497abbfb9847469546900f823abe5a"></a><a name="ae5497abbfb9847469546900f823abe5a"></a>25018</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.4 "><p id="a2798b3c9426f4a9184ed599a5c4e60b3"><a name="a2798b3c9426f4a9184ed599a5c4e60b3"></a><a name="a2798b3c9426f4a9184ed599a5c4e60b3"></a>14000</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.6.1.5 "><p id="a7d05dc40608f45d9962f17d79c733d20"><a name="a7d05dc40608f45d9962f17d79c733d20"></a><a name="a7d05dc40608f45d9962f17d79c733d20"></a>HttpFS HTTP server monitoring port</p>
<p id="a5a186d48e32e48caa4893a0be4195524"><a name="a5a186d48e32e48caa4893a0be4195524"></a><a name="a5a186d48e32e48caa4893a0be4195524"></a>Used for a remote REST API to connect to HttpFS.</p>
<div class="note" id="n5c47ec45c4bb4094b92c79d201bae69c"><a name="n5c47ec45c4bb4094b92c79d201bae69c"></a><a name="n5c47ec45c4bb4094b92c79d201bae69c"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="af5d46db3691b4896a02d61f170c5c4f5"><a name="af5d46db3691b4896a02d61f170c5c4f5"></a><a name="af5d46db3691b4896a02d61f170c5c4f5"></a>The value range of the port is just a suggestion and is specified in the product. In addition, the value range of the port is not limited in code.</p>
</div></div>
<a name="u38a2ae240a9d45e097937fd2d8735149"></a><a name="u38a2ae240a9d45e097937fd2d8735149"></a><ul id="u38a2ae240a9d45e097937fd2d8735149"><li>Port enabled by default during the installation: Yes</li><li>Port enabled after security hardening: Yes</li></ul>
</td>
</tr>
<tr id="re542a6d1fd07499394e13b9dd52038ea"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.1 "><p id="a9910945abfcb4fba9a4256a2fe479d81"><a name="a9910945abfcb4fba9a4256a2fe479d81"></a><a name="a9910945abfcb4fba9a4256a2fe479d81"></a>HDFS</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="ad2cd7cc19865495382a1426e77211b4c"><a name="ad2cd7cc19865495382a1426e77211b4c"></a><a name="ad2cd7cc19865495382a1426e77211b4c"></a>HTTPFS_ADMIN_PORT</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="a7bbd0de0d2f34537b62c72a1cea39c1b"><a name="a7bbd0de0d2f34537b62c72a1cea39c1b"></a><a name="a7bbd0de0d2f34537b62c72a1cea39c1b"></a>25020</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.4 "><p id="a253ef119d1cf4e43a42891dc1db08f23"><a name="a253ef119d1cf4e43a42891dc1db08f23"></a><a name="a253ef119d1cf4e43a42891dc1db08f23"></a>14001</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.6.1.5 "><p id="a71caf075822a49dfb979b31afbb6a2cc"><a name="a71caf075822a49dfb979b31afbb6a2cc"></a><a name="a71caf075822a49dfb979b31afbb6a2cc"></a>HttpFS ADMIN server monitoring port</p>
<p id="a40c96fafd31945c39c5b3245ec807e24"><a name="a40c96fafd31945c39c5b3245ec807e24"></a><a name="a40c96fafd31945c39c5b3245ec807e24"></a>Used for a remote REST API to connect to HttpFS.</p>
<div class="note" id="n57f4b4a52d13460bbf4b42b6296b9353"><a name="n57f4b4a52d13460bbf4b42b6296b9353"></a><a name="n57f4b4a52d13460bbf4b42b6296b9353"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="ac78d7d2260854343b677882551833d26"><a name="ac78d7d2260854343b677882551833d26"></a><a name="ac78d7d2260854343b677882551833d26"></a>The value range of the port is just a suggestion and is specified in the product. In addition, the value range of the port is not limited in code.</p>
</div></div>
<a name="ue25a1879897a48e782af7a8f8943e8cd"></a><a name="ue25a1879897a48e782af7a8f8943e8cd"></a><ul id="ue25a1879897a48e782af7a8f8943e8cd"><li>Port enabled by default during the installation: Yes</li><li>Port enabled after security hardening: Yes</li></ul>
</td>
</tr>
<tr id="red9ede190b944e6485b0969d2b124de5"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.1 "><p id="ad185f9b8ded64a7d9b4a96c13da43dbd"><a name="ad185f9b8ded64a7d9b4a96c13da43dbd"></a><a name="ad185f9b8ded64a7d9b4a96c13da43dbd"></a>HDFS</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="a9542172f9ba44616bf66142a5d1357a9"><a name="a9542172f9ba44616bf66142a5d1357a9"></a><a name="a9542172f9ba44616bf66142a5d1357a9"></a>dfs.datanode.http.address.ext</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="af30d8b1fdc43415c9002830e9a0dae54"><a name="af30d8b1fdc43415c9002830e9a0dae54"></a><a name="af30d8b1fdc43415c9002830e9a0dae54"></a>25016</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.4 "><p id="a440ceb50a76e4e3e84e8c92d35f2fb09"><a name="a440ceb50a76e4e3e84e8c92d35f2fb09"></a><a name="a440ceb50a76e4e3e84e8c92d35f2fb09"></a>25016</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.6.1.5 "><p id="a04edb2e474874db181752c8256071660"><a name="a04edb2e474874db181752c8256071660"></a><a name="a04edb2e474874db181752c8256071660"></a>DataNode HTTP address extension port</p>
<p id="a15ece206fa424831a8497d98e79855a3"><a name="a15ece206fa424831a8497d98e79855a3"></a><a name="a15ece206fa424831a8497d98e79855a3"></a>Used for a remote Web client to connect to the DataNode UI in security mode.</p>
<div class="note" id="n1a4bcfe19a53451f91797580251f4661"><a name="n1a4bcfe19a53451f91797580251f4661"></a><a name="n1a4bcfe19a53451f91797580251f4661"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="a7051c869c9054780bbb84afe1b35f322"><a name="a7051c869c9054780bbb84afe1b35f322"></a><a name="a7051c869c9054780bbb84afe1b35f322"></a>The value range of the port is just a suggestion and is specified in the product. In addition, the value range of the port is not limited in code.</p>
</div></div>
<a name="ue94bb983c9d24cf7aa9a2eea80c1a600"></a><a name="ue94bb983c9d24cf7aa9a2eea80c1a600"></a><ul id="ue94bb983c9d24cf7aa9a2eea80c1a600"><li>Port enabled by default during the installation: Yes</li><li>Port enabled after security hardening: Yes</li></ul>
</td>
</tr>
<tr id="rf840171f238d4f5d8cc83ded4f1edf4e"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.1 "><p id="a1131d525d1f94558855dfbf9d3874612"><a name="a1131d525d1f94558855dfbf9d3874612"></a><a name="a1131d525d1f94558855dfbf9d3874612"></a>HDFS</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="a7ee38068fbd1443f9b5373c483787e76"><a name="a7ee38068fbd1443f9b5373c483787e76"></a><a name="a7ee38068fbd1443f9b5373c483787e76"></a>HTTPFS_HTTPS_PORT</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="a0a3a0ad74bfd48c599d165893108a3b3"><a name="a0a3a0ad74bfd48c599d165893108a3b3"></a><a name="a0a3a0ad74bfd48c599d165893108a3b3"></a>25019</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.4 "><p id="aa08995218fdb43a9addd447efa9bc27d"><a name="aa08995218fdb43a9addd447efa9bc27d"></a><a name="aa08995218fdb43a9addd447efa9bc27d"></a>25019</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.6.1.5 "><p id="ad42ff521109d43c2a7bd06c6cee61426"><a name="ad42ff521109d43c2a7bd06c6cee61426"></a><a name="ad42ff521109d43c2a7bd06c6cee61426"></a>HttpFS HTTPS server monitoring port</p>
<p id="a893c2335c554499e8957435b692434ed"><a name="a893c2335c554499e8957435b692434ed"></a><a name="a893c2335c554499e8957435b692434ed"></a>Used for a remote REST API to connect to HttpFS.</p>
<div class="note" id="n424bbf0fa0254fe092754a49bc902918"><a name="n424bbf0fa0254fe092754a49bc902918"></a><a name="n424bbf0fa0254fe092754a49bc902918"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="a3369a7bae532434b846307bc914d4531"><a name="a3369a7bae532434b846307bc914d4531"></a><a name="a3369a7bae532434b846307bc914d4531"></a>The value range of the port is just a suggestion and is specified in the product. In addition, the value range of the port is not limited in code.</p>
</div></div>
<a name="u83e382b947704ec991cbd407ff7dbc7f"></a><a name="u83e382b947704ec991cbd407ff7dbc7f"></a><ul id="u83e382b947704ec991cbd407ff7dbc7f"><li>Port enabled by default during the installation: Yes</li><li>Port enabled after security hardening: Yes</li></ul>
</td>
</tr>
<tr id="r14dd95b2742741ee9b2bf5284859e3fe"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.1 "><p id="a1b7f994671ee467e96f2002cc640dc31"><a name="a1b7f994671ee467e96f2002cc640dc31"></a><a name="a1b7f994671ee467e96f2002cc640dc31"></a>Hive</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="a00ad5d2a203f42b7bd9e16f16df58d73"><a name="a00ad5d2a203f42b7bd9e16f16df58d73"></a><a name="a00ad5d2a203f42b7bd9e16f16df58d73"></a>templeton.port</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="a44541626b76847038ddb3aa0ae11f6cf"><a name="a44541626b76847038ddb3aa0ae11f6cf"></a><a name="a44541626b76847038ddb3aa0ae11f6cf"></a>21055</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.4 "><p id="af1e38114b49c4c439f938f166d3d18f5"><a name="af1e38114b49c4c439f938f166d3d18f5"></a><a name="af1e38114b49c4c439f938f166d3d18f5"></a>50111</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.6.1.5 "><p id="a074a77100c9341f3aa1063ca11e1f004"><a name="a074a77100c9341f3aa1063ca11e1f004"></a><a name="a074a77100c9341f3aa1063ca11e1f004"></a>Port for WebHCat to provide REST services</p>
<p id="a0ba65cd6a112451cb77f8b7eeb52612d"><a name="a0ba65cd6a112451cb77f8b7eeb52612d"></a><a name="a0ba65cd6a112451cb77f8b7eeb52612d"></a>Used for communications between WebHCat clients and WebHCat servers.</p>
<a name="u996d96a1bae14321b5149b7c783fefd7"></a><a name="u996d96a1bae14321b5149b7c783fefd7"></a><ul id="u996d96a1bae14321b5149b7c783fefd7"><li>Port enabled by default during the installation: Yes</li><li>Port enabled after security hardening: Yes</li></ul>
</td>
</tr>
<tr id="rf6c3ea542b0a4f1381cb09a2c1a174b8"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.1 "><p id="a988722f778a34f2482a1335cd646ccda"><a name="a988722f778a34f2482a1335cd646ccda"></a><a name="a988722f778a34f2482a1335cd646ccda"></a>Hive</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="af42fef130f6440e9b34214a92bd94cb6"><a name="af42fef130f6440e9b34214a92bd94cb6"></a><a name="af42fef130f6440e9b34214a92bd94cb6"></a>templeton.port</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="aea35405a648045d8bfbbe599c1b00233"><a name="aea35405a648045d8bfbbe599c1b00233"></a><a name="aea35405a648045d8bfbbe599c1b00233"></a>21066</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.4 "><p id="a04f618071e4f4a629dccbe21a6285eb0"><a name="a04f618071e4f4a629dccbe21a6285eb0"></a><a name="a04f618071e4f4a629dccbe21a6285eb0"></a>10000</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.6.1.5 "><p id="a379150bca631456d9625e362afc953ab"><a name="a379150bca631456d9625e362afc953ab"></a><a name="a379150bca631456d9625e362afc953ab"></a>Port for HiveServer to provide Thrift services</p>
<p id="ab587f0035d544718af1696d7c58b33c0"><a name="ab587f0035d544718af1696d7c58b33c0"></a><a name="ab587f0035d544718af1696d7c58b33c0"></a>Used for communications between HiveServer clients and HiveServer.</p>
<a name="u3fdba31605e84c0d8c6aa67d80efcc33"></a><a name="u3fdba31605e84c0d8c6aa67d80efcc33"></a><ul id="u3fdba31605e84c0d8c6aa67d80efcc33"><li>Port enabled by default during the installation: Yes</li><li>Port enabled after security hardening: Yes</li></ul>
</td>
</tr>
<tr id="ra6f9de02a9494bc8a9ce14672b48839a"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.1 "><p id="aa3881660f2614cf4aa571db0610b08a6"><a name="aa3881660f2614cf4aa571db0610b08a6"></a><a name="aa3881660f2614cf4aa571db0610b08a6"></a>Hive</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="a48f8c6a557584449ad26bc32c6c24a5d"><a name="a48f8c6a557584449ad26bc32c6c24a5d"></a><a name="a48f8c6a557584449ad26bc32c6c24a5d"></a>templeton.port</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="adf53f9faa30a44dfba4458b127602f48"><a name="adf53f9faa30a44dfba4458b127602f48"></a><a name="adf53f9faa30a44dfba4458b127602f48"></a>21088</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.4 "><p id="a3f0caf921eff4e16a41a4a9d5e8fde49"><a name="a3f0caf921eff4e16a41a4a9d5e8fde49"></a><a name="a3f0caf921eff4e16a41a4a9d5e8fde49"></a>9083</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.6.1.5 "><p id="a94d755450d41488f9ff19add2d716db8"><a name="a94d755450d41488f9ff19add2d716db8"></a><a name="a94d755450d41488f9ff19add2d716db8"></a>Port for MetaStore to provide Thrift services</p>
<p id="a5466284f38334b68a50d52313da83e62"><a name="a5466284f38334b68a50d52313da83e62"></a><a name="a5466284f38334b68a50d52313da83e62"></a>Used for communications between the MetaStore client and MetaStore, that is, communications between HiveServer and MetaStore.</p>
<a name="u8e4e3d4ccedd4dc28d31b80cbcfeceae"></a><a name="u8e4e3d4ccedd4dc28d31b80cbcfeceae"></a><ul id="u8e4e3d4ccedd4dc28d31b80cbcfeceae"><li>Port enabled by default during the installation: Yes</li><li>Port enabled after security hardening: Yes</li></ul>
</td>
</tr>
<tr id="rdebcd0e9039d4f2f9c5fd98b72cd9900"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.1 "><p id="ab78a965ebdcc4602b3c0dd3719d3afb7"><a name="ab78a965ebdcc4602b3c0dd3719d3afb7"></a><a name="ab78a965ebdcc4602b3c0dd3719d3afb7"></a>Hue</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="a44189aea245e4932ad3810611d20d713"><a name="a44189aea245e4932ad3810611d20d713"></a><a name="a44189aea245e4932ad3810611d20d713"></a>HTTP_PORT</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="a7966119d6d5441d385b0ca1a431b5f49"><a name="a7966119d6d5441d385b0ca1a431b5f49"></a><a name="a7966119d6d5441d385b0ca1a431b5f49"></a>21200</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.4 "><p id="aaa711d1413af4cdca2281e0cdfed8b15"><a name="aaa711d1413af4cdca2281e0cdfed8b15"></a><a name="aaa711d1413af4cdca2281e0cdfed8b15"></a>8888</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.6.1.5 "><p id="af54e9a930e7a4020916fe15ffba80e70"><a name="af54e9a930e7a4020916fe15ffba80e70"></a><a name="af54e9a930e7a4020916fe15ffba80e70"></a>Port for Hue to provide HTTPS services</p>
<p id="a4e9a60c65452468d933eeb2c9e299e82"><a name="a4e9a60c65452468d933eeb2c9e299e82"></a><a name="a4e9a60c65452468d933eeb2c9e299e82"></a>Used to provide web services using HTTPS. This parameter can be modified.</p>
<a name="u20473508e8dc43f28de1544c14b0c823"></a><a name="u20473508e8dc43f28de1544c14b0c823"></a><ul id="u20473508e8dc43f28de1544c14b0c823"><li>Port enabled by default during the installation: Yes</li><li>Port enabled after security hardening: Yes</li></ul>
</td>
</tr>
<tr id="r57317666c1d947de8f6fa2d5d51c4f4d"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.1 "><p id="a06a9956a4d62435d83e83d7b0f433a49"><a name="a06a9956a4d62435d83e83d7b0f433a49"></a><a name="a06a9956a4d62435d83e83d7b0f433a49"></a>Kafka</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="a2fb498891a8d4a5d957b6b5b239ce52d"><a name="a2fb498891a8d4a5d957b6b5b239ce52d"></a><a name="a2fb498891a8d4a5d957b6b5b239ce52d"></a>port</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="aee94448588904e718af0cf2b522ec19a"><a name="aee94448588904e718af0cf2b522ec19a"></a><a name="aee94448588904e718af0cf2b522ec19a"></a>21005</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.4 "><p id="a160161503a094431816aaf3c71591803"><a name="a160161503a094431816aaf3c71591803"></a><a name="a160161503a094431816aaf3c71591803"></a>9092</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.6.1.5 "><p id="aada49421314c4c3aadc1aaee943d3aed"><a name="aada49421314c4c3aadc1aaee943d3aed"></a><a name="aada49421314c4c3aadc1aaee943d3aed"></a>Port for Broker to receive and obtain data</p>
</td>
</tr>
<tr id="rf22a477cb8ce4081abb06df68d35f3b3"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.1 "><p id="a1f980321e9464dd18d01d9096982a264"><a name="a1f980321e9464dd18d01d9096982a264"></a><a name="a1f980321e9464dd18d01d9096982a264"></a>Kafka</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="a925b3931225f4a968b5428dc2c96b32b"><a name="a925b3931225f4a968b5428dc2c96b32b"></a><a name="a925b3931225f4a968b5428dc2c96b32b"></a>ssl.port</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="a04cdf1cebf434b858555107eddc4a3bb"><a name="a04cdf1cebf434b858555107eddc4a3bb"></a><a name="a04cdf1cebf434b858555107eddc4a3bb"></a>21008</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.4 "><p id="a5174a6bcd4354cbd93d0c4dd2aaa0d4d"><a name="a5174a6bcd4354cbd93d0c4dd2aaa0d4d"></a><a name="a5174a6bcd4354cbd93d0c4dd2aaa0d4d"></a>9093</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.6.1.5 "><p id="af1adbd09faef48e28dfc1134afcbca87"><a name="af1adbd09faef48e28dfc1134afcbca87"></a><a name="af1adbd09faef48e28dfc1134afcbca87"></a>SSL port for Broker to receive and obtain data</p>
</td>
</tr>
<tr id="r89d0c8fb31cb4d3e92783b06eee1d2c5"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.1 "><p id="a2fe85e1efef743b7836b38ad63ed2f4d"><a name="a2fe85e1efef743b7836b38ad63ed2f4d"></a><a name="a2fe85e1efef743b7836b38ad63ed2f4d"></a>Kafka</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="a9031c9f2b4f04e079c2bfc89c6cefead"><a name="a9031c9f2b4f04e079c2bfc89c6cefead"></a><a name="a9031c9f2b4f04e079c2bfc89c6cefead"></a>sasl.port</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="a30af0b8de51c4626ba26e72752c24b78"><a name="a30af0b8de51c4626ba26e72752c24b78"></a><a name="a30af0b8de51c4626ba26e72752c24b78"></a>21007</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.4 "><p id="a5eeed25da43e4d7ebe847fd853fcb518"><a name="a5eeed25da43e4d7ebe847fd853fcb518"></a><a name="a5eeed25da43e4d7ebe847fd853fcb518"></a>21007</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.6.1.5 "><p id="a22f8fdc4f4f8482bafd718b32888eea0"><a name="a22f8fdc4f4f8482bafd718b32888eea0"></a><a name="a22f8fdc4f4f8482bafd718b32888eea0"></a>Port for Broker to provide SASL security authentication and security Kafka services</p>
</td>
</tr>
<tr id="r5783ebce12ad484786d7fce3f355b082"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.1 "><p id="af2a62b4d8cf744afb9a32291f2978a85"><a name="af2a62b4d8cf744afb9a32291f2978a85"></a><a name="af2a62b4d8cf744afb9a32291f2978a85"></a>Kafka</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="ac6f88db25ed0432f878e5d1db084737f"><a name="ac6f88db25ed0432f878e5d1db084737f"></a><a name="ac6f88db25ed0432f878e5d1db084737f"></a>sasl-ssl.port</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="a1e81b82be5f14d3cb3a111a98c9a42c9"><a name="a1e81b82be5f14d3cb3a111a98c9a42c9"></a><a name="a1e81b82be5f14d3cb3a111a98c9a42c9"></a>21009</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.4 "><p id="abff5d11eb9804e1883aa75d6d9561548"><a name="abff5d11eb9804e1883aa75d6d9561548"></a><a name="abff5d11eb9804e1883aa75d6d9561548"></a>21009</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.6.1.5 "><p id="a1689c06b0b6b410f988bc02647c7b2fc"><a name="a1689c06b0b6b410f988bc02647c7b2fc"></a><a name="a1689c06b0b6b410f988bc02647c7b2fc"></a>Port for Broker to provide SASL security authentication and SSL communications as well as security authentication and communication encryption services</p>
</td>
</tr>
<tr id="r4d01a7e6a51141e3a43a23ee73c46131"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.1 "><p id="a347f30565f4b46399af4faa7a91446a5"><a name="a347f30565f4b46399af4faa7a91446a5"></a><a name="a347f30565f4b46399af4faa7a91446a5"></a>Loader</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="a52e0b4106b4d494aae76429e95317c5a"><a name="a52e0b4106b4d494aae76429e95317c5a"></a><a name="a52e0b4106b4d494aae76429e95317c5a"></a>LOADER_HTTPS_PORT</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="a99a5a848112945f99b423b418bee6148"><a name="a99a5a848112945f99b423b418bee6148"></a><a name="a99a5a848112945f99b423b418bee6148"></a>21351</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.4 "><p id="a6cf32c1658954dcab45e7a414d8fbaa1"><a name="a6cf32c1658954dcab45e7a414d8fbaa1"></a><a name="a6cf32c1658954dcab45e7a414d8fbaa1"></a>21351</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.6.1.5 "><p id="a9edd407517854452aafb4f42739a84ee"><a name="a9edd407517854452aafb4f42739a84ee"></a><a name="a9edd407517854452aafb4f42739a84ee"></a>Port for providing REST APIs for Loader job configuration and running</p>
<a name="u45c6c25702394a4994b42943f2e5b7da"></a><a name="u45c6c25702394a4994b42943f2e5b7da"></a><ul id="u45c6c25702394a4994b42943f2e5b7da"><li>Port enabled by default during the installation: Yes</li><li>Port enabled after security hardening: Yes</li></ul>
</td>
</tr>
<tr id="r5c417d7e9a6f4d488d8ff676d168e727"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.1 "><p id="ab1ad2c41719043d7bde0166a4114578d"><a name="ab1ad2c41719043d7bde0166a4114578d"></a><a name="ab1ad2c41719043d7bde0166a4114578d"></a>Manager</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="aaa56e5d741c04874a4ba3c26401a3ded"><a name="aaa56e5d741c04874a4ba3c26401a3ded"></a><a name="aaa56e5d741c04874a4ba3c26401a3ded"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="a10cb12f6a2454b388379003f80267074"><a name="a10cb12f6a2454b388379003f80267074"></a><a name="a10cb12f6a2454b388379003f80267074"></a>8080</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.4 "><p id="a0b82d07631ec471dbe46e22d70d9a8cb"><a name="a0b82d07631ec471dbe46e22d70d9a8cb"></a><a name="a0b82d07631ec471dbe46e22d70d9a8cb"></a>8080</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.6.1.5 "><p id="afe4ac4d3a5504cbe99cadde481ebc12f"><a name="afe4ac4d3a5504cbe99cadde481ebc12f"></a><a name="afe4ac4d3a5504cbe99cadde481ebc12f"></a>Port provided by WebService for user access</p>
<p id="ab83a11acb8334dc4bf32823a7de4e13b"><a name="ab83a11acb8334dc4bf32823a7de4e13b"></a><a name="ab83a11acb8334dc4bf32823a7de4e13b"></a>Used to access the Web UI.</p>
<a name="u538b4d52163640b589e96303ddcddd13"></a><a name="u538b4d52163640b589e96303ddcddd13"></a><ul id="u538b4d52163640b589e96303ddcddd13"><li>Port enabled by default during the installation: Yes</li><li>Port enabled after security hardening: Yes</li></ul>
</td>
</tr>
<tr id="r3e2c8c8233df488d9376af29a30f26ee"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.1 "><p id="abec15be296704606988f384c3b7acf23"><a name="abec15be296704606988f384c3b7acf23"></a><a name="abec15be296704606988f384c3b7acf23"></a>Manager</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="a9db8df673c8345399a8fab2f4a17d8fc"><a name="a9db8df673c8345399a8fab2f4a17d8fc"></a><a name="a9db8df673c8345399a8fab2f4a17d8fc"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="a9bc025da7afc4395aacbdc510b78d0a9"><a name="a9bc025da7afc4395aacbdc510b78d0a9"></a><a name="a9bc025da7afc4395aacbdc510b78d0a9"></a>28443</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.4 "><p id="a12fcd644055f4ea1a2d4f8b40f6e726f"><a name="a12fcd644055f4ea1a2d4f8b40f6e726f"></a><a name="a12fcd644055f4ea1a2d4f8b40f6e726f"></a>28443</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.6.1.5 "><p id="a8d66a63eb0944ebfbd3f9bff3e6bb85b"><a name="a8d66a63eb0944ebfbd3f9bff3e6bb85b"></a><a name="a8d66a63eb0944ebfbd3f9bff3e6bb85b"></a>Port provided by WebService for user access</p>
<p id="a9f2c9ee2cc7a4f399637680c8f9e7908"><a name="a9f2c9ee2cc7a4f399637680c8f9e7908"></a><a name="a9f2c9ee2cc7a4f399637680c8f9e7908"></a>Used to access the Web UI.</p>
<a name="u52363ead31a74340bc4c74724c8ea464"></a><a name="u52363ead31a74340bc4c74724c8ea464"></a><ul id="u52363ead31a74340bc4c74724c8ea464"><li>Port enabled by default during the installation: Yes</li><li>Port enabled after security hardening: Yes</li></ul>
</td>
</tr>
<tr id="r1ff560e3cd8d4044b05526e88edb6468"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.1 "><p id="af3df083a74904760861b99621e83e24d"><a name="af3df083a74904760861b99621e83e24d"></a><a name="af3df083a74904760861b99621e83e24d"></a>MapReduce</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="a2e04ce00f47440c1857c05bec6228070"><a name="a2e04ce00f47440c1857c05bec6228070"></a><a name="a2e04ce00f47440c1857c05bec6228070"></a>mapreduce.jobhistory.webapp.port</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="aa9042395b730499d9a1a1cc177435f2c"><a name="aa9042395b730499d9a1a1cc177435f2c"></a><a name="aa9042395b730499d9a1a1cc177435f2c"></a>26012</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.4 "><p id="a1cb0c543d80747178c987e3bb2c71cfb"><a name="a1cb0c543d80747178c987e3bb2c71cfb"></a><a name="a1cb0c543d80747178c987e3bb2c71cfb"></a>19888</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.6.1.5 "><p id="af3abce14222547378a9ba50655d380b0"><a name="af3abce14222547378a9ba50655d380b0"></a><a name="af3abce14222547378a9ba50655d380b0"></a>Web HTTP port of the JobHistory server</p>
<p id="af91d395181df4a1da0c36828207e8fb3"><a name="af91d395181df4a1da0c36828207e8fb3"></a><a name="af91d395181df4a1da0c36828207e8fb3"></a>Used to view the web page of the JobHistory server.</p>
<div class="note" id="ncedfb9e87edb46b587068ad09c5a53fa"><a name="ncedfb9e87edb46b587068ad09c5a53fa"></a><a name="ncedfb9e87edb46b587068ad09c5a53fa"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="a94bf57bf86184d8aba83ab30dd156e30"><a name="a94bf57bf86184d8aba83ab30dd156e30"></a><a name="a94bf57bf86184d8aba83ab30dd156e30"></a>The value range of the port is just a suggestion and is specified in the product. In addition, the value range of the port is not limited in code.</p>
</div></div>
<a name="u719aa160b20d47d9b88b49bd0974254f"></a><a name="u719aa160b20d47d9b88b49bd0974254f"></a><ul id="u719aa160b20d47d9b88b49bd0974254f"><li>Port enabled by default during the installation: Yes</li><li>Port enabled after security hardening: Yes</li></ul>
</td>
</tr>
<tr id="r1c2d6d7e5be0470d8feba16ab45d325a"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.1 "><p id="a3f7118cdc19f4d2db0ae5f52b22f9b1e"><a name="a3f7118cdc19f4d2db0ae5f52b22f9b1e"></a><a name="a3f7118cdc19f4d2db0ae5f52b22f9b1e"></a>MapReduce</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="a4a49ea5749f34168be3b39c2961ee515"><a name="a4a49ea5749f34168be3b39c2961ee515"></a><a name="a4a49ea5749f34168be3b39c2961ee515"></a>mapreduce.jobhistory.port</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="afa3aadb4d1bf464e8351f1378190730f"><a name="afa3aadb4d1bf464e8351f1378190730f"></a><a name="afa3aadb4d1bf464e8351f1378190730f"></a>26013</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.4 "><p id="a87b22ff7054c4aad878b57ebbbcc7bb6"><a name="a87b22ff7054c4aad878b57ebbbcc7bb6"></a><a name="a87b22ff7054c4aad878b57ebbbcc7bb6"></a>10020</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.6.1.5 "><p id="a15b9af66bbb24997abf9a9032335686c"><a name="a15b9af66bbb24997abf9a9032335686c"></a><a name="a15b9af66bbb24997abf9a9032335686c"></a>JobHistory server port</p>
<p id="a28d160bba014430abe32b035e249d12b"><a name="a28d160bba014430abe32b035e249d12b"></a><a name="a28d160bba014430abe32b035e249d12b"></a>Used for:</p>
<p id="ae86cff00516649bca2e29b059a7ecdbe"><a name="ae86cff00516649bca2e29b059a7ecdbe"></a><a name="ae86cff00516649bca2e29b059a7ecdbe"></a>1. The MapReduce client restores task data.</p>
<p id="adb2375d58f7940dea4e641adc39e5677"><a name="adb2375d58f7940dea4e641adc39e5677"></a><a name="adb2375d58f7940dea4e641adc39e5677"></a>2. The Job client obtains task reports.</p>
<div class="note" id="n220beb0cfd4144efafbb7d9b0d5a6d9c"><a name="n220beb0cfd4144efafbb7d9b0d5a6d9c"></a><a name="n220beb0cfd4144efafbb7d9b0d5a6d9c"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="a5797a569de6e42da81fd0bef665f9956"><a name="a5797a569de6e42da81fd0bef665f9956"></a><a name="a5797a569de6e42da81fd0bef665f9956"></a>The value range of the port is just a suggestion and is specified in the product. In addition, the value range of the port is not limited in code.</p>
</div></div>
<a name="u4fc28ce0f93948a18a8e50603a08bfab"></a><a name="u4fc28ce0f93948a18a8e50603a08bfab"></a><ul id="u4fc28ce0f93948a18a8e50603a08bfab"><li>Port enabled by default during the installation: Yes</li><li>Port enabled after security hardening: Yes</li></ul>
</td>
</tr>
<tr id="r1ab96dd6d5294186906ce769becb8a94"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.1 "><p id="ab03e9240c984446f96ec0df9e0efba24"><a name="ab03e9240c984446f96ec0df9e0efba24"></a><a name="ab03e9240c984446f96ec0df9e0efba24"></a>MapReduce</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="ac6654e0f43ba41c2b08e1316045c8778"><a name="ac6654e0f43ba41c2b08e1316045c8778"></a><a name="ac6654e0f43ba41c2b08e1316045c8778"></a>mapreduce.jobhistory.webapp.https.port</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="a3bef2589ec9c40eeb4d5928002175612"><a name="a3bef2589ec9c40eeb4d5928002175612"></a><a name="a3bef2589ec9c40eeb4d5928002175612"></a>26014</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.4 "><p id="a42a5be2941204f8b967f500ab2d08a3b"><a name="a42a5be2941204f8b967f500ab2d08a3b"></a><a name="a42a5be2941204f8b967f500ab2d08a3b"></a>19890</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.6.1.5 "><p id="a6a4d6991730f446785fc0baaf42d2a8a"><a name="a6a4d6991730f446785fc0baaf42d2a8a"></a><a name="a6a4d6991730f446785fc0baaf42d2a8a"></a>Web HTTPS port of the JobHistory server</p>
<p id="a3b8d63990a4e474796a4c1c50c3f9e6c"><a name="a3b8d63990a4e474796a4c1c50c3f9e6c"></a><a name="a3b8d63990a4e474796a4c1c50c3f9e6c"></a>Used to view the web page of the JobHistory server.</p>
<div class="note" id="n044b01d10d834c9495bbc8286168ab77"><a name="n044b01d10d834c9495bbc8286168ab77"></a><a name="n044b01d10d834c9495bbc8286168ab77"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="af0359dae061f415d8d32043a8d591dd8"><a name="af0359dae061f415d8d32043a8d591dd8"></a><a name="af0359dae061f415d8d32043a8d591dd8"></a>The value range of the port is just a suggestion and is specified in the product. In addition, the value range of the port is not limited in code.</p>
</div></div>
<a name="udcd0eb10b4384e29975197c077aed455"></a><a name="udcd0eb10b4384e29975197c077aed455"></a><ul id="udcd0eb10b4384e29975197c077aed455"><li>Port enabled by default during the installation: Yes</li><li>Port enabled after security hardening: Yes</li></ul>
</td>
</tr>
<tr id="r8fc3580d6f1a4e9e8bde5e589ff241b9"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.1 "><p id="a86a2298cfa6c421985a0044507370368"><a name="a86a2298cfa6c421985a0044507370368"></a><a name="a86a2298cfa6c421985a0044507370368"></a>Spark2.1.0</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="a04bd0daae2dc4894ac714e228a92c7cd"><a name="a04bd0daae2dc4894ac714e228a92c7cd"></a><a name="a04bd0daae2dc4894ac714e228a92c7cd"></a>hive.server2.thrift.port</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="a952478f2fe864bb298f28209ecfe19fc"><a name="a952478f2fe864bb298f28209ecfe19fc"></a><a name="a952478f2fe864bb298f28209ecfe19fc"></a>22550</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.4 "><p id="a49b73f807a9a443891f35d378124d5c4"><a name="a49b73f807a9a443891f35d378124d5c4"></a><a name="a49b73f807a9a443891f35d378124d5c4"></a>22550</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.6.1.5 "><p id="ab08858fd8f8e43e59adb88f9998ca6af"><a name="ab08858fd8f8e43e59adb88f9998ca6af"></a><a name="ab08858fd8f8e43e59adb88f9998ca6af"></a>JDBC Thrift port</p>
<p id="ac098c3606cf643f9847a4a1cac18f3e2"><a name="ac098c3606cf643f9847a4a1cac18f3e2"></a><a name="ac098c3606cf643f9847a4a1cac18f3e2"></a>Used for socket communications between Spark2.1.0 CLI/JDBC and the Spark2.1.0 CLI/JDBC server.</p>
<div class="note" id="n1ed9e79f242741a4be996aa5ae9bae8e"><a name="n1ed9e79f242741a4be996aa5ae9bae8e"></a><a name="n1ed9e79f242741a4be996aa5ae9bae8e"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="a8c55d28f5d634a2799898c9fcdf4d221"><a name="a8c55d28f5d634a2799898c9fcdf4d221"></a><a name="a8c55d28f5d634a2799898c9fcdf4d221"></a>If <strong id="b18207182212526"><a name="b18207182212526"></a><a name="b18207182212526"></a>hive.server2.thrift.port</strong> is occupied, a port occupation exception will be thrown.</p>
</div></div>
<a name="uf59cee59dd3d4845bc67bfe7e6a3c0e9"></a><a name="uf59cee59dd3d4845bc67bfe7e6a3c0e9"></a><ul id="uf59cee59dd3d4845bc67bfe7e6a3c0e9"><li>Port enabled by default during the installation: Yes</li><li>Port enabled after security hardening: Yes</li></ul>
</td>
</tr>
<tr id="rfb62fbac54f84a9582c48d068df88f40"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.1 "><p id="a384b4a46007f4b13b8dc925b57b5a973"><a name="a384b4a46007f4b13b8dc925b57b5a973"></a><a name="a384b4a46007f4b13b8dc925b57b5a973"></a>Spark2.1.0</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="ac7e7bb5e5ef64d27930fcbb30b7c2b8f"><a name="ac7e7bb5e5ef64d27930fcbb30b7c2b8f"></a><a name="ac7e7bb5e5ef64d27930fcbb30b7c2b8f"></a>spark.ui.port</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="a310bc17b6f5a488c8af0496a14706c3f"><a name="a310bc17b6f5a488c8af0496a14706c3f"></a><a name="a310bc17b6f5a488c8af0496a14706c3f"></a>22950</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.4 "><p id="a24172c03e3e342c09807de8a2677b8b8"><a name="a24172c03e3e342c09807de8a2677b8b8"></a><a name="a24172c03e3e342c09807de8a2677b8b8"></a>4040</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.6.1.5 "><p id="a695fd0bd073b4dd7a97e909830748cd9"><a name="a695fd0bd073b4dd7a97e909830748cd9"></a><a name="a695fd0bd073b4dd7a97e909830748cd9"></a>JDBC Web UI port</p>
<p id="a8dc68fdb8fc54c31a55cf397c68b5eba"><a name="a8dc68fdb8fc54c31a55cf397c68b5eba"></a><a name="a8dc68fdb8fc54c31a55cf397c68b5eba"></a>Used for HTTPS/HTTP communications between Web requests and the JDBC Server Web UI server</p>
<div class="note" id="ne26744b6738541f2b2dde0984fe61bd6"><a name="ne26744b6738541f2b2dde0984fe61bd6"></a><a name="ne26744b6738541f2b2dde0984fe61bd6"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="a958465680ee84e5aaafe74db0969a74a"><a name="a958465680ee84e5aaafe74db0969a74a"></a><a name="a958465680ee84e5aaafe74db0969a74a"></a>The system obtains the port according to the parameter setting and checks its validity. If the port is invalid, the system increases the port number by 1 each time for a maximum of 16 times until a valid port is obtained. The number of retries can be configured using <strong id="aab6c506673ee4775b30bdeba65ef14b9"><a name="aab6c506673ee4775b30bdeba65ef14b9"></a><a name="aab6c506673ee4775b30bdeba65ef14b9"></a>spark.port.maxRetries</strong>.</p>
</div></div>
<a name="u12635084b2e043af99a22c0211afae42"></a><a name="u12635084b2e043af99a22c0211afae42"></a><ul id="u12635084b2e043af99a22c0211afae42"><li>Port enabled by default during the installation: Yes</li><li>Port enabled after security hardening: Yes</li></ul>
</td>
</tr>
<tr id="r58fcb01e258d47c2a019b6fa3ef13a26"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.1 "><p id="ae6d2bd7a08ad4f47a56254123f9fe0ad"><a name="ae6d2bd7a08ad4f47a56254123f9fe0ad"></a><a name="ae6d2bd7a08ad4f47a56254123f9fe0ad"></a>Spark2.1.0</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="a4363545073e7488ea6c98d7a2eac6a3e"><a name="a4363545073e7488ea6c98d7a2eac6a3e"></a><a name="a4363545073e7488ea6c98d7a2eac6a3e"></a>spark.history.ui.port</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="a48e629bb32464f43b1fa16b48baf9974"><a name="a48e629bb32464f43b1fa16b48baf9974"></a><a name="a48e629bb32464f43b1fa16b48baf9974"></a>22500</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.4 "><p id="af76ca63843374e80a9e02d3337700c73"><a name="af76ca63843374e80a9e02d3337700c73"></a><a name="af76ca63843374e80a9e02d3337700c73"></a>18080</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.6.1.5 "><p id="abd85086687504320b5c7274a38f44f78"><a name="abd85086687504320b5c7274a38f44f78"></a><a name="abd85086687504320b5c7274a38f44f78"></a>JobHistory Web UI port</p>
<p id="aefd89318232e45ed8f3bee72f81f45c0"><a name="aefd89318232e45ed8f3bee72f81f45c0"></a><a name="aefd89318232e45ed8f3bee72f81f45c0"></a>Used for HTTPS/HTTP communications between Web requests and the Spark2.1.0 History Server server.</p>
<div class="note" id="nd4da776097834ce8a12233bbdd62a714"><a name="nd4da776097834ce8a12233bbdd62a714"></a><a name="nd4da776097834ce8a12233bbdd62a714"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="a9f5a70ea05824f149b53ed66548f9c36"><a name="a9f5a70ea05824f149b53ed66548f9c36"></a><a name="a9f5a70ea05824f149b53ed66548f9c36"></a>The system obtains the port according to the parameter setting and checks its validity. If the port is invalid, the system increases the port number by 1 each time for a maximum of 16 times until a valid port is obtained. The number of retries can be configured using <strong id="afd55f221408a4c049e505442213e56fd"><a name="afd55f221408a4c049e505442213e56fd"></a><a name="afd55f221408a4c049e505442213e56fd"></a>spark.port.maxRetries</strong>.</p>
</div></div>
<a name="ud8ec5b17570f4cfebbf1adbac8f0f655"></a><a name="ud8ec5b17570f4cfebbf1adbac8f0f655"></a><ul id="ud8ec5b17570f4cfebbf1adbac8f0f655"><li>Port enabled by default during the installation: Yes</li><li>Port enabled after security hardening: Yes</li></ul>
</td>
</tr>
<tr id="re6d94b4281bb44eab808114d4b38642f"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.1 "><p id="a2ed2e27f58f440b998348b54342cd0f7"><a name="a2ed2e27f58f440b998348b54342cd0f7"></a><a name="a2ed2e27f58f440b998348b54342cd0f7"></a>Storm</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="adc58424a7a5c424f9da0318a1f189366"><a name="adc58424a7a5c424f9da0318a1f189366"></a><a name="adc58424a7a5c424f9da0318a1f189366"></a>nimbus.thrift.port</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="a7e1ff69403834413899e621fa5810d2c"><a name="a7e1ff69403834413899e621fa5810d2c"></a><a name="a7e1ff69403834413899e621fa5810d2c"></a>29200</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.4 "><p id="a47f8e37d13a344e685341dbccd5691e9"><a name="a47f8e37d13a344e685341dbccd5691e9"></a><a name="a47f8e37d13a344e685341dbccd5691e9"></a>6627</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.6.1.5 "><p id="a14b789bd603044e197f078c9878e9728"><a name="a14b789bd603044e197f078c9878e9728"></a><a name="a14b789bd603044e197f078c9878e9728"></a>Port for Nimbus to provide thrift services</p>
</td>
</tr>
<tr id="r9ca47957dd744bf9a16fa4c6a854e4b3"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.1 "><p id="a70982b98eef54004afd4e5c990967e94"><a name="a70982b98eef54004afd4e5c990967e94"></a><a name="a70982b98eef54004afd4e5c990967e94"></a>Storm</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="ab62021c0ec7b4f8a89cbae315813487a"><a name="ab62021c0ec7b4f8a89cbae315813487a"></a><a name="ab62021c0ec7b4f8a89cbae315813487a"></a>supervisor.slots.ports</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="a71c260050f1c4913b4fe23366b820a0f"><a name="a71c260050f1c4913b4fe23366b820a0f"></a><a name="a71c260050f1c4913b4fe23366b820a0f"></a>29200-29499</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.4 "><p id="a5d2bf870d7b8431c87ff05fa1c6687fe"><a name="a5d2bf870d7b8431c87ff05fa1c6687fe"></a><a name="a5d2bf870d7b8431c87ff05fa1c6687fe"></a>"6700,6701,6702,6703"</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.6.1.5 "><p id="a3d7d7e58509d4465b81a1049c0b3aa56"><a name="a3d7d7e58509d4465b81a1049c0b3aa56"></a><a name="a3d7d7e58509d4465b81a1049c0b3aa56"></a>Port for receiving requests forwarded from other servers</p>
</td>
</tr>
<tr id="recbf34b5aad04e7f9bffaf7aba3e7e98"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.1 "><p id="a8c0d669a7ede4325937acee6291b0fc8"><a name="a8c0d669a7ede4325937acee6291b0fc8"></a><a name="a8c0d669a7ede4325937acee6291b0fc8"></a>Storm</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="a449280fb10d1407b8be4d688a2011990"><a name="a449280fb10d1407b8be4d688a2011990"></a><a name="a449280fb10d1407b8be4d688a2011990"></a>logviewer.port 29288</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="a954c7932e1de481099bdd43f9ccc9b60"><a name="a954c7932e1de481099bdd43f9ccc9b60"></a><a name="a954c7932e1de481099bdd43f9ccc9b60"></a>29248</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.4 "><p id="a2b90d7b0defb4d1abac57dfa58f11f9d"><a name="a2b90d7b0defb4d1abac57dfa58f11f9d"></a><a name="a2b90d7b0defb4d1abac57dfa58f11f9d"></a>8000</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.6.1.5 "><p id="a8a9ca43fd2314e47b72d7bf922056908"><a name="a8a9ca43fd2314e47b72d7bf922056908"></a><a name="a8a9ca43fd2314e47b72d7bf922056908"></a>Port for Logviewer to provide HTTPS services</p>
</td>
</tr>
<tr id="rf4d0a94ec6984584ad8f07336524673e"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.1 "><p id="a7574ed05a96845d298fd50c14141bd25"><a name="a7574ed05a96845d298fd50c14141bd25"></a><a name="a7574ed05a96845d298fd50c14141bd25"></a>Storm</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="a827493fd01144709af989f85ad655974"><a name="a827493fd01144709af989f85ad655974"></a><a name="a827493fd01144709af989f85ad655974"></a>ui.port</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="a30f31dfa96724ed2a13eafb09dd01073"><a name="a30f31dfa96724ed2a13eafb09dd01073"></a><a name="a30f31dfa96724ed2a13eafb09dd01073"></a>29280</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.4 "><p id="a2e18cc51f69541a79455a65f11a555e9"><a name="a2e18cc51f69541a79455a65f11a555e9"></a><a name="a2e18cc51f69541a79455a65f11a555e9"></a>29280</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.6.1.5 "><p id="a3d5833093c23429bb58cabb4217107d1"><a name="a3d5833093c23429bb58cabb4217107d1"></a><a name="a3d5833093c23429bb58cabb4217107d1"></a>Port for the Storm UI to provide HTTP services (ui.port)</p>
</td>
</tr>
<tr id="rbdb50e93fafd4474baec2fb7f5dd05ef"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.1 "><p id="a424b9c01d0214c3caf0c3cde467fa43f"><a name="a424b9c01d0214c3caf0c3cde467fa43f"></a><a name="a424b9c01d0214c3caf0c3cde467fa43f"></a>Storm</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="ad016e9788fdd424e83aad7d5d6ab31e6"><a name="ad016e9788fdd424e83aad7d5d6ab31e6"></a><a name="ad016e9788fdd424e83aad7d5d6ab31e6"></a>ui.port</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="a921a9ec6b64e41918136da0518ea040e"><a name="a921a9ec6b64e41918136da0518ea040e"></a><a name="a921a9ec6b64e41918136da0518ea040e"></a>29243</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.4 "><p id="abc06cac40ba24d85bba6a4eb9f18fe60"><a name="abc06cac40ba24d85bba6a4eb9f18fe60"></a><a name="abc06cac40ba24d85bba6a4eb9f18fe60"></a>29243</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.6.1.5 "><p id="ad297e724d1f346ee8debb4a95d735855"><a name="ad297e724d1f346ee8debb4a95d735855"></a><a name="ad297e724d1f346ee8debb4a95d735855"></a>Port for the Storm UI to provide HTTPS services (ui.port)</p>
</td>
</tr>
<tr id="r888f085dcd29402bb7f0164fffcda0fd"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.1 "><p id="a692a2b737a434c74aa70c3333152b785"><a name="a692a2b737a434c74aa70c3333152b785"></a><a name="a692a2b737a434c74aa70c3333152b785"></a>YARN</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="a3f5ae3cc1571481183cd06ff44a1b9a6"><a name="a3f5ae3cc1571481183cd06ff44a1b9a6"></a><a name="a3f5ae3cc1571481183cd06ff44a1b9a6"></a>yarn.resourcemanager.webapp.port</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="a8ab90b52efab414cb37f13a121328b69"><a name="a8ab90b52efab414cb37f13a121328b69"></a><a name="a8ab90b52efab414cb37f13a121328b69"></a>26000</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.4 "><p id="a9aae30c1445a4eaca18b80328e3be82f"><a name="a9aae30c1445a4eaca18b80328e3be82f"></a><a name="a9aae30c1445a4eaca18b80328e3be82f"></a>8088</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.6.1.5 "><p id="a42e437d3269a49a8b909850d36b1b3c1"><a name="a42e437d3269a49a8b909850d36b1b3c1"></a><a name="a42e437d3269a49a8b909850d36b1b3c1"></a>Web HTTP port of the ResourceManager service</p>
</td>
</tr>
<tr id="r5e5d05087c404d00a44a1bce905846ce"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.1 "><p id="a0bdba5889c394ef4af78922b21c4ee7b"><a name="a0bdba5889c394ef4af78922b21c4ee7b"></a><a name="a0bdba5889c394ef4af78922b21c4ee7b"></a>YARN</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="afd5da9774f0641a0a5b5f49a4cbcb81f"><a name="afd5da9774f0641a0a5b5f49a4cbcb81f"></a><a name="afd5da9774f0641a0a5b5f49a4cbcb81f"></a>yarn.resourcemanager.webapp.https.port</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="affe8a2190c7f44d48db4244b317622e5"><a name="affe8a2190c7f44d48db4244b317622e5"></a><a name="affe8a2190c7f44d48db4244b317622e5"></a>26001</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.4 "><p id="ab21428ea28094c8b990fd1f01f3c86f4"><a name="ab21428ea28094c8b990fd1f01f3c86f4"></a><a name="ab21428ea28094c8b990fd1f01f3c86f4"></a>8090</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.6.1.5 "><p id="ab4aa85a2c9824f96800d1ff5081667d0"><a name="ab4aa85a2c9824f96800d1ff5081667d0"></a><a name="ab4aa85a2c9824f96800d1ff5081667d0"></a>Web HTTPS port of the ResourceManager service</p>
<p id="aa2efada6a58b4b7b9a740ba2b3bf1e9c"><a name="aa2efada6a58b4b7b9a740ba2b3bf1e9c"></a><a name="aa2efada6a58b4b7b9a740ba2b3bf1e9c"></a>Used to access the ResourceManager web application in security mode.</p>
<div class="note" id="n264d58ab2c214c11b692a14f4f059ded"><a name="n264d58ab2c214c11b692a14f4f059ded"></a><a name="n264d58ab2c214c11b692a14f4f059ded"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="acf7f73b2cfa445229a7435dc472df93c"><a name="acf7f73b2cfa445229a7435dc472df93c"></a><a name="acf7f73b2cfa445229a7435dc472df93c"></a>The value range of the port is just a suggestion and is specified in the product. In addition, the value range of the port is not limited in code.</p>
</div></div>
<a name="ud4a617e4219f496aaa0af4a2b489cda0"></a><a name="ud4a617e4219f496aaa0af4a2b489cda0"></a><ul id="ud4a617e4219f496aaa0af4a2b489cda0"><li>Port enabled by default during the installation: Yes</li><li>Port enabled after security hardening: Yes</li></ul>
</td>
</tr>
<tr id="r01f26022cf4a4a8ab6774370494dce20"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.1 "><p id="ac4394d2b9a5647fab94065269185098c"><a name="ac4394d2b9a5647fab94065269185098c"></a><a name="ac4394d2b9a5647fab94065269185098c"></a>YARN</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="aef43063cc275455595b7068941df7207"><a name="aef43063cc275455595b7068941df7207"></a><a name="aef43063cc275455595b7068941df7207"></a>yarn.nodemanager.webapp.address</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="a73c767ad577241ff845f2b6b9a30383a"><a name="a73c767ad577241ff845f2b6b9a30383a"></a><a name="a73c767ad577241ff845f2b6b9a30383a"></a>26006</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.4 "><p id="ab063918b07de40cdac12e18943df2e36"><a name="ab063918b07de40cdac12e18943df2e36"></a><a name="ab063918b07de40cdac12e18943df2e36"></a>8042</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.6.1.5 "><p id="a01210f2ff6e841ada1e6c3de3deb9cbd"><a name="a01210f2ff6e841ada1e6c3de3deb9cbd"></a><a name="a01210f2ff6e841ada1e6c3de3deb9cbd"></a>NodeManager Web HTTP port</p>
</td>
</tr>
<tr id="r649494aad3c149c1983b1204eda0d146"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.1 "><p id="ad36a7c20ff4e44a9b833c5a1bd692f9c"><a name="ad36a7c20ff4e44a9b833c5a1bd692f9c"></a><a name="ad36a7c20ff4e44a9b833c5a1bd692f9c"></a>YARN</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="a6f33ba991fa743ae8273830139c9708d"><a name="a6f33ba991fa743ae8273830139c9708d"></a><a name="a6f33ba991fa743ae8273830139c9708d"></a>yarn.nodemanager.webapp.https.port</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="a92ab9b80af8844c588530c3a4d0808f6"><a name="a92ab9b80af8844c588530c3a4d0808f6"></a><a name="a92ab9b80af8844c588530c3a4d0808f6"></a>26010</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.4 "><p id="a9e7d2662a0ae4379baa581329dccbeea"><a name="a9e7d2662a0ae4379baa581329dccbeea"></a><a name="a9e7d2662a0ae4379baa581329dccbeea"></a>8044</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.6.1.5 "><p id="abe3a2c1198f349c3b364eed086a4cc9e"><a name="abe3a2c1198f349c3b364eed086a4cc9e"></a><a name="abe3a2c1198f349c3b364eed086a4cc9e"></a>NodeManager Web HTTPS port</p>
<p id="a59f9751744b046fcb88a3958f69bdc28"><a name="a59f9751744b046fcb88a3958f69bdc28"></a><a name="a59f9751744b046fcb88a3958f69bdc28"></a>Used to access the NodeManager web applications in security mode.</p>
<div class="note" id="n273d7b5c5a8a4e9897eae23dcd342b06"><a name="n273d7b5c5a8a4e9897eae23dcd342b06"></a><a name="n273d7b5c5a8a4e9897eae23dcd342b06"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="a8e7f779447c64f79beb13b5ce19bc299"><a name="a8e7f779447c64f79beb13b5ce19bc299"></a><a name="a8e7f779447c64f79beb13b5ce19bc299"></a>The value range of the port is just a suggestion and is specified in the product. In addition, the value range of the port is not limited in code.</p>
</div></div>
<a name="u2eca98ed1b714f05be7e57c2d574c5d4"></a><a name="u2eca98ed1b714f05be7e57c2d574c5d4"></a><ul id="u2eca98ed1b714f05be7e57c2d574c5d4"><li>Port enabled by default during the installation: Yes</li><li>Port enabled after security hardening: Yes</li></ul>
</td>
</tr>
<tr id="radd1302ccb5147688b0f1aa850cedfc0"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.1 "><p id="ace635e05e8034eda89d93ad01d854dc9"><a name="ace635e05e8034eda89d93ad01d854dc9"></a><a name="ace635e05e8034eda89d93ad01d854dc9"></a>ZooKeeper</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="a44f1f583940d43db9011dcf023bca092"><a name="a44f1f583940d43db9011dcf023bca092"></a><a name="a44f1f583940d43db9011dcf023bca092"></a>clientPort</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="a0a02792cc79948df85275e6d0fbe5d4b"><a name="a0a02792cc79948df85275e6d0fbe5d4b"></a><a name="a0a02792cc79948df85275e6d0fbe5d4b"></a>24002</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.4 "><p id="a1012a9bb15b143b59904b82e594e5639"><a name="a1012a9bb15b143b59904b82e594e5639"></a><a name="a1012a9bb15b143b59904b82e594e5639"></a>2181</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.6.1.5 "><p id="aec26301f86824daf9766c2f097e5e2d6"><a name="aec26301f86824daf9766c2f097e5e2d6"></a><a name="aec26301f86824daf9766c2f097e5e2d6"></a>ZooKeeper client port</p>
<p id="a73d5c8b4a4cf49258068b5ec9eeb243d"><a name="a73d5c8b4a4cf49258068b5ec9eeb243d"></a><a name="a73d5c8b4a4cf49258068b5ec9eeb243d"></a>Used for the ZooKeeper client to connect to the ZooKeeper server.</p>
<div class="note" id="n38a91132234143c5a8cd43618d683019"><a name="n38a91132234143c5a8cd43618d683019"></a><a name="n38a91132234143c5a8cd43618d683019"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="ad42e8c494df84d77a38e91479231831e"><a name="ad42e8c494df84d77a38e91479231831e"></a><a name="ad42e8c494df84d77a38e91479231831e"></a>The value range of the port is just a suggestion and is specified in the product. In addition, the value range of the port is not limited in code.</p>
</div></div>
<a name="u2f1c24929df3438ebf1bcb5e03fcce39"></a><a name="u2f1c24929df3438ebf1bcb5e03fcce39"></a><ul id="u2f1c24929df3438ebf1bcb5e03fcce39"><li>Port enabled by default during the installation: Yes</li><li>Port enabled after security hardening: Yes</li></ul>
</td>
</tr>
<tr id="r0a33ce9d4d9f415b80a3474085428047"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.1 "><p id="af6b71d8552604221aba7c6ada88f8078"><a name="af6b71d8552604221aba7c6ada88f8078"></a><a name="af6b71d8552604221aba7c6ada88f8078"></a>Kerberos</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="ad0f76d57bf114083aaeac483e6f30c00"><a name="ad0f76d57bf114083aaeac483e6f30c00"></a><a name="ad0f76d57bf114083aaeac483e6f30c00"></a>kdc_ports</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="a0fc39525f8b648c59227782a987487f8"><a name="a0fc39525f8b648c59227782a987487f8"></a><a name="a0fc39525f8b648c59227782a987487f8"></a>21732</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.4 "><p id="adb48b12c60424f57a87e52a28559a58b"><a name="adb48b12c60424f57a87e52a28559a58b"></a><a name="adb48b12c60424f57a87e52a28559a58b"></a>21732</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.6.1.5 "><p id="a177334273c8a4c96860f691947302bf7"><a name="a177334273c8a4c96860f691947302bf7"></a><a name="a177334273c8a4c96860f691947302bf7"></a>KerberOS server port</p>
<p id="a141709f7507b494992980e8b3fb94371"><a name="a141709f7507b494992980e8b3fb94371"></a><a name="a141709f7507b494992980e8b3fb94371"></a>Used for Kerberos authentication. This parameter may be used for configuring mutual trust relationships between clusters.</p>
<div class="note" id="n5b9fa81073c941c89acf8d985db4a584"><a name="n5b9fa81073c941c89acf8d985db4a584"></a><a name="n5b9fa81073c941c89acf8d985db4a584"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="a32f4c8b2cf48477583ec9e141eadf656"><a name="a32f4c8b2cf48477583ec9e141eadf656"></a><a name="a32f4c8b2cf48477583ec9e141eadf656"></a>The value range of the port is just a suggestion and is specified in the product. In addition, the value range of the port is not limited in code.</p>
</div></div>
<a name="ud814152744584185bd95492d3ff3b400"></a><a name="ud814152744584185bd95492d3ff3b400"></a><ul id="ud814152744584185bd95492d3ff3b400"><li>Port enabled by default during the installation: Yes</li><li>Port enabled after security hardening: Yes</li></ul>
</td>
</tr>
<tr id="row1863093814246"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.1 "><p id="en-us_topic_0104564856_p81151216959"><a name="en-us_topic_0104564856_p81151216959"></a><a name="en-us_topic_0104564856_p81151216959"></a>Opentsdb</p>
</td>
<td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.6.1.2 "><p id="en-us_topic_0104564856_p141157162058"><a name="en-us_topic_0104564856_p141157162058"></a><a name="en-us_topic_0104564856_p141157162058"></a>tsd.network.port</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.3 "><p id="en-us_topic_0104564856_p1211641613512"><a name="en-us_topic_0104564856_p1211641613512"></a><a name="en-us_topic_0104564856_p1211641613512"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.6.1.4 "><p id="en-us_topic_0104564856_p4116121612517"><a name="en-us_topic_0104564856_p4116121612517"></a><a name="en-us_topic_0104564856_p4116121612517"></a>4242</p>
</td>
<td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.6.1.5 "><p id="en-us_topic_0104564856_p11200164712511"><a name="en-us_topic_0104564856_p11200164712511"></a><a name="en-us_topic_0104564856_p11200164712511"></a>Web UI port of OpenTSDB</p>
<p id="en-us_topic_0104564856_p122001947259"><a name="en-us_topic_0104564856_p122001947259"></a><a name="en-us_topic_0104564856_p122001947259"></a>Used for HTTPS/HTTP communications between web requests and OpenTSDB UI servers</p>
</td>
</tr>
</tbody>
</table>


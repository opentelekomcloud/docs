# Key Operations on SDRS<a name="en-us_cts_01_0002"></a>

Storage Disaster Recovery Service \(SDRS\) provides disaster recovery \(DR\) services for many public cloud services, such as Elastic Cloud Server \(ECS\), Dedicated Distributed Storage Service \(DSS\), and Elastic Volume Service \(EVS\). SDRS uses multiple technologies, such as storage replication, data redundancy, and cache acceleration, to provide high data reliability and service continuity for users.

With CTS, you can record operations associated with SDRS for future query, audit, and backtrack operations.

**Table  1**  SDRS operations that can be recorded by CTS

<a name="table8064500142947"></a>
<table><thead align="left"><tr id="r775e13cd14af4c6593e66cfa36ad850f"><th class="cellrowborder" valign="top" width="33.84848484848485%" id="mcps1.2.4.1.1"><p id="a8267f4cf876348ce9a896a72d20b8344"><a name="a8267f4cf876348ce9a896a72d20b8344"></a><a name="a8267f4cf876348ce9a896a72d20b8344"></a><strong id="b842352706103557"><a name="b842352706103557"></a><a name="b842352706103557"></a>Operation</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.16161616161616%" id="mcps1.2.4.1.2"><p id="aa06dda0651794ab29de1ee7025e9379c"><a name="aa06dda0651794ab29de1ee7025e9379c"></a><a name="aa06dda0651794ab29de1ee7025e9379c"></a><strong id="b84235270610360"><a name="b84235270610360"></a><a name="b84235270610360"></a>Resource Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="32.98989898989899%" id="mcps1.2.4.1.3"><p id="aa73bf607a8d747578d80c87e698dd11e"><a name="aa73bf607a8d747578d80c87e698dd11e"></a><a name="aa73bf607a8d747578d80c87e698dd11e"></a><strong id="b842352706182955"><a name="b842352706182955"></a><a name="b842352706182955"></a>Trace Name</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="rb710fdb4bcb449df8fc14117e2cf2eb4"><td class="cellrowborder" valign="top" width="33.84848484848485%" headers="mcps1.2.4.1.1 "><p id="a925045f3d4a749c988164cfd242e1e52"><a name="a925045f3d4a749c988164cfd242e1e52"></a><a name="a925045f3d4a749c988164cfd242e1e52"></a>Creating a protection group</p>
</td>
<td class="cellrowborder" valign="top" width="33.16161616161616%" headers="mcps1.2.4.1.2 "><p id="a9fb15bc0449b4dd7a76833973c1e7d00"><a name="a9fb15bc0449b4dd7a76833973c1e7d00"></a><a name="a9fb15bc0449b4dd7a76833973c1e7d00"></a>protectionGroup</p>
</td>
<td class="cellrowborder" valign="top" width="32.98989898989899%" headers="mcps1.2.4.1.3 "><p id="aed868bff87704dbc8c63f02964c9f321"><a name="aed868bff87704dbc8c63f02964c9f321"></a><a name="aed868bff87704dbc8c63f02964c9f321"></a>createProtectionGroupNoCG</p>
</td>
</tr>
<tr id="raf210888bf3d4c45bbd1ed10be06a5e8"><td class="cellrowborder" valign="top" width="33.84848484848485%" headers="mcps1.2.4.1.1 "><p id="adf460d7ff38a4f6398f704dbb833467f"><a name="adf460d7ff38a4f6398f704dbb833467f"></a><a name="adf460d7ff38a4f6398f704dbb833467f"></a>Deleting a protection group</p>
</td>
<td class="cellrowborder" valign="top" width="33.16161616161616%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0140053350_p131855301467"><a name="en-us_topic_0140053350_p131855301467"></a><a name="en-us_topic_0140053350_p131855301467"></a>protectionGroup</p>
</td>
<td class="cellrowborder" valign="top" width="32.98989898989899%" headers="mcps1.2.4.1.3 "><p id="a30342a26be9346829b6be737b68fc087"><a name="a30342a26be9346829b6be737b68fc087"></a><a name="a30342a26be9346829b6be737b68fc087"></a>deleteProtectionGroupNoCG</p>
</td>
</tr>
<tr id="r9d000f4d1ed54144968e01267aa43101"><td class="cellrowborder" valign="top" width="33.84848484848485%" headers="mcps1.2.4.1.1 "><p id="aacdb3b2e69644e2eb755ecc287d892b6"><a name="aacdb3b2e69644e2eb755ecc287d892b6"></a><a name="aacdb3b2e69644e2eb755ecc287d892b6"></a>Updating a protection group</p>
</td>
<td class="cellrowborder" valign="top" width="33.16161616161616%" headers="mcps1.2.4.1.2 "><p id="a65497f6604814dcaabdf4fb4b57a1f73"><a name="a65497f6604814dcaabdf4fb4b57a1f73"></a><a name="a65497f6604814dcaabdf4fb4b57a1f73"></a>protectionGroup</p>
</td>
<td class="cellrowborder" valign="top" width="32.98989898989899%" headers="mcps1.2.4.1.3 "><p id="abbc282bf7935483a9ef8be94c2381d4f"><a name="abbc282bf7935483a9ef8be94c2381d4f"></a><a name="abbc282bf7935483a9ef8be94c2381d4f"></a>updateProtectionGroup</p>
</td>
</tr>
<tr id="r0cfc2504142c45829f101b1cde4853d3"><td class="cellrowborder" valign="top" width="33.84848484848485%" headers="mcps1.2.4.1.1 "><p id="ad06b33b568c64be7a7703b3ba5ec4b6b"><a name="ad06b33b568c64be7a7703b3ba5ec4b6b"></a><a name="ad06b33b568c64be7a7703b3ba5ec4b6b"></a>Enabling protection for a protection group (when the protection group is in the <strong id="b149919325244"><a name="b149919325244"></a><a name="b149919325244"></a>Available</strong> state)</p>
</td>
<td class="cellrowborder" valign="top" width="33.16161616161616%" headers="mcps1.2.4.1.2 "><p id="a1e3bf1a3f00b45719629d81a2c8ee140"><a name="a1e3bf1a3f00b45719629d81a2c8ee140"></a><a name="a1e3bf1a3f00b45719629d81a2c8ee140"></a>protectionGroup</p>
</td>
<td class="cellrowborder" valign="top" width="32.98989898989899%" headers="mcps1.2.4.1.3 "><p id="a6b4b8313cafe4379978c03697a202d20"><a name="a6b4b8313cafe4379978c03697a202d20"></a><a name="a6b4b8313cafe4379978c03697a202d20"></a>startProtectionGroupNoCG</p>
</td>
</tr>
<tr id="r7850f1ea0414441bbbca35ca02772901"><td class="cellrowborder" valign="top" width="33.84848484848485%" headers="mcps1.2.4.1.1 "><p id="a9d566072ce904ee99fb9f736f9d28a50"><a name="a9d566072ce904ee99fb9f736f9d28a50"></a><a name="a9d566072ce904ee99fb9f736f9d28a50"></a>Enabling protection for a protection group (when the protection group is in the <strong id="b1859182119253"><a name="b1859182119253"></a><a name="b1859182119253"></a>failed-over</strong> or <strong id="b194516587378"><a name="b194516587378"></a><a name="b194516587378"></a>failed-over-back</strong> state)</p>
</td>
<td class="cellrowborder" valign="top" width="33.16161616161616%" headers="mcps1.2.4.1.2 "><p id="ae4ca040a5c6b4c529e7ad42d237051c4"><a name="ae4ca040a5c6b4c529e7ad42d237051c4"></a><a name="ae4ca040a5c6b4c529e7ad42d237051c4"></a>protectionGroup</p>
</td>
<td class="cellrowborder" valign="top" width="32.98989898989899%" headers="mcps1.2.4.1.3 "><p id="ab3ae1762f996492fbf81ff21ae8015a4"><a name="ab3ae1762f996492fbf81ff21ae8015a4"></a><a name="ab3ae1762f996492fbf81ff21ae8015a4"></a>reprotectProtectionGroupNoCG</p>
</td>
</tr>
<tr id="rfe1c2e67295149a2ab31c5eb4f55c5ef"><td class="cellrowborder" valign="top" width="33.84848484848485%" headers="mcps1.2.4.1.1 "><p id="aded343887da14160bf73aeb0635cd36c"><a name="aded343887da14160bf73aeb0635cd36c"></a><a name="aded343887da14160bf73aeb0635cd36c"></a>Disabling protection for a protection group</p>
</td>
<td class="cellrowborder" valign="top" width="33.16161616161616%" headers="mcps1.2.4.1.2 "><p id="a78a60afac5d54983944801d1185746af"><a name="a78a60afac5d54983944801d1185746af"></a><a name="a78a60afac5d54983944801d1185746af"></a>protectionGroup</p>
</td>
<td class="cellrowborder" valign="top" width="32.98989898989899%" headers="mcps1.2.4.1.3 "><p id="a09acc3f03a3c4bed9756b1b87511be0d"><a name="a09acc3f03a3c4bed9756b1b87511be0d"></a><a name="a09acc3f03a3c4bed9756b1b87511be0d"></a>stopProtectionGroupNoCG</p>
</td>
</tr>
<tr id="rc714b79a70ee4cc38ca8c894b3331c5f"><td class="cellrowborder" valign="top" width="33.84848484848485%" headers="mcps1.2.4.1.1 "><p id="a5513e13d3a5f43aea73a97ee0b7c8730"><a name="a5513e13d3a5f43aea73a97ee0b7c8730"></a><a name="a5513e13d3a5f43aea73a97ee0b7c8730"></a>Executing a failover or failback</p>
</td>
<td class="cellrowborder" valign="top" width="33.16161616161616%" headers="mcps1.2.4.1.2 "><p id="a26f0e0236f09450fb74596de89d941d8"><a name="a26f0e0236f09450fb74596de89d941d8"></a><a name="a26f0e0236f09450fb74596de89d941d8"></a>protectionGroup</p>
</td>
<td class="cellrowborder" valign="top" width="32.98989898989899%" headers="mcps1.2.4.1.3 "><p id="ad4ca7c5eeb3c47c6b1a9cd6d83f68a75"><a name="ad4ca7c5eeb3c47c6b1a9cd6d83f68a75"></a><a name="ad4ca7c5eeb3c47c6b1a9cd6d83f68a75"></a>failoverProtectionGroupNoCG</p>
</td>
</tr>
<tr id="re1673985a70f408ea05110255a6251ee"><td class="cellrowborder" valign="top" width="33.84848484848485%" headers="mcps1.2.4.1.1 "><p id="af7eafa322043402290ce0dd6c22f2e5e"><a name="af7eafa322043402290ce0dd6c22f2e5e"></a><a name="af7eafa322043402290ce0dd6c22f2e5e"></a>Executing a planned failover or planned failback</p>
</td>
<td class="cellrowborder" valign="top" width="33.16161616161616%" headers="mcps1.2.4.1.2 "><p id="a8689cae2389a4815ae8b612b586f101b"><a name="a8689cae2389a4815ae8b612b586f101b"></a><a name="a8689cae2389a4815ae8b612b586f101b"></a>protectionGroup</p>
</td>
<td class="cellrowborder" valign="top" width="32.98989898989899%" headers="mcps1.2.4.1.3 "><p id="abab330f2e31349b9bd7da21379a43fd3"><a name="abab330f2e31349b9bd7da21379a43fd3"></a><a name="abab330f2e31349b9bd7da21379a43fd3"></a>reverseProtectionGroupNoCG</p>
</td>
</tr>
<tr id="r61f1b71c032d4d41afc380b17d6e5be8"><td class="cellrowborder" valign="top" width="33.84848484848485%" headers="mcps1.2.4.1.1 "><p id="a2722d2e7c32e4005a2ed62499a4fdb61"><a name="a2722d2e7c32e4005a2ed62499a4fdb61"></a><a name="a2722d2e7c32e4005a2ed62499a4fdb61"></a>Action performed when a job of the protection group failed to submit</p>
</td>
<td class="cellrowborder" valign="top" width="33.16161616161616%" headers="mcps1.2.4.1.2 "><p id="ad7e9f7bb28d847bfa2327e919320d207"><a name="ad7e9f7bb28d847bfa2327e919320d207"></a><a name="ad7e9f7bb28d847bfa2327e919320d207"></a>protectionGroup</p>
</td>
<td class="cellrowborder" valign="top" width="32.98989898989899%" headers="mcps1.2.4.1.3 "><p id="afb894cdb451d4c43bc2afef366973f83"><a name="afb894cdb451d4c43bc2afef366973f83"></a><a name="afb894cdb451d4c43bc2afef366973f83"></a>protectionGroupAction</p>
</td>
</tr>
<tr id="r3d4b902ff031415cad6e9c3883828dd6"><td class="cellrowborder" valign="top" width="33.84848484848485%" headers="mcps1.2.4.1.1 "><p id="ad2c610446fea44378b20e8ff17d578cc"><a name="ad2c610446fea44378b20e8ff17d578cc"></a><a name="ad2c610446fea44378b20e8ff17d578cc"></a>Creating a protected instance</p>
</td>
<td class="cellrowborder" valign="top" width="33.16161616161616%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0140053350_p918643004619"><a name="en-us_topic_0140053350_p918643004619"></a><a name="en-us_topic_0140053350_p918643004619"></a>protectedInstance</p>
</td>
<td class="cellrowborder" valign="top" width="32.98989898989899%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0140053350_p122620399243"><a name="en-us_topic_0140053350_p122620399243"></a><a name="en-us_topic_0140053350_p122620399243"></a>createProtectedInstanceNoCG</p>
</td>
</tr>
<tr id="r302dc09a06ac483493c875df22c8b350"><td class="cellrowborder" valign="top" width="33.84848484848485%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0140053350_p981484972411"><a name="en-us_topic_0140053350_p981484972411"></a><a name="en-us_topic_0140053350_p981484972411"></a>Deleting a protected instance</p>
</td>
<td class="cellrowborder" valign="top" width="33.16161616161616%" headers="mcps1.2.4.1.2 "><p id="adc159002a68a4de2b0d6dce03d2299c2"><a name="adc159002a68a4de2b0d6dce03d2299c2"></a><a name="adc159002a68a4de2b0d6dce03d2299c2"></a>protectedInstance</p>
</td>
<td class="cellrowborder" valign="top" width="32.98989898989899%" headers="mcps1.2.4.1.3 "><p id="a0512a95fc7be416b994a390c728bd45f"><a name="a0512a95fc7be416b994a390c728bd45f"></a><a name="a0512a95fc7be416b994a390c728bd45f"></a>deleteProtectedInstanceNoCG</p>
</td>
</tr>
<tr id="r8c0ee0c8e9d5485d9ea672ccdb8edd2a"><td class="cellrowborder" valign="top" width="33.84848484848485%" headers="mcps1.2.4.1.1 "><p id="aa14ea5044363425eb7145f6c781a187e"><a name="aa14ea5044363425eb7145f6c781a187e"></a><a name="aa14ea5044363425eb7145f6c781a187e"></a>Updating a protected instance</p>
</td>
<td class="cellrowborder" valign="top" width="33.16161616161616%" headers="mcps1.2.4.1.2 "><p id="aea28a6f249704f438dbdc5984cf80939"><a name="aea28a6f249704f438dbdc5984cf80939"></a><a name="aea28a6f249704f438dbdc5984cf80939"></a>protectedInstance</p>
</td>
<td class="cellrowborder" valign="top" width="32.98989898989899%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0140053350_p212625612242"><a name="en-us_topic_0140053350_p212625612242"></a><a name="en-us_topic_0140053350_p212625612242"></a>updateProtectedInstance</p>
</td>
</tr>
<tr id="r9c5cac72ec99493c951147f85bf40327"><td class="cellrowborder" valign="top" width="33.84848484848485%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0140053350_p31775912410"><a name="en-us_topic_0140053350_p31775912410"></a><a name="en-us_topic_0140053350_p31775912410"></a>Attaching a replication pair to a protected instance</p>
</td>
<td class="cellrowborder" valign="top" width="33.16161616161616%" headers="mcps1.2.4.1.2 "><p id="a7acebecbb17c44aca3c967f7263406c7"><a name="a7acebecbb17c44aca3c967f7263406c7"></a><a name="a7acebecbb17c44aca3c967f7263406c7"></a>protectedInstance</p>
</td>
<td class="cellrowborder" valign="top" width="32.98989898989899%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0140053350_p317359102416"><a name="en-us_topic_0140053350_p317359102416"></a><a name="en-us_topic_0140053350_p317359102416"></a>attachReplicationPair</p>
</td>
</tr>
<tr id="redc4351db6234c78adbfe98c6f6e7891"><td class="cellrowborder" valign="top" width="33.84848484848485%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0140053350_p118912213251"><a name="en-us_topic_0140053350_p118912213251"></a><a name="en-us_topic_0140053350_p118912213251"></a>Detaching a replication pair from a protected instance</p>
</td>
<td class="cellrowborder" valign="top" width="33.16161616161616%" headers="mcps1.2.4.1.2 "><p id="afa373a201a754b8cb9ae09466e776580"><a name="afa373a201a754b8cb9ae09466e776580"></a><a name="afa373a201a754b8cb9ae09466e776580"></a>protectedInstance</p>
</td>
<td class="cellrowborder" valign="top" width="32.98989898989899%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0140053350_p151891122252"><a name="en-us_topic_0140053350_p151891122252"></a><a name="en-us_topic_0140053350_p151891122252"></a>detachReplicationPair</p>
</td>
</tr>
<tr id="rbe044a42d07e4ae0bdf239423a637b19"><td class="cellrowborder" valign="top" width="33.84848484848485%" headers="mcps1.2.4.1.1 "><p id="a72ca1456a63a484aa69ba01131081528"><a name="a72ca1456a63a484aa69ba01131081528"></a><a name="a72ca1456a63a484aa69ba01131081528"></a>Adding a NIC to a protected instance</p>
</td>
<td class="cellrowborder" valign="top" width="33.16161616161616%" headers="mcps1.2.4.1.2 "><p id="a516ed495dfe84060851d637f13c67eb6"><a name="a516ed495dfe84060851d637f13c67eb6"></a><a name="a516ed495dfe84060851d637f13c67eb6"></a>protectedInstance</p>
</td>
<td class="cellrowborder" valign="top" width="32.98989898989899%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0140053350_p183385317248"><a name="en-us_topic_0140053350_p183385317248"></a><a name="en-us_topic_0140053350_p183385317248"></a>addNicNew</p>
</td>
</tr>
<tr id="r46df6898431a40fd87ace5b442b4ad5b"><td class="cellrowborder" valign="top" width="33.84848484848485%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0140053350_p787574610248"><a name="en-us_topic_0140053350_p787574610248"></a><a name="en-us_topic_0140053350_p787574610248"></a>Deleting a NIC from a protected instance</p>
</td>
<td class="cellrowborder" valign="top" width="33.16161616161616%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0140053350_p41869302467"><a name="en-us_topic_0140053350_p41869302467"></a><a name="en-us_topic_0140053350_p41869302467"></a>protectedInstance</p>
</td>
<td class="cellrowborder" valign="top" width="32.98989898989899%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0140053350_p887534615247"><a name="en-us_topic_0140053350_p887534615247"></a><a name="en-us_topic_0140053350_p887534615247"></a>deleteNicNew</p>
</td>
</tr>
<tr id="rbee126aa580b4f3896b4caf4716f434b"><td class="cellrowborder" valign="top" width="33.84848484848485%" headers="mcps1.2.4.1.1 "><p id="ab40be8000ea2419abe78d582960e0222"><a name="ab40be8000ea2419abe78d582960e0222"></a><a name="ab40be8000ea2419abe78d582960e0222"></a>Modifying the specifications of a protected instance</p>
</td>
<td class="cellrowborder" valign="top" width="33.16161616161616%" headers="mcps1.2.4.1.2 "><p id="ab9f801207af94ee3bee934ca67b74ad5"><a name="ab9f801207af94ee3bee934ca67b74ad5"></a><a name="ab9f801207af94ee3bee934ca67b74ad5"></a>protectedInstance</p>
</td>
<td class="cellrowborder" valign="top" width="32.98989898989899%" headers="mcps1.2.4.1.3 "><p id="a17440f16be864a1ba1d7f5a368f25108"><a name="a17440f16be864a1ba1d7f5a368f25108"></a><a name="a17440f16be864a1ba1d7f5a368f25108"></a>resizeProtectedInstanceNew</p>
</td>
</tr>
<tr id="r6d67b8f041d54c71b5bf27021a804506"><td class="cellrowborder" valign="top" width="33.84848484848485%" headers="mcps1.2.4.1.1 "><p id="a96a2991cd65e42f69ff3c7cec854797d"><a name="a96a2991cd65e42f69ff3c7cec854797d"></a><a name="a96a2991cd65e42f69ff3c7cec854797d"></a>Creating a replication pair</p>
</td>
<td class="cellrowborder" valign="top" width="33.16161616161616%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0140053350_p151861303468"><a name="en-us_topic_0140053350_p151861303468"></a><a name="en-us_topic_0140053350_p151861303468"></a>replicationPair</p>
</td>
<td class="cellrowborder" valign="top" width="32.98989898989899%" headers="mcps1.2.4.1.3 "><p id="a6be307cd1cbc4f528ac6350e92b0b05e"><a name="a6be307cd1cbc4f528ac6350e92b0b05e"></a><a name="a6be307cd1cbc4f528ac6350e92b0b05e"></a>createReplicationPairNoCG</p>
</td>
</tr>
<tr id="re6c720d481df410896502d443924ac79"><td class="cellrowborder" valign="top" width="33.84848484848485%" headers="mcps1.2.4.1.1 "><p id="a2a26fb473eba41088a46938589a4add5"><a name="a2a26fb473eba41088a46938589a4add5"></a><a name="a2a26fb473eba41088a46938589a4add5"></a>Deleting a replication pair</p>
</td>
<td class="cellrowborder" valign="top" width="33.16161616161616%" headers="mcps1.2.4.1.2 "><p id="ae29e96effc924b3bb09d0835ef413643"><a name="ae29e96effc924b3bb09d0835ef413643"></a><a name="ae29e96effc924b3bb09d0835ef413643"></a>replicationPair</p>
</td>
<td class="cellrowborder" valign="top" width="32.98989898989899%" headers="mcps1.2.4.1.3 "><p id="a807d230329d54fea87b663cce7794025"><a name="a807d230329d54fea87b663cce7794025"></a><a name="a807d230329d54fea87b663cce7794025"></a>deleteReplicationPairNoCG</p>
</td>
</tr>
<tr id="rc9deabe6c3dd49868aae9770fe074ccf"><td class="cellrowborder" valign="top" width="33.84848484848485%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0140053350_p78615389274"><a name="en-us_topic_0140053350_p78615389274"></a><a name="en-us_topic_0140053350_p78615389274"></a>Updating a replication pair</p>
</td>
<td class="cellrowborder" valign="top" width="33.16161616161616%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0140053350_p612943714619"><a name="en-us_topic_0140053350_p612943714619"></a><a name="en-us_topic_0140053350_p612943714619"></a>replicationPair</p>
</td>
<td class="cellrowborder" valign="top" width="32.98989898989899%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0140053350_p286193832710"><a name="en-us_topic_0140053350_p286193832710"></a><a name="en-us_topic_0140053350_p286193832710"></a>updateReplicationPair</p>
</td>
</tr>
<tr id="re826b2794178404094c1c9283fddce05"><td class="cellrowborder" valign="top" width="33.84848484848485%" headers="mcps1.2.4.1.1 "><p id="ac7ec0213c1cc424f808c07daea5557d6"><a name="ac7ec0213c1cc424f808c07daea5557d6"></a><a name="ac7ec0213c1cc424f808c07daea5557d6"></a>Expanding the capacity of a replication pair</p>
</td>
<td class="cellrowborder" valign="top" width="33.16161616161616%" headers="mcps1.2.4.1.2 "><p id="a7a13f9edd85b49c58ac3546f290b494a"><a name="a7a13f9edd85b49c58ac3546f290b494a"></a><a name="a7a13f9edd85b49c58ac3546f290b494a"></a>replicationPair</p>
</td>
<td class="cellrowborder" valign="top" width="32.98989898989899%" headers="mcps1.2.4.1.3 "><p id="a4c99f04f4e0740039b9c260c4d09c065"><a name="a4c99f04f4e0740039b9c260c4d09c065"></a><a name="a4c99f04f4e0740039b9c260c4d09c065"></a>expandReplicationPairNew</p>
</td>
</tr>
</tbody>
</table>


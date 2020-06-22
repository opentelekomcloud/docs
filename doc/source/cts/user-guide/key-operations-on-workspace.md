# Key Operations on Workspace<a name="en-us_topic_0100363628"></a>

Workspace is a cloud computing–based desktop service that is superior to traditional desktop services. Workspace supports access by various devices, including PCs running Windows or Mac, iPad, iPhone, and Android smart devices. It enables you to access, store, and obtain files and applications anywhere and at any time, that is, mobile working and entertainment. Workspace provides configuration similar to a traditional desktop, including vCPU, GPU, memory, disks, and Windows. You can use it in the same way you use a PC.

With CTS, you can record operations associated with Workspace for later query, audit, and backtrack operations.

**Table  1**  Workspace operations that can be recorded by CTS

<a name="table50443047153217"></a>
<table><thead align="left"><tr id="r8b35e687bfe9495da62420ff89d82020"><th class="cellrowborder" valign="top" width="30.403040304030405%" id="mcps1.2.4.1.1"><p id="a0df296b4d79c47fd819c3dfcbf984f10"><a name="a0df296b4d79c47fd819c3dfcbf984f10"></a><a name="a0df296b4d79c47fd819c3dfcbf984f10"></a><strong id="b842352706103557"><a name="b842352706103557"></a><a name="b842352706103557"></a>Operation</strong></p>
</th>
<th class="cellrowborder" valign="top" width="27.07270727072707%" id="mcps1.2.4.1.2"><p id="a8c83be0cc900438eb3fd30523e559947"><a name="a8c83be0cc900438eb3fd30523e559947"></a><a name="a8c83be0cc900438eb3fd30523e559947"></a><strong id="b84235270610360"><a name="b84235270610360"></a><a name="b84235270610360"></a>Resource Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="42.52425242524252%" id="mcps1.2.4.1.3"><p id="a4e79f4e4e2024d3ba2cf8c99ce54fa0d"><a name="a4e79f4e4e2024d3ba2cf8c99ce54fa0d"></a><a name="a4e79f4e4e2024d3ba2cf8c99ce54fa0d"></a><strong id="b842352706182955"><a name="b842352706182955"></a><a name="b842352706182955"></a>Trace Name</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r66f0dcb85991490e9ff398a2a3fa203a"><td class="cellrowborder" valign="top" width="30.403040304030405%" headers="mcps1.2.4.1.1 "><p id="a51bd43c6376f4c3db4b110647ce2bb5b"><a name="a51bd43c6376f4c3db4b110647ce2bb5b"></a><a name="a51bd43c6376f4c3db4b110647ce2bb5b"></a>Updating the status of a cloud service</p>
</td>
<td class="cellrowborder" valign="top" width="27.07270727072707%" headers="mcps1.2.4.1.2 "><p id="a5f9d48b2d75d4afabb75aa95f75aa06f"><a name="a5f9d48b2d75d4afabb75aa95f75aa06f"></a><a name="a5f9d48b2d75d4afabb75aa95f75aa06f"></a>workspace</p>
</td>
<td class="cellrowborder" valign="top" width="42.52425242524252%" headers="mcps1.2.4.1.3 "><p id="a130559ef40484538b88144b369af6d1a"><a name="a130559ef40484538b88144b369af6d1a"></a><a name="a130559ef40484538b88144b369af6d1a"></a>updateDesktopMetadata</p>
</td>
</tr>
<tr id="r539e9daad934433fab4db6e636e90ca4"><td class="cellrowborder" valign="top" width="30.403040304030405%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0100240418_p248726153217"><a name="en-us_topic_0100240418_p248726153217"></a><a name="en-us_topic_0100240418_p248726153217"></a>Subscribing to Workspace</p>
</td>
<td class="cellrowborder" valign="top" width="27.07270727072707%" headers="mcps1.2.4.1.2 "><p id="ac62a09fcc2424596997ab99df089acd5"><a name="ac62a09fcc2424596997ab99df089acd5"></a><a name="ac62a09fcc2424596997ab99df089acd5"></a>workspace</p>
</td>
<td class="cellrowborder" valign="top" width="42.52425242524252%" headers="mcps1.2.4.1.3 "><p id="a39fa76aed6ca4c3eaa049df614832d3a"><a name="a39fa76aed6ca4c3eaa049df614832d3a"></a><a name="a39fa76aed6ca4c3eaa049df614832d3a"></a>orderVm</p>
</td>
</tr>
<tr id="re231ecd0b7244f58bc0eeebbee0e006a"><td class="cellrowborder" valign="top" width="30.403040304030405%" headers="mcps1.2.4.1.1 "><p id="a44f6869ba99042fdb6a4cd8980e87663"><a name="a44f6869ba99042fdb6a4cd8980e87663"></a><a name="a44f6869ba99042fdb6a4cd8980e87663"></a>Restarting a VM</p>
</td>
<td class="cellrowborder" valign="top" width="27.07270727072707%" headers="mcps1.2.4.1.2 "><p id="ae51d12af7d6947e8921720925ef64642"><a name="ae51d12af7d6947e8921720925ef64642"></a><a name="ae51d12af7d6947e8921720925ef64642"></a>workspace</p>
</td>
<td class="cellrowborder" valign="top" width="42.52425242524252%" headers="mcps1.2.4.1.3 "><p id="a4ac3501940fb470285d858b66823ecd0"><a name="a4ac3501940fb470285d858b66823ecd0"></a><a name="a4ac3501940fb470285d858b66823ecd0"></a>rebootDesktop</p>
</td>
</tr>
<tr id="r4c2efe52e98c415e8ea8a5a41219458a"><td class="cellrowborder" valign="top" width="30.403040304030405%" headers="mcps1.2.4.1.1 "><p id="ae72c377ce6cd4ddd8bf727112145e847"><a name="ae72c377ce6cd4ddd8bf727112145e847"></a><a name="ae72c377ce6cd4ddd8bf727112145e847"></a>Stopping a VM</p>
</td>
<td class="cellrowborder" valign="top" width="27.07270727072707%" headers="mcps1.2.4.1.2 "><p id="a38ba2509a06f484c883a3bd13a3d5990"><a name="a38ba2509a06f484c883a3bd13a3d5990"></a><a name="a38ba2509a06f484c883a3bd13a3d5990"></a>workspace</p>
</td>
<td class="cellrowborder" valign="top" width="42.52425242524252%" headers="mcps1.2.4.1.3 "><p id="a73ac23372b8e42e18aabb34bfbc179d7"><a name="a73ac23372b8e42e18aabb34bfbc179d7"></a><a name="a73ac23372b8e42e18aabb34bfbc179d7"></a>shutdownDesktop</p>
</td>
</tr>
<tr id="r7f99df94e9794a97a663c7c6bf34bcd6"><td class="cellrowborder" valign="top" width="30.403040304030405%" headers="mcps1.2.4.1.1 "><p id="a485e8458622341a98bb97e6c7ff25421"><a name="a485e8458622341a98bb97e6c7ff25421"></a><a name="a485e8458622341a98bb97e6c7ff25421"></a>Starting a VM</p>
</td>
<td class="cellrowborder" valign="top" width="27.07270727072707%" headers="mcps1.2.4.1.2 "><p id="aa1efa0c3bcb442cca12ba9e370ed5400"><a name="aa1efa0c3bcb442cca12ba9e370ed5400"></a><a name="aa1efa0c3bcb442cca12ba9e370ed5400"></a>workspace</p>
</td>
<td class="cellrowborder" valign="top" width="42.52425242524252%" headers="mcps1.2.4.1.3 "><p id="a951ace6a20484ee7bf658158b1773f81"><a name="a951ace6a20484ee7bf658158b1773f81"></a><a name="a951ace6a20484ee7bf658158b1773f81"></a>startDesktop</p>
</td>
</tr>
<tr id="r035c5baae6044747819f204a8f3079bc"><td class="cellrowborder" valign="top" width="30.403040304030405%" headers="mcps1.2.4.1.1 "><p id="aaa0f1b8997fb4f5fbbe50c85cda75b65"><a name="aaa0f1b8997fb4f5fbbe50c85cda75b65"></a><a name="aaa0f1b8997fb4f5fbbe50c85cda75b65"></a>Deleting a VM</p>
</td>
<td class="cellrowborder" valign="top" width="27.07270727072707%" headers="mcps1.2.4.1.2 "><p id="aac46b0be000b41cf919838257c645eff"><a name="aac46b0be000b41cf919838257c645eff"></a><a name="aac46b0be000b41cf919838257c645eff"></a>workspace</p>
</td>
<td class="cellrowborder" valign="top" width="42.52425242524252%" headers="mcps1.2.4.1.3 "><p id="ab336ad35f0d24c04b49a4fbda19a8f6a"><a name="ab336ad35f0d24c04b49a4fbda19a8f6a"></a><a name="ab336ad35f0d24c04b49a4fbda19a8f6a"></a>deleteDesktop</p>
</td>
</tr>
<tr id="rab402ac6da7647248f2f1479e1ef1638"><td class="cellrowborder" valign="top" width="30.403040304030405%" headers="mcps1.2.4.1.1 "><p id="aa263795ebba645789b273f5ca281b4cd"><a name="aa263795ebba645789b273f5ca281b4cd"></a><a name="aa263795ebba645789b273f5ca281b4cd"></a>Updating the status of a desktop</p>
</td>
<td class="cellrowborder" valign="top" width="27.07270727072707%" headers="mcps1.2.4.1.2 "><p id="aa0bc77a9a0ea4a9f9d242b68b2f8fe3e"><a name="aa0bc77a9a0ea4a9f9d242b68b2f8fe3e"></a><a name="aa0bc77a9a0ea4a9f9d242b68b2f8fe3e"></a>workspace</p>
</td>
<td class="cellrowborder" valign="top" width="42.52425242524252%" headers="mcps1.2.4.1.3 "><p id="a3f3e1cf60a894c56acb80e879bc05d82"><a name="a3f3e1cf60a894c56acb80e879bc05d82"></a><a name="a3f3e1cf60a894c56acb80e879bc05d82"></a>updateDesktopStatus</p>
</td>
</tr>
<tr id="rc035089cace24a698bec03c0c1dcd336"><td class="cellrowborder" valign="top" width="30.403040304030405%" headers="mcps1.2.4.1.1 "><p id="a629b6384e12245638a8ec51b30b471ef"><a name="a629b6384e12245638a8ec51b30b471ef"></a><a name="a629b6384e12245638a8ec51b30b471ef"></a>Deleting user information</p>
</td>
<td class="cellrowborder" valign="top" width="27.07270727072707%" headers="mcps1.2.4.1.2 "><p id="ab82ca9803834414faa77d2d10b997a67"><a name="ab82ca9803834414faa77d2d10b997a67"></a><a name="ab82ca9803834414faa77d2d10b997a67"></a>workspace</p>
</td>
<td class="cellrowborder" valign="top" width="42.52425242524252%" headers="mcps1.2.4.1.3 "><p id="ae17adb8400254b329289c61ec4f19a5e"><a name="ae17adb8400254b329289c61ec4f19a5e"></a><a name="ae17adb8400254b329289c61ec4f19a5e"></a>deleteUser</p>
</td>
</tr>
<tr id="r0044fc949944470c9284131573228a83"><td class="cellrowborder" valign="top" width="30.403040304030405%" headers="mcps1.2.4.1.1 "><p id="abc250454a70143c896dd97db76043a6a"><a name="abc250454a70143c896dd97db76043a6a"></a><a name="abc250454a70143c896dd97db76043a6a"></a>Exporting user information</p>
</td>
<td class="cellrowborder" valign="top" width="27.07270727072707%" headers="mcps1.2.4.1.2 "><p id="a743ab8f693af49dd85e3b11d114b9f8b"><a name="a743ab8f693af49dd85e3b11d114b9f8b"></a><a name="a743ab8f693af49dd85e3b11d114b9f8b"></a>workspace</p>
</td>
<td class="cellrowborder" valign="top" width="42.52425242524252%" headers="mcps1.2.4.1.3 "><p id="adb36525d05ca45f2a3b43ab7a901d1c1"><a name="adb36525d05ca45f2a3b43ab7a901d1c1"></a><a name="adb36525d05ca45f2a3b43ab7a901d1c1"></a>exportUserInfo</p>
</td>
</tr>
<tr id="r6594f697680d422f9097eb7331335618"><td class="cellrowborder" valign="top" width="30.403040304030405%" headers="mcps1.2.4.1.1 "><p id="a997d1d8a6e6d43ff9c7294030c9338e9"><a name="a997d1d8a6e6d43ff9c7294030c9338e9"></a><a name="a997d1d8a6e6d43ff9c7294030c9338e9"></a>Unlocking a user</p>
</td>
<td class="cellrowborder" valign="top" width="27.07270727072707%" headers="mcps1.2.4.1.2 "><p id="a35825f53ac8b4837aab392cfae66b43a"><a name="a35825f53ac8b4837aab392cfae66b43a"></a><a name="a35825f53ac8b4837aab392cfae66b43a"></a>workspace</p>
</td>
<td class="cellrowborder" valign="top" width="42.52425242524252%" headers="mcps1.2.4.1.3 "><p id="aa509658b2ae84775b6b2134cfbb56bcd"><a name="aa509658b2ae84775b6b2134cfbb56bcd"></a><a name="aa509658b2ae84775b6b2134cfbb56bcd"></a>unlockUser</p>
</td>
</tr>
<tr id="rd5c9ab4d4e90472ba1abc76f2d9ce58e"><td class="cellrowborder" valign="top" width="30.403040304030405%" headers="mcps1.2.4.1.1 "><p id="a23caf25aa65a48739468b2bb346fe42a"><a name="a23caf25aa65a48739468b2bb346fe42a"></a><a name="a23caf25aa65a48739468b2bb346fe42a"></a>Resetting the password</p>
</td>
<td class="cellrowborder" valign="top" width="27.07270727072707%" headers="mcps1.2.4.1.2 "><p id="a70afd85d8f754bccb4dfc51702943ecf"><a name="a70afd85d8f754bccb4dfc51702943ecf"></a><a name="a70afd85d8f754bccb4dfc51702943ecf"></a>workspace</p>
</td>
<td class="cellrowborder" valign="top" width="42.52425242524252%" headers="mcps1.2.4.1.3 "><p id="a28fd6a1a7af84bf8b7542b7f289a7557"><a name="a28fd6a1a7af84bf8b7542b7f289a7557"></a><a name="a28fd6a1a7af84bf8b7542b7f289a7557"></a>resetUserPassword</p>
</td>
</tr>
<tr id="r6d7125ea95874f799ccfe5e38923817e"><td class="cellrowborder" valign="top" width="30.403040304030405%" headers="mcps1.2.4.1.1 "><p id="ad7440ed60b474142b9ab470b56665bb2"><a name="ad7440ed60b474142b9ab470b56665bb2"></a><a name="ad7440ed60b474142b9ab470b56665bb2"></a>Downloading a user template</p>
</td>
<td class="cellrowborder" valign="top" width="27.07270727072707%" headers="mcps1.2.4.1.2 "><p id="a7b9e77ad3b89406f87c39dd9c73a0686"><a name="a7b9e77ad3b89406f87c39dd9c73a0686"></a><a name="a7b9e77ad3b89406f87c39dd9c73a0686"></a>workspace</p>
</td>
<td class="cellrowborder" valign="top" width="42.52425242524252%" headers="mcps1.2.4.1.3 "><p id="a3bf9059592324d498865be1cd256448e"><a name="a3bf9059592324d498865be1cd256448e"></a><a name="a3bf9059592324d498865be1cd256448e"></a>downloadUserModel</p>
</td>
</tr>
<tr id="rd2ada7f495d742749b0f75256af04f5f"><td class="cellrowborder" valign="top" width="30.403040304030405%" headers="mcps1.2.4.1.1 "><p id="a6019bde40efd4c30b01720f9dc3e7feb"><a name="a6019bde40efd4c30b01720f9dc3e7feb"></a><a name="a6019bde40efd4c30b01720f9dc3e7feb"></a>Deleting an on-demand task</p>
</td>
<td class="cellrowborder" valign="top" width="27.07270727072707%" headers="mcps1.2.4.1.2 "><p id="a62d18abd2cbe408db5bb234592b01212"><a name="a62d18abd2cbe408db5bb234592b01212"></a><a name="a62d18abd2cbe408db5bb234592b01212"></a>workspace</p>
</td>
<td class="cellrowborder" valign="top" width="42.52425242524252%" headers="mcps1.2.4.1.3 "><p id="adbb2b691ff8d4586a96bc8791949a62e"><a name="adbb2b691ff8d4586a96bc8791949a62e"></a><a name="adbb2b691ff8d4586a96bc8791949a62e"></a>deleteJob</p>
</td>
</tr>
<tr id="r2990fd87a4c24fa4a1ee493865596f62"><td class="cellrowborder" valign="top" width="30.403040304030405%" headers="mcps1.2.4.1.1 "><p id="a0f8390d2c6ae4413886d2c6000c393d4"><a name="a0f8390d2c6ae4413886d2c6000c393d4"></a><a name="a0f8390d2c6ae4413886d2c6000c393d4"></a>Applying for modifying the password (the domain user)</p>
</td>
<td class="cellrowborder" valign="top" width="27.07270727072707%" headers="mcps1.2.4.1.2 "><p id="a4bd72d203eeb403992eaed922a1179dc"><a name="a4bd72d203eeb403992eaed922a1179dc"></a><a name="a4bd72d203eeb403992eaed922a1179dc"></a>workspace</p>
</td>
<td class="cellrowborder" valign="top" width="42.52425242524252%" headers="mcps1.2.4.1.3 "><p id="ad52dc4f1ba804c5b9daa3627916010da"><a name="ad52dc4f1ba804c5b9daa3627916010da"></a><a name="ad52dc4f1ba804c5b9daa3627916010da"></a>updateDomainUserPassword</p>
</td>
</tr>
<tr id="r8e62d4de379d4c45af3088c38085f53a"><td class="cellrowborder" valign="top" width="30.403040304030405%" headers="mcps1.2.4.1.1 "><p id="aaea3757d804d4173a33cde69603f2633"><a name="aaea3757d804d4173a33cde69603f2633"></a><a name="aaea3757d804d4173a33cde69603f2633"></a>Synchronizing the resource tenants (Identity and Access Management)</p>
</td>
<td class="cellrowborder" valign="top" width="27.07270727072707%" headers="mcps1.2.4.1.2 "><p id="a42bda0f4748644c49a1bb66f29c48dda"><a name="a42bda0f4748644c49a1bb66f29c48dda"></a><a name="a42bda0f4748644c49a1bb66f29c48dda"></a>workspace</p>
</td>
<td class="cellrowborder" valign="top" width="42.52425242524252%" headers="mcps1.2.4.1.3 "><p id="a8eabf129dc0e4064bdfc37301675d87b"><a name="a8eabf129dc0e4064bdfc37301675d87b"></a><a name="a8eabf129dc0e4064bdfc37301675d87b"></a>synIamResourceTenant</p>
</td>
</tr>
<tr id="rd0c4003f300d45ac9ebb40e26efc2b15"><td class="cellrowborder" valign="top" width="30.403040304030405%" headers="mcps1.2.4.1.1 "><p id="ab1f2b1af62b84bc3983c647f39c7bbc1"><a name="ab1f2b1af62b84bc3983c647f39c7bbc1"></a><a name="ab1f2b1af62b84bc3983c647f39c7bbc1"></a>Updating the policy group</p>
</td>
<td class="cellrowborder" valign="top" width="27.07270727072707%" headers="mcps1.2.4.1.2 "><p id="a6e802b8012154f9795cc9920bec1a7b1"><a name="a6e802b8012154f9795cc9920bec1a7b1"></a><a name="a6e802b8012154f9795cc9920bec1a7b1"></a>workspace</p>
</td>
<td class="cellrowborder" valign="top" width="42.52425242524252%" headers="mcps1.2.4.1.3 "><p id="a9c9e2868ba724653905e12a4046b4741"><a name="a9c9e2868ba724653905e12a4046b4741"></a><a name="a9c9e2868ba724653905e12a4046b4741"></a>updatePolicy</p>
</td>
</tr>
<tr id="rcaf1152c448d45cd8596932c6c5c4e0e"><td class="cellrowborder" valign="top" width="30.403040304030405%" headers="mcps1.2.4.1.1 "><p id="a92f01496ddd745a09264114180afea93"><a name="a92f01496ddd745a09264114180afea93"></a><a name="a92f01496ddd745a09264114180afea93"></a>Enabling Workspace</p>
</td>
<td class="cellrowborder" valign="top" width="27.07270727072707%" headers="mcps1.2.4.1.2 "><p id="a982c60fdd24a46559d7bc295df73a245"><a name="a982c60fdd24a46559d7bc295df73a245"></a><a name="a982c60fdd24a46559d7bc295df73a245"></a>workspace</p>
</td>
<td class="cellrowborder" valign="top" width="42.52425242524252%" headers="mcps1.2.4.1.3 "><p id="a24fefe19296a41f8afdb39de304a9ba6"><a name="a24fefe19296a41f8afdb39de304a9ba6"></a><a name="a24fefe19296a41f8afdb39de304a9ba6"></a>openService</p>
</td>
</tr>
<tr id="rfe257bbebde2438e87cef00568f429f8"><td class="cellrowborder" valign="top" width="30.403040304030405%" headers="mcps1.2.4.1.1 "><p id="aff0298bcb3ee4371a1dd44c60e6d5d35"><a name="aff0298bcb3ee4371a1dd44c60e6d5d35"></a><a name="aff0298bcb3ee4371a1dd44c60e6d5d35"></a>Changing the domain password</p>
</td>
<td class="cellrowborder" valign="top" width="27.07270727072707%" headers="mcps1.2.4.1.2 "><p id="a9202b5b218644899afc1dbaa1e340104"><a name="a9202b5b218644899afc1dbaa1e340104"></a><a name="a9202b5b218644899afc1dbaa1e340104"></a>workspace</p>
</td>
<td class="cellrowborder" valign="top" width="42.52425242524252%" headers="mcps1.2.4.1.3 "><p id="ab55250c768b444b4b9d6c9f1ffb468a3"><a name="ab55250c768b444b4b9d6c9f1ffb468a3"></a><a name="ab55250c768b444b4b9d6c9f1ffb468a3"></a>updateAdPwd</p>
</td>
</tr>
<tr id="r13905fbbff34435ca3a65759a7d87717"><td class="cellrowborder" valign="top" width="30.403040304030405%" headers="mcps1.2.4.1.1 "><p id="ae0c9abaab3e14b7abb9b6bdcb03c080b"><a name="ae0c9abaab3e14b7abb9b6bdcb03c080b"></a><a name="ae0c9abaab3e14b7abb9b6bdcb03c080b"></a>Disabling Workspace</p>
</td>
<td class="cellrowborder" valign="top" width="27.07270727072707%" headers="mcps1.2.4.1.2 "><p id="ad062a5f6148b4516ae731e0a4a7fd9ab"><a name="ad062a5f6148b4516ae731e0a4a7fd9ab"></a><a name="ad062a5f6148b4516ae731e0a4a7fd9ab"></a>workspace</p>
</td>
<td class="cellrowborder" valign="top" width="42.52425242524252%" headers="mcps1.2.4.1.3 "><p id="ab64a87b20ce643928a39e058b5ac4084"><a name="ab64a87b20ce643928a39e058b5ac4084"></a><a name="ab64a87b20ce643928a39e058b5ac4084"></a>tenantClose</p>
</td>
</tr>
<tr id="rb917fda7745b4fc18f7ef30494eb4664"><td class="cellrowborder" valign="top" width="30.403040304030405%" headers="mcps1.2.4.1.1 "><p id="af2734227a5fe4f27908af58a52bb7ebc"><a name="af2734227a5fe4f27908af58a52bb7ebc"></a><a name="af2734227a5fe4f27908af58a52bb7ebc"></a>Retrying failed Workspace enabling and disabling tasks</p>
</td>
<td class="cellrowborder" valign="top" width="27.07270727072707%" headers="mcps1.2.4.1.2 "><p id="a5a5dbba9238746dc92d8a7bd56ef0910"><a name="a5a5dbba9238746dc92d8a7bd56ef0910"></a><a name="a5a5dbba9238746dc92d8a7bd56ef0910"></a>workspace</p>
</td>
<td class="cellrowborder" valign="top" width="42.52425242524252%" headers="mcps1.2.4.1.3 "><p id="a3aae9c97deb44799a5494e2f453dd3e1"><a name="a3aae9c97deb44799a5494e2f453dd3e1"></a><a name="a3aae9c97deb44799a5494e2f453dd3e1"></a>tenantRetryServiceTask</p>
</td>
</tr>
<tr id="r5f3aba2125bf4481b663b22ec24851d6"><td class="cellrowborder" valign="top" width="30.403040304030405%" headers="mcps1.2.4.1.1 "><p id="a22e0f94d4969462db8c5c97981b06883"><a name="a22e0f94d4969462db8c5c97981b06883"></a><a name="a22e0f94d4969462db8c5c97981b06883"></a>Restoring the infrastructure VM</p>
</td>
<td class="cellrowborder" valign="top" width="27.07270727072707%" headers="mcps1.2.4.1.2 "><p id="a2acd7e4f5d5449a083bc182fe3f581fe"><a name="a2acd7e4f5d5449a083bc182fe3f581fe"></a><a name="a2acd7e4f5d5449a083bc182fe3f581fe"></a>workspace</p>
</td>
<td class="cellrowborder" valign="top" width="42.52425242524252%" headers="mcps1.2.4.1.3 "><p id="ac4e6a577ae4f4518af8d1a7dc110b97b"><a name="ac4e6a577ae4f4518af8d1a7dc110b97b"></a><a name="ac4e6a577ae4f4518af8d1a7dc110b97b"></a>restoreManagerVmBackup</p>
</td>
</tr>
<tr id="r0be48da09aaf4d6282836fb92f6f4d95"><td class="cellrowborder" valign="top" width="30.403040304030405%" headers="mcps1.2.4.1.1 "><p id="a72a03a061ebf42c0b096ada1905c1e52"><a name="a72a03a061ebf42c0b096ada1905c1e52"></a><a name="a72a03a061ebf42c0b096ada1905c1e52"></a>Modifying the desktop attributes</p>
</td>
<td class="cellrowborder" valign="top" width="27.07270727072707%" headers="mcps1.2.4.1.2 "><p id="a9aa1bfc774414903ac97803a34cf24b3"><a name="a9aa1bfc774414903ac97803a34cf24b3"></a><a name="a9aa1bfc774414903ac97803a34cf24b3"></a>workspace</p>
</td>
<td class="cellrowborder" valign="top" width="42.52425242524252%" headers="mcps1.2.4.1.3 "><p id="a30de5f7d1ad640f09bc9eaca6d6aff4c"><a name="a30de5f7d1ad640f09bc9eaca6d6aff4c"></a><a name="a30de5f7d1ad640f09bc9eaca6d6aff4c"></a>modifyDesktopAttributes</p>
</td>
</tr>
<tr id="rb332e758db7f466bb64694053040d96f"><td class="cellrowborder" valign="top" width="30.403040304030405%" headers="mcps1.2.4.1.1 "><p id="a7183d27b23444340a15bcc7ddb3fcfa4"><a name="a7183d27b23444340a15bcc7ddb3fcfa4"></a><a name="a7183d27b23444340a15bcc7ddb3fcfa4"></a>Updating the domain name</p>
</td>
<td class="cellrowborder" valign="top" width="27.07270727072707%" headers="mcps1.2.4.1.2 "><p id="aa775863914cb485bbf97f741e737b493"><a name="aa775863914cb485bbf97f741e737b493"></a><a name="aa775863914cb485bbf97f741e737b493"></a>workspace</p>
</td>
<td class="cellrowborder" valign="top" width="42.52425242524252%" headers="mcps1.2.4.1.3 "><p id="ac7e757256b56439897ed224bf62620ca"><a name="ac7e757256b56439897ed224bf62620ca"></a><a name="ac7e757256b56439897ed224bf62620ca"></a>updateRecordSet</p>
</td>
</tr>
</tbody>
</table>


# Key Operations on IMS<a name="en-us_topic_0100236047"></a>

Image Management Service \(IMS\) provides easy and convenient image management. You can use a public or private image to create an ECS. You can also create a private image using an ECS or an external image file.

With CTS, you can record operations associated with IMS for future query, audit, and backtrack operations.

**Table  1**  IMS operations that can be recorded by CTS

<a name="table30216176152351"></a>
<table><thead align="left"><tr id="r24a7c521090a4f9582cde9233b0fddb4"><th class="cellrowborder" valign="top" width="25.430000000000003%" id="mcps1.2.4.1.1"><p id="a06c79d9abeb64efc88fda32dfc49329a"><a name="a06c79d9abeb64efc88fda32dfc49329a"></a><a name="a06c79d9abeb64efc88fda32dfc49329a"></a><strong id="b842352706103557"><a name="b842352706103557"></a><a name="b842352706103557"></a>Operation</strong></p>
</th>
<th class="cellrowborder" valign="top" width="34.78%" id="mcps1.2.4.1.2"><p id="ac4fb23b3248346c4830a6c354a8ddf40"><a name="ac4fb23b3248346c4830a6c354a8ddf40"></a><a name="ac4fb23b3248346c4830a6c354a8ddf40"></a><strong id="b84235270610360"><a name="b84235270610360"></a><a name="b84235270610360"></a>Resource Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.79%" id="mcps1.2.4.1.3"><p id="ac0df6ba904f44e1e9724bd48c8dcae1f"><a name="ac0df6ba904f44e1e9724bd48c8dcae1f"></a><a name="ac0df6ba904f44e1e9724bd48c8dcae1f"></a><strong id="b842352706182955"><a name="b842352706182955"></a><a name="b842352706182955"></a>Trace Name</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r0f13d2aa9f7d41d9ac2ce53312a31a86"><td class="cellrowborder" valign="top" width="25.430000000000003%" headers="mcps1.2.4.1.1 "><p id="aee64c52613004576b71ceb3da7099776"><a name="aee64c52613004576b71ceb3da7099776"></a><a name="aee64c52613004576b71ceb3da7099776"></a>Creating an image</p>
</td>
<td class="cellrowborder" valign="top" width="34.78%" headers="mcps1.2.4.1.2 "><p id="a7fe34a002b4d431aacf2405560586738"><a name="a7fe34a002b4d431aacf2405560586738"></a><a name="a7fe34a002b4d431aacf2405560586738"></a>ims</p>
</td>
<td class="cellrowborder" valign="top" width="39.79%" headers="mcps1.2.4.1.3 "><p id="a76ef900cf70146c7985b5d5d2b9b4d7e"><a name="a76ef900cf70146c7985b5d5d2b9b4d7e"></a><a name="a76ef900cf70146c7985b5d5d2b9b4d7e"></a>createImage</p>
</td>
</tr>
<tr id="r53d48c46bc55413b9b1eafc7c126dc33"><td class="cellrowborder" valign="top" width="25.430000000000003%" headers="mcps1.2.4.1.1 "><p id="ac9055e7de1e54f1e8065df9c61f810c9"><a name="ac9055e7de1e54f1e8065df9c61f810c9"></a><a name="ac9055e7de1e54f1e8065df9c61f810c9"></a>Modifying an image</p>
</td>
<td class="cellrowborder" valign="top" width="34.78%" headers="mcps1.2.4.1.2 "><p id="ac451afb71b684ca7bbed47740b32c425"><a name="ac451afb71b684ca7bbed47740b32c425"></a><a name="ac451afb71b684ca7bbed47740b32c425"></a>ims</p>
</td>
<td class="cellrowborder" valign="top" width="39.79%" headers="mcps1.2.4.1.3 "><p id="ac85cae18d2184343ad8d6dfc62b6ec00"><a name="ac85cae18d2184343ad8d6dfc62b6ec00"></a><a name="ac85cae18d2184343ad8d6dfc62b6ec00"></a>updateImage</p>
</td>
</tr>
<tr id="r6cc45701d9904d0cb51cb2f02025c5b7"><td class="cellrowborder" valign="top" width="25.430000000000003%" headers="mcps1.2.4.1.1 "><p id="aac60dc974bf84940b0849be37a9c2c15"><a name="aac60dc974bf84940b0849be37a9c2c15"></a><a name="aac60dc974bf84940b0849be37a9c2c15"></a>Deleting images in batches</p>
</td>
<td class="cellrowborder" valign="top" width="34.78%" headers="mcps1.2.4.1.2 "><p id="aa23006c48a4a437599361791d9b229cb"><a name="aa23006c48a4a437599361791d9b229cb"></a><a name="aa23006c48a4a437599361791d9b229cb"></a>ims</p>
</td>
<td class="cellrowborder" valign="top" width="39.79%" headers="mcps1.2.4.1.3 "><p id="a4a88e5dd63c143f8877c9deb37b3008d"><a name="a4a88e5dd63c143f8877c9deb37b3008d"></a><a name="a4a88e5dd63c143f8877c9deb37b3008d"></a>deleteImage</p>
</td>
</tr>
<tr id="r27427b607278461ab777e92aaec44245"><td class="cellrowborder" valign="top" width="25.430000000000003%" headers="mcps1.2.4.1.1 "><p id="aa52db0352e674718b1d70dbf51471586"><a name="aa52db0352e674718b1d70dbf51471586"></a><a name="aa52db0352e674718b1d70dbf51471586"></a>Copying an image</p>
</td>
<td class="cellrowborder" valign="top" width="34.78%" headers="mcps1.2.4.1.2 "><p id="a8b409972b65f477f9df3b6a965a10081"><a name="a8b409972b65f477f9df3b6a965a10081"></a><a name="a8b409972b65f477f9df3b6a965a10081"></a>ims</p>
</td>
<td class="cellrowborder" valign="top" width="39.79%" headers="mcps1.2.4.1.3 "><p id="a67a0b1d69b2741fc8fe9a8c261e0e865"><a name="a67a0b1d69b2741fc8fe9a8c261e0e865"></a><a name="a67a0b1d69b2741fc8fe9a8c261e0e865"></a>copyImage</p>
</td>
</tr>
<tr id="r1b2ffef365d64672877e8f0713d6bcac"><td class="cellrowborder" valign="top" width="25.430000000000003%" headers="mcps1.2.4.1.1 "><p id="a08b307d9af314ec6b8b0281eaaf5aecc"><a name="a08b307d9af314ec6b8b0281eaaf5aecc"></a><a name="a08b307d9af314ec6b8b0281eaaf5aecc"></a>Exporting an image</p>
</td>
<td class="cellrowborder" valign="top" width="34.78%" headers="mcps1.2.4.1.2 "><p id="a9b8c2e6848404cd6bdb4ec6559f6d9de"><a name="a9b8c2e6848404cd6bdb4ec6559f6d9de"></a><a name="a9b8c2e6848404cd6bdb4ec6559f6d9de"></a>ims</p>
</td>
<td class="cellrowborder" valign="top" width="39.79%" headers="mcps1.2.4.1.3 "><p id="a949619d44c434648bc163911595cc797"><a name="a949619d44c434648bc163911595cc797"></a><a name="a949619d44c434648bc163911595cc797"></a>exportImage</p>
</td>
</tr>
<tr id="r3cb55fb9319c4ff79d99343d274c77cc"><td class="cellrowborder" valign="top" width="25.430000000000003%" headers="mcps1.2.4.1.1 "><p id="a2dbe1c778707470597a426ac5d0c9143"><a name="a2dbe1c778707470597a426ac5d0c9143"></a><a name="a2dbe1c778707470597a426ac5d0c9143"></a>Adding a member</p>
</td>
<td class="cellrowborder" valign="top" width="34.78%" headers="mcps1.2.4.1.2 "><p id="a9602d013117646a4b9a25e664aa1ff04"><a name="a9602d013117646a4b9a25e664aa1ff04"></a><a name="a9602d013117646a4b9a25e664aa1ff04"></a>ims</p>
</td>
<td class="cellrowborder" valign="top" width="39.79%" headers="mcps1.2.4.1.3 "><p id="ae4a1da94091a400c82453bbd855a333a"><a name="ae4a1da94091a400c82453bbd855a333a"></a><a name="ae4a1da94091a400c82453bbd855a333a"></a>addMember</p>
</td>
</tr>
<tr id="re3d3cba9f27142ecbdc7be06740b3f01"><td class="cellrowborder" valign="top" width="25.430000000000003%" headers="mcps1.2.4.1.1 "><p id="a96645e41e2ac463e811b2803dec7c472"><a name="a96645e41e2ac463e811b2803dec7c472"></a><a name="a96645e41e2ac463e811b2803dec7c472"></a>Modifying members in batches</p>
</td>
<td class="cellrowborder" valign="top" width="34.78%" headers="mcps1.2.4.1.2 "><p id="aca2d6c719f7c453bbd2fcc27f847e1e9"><a name="aca2d6c719f7c453bbd2fcc27f847e1e9"></a><a name="aca2d6c719f7c453bbd2fcc27f847e1e9"></a>ims</p>
</td>
<td class="cellrowborder" valign="top" width="39.79%" headers="mcps1.2.4.1.3 "><p id="a01d3292ac7bf46daac9d901979a5bb9d"><a name="a01d3292ac7bf46daac9d901979a5bb9d"></a><a name="a01d3292ac7bf46daac9d901979a5bb9d"></a>updateMember</p>
</td>
</tr>
<tr id="r78daa1c8577940109a1cbd8b5111fdc9"><td class="cellrowborder" valign="top" width="25.430000000000003%" headers="mcps1.2.4.1.1 "><p id="a07ae0ce21ba5446781cc624ef33f09a5"><a name="a07ae0ce21ba5446781cc624ef33f09a5"></a><a name="a07ae0ce21ba5446781cc624ef33f09a5"></a>Deleting members in batches</p>
</td>
<td class="cellrowborder" valign="top" width="34.78%" headers="mcps1.2.4.1.2 "><p id="aaa10e17d522f4968a4ee7f4f15dbe0db"><a name="aaa10e17d522f4968a4ee7f4f15dbe0db"></a><a name="aaa10e17d522f4968a4ee7f4f15dbe0db"></a>ims</p>
</td>
<td class="cellrowborder" valign="top" width="39.79%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0100240378_p37834193922"><a name="en-us_topic_0100240378_p37834193922"></a><a name="en-us_topic_0100240378_p37834193922"></a>deleteMember</p>
</td>
</tr>
</tbody>
</table>


# DB Instance Statuses<a name="en-us_topic_0032472291"></a>

## DB Instance Statuses<a name="sc3b964fa7fb546c4a5de6d2232f2eed3"></a>

The status of a DB instance indicates the health of the DB instance. You can use the management console or API to view the status of a DB instance.

**Table  1**  DB instance statuses

<a name="ta8e30128dae74adba4d88ae180288ac5"></a>
<table><thead align="left"><tr id="r2aaeaca2ae2a4cb5b9fbb49e5f0be784"><th class="cellrowborder" valign="top" width="22.42%" id="mcps1.2.3.1.1"><p id="acac809fed8be41ef99fe6170d519f402"><a name="acac809fed8be41ef99fe6170d519f402"></a><a name="acac809fed8be41ef99fe6170d519f402"></a><strong id="a09e05ecaf5dc42b49282b47838f2b407"><a name="a09e05ecaf5dc42b49282b47838f2b407"></a><a name="a09e05ecaf5dc42b49282b47838f2b407"></a>Status</strong></p>
</th>
<th class="cellrowborder" valign="top" width="77.58%" id="mcps1.2.3.1.2"><p id="ae4e7c52e4cd64669b9d8ddbe2fcf1001"><a name="ae4e7c52e4cd64669b9d8ddbe2fcf1001"></a><a name="ae4e7c52e4cd64669b9d8ddbe2fcf1001"></a><strong id="a97668864bf874d57b57a1c1492147784"><a name="a97668864bf874d57b57a1c1492147784"></a><a name="a97668864bf874d57b57a1c1492147784"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r2b715a4b06d4496187d21c3c88a2415b"><td class="cellrowborder" valign="top" width="22.42%" headers="mcps1.2.3.1.1 "><p id="accdc25b04b4047508a13e07b900a9646"><a name="accdc25b04b4047508a13e07b900a9646"></a><a name="accdc25b04b4047508a13e07b900a9646"></a>Available</p>
</td>
<td class="cellrowborder" valign="top" width="77.58%" headers="mcps1.2.3.1.2 "><p id="a49aa47c257a141ecbae664a8c93ec72a"><a name="a49aa47c257a141ecbae664a8c93ec72a"></a><a name="a49aa47c257a141ecbae664a8c93ec72a"></a>DB instance is available.</p>
</td>
</tr>
<tr id="rdc652434ec1b42239e0659c0ff1eebe4"><td class="cellrowborder" valign="top" width="22.42%" headers="mcps1.2.3.1.1 "><p id="a2fcdb91ffa7f412790c529def0d09354"><a name="a2fcdb91ffa7f412790c529def0d09354"></a><a name="a2fcdb91ffa7f412790c529def0d09354"></a>Abnormal</p>
</td>
<td class="cellrowborder" valign="top" width="77.58%" headers="mcps1.2.3.1.2 "><p id="a66fa42cfeefe4bb49b3d2852fed43c5d"><a name="a66fa42cfeefe4bb49b3d2852fed43c5d"></a><a name="a66fa42cfeefe4bb49b3d2852fed43c5d"></a>DB instance is abnormal.</p>
</td>
</tr>
<tr id="r75f245ae4f3f49ee9f57da5f4ffae2e7"><td class="cellrowborder" valign="top" width="22.42%" headers="mcps1.2.3.1.1 "><p id="a07f39b184b8e47f589cb110b159bc085"><a name="a07f39b184b8e47f589cb110b159bc085"></a><a name="a07f39b184b8e47f589cb110b159bc085"></a>Creating</p>
</td>
<td class="cellrowborder" valign="top" width="77.58%" headers="mcps1.2.3.1.2 "><p id="a64a5bd8080f24c2694b2090070917e9b"><a name="a64a5bd8080f24c2694b2090070917e9b"></a><a name="a64a5bd8080f24c2694b2090070917e9b"></a>DB instance or backup is being created.</p>
</td>
</tr>
<tr id="r62d49a4bc1444393856cceb41fb833a2"><td class="cellrowborder" valign="top" width="22.42%" headers="mcps1.2.3.1.1 "><p id="af90c5bc98fbf4a27a92f89e751b49664"><a name="af90c5bc98fbf4a27a92f89e751b49664"></a><a name="af90c5bc98fbf4a27a92f89e751b49664"></a>Creation failed</p>
</td>
<td class="cellrowborder" valign="top" width="77.58%" headers="mcps1.2.3.1.2 "><p id="a4f12fb7689be4473a4767fe050fd2aff"><a name="a4f12fb7689be4473a4767fe050fd2aff"></a><a name="a4f12fb7689be4473a4767fe050fd2aff"></a>DB instance has failed to be created.</p>
</td>
</tr>
<tr id="r5e4c08a5de1f4cd9b3b8578b1996c3cd"><td class="cellrowborder" valign="top" width="22.42%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0086557181_p997227116366"><a name="en-us_topic_0086557181_p997227116366"></a><a name="en-us_topic_0086557181_p997227116366"></a>Switchover in progress</p>
</td>
<td class="cellrowborder" valign="top" width="77.58%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0086557181_p244758916366"><a name="en-us_topic_0086557181_p244758916366"></a><a name="en-us_topic_0086557181_p244758916366"></a>Standby DB instance is being switched over to the primary DB instance.</p>
</td>
</tr>
<tr id="row8551910191517"><td class="cellrowborder" valign="top" width="22.42%" headers="mcps1.2.3.1.1 "><p id="p755141019154"><a name="p755141019154"></a><a name="p755141019154"></a>Changing type to primary/standby</p>
</td>
<td class="cellrowborder" valign="top" width="77.58%" headers="mcps1.2.3.1.2 "><p id="p15512010151516"><a name="p15512010151516"></a><a name="p15512010151516"></a>Single DB instance is being changed to primary/standby DB instances.</p>
</td>
</tr>
<tr id="rf33f49489d854ce8a1e6bcd2aee15978"><td class="cellrowborder" valign="top" width="22.42%" headers="mcps1.2.3.1.1 "><p id="aef96ea708e1e42d086b2155019bd01a4"><a name="aef96ea708e1e42d086b2155019bd01a4"></a><a name="aef96ea708e1e42d086b2155019bd01a4"></a>Rebooting</p>
</td>
<td class="cellrowborder" valign="top" width="77.58%" headers="mcps1.2.3.1.2 "><p id="a8dd46f4afd02432cb9d967fc44131dff"><a name="a8dd46f4afd02432cb9d967fc44131dff"></a><a name="a8dd46f4afd02432cb9d967fc44131dff"></a>DB instance is rebooting because of a user request or a modification that requires a reboot for the changes to take effect.</p>
</td>
</tr>
<tr id="r4b7759fc518946cabe372836b292dc5d"><td class="cellrowborder" valign="top" width="22.42%" headers="mcps1.2.3.1.1 "><p id="a8cdd715f9b0d4248ac24620085706d0c"><a name="a8cdd715f9b0d4248ac24620085706d0c"></a><a name="a8cdd715f9b0d4248ac24620085706d0c"></a>Changing port</p>
</td>
<td class="cellrowborder" valign="top" width="77.58%" headers="mcps1.2.3.1.2 "><p id="a884e93dcaf05469c99cc1b7abfe93ca4"><a name="a884e93dcaf05469c99cc1b7abfe93ca4"></a><a name="a884e93dcaf05469c99cc1b7abfe93ca4"></a>DB instance port is being changed.</p>
</td>
</tr>
<tr id="ra68e3373eb36424fa178a25a99464216"><td class="cellrowborder" valign="top" width="22.42%" headers="mcps1.2.3.1.1 "><p id="a5fcb1bb40c1249e3b3e44ca400870275"><a name="a5fcb1bb40c1249e3b3e44ca400870275"></a><a name="a5fcb1bb40c1249e3b3e44ca400870275"></a>Changing instance class</p>
</td>
<td class="cellrowborder" valign="top" width="77.58%" headers="mcps1.2.3.1.2 "><p id="acd55e347b56a4a7d8233da0a6311031e"><a name="acd55e347b56a4a7d8233da0a6311031e"></a><a name="acd55e347b56a4a7d8233da0a6311031e"></a>CPU or memory of a DB instance is being modified.</p>
</td>
</tr>
<tr id="re4116bb501694c3b976ba287856cff3d"><td class="cellrowborder" valign="top" width="22.42%" headers="mcps1.2.3.1.1 "><p id="ada41ff2498eb4bd6a9ccc1a9a8167860"><a name="ada41ff2498eb4bd6a9ccc1a9a8167860"></a><a name="ada41ff2498eb4bd6a9ccc1a9a8167860"></a>Scaling up</p>
</td>
<td class="cellrowborder" valign="top" width="77.58%" headers="mcps1.2.3.1.2 "><p id="a1b6f7026d9384c8b835745cdf0fe2101"><a name="a1b6f7026d9384c8b835745cdf0fe2101"></a><a name="a1b6f7026d9384c8b835745cdf0fe2101"></a>Storage space of a DB instance is being scaled up.</p>
</td>
</tr>
<tr id="r5bb1a9ec9bd843bfa4635374a2f3ec7b"><td class="cellrowborder" valign="top" width="22.42%" headers="mcps1.2.3.1.1 "><p id="a87a1e3b149f34514ac34f8812b2783b1"><a name="a87a1e3b149f34514ac34f8812b2783b1"></a><a name="a87a1e3b149f34514ac34f8812b2783b1"></a>Restoring</p>
</td>
<td class="cellrowborder" valign="top" width="77.58%" headers="mcps1.2.3.1.2 "><p id="a30bc1e86884441e09b97f72f05ad845f"><a name="a30bc1e86884441e09b97f72f05ad845f"></a><a name="a30bc1e86884441e09b97f72f05ad845f"></a>DB instance is being restored from a backup.</p>
</td>
</tr>
<tr id="rbfffff6b57fe4737ad0d6f6ad6e334bb"><td class="cellrowborder" valign="top" width="22.42%" headers="mcps1.2.3.1.1 "><p id="a1e1ba26f8613432a8658f447c5a67e61"><a name="a1e1ba26f8613432a8658f447c5a67e61"></a><a name="a1e1ba26f8613432a8658f447c5a67e61"></a>Restore failed</p>
</td>
<td class="cellrowborder" valign="top" width="77.58%" headers="mcps1.2.3.1.2 "><p id="aee32b8223cbc4203889d5484b2bc0b53"><a name="aee32b8223cbc4203889d5484b2bc0b53"></a><a name="aee32b8223cbc4203889d5484b2bc0b53"></a>DB instance fails to be restored.</p>
</td>
</tr>
<tr id="row16772491664"><td class="cellrowborder" valign="top" width="22.42%" headers="mcps1.2.3.1.1 "><p id="p142491329556"><a name="p142491329556"></a><a name="p142491329556"></a>Storage full</p>
</td>
<td class="cellrowborder" valign="top" width="77.58%" headers="mcps1.2.3.1.2 "><p id="p17781849464"><a name="p17781849464"></a><a name="p17781849464"></a>Storage space of the DB instance is full. Data cannot be written to databases.</p>
</td>
</tr>
<tr id="row15951182011120"><td class="cellrowborder" valign="top" width="22.42%" headers="mcps1.2.3.1.1 "><p id="p179511420191215"><a name="p179511420191215"></a><a name="p179511420191215"></a>Deleted</p>
</td>
<td class="cellrowborder" valign="top" width="77.58%" headers="mcps1.2.3.1.2 "><p id="p189511420151213"><a name="p189511420151213"></a><a name="p189511420151213"></a>DB instance has been deleted and will not be displayed in the instance list.</p>
</td>
</tr>
</tbody>
</table>

## Parameter Template Statuses<a name="sf14afc99d1fe4941b44ffca460288867"></a>

You can use the management console or API to view the status of a parameter template after parameters are modified.

**Table  2**  Parameter template statuses

<a name="t9a2b502da1bb4bc994469557920ee8d7"></a>
<table><thead align="left"><tr id="rd92b1040908f4f9ead560221e858ea56"><th class="cellrowborder" valign="top" width="23.49%" id="mcps1.2.3.1.1"><p id="a01254283ec57435c906025b4b81ac05f"><a name="a01254283ec57435c906025b4b81ac05f"></a><a name="a01254283ec57435c906025b4b81ac05f"></a><strong id="a85426a60330342b79c20fb9575072518"><a name="a85426a60330342b79c20fb9575072518"></a><a name="a85426a60330342b79c20fb9575072518"></a>Status</strong></p>
</th>
<th class="cellrowborder" valign="top" width="76.51%" id="mcps1.2.3.1.2"><p id="a78186c7fff2045b2b4855dfdb4db9f70"><a name="a78186c7fff2045b2b4855dfdb4db9f70"></a><a name="a78186c7fff2045b2b4855dfdb4db9f70"></a><strong id="a0053402df05f4db2bd0ce219cec017f6"><a name="a0053402df05f4db2bd0ce219cec017f6"></a><a name="a0053402df05f4db2bd0ce219cec017f6"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r7c57cd8024e34c3aa94827d4ae0e41e3"><td class="cellrowborder" valign="top" width="23.49%" headers="mcps1.2.3.1.1 "><p id="a8604e15d685b4505b12e7bfded1007fd"><a name="a8604e15d685b4505b12e7bfded1007fd"></a><a name="a8604e15d685b4505b12e7bfded1007fd"></a>In-sync</p>
</td>
<td class="cellrowborder" valign="top" width="76.51%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0086557181_p416995414358"><a name="en-us_topic_0086557181_p416995414358"></a><a name="en-us_topic_0086557181_p416995414358"></a>A database parameter has taken effect.</p>
</td>
</tr>
<tr id="rf4f5a03db63f4127b87e0994f89ebd36"><td class="cellrowborder" valign="top" width="23.49%" headers="mcps1.2.3.1.1 "><p id="a6525432e289247d39811ce2598d1c0bb"><a name="a6525432e289247d39811ce2598d1c0bb"></a><a name="a6525432e289247d39811ce2598d1c0bb"></a>Applying</p>
</td>
<td class="cellrowborder" valign="top" width="76.51%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0086557181_p924166714358"><a name="en-us_topic_0086557181_p924166714358"></a><a name="en-us_topic_0086557181_p924166714358"></a>A modification to a database parameter is being applied.</p>
</td>
</tr>
<tr id="ra825e06d59594087907c2ce1c376cc7c"><td class="cellrowborder" valign="top" width="23.49%" headers="mcps1.2.3.1.1 "><p id="ad78463f4003a409aaf247a6e6439b8e7"><a name="ad78463f4003a409aaf247a6e6439b8e7"></a><a name="ad78463f4003a409aaf247a6e6439b8e7"></a>Pending reboot</p>
</td>
<td class="cellrowborder" valign="top" width="76.51%" headers="mcps1.2.3.1.2 "><p id="a8c26b6df02894dc9b678ecc3b729a30b"><a name="a8c26b6df02894dc9b678ecc3b729a30b"></a><a name="a8c26b6df02894dc9b678ecc3b729a30b"></a>A modification to a database parameter is waiting for a DB instance to reboot before it can take effect.</p>
</td>
</tr>
</tbody>
</table>


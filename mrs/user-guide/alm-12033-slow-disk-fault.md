# ALM-12033 Slow Disk Fault<a name="EN-US_TOPIC_0125375264"></a>

## Description<a name="sa3456429e3934897b92647525eb54d32"></a>

The system runs the  **iostat** command every second to monitor the disk I/O indicator. This alarm is generated when the **svctm**  value exceeds 100 ms more than 30 times in 60 seconds, which indicates that the disk is faulty.

This alarm is automatically cleared after the disk is replaced.

## Attribute<a name="s8cd1b072b54f471bb5c868c04d3cd243"></a>

<a name="tf42f69e0aa2a42fcaccf3a6458a6adf9"></a>
<table><thead align="left"><tr id="r013db514c70b460a91b02fc619937525"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="aff355f41e67b4af08515f4c6e86b1b64"><a name="aff355f41e67b4af08515f4c6e86b1b64"></a><a name="aff355f41e67b4af08515f4c6e86b1b64"></a><strong id="a3c291f31b945479cb2ab4f5ef57d4976"><a name="a3c291f31b945479cb2ab4f5ef57d4976"></a><a name="a3c291f31b945479cb2ab4f5ef57d4976"></a>Alarm ID</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="a7bb97a8c8d1b4f51acc7d8fdf1fa91f2"><a name="a7bb97a8c8d1b4f51acc7d8fdf1fa91f2"></a><a name="a7bb97a8c8d1b4f51acc7d8fdf1fa91f2"></a><strong id="a23a7ba66a70e4318a14259a5dce95dbf"><a name="a23a7ba66a70e4318a14259a5dce95dbf"></a><a name="a23a7ba66a70e4318a14259a5dce95dbf"></a>Alarm Severity</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="en-us_topic_0035512807_p542052114212"><a name="en-us_topic_0035512807_p542052114212"></a><a name="en-us_topic_0035512807_p542052114212"></a><strong id="a9f4a6e7a9eac4e648433952e68e0b9be"><a name="a9f4a6e7a9eac4e648433952e68e0b9be"></a><a name="a9f4a6e7a9eac4e648433952e68e0b9be"></a>Automatically Cleared</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r284f709fd1cf4382841eaead8caba4f0"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="a5b1de716c50d4deca598ec8906a27f65"><a name="a5b1de716c50d4deca598ec8906a27f65"></a><a name="a5b1de716c50d4deca598ec8906a27f65"></a>12033</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="a3a36114b505b44b99ae9d0b3d7e66d53"><a name="a3a36114b505b44b99ae9d0b3d7e66d53"></a><a name="a3a36114b505b44b99ae9d0b3d7e66d53"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="a776d7c32a8604ab0b0ab3ccca1d5476a"><a name="a776d7c32a8604ab0b0ab3ccca1d5476a"></a><a name="a776d7c32a8604ab0b0ab3ccca1d5476a"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s30f6f787dc2f47efb7d5633fecef4ebc"></a>

<a name="tff394b24ec1049c0834ef0ad4011b46b"></a>
<table><thead align="left"><tr id="rbf58e9b19349479cb3f544f90c0b364a"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="a602fdec9c1964723a0d9f13abe4b4725"><a name="a602fdec9c1964723a0d9f13abe4b4725"></a><a name="a602fdec9c1964723a0d9f13abe4b4725"></a><strong id="a1b28423a59bb4f5f9fc54a083aa007d1"><a name="a1b28423a59bb4f5f9fc54a083aa007d1"></a><a name="a1b28423a59bb4f5f9fc54a083aa007d1"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="a5e1263c6a54242fea51af46914f9b5d8"><a name="a5e1263c6a54242fea51af46914f9b5d8"></a><a name="a5e1263c6a54242fea51af46914f9b5d8"></a><strong id="ad41a62a5b34445098e3c31fe370af4ec"><a name="ad41a62a5b34445098e3c31fe370af4ec"></a><a name="ad41a62a5b34445098e3c31fe370af4ec"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r0d2c67d2dc1c4547ba278150dd9d4fc5"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a39cd31656bbc41b89c931a7297829d6b"><a name="a39cd31656bbc41b89c931a7297829d6b"></a><a name="a39cd31656bbc41b89c931a7297829d6b"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a60fef7c7d3224deb8be8ba449b71ad38"><a name="a60fef7c7d3224deb8be8ba449b71ad38"></a><a name="a60fef7c7d3224deb8be8ba449b71ad38"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="rc56e5aea5759460fa058f24e509ecf83"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="ae227f28ea9d74cd7bba67e083a3c3d93"><a name="ae227f28ea9d74cd7bba67e083a3c3d93"></a><a name="ae227f28ea9d74cd7bba67e083a3c3d93"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="ad940d8e9e0dd425bab81230cfd05929b"><a name="ad940d8e9e0dd425bab81230cfd05929b"></a><a name="ad940d8e9e0dd425bab81230cfd05929b"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="rc7281062f7d1412391ff2ef0ee601edb"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a76b355cad2cc4f5cb97fedf4810d533c"><a name="a76b355cad2cc4f5cb97fedf4810d533c"></a><a name="a76b355cad2cc4f5cb97fedf4810d533c"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a0e91462d6f2044f9bd01bbd76fdf984a"><a name="a0e91462d6f2044f9bd01bbd76fdf984a"></a><a name="a0e91462d6f2044f9bd01bbd76fdf984a"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
<tr id="r0a0a0a9c844746e197141e9447196e43"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="ab9370426c2c8418da727d9d3d4f5fb26"><a name="ab9370426c2c8418da727d9d3d4f5fb26"></a><a name="ab9370426c2c8418da727d9d3d4f5fb26"></a>DiskName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a971c0c33b6564f6a9bd6598379f17545"><a name="a971c0c33b6564f6a9bd6598379f17545"></a><a name="a971c0c33b6564f6a9bd6598379f17545"></a>Specifies the disk for which the alarm is generated.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s0cc942cbcf0446b9b20f8170ca0a7984"></a>

Service performance and service processing capabilities deteriorate. For example, DBService active/standby synchronization is affected and the service becomes unavailable.

## Possible Causes<a name="s34419cb6451741a79cb40858a168d94a"></a>

The disk is aged or has bad sectors.

## Procedure<a name="s1dc2adc48e724e58854afd119f88dca6"></a>

Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).

## Related Information<a name="s42a8881add354556b8d4b70eacef5f25"></a>

N/A


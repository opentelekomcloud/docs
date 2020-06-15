# Key Operations on BMS<a name="en-us_topic_0100236048"></a>

Bare Metal Servers \(BMSs\) provide dedicated physical servers in single-tenant environments. They provide excellent computing performance and data security for core databases, key application systems, and high performance computing. They also offer the high scalability of a cloud-based service. You can buy BMSs directly or in a DeC as you need.

With CTS, you can record operations associated with BMS for future query, audit, and backtrack operations.

**Table  1**  BMS operations that can be recorded by CTS

<a name="table48767281152351"></a>
<table><thead align="left"><tr id="ra8c51250602645f5ae7fbb86743902c2"><th class="cellrowborder" valign="top" width="29.967003299670036%" id="mcps1.2.4.1.1"><p id="ad643656fc11640c3b06229d42f0774c4"><a name="ad643656fc11640c3b06229d42f0774c4"></a><a name="ad643656fc11640c3b06229d42f0774c4"></a><strong id="b842352706103557"><a name="b842352706103557"></a><a name="b842352706103557"></a>Operation</strong></p>
</th>
<th class="cellrowborder" valign="top" width="31.986801319868015%" id="mcps1.2.4.1.2"><p id="a4208d0495ed44c67928ecb24b6b75925"><a name="a4208d0495ed44c67928ecb24b6b75925"></a><a name="a4208d0495ed44c67928ecb24b6b75925"></a><strong id="b84235270610360"><a name="b84235270610360"></a><a name="b84235270610360"></a>Resource Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="38.04619538046195%" id="mcps1.2.4.1.3"><p id="a1d3bb1e274454e728c47277a98a23ea5"><a name="a1d3bb1e274454e728c47277a98a23ea5"></a><a name="a1d3bb1e274454e728c47277a98a23ea5"></a><strong id="b842352706182955"><a name="b842352706182955"></a><a name="b842352706182955"></a>Trace Name</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="rc9da6d0058e948e3840c126cb0ac5741"><td class="cellrowborder" valign="top" width="29.967003299670036%" headers="mcps1.2.4.1.1 "><p id="a4ab6ff96bd7a4dd0a938343d27fa01b3"><a name="a4ab6ff96bd7a4dd0a938343d27fa01b3"></a><a name="a4ab6ff96bd7a4dd0a938343d27fa01b3"></a>Creating a BMS</p>
</td>
<td class="cellrowborder" valign="top" width="31.986801319868015%" headers="mcps1.2.4.1.2 "><p id="acbab63e2060f4bcba3a34e487a620947"><a name="acbab63e2060f4bcba3a34e487a620947"></a><a name="acbab63e2060f4bcba3a34e487a620947"></a>bms</p>
</td>
<td class="cellrowborder" valign="top" width="38.04619538046195%" headers="mcps1.2.4.1.3 "><p id="a8b1dcebb0b7f46a3bd7e4fcff1494539"><a name="a8b1dcebb0b7f46a3bd7e4fcff1494539"></a><a name="a8b1dcebb0b7f46a3bd7e4fcff1494539"></a>createBareMetalServers</p>
</td>
</tr>
<tr id="r3e1b54a29cd14488883f07b289b11c78"><td class="cellrowborder" valign="top" width="29.967003299670036%" headers="mcps1.2.4.1.1 "><p id="aa5217e3319a3416ca03eadcaf7c85809"><a name="aa5217e3319a3416ca03eadcaf7c85809"></a><a name="aa5217e3319a3416ca03eadcaf7c85809"></a>Deleting a BMS</p>
</td>
<td class="cellrowborder" valign="top" width="31.986801319868015%" headers="mcps1.2.4.1.2 "><p id="a2641a14616f94c77a458bda9185061bb"><a name="a2641a14616f94c77a458bda9185061bb"></a><a name="a2641a14616f94c77a458bda9185061bb"></a>bms</p>
</td>
<td class="cellrowborder" valign="top" width="38.04619538046195%" headers="mcps1.2.4.1.3 "><p id="a6f9279036f45404c96f1790f801b8825"><a name="a6f9279036f45404c96f1790f801b8825"></a><a name="a6f9279036f45404c96f1790f801b8825"></a>deleteBareMetalServers</p>
</td>
</tr>
<tr id="re2fb7256a74440519ad29bd2842f8dcf"><td class="cellrowborder" valign="top" width="29.967003299670036%" headers="mcps1.2.4.1.1 "><p id="a331a6a8ea165438a82cf349515b235b2"><a name="a331a6a8ea165438a82cf349515b235b2"></a><a name="a331a6a8ea165438a82cf349515b235b2"></a>Starting a BMS</p>
</td>
<td class="cellrowborder" valign="top" width="31.986801319868015%" headers="mcps1.2.4.1.2 "><p id="aab17d5ea0bce41cc816e0db1984fec0e"><a name="aab17d5ea0bce41cc816e0db1984fec0e"></a><a name="aab17d5ea0bce41cc816e0db1984fec0e"></a>bms</p>
</td>
<td class="cellrowborder" valign="top" width="38.04619538046195%" headers="mcps1.2.4.1.3 "><p id="ad0bba91eb3f7480d9d86fa86bd73cdc5"><a name="ad0bba91eb3f7480d9d86fa86bd73cdc5"></a><a name="ad0bba91eb3f7480d9d86fa86bd73cdc5"></a>startBareMetalServers</p>
</td>
</tr>
<tr id="rdafa4e1930a54805a40018ad8b613f0c"><td class="cellrowborder" valign="top" width="29.967003299670036%" headers="mcps1.2.4.1.1 "><p id="aa41c5fb6d84c4c259eb63e3eabcb00c1"><a name="aa41c5fb6d84c4c259eb63e3eabcb00c1"></a><a name="aa41c5fb6d84c4c259eb63e3eabcb00c1"></a>Stopping a BMS</p>
</td>
<td class="cellrowborder" valign="top" width="31.986801319868015%" headers="mcps1.2.4.1.2 "><p id="a0f92399d1b1447afb14595d27c9feb6d"><a name="a0f92399d1b1447afb14595d27c9feb6d"></a><a name="a0f92399d1b1447afb14595d27c9feb6d"></a>bms</p>
</td>
<td class="cellrowborder" valign="top" width="38.04619538046195%" headers="mcps1.2.4.1.3 "><p id="af647be69c49840f6b5dcce87f144f981"><a name="af647be69c49840f6b5dcce87f144f981"></a><a name="af647be69c49840f6b5dcce87f144f981"></a>stopBareMetalServers</p>
</td>
</tr>
<tr id="r0f527d5e0b6d4ca985d5f70892f488ef"><td class="cellrowborder" valign="top" width="29.967003299670036%" headers="mcps1.2.4.1.1 "><p id="a50e3b346069e489d9ed892ed99aa616b"><a name="a50e3b346069e489d9ed892ed99aa616b"></a><a name="a50e3b346069e489d9ed892ed99aa616b"></a>Restarting a BMS</p>
</td>
<td class="cellrowborder" valign="top" width="31.986801319868015%" headers="mcps1.2.4.1.2 "><p id="aac2813db29c948e1a4d560b114826e3c"><a name="aac2813db29c948e1a4d560b114826e3c"></a><a name="aac2813db29c948e1a4d560b114826e3c"></a>bms</p>
</td>
<td class="cellrowborder" valign="top" width="38.04619538046195%" headers="mcps1.2.4.1.3 "><p id="aba70e838a8c14570a1e714bf9c587633"><a name="aba70e838a8c14570a1e714bf9c587633"></a><a name="aba70e838a8c14570a1e714bf9c587633"></a>rebootBareMetalServers</p>
</td>
</tr>
<tr id="rbe36e056a7d04c0bba18d9bd8f95734c"><td class="cellrowborder" valign="top" width="29.967003299670036%" headers="mcps1.2.4.1.1 "><p id="a7f3288a0bd8d41ca8f90f7b5f64e2c52"><a name="a7f3288a0bd8d41ca8f90f7b5f64e2c52"></a><a name="a7f3288a0bd8d41ca8f90f7b5f64e2c52"></a>Attaching a data disk to a BMS</p>
</td>
<td class="cellrowborder" valign="top" width="31.986801319868015%" headers="mcps1.2.4.1.2 "><p id="a65a94d1981524e87bb936047b0cbd3ed"><a name="a65a94d1981524e87bb936047b0cbd3ed"></a><a name="a65a94d1981524e87bb936047b0cbd3ed"></a>bms</p>
</td>
<td class="cellrowborder" valign="top" width="38.04619538046195%" headers="mcps1.2.4.1.3 "><p id="a96946e4c647c4d7daae9d165b5fc577a"><a name="a96946e4c647c4d7daae9d165b5fc577a"></a><a name="a96946e4c647c4d7daae9d165b5fc577a"></a>attachDataVolume</p>
</td>
</tr>
<tr id="r4c9008c1ae40418bb68fc00f2740a919"><td class="cellrowborder" valign="top" width="29.967003299670036%" headers="mcps1.2.4.1.1 "><p id="aa18d67f75ba047819fd4642ca294bec7"><a name="aa18d67f75ba047819fd4642ca294bec7"></a><a name="aa18d67f75ba047819fd4642ca294bec7"></a>Detaching a data disk from a BMS</p>
</td>
<td class="cellrowborder" valign="top" width="31.986801319868015%" headers="mcps1.2.4.1.2 "><p id="a91c6b401f5f147f7ac50e5643e34e2e3"><a name="a91c6b401f5f147f7ac50e5643e34e2e3"></a><a name="a91c6b401f5f147f7ac50e5643e34e2e3"></a>bms</p>
</td>
<td class="cellrowborder" valign="top" width="38.04619538046195%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0100240378_p270435117272"><a name="en-us_topic_0100240378_p270435117272"></a><a name="en-us_topic_0100240378_p270435117272"></a>detachDataVolume</p>
</td>
</tr>
</tbody>
</table>


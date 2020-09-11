# Key Operations on TMS<a name="en-us_topic_0100291677"></a>

Tag Management Service \(TMS\) is a visualized service for fast, unified tag management that enables you to control your resource permissions and billing more efficiently. It allows you to tag and categorize cloud services across regions, and it can be accessed through the TMS console or using APIs.

With CTS, you can record operations associated with TMS for later query, audit, and backtrack operations.

>![](/images/icon-note.gif) **NOTE:**   
>TMS is a global-level service and TMS traces are only displayed in the central region of the current site.  

**Table  1**  TMS operations that can be recorded by CTS

<a name="table2825381514365"></a>
<table><thead align="left"><tr id="r9e5aa3568bac4edfa5171b237588041f"><th class="cellrowborder" valign="top" width="32.32323232323232%" id="mcps1.2.4.1.1"><p id="af05ae7bb17624ee58aa5f3c4d70b6c3a"><a name="af05ae7bb17624ee58aa5f3c4d70b6c3a"></a><a name="af05ae7bb17624ee58aa5f3c4d70b6c3a"></a><strong id="b842352706103557"><a name="b842352706103557"></a><a name="b842352706103557"></a>Operation</strong></p>
</th>
<th class="cellrowborder" valign="top" width="29.292929292929294%" id="mcps1.2.4.1.2"><p id="af6a2525b5add413da0864514317a6e95"><a name="af6a2525b5add413da0864514317a6e95"></a><a name="af6a2525b5add413da0864514317a6e95"></a><strong id="b84235270610360"><a name="b84235270610360"></a><a name="b84235270610360"></a>Resource Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="38.38383838383838%" id="mcps1.2.4.1.3"><p id="ad5421c404b3c460b8f5ffaa8c101b00f"><a name="ad5421c404b3c460b8f5ffaa8c101b00f"></a><a name="ad5421c404b3c460b8f5ffaa8c101b00f"></a><strong id="b842352706182955"><a name="b842352706182955"></a><a name="b842352706182955"></a>Trace Name</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r11f11fed951949e09d8495d420853a92"><td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.2.4.1.1 "><p id="a48a342ec8c3f4805a0120b5c1103429f"><a name="a48a342ec8c3f4805a0120b5c1103429f"></a><a name="a48a342ec8c3f4805a0120b5c1103429f"></a>Creating or deleting a predefined tag</p>
</td>
<td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="a71af55df2d6147c4b5bbbbe21eb314f3"><a name="a71af55df2d6147c4b5bbbbe21eb314f3"></a><a name="a71af55df2d6147c4b5bbbbe21eb314f3"></a>application</p>
</td>
<td class="cellrowborder" valign="top" width="38.38383838383838%" headers="mcps1.2.4.1.3 "><p id="a51cca6f3aa184dd7a6d12b4f2512aaf4"><a name="a51cca6f3aa184dd7a6d12b4f2512aaf4"></a><a name="a51cca6f3aa184dd7a6d12b4f2512aaf4"></a>addTag/deleteTag</p>
</td>
</tr>
<tr id="r1a32cfbfa6a84899b85bdf0b13741b53"><td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.2.4.1.1 "><p id="ac3a1d164bdd5429fb26ebf497a8430fb"><a name="ac3a1d164bdd5429fb26ebf497a8430fb"></a><a name="ac3a1d164bdd5429fb26ebf497a8430fb"></a>Modifying a predefined tag</p>
</td>
<td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="a0fc666f7d8e04f51973d7f3d914ade10"><a name="a0fc666f7d8e04f51973d7f3d914ade10"></a><a name="a0fc666f7d8e04f51973d7f3d914ade10"></a>application</p>
</td>
<td class="cellrowborder" valign="top" width="38.38383838383838%" headers="mcps1.2.4.1.3 "><p id="a3c5b6db13bae4cbbbc42bc07fc965836"><a name="a3c5b6db13bae4cbbbc42bc07fc965836"></a><a name="a3c5b6db13bae4cbbbc42bc07fc965836"></a>modifyTag</p>
</td>
</tr>
<tr id="r5f2e61e4fd2d4250956797c33aaebcda"><td class="cellrowborder" valign="top" width="32.32323232323232%" headers="mcps1.2.4.1.1 "><p id="ad21665da89bc4f0688c00a93280e6ab0"><a name="ad21665da89bc4f0688c00a93280e6ab0"></a><a name="ad21665da89bc4f0688c00a93280e6ab0"></a>Creating or deleting a resource tag</p>
</td>
<td class="cellrowborder" valign="top" width="29.292929292929294%" headers="mcps1.2.4.1.2 "><p id="a66d6843baec046038a392f5051e8f790"><a name="a66d6843baec046038a392f5051e8f790"></a><a name="a66d6843baec046038a392f5051e8f790"></a>application</p>
</td>
<td class="cellrowborder" valign="top" width="38.38383838383838%" headers="mcps1.2.4.1.3 "><p id="a683a6b4fdb2942899a9840df73d6a331"><a name="a683a6b4fdb2942899a9840df73d6a331"></a><a name="a683a6b4fdb2942899a9840df73d6a331"></a>addResourceTag/deleteResourceTag</p>
</td>
</tr>
</tbody>
</table>


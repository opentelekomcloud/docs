# APIs Overview<a name="EN-US_TOPIC_0091845611"></a>

Currently, SFS only provides APIs as shown in the following table.

**Table  1**  APIs overview

<a name="table44686951202556"></a>
<table><thead align="left"><tr id="row8687869202556"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p25223878202556"><a name="p25223878202556"></a><a name="p25223878202556"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p29868257202556"><a name="p29868257202556"></a><a name="p29868257202556"></a>Operation</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p3409765202556"><a name="p3409765202556"></a><a name="p3409765202556"></a>Command</p>
</th>
</tr>
</thead>
<tbody><tr id="row30687885202556"><td class="cellrowborder" rowspan="6" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p63183968202731"><a name="p63183968202731"></a><a name="p63183968202731"></a>File Sharing</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p16624368202556"><a name="p16624368202556"></a><a name="p16624368202556"></a>Creating a Shared File System</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p4396548202556"><a name="p4396548202556"></a><a name="p4396548202556"></a>manila create</p>
</td>
</tr>
<tr id="row39568935202556"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p34701003202556"><a name="p34701003202556"></a><a name="p34701003202556"></a>Querying Details About All Shared File Systems</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p59317898202556"><a name="p59317898202556"></a><a name="p59317898202556"></a>manila list</p>
</td>
</tr>
<tr id="row64099042202556"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p49672955202556"><a name="p49672955202556"></a><a name="p49672955202556"></a>Querying Details About a Shared File System</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p64086447202556"><a name="p64086447202556"></a><a name="p64086447202556"></a>manila show</p>
</td>
</tr>
<tr id="row39907115202556"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p38906446202556"><a name="p38906446202556"></a><a name="p38906446202556"></a>Querying Mount Locations of a Shared File System</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p64414449202556"><a name="p64414449202556"></a><a name="p64414449202556"></a>manila share-export-location-list</p>
</td>
</tr>
<tr id="row42859131202556"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p12619163202556"><a name="p12619163202556"></a><a name="p12619163202556"></a>Modifying a Shared File System</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p15519319202556"><a name="p15519319202556"></a><a name="p15519319202556"></a>manila update</p>
</td>
</tr>
<tr id="row5456143202556"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p28735362202556"><a name="p28735362202556"></a><a name="p28735362202556"></a>Deleting a Shared File System</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p45862960202556"><a name="p45862960202556"></a><a name="p45862960202556"></a>manila delete</p>
</td>
</tr>
<tr id="row10113456202556"><td class="cellrowborder" rowspan="3" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p46825974202830"><a name="p46825974202830"></a><a name="p46825974202830"></a>Share Access Rules</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p50831912202556"><a name="p50831912202556"></a><a name="p50831912202556"></a>Adding a Share Access Rule</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p23744211202556"><a name="p23744211202556"></a><a name="p23744211202556"></a>manila access-allow</p>
</td>
</tr>
<tr id="row40878604202727"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p37501645202727"><a name="p37501645202727"></a><a name="p37501645202727"></a>Deleting a Share Access Rule</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p17734406202727"><a name="p17734406202727"></a><a name="p17734406202727"></a>manila access-deny</p>
</td>
</tr>
<tr id="row53073051202719"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p51506830202719"><a name="p51506830202719"></a><a name="p51506830202719"></a>Querying a Share Access Rule</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p11303676202719"><a name="p11303676202719"></a><a name="p11303676202719"></a>manila access-list</p>
</td>
</tr>
<tr id="row30213251202723"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p31354281202723"><a name="p31354281202723"></a><a name="p31354281202723"></a>Quota Management</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p56668839202723"><a name="p56668839202723"></a><a name="p56668839202723"></a>Querying a Quota</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p26773286202723"><a name="p26773286202723"></a><a name="p26773286202723"></a>manila quota-show</p>
</td>
</tr>
<tr id="row14724397202825"><td class="cellrowborder" rowspan="2" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p51825476202825"><a name="p51825476202825"></a><a name="p51825476202825"></a>Capacity Expansion or Reduction</p>
<p id="p49946724202818"><a name="p49946724202818"></a><a name="p49946724202818"></a></p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p37114048202825"><a name="p37114048202825"></a><a name="p37114048202825"></a>Expanding the Capacity of a Shared File System</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p53447945202825"><a name="p53447945202825"></a><a name="p53447945202825"></a>manila extend</p>
</td>
</tr>
<tr id="row31271292202818"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p19152857202818"><a name="p19152857202818"></a><a name="p19152857202818"></a>Reducing the Capacity a Shared File System</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p7877570202818"><a name="p7877570202818"></a><a name="p7877570202818"></a>manila shrink</p>
</td>
</tr>
<tr id="row44954445202822"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p17431419202822"><a name="p17431419202822"></a><a name="p17431419202822"></a>Querying API Versions</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p2658838202822"><a name="p2658838202822"></a><a name="p2658838202822"></a>Querying All Major Versions</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p14039301202822"><a name="p14039301202822"></a><a name="p14039301202822"></a>manila api-version</p>
</td>
</tr>
</tbody>
</table>


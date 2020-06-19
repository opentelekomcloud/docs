# Key Operations on VBS<a name="en-us_topic_0100273732"></a>

Volume Backup Service \(VBS\) provides snapshot-based data protection for EVS disks on ECSs in public cloud environments. VBS supports both full and incremental backups. By default, the system performs a full backup initially, and then performs incremental backups. You can use those data backups generated in either backup mode to restore EVS disks to the state they were in when the backup was created.

With CTS, you can record operations associated with VBS for future query, audit, and backtrack operations.

**Table  1**  VBS operations that can be recorded by CTS

<a name="table3263159911376"></a>
<table><thead align="left"><tr id="r46a9307ed83b4070a542a4589f3b7a82"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="a83fdb5cbccbd407ba78964c769363894"><a name="a83fdb5cbccbd407ba78964c769363894"></a><a name="a83fdb5cbccbd407ba78964c769363894"></a><strong id="b842352706103557"><a name="b842352706103557"></a><a name="b842352706103557"></a>Operation</strong></p>
</th>
<th class="cellrowborder" valign="top" width="36%" id="mcps1.2.4.1.2"><p id="en-us_topic_0100240354_p226716611376"><a name="en-us_topic_0100240354_p226716611376"></a><a name="en-us_topic_0100240354_p226716611376"></a><strong id="b84235270610360"><a name="b84235270610360"></a><a name="b84235270610360"></a>Resource Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39%" id="mcps1.2.4.1.3"><p id="ad9198950e9e34b7f9df41ff33e249eb4"><a name="ad9198950e9e34b7f9df41ff33e249eb4"></a><a name="ad9198950e9e34b7f9df41ff33e249eb4"></a><strong id="b842352706182955"><a name="b842352706182955"></a><a name="b842352706182955"></a>Trace Name</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r5a1f5660e23b4958bc2fe88a7d51612e"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1988104192517"><a name="p1988104192517"></a><a name="p1988104192517"></a>Creating a backup</p>
</td>
<td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.2 "><p id="p26354544255"><a name="p26354544255"></a><a name="p26354544255"></a>vbs</p>
</td>
<td class="cellrowborder" valign="top" width="39%" headers="mcps1.2.4.1.3 "><p id="p184301342613"><a name="p184301342613"></a><a name="p184301342613"></a>bksCreateBackup</p>
</td>
</tr>
<tr id="rf5fb92a076294886883d3371bf543ec0"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p9882041142518"><a name="p9882041142518"></a><a name="p9882041142518"></a>Deleting a backup</p>
</td>
<td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.2 "><p id="p126355542250"><a name="p126355542250"></a><a name="p126355542250"></a>vbs</p>
</td>
<td class="cellrowborder" valign="top" width="39%" headers="mcps1.2.4.1.3 "><p id="p8430735267"><a name="p8430735267"></a><a name="p8430735267"></a>bksDeleteBackup</p>
</td>
</tr>
<tr id="rbb1186a8e42e458e9eefbbd2d86c63fc"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p118817411251"><a name="p118817411251"></a><a name="p118817411251"></a>Restoring a backup</p>
</td>
<td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.2 "><p id="p15635154152512"><a name="p15635154152512"></a><a name="p15635154152512"></a>vbs</p>
</td>
<td class="cellrowborder" valign="top" width="39%" headers="mcps1.2.4.1.3 "><p id="p243019312614"><a name="p243019312614"></a><a name="p243019312614"></a>bksRestoreBackup</p>
</td>
</tr>
<tr id="r10d5e8f3468641b59d6dc9dcaf8f2155"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p178816417255"><a name="p178816417255"></a><a name="p178816417255"></a>Binding a backup policy</p>
</td>
<td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.2 "><p id="p13635175410256"><a name="p13635175410256"></a><a name="p13635175410256"></a>autobackup</p>
</td>
<td class="cellrowborder" valign="top" width="39%" headers="mcps1.2.4.1.3 "><p id="p10430103112610"><a name="p10430103112610"></a><a name="p10430103112610"></a>addPolicyResource</p>
</td>
</tr>
<tr id="r05b6d587bac04b50bd3e64ecd0ef330b"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p138813414257"><a name="p138813414257"></a><a name="p138813414257"></a>Unbinding a backup policy</p>
</td>
<td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.2 "><p id="p76359543253"><a name="p76359543253"></a><a name="p76359543253"></a>autobackup</p>
</td>
<td class="cellrowborder" valign="top" width="39%" headers="mcps1.2.4.1.3 "><p id="p54301834265"><a name="p54301834265"></a><a name="p54301834265"></a>deletePolicyResource</p>
</td>
</tr>
<tr id="r52722966cd5b46e7b02aae2e6119dc82"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p128813416259"><a name="p128813416259"></a><a name="p128813416259"></a>Executing a backup policy</p>
</td>
<td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.2 "><p id="p166351054142517"><a name="p166351054142517"></a><a name="p166351054142517"></a>autobackup</p>
</td>
<td class="cellrowborder" valign="top" width="39%" headers="mcps1.2.4.1.3 "><p id="p164302342617"><a name="p164302342617"></a><a name="p164302342617"></a>actionPolicy</p>
</td>
</tr>
<tr id="r214efe4587d34041bdf87e1e31f03ed6"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1988104122513"><a name="p1988104122513"></a><a name="p1988104122513"></a>Creating a backup policy</p>
</td>
<td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.2 "><p id="p76352540255"><a name="p76352540255"></a><a name="p76352540255"></a>autobackup</p>
</td>
<td class="cellrowborder" valign="top" width="39%" headers="mcps1.2.4.1.3 "><p id="p2430123122612"><a name="p2430123122612"></a><a name="p2430123122612"></a>createPolicy</p>
</td>
</tr>
<tr id="r8350278bf72b4692bd1d012f93456f56"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p588141132520"><a name="p588141132520"></a><a name="p588141132520"></a>Deleting a backup policy</p>
</td>
<td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.2 "><p id="p3635125416255"><a name="p3635125416255"></a><a name="p3635125416255"></a>autobackup</p>
</td>
<td class="cellrowborder" valign="top" width="39%" headers="mcps1.2.4.1.3 "><p id="p184306302613"><a name="p184306302613"></a><a name="p184306302613"></a>deletePolicy</p>
</td>
</tr>
<tr id="r33a7ebc962574856840c93c8082d5c8c"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p988134182511"><a name="p988134182511"></a><a name="p988134182511"></a>Modifying a backup policy</p>
</td>
<td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.2 "><p id="p16359548257"><a name="p16359548257"></a><a name="p16359548257"></a>autobackup</p>
</td>
<td class="cellrowborder" valign="top" width="39%" headers="mcps1.2.4.1.3 "><p id="p6430134263"><a name="p6430134263"></a><a name="p6430134263"></a>modifyPolicy</p>
</td>
</tr>
<tr id="r36cd5b870a434711944b2e304be322ee"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1888194142510"><a name="p1888194142510"></a><a name="p1888194142510"></a>Creating backups scheduled by a backup policy</p>
</td>
<td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.2 "><p id="p1363525452519"><a name="p1363525452519"></a><a name="p1363525452519"></a>autobackup</p>
</td>
<td class="cellrowborder" valign="top" width="39%" headers="mcps1.2.4.1.3 "><p id="p543033202614"><a name="p543033202614"></a><a name="p543033202614"></a>scheduleCreateBackup</p>
</td>
</tr>
<tr id="rd80d7573a14b47649e5f5531b35d5863"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1388641132517"><a name="p1388641132517"></a><a name="p1388641132517"></a>Automatically deleting redundant backups scheduled by a backup policy</p>
</td>
<td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.2 "><p id="p1863519542250"><a name="p1863519542250"></a><a name="p1863519542250"></a>autobackup</p>
</td>
<td class="cellrowborder" valign="top" width="39%" headers="mcps1.2.4.1.3 "><p id="p543014316261"><a name="p543014316261"></a><a name="p543014316261"></a>scheduleDeleteBackup</p>
</td>
</tr>
<tr id="row132108559140"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p188814152516"><a name="p188814152516"></a><a name="p188814152516"></a>Batch adding or modifying tags of a backup policy</p>
</td>
<td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.2 "><p id="p1863535415257"><a name="p1863535415257"></a><a name="p1863535415257"></a>autobackup</p>
</td>
<td class="cellrowborder" valign="top" width="39%" headers="mcps1.2.4.1.3 "><p id="p34301039260"><a name="p34301039260"></a><a name="p34301039260"></a>batchAddPolicyTag</p>
</td>
</tr>
<tr id="r0cd86f8e1a6745bb98c2ff6e863693f3"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p108864110255"><a name="p108864110255"></a><a name="p108864110255"></a>Batch deleting tags of a backup policy</p>
</td>
<td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.2 "><p id="p5635175417259"><a name="p5635175417259"></a><a name="p5635175417259"></a>autobackup</p>
</td>
<td class="cellrowborder" valign="top" width="39%" headers="mcps1.2.4.1.3 "><p id="p1243093162616"><a name="p1243093162616"></a><a name="p1243093162616"></a>batchDeletePolicyTag</p>
</td>
</tr>
<tr id="ra70aabe8db804b74ba6f75a45842ced0"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1388174115250"><a name="p1388174115250"></a><a name="p1388174115250"></a>Adding or modifying a backup policy tag</p>
</td>
<td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.2 "><p id="p14635175412256"><a name="p14635175412256"></a><a name="p14635175412256"></a>autobackup</p>
</td>
<td class="cellrowborder" valign="top" width="39%" headers="mcps1.2.4.1.3 "><p id="p1243063152618"><a name="p1243063152618"></a><a name="p1243063152618"></a>addPolicyTag</p>
</td>
</tr>
<tr id="row1681143612510"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1188174182518"><a name="p1188174182518"></a><a name="p1188174182518"></a>Deleting a backup policy tag</p>
</td>
<td class="cellrowborder" valign="top" width="36%" headers="mcps1.2.4.1.2 "><p id="p363517547254"><a name="p363517547254"></a><a name="p363517547254"></a>autobackup</p>
</td>
<td class="cellrowborder" valign="top" width="39%" headers="mcps1.2.4.1.3 "><p id="p743010322614"><a name="p743010322614"></a><a name="p743010322614"></a>deletePolicyTag</p>
</td>
</tr>
</tbody>
</table>


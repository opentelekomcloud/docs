# ALM-12015 Partition Filesystem Readonly<a name="EN-US_TOPIC_0125375189"></a>

## Description<a name="s8e772fbe26ef4dd0b69e9553bfc44c46"></a>

The system checks the partition status periodically. This alarm is generated when the system detects that a partition to which service directories are mounted enters the read-only mode \(due to a bad sector or a faulty file system\).

This alarm is cleared when the system detects that the partition to which service directories are mounted exits from the read-only mode \(because the file system is restored to read/write mode, the device is removed, or the device is formatted\).

## Attribute<a name="sea9c916ad454441d950f4f272d90052f"></a>

<a name="td562eac2174f47378c094d203030018b"></a>
<table><thead align="left"><tr id="r514b76348c14431585cb5c9c45773024"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="a3787a9feaad7480c9452049603eed4b1"><a name="a3787a9feaad7480c9452049603eed4b1"></a><a name="a3787a9feaad7480c9452049603eed4b1"></a>Alarm ID</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="ae2199c3fd4e243fba66b5882988f320f"><a name="ae2199c3fd4e243fba66b5882988f320f"></a><a name="ae2199c3fd4e243fba66b5882988f320f"></a>Alarm Severity</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="a264f337fe7a844cd846ff0f1803dcc8b"><a name="a264f337fe7a844cd846ff0f1803dcc8b"></a><a name="a264f337fe7a844cd846ff0f1803dcc8b"></a>Automatically&nbsp;Cleared</p>
</th>
</tr>
</thead>
<tbody><tr id="rc1794a7e7a644ddbadac09d29949ee3b"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="a6d5353809c6e43c596fca5d28831d3bb"><a name="a6d5353809c6e43c596fca5d28831d3bb"></a><a name="a6d5353809c6e43c596fca5d28831d3bb"></a>12015</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="a3db14d72620e406d9a977a6864e59681"><a name="a3db14d72620e406d9a977a6864e59681"></a><a name="a3db14d72620e406d9a977a6864e59681"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="adbbc15983b314cefae11afdf0fd2266b"><a name="adbbc15983b314cefae11afdf0fd2266b"></a><a name="adbbc15983b314cefae11afdf0fd2266b"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="sd8a980f088154e81b7b0c17999438203"></a>

<a name="t5e41abbf3cb14f339af6927536dbf138"></a>
<table><thead align="left"><tr id="r7d1d4d4e94654ce0a6aa1f134255f8d8"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="a461b75f7702147c29966a9b2762aa6e6"><a name="a461b75f7702147c29966a9b2762aa6e6"></a><a name="a461b75f7702147c29966a9b2762aa6e6"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="ab143fd59926d49af9d1fed164bb8c8d0"><a name="ab143fd59926d49af9d1fed164bb8c8d0"></a><a name="ab143fd59926d49af9d1fed164bb8c8d0"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="rcf713f99d37747a9b4f4d3a854790d11"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="af8aa8c919de64c15ae9d803e79b5a2b5"><a name="af8aa8c919de64c15ae9d803e79b5a2b5"></a><a name="af8aa8c919de64c15ae9d803e79b5a2b5"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a863ed6aaeb794682a9e765a8bbb6cf47"><a name="a863ed6aaeb794682a9e765a8bbb6cf47"></a><a name="a863ed6aaeb794682a9e765a8bbb6cf47"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="r8bc7965ec8684451a3548831072e98fc"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a8f349915908d4ecb8c5092fa976af2ed"><a name="a8f349915908d4ecb8c5092fa976af2ed"></a><a name="a8f349915908d4ecb8c5092fa976af2ed"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a60f82dbc0a9b4873afed26df0ce9f0a9"><a name="a60f82dbc0a9b4873afed26df0ce9f0a9"></a><a name="a60f82dbc0a9b4873afed26df0ce9f0a9"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="rb1436da5a7f94594bdcba143e003b08f"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="ace84f9c5928e49deaad319aa863e4303"><a name="ace84f9c5928e49deaad319aa863e4303"></a><a name="ace84f9c5928e49deaad319aa863e4303"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a536871b09e0d48c69e4c16cb1f876668"><a name="a536871b09e0d48c69e4c16cb1f876668"></a><a name="a536871b09e0d48c69e4c16cb1f876668"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
<tr id="r0a1693927a364c4b8a885350a16fd9ec"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a85f8e99e9c1144dfb8b36bb3817cd6a3"><a name="a85f8e99e9c1144dfb8b36bb3817cd6a3"></a><a name="a85f8e99e9c1144dfb8b36bb3817cd6a3"></a>DirName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="ab538cff9fb2841c1bc3258d447087347"><a name="ab538cff9fb2841c1bc3258d447087347"></a><a name="ab538cff9fb2841c1bc3258d447087347"></a>Specifies the directory for which the alarm is generated.</p>
</td>
</tr>
<tr id="r3a8f14043bcf4c5ea22b2cf32cec280d"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a2f1881459dce410da4e8bde6023cc569"><a name="a2f1881459dce410da4e8bde6023cc569"></a><a name="a2f1881459dce410da4e8bde6023cc569"></a>PartitionName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a7b3cfb56c70749d5a8e6b4aa6abdce00"><a name="a7b3cfb56c70749d5a8e6b4aa6abdce00"></a><a name="a7b3cfb56c70749d5a8e6b4aa6abdce00"></a>Specifies the device partition for which the alarm is generated.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="sbe43d768a1ce4df3965ae05461997b2b"></a>

Service data fails to be written into the partition, and the service system runs abnormally.

## Possible Causes<a name="s342c1876a43b4093b9c9d04e8aa4ca8d"></a>

The hard disk is faulty. For example, a bad sector exists.

## Procedure<a name="s7e49cd4b667c4ecfae7a4a4ab41c1277"></a>

1.  On MRS Manager, click the alarm in the real-time alarm list.
2.  In the  **Alarm Details** area, obtain **HostName** and **PartitionName** from **Location**. **HostName** is the node where the alarm is reported, and **PartitionName**  is the partition of the faulty disk.
3.  Contact hardware engineers to check whether the disk is faulty. If the disk is faulty, remove it from the server.
4.  After the disk is removed, alarm  **ALM-12014 Partition Lost** is reported. Handle the alarm. For details, see [ALM-12014 Partition Lost](alm-12014-partition-lost.md). After the alarm **ALM-12014 Partition Lost** is cleared, alarm **ALM-12015 Partition Filesystem Readonly**  is automatically cleared.

## Related Information<a name="sc793d45c1439493b8cd255e484dba47b"></a>

N/A


# Scenarios<a name="EN-US_TOPIC_0056584596"></a>

CSBS supports one-off backup and periodic backup. A one-off backup job is manually created by users and takes effect for only one time. Periodic backup jobs are automatically driven by a user-defined backup policy.

[Table 1](#table31963779194543)  describes the two backup options.

**Table  1**  One-off backup and periodic backup

<a name="table31963779194543"></a>
<table><thead align="left"><tr id="row25019286194543"><th class="cellrowborder" valign="top" width="19.830000000000002%" id="mcps1.2.4.1.1"><p id="p52557898194543"><a name="p52557898194543"></a><a name="p52557898194543"></a>Item</p>
</th>
<th class="cellrowborder" valign="top" width="40.17%" id="mcps1.2.4.1.2"><p id="p29331320194543"><a name="p29331320194543"></a><a name="p29331320194543"></a>One-Off Backup</p>
</th>
<th class="cellrowborder" valign="top" width="40%" id="mcps1.2.4.1.3"><p id="p27026686194543"><a name="p27026686194543"></a><a name="p27026686194543"></a>Periodic Backup</p>
</th>
</tr>
</thead>
<tbody><tr id="row39557296194543"><td class="cellrowborder" valign="top" width="19.830000000000002%" headers="mcps1.2.4.1.1 "><p id="p50024411194543"><a name="p50024411194543"></a><a name="p50024411194543"></a>Backup policy</p>
</td>
<td class="cellrowborder" valign="top" width="40.17%" headers="mcps1.2.4.1.2 "><p id="p25445466194543"><a name="p25445466194543"></a><a name="p25445466194543"></a>None</p>
</td>
<td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.4.1.3 "><p id="p47816854194543"><a name="p47816854194543"></a><a name="p47816854194543"></a>Required</p>
</td>
</tr>
<tr id="row28986151194543"><td class="cellrowborder" valign="top" width="19.830000000000002%" headers="mcps1.2.4.1.1 "><p id="p66176889194543"><a name="p66176889194543"></a><a name="p66176889194543"></a>Number of backup operations</p>
</td>
<td class="cellrowborder" valign="top" width="40.17%" headers="mcps1.2.4.1.2 "><p id="p58727779194543"><a name="p58727779194543"></a><a name="p58727779194543"></a>Only one, manual</p>
</td>
<td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.4.1.3 "><p id="p59329678194543"><a name="p59329678194543"></a><a name="p59329678194543"></a>Periodic operations driven by the backup policy</p>
</td>
</tr>
<tr id="row30678101194912"><td class="cellrowborder" valign="top" width="19.830000000000002%" headers="mcps1.2.4.1.1 "><p id="p7667457194912"><a name="p7667457194912"></a><a name="p7667457194912"></a>Backup name</p>
</td>
<td class="cellrowborder" valign="top" width="40.17%" headers="mcps1.2.4.1.2 "><p id="p17084271194912"><a name="p17084271194912"></a><a name="p17084271194912"></a>User-defined backup name, which defaults to <strong id="b842352706163625"><a name="b842352706163625"></a><a name="b842352706163625"></a>manualbk_</strong><em id="i842352697163627"><a name="i842352697163627"></a><a name="i842352697163627"></a>xxxx</em></p>
</td>
<td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.4.1.3 "><p id="p41648714194912"><a name="p41648714194912"></a><a name="p41648714194912"></a>System-assigned backup name, which defaults to <strong id="b842352706163712"><a name="b842352706163712"></a><a name="b842352706163712"></a>autobk_</strong><em id="i842352697163714"><a name="i842352697163714"></a><a name="i842352697163714"></a>xxxx</em></p>
</td>
</tr>
<tr id="row11946619194919"><td class="cellrowborder" valign="top" width="19.830000000000002%" headers="mcps1.2.4.1.1 "><p id="p28152045194919"><a name="p28152045194919"></a><a name="p28152045194919"></a>Backup method</p>
</td>
<td class="cellrowborder" valign="top" width="40.17%" headers="mcps1.2.4.1.2 "><p id="p65723188194919"><a name="p65723188194919"></a><a name="p65723188194919"></a>Full backup at the first time and incremental backup subsequently, by default</p>
</td>
<td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.4.1.3 "><p id="p21978040194919"><a name="p21978040194919"></a><a name="p21978040194919"></a>Full backup at the first time and incremental backup subsequently, by default</p>
</td>
</tr>
<tr id="row52750521201028"><td class="cellrowborder" valign="top" width="19.830000000000002%" headers="mcps1.2.4.1.1 "><p id="p4992645201028"><a name="p4992645201028"></a><a name="p4992645201028"></a>Application scenario</p>
</td>
<td class="cellrowborder" valign="top" width="40.17%" headers="mcps1.2.4.1.2 "><p id="p1751091201028"><a name="p1751091201028"></a><a name="p1751091201028"></a>Executed before patching or upgrading the OS or upgrading an application on an ECS. A one-off backup can be used to restore an ECS to the original state in case the patching or upgrading fails.</p>
<p id="p285423841619"><a name="p285423841619"></a><a name="p285423841619"></a>Executed before patching or upgrading the OS or upgrading an application on a server. A one-off backup can be used to restore a server to the original state in case the patching or upgrading fails.</p>
</td>
<td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.4.1.3 "><p id="p7620686201028"><a name="p7620686201028"></a><a name="p7620686201028"></a>Executed for routine maintenance of an ECS. The latest backup can be used to restore an ECS in case an unexpected failure or data loss occurs.</p>
</td>
</tr>
</tbody>
</table>

Users can also intermix the two backup options for a special need. For example, associate all ECSs with a backup policy to execute periodic backup of all ECSs, and manually perform one-off backups for the most important ECSs to further ensure those ECSs' data security, as shown in  [Figure 1](#fig6436164020634).

**Figure  1**  Intermixed use of the two backup options<a name="fig6436164020634"></a>  
![](figures/intermixed-use-of-the-two-backup-options.png "intermixed-use-of-the-two-backup-options")


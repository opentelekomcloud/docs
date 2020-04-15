# ALM-12014 Partition Lost<a name="EN-US_TOPIC_0125375827"></a>

## Description<a name="sf33f4b8b9fe34506bdf7f0f7a2864d2f"></a>

The system checks the partition status periodically. This alarm is generated when the system detects that a partition to which service directories are mounted is lost \(because the device is removed or goes offline, or the partition is deleted\).

This alarm must be manually cleared.

## Attribute<a name="s419b971162314325a7c031898b7f9339"></a>

<a name="t7b9d24708c37428c8bd5f1575185a525"></a>
<table><thead align="left"><tr id="r584ea5ad278c4882b94824f11a4d44d6"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="a91edfb43c09d4fbf8be665e42d5d3280"><a name="a91edfb43c09d4fbf8be665e42d5d3280"></a><a name="a91edfb43c09d4fbf8be665e42d5d3280"></a>Alarm ID</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="a5aad8f8b57204a5fb253cc6a5701768e"><a name="a5aad8f8b57204a5fb253cc6a5701768e"></a><a name="a5aad8f8b57204a5fb253cc6a5701768e"></a>Alarm Severity</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="a9dfb2cd34cba479387fc0a0821b79088"><a name="a9dfb2cd34cba479387fc0a0821b79088"></a><a name="a9dfb2cd34cba479387fc0a0821b79088"></a>Automatically Cleared</p>
</th>
</tr>
</thead>
<tbody><tr id="rfe911c129f374fa083673e1cd4774911"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="afb0fe4ce8765458b90ca6719cb378a43"><a name="afb0fe4ce8765458b90ca6719cb378a43"></a><a name="afb0fe4ce8765458b90ca6719cb378a43"></a>12014</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="ab72a8059599e4854a0cffb9a71f275ef"><a name="ab72a8059599e4854a0cffb9a71f275ef"></a><a name="ab72a8059599e4854a0cffb9a71f275ef"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="a990fa3fc79c246448e2f632604b6ed25"><a name="a990fa3fc79c246448e2f632604b6ed25"></a><a name="a990fa3fc79c246448e2f632604b6ed25"></a>No</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s0d45568c4bee4eb399a0f13d0b67be47"></a>

<a name="tbdf47887144544f4bb729557e8fc67e9"></a>
<table><thead align="left"><tr id="rcc81af5d28bc4df9b40dfa36de4f35a7"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="a89428da4a7ca4714a0f7205ea11b23fc"><a name="a89428da4a7ca4714a0f7205ea11b23fc"></a><a name="a89428da4a7ca4714a0f7205ea11b23fc"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="a61509856d83f4838bfbd33c4e3f6eac7"><a name="a61509856d83f4838bfbd33c4e3f6eac7"></a><a name="a61509856d83f4838bfbd33c4e3f6eac7"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="re639a23996044ea4a3a033372d6db85f"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="ad664d902e63f43d0aaebcdf9e244f5b0"><a name="ad664d902e63f43d0aaebcdf9e244f5b0"></a><a name="ad664d902e63f43d0aaebcdf9e244f5b0"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a976328c0a6a543f28cd90dd70565ecaf"><a name="a976328c0a6a543f28cd90dd70565ecaf"></a><a name="a976328c0a6a543f28cd90dd70565ecaf"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="rff871d81622a483aa5a81dc3612fd7ef"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a7f51da0be53c46869a6984c22d3ed932"><a name="a7f51da0be53c46869a6984c22d3ed932"></a><a name="a7f51da0be53c46869a6984c22d3ed932"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="ad2e86b6b25a844d68bef1b21d11a5948"><a name="ad2e86b6b25a844d68bef1b21d11a5948"></a><a name="ad2e86b6b25a844d68bef1b21d11a5948"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="r84ceeae7dd514531adaf6f0ddf8bbda8"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a910cfab048ba4b70bcd8658fcab6c3ab"><a name="a910cfab048ba4b70bcd8658fcab6c3ab"></a><a name="a910cfab048ba4b70bcd8658fcab6c3ab"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="ac7611b91410141d0aacf70cac5102714"><a name="ac7611b91410141d0aacf70cac5102714"></a><a name="ac7611b91410141d0aacf70cac5102714"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
<tr id="rf45df78eabb14155bf20866ccb23249e"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a6e3cfad715104297bddbecca371c524e"><a name="a6e3cfad715104297bddbecca371c524e"></a><a name="a6e3cfad715104297bddbecca371c524e"></a>DirName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a7c64804ef1aa492a9ab2e34af8cad5cb"><a name="a7c64804ef1aa492a9ab2e34af8cad5cb"></a><a name="a7c64804ef1aa492a9ab2e34af8cad5cb"></a>Specifies the directory for which the alarm is generated.</p>
</td>
</tr>
<tr id="rc10a038ce7f749d7baf3667091b9863f"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="af4f50513bd6a4820aded98ed4ffb4a70"><a name="af4f50513bd6a4820aded98ed4ffb4a70"></a><a name="af4f50513bd6a4820aded98ed4ffb4a70"></a>PartitionName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="af022035b09b54630a2eb15309743b8db"><a name="af022035b09b54630a2eb15309743b8db"></a><a name="af022035b09b54630a2eb15309743b8db"></a>Specifies the device partition for which the alarm is generated.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s89112668e07843ba98ca09f91b6f0524"></a>

Service data fails to be written into the partition, and the service system runs abnormally.

## Possible Causes<a name="sb160cc3a6072410581d2b83f9acc33a7"></a>

-   The hard disk is removed.
-   The hard disk is offline, or a bad sector exists on the hard disk.

## Procedure<a name="s1ae7b6e156fb409da00b507ff1e6ec92"></a>

1.  On MRS Manager, click  **Alarm**, and click the alarm in the real-time alarm list.
2.  In the  **Alarm Details** area, obtain **HostName**, **PartitionName** and **DirName** from **Location**.
3.  Check whether the disk of  **PartitionName** on **HostName**  is inserted to the correct server slot.
    -   If yes, go to  [4](#l717992fbc5f4419887818649cee4ebb2).
    -   If no, go to  [5](#l1ba7cb6df0c347d5a1ab8623ae39601c).

4.  <a name="l717992fbc5f4419887818649cee4ebb2"></a>Contact hardware engineers to remove the faulty disk.
5.  <a name="l1ba7cb6df0c347d5a1ab8623ae39601c"></a>Use PuTTY to log in to the  **HostName** node where an alarm is reported and check whether there is a line containing **DirName** in the **/etc/fstab**  file.
    -   If yes, go to  [6](#l6e02ca246eb3480ca641669ee9e877c5).
    -   If no, go to  [7](#laeb1a8bf92f74bd2abb36ebafbe30db3).

6.  <a name="l6e02ca246eb3480ca641669ee9e877c5"></a>Run the  **vi /etc/fstab** command to edit the file and delete the line containing **DirName**.
7.  <a name="laeb1a8bf92f74bd2abb36ebafbe30db3"></a>Contact hardware engineers to insert a new disk. For details, see the hardware product document of the relevant model. If the faulty disk is in a RAID group, configure the RAID group. For details, see the configuration methods of the relevant RAID controller card.
8.  Wait 20 to 30 minutes \(The disk size determines the waiting time\), and run the  **mount** command to check whether the disk has been mounted to the **DirName**  directory.
    -   If yes, manually clear the alarm. No further operation is required.
    -   If no, go to  [9](#lf2561b42e0d54058a78e6a9f4459304b).

9.  <a name="lf2561b42e0d54058a78e6a9f4459304b"></a>Collect fault information.
    1.  On MRS Manager, choose  **System \> Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="s25f4f45a7e6d489aabc93cf72bdc626c"></a>

N/A


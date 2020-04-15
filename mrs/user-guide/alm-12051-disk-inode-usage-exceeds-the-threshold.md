# ALM-12051 Disk Inode Usage Exceeds the Threshold<a name="EN-US_TOPIC_0125375402"></a>

## Description<a name="sd604e831f88b4e029904e992fec5891b"></a>

The system checks the disk Inode usage every 30 seconds and compares the actual Inode usage with the threshold \(the default threshold is 80%\). This alarm is generated when the Inode usage exceeds the threshold for several times \(5 times by default\) consecutively.

To change the threshold, choose  **System**  \>  **Threshold Configuration**  \>  **Device**  \>  **Host**  \>  **Disk**  \>  **Disk Inode Usage**  \>  **Disk Inode Usage**.

When the  **hit number**  is 1, this alarm is cleared when the disk Inode usage is less than or equal to the threshold. When the  **hit number**  is greater than 1, this alarm is cleared when the disk Inode usage is less than or equal to 90% of the threshold.

## Attribute<a name="s91da6cb6e7c543edb2365b56a0d94054"></a>

<a name="t956a9ad8f4c1420685494f5fee921b42"></a>
<table><thead align="left"><tr id="r42ffd5d3352247cca950cbc0c0fbefc6"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="a82ef60a3e0074cf5b01c60e6e35499d0"><a name="a82ef60a3e0074cf5b01c60e6e35499d0"></a><a name="a82ef60a3e0074cf5b01c60e6e35499d0"></a>Alarm ID</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="acaea057b1c0a47ddba15f5db294dbb25"><a name="acaea057b1c0a47ddba15f5db294dbb25"></a><a name="acaea057b1c0a47ddba15f5db294dbb25"></a>Alarm Severity</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="a9a1d1ed831b34768809a6b16e61eef9d"><a name="a9a1d1ed831b34768809a6b16e61eef9d"></a><a name="a9a1d1ed831b34768809a6b16e61eef9d"></a>Automatically Cleared</p>
</th>
</tr>
</thead>
<tbody><tr id="r19d0741707c34f19b3d001b32a91ea66"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="af64e87a464b3422781af60f5e7bd1bc8"><a name="af64e87a464b3422781af60f5e7bd1bc8"></a><a name="af64e87a464b3422781af60f5e7bd1bc8"></a>12051</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="a80bcec7a899d491bb636a3d251030f34"><a name="a80bcec7a899d491bb636a3d251030f34"></a><a name="a80bcec7a899d491bb636a3d251030f34"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="a5069496c9f3c4c1da5af0734f65783d6"><a name="a5069496c9f3c4c1da5af0734f65783d6"></a><a name="a5069496c9f3c4c1da5af0734f65783d6"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="sf7a6c7d695c147d6b618c19748a67d52"></a>

<a name="t4d15f6caab444662a3200d5ac554c5f0"></a>
<table><thead align="left"><tr id="rd1e2af73645f45de80704b374f8d75a5"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="a4c0f953dee1c43dd97b61c0d2e8d6ef6"><a name="a4c0f953dee1c43dd97b61c0d2e8d6ef6"></a><a name="a4c0f953dee1c43dd97b61c0d2e8d6ef6"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="afab4df3680124a10881bd48c3743b76a"><a name="afab4df3680124a10881bd48c3743b76a"></a><a name="afab4df3680124a10881bd48c3743b76a"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="rc380c87f59f242e4b10cf3d7ad51adab"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="afc08b51e0b3740528a7fe527af877609"><a name="afc08b51e0b3740528a7fe527af877609"></a><a name="afc08b51e0b3740528a7fe527af877609"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a6a444debe322456da2d584a4c6e85f01"><a name="a6a444debe322456da2d584a4c6e85f01"></a><a name="a6a444debe322456da2d584a4c6e85f01"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="refcee2e3bf3e42d59d086a7187ef5708"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a0e4c3645c82a45fa9e1eaa4c22b81334"><a name="a0e4c3645c82a45fa9e1eaa4c22b81334"></a><a name="a0e4c3645c82a45fa9e1eaa4c22b81334"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a44deb138db2c49efa7774ea8f2297685"><a name="a44deb138db2c49efa7774ea8f2297685"></a><a name="a44deb138db2c49efa7774ea8f2297685"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="rca8acda81d53471583ef4fd4f092fcd4"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a60bf6f445cf44767899c16af3efdeeb0"><a name="a60bf6f445cf44767899c16af3efdeeb0"></a><a name="a60bf6f445cf44767899c16af3efdeeb0"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a173e1a558f5e4b24b86b89a71e466941"><a name="a173e1a558f5e4b24b86b89a71e466941"></a><a name="a173e1a558f5e4b24b86b89a71e466941"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
<tr id="r319a7c44454145b3931a482b7c129c44"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="aca44837446b04133a95ea9c8ce4e0f8f"><a name="aca44837446b04133a95ea9c8ce4e0f8f"></a><a name="aca44837446b04133a95ea9c8ce4e0f8f"></a>PartitionName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="ac9d3ba4471964935841bf43c8641b712"><a name="ac9d3ba4471964935841bf43c8641b712"></a><a name="ac9d3ba4471964935841bf43c8641b712"></a>Specifies the disk partition for which the alarm is generated.</p>
</td>
</tr>
<tr id="r3899e28c251b4795bbf3596465ebd37d"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a3661984072fa4dfaa5954887a87c90f4"><a name="a3661984072fa4dfaa5954887a87c90f4"></a><a name="a3661984072fa4dfaa5954887a87c90f4"></a>Trigger Condition</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a76903c41484b41bdb59ea7f000a0ca56"><a name="a76903c41484b41bdb59ea7f000a0ca56"></a><a name="a76903c41484b41bdb59ea7f000a0ca56"></a>Generates an alarm when the actual indicator value exceeds the specified threshold.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="sa5603184a13640f390983a0b62b11b0f"></a>

Data cannot be properly written to the file system.

## Possible Causes<a name="s24fca19098154896af5070a0420864de"></a>

-   Massive small files are stored in the disk.
-   The system is abnormal.

## Procedure<a name="se8eadf0686794c5f8214423497218ff7"></a>

**Massive small files are stored in the disk.**

1.  On MRS Manager, click the alarm in the real-time alarm list. In the  **Alarm Details**  area, obtain the IP address of the host and the disk partition for which the alarm is generated.
2.  Use PuTTY to log in to the host for which the alarm is generated as user  **root**.
3.  Run the  **df -i** _partition name_  command to check the current disk Inode usage.
4.  If the Inode usage exceeds the threshold, manually check small files stored in the disk partition and confirm whether these small files can be deleted.
    -   If yes, delete files and go to  [5](#l9747dd5736ab4833b9bc103fcf469b1a).
    -   If no, adjust the capacity. For details, see the  _FusionInsight HD Capacity Adjustment Guide_. Go to  [6](#l62858124a09941b0a6f263e970dd9642).

5.  <a name="l9747dd5736ab4833b9bc103fcf469b1a"></a>Wait 5 minutes and check whether the alarm is cleared.
    -   If yes, no further action is required.
    -   If no, go to  [6](#l62858124a09941b0a6f263e970dd9642).


**Check whether the system environment is abnormal.**

1.  <a name="l62858124a09941b0a6f263e970dd9642"></a>Contact the operating system maintenance personnel to check whether the operating system is abnormal.
    -   If yes, go to  [7](#l9d1fa963652d43e7a02cfa78a25463a8)  to rectify the fault.
    -   If no, go to  [9](#l71bfaa810f464682b1bb0dd32f6bb8da).

2.  <a name="l9d1fa963652d43e7a02cfa78a25463a8"></a>Wait 5 minutes and check whether the alarm is cleared.
    -   If yes, no further action is required.
    -   If no, go to  [9](#l71bfaa810f464682b1bb0dd32f6bb8da).


**Collect fault information.**

1.  On MRS Manager, choose  **System**  \>  **Export Log**.
2.  <a name="l71bfaa810f464682b1bb0dd32f6bb8da"></a>Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).

## Related Information<a name="s28b48d74966243d1ad902701b043be15"></a>

N/A


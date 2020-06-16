# ALM-12017 Insufficient Disk Capacity<a name="EN-US_TOPIC_0125375199"></a>

## Description<a name="sa64df5041e7743f8817fe5d5949bf9a7"></a>

The system checks the host disk usage every 30 seconds and compares it with the threshold. This alarm is generated when the host disk usage exceeds the specified threshold and is cleared when the host disk usage is less than or equal to the threshold.

## Attribute<a name="s596042c704ef4db0b90e8dac19d40122"></a>

<a name="te198088b168745aa8b9f388249248935"></a>
<table><thead align="left"><tr id="r4dbb2f93971142ef9b520d2a4dcb70cd"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="ac8c579b7ba494ca98c90cb5e63a89f55"><a name="ac8c579b7ba494ca98c90cb5e63a89f55"></a><a name="ac8c579b7ba494ca98c90cb5e63a89f55"></a><strong id="a03a98a1857c3469384bf2d6fb207ad12"><a name="a03a98a1857c3469384bf2d6fb207ad12"></a><a name="a03a98a1857c3469384bf2d6fb207ad12"></a>Alarm ID</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="a3a097177cf734f4bbaad338b7cf1fac2"><a name="a3a097177cf734f4bbaad338b7cf1fac2"></a><a name="a3a097177cf734f4bbaad338b7cf1fac2"></a><strong id="a0d5b78fafad741a0bdcedfc6bd76616d"><a name="a0d5b78fafad741a0bdcedfc6bd76616d"></a><a name="a0d5b78fafad741a0bdcedfc6bd76616d"></a>Alarm Severity</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="a169cd7eeb4274a26b5769c7ce1be42d5"><a name="a169cd7eeb4274a26b5769c7ce1be42d5"></a><a name="a169cd7eeb4274a26b5769c7ce1be42d5"></a><strong id="a888c2dd5315a40b3b02e64abe5c25e5f"><a name="a888c2dd5315a40b3b02e64abe5c25e5f"></a><a name="a888c2dd5315a40b3b02e64abe5c25e5f"></a>Automatically Cleared</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="rd4cac1809c9d46b7ad0fa5370a384e5b"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0035498391_p688022102139"><a name="en-us_topic_0035498391_p688022102139"></a><a name="en-us_topic_0035498391_p688022102139"></a>12017</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="a1633dab02b58453284a98d2370201e2b"><a name="a1633dab02b58453284a98d2370201e2b"></a><a name="a1633dab02b58453284a98d2370201e2b"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="a8cea8945256144a9b250affb658f9f63"><a name="a8cea8945256144a9b250affb658f9f63"></a><a name="a8cea8945256144a9b250affb658f9f63"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="se4f96a7e92e44461a79085831bc17a40"></a>

<a name="tcd790fba7eb442c89e07b838d9054e3f"></a>
<table><thead align="left"><tr id="r1112f649654249d0b577ba3c1b489ac7"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="a798fff21f9824e33ab1815e6badbdb6e"><a name="a798fff21f9824e33ab1815e6badbdb6e"></a><a name="a798fff21f9824e33ab1815e6badbdb6e"></a><strong id="a4286dafd49d048a59967e75b98ccb926"><a name="a4286dafd49d048a59967e75b98ccb926"></a><a name="a4286dafd49d048a59967e75b98ccb926"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="a6cda45ef120747e2a3a8db73df7f5dbd"><a name="a6cda45ef120747e2a3a8db73df7f5dbd"></a><a name="a6cda45ef120747e2a3a8db73df7f5dbd"></a><strong id="a917a7e196f234361b72d477ad8ea2e0f"><a name="a917a7e196f234361b72d477ad8ea2e0f"></a><a name="a917a7e196f234361b72d477ad8ea2e0f"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="rb6981fa67fc44ea7828a39bc12dfc1b3"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="ac41873b50e894631b406341b50ed88a2"><a name="ac41873b50e894631b406341b50ed88a2"></a><a name="ac41873b50e894631b406341b50ed88a2"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a3b615b6183004b34885533c508e7a488"><a name="a3b615b6183004b34885533c508e7a488"></a><a name="a3b615b6183004b34885533c508e7a488"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="r7f57a390ca1943fd9cc465b8c25f9742"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="adfec90665f5a42b984419b445b7454ee"><a name="adfec90665f5a42b984419b445b7454ee"></a><a name="adfec90665f5a42b984419b445b7454ee"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="ada66e25504e14688b60d0e5477e9024e"><a name="ada66e25504e14688b60d0e5477e9024e"></a><a name="ada66e25504e14688b60d0e5477e9024e"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="reddb2dc994b24b14b19aea08d3a43a2c"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a1ea198ab272f439b956e4737081543df"><a name="a1ea198ab272f439b956e4737081543df"></a><a name="a1ea198ab272f439b956e4737081543df"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="acfc9e95637a84fb8a44ea28dcfac318f"><a name="acfc9e95637a84fb8a44ea28dcfac318f"></a><a name="acfc9e95637a84fb8a44ea28dcfac318f"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
<tr id="r4b847eeda19349b2a025d54b110ada24"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a8d179a316af24caa86e844422352588a"><a name="a8d179a316af24caa86e844422352588a"></a><a name="a8d179a316af24caa86e844422352588a"></a>PartitionName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="acc00755a3b434362b118b41dd3898a59"><a name="acc00755a3b434362b118b41dd3898a59"></a><a name="acc00755a3b434362b118b41dd3898a59"></a>Specifies the disk partition for which the alarm is generated.</p>
</td>
</tr>
<tr id="r7f1fcbb128dd47ee954b7fff46a0d625"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a786c85ae7b7a414b8845d9b049f4c6b4"><a name="a786c85ae7b7a414b8845d9b049f4c6b4"></a><a name="a786c85ae7b7a414b8845d9b049f4c6b4"></a>Trigger Condition</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a26f403237762441e898ec51aaff1ce86"><a name="a26f403237762441e898ec51aaff1ce86"></a><a name="a26f403237762441e898ec51aaff1ce86"></a>Generates an alarm when the actual indicator value exceeds the specified threshold.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s0ebd961aea224fa18c511f36f874fd3b"></a>

Service processes become unavailable.

## Possible Causes<a name="s6e8970ba74834a23978e806d01fb1407"></a>

The disk configuration does not meet service requirements. As a result, the disk usage reaches the upper limit.

## Procedure<a name="seadaba80d58b4698a0baa958940823e1"></a>

1.  Log in to MRS Manager and check whether the alarm threshold is appropriate.
    -   If yes, go to  [2](#l51821eb7dc724d49b61635acbd894267).
    -   If no, go to  [1.a](#l8caee3b8650f4c5a9e5556172e4d2ecc).

    1.  <a name="l8caee3b8650f4c5a9e5556172e4d2ecc"></a>Choose  **System**  \>  **Configure Alarm Threshold**  \>  **Device**  \>  **Disk**  \>  **Disk Usage**  \>  **Disk Usage**  and change the alarm threshold based on the actual disk usage.
    2.  Wait 2 minutes and check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [2](#l51821eb7dc724d49b61635acbd894267).

2.  <a name="l51821eb7dc724d49b61635acbd894267"></a>Check whether the disk is a system disk.
    1.  <a name="l68dc7e03244a4ec3a8e103aa7f189992"></a>In the alarm list on MRS Manager, locate the row that contains the alarm, and view its host name and disk partition information in the alarm details.
    2.  Log in to the alarm node.
    3.  Run the  **df -h** command to check the system disk partition usage. Check whether the disk is mounted to the following directories based on the disk partition name obtained in [2.a](#l68dc7e03244a4ec3a8e103aa7f189992): **/**, **/boot**, **/home**, **/opt**, **/tmp**, **/var**, **/var/log**, **/boot**, and **/srv/BigData**.
        -   If yes, the disk is a system disk. Go to  [3.a](#lcbe14846b44542b4af063d17ce265a98).
        -   If no, the disk is not a system disk. Go to  [2.d](#l136aa407ceb84f23a4eb4f06ab3df6a9).

    4.  <a name="l136aa407ceb84f23a4eb4f06ab3df6a9"></a>Run the  **df -h** command to check the system disk partition usage. Determine the role of the disk based on the disk partition name obtained in [2.a](#l68dc7e03244a4ec3a8e103aa7f189992).
    5.  Check whether the disk is used by HDFS or Yarn.
        -   If yes, expand the disk capacity for the Core node. Go to  [2.f](#l46d3881e68de4900a5ed8d090b34dc6b).
        -   If no, go to  [4](#l8f1390e01f9844f2a9fe064dd5cb5fd2).

    6.  <a name="l46d3881e68de4900a5ed8d090b34dc6b"></a>Wait 2 minutes and check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [3](#l35081fb7c2854ccabafcf884404bc42a).

3.  <a name="l35081fb7c2854ccabafcf884404bc42a"></a>Check whether a large file is written to the disk.
    1.  <a name="lcbe14846b44542b4af063d17ce265a98"></a>Run the  **find / -xdev -size +500M -exec ls -l \{\} \\;**  command to view files larger than 500 MB on the node. Check whether these files are written to the disk.
        -   If yes, go to  [3.b](#l82908da420764aa389eccb1969c804b8).
        -   If no, go to  [4](#l8f1390e01f9844f2a9fe064dd5cb5fd2).

    2.  <a name="l82908da420764aa389eccb1969c804b8"></a>Process the large files and check whether the alarm is cleared after 2 minutes.
        -   If yes, no further action is required.
        -   If no, go to  [4](#l8f1390e01f9844f2a9fe064dd5cb5fd2).

    3.  Expand the disk capacity.
    4.  Wait 2 minutes and check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [4](#l8f1390e01f9844f2a9fe064dd5cb5fd2).

4.  <a name="l8f1390e01f9844f2a9fe064dd5cb5fd2"></a>Collect fault information.
    1.  On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## **Related Information**<a name="sf76041e8478e4b72860bb15f22422427"></a>

N/A


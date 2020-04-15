# ALM-14011 HDFS DataNode Data Directory Is Not Configured Properly<a name="EN-US_TOPIC_0125375381"></a>

## Description<a name="s68c68afb99884c5fa965cb75c55acd9b"></a>

The DataNode parameter  **dfs.datanode.data.dir**  specifies DataNode data directories. This alarm is generated in any of the following scenarios:

-   A configured data directory cannot be created.
-   A data directory uses the same disk as other critical directories in the system.
-   Multiple directories use the same disk.

This alarm is cleared when the DataNode data directory is configured properly and this DataNode is restarted.

## Attribute<a name="sc88a89b6f3b94ea3b3b2f46d9b7b99ee"></a>

<a name="ta6ba86190b6148c2b2cc0ec961302517"></a>
<table><thead align="left"><tr id="rc615aa9dcc9f49caaca76de19629e5e8"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="a7d6dbdf387a3423488aad001f5a50586"><a name="a7d6dbdf387a3423488aad001f5a50586"></a><a name="a7d6dbdf387a3423488aad001f5a50586"></a>Alarm ID</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="adfa146528fc647489e635215fc39340f"><a name="adfa146528fc647489e635215fc39340f"></a><a name="adfa146528fc647489e635215fc39340f"></a>Alarm Severity</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="a7e4e985cd9c148a8a3c42481f28fd816"><a name="a7e4e985cd9c148a8a3c42481f28fd816"></a><a name="a7e4e985cd9c148a8a3c42481f28fd816"></a>Automatically Cleared</p>
</th>
</tr>
</thead>
<tbody><tr id="r19835ec4c25949cca1473da1495eec0e"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="a30a420e4718d42f285a9c26dc3ef79c7"><a name="a30a420e4718d42f285a9c26dc3ef79c7"></a><a name="a30a420e4718d42f285a9c26dc3ef79c7"></a>14011</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="aac80e044509547c38a6b8e2a94ba988a"><a name="aac80e044509547c38a6b8e2a94ba988a"></a><a name="aac80e044509547c38a6b8e2a94ba988a"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="a30e5f4db9fb44a65a3affc69adfabc9c"><a name="a30e5f4db9fb44a65a3affc69adfabc9c"></a><a name="a30e5f4db9fb44a65a3affc69adfabc9c"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s5b8a190ba12e4483acf0951d2f92806e"></a>

<a name="t2ba1eb22983b4fefb1cfa775c528a6e3"></a>
<table><thead align="left"><tr id="rb55eb7cff7724f98b1db006c5b046918"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="ae286427a45cb49e1909fecfc9cf2935e"><a name="ae286427a45cb49e1909fecfc9cf2935e"></a><a name="ae286427a45cb49e1909fecfc9cf2935e"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="a3762f0bdf1164dca8c5890d00e41b80e"><a name="a3762f0bdf1164dca8c5890d00e41b80e"></a><a name="a3762f0bdf1164dca8c5890d00e41b80e"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="r51cb586e0ecc4e9483326360dfc54190"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a8069f2151eab4c4eb62f4dd4072237dd"><a name="a8069f2151eab4c4eb62f4dd4072237dd"></a><a name="a8069f2151eab4c4eb62f4dd4072237dd"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a7ce09e24d5504381b74615f8244ff65b"><a name="a7ce09e24d5504381b74615f8244ff65b"></a><a name="a7ce09e24d5504381b74615f8244ff65b"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="r9cb2a9a9d67443a2ae1cb6df5ffa8474"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="ad84ae78c7c654d4b862119e2ef432da4"><a name="ad84ae78c7c654d4b862119e2ef432da4"></a><a name="ad84ae78c7c654d4b862119e2ef432da4"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a5e93c17e963c4b7398c457ffaeb8daea"><a name="a5e93c17e963c4b7398c457ffaeb8daea"></a><a name="a5e93c17e963c4b7398c457ffaeb8daea"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="rea6f05caf458423fb9577dfda4ce2dc2"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a112821e0ecdd4316a4373f196a7e39f5"><a name="a112821e0ecdd4316a4373f196a7e39f5"></a><a name="a112821e0ecdd4316a4373f196a7e39f5"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a521a15e4db984c5b9b8f38e0ebeebac6"><a name="a521a15e4db984c5b9b8f38e0ebeebac6"></a><a name="a521a15e4db984c5b9b8f38e0ebeebac6"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="sd400057b00974761bdc0f7db01e0f660"></a>

If the DataNode data directory is mounted on critical directories such as the root directory, the disk space of the root directory will be used up after running for a long time. This causes a system fault.

If the DataNode data directory is not configured properly, HDFS performance will deteriorate.

## Possible Causes<a name="s892348f47acb41c0873c57b3434b8e1d"></a>

-   The DataNode data directory fails to be created.
-   The DataNode data directory uses the same disk as critical directories, such as  **/** or **/boot**.
-   Multiple directories in the DataNode data directory use the same disk.

## Procedure<a name="s71c43c21dab84104841aadefd1af156f"></a>

1.  Check the alarm cause and information about the DataNode that generated the alarm.
    1.  On the MRS Manager portal, click  **Alarm**. In the alarm list, click the alarm.
    2.  In the  **Alarm Details** area, view **Alarm Cause**. In **HostName** of **Location**, obtain the host name of the DataNode that generated the alarm.

2.  Delete directories that do not comply with the disk plan from the DataNode data directory.
    1.  Choose  **Service** \> **HDFS** \> **Instance**. In the instance list, click the DataNode instance on the alarm node.
    2.  Click  **Instance Configuration** and view the value of the DataNode parameter **dfs.datanode.data.dir**.
    3.  Check whether all DataNode data directories are consistent with the disk plan.
        -   If yes, go to  [2.d](#l0c059b812240426d83afc374699b5c6c).
        -   If no, go to  [2.g](#l6f844519850a4c12921b610a8cca896f).

    4.  <a name="l0c059b812240426d83afc374699b5c6c"></a>Modify the DataNode parameter  **dfs.datanode.data.dir**  and delete the incorrect directories.
    5.  Choose  **Service** \> **HDFS** \> **Instance**  and restart the DataNode instance.
    6.  Check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [2.g](#l6f844519850a4c12921b610a8cca896f).

    7.  <a name="l6f844519850a4c12921b610a8cca896f"></a>Log in to the DataNode that generated the alarm.
        -   If the alarm cause is "The DataNode data directory fails to be created", go to  [3.a](#ld362f856ca5c42a7b5c5df5b20ac250d).
        -   If the alarm cause is "The DataNode data directory uses the same disk as critical directories, such  **/** or **/boot**", go to [4.a](#l83470eec4d6041c1a3a0181cd7f6d89e).
        -   If the alarm cause is "Multiple directories in the DataNode data directory use the same disk", go to  [5.a](#l9e21d99b940940c9b077b4fb7c062aef).

3.  Check whether the DataNode data directory is created.
    1.  <a name="ld362f856ca5c42a7b5c5df5b20ac250d"></a>Run the following command to switch the user:

        **sudo su - root**

        **su - omm**

    2.  Run the  **ls**  command to check whether the directories exist in the DataNode data directory.
        -   If yes, go to  [7](#l2e597fb9523d49ac8a3b0b6aecbeaac4).
        -   If no, go to  [3.c](#l20426dd5bbc745a4a759883ccbc96889).

    3.  <a name="l20426dd5bbc745a4a759883ccbc96889"></a>Run the  **mkdir** _data directory_  command to create a directory. Check whether the directory is successfully created.
        -   If yes, go to  [6.a](#l37377783214f49b1bd0ecade99b09b16).
        -   If no, go to  [3.d](#lf7031d68bb44488da81cf921467eb03a).

    1.  <a name="lf7031d68bb44488da81cf921467eb03a"></a>On the MRS Manager portal, click  **Alarm**  to check whether alarm  **ALM-12017 Insufficient Disk Capacity**  exists.
        -   If yes, go to  [3.e](#lad07f29ea8e143b39b3c383436b758f5).
        -   If no, go to  [3.f](#l21d37fc5dea547dbb026633e0edac4c4).

    2.  <a name="lad07f29ea8e143b39b3c383436b758f5"></a>Adjust the disk capacity and check whether alarm  **ALM-12017 Insufficient Disk Capacity** is cleared. For details, see [ALM-12017 Insufficient Disk Capacity](alm-12017-insufficient-disk-capacity.md).
        -   If yes, go to  [3.c](#l20426dd5bbc745a4a759883ccbc96889).
        -   If no, go to  [7](#l2e597fb9523d49ac8a3b0b6aecbeaac4).

    3.  <a name="l21d37fc5dea547dbb026633e0edac4c4"></a>Check whether user  **omm** has the **rwx** or **x**  permission for all upper-layer directories of the directory. For example, for  **/tmp/abc/**, user **omm** has the **x** permission for the **tmp** directory and the **rwx** permission for the **abc**  directory.
        -   If yes, go to  [6.a](#l37377783214f49b1bd0ecade99b09b16).
        -   If no, go to  [3.g](#la745937080e94ca89ce539fccd8f2355).

    4.  <a name="la745937080e94ca89ce539fccd8f2355"></a>Run the  **chmod u+rwx** _path_ or **chmod u+x** _path_ command as user **root** to assign the **rwx** or **x**  permission to user  **omm**. Go to [3.c](#l20426dd5bbc745a4a759883ccbc96889).

4.  Check whether the DataNode data directory uses the same disk as other critical directories in the system.
    1.  <a name="l83470eec4d6041c1a3a0181cd7f6d89e"></a>Run the  **df**  command to obtain the disk mounting information of each directory in the DataNode data directory.
    2.  Check whether the directories mounted on the disk are critical directories, such as  **/** or **/boot**.
        -   If yes, go to  [4.c](#l00608122bd6445bc967b437813f11e01).
        -   If no, go to  [6.a](#l37377783214f49b1bd0ecade99b09b16).

    3.  <a name="l00608122bd6445bc967b437813f11e01"></a>Change the value of the DataNode parameter  **dfs.datanode.data.dir**  and delete the directories that use the same disk as critical directories.
    4.  Go to  [6.a](#l37377783214f49b1bd0ecade99b09b16).

5.  Check whether multiple directories in the DataNode data directory use the same disk.
    1.  <a name="l9e21d99b940940c9b077b4fb7c062aef"></a>Run the  **df**  command to obtain the disk mounting information of each directory in the DataNode data directory. Record the mounted directory in the command output.
    2.  Modify the DataNode parameter  **dfs.datanode.data.dir**  to reserve one of the directories mounted on the same disk directory.
    3.  Go to  [6.a](#l37377783214f49b1bd0ecade99b09b16).

6.  Restart the DataNode and check whether the alarm is cleared.
    1.  <a name="l37377783214f49b1bd0ecade99b09b16"></a>On the MRS Manager portal, choose  **Service** \> **HDFS** \> **Instance**  and restart the DataNode instance.
    2.  Check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [7](#l2e597fb9523d49ac8a3b0b6aecbeaac4).

7.  <a name="l2e597fb9523d49ac8a3b0b6aecbeaac4"></a>Collect fault information.
    1.  On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="s983d800595a24198a5a68cb1ce77da56"></a>

N/A


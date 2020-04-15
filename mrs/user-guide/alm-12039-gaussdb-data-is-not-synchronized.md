# ALM-12039 GaussDB Data Is Not Synchronized<a name="EN-US_TOPIC_0125375763"></a>

## Description<a name="s1fc5083b928040c291f4efd9ed8c770c"></a>

The system checks the data synchronization status between the active and standby GaussDBs every 10 seconds. This alarm is generated when the synchronization status cannot be queried six times consecutively or when the synchronization status is abnormal.

This alarm is cleared when data synchronization is normal.

## Attribute<a name="s7128172730b94762bef1e72cf32e5b00"></a>

<a name="t9fa60cac644743479fce6655127ae23b"></a>
<table><thead align="left"><tr id="r2396a3243d2248608a036a5c4f164d52"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="a8b26110d8e4f485291cf9e55ec47b7ce"><a name="a8b26110d8e4f485291cf9e55ec47b7ce"></a><a name="a8b26110d8e4f485291cf9e55ec47b7ce"></a><strong id="a17d7460ba2bd4ba086643912cf16ff1a"><a name="a17d7460ba2bd4ba086643912cf16ff1a"></a><a name="a17d7460ba2bd4ba086643912cf16ff1a"></a>Alarm ID</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="aac835bf5b6de42bd84c5a1b80eae6833"><a name="aac835bf5b6de42bd84c5a1b80eae6833"></a><a name="aac835bf5b6de42bd84c5a1b80eae6833"></a><strong id="aa591b22817f54c5681f6928fc05029c0"><a name="aa591b22817f54c5681f6928fc05029c0"></a><a name="aa591b22817f54c5681f6928fc05029c0"></a>Alarm Severity</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="a72d4856a5d9d49c98e3640a95432ef61"><a name="a72d4856a5d9d49c98e3640a95432ef61"></a><a name="a72d4856a5d9d49c98e3640a95432ef61"></a><strong id="a4ba46a915598418d91cb0f8c2e775597"><a name="a4ba46a915598418d91cb0f8c2e775597"></a><a name="a4ba46a915598418d91cb0f8c2e775597"></a>Automatically Cleared</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="rbb01e5edcfe84e619df16e6f00da547e"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="a73e36ae1dcca426eb6bb8a4c025c4cfd"><a name="a73e36ae1dcca426eb6bb8a4c025c4cfd"></a><a name="a73e36ae1dcca426eb6bb8a4c025c4cfd"></a>12039</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="a4ddee237972f4bb0ba6e09bfae65fda1"><a name="a4ddee237972f4bb0ba6e09bfae65fda1"></a><a name="a4ddee237972f4bb0ba6e09bfae65fda1"></a>Critical</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="a4f196225e1ab454eaf5bcd1676ee054e"><a name="a4f196225e1ab454eaf5bcd1676ee054e"></a><a name="a4f196225e1ab454eaf5bcd1676ee054e"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="sf7652651b8734f40bb0c6416d275c8fd"></a>

<a name="t593d5a28a98d42be9d24c302f492a5a7"></a>
<table><thead align="left"><tr id="r7f2414ec556143a9a67d094fe99099be"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="ae134cb0f9092490ab9081d4ba8b76655"><a name="ae134cb0f9092490ab9081d4ba8b76655"></a><a name="ae134cb0f9092490ab9081d4ba8b76655"></a><strong id="aa48b989df0d14c8aae7fdb4282d3bc52"><a name="aa48b989df0d14c8aae7fdb4282d3bc52"></a><a name="aa48b989df0d14c8aae7fdb4282d3bc52"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="a567cc293bcb0447082accf6df3dca82c"><a name="a567cc293bcb0447082accf6df3dca82c"></a><a name="a567cc293bcb0447082accf6df3dca82c"></a><strong id="ac5b31477c9db47749ea9e4cb76365362"><a name="ac5b31477c9db47749ea9e4cb76365362"></a><a name="ac5b31477c9db47749ea9e4cb76365362"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="rc157e86ab08b435393c90e8a24e19535"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a4b08263af0ac4d86bf9a6da631695d4e"><a name="a4b08263af0ac4d86bf9a6da631695d4e"></a><a name="a4b08263af0ac4d86bf9a6da631695d4e"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a052c574a79fa43539918047822c27f60"><a name="a052c574a79fa43539918047822c27f60"></a><a name="a052c574a79fa43539918047822c27f60"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="r557c5a8126c84d4e8e156b0d985380a9"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a164a09e60cf34f07a56145232de4688a"><a name="a164a09e60cf34f07a56145232de4688a"></a><a name="a164a09e60cf34f07a56145232de4688a"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a808cc29b205e408b8721b341e4b140c1"><a name="a808cc29b205e408b8721b341e4b140c1"></a><a name="a808cc29b205e408b8721b341e4b140c1"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="r28c882812de64baa88ca64279dbeb588"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a720f239808bf44e1ba22d306f3df68d5"><a name="a720f239808bf44e1ba22d306f3df68d5"></a><a name="a720f239808bf44e1ba22d306f3df68d5"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="abdea9433d70f4fcebd5f1ecc9d1c259b"><a name="abdea9433d70f4fcebd5f1ecc9d1c259b"></a><a name="abdea9433d70f4fcebd5f1ecc9d1c259b"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
<tr id="ra3fdb84500bc418381e58b1f9157b2ab"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a220561d8b4be45d48a69cac9952dae74"><a name="a220561d8b4be45d48a69cac9952dae74"></a><a name="a220561d8b4be45d48a69cac9952dae74"></a>Local GaussDB HA IP</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035546889_p541922172753"><a name="en-us_topic_0035546889_p541922172753"></a><a name="en-us_topic_0035546889_p541922172753"></a>Specifies the HA IP address of the local GaussDB.</p>
</td>
</tr>
<tr id="r99f748d52b8a444a8e853a4a01cd174a"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="af6035dd9800b42e2b1f393a82d398562"><a name="af6035dd9800b42e2b1f393a82d398562"></a><a name="af6035dd9800b42e2b1f393a82d398562"></a>Peer GaussDB HA IP</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a4e172a9f10cf45dcb4ba650c9a4e2344"><a name="a4e172a9f10cf45dcb4ba650c9a4e2344"></a><a name="a4e172a9f10cf45dcb4ba650c9a4e2344"></a>Specifies the HA IP address of the peer GaussDB.</p>
</td>
</tr>
<tr id="r76a436b89b5141d5b74a17d231dee437"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035546889_p41256172753"><a name="en-us_topic_0035546889_p41256172753"></a><a name="en-us_topic_0035546889_p41256172753"></a>SYNC_PERSENT</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a1a18a50702a64992bb8a0c1dfbd5db9d"><a name="a1a18a50702a64992bb8a0c1dfbd5db9d"></a><a name="a1a18a50702a64992bb8a0c1dfbd5db9d"></a>Specifies the synchronization percentage.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s1b83f471fc4544dc942e755f41626fad"></a>

If the active instance becomes abnormal while data is not synchronized between the active and standby GaussDBs, data may be lost or abnormal.

## Possible Causes<a name="s770a183eced04b74b0f469453f31b3b7"></a>

-   The network between the active and standby nodes is unstable.
-   The standby GaussDB is abnormal.
-   The disk space of the standby node is full.

## Procedure<a name="se971d4bc08cb45aa99b25c7733bdae40"></a>

1.  Log in to MRS Manager, click  **Alarm**, locate the row that contains the alarm, and view the IP address of the standby GaussDB in the alarm details.
2.  Log in to the active management node.
3.  Run the following command to check whether the standby GaussDB is reachable:

    **ping** _heartbeat IP address of the standby GaussDB_

    If yes, go to  [6](#l7f980008967646779cfc2c50814ccb2e).

    If no, go to  [4](#lc18c4ee25ddf4aeea458edda74d4c8a2).

4.  <a name="lc18c4ee25ddf4aeea458edda74d4c8a2"></a>Contact the public cloud O&M personnel to check whether the network is faulty.
    -   If yes, go to  [5](#l348eaff2430e405fba12b9432dc9f599).
    -   If no, go to  [6](#l7f980008967646779cfc2c50814ccb2e).

5.  <a name="l348eaff2430e405fba12b9432dc9f599"></a>Rectify the network fault and check whether the alarm is cleared from the alarm list.
    -   If yes, no further action is required.
    -   If no, go to  [6](#l7f980008967646779cfc2c50814ccb2e).

6.  <a name="l7f980008967646779cfc2c50814ccb2e"></a>Log in to the standby GaussDB node.
7.  Run the following command to switch the user:

    **sudo su - root**

    **su - omm**

8.  Go to the  **$\{BIGDATA\_HOME\}/om-0.0.1/sbin/**  directory.

    Run the following command to check whether the resource status of the standby GaussDB is normal:

    **sh status-oms.sh**

    In the command output, check whether the following information is displayed in the row where  **ResName** is **gaussDB**:

    ```
    10_10_10_231 gaussDB Standby_normal Normal Active_standby
    ```

    -   If yes, go to  [9](#l1db02af4bc9241a8ba73439346ceb70d).
    -   If no, go to  [15](#l22dc3fea6ec2410a9ddd4a62b71811fb).


1.  <a name="l1db02af4bc9241a8ba73439346ceb70d"></a>Log in to the standby GaussDB node.
2.  Run the following command to switch the user:

    **sudo su - root**

    **su - omm**

3.  Run the  **echo $\{BIGDATA\_DATA\_HOME\}/dbdata\_om**  command to obtain the GaussDB data directory.
4.  Run the  **df -h**  command to check the system disk partition usage.
5.  Check whether the disk on which the GaussDB data directory is mounted is full.
    -   If yes, go to  [14](#l416ddabe128243478e18376cc688855f).
    -   If no, go to  [15](#l22dc3fea6ec2410a9ddd4a62b71811fb).

6.  <a name="l416ddabe128243478e18376cc688855f"></a>Contact the public cloud O&M personnel to expand the disk capacity. After capacity expansion, wait 2 minutes and check whether the alarm is cleared.
    -   If yes, no further action is required.
    -   If no, go to  [15](#l22dc3fea6ec2410a9ddd4a62b71811fb).

7.  <a name="l22dc3fea6ec2410a9ddd4a62b71811fb"></a>Collect fault information.
    1.  On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="s4602a60862354904a1bfd99755eae2fe"></a>

N/A


# ALM-19006 HBase Replication Synchronization Failed<a name="EN-US_TOPIC_0125375415"></a>

## Description<a name="s126c9913a8cf447389fb4482bfc158ef"></a>

This alarm is generated when disaster recovery \(DR\) data fails to be synchronized to a standby cluster. It is cleared when DR data is successfully synchronized.

## Attribute<a name="s614cb0e74e9341fe8407fac0697b56c4"></a>

<a name="en-us_topic_0035998741_table57434139"></a>
<table><thead align="left"><tr id="en-us_topic_0035998741_row461342"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="en-us_topic_0035998741_p37368736"><a name="en-us_topic_0035998741_p37368736"></a><a name="en-us_topic_0035998741_p37368736"></a>Alarm ID</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="en-us_topic_0035998741_p6968762"><a name="en-us_topic_0035998741_p6968762"></a><a name="en-us_topic_0035998741_p6968762"></a>Alarm Severity</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="en-us_topic_0035998741_p27598869"><a name="en-us_topic_0035998741_p27598869"></a><a name="en-us_topic_0035998741_p27598869"></a>Automatically Cleared</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998741_row20915929"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0035998741_p16468652"><a name="en-us_topic_0035998741_p16468652"></a><a name="en-us_topic_0035998741_p16468652"></a>19006</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0035998741_p58892473"><a name="en-us_topic_0035998741_p58892473"></a><a name="en-us_topic_0035998741_p58892473"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0035998741_p5560998"><a name="en-us_topic_0035998741_p5560998"></a><a name="en-us_topic_0035998741_p5560998"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s525b31f7143249b29e05d2b688e203fe"></a>

<a name="en-us_topic_0035998741_table47787675"></a>
<table><thead align="left"><tr id="en-us_topic_0035998741_row20947391"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0035998741_p19017142"><a name="en-us_topic_0035998741_p19017142"></a><a name="en-us_topic_0035998741_p19017142"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0035998741_p63993496"><a name="en-us_topic_0035998741_p63993496"></a><a name="en-us_topic_0035998741_p63993496"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998741_row16090703"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998741_p28278595"><a name="en-us_topic_0035998741_p28278595"></a><a name="en-us_topic_0035998741_p28278595"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998741_p8864859"><a name="en-us_topic_0035998741_p8864859"></a><a name="en-us_topic_0035998741_p8864859"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998741_row12674872"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998741_p20031746"><a name="en-us_topic_0035998741_p20031746"></a><a name="en-us_topic_0035998741_p20031746"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998741_p11958757"><a name="en-us_topic_0035998741_p11958757"></a><a name="en-us_topic_0035998741_p11958757"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998741_row40519951"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998741_p60890569"><a name="en-us_topic_0035998741_p60890569"></a><a name="en-us_topic_0035998741_p60890569"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998741_p33189039"><a name="en-us_topic_0035998741_p33189039"></a><a name="en-us_topic_0035998741_p33189039"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s62e3d57c4c8c4c738f7613f9cc02b7e2"></a>

HBase data in a cluster fails to be synchronized to the standby cluster, causing data inconsistency between active and standby clusters.

## Possible Causes<a name="s525aa3ce42744ee8aaf71178a7b7ebcb"></a>

-   The HBase service on the standby cluster is abnormal.
-   The network is abnormal.

## Procedure<a name="s8acf088839484c2db339cb1834c184eb"></a>

1.  Check whether the alarm is automatically cleared.
    1.  Log in to MRS Manager of the active cluster, and click  **Alarm**.
    2.  In the alarm list, click the alarm and obtain the alarm generation time from  **Generated On** in **Alarm Details**. Check whether the alarm persists for over 5 minutes.
        -   If yes, go to  [2.a](#en-us_topic_0035998741_status).
        -   If no, go to  [1.c](#en-us_topic_0035998741_step3).

    3.  <a name="en-us_topic_0035998741_step3"></a>Wait 5 minutes and check whether the alarm is automatically cleared.
        -   If yes, no further action is required.
        -   If no, go to  [2.a](#en-us_topic_0035998741_status).

2.  Check the HBase service status of the standby cluster.
    1.  <a name="en-us_topic_0035998741_status"></a>Log in to MRS Manager of the active cluster, and click  **Alarm**.
    2.  In the alarm list, click the alarm and obtain  **HostName** from **Location** in **Alarm Details**.
    3.  Log in to the node where the HBase client resides in the active cluster. Run the following command to switch the user:

        **sudo su - root**

        **su - omm**

    4.  Run the  **status 'replication', 'source'**  command to check the replication synchronization status of the faulty node.

        The replication synchronization status of a node is as follows.

        ```
        10-10-10-153: 
         SOURCE: PeerID=abc, SizeOfLogQueue=0, ShippedBatches=2, ShippedOps=2, ShippedBytes=320, LogReadInBytes=1636, LogEditsRead=5, LogEditsFiltered=3, SizeOfLogToReplicate=0, TimeForLogToReplicate=0, ShippedHFiles=0, SizeOfHFileRefsQueue=0, AgeOfLastShippedOp=0, TimeStampsOfLastShippedOp=Mon Jul 18 09:53:28 CST 2016, Replication Lag=0, FailedReplicationAttempts=0 
         SURCE: PeerID=abc1, SizeOfLogQueue=0, ShippedBatches=1, ShippedOps=1, ShippedBytes=160, LogReadInBytes=1636, LogEditsRead=5, LogEditsFiltered=3, SizeOfLogToReplicate=0, TimeForLogToReplicate=0, ShippedHFiles=0, SizeOfHFileRefsQueue=0, AgeOfLastShippedOp=16788, TimeStampsOfLastShippedOp=Sat Jul 16 13:19:00 CST 2016, Replication Lag=16788, FailedReplicationAttempts=5
        ```

    5.  Obtain  **PeerID**  corresponding to a record whose value of  **FailedReplicationAttempts**  is greater than 0.

        In the preceding step, data on faulty node 10-10-10-153 fails to be synchronized to a standby cluster whose  **PeerID** is **abc1**.

    6.  <a name="en-us_topic_0035998741_peerid"></a>Run the  **list\_peers** command to find the cluster and the HBase instance corresponding to the **PeerID**.

        ```
        PEER_ID CLUSTER_KEY STATE TABLE_CFS 
         abc1 10.10.10.110,10.10.10.119,10.10.10.133:24002:/hbase2 ENABLED  
         abc 10.10.10.110,10.10.10.119,10.10.10.133:24002:/hbase ENABLED 
        ```

        **/hbase2**  indicates that data is synchronized to the HBase2 instance of the standby cluster.

    7.  In the service list on MRS Manager of the standby cluster, check whether the health status of the HBase instance obtained in  [2.f](#en-us_topic_0035998741_peerid) is **Good**.
        -   If yes, go to  [3.a](#la3f11a329bb84642abcb5619eff3c221).
        -   If no, go to  [2.h](#en-us_topic_0035998741_alm-19000).

    8.  <a name="en-us_topic_0035998741_alm-19000"></a>In the alarm list, check whether alarm  **ALM-19000 HBase Service Unavailable**  exists.
        -   If yes, go to  [2.i](#l2d9ea324f37e4a1eaf456b10dadbdded).
        -   If no, go to  [3.a](#la3f11a329bb84642abcb5619eff3c221).

    9.  <a name="l2d9ea324f37e4a1eaf456b10dadbdded"></a>Rectify the fault by following the steps provided in  **ALM-19000 HBase Service Unavailable**.
    10. Wait several minutes and check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [3.a](#la3f11a329bb84642abcb5619eff3c221).

3.  Check the network connection between RegionServers on active and standby clusters.
    1.  <a name="la3f11a329bb84642abcb5619eff3c221"></a>Log in to MRS Manager of the active cluster, and click  **Alarm**.
    2.  In the alarm list, click the alarm and obtain  **HostName** from **Location** in **Alarm Details**.
    3.  Log in to the faulty RegionServer node.
    4.  Run the  **ping**  command to check whether the network connection between the faulty RegionServer node and the host where RegionServer of the standby cluster resides is in the normal state.
        -   If yes, go to  [4](#laef5eba4c3c9412bb010b7a54ed08766).
        -   If no, go to  [3.e](#en-us_topic_0035998741_s1).

    5.  <a name="en-us_topic_0035998741_s1"></a>Contact public cloud O&M personnel to recover the network.
    6.  After the network recovers, check whether the alarm is cleared in the alarm list.
        -   If yes, no further action is required.
        -   If no, go to  [4](#laef5eba4c3c9412bb010b7a54ed08766).

4.  <a name="laef5eba4c3c9412bb010b7a54ed08766"></a>Collect fault information.
    1.  On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="s16ada0691ac8495d87175a4051e5076b"></a>

N/A


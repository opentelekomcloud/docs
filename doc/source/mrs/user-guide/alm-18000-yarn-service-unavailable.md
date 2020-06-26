# ALM-18000 Yarn Service Unavailable<a name="EN-US_TOPIC_0125375206"></a>

## Description<a name="se691173983f34313b6cd48a2ff325791"></a>

The alarm module checks the Yarn service status every 30 seconds. This alarm is generated when the Yarn service is unavailable and is cleared when the Yarn service recovers.

## Attribute<a name="sb88f5100b29d473da557a912ba8e1167"></a>

<a name="en-us_topic_0035998736_table17937528"></a>
<table><thead align="left"><tr id="en-us_topic_0035998736_row57980147"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="en-us_topic_0035998736_p65880360"><a name="en-us_topic_0035998736_p65880360"></a><a name="en-us_topic_0035998736_p65880360"></a>Alarm ID</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="en-us_topic_0035998736_p34708966"><a name="en-us_topic_0035998736_p34708966"></a><a name="en-us_topic_0035998736_p34708966"></a>Alarm Severity</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="en-us_topic_0035998736_p59962836"><a name="en-us_topic_0035998736_p59962836"></a><a name="en-us_topic_0035998736_p59962836"></a>Automatically Cleared</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998736_row25151514"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0035998736_p24006753"><a name="en-us_topic_0035998736_p24006753"></a><a name="en-us_topic_0035998736_p24006753"></a>18000</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0035998736_p65498832"><a name="en-us_topic_0035998736_p65498832"></a><a name="en-us_topic_0035998736_p65498832"></a>Critical</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0035998736_p3805200"><a name="en-us_topic_0035998736_p3805200"></a><a name="en-us_topic_0035998736_p3805200"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s00ebe37761e342ba8f3cab8f63706108"></a>

<a name="en-us_topic_0035998736_table39785801"></a>
<table><thead align="left"><tr id="en-us_topic_0035998736_row31767774"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0035998736_p23052927"><a name="en-us_topic_0035998736_p23052927"></a><a name="en-us_topic_0035998736_p23052927"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0035998736_p55347837"><a name="en-us_topic_0035998736_p55347837"></a><a name="en-us_topic_0035998736_p55347837"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998736_row53989823"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998736_p11099566"><a name="en-us_topic_0035998736_p11099566"></a><a name="en-us_topic_0035998736_p11099566"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998736_p26649649"><a name="en-us_topic_0035998736_p26649649"></a><a name="en-us_topic_0035998736_p26649649"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998736_row38520254"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998736_p33132859"><a name="en-us_topic_0035998736_p33132859"></a><a name="en-us_topic_0035998736_p33132859"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998736_p66515904"><a name="en-us_topic_0035998736_p66515904"></a><a name="en-us_topic_0035998736_p66515904"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998736_row61772230"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998736_p37494699"><a name="en-us_topic_0035998736_p37494699"></a><a name="en-us_topic_0035998736_p37494699"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998736_p17171756"><a name="en-us_topic_0035998736_p17171756"></a><a name="en-us_topic_0035998736_p17171756"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s2bc3e63a78744656954501382ca0ff35"></a>

-   The cluster cannot provide the Yarn service.
-   Users cannot run new applications.
-   Submitted applications cannot be run.

## Possible Causes<a name="sfcaa7ba59cec452ca6a8eb1ff5c45ecc"></a>

-   The ZooKeeper service is abnormal.
-   The HDFS service is abnormal.
-   There is no active ResourceManager node in the Yarn cluster.
-   All NodeManager nodes in the Yarn cluster are abnormal.

## Procedure<a name="sf6ec6831356c4bc7b86db3e0e0f32f08"></a>

1.  Check the ZooKeeper service status.
    1.  In the alarm list on MRS Manager, check whether alarm  **ALM-13000 ZooKeeper Service Unavailable**  is generated.
        -   If yes, go to  [1.b](#l55cd8da61f0640b0bd1bd6db07ac0fbc).
        -   If no, go to  [2.a](#l25e96e07ada14aa0b8998794ac62abd8).

    2.  <a name="l55cd8da61f0640b0bd1bd6db07ac0fbc"></a>Rectify the fault by following the steps provided in  [ALM-13000 ZooKeeper Service Unavailable](alm-13000-zookeeper-service-unavailable.md), and check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [2.a](#l25e96e07ada14aa0b8998794ac62abd8).

2.  Check the HDFS service status.
    1.  <a name="l25e96e07ada14aa0b8998794ac62abd8"></a>In the alarm list on MRS Manager, check whether an alarm related to HDFS is generated.
        -   If yes, go to  [2.b](#l2d1974eda1d24512bc0022fb8a6a9d93).
        -   If no, go to  [3.a](#l465ab034b71144aabada8c8b470b3297).

    2.  <a name="l2d1974eda1d24512bc0022fb8a6a9d93"></a>Click  **Alarm**, and handle HDFS alarms according to Alarm Help. Check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [3.a](#l465ab034b71144aabada8c8b470b3297).

3.  Check the ResourceManager node status in the Yarn cluster.
    1.  <a name="l465ab034b71144aabada8c8b470b3297"></a>On MRS Manager, choose  **Service**  \>  **Yarn**.
    2.  In  **Yarn Summary**, check whether there is an active ResourceManager node in the Yarn cluster.
        -   If yes, go to  [4.a](#en-us_topic_0035998736_step_5).
        -   If no, go to  [5](#lb2dd0fafcdbb4b3c8b4acb73478ca82e).

4.  Check the NodeManager node status in the Yarn cluster.
    1.  <a name="en-us_topic_0035998736_step_5"></a>On MRS Manager, choose  **Service**  \>  **Yarn**  \>  **Instance**.
    2.  Check  **Health Status**  of NodeManager, and check whether there are unhealthy nodes.
        -   If yes, go to  [4.c](#lace20b8327914ab6b28d2669685ebf60).
        -   If no, go to  [5](#lb2dd0fafcdbb4b3c8b4acb73478ca82e).

    3.  <a name="lace20b8327914ab6b28d2669685ebf60"></a>Rectify the fault by following the steps provided in  [ALM-18002 NodeManager Heartbeat Lost](alm-18002-nodemanager-heartbeat-lost.md) or [ALM-18003 NodeManager Unhealthy](alm-18003-nodemanager-unhealthy.md). After the fault is rectified, check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [5](#lb2dd0fafcdbb4b3c8b4acb73478ca82e).

5.  <a name="lb2dd0fafcdbb4b3c8b4acb73478ca82e"></a>Collect fault information.
    1.  On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="sed6b11ca1ed64f4c8e44e05d3284c2fb"></a>

N/A


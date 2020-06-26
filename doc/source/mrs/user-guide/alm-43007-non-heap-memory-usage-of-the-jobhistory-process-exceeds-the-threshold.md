# ALM-43007 Non-Heap Memory Usage of the JobHistory Process Exceeds the Threshold<a name="EN-US_TOPIC_0125375654"></a>

## Description<a name="sd3d7dcbaec6349fb92768c17dc054c45"></a>

The system checks the non-heap memory usage of the JobHistory process every 30 seconds. The alarm is generated when the non-heap memory usage of the JobHistory process exceeds the threshold \(90% of the maximum memory\).

## Attribute<a name="seb00b73fb8d54b0b80cb2fe52d3f212b"></a>

<a name="t6b5a75b767d8410582050f1567cf9eff"></a>
<table><thead align="left"><tr id="r0189f7c1ca03493388e7955d106a73ba"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="a70c3042db5bf4c8aadbb0b4d4db3da62"><a name="a70c3042db5bf4c8aadbb0b4d4db3da62"></a><a name="a70c3042db5bf4c8aadbb0b4d4db3da62"></a>Alarm ID</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="a4da8c111245d40ab887123f06802d538"><a name="a4da8c111245d40ab887123f06802d538"></a><a name="a4da8c111245d40ab887123f06802d538"></a>Alarm Severity</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="a251b850d63ae4d1bbaebd26b78dae8b2"><a name="a251b850d63ae4d1bbaebd26b78dae8b2"></a><a name="a251b850d63ae4d1bbaebd26b78dae8b2"></a>Automatically Cleared</p>
</th>
</tr>
</thead>
<tbody><tr id="r4c4aa3d858204d0cbe512834f6d1d4bf"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="a3b14f84bc8c846a89e2e3624047994dc"><a name="a3b14f84bc8c846a89e2e3624047994dc"></a><a name="a3b14f84bc8c846a89e2e3624047994dc"></a>43007</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="a62a4150a8ebc4da48c4f23f252be20a3"><a name="a62a4150a8ebc4da48c4f23f252be20a3"></a><a name="a62a4150a8ebc4da48c4f23f252be20a3"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="a6123265b22f7471f99611646aef47ff8"><a name="a6123265b22f7471f99611646aef47ff8"></a><a name="a6123265b22f7471f99611646aef47ff8"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s5c7d95b8a0d9404483ad496e5e64f232"></a>

<a name="t1af4bd29b86f455381f4e7da194b600e"></a>
<table><thead align="left"><tr id="r5a1db9bbf897409787b8b50bc0166fe1"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="a10ede6cce9b64706b174ad65214c9641"><a name="a10ede6cce9b64706b174ad65214c9641"></a><a name="a10ede6cce9b64706b174ad65214c9641"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="a90f20d47c55642e3b6f5c32b4da2eddf"><a name="a90f20d47c55642e3b6f5c32b4da2eddf"></a><a name="a90f20d47c55642e3b6f5c32b4da2eddf"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="ra3450b4f6bc64687824aa9a926e8f708"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a06c15c83e60b4bb4a75bd548c76c4478"><a name="a06c15c83e60b4bb4a75bd548c76c4478"></a><a name="a06c15c83e60b4bb4a75bd548c76c4478"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a8d8fd00eb8964937be4e863ec3df06de"><a name="a8d8fd00eb8964937be4e863ec3df06de"></a><a name="a8d8fd00eb8964937be4e863ec3df06de"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="r4d6191b27ba04fae9b674fcf291918d3"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a28da86a6272f4d7ea8d9b147344ca504"><a name="a28da86a6272f4d7ea8d9b147344ca504"></a><a name="a28da86a6272f4d7ea8d9b147344ca504"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="afc5bd55cf2094ac7b616a95916e2fe22"><a name="afc5bd55cf2094ac7b616a95916e2fe22"></a><a name="afc5bd55cf2094ac7b616a95916e2fe22"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="r21377d91edf340448886bc5594f06870"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="aafe5e066c0a147fca6290167413f25c2"><a name="aafe5e066c0a147fca6290167413f25c2"></a><a name="aafe5e066c0a147fca6290167413f25c2"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a9ce84fd5dc194f409aa95c25cbc106a4"><a name="a9ce84fd5dc194f409aa95c25cbc106a4"></a><a name="a9ce84fd5dc194f409aa95c25cbc106a4"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s0fbf003bcef042bea749759dd760440e"></a>

Overhigh non-heap memory usage of the JobHistory process deteriorates JobHistory running performance or even causes OOM, which results in unavailable JobHistory process.

## Possible Causes<a name="sf92530d0dd6e408592697652367477d6"></a>

The non-heap memory of the JobHistory process is overused or inappropriately allocated.

## Procedure<a name="s1c20cc255f314034a0fde7c91a0d7658"></a>

1.  Check non-heap memory usage.
    1.  On MRS Manager, click  **Alarm** and select the alarm whose **Alarm ID** is **43007**. Then check the IP address and role name of the instance in **Location**.
    2.  On MRS Manager, choose  **Service** \> **Spark** \> **Instance** and click the JobHistory for which the alarm is generated to enter the **Instance Status** page. Then choose **Customize** \> **Statistics for the non-heap memory of the JobHistory Process** and click **OK**.
    3.  Check whether the used non-heap memory of the JobHistory process reaches 90% of the maximum non-heap memory specified for JobHistory.
        -   If yes, go to  [1.d](#l462c211400174128a5c9009ceef0f91b).
        -   If no, go to  [2](#la23b479fe172424ba1e9ae701e2a3423).

    4.  <a name="l462c211400174128a5c9009ceef0f91b"></a>On MRS Manager, choose  **Service** \> **Spark** \> **Service Configuration**, and set **Type** to **All**. Choose **JobHistory** \> **Default**. Increase the value of **-XX:MaxMetaspaceSize** in **SPARK\_DAEMON\_JAVA\_OPTS**  as required.
    5.  Check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [2](#la23b479fe172424ba1e9ae701e2a3423).

2.  <a name="la23b479fe172424ba1e9ae701e2a3423"></a>Collect fault information.
    1.  On MRS Manager, choose  **System** \> **Export Log**.
    2.  Select  **Spark** from the **Service** drop-down list and click **OK**.
    3.  Set  **Start Time** for log collection to 10 minutes ahead of the alarm generation time and **End Time** to 10 minutes behind the alarm generation time, and click **Download**.
        1.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).



## Related Information<a name="s51bc9b2d88f34dca980e3cdc3209b47a"></a>

N/A


# ALM-43010 Heap Memory Usage of the JDBCServer Process Exceeds the Threshold<a name="EN-US_TOPIC_0125375232"></a>

## Description<a name="sa8af754cfd604c959c27eabd334b795d"></a>

The system checks the heap memory usage of the JDBCServer process every 30 seconds. The alarm is generated when the heap memory usage of the JDBCServer process exceeds the threshold \(90% of the maximum memory\).

## Attribute<a name="s0341bfdaa7db4acb8eef21a4e0f658bf"></a>

<a name="t0bc26afd1335458d83bcfa8b3bf69cab"></a>
<table><thead align="left"><tr id="r1de9f03160c043e589a32831202428d3"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="aeb9dccb7bf4d46eeb31aaf68d438888b"><a name="aeb9dccb7bf4d46eeb31aaf68d438888b"></a><a name="aeb9dccb7bf4d46eeb31aaf68d438888b"></a>Alarm ID</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="aedaf360375524e93bd266adcac68ab16"><a name="aedaf360375524e93bd266adcac68ab16"></a><a name="aedaf360375524e93bd266adcac68ab16"></a>Alarm Severity</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="a8dd0a93ed5824d148e5dcd5cb3fb9c74"><a name="a8dd0a93ed5824d148e5dcd5cb3fb9c74"></a><a name="a8dd0a93ed5824d148e5dcd5cb3fb9c74"></a>Automatically Cleared</p>
</th>
</tr>
</thead>
<tbody><tr id="r862d745a537648aca76b75f8ffa9014c"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="ad57169680e454d30ac943bc581a3edc4"><a name="ad57169680e454d30ac943bc581a3edc4"></a><a name="ad57169680e454d30ac943bc581a3edc4"></a>43010</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="ad012aa45117c4958b3cf1f36620fb88f"><a name="ad012aa45117c4958b3cf1f36620fb88f"></a><a name="ad012aa45117c4958b3cf1f36620fb88f"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="a6b003025c2214a3481d4c776cdf71951"><a name="a6b003025c2214a3481d4c776cdf71951"></a><a name="a6b003025c2214a3481d4c776cdf71951"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s144c24bec24745af9c3be6af31e1f9b3"></a>

<a name="ta9270469bd504041b7e15935aa639fd6"></a>
<table><thead align="left"><tr id="r30e8ad5e76d044ae91be270181926c31"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="a7ff16b0f8f3c48e99b177e6e087d9f9d"><a name="a7ff16b0f8f3c48e99b177e6e087d9f9d"></a><a name="a7ff16b0f8f3c48e99b177e6e087d9f9d"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="adfd63e134ca74c32ad251a7d178362e3"><a name="adfd63e134ca74c32ad251a7d178362e3"></a><a name="adfd63e134ca74c32ad251a7d178362e3"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="re33283b0974b435689fc25a7977ee2db"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a8cde4231f9c740bb95815bcdd2d3ae41"><a name="a8cde4231f9c740bb95815bcdd2d3ae41"></a><a name="a8cde4231f9c740bb95815bcdd2d3ae41"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a7ff833bbc96d4c67856e4585b9775e79"><a name="a7ff833bbc96d4c67856e4585b9775e79"></a><a name="a7ff833bbc96d4c67856e4585b9775e79"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="r33bbd071ae2343eeb2ca420d8245be04"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="aa3d93e1da9dd4c07b19529d6d1795cd2"><a name="aa3d93e1da9dd4c07b19529d6d1795cd2"></a><a name="aa3d93e1da9dd4c07b19529d6d1795cd2"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a179e479d138f475e88e191182109d2e3"><a name="a179e479d138f475e88e191182109d2e3"></a><a name="a179e479d138f475e88e191182109d2e3"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="r770b5f0ed3fe4083b3302698435b45ee"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a04f51566bc2a4ecdb82fd2c77a66f2a6"><a name="a04f51566bc2a4ecdb82fd2c77a66f2a6"></a><a name="a04f51566bc2a4ecdb82fd2c77a66f2a6"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a17b1ca8dd33a46c4a965fcccc5aa5cf3"><a name="a17b1ca8dd33a46c4a965fcccc5aa5cf3"></a><a name="a17b1ca8dd33a46c4a965fcccc5aa5cf3"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s5baf55db64f446cab38a55bdd98e56ef"></a>

Overhigh heap memory usage of the JDBCServer process deteriorates JDBCServer running performance or even causes OOM, which results in unavailable JDBCServer process.

## Possible Causes<a name="s164d7bae5f894c21ae7e772a5d7c9832"></a>

The heap memory of the JDBCServer process is overused or inappropriately allocated.

## Procedure<a name="sc97a491b320342709903efe5867dfea0"></a>

1.  Check heap memory usage.
    1.  On MRS Manager, click  **Alarm** and select the alarm whose **Alarm ID** is **43010**. Then check the IP address and role name of the instance in **Location**.
    2.  On MRS Manager, choose  **Service** \> **Spark** \> **Instance** and click the JDBCServer for which the alarm is generated to enter the **Instance Status** page. Then choose **Customize** \> **Statistics for the heap memory of the JDBCServer Process** and click **OK**.
    3.  Check whether the used heap memory of the JDBCServer process reaches 90% of the maximum heap memory specified for JDBCServer.
        -   If yes, go to  [1.d](#lde103c22cfc84675b925ef6f48a01577).
        -   If no, go to  [2](#lf0fb5a3f43924b9a82746cdff3c123a9).

    4.  <a name="lde103c22cfc84675b925ef6f48a01577"></a>On MRS Manager, choose  **Service** \> **Spark** \> **Service Configuration**, and set **Type** to **All**. Choose **JDBCServer** \> **Tuning**. Increase the value of **SPARK\_DRIVER\_MEMORY**  as required.
    5.  Check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [2](#lf0fb5a3f43924b9a82746cdff3c123a9).

2.  <a name="lf0fb5a3f43924b9a82746cdff3c123a9"></a>Collect fault information.
    1.  On MRS Manager, choose  **System** \> **Export Log**.
    2.  Select  **Spark** from the **Service** drop-down list and click **OK**.
    3.  Set  **Start Time** for log collection to 10 minutes ahead of the alarm generation time and **End Time** to 10 minutes behind the alarm generation time, and click **Download.**
    4.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="s9bfc6dd14fe8469e8f6e70570562f60e"></a>

N/A


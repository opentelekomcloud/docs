# ALM-43012 Direct Memory Usage of the JDBCServer Process Exceeds the Threshold<a name="EN-US_TOPIC_0125375819"></a>

## Description<a name="sb84d0d30c7ef4e0a9bcc78d0f03fe3c2"></a>

The system checks the direct memory usage of the JDBCServer process every 30 seconds. The alarm is generated when the direct memory usage of the JDBCServer process exceeds the threshold \(90% of the maximum memory\).

## Attribute<a name="s950e609f846049929aad59041bacd3cf"></a>

<a name="tf32df60894664e9182b728d96cc945b4"></a>
<table><thead align="left"><tr id="r050ea54d172b4977b69bfdd1a348150f"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="a56c99339f2cc4d28a8ead0ce1ed8ebf8"><a name="a56c99339f2cc4d28a8ead0ce1ed8ebf8"></a><a name="a56c99339f2cc4d28a8ead0ce1ed8ebf8"></a>Alarm ID</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="a032ffc4d78cb4f61a0746b3e27dd0e22"><a name="a032ffc4d78cb4f61a0746b3e27dd0e22"></a><a name="a032ffc4d78cb4f61a0746b3e27dd0e22"></a>Alarm Severity</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="abeadecebe04942b4b59a89fe52a79b8a"><a name="abeadecebe04942b4b59a89fe52a79b8a"></a><a name="abeadecebe04942b4b59a89fe52a79b8a"></a>Automatically Cleared</p>
</th>
</tr>
</thead>
<tbody><tr id="r0f299213ff854f2ea7adc9fcfc404515"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="a491e57eceeda43028ed53357007bb05a"><a name="a491e57eceeda43028ed53357007bb05a"></a><a name="a491e57eceeda43028ed53357007bb05a"></a>43012</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="a308619d810dc4ba78920f09127f59c86"><a name="a308619d810dc4ba78920f09127f59c86"></a><a name="a308619d810dc4ba78920f09127f59c86"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="a98d16c8417524d08a58c2b37a92873f3"><a name="a98d16c8417524d08a58c2b37a92873f3"></a><a name="a98d16c8417524d08a58c2b37a92873f3"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s6f71e94536f0459d847e1c8b3e62772b"></a>

<a name="t2157db49784e43d798e690b9080cebf7"></a>
<table><thead align="left"><tr id="r4f9d05f2847a4082aadd37dc8167a819"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="ac75ba7233e224c47b6a097188b9688f4"><a name="ac75ba7233e224c47b6a097188b9688f4"></a><a name="ac75ba7233e224c47b6a097188b9688f4"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="aa25df0568ab24ea88e24600195db8d98"><a name="aa25df0568ab24ea88e24600195db8d98"></a><a name="aa25df0568ab24ea88e24600195db8d98"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="r2129d4cba1454b9a8986b1538ac8b1be"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a82b6610f06f0469da6101d07a482edc6"><a name="a82b6610f06f0469da6101d07a482edc6"></a><a name="a82b6610f06f0469da6101d07a482edc6"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a0c255ccec30143d58f2c298b9ba850d1"><a name="a0c255ccec30143d58f2c298b9ba850d1"></a><a name="a0c255ccec30143d58f2c298b9ba850d1"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="rdfbd8c1955684dac83f5a543f8a656a7"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a3ebdb050071a4e38ae61fa8073c62635"><a name="a3ebdb050071a4e38ae61fa8073c62635"></a><a name="a3ebdb050071a4e38ae61fa8073c62635"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="abfabcdd111a84a12b4508b4563aef5a0"><a name="abfabcdd111a84a12b4508b4563aef5a0"></a><a name="abfabcdd111a84a12b4508b4563aef5a0"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="r9d901c5b2f57489dac6aa755cb8e7190"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a8bdb842208f24abe8de3d2bb80ae7c2e"><a name="a8bdb842208f24abe8de3d2bb80ae7c2e"></a><a name="a8bdb842208f24abe8de3d2bb80ae7c2e"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a823886acdb034e85b692a54aa4934985"><a name="a823886acdb034e85b692a54aa4934985"></a><a name="a823886acdb034e85b692a54aa4934985"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="sf18ed6a91e724de98161ff1a85b32a3c"></a>

Overhigh direct memory usage of the JDBCServer process deteriorates JDBCServer running performance or even causes OOM, which results in unavailable JDBCServer process.

## Possible Causes<a name="s54995653f88147de94526c26d8694d31"></a>

The direct memory of the JDBCServer process is overused or inappropriately allocated.

## Procedure<a name="s8de182a1589e4fe88a48acf0e0a8117b"></a>

1.  Check direct memory usage.
    1.  On MRS Manager, click  **Alarm** and select the alarm whose **Alarm ID** is **43012**. Then check the IP address and role name of the instance in **Location**.
    2.  On MRS Manager, choose  **Service** \> **Spark** \> **Instance** and click the JDBCServer for which the alarm is generated to enter the **Instance Status** page. Then choose **Customize** \> **Direct Memory of JDBCServer** and click **OK**.
    3.  Check whether the used direct memory of the JDBCServer process reaches 90% of the maximum direct memory specified for JDBCServer.
        -   If yes, go to  [1.d](#l40f74faafbd147d1918114c4fbe36d41)
        -   If no, go to  [2](#lf1c03cfdbea84aa1bdaa3f98a6d609e0).

    4.  <a name="l40f74faafbd147d1918114c4fbe36d41"></a>On MRS Manager, choose  **Service** \> **Spark** \> **Service Configuration**, and set **Type** to **All**. Choose **JDBCServer** \> **Tuning**. Increase the value of **-XX:MaxDirectMemorySize** in **spark.driver.extraJavaOptions**  as required.
    5.  Check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [2](#lf1c03cfdbea84aa1bdaa3f98a6d609e0).

2.  <a name="lf1c03cfdbea84aa1bdaa3f98a6d609e0"></a>Collect fault information.
    1.  On MRS Manager, choose  **System** \> **Export Log**.
    2.  Select  **Spark** from the **Service** drop-down list and click **OK**.
    3.  Set  **Start Time** for log collection to 10 minutes ahead of the alarm generation time and **End Time** to 10 minutes behind the alarm generation time, and click **Download**.
    4.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="sd7b0c1a4d1c947028c8c2e5173068f7e"></a>

N/A


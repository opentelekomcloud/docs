# ALM-43009 JobHistory GC Time Exceeds the Threshold<a name="EN-US_TOPIC_0125375490"></a>

## Description<a name="s1c55656fac8b40ceaff5672adacf360f"></a>

The system checks the garbage collection \(GC\) time of the JobHistory process every 60 seconds. This alarm is generated when the detected GC time exceeds the threshold \(exceeds 12 seconds for three consecutive checks.\) To change the threshold, choose  **System** \> **Threshold Configuration** \> **Service** \> **Spark** \> **Garbage Collection \(GC\) Time of JobHistory** \> **Total GC time in milliseconds**. This alarm is cleared when the JobHistory GC time is shorter than or equal to the threshold.

## Attribute<a name="sd2b848c44c8140cca5350c1e7649f32d"></a>

<a name="tc9e50caf6d464cb3ae389831c2b0e667"></a>
<table><thead align="left"><tr id="ra8b96ba352e5426dabc183ab912ba6fb"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="a0b7307369cf8457186e16a5998d896ba"><a name="a0b7307369cf8457186e16a5998d896ba"></a><a name="a0b7307369cf8457186e16a5998d896ba"></a>Alarm ID</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="af61242e05fde4490906efe1c2642bb9d"><a name="af61242e05fde4490906efe1c2642bb9d"></a><a name="af61242e05fde4490906efe1c2642bb9d"></a>Alarm Severity</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="abe488fba5f784d1ca25138e20b9f1792"><a name="abe488fba5f784d1ca25138e20b9f1792"></a><a name="abe488fba5f784d1ca25138e20b9f1792"></a>Automatically Cleared</p>
</th>
</tr>
</thead>
<tbody><tr id="r24c1d387b6a94a40a7031a2d12b26923"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="a67f802b207c04a04864d15b69307d0bc"><a name="a67f802b207c04a04864d15b69307d0bc"></a><a name="a67f802b207c04a04864d15b69307d0bc"></a>43009</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="a914725b790934eaab4077b1665feff2d"><a name="a914725b790934eaab4077b1665feff2d"></a><a name="a914725b790934eaab4077b1665feff2d"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="a80e15fddc69e4eac992db90317876563"><a name="a80e15fddc69e4eac992db90317876563"></a><a name="a80e15fddc69e4eac992db90317876563"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="sdc456bbf81bc42e6823073409cff4b24"></a>

<a name="t475baaf256b3491cbd63d14ac785bb74"></a>
<table><thead align="left"><tr id="rd640925dfe7f42c1878bbf2b11943082"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="a4f45136d05254fcbb8a9c2a917f71f39"><a name="a4f45136d05254fcbb8a9c2a917f71f39"></a><a name="a4f45136d05254fcbb8a9c2a917f71f39"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="af7522fcbfca14d5ca10aeb15d8a00f4e"><a name="af7522fcbfca14d5ca10aeb15d8a00f4e"></a><a name="af7522fcbfca14d5ca10aeb15d8a00f4e"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="rd42a33bb96ca407790de74b487cb5352"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="aaeabb0c71b564b7a94707a323fb23585"><a name="aaeabb0c71b564b7a94707a323fb23585"></a><a name="aaeabb0c71b564b7a94707a323fb23585"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0087163597_p763056517559"><a name="en-us_topic_0087163597_p763056517559"></a><a name="en-us_topic_0087163597_p763056517559"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="r12cd7d439c7545dca047d72aae1ca93a"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a6111e8f932564ca090f691b7a4927df3"><a name="a6111e8f932564ca090f691b7a4927df3"></a><a name="a6111e8f932564ca090f691b7a4927df3"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="ab0ceee8d64a1462aa68072da81f591a8"><a name="ab0ceee8d64a1462aa68072da81f591a8"></a><a name="ab0ceee8d64a1462aa68072da81f591a8"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="r8bdac432204841dc98d5cb04715290d7"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="abaa220e696134505a369b4d6a89bfcff"><a name="abaa220e696134505a369b4d6a89bfcff"></a><a name="abaa220e696134505a369b4d6a89bfcff"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0087163597_p786161617559"><a name="en-us_topic_0087163597_p786161617559"></a><a name="en-us_topic_0087163597_p786161617559"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="scfe6b84df7ef406fad9aeaeae1cb5cc2"></a>

If the GC time exceeds the threshold, the JobHistory process running performance will be affected and the JobHistory process will even be unavailable.

## Possible Causes<a name="sa627c33ea56b42a8860fad37bd04d8e6"></a>

The heap memory of the JobHistory process is overused or inappropriately allocated, causing frequent occurrence of the GC process.

## Procedure<a name="s50c1547f5d90490baaaaaaac1752fbdf"></a>

1.  Check the GC time.
    1.  On MRS Manager, click  **Alarm** and select the alarm whose **Alarm ID** is **43009**. Then check the IP address and role name of the instance in **Location**.
    2.  On MRS Manager, choose  **Service** \> **Spark** \> **Instance** and click the JobHistory for which the alarm is generated to enter the **Instance Status** page. Then choose **Customize** \> **Garbage Collection \(GC\) Time of JobHistory** and click **OK**.
    3.  Check whether the GC time is longer than 12 seconds.
        -   If yes, go to  [1.d](#l0e2d5072c33d44c4ad4d0d9983d4ce38).
        -   If no, go to  [2](#l3d544c825b4c462eb0ac92b333ef8e22).

    4.  <a name="l0e2d5072c33d44c4ad4d0d9983d4ce38"></a>On MRS Manager, choose  **Service** \> **Spark** \> **Service Configuration**, and set **Type** to **All**. Choose **JobHistory** \> **Default**. Increase the value of **SPARK\_DAEMON\_MEMORY**  as required.
    5.  Check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [2](#l3d544c825b4c462eb0ac92b333ef8e22).

2.  <a name="l3d544c825b4c462eb0ac92b333ef8e22"></a>Collect fault information.
    1.  On MRS Manager, choose  **System** \> **Export Log**.
    2.  In the  **Service** drop-down list box, select **Spark** and click **OK**.
    3.  Set  **Start Time** for log collection to 10 minutes ahead of the alarm generation time and **End Time** to 10 minutes behind the alarm generation time, and click **Download**.
    4.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="s2d5ee2f500e544ababc108fd2032fb32"></a>

N/A


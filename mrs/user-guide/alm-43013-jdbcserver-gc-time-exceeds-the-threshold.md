# ALM-43013 JDBCServer GC Time Exceeds the Threshold<a name="EN-US_TOPIC_0125375458"></a>

## Description<a name="s81043f248ff7451ca9b89969a8dc0a26"></a>

The system checks the garbage collection \(GC\) time of the JDBCServer process every 60 seconds. This alarm is generated when the detected GC time exceeds the threshold \(exceeds 12 seconds for three consecutive checks.\) To change the threshold, choose  **System** \> **Threshold Configuration** \> **Service** \> **Spark** \> **Garbage Collection \(GC\) Time of JDBCServer** \> **Total GC time in milliseconds**. This alarm is cleared when the JDBCServer GC time is shorter than or equal to the threshold.

## Attribute<a name="s8b92804bd1e442d18a63384a67734693"></a>

<a name="t9335e7a8132e4b7694adbd6f74500b07"></a>
<table><thead align="left"><tr id="re389cee4f81c4fc0b3a7f66914b1414b"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="ad3c22503c507469aa9637f6f5d7c4232"><a name="ad3c22503c507469aa9637f6f5d7c4232"></a><a name="ad3c22503c507469aa9637f6f5d7c4232"></a>Alarm ID</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="ada448dcfa4f64b42a269685712d3fe36"><a name="ada448dcfa4f64b42a269685712d3fe36"></a><a name="ada448dcfa4f64b42a269685712d3fe36"></a>Alarm Severity</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="a744d9bf11a9c40eeb6a7e0deaa521b10"><a name="a744d9bf11a9c40eeb6a7e0deaa521b10"></a><a name="a744d9bf11a9c40eeb6a7e0deaa521b10"></a>Automatically Cleared</p>
</th>
</tr>
</thead>
<tbody><tr id="r68a42c726d514ce1924793c473b8a46c"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="ad8ab7215acca417db49d171cdb57cc67"><a name="ad8ab7215acca417db49d171cdb57cc67"></a><a name="ad8ab7215acca417db49d171cdb57cc67"></a>43013</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="af06ddaac32c4443a931da65c31d8cb99"><a name="af06ddaac32c4443a931da65c31d8cb99"></a><a name="af06ddaac32c4443a931da65c31d8cb99"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="a2ce97fe5c9dc458eb949ea623ed7f31b"><a name="a2ce97fe5c9dc458eb949ea623ed7f31b"></a><a name="a2ce97fe5c9dc458eb949ea623ed7f31b"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s4b750eb5fad244198fe913ef684cb702"></a>

<a name="t5690da1b02b34a4aabec5ec7cb103d39"></a>
<table><thead align="left"><tr id="r705924733c1a4949b45fd8122a288420"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="a63de6188cc234d1597464c91b0b81bc2"><a name="a63de6188cc234d1597464c91b0b81bc2"></a><a name="a63de6188cc234d1597464c91b0b81bc2"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="a246e3133bcfb4ce1ba2af11d3c69df75"><a name="a246e3133bcfb4ce1ba2af11d3c69df75"></a><a name="a246e3133bcfb4ce1ba2af11d3c69df75"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="r439a2cbc2ec948f690e0ab8fe6da1dfd"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a123da339778e479289e571b7f5597e9d"><a name="a123da339778e479289e571b7f5597e9d"></a><a name="a123da339778e479289e571b7f5597e9d"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a57519d7ba0ee4aec8fce5939360484fb"><a name="a57519d7ba0ee4aec8fce5939360484fb"></a><a name="a57519d7ba0ee4aec8fce5939360484fb"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="r66037db85b754ecf9ae25434617a6c68"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a135a8780b4e643bba628f4c6ec371a00"><a name="a135a8780b4e643bba628f4c6ec371a00"></a><a name="a135a8780b4e643bba628f4c6ec371a00"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="ae0c0ed793bbe4e94a7759a55533efe5e"><a name="ae0c0ed793bbe4e94a7759a55533efe5e"></a><a name="ae0c0ed793bbe4e94a7759a55533efe5e"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="rf39f8b3ecbaf4de09ad0604c677cacb2"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="abb2467cc3d0049f78e48c09ae3ce7c24"><a name="abb2467cc3d0049f78e48c09ae3ce7c24"></a><a name="abb2467cc3d0049f78e48c09ae3ce7c24"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="ab1a5b7e8b8d34c678477744578a4cfe2"><a name="ab1a5b7e8b8d34c678477744578a4cfe2"></a><a name="ab1a5b7e8b8d34c678477744578a4cfe2"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s978b6efc8fd7414cb922e7edf9acfd24"></a>

If the GC time exceeds the threshold, the JDBCServer process running performance will be affected and the JDBCServer process will even be unavailable.

## Possible Causes<a name="s82a92e49d1fb4f34843e0297bb6c77f9"></a>

The heap memory of the JDBCServer process is overused or inappropriately allocated, causing frequent occurrence of the GC process.

## Procedure<a name="sbb457de257c24676852b78c5f7476504"></a>

1.  Check the GC time.
    1.  On MRS Manager, click  **Alarm** and select the alarm whose **Alarm ID** is **43013**. Then check the IP address and role name of the instance in **Location**.
    2.  On MRS Manager, choose  **Service** \> **Spark** \> **Instance** and click the JDBCServer for which the alarm is generated to enter the **Instance Status** page. Then choose **Customize** \> **Garbage Collection \(GC\) Time of JDBCServer** and click **OK**.
    3.  Check whether the GC time is longer than 12 seconds.
        -   If yes, go to  [1.d](#l08759bc1c2144825806aaa9754fd4d14).
        -   If no, go to  [2](#lbc699f1f6b66473cb6f5a9b084e63a00).

    4.  <a name="l08759bc1c2144825806aaa9754fd4d14"></a>On MRS Manager, choose  **Service**  \> **Spark** \> **Service Configuration**, and set **Type** to **All**. Choose **JDBCServer** \> **Tuning**. Increase the value of **SPARK\_DRIVER\_MEMORY**  as required.
    5.  Check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [2](#lbc699f1f6b66473cb6f5a9b084e63a00).

2.  <a name="lbc699f1f6b66473cb6f5a9b084e63a00"></a>Collect fault information.
    1.  On MRS Manager, choose  **System** \> **Export Log**.
    2.  In the  **Service** drop-down list box, select **Spark** and click **OK**.
    3.  Set  **Start Time** for log collection to 10 minutes ahead of the alarm generation time and **End Time** to 10 minutes behind the alarm generation time, and click **Download**.
    4.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="se0f5e514e2714404b62ebb65a29ea23b"></a>

N/A


# ALM-43006 Heap Memory Usage of the JobHistory Process Exceeds the Threshold<a name="EN-US_TOPIC_0125375677"></a>

## Description<a name="s41d3893c9bbe4ca89107cbedd668c0b3"></a>

The system checks the heap memory usage of the JobHistory process every 30 seconds. The alarm is generated when the heap memory usage of the JobHistory process exceeds the threshold \(90% of the maximum memory\).

## Attribute<a name="sfef568985c354e5fb01a535c64b623e5"></a>

<a name="t4e32235214a04f6a9d88c47e0275fd21"></a>
<table><thead align="left"><tr id="rb3b8011a38194aedb34dd8e9441e32d6"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="afd0256b116544531ba9a44471ae8399e"><a name="afd0256b116544531ba9a44471ae8399e"></a><a name="afd0256b116544531ba9a44471ae8399e"></a>Alarm ID</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="ad195d4963c284067a9dd11b47ba38422"><a name="ad195d4963c284067a9dd11b47ba38422"></a><a name="ad195d4963c284067a9dd11b47ba38422"></a>Alarm Severity</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="a9e517ac9270b4f44811f469ef530bd9a"><a name="a9e517ac9270b4f44811f469ef530bd9a"></a><a name="a9e517ac9270b4f44811f469ef530bd9a"></a>Automatically Cleared</p>
</th>
</tr>
</thead>
<tbody><tr id="r9afcb9f3ac974f9c9bd6267672eb273d"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="aa858a87838fb43cd9c7b364250e4b534"><a name="aa858a87838fb43cd9c7b364250e4b534"></a><a name="aa858a87838fb43cd9c7b364250e4b534"></a>43006</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="a8ee9059a32b84543b89757db892089b7"><a name="a8ee9059a32b84543b89757db892089b7"></a><a name="a8ee9059a32b84543b89757db892089b7"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="a088ddd08a3f14cd184203b4bdab18ccf"><a name="a088ddd08a3f14cd184203b4bdab18ccf"></a><a name="a088ddd08a3f14cd184203b4bdab18ccf"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s17d1387fdb7149febf73a19d1af00a57"></a>

<a name="t3530c7decc634903939887d8195d8971"></a>
<table><thead align="left"><tr id="r441d82b7cccc4f4fa2461faf0478c5ad"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="ab27b12fc392d4344aa9b02530c8be419"><a name="ab27b12fc392d4344aa9b02530c8be419"></a><a name="ab27b12fc392d4344aa9b02530c8be419"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="aac0e6cabe9134d0a9be19456c499dbad"><a name="aac0e6cabe9134d0a9be19456c499dbad"></a><a name="aac0e6cabe9134d0a9be19456c499dbad"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="r1cf3119ec9f044a8a0bc20198499ce2d"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a25b391439c9e4e69b27d89f4cf6eeb95"><a name="a25b391439c9e4e69b27d89f4cf6eeb95"></a><a name="a25b391439c9e4e69b27d89f4cf6eeb95"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a08b8ab3ab5d843ac848b58bd524d29a3"><a name="a08b8ab3ab5d843ac848b58bd524d29a3"></a><a name="a08b8ab3ab5d843ac848b58bd524d29a3"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="r1e027d0974c44d7ca99691c22378bc50"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a2c1802af1b544b75a86c17c6b89c41e6"><a name="a2c1802af1b544b75a86c17c6b89c41e6"></a><a name="a2c1802af1b544b75a86c17c6b89c41e6"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="ab7062cadddaa40cd9dcd2ebc9f4eeaa2"><a name="ab7062cadddaa40cd9dcd2ebc9f4eeaa2"></a><a name="ab7062cadddaa40cd9dcd2ebc9f4eeaa2"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="r1663ff362dd6463ab7630152db5b6f92"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a9b094026ebc64fa19bbc0e9954515ad8"><a name="a9b094026ebc64fa19bbc0e9954515ad8"></a><a name="a9b094026ebc64fa19bbc0e9954515ad8"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a427b56078d8c487eb51152e30261e1ac"><a name="a427b56078d8c487eb51152e30261e1ac"></a><a name="a427b56078d8c487eb51152e30261e1ac"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="sb3abc782185648c685547aabb9314f7e"></a>

Overhigh heap memory usage of the JobHistory process deteriorates JobHistory running performance or even causes OOM, which results in unavailable JobHistory process.

## Possible Causes<a name="s719d5012270844a68dd561f5cab96c34"></a>

The heap memory of the JobHistory process is overused or inappropriately allocated.

## Procedure<a name="s5aee06dfc8794beeb2da9b8922ea6e8a"></a>

1.  Check heap memory usage.
    1.  On MRS Manager, click  **Alarm** and select the alarm whose **Alarm ID** is **43006**. Then check the IP address and role name of the instance in **Location**.
    2.  On MRS Manager, choose  **Service** \> **Spark** \> **Instance** and click the JobHistory for which the alarm is generated to enter the **Instance Status** page. Then choose **Customize** \>  **Statistics for the heap memory of the JobHistory Process**  and click **OK**.
    3.  Check whether the used heap memory of the JobHistory process reaches 90% of the maximum heap memory specified for JobHistory.
        -   If yes, go to  [1.d](#l757b2c570a454fefb4b20e7a5a2f7100).
        -   If no, go to  [2](#l6496331719ca41bebe5148ba0d28a93e).

    4.  <a name="l757b2c570a454fefb4b20e7a5a2f7100"></a>On MRS Manager, choose  **Service** \> **Spark** \> **Service Configuration**, and set **Type** to **All**. Choose **JobHistory** \> **Default**. Increase the value of **SPARK\_DAEMON\_MEMORY**  as required.
    5.  Check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [2](#l6496331719ca41bebe5148ba0d28a93e).

2.  <a name="l6496331719ca41bebe5148ba0d28a93e"></a>Collect fault information.
    1.  On MRS Manager, choose  **System** \> **Export Log**.
    2.  Select  **Spark** from the **Service** drop-down list and click **OK**.
    3.  Set  **Start Time** for log collection to 10 minutes ahead of the alarm generation time and **End Time** to 10 minutes behind the alarm generation time, and click **Download**.
    4.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="sa5f3a20b57bc4b1ebb6894de279d1d4c"></a>

N/A


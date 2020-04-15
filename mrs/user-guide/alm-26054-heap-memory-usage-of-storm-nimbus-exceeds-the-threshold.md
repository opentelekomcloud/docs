# ALM-26054 Heap Memory Usage of Storm Nimbus Exceeds the Threshold<a name="EN-US_TOPIC_0125376026"></a>

## Description<a name="s774029ea40f7424fa7b7602b33ee140d"></a>

The system checks the heap memory usage of Storm Nimbus every 30 seconds and compares it with the threshold. This alarm is generated if the heap memory usage exceeds the threshold \(80% by default\).

To modify the threshold, users can choose  **System**  \>  **Threshold Configuration**  \>  **Service**  \>  **Storm**  on MRS Manager.

This alarm is cleared if the heap memory usage is lower than or equal to the threshold.

## Attribute<a name="s0fdf58df3f6b40b2a708afb6e5db9b7d"></a>

<a name="t98fab57f60214959982cd316cb675d6e"></a>
<table><thead align="left"><tr id="r52e04ad755dc4df091019a6b69977928"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="a28c3e6dffdcf44d6a0770ab06e194285"><a name="a28c3e6dffdcf44d6a0770ab06e194285"></a><a name="a28c3e6dffdcf44d6a0770ab06e194285"></a><strong id="a5d20ec122ffb40ff9ceb3956f928796c"><a name="a5d20ec122ffb40ff9ceb3956f928796c"></a><a name="a5d20ec122ffb40ff9ceb3956f928796c"></a>Alarm ID</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="adc5fa1b17e3448efaa40853d0f9bedc9"><a name="adc5fa1b17e3448efaa40853d0f9bedc9"></a><a name="adc5fa1b17e3448efaa40853d0f9bedc9"></a><strong id="acf53183250a94863b8e69501c44debe7"><a name="acf53183250a94863b8e69501c44debe7"></a><a name="acf53183250a94863b8e69501c44debe7"></a>Alarm Severity</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="a071088f67a0747fca3ac23a6bfca1832"><a name="a071088f67a0747fca3ac23a6bfca1832"></a><a name="a071088f67a0747fca3ac23a6bfca1832"></a><strong id="a60b77c2294f84a8ba1a3ac02dddec384"><a name="a60b77c2294f84a8ba1a3ac02dddec384"></a><a name="a60b77c2294f84a8ba1a3ac02dddec384"></a>Automatically Cleared</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r1a6254581957449db689137f7e1f38e6"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="a8b19838394784038ace8caae1cdcd693"><a name="a8b19838394784038ace8caae1cdcd693"></a><a name="a8b19838394784038ace8caae1cdcd693"></a>26054</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="a1d90d12092f24766a9ee9892f317c115"><a name="a1d90d12092f24766a9ee9892f317c115"></a><a name="a1d90d12092f24766a9ee9892f317c115"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="a7739dcfedf7646eda07207e8709d1a60"><a name="a7739dcfedf7646eda07207e8709d1a60"></a><a name="a7739dcfedf7646eda07207e8709d1a60"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="sae4dd9778749496189b2fa9a9da77138"></a>

<a name="t1393e61bb1fe4e0aaf02b952b755f477"></a>
<table><thead align="left"><tr id="r02d3d06a508b48fca74092f02e05da05"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="a3f7a576bd5c04a5fbab19427ea4589df"><a name="a3f7a576bd5c04a5fbab19427ea4589df"></a><a name="a3f7a576bd5c04a5fbab19427ea4589df"></a><strong id="a968022acdebe4c95b3ed82cd790041a5"><a name="a968022acdebe4c95b3ed82cd790041a5"></a><a name="a968022acdebe4c95b3ed82cd790041a5"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="a01967af51cc34b279567ca3199ca6681"><a name="a01967af51cc34b279567ca3199ca6681"></a><a name="a01967af51cc34b279567ca3199ca6681"></a><strong id="a084f7cbc71984d938bc23d2308bc6b40"><a name="a084f7cbc71984d938bc23d2308bc6b40"></a><a name="a084f7cbc71984d938bc23d2308bc6b40"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="rc51164e6026342ebb76b1fd6562eb6bc"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a3584eefe4d0649c099852da61ce754d4"><a name="a3584eefe4d0649c099852da61ce754d4"></a><a name="a3584eefe4d0649c099852da61ce754d4"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a22c02997160948f2b65c3dbb5ba8b3db"><a name="a22c02997160948f2b65c3dbb5ba8b3db"></a><a name="a22c02997160948f2b65c3dbb5ba8b3db"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="r63045f5a6a1b48fc96a9bf075cc0cde9"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="ab80c0ae9d903426fac9f8837e86c0b8c"><a name="ab80c0ae9d903426fac9f8837e86c0b8c"></a><a name="ab80c0ae9d903426fac9f8837e86c0b8c"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a9007074b8b4740eb8ace6767101aa3ec"><a name="a9007074b8b4740eb8ace6767101aa3ec"></a><a name="a9007074b8b4740eb8ace6767101aa3ec"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="rdb9d69166bbd405b96f76eef019cfa91"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a9ed8b38bfffe4ca18ad0d6321d5662d9"><a name="a9ed8b38bfffe4ca18ad0d6321d5662d9"></a><a name="a9ed8b38bfffe4ca18ad0d6321d5662d9"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a276fc9da490f4309809178a3da7f649c"><a name="a276fc9da490f4309809178a3da7f649c"></a><a name="a276fc9da490f4309809178a3da7f649c"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
<tr id="r7f66a243f5e1466895da1184c6a2ae4f"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="aaa11f2f2f1c444cc8a10a2165c4846ae"><a name="aaa11f2f2f1c444cc8a10a2165c4846ae"></a><a name="aaa11f2f2f1c444cc8a10a2165c4846ae"></a>Trigger Condition</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="ad7e2e685fae64f6d96fb2740d5f0d53f"><a name="ad7e2e685fae64f6d96fb2740d5f0d53f"></a><a name="ad7e2e685fae64f6d96fb2740d5f0d53f"></a>Generates an alarm when the actual indicator value exceeds the specified threshold.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s34bce58d356d46e5b7dc6051fdb7662b"></a>

Frequent memory garbage collection or memory overflow may occur, affecting submission of Storm services.

## Possible Causes<a name="s4d13aab8f7754b4aafc37ed12e41de4e"></a>

The heap memory usage is high or the heap memory is improperly allocated.

## Procedure<a name="s0119e5f6f3054568b09579b5cfb29c24"></a>

1.  Check the heap memory usage.
    1.  On MRS Manager, choose  **Alarm \> ALM-26054 Heap Memory Usage of Storm Nimbus Exceeds the Threshold \> Location**. Query the **HostName**  of the alarmed instance.
    2.  On MRS Manager, choose  **Service \> Storm \> Instance\> Nimbus \(corresponding to the HostName of the alarmed instance\) \> Customize \> Heap Memory Usage of Nimbus**.
    3.  Check whether the heap memory usage of Nimbus has reached the threshold \(80%\).
        -   If yes, go to  [1.d](#l31923ad56f1b4d019f78ba354d4b4058).
        -   If no, go to  [2.a](#l4e73f668d64b46f0b6f5af5e4346b2bb).

    4.  <a name="l31923ad56f1b4d019f78ba354d4b4058"></a>Adjust the heap memory.

        On MRS Manager, choose  **Service \> Storm \> Service Configuration \> All \> Nimbus \> System**. Increase the value of **-Xmx** in **NIMBUS\_GC\_OPTS**. Click **Save Configuration**. Select **Restart the affected services or instances** and click **OK**.

    5.  Check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [2.a](#l4e73f668d64b46f0b6f5af5e4346b2bb).

2.  Collect fault information.
    1.  <a name="l4e73f668d64b46f0b6f5af5e4346b2bb"></a>On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="s693b097481ad44558c1d1ed69a1612df"></a>

N/A


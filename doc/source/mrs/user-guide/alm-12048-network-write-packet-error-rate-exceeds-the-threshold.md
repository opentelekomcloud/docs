# ALM-12048 Network Write Packet Error Rate Exceeds the Threshold<a name="EN-US_TOPIC_0125376101"></a>

## Description<a name="s25e474213f6143eda54a78a987c6a22e"></a>

The system checks the network write packet error rate every 30 seconds and compares the actual packet error rate with the threshold \(the default threshold is 0.5%\). This alarm is generated when the system detects that the network write packet error rate exceeds the threshold for several times \(5 times by default\) consecutively.

To change the threshold, choose  **System** \> **Threshold Configuration** \> **Device** \> **Host** \> **Network Writing** \> **Network Write Packet Rate Information** \> **Write Packet Error Rate**.

When the  **hit number** is 1, this alarm is cleared when the network write packet error rate is less than or equal to the threshold. When the **hit number**  is greater than 1, this alarm is cleared when the value of the network write packet error rate is less than or equal to 90% of the threshold.

## Attribute<a name="s9232a730f83248cab1f5cee67b49993f"></a>

<a name="t54838b06e2d64ae7b32b7cbb351131dc"></a>
<table><thead align="left"><tr id="r339ff46ea88c4d94a565a70f176f0856"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="a574c5415fb9546aab08d2caa7165b132"><a name="a574c5415fb9546aab08d2caa7165b132"></a><a name="a574c5415fb9546aab08d2caa7165b132"></a>Alarm ID</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="a6ab0df07f78140f59e543ccee73992ba"><a name="a6ab0df07f78140f59e543ccee73992ba"></a><a name="a6ab0df07f78140f59e543ccee73992ba"></a>Alarm Severity</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="a365958d1c53d4887a28239e8952ac339"><a name="a365958d1c53d4887a28239e8952ac339"></a><a name="a365958d1c53d4887a28239e8952ac339"></a>Automatically Cleared</p>
</th>
</tr>
</thead>
<tbody><tr id="r2a3c27e47b2740aca8f4a9f3575031f1"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="aa86d16b469fd44a692f3b6e597c8722f"><a name="aa86d16b469fd44a692f3b6e597c8722f"></a><a name="aa86d16b469fd44a692f3b6e597c8722f"></a>12048</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="ad363441e112e407dbb8e585a43770037"><a name="ad363441e112e407dbb8e585a43770037"></a><a name="ad363441e112e407dbb8e585a43770037"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="a12281dbf991348b4bdbb75d5dd495838"><a name="a12281dbf991348b4bdbb75d5dd495838"></a><a name="a12281dbf991348b4bdbb75d5dd495838"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s5d167d05d7c441f3858798945b71acb8"></a>

<a name="t019f563490a34d0c8daaf924c8e1bd40"></a>
<table><thead align="left"><tr id="rea9d34c54c044ee4b67884e51355bfca"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="a6ea4f6695c4042fb9c748d86ed4fbeb8"><a name="a6ea4f6695c4042fb9c748d86ed4fbeb8"></a><a name="a6ea4f6695c4042fb9c748d86ed4fbeb8"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="a840a9dadad6c48948d55a1814de5d41d"><a name="a840a9dadad6c48948d55a1814de5d41d"></a><a name="a840a9dadad6c48948d55a1814de5d41d"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="r306f00142b6d40b08d6fe5831804a2e0"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a5d8e2cce17ff4440b91b9c90ddc785df"><a name="a5d8e2cce17ff4440b91b9c90ddc785df"></a><a name="a5d8e2cce17ff4440b91b9c90ddc785df"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="aee63a6c7147f49a7a7cc3e24f725b3c2"><a name="aee63a6c7147f49a7a7cc3e24f725b3c2"></a><a name="aee63a6c7147f49a7a7cc3e24f725b3c2"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="rc7b7f49a108c40a99be28a3da7ce2c15"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a34255d8369e24802833deb704e8f723c"><a name="a34255d8369e24802833deb704e8f723c"></a><a name="a34255d8369e24802833deb704e8f723c"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a830882dc3cad4defbe897448b15a6649"><a name="a830882dc3cad4defbe897448b15a6649"></a><a name="a830882dc3cad4defbe897448b15a6649"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="r91f06447694d42c6a5644f0bdc81e834"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a24736e0c6cec42a9b39b7f7f8b673c3d"><a name="a24736e0c6cec42a9b39b7f7f8b673c3d"></a><a name="a24736e0c6cec42a9b39b7f7f8b673c3d"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="aefd1e24b34c141309465b3b27d562150"><a name="aefd1e24b34c141309465b3b27d562150"></a><a name="aefd1e24b34c141309465b3b27d562150"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
<tr id="r018d6ec6a9d94b52abff69589afb69ed"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a252bae214b8a4b82a92b332f1a4710e5"><a name="a252bae214b8a4b82a92b332f1a4710e5"></a><a name="a252bae214b8a4b82a92b332f1a4710e5"></a>NetworkCardName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a9b9184009d4e490ebb1d9a31aaeac393"><a name="a9b9184009d4e490ebb1d9a31aaeac393"></a><a name="a9b9184009d4e490ebb1d9a31aaeac393"></a>Specifies the network port for which the alarm is generated.</p>
</td>
</tr>
<tr id="r0c0d150afac84570b59af31240702548"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a357c633ba92e47a1a812daf217f014aa"><a name="a357c633ba92e47a1a812daf217f014aa"></a><a name="a357c633ba92e47a1a812daf217f014aa"></a>Trigger Condition</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a6729dcf201744a2ca23ce340e5b5db78"><a name="a6729dcf201744a2ca23ce340e5b5db78"></a><a name="a6729dcf201744a2ca23ce340e5b5db78"></a>Generates an alarm when the actual indicator value exceeds the specified threshold.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s6781208df33445bea4fcc1b0a01076ef"></a>

The communication interrupts intermittently and services time out.

## Possible Causes<a name="s1305644a7d9b45929b02ca08775cfbf5"></a>

-   The alarm threshold is set improperly.
-   The network is abnormal.

## Procedure<a name="s54c4b033cafe473588fa5d18ee350b53"></a>

**Check whether the threshold is set properly.**

1.  Log in to MRS Manager and check whether the alarm threshold is set properly. \(By default, 0.5% is a proper value. However, users can configure the value as required.\)
    -   If yes, go to  [4](#le4924487184c4a3cb7dc48c77eb0d5bc).
    -   If no, go to  [2](#lcefd1ea87ed24620b1f60e150db6b928).

2.  <a name="lcefd1ea87ed24620b1f60e150db6b928"></a>Based on actual usage condition, choose  **System** \> **Threshold Configuration** \> **Device** \> **Host** \> **Network Writing** \> **Network Write Packet Rate Information** \> **Write Packet Error Rate**  to modify the alarm threshold.
3.  Wait 5 minutes and check whether the alarm is cleared.
    -   If yes, no further action is required.
    -   If no, go to  [4](#le4924487184c4a3cb7dc48c77eb0d5bc).


**Check whether the network is normal.**

1.  <a name="le4924487184c4a3cb7dc48c77eb0d5bc"></a>Contact the system administrator to check whether the network is abnormal.
    -   If yes, go to  [5](#l75f9f9aa1e524a809d9ee2138cd6041f)  to rectify the network fault.
    -   If no, go to  [7](#l28f369bb61fe40fba20bcc9c51341794).

2.  <a name="l75f9f9aa1e524a809d9ee2138cd6041f"></a>Wait 5 minutes and check whether the alarm is cleared.
    -   If yes, no further action is required.
    -   If no, go to  [7](#l28f369bb61fe40fba20bcc9c51341794).


**Collect fault information.**

1.  On MRS Manager, choose  **System** \> **Export Log**.
2.  <a name="l28f369bb61fe40fba20bcc9c51341794"></a>Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).

## Related Information<a name="scde43b3f8dfa4b6c8935f19a575d6218"></a>

N/A


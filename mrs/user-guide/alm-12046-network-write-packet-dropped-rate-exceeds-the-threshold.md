# ALM-12046 Network Write Packet Dropped Rate Exceeds the Threshold<a name="EN-US_TOPIC_0125375891"></a>

## Description<a name="s41bd11211c3247a7b0ccca044a5075cb"></a>

The system checks the network write packet dropped rate every 30 seconds and compares the actual packet dropped rate with the threshold \(the default threshold is 0.5%\). This alarm is generated when the system detects that the network write packet dropped rate exceeds the threshold for several times \(5 times by default\) consecutively.

To change the threshold, choose  **System** \> **Threshold Configuration** \> **Device** \> **Host** \> **Network Writing** \> **Network Write Packet Rate Information** \> **Write Packet Dropped Rate**.

When the  **hit number** is 1, this alarm is cleared when the network write packet dropped rate is less than or equal to the threshold. When the **hit number**  is greater than 1, this alarm is cleared when the network write packet dropped rate is less than or equal to 90% of the threshold.

## Attribute<a name="sea46c6779dba40f3b13f04d0ce1054cb"></a>

<a name="tdd22576d25124bba8a9fde9730e112fe"></a>
<table><thead align="left"><tr id="r492e71499f034e4ba05812dac089461c"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="abfa5e5e035d24cde90d8040db5a8033d"><a name="abfa5e5e035d24cde90d8040db5a8033d"></a><a name="abfa5e5e035d24cde90d8040db5a8033d"></a>Alarm ID</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="a8efccbd6aac949d6968791c7034859b4"><a name="a8efccbd6aac949d6968791c7034859b4"></a><a name="a8efccbd6aac949d6968791c7034859b4"></a>Alarm Severity</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="a0de796fe787342ab8b4d79605c26fd5e"><a name="a0de796fe787342ab8b4d79605c26fd5e"></a><a name="a0de796fe787342ab8b4d79605c26fd5e"></a>Automatically Cleared</p>
</th>
</tr>
</thead>
<tbody><tr id="r421248abf6e7467f8a5f35369e49f919"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="a89c1bbde023c49b589d51a4333104bc0"><a name="a89c1bbde023c49b589d51a4333104bc0"></a><a name="a89c1bbde023c49b589d51a4333104bc0"></a>12046</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="a2c4a1021d48243eab54f33a4ad3cc476"><a name="a2c4a1021d48243eab54f33a4ad3cc476"></a><a name="a2c4a1021d48243eab54f33a4ad3cc476"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="a1ef04204407e4501a45530111c3474f6"><a name="a1ef04204407e4501a45530111c3474f6"></a><a name="a1ef04204407e4501a45530111c3474f6"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s48a399d9c90b4e35948f704e3eb12a80"></a>

<a name="t3420b492362246468ce3daace11b4b40"></a>
<table><thead align="left"><tr id="r259e09aa76a24a4296dec132c9c060dc"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="afb0ac28dd20a4422ab92543b54bc76bf"><a name="afb0ac28dd20a4422ab92543b54bc76bf"></a><a name="afb0ac28dd20a4422ab92543b54bc76bf"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="add92e140675846e7b133879c8f09cdea"><a name="add92e140675846e7b133879c8f09cdea"></a><a name="add92e140675846e7b133879c8f09cdea"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="r0ec7b2f577d44d12a024d9394831e85d"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a0143328c00b44a50b516e63f32fcfeed"><a name="a0143328c00b44a50b516e63f32fcfeed"></a><a name="a0143328c00b44a50b516e63f32fcfeed"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a189107110c09471180582ad712be80ba"><a name="a189107110c09471180582ad712be80ba"></a><a name="a189107110c09471180582ad712be80ba"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="r4b0dcf6e86184509a26c40d5bb339726"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a658fff024bec4169a4afeb426e9774ac"><a name="a658fff024bec4169a4afeb426e9774ac"></a><a name="a658fff024bec4169a4afeb426e9774ac"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a6ae49873bfe447c9bfa7c0bde0d5fc2d"><a name="a6ae49873bfe447c9bfa7c0bde0d5fc2d"></a><a name="a6ae49873bfe447c9bfa7c0bde0d5fc2d"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="r5075ead7721149fd950b27ff33fae633"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a1d119a6e436649b494910e147c1ecbe6"><a name="a1d119a6e436649b494910e147c1ecbe6"></a><a name="a1d119a6e436649b494910e147c1ecbe6"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a308a7477a685449aa8e71dab8d6510f2"><a name="a308a7477a685449aa8e71dab8d6510f2"></a><a name="a308a7477a685449aa8e71dab8d6510f2"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
<tr id="r1b102a40bca548bd87ef313e3d820aaa"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="af8ec38bc29674ece80e72f5a5b2ec259"><a name="af8ec38bc29674ece80e72f5a5b2ec259"></a><a name="af8ec38bc29674ece80e72f5a5b2ec259"></a>NetworkCardName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a4c4b3ab5b46b43d4b6885ae3e88d6c40"><a name="a4c4b3ab5b46b43d4b6885ae3e88d6c40"></a><a name="a4c4b3ab5b46b43d4b6885ae3e88d6c40"></a>Specifies the network port for which the alarm is generated.</p>
</td>
</tr>
<tr id="r7f5e6940dcca42dbb494842a7df46979"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a604428ef3d104f38ad4e9ca94270277a"><a name="a604428ef3d104f38ad4e9ca94270277a"></a><a name="a604428ef3d104f38ad4e9ca94270277a"></a>Trigger Condition</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a75e097b1cc494aebabab911f659c7fad"><a name="a75e097b1cc494aebabab911f659c7fad"></a><a name="a75e097b1cc494aebabab911f659c7fad"></a>Generates an alarm when the actual indicator value exceeds the specified threshold.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s797be2c70ee4414dae8250558a1e9f75"></a>

The service performance deteriorates or services time out.

## Possible Causes<a name="sc95144fb23954aab8954477058b4b761"></a>

-   The alarm threshold is set improperly.
-   The network is abnormal.

## Procedure<a name="sa4515ea169554523a1fa203b8b482dc2"></a>

**Check whether the threshold is set properly.**

1.  Log in to MRS Manager and check whether the alarm threshold is set properly. \(By default, 0.5% is a proper value. However, users can configure the value as required.\)
    -   If yes, go to  [4](#lfa26e370338e428298aa1e49a437a7d7).
    -   If no, go to  [2](#l2b039a16453a418bafb5f800a1d72027).

2.  <a name="l2b039a16453a418bafb5f800a1d72027"></a>Based on actual usage condition, choose  **System** \> **Threshold Configuration** \> **Device** \> **Host** \> **Network Writing** \> **Network Write Packet Rate Information** \> **Write Packet Dropped Rate**  to modify the alarm threshold.
3.  Wait 5 minutes and check whether the alarm is cleared.
    -   If yes, no further action is required.
    -   If no, go to  [4](#lfa26e370338e428298aa1e49a437a7d7).


**Check whether the network is normal.**

1.  <a name="lfa26e370338e428298aa1e49a437a7d7"></a>Contact the system administrator to check whether the network is abnormal.
    -   If yes, go to  [5](#l717ea30d24974c67bf22471a08a44c8f)  to rectify the network fault.
    -   If no, go to  [7](#l1bf2c9a120e34912898a011f23ba7835).

2.  <a name="l717ea30d24974c67bf22471a08a44c8f"></a>Wait 5 minutes and check whether the alarm is cleared.
    -   If yes, no further action is required.
    -   If no, go to  [7](#l1bf2c9a120e34912898a011f23ba7835).


**Collect fault information.**

1.  On MRS Manager, choose  **System** \> **Export Log**.
2.  <a name="l1bf2c9a120e34912898a011f23ba7835"></a>Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).

## Related Information<a name="s59e958b994424bd38ef615bb89504c26"></a>

N/A


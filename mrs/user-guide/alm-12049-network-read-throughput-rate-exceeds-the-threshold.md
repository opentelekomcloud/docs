# ALM-12049 Network Read Throughput Rate Exceeds the Threshold<a name="EN-US_TOPIC_0125375533"></a>

## Description<a name="sf2f03e5aad23486680e153360b880331"></a>

The system checks the network read throughput rate every 30 seconds and compares the actual throughput rate with the threshold \(the default threshold is 80%\). This alarm is generated when the system detects that the network read throughput rate exceeds the threshold for several times \(5 times by default\) consecutively.

To change the threshold, choose  **System** \> **Threshold Configuration** \> **Device** \> **Host** \> **Network Reading** \> **Network Read Throughput Rate** \> **Read Throughput Rate**.

When the  **hit number** is 1, this alarm is cleared when the network read throughput rate is less than or equal to the threshold. When the **hit number**  is greater than 1, this alarm is cleared when the network read throughput rate is less than or equal to 90% of the threshold.

## Attribute<a name="s69f37d4097eb499a8b25813ebf05b956"></a>

<a name="t73d0d4a6b9894c459a1288247cb4f8b2"></a>
<table><thead align="left"><tr id="r555e4065ee9e40109523018287e042b0"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="acc8e2798d0a944738298c5f0314dfa43"><a name="acc8e2798d0a944738298c5f0314dfa43"></a><a name="acc8e2798d0a944738298c5f0314dfa43"></a>Alarm ID</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="af4470cc5f4af493cbcc570d220b27c9e"><a name="af4470cc5f4af493cbcc570d220b27c9e"></a><a name="af4470cc5f4af493cbcc570d220b27c9e"></a>Alarm Severity</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="a3f6d32515da4425697b3f063dc1aa45f"><a name="a3f6d32515da4425697b3f063dc1aa45f"></a><a name="a3f6d32515da4425697b3f063dc1aa45f"></a>Automatically Cleared</p>
</th>
</tr>
</thead>
<tbody><tr id="rc7eee6eb04154cfd9b2e4dcd69c20bc2"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="ab86b42435e7f4973adf9b5b5893df863"><a name="ab86b42435e7f4973adf9b5b5893df863"></a><a name="ab86b42435e7f4973adf9b5b5893df863"></a>12049</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="a77de872f91cd4fff806d74139d194ee0"><a name="a77de872f91cd4fff806d74139d194ee0"></a><a name="a77de872f91cd4fff806d74139d194ee0"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="a030c7cf1ddf3406d8a741f1ab1480a54"><a name="a030c7cf1ddf3406d8a741f1ab1480a54"></a><a name="a030c7cf1ddf3406d8a741f1ab1480a54"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s46e4698236e04df483bd30443feb0c4e"></a>

<a name="t1ee6407df2bb4c3892346d5d6fe7643a"></a>
<table><thead align="left"><tr id="r31f004501f984cc7b8c2d1ab83b61ae1"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="a3445c3d422154dfc8f5308a4adc11f26"><a name="a3445c3d422154dfc8f5308a4adc11f26"></a><a name="a3445c3d422154dfc8f5308a4adc11f26"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="a45b660672c1a4b0fb8f1cfdb302c7a10"><a name="a45b660672c1a4b0fb8f1cfdb302c7a10"></a><a name="a45b660672c1a4b0fb8f1cfdb302c7a10"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="r82a4e45780754638814beb9605668536"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a88a30c9da6d24d52a19de7e90c291e34"><a name="a88a30c9da6d24d52a19de7e90c291e34"></a><a name="a88a30c9da6d24d52a19de7e90c291e34"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="ae8ee7e2fc4954fe5bacea2569a02ccb0"><a name="ae8ee7e2fc4954fe5bacea2569a02ccb0"></a><a name="ae8ee7e2fc4954fe5bacea2569a02ccb0"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="r4e05e8daeeb5436085f228716d7c2ed6"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a831c6e0959e4407f883854bb1dd6e44a"><a name="a831c6e0959e4407f883854bb1dd6e44a"></a><a name="a831c6e0959e4407f883854bb1dd6e44a"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="ab6738c5d9bd5446cbee753e76b3af22a"><a name="ab6738c5d9bd5446cbee753e76b3af22a"></a><a name="ab6738c5d9bd5446cbee753e76b3af22a"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="rdd9ea0a6d9704018a0b30f85373afba4"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a244458cb79214a548a56e8c3e2c178e1"><a name="a244458cb79214a548a56e8c3e2c178e1"></a><a name="a244458cb79214a548a56e8c3e2c178e1"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a1763ad2130114758b86e5c084fdcfc44"><a name="a1763ad2130114758b86e5c084fdcfc44"></a><a name="a1763ad2130114758b86e5c084fdcfc44"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
<tr id="rb7462e74186342a79018905275086729"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="abad2e6f72e1f442abf593ce4b45a685b"><a name="abad2e6f72e1f442abf593ce4b45a685b"></a><a name="abad2e6f72e1f442abf593ce4b45a685b"></a>NetworkCardName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a06592d6b1c58474289bb0d194dafaa7f"><a name="a06592d6b1c58474289bb0d194dafaa7f"></a><a name="a06592d6b1c58474289bb0d194dafaa7f"></a>Specifies the network port for which the alarm is generated.</p>
</td>
</tr>
<tr id="r727ecd5f863f4fb290baee3c6bb9529d"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a79db561247bb40c3930b2868acf5fc21"><a name="a79db561247bb40c3930b2868acf5fc21"></a><a name="a79db561247bb40c3930b2868acf5fc21"></a>Trigger Condition</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a36fd6f66249b48269a1076b823f43b94"><a name="a36fd6f66249b48269a1076b823f43b94"></a><a name="a36fd6f66249b48269a1076b823f43b94"></a>Generates an alarm when the actual indicator value exceeds the specified threshold.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s23da36df666942af8d83d81abd6eede6"></a>

The service system runs improperly or is unavailable.

## Possible Causes<a name="s1727c552d5d54e96968bbb99e7c52eca"></a>

-   The alarm threshold is set improperly.
-   The network port rate cannot meet the current service requirements.

## Procedure<a name="sfb447b499c764fb7a0bd6fd8d7c6a64f"></a>

**Check whether the threshold is set properly.**

1.  Log in to MRS Manager and check whether the alarm threshold is set properly. \(By default, 80% is a proper value. However, users can configure the value as required.\)
    -   If yes, go to  [2](#le8402dd131c949ae8fbfa1dd7f191e24).
    -   If no, go to  [4](#l3636a1c6fbac4732899bcdf4e562e1dc).

2.  <a name="le8402dd131c949ae8fbfa1dd7f191e24"></a>Based on actual usage condition, choose  **System** \> **Threshold Configuration** \> **Device** \> **Host** \> **Network Reading** \> **Network Read Throughput Rate** \> **Read Throughput Rate**  to modify the alarm threshold.
3.  Wait 5 minutes and check whether the alarm is cleared.
    -   If yes, no further action is required.
    -   If no, go to  [4](#l3636a1c6fbac4732899bcdf4e562e1dc).


**Check whether the network port rate can meet the service requirements.**

1.  <a name="l3636a1c6fbac4732899bcdf4e562e1dc"></a>On MRS Manager, click the alarm in the real-time alarm list. In the  **Alarm Details**  area, obtain the IP address of the host and the network port name for which the alarm is generated.
2.  Use PuTTY to log in to the host for which the alarm is generated as user  **root**.
3.  Run the  **ethtool** _network port name_  command to check the maximum speed of the current network port.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >In the VM environment, you cannot run a command to query the network port rate. It is recommended that you contact the system administrator to confirm whether the network port rate meets the requirements.  

4.  If the network read throughput rate exceeds the threshold, contact the system administrator to increase the network port rate.
5.  Check whether the alarm is cleared.
    -   If yes, no further action is required.
    -   If no, go to  [10](#l75a1214d0eca42f8be61e9bfa3f175be).


**Collect fault information.**

1.  On MRS Manager, choose  **System** \> **Export Log**.
2.  <a name="l75a1214d0eca42f8be61e9bfa3f175be"></a>Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).

## Related Information<a name="s5cc0f965254f431e903a8044249a929c"></a>

N/A


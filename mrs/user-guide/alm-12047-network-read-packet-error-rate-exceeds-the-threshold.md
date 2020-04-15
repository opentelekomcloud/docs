# ALM-12047 Network Read Packet Error Rate Exceeds the Threshold<a name="EN-US_TOPIC_0125375303"></a>

## Description<a name="s9b68b91bac6541d1b37a9af9f01bf827"></a>

The system checks the network read packet error rate every 30 seconds and compares the actual packet error rate with the threshold \(the default threshold is 0.5%\). This alarm is generated when the system detects that the network read packet error rate exceeds the threshold for several times \(5 times by default\) consecutively.

To change the threshold, choose  **System** \> **Threshold Configuration** \> **Device** \> **Host** \> **Network Reading** \> **Network Read Packet Rate Information** \> **Read Packet Error Rate**.

When the  **hit number** is 1, this alarm is cleared when the network read packet error rate is less than or equal to the threshold. When the **hit number**  is greater than 1, this alarm is cleared when the value of the network read packet error rate is less than or equal to 90% of the threshold.

## Attribute<a name="sf61fb5c321d748c89f200b8597a73403"></a>

<a name="tadcd2144a7cf48728d24880f3e3353ce"></a>
<table><thead align="left"><tr id="r8e80a6de06094488868cafd46d5e3a0b"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="ab2a64c728b5f48f28b316bc7adc97528"><a name="ab2a64c728b5f48f28b316bc7adc97528"></a><a name="ab2a64c728b5f48f28b316bc7adc97528"></a>Alarm ID</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="ab17c3e8a853e4983b2e901bf46293217"><a name="ab17c3e8a853e4983b2e901bf46293217"></a><a name="ab17c3e8a853e4983b2e901bf46293217"></a>Alarm Severity</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="a4d3ea0f1b4c14505817651453b85d774"><a name="a4d3ea0f1b4c14505817651453b85d774"></a><a name="a4d3ea0f1b4c14505817651453b85d774"></a>Automatically Cleared</p>
</th>
</tr>
</thead>
<tbody><tr id="r47f4d39629aa463688124433695b71c2"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="a6372f1e11d8a4bb2ae7bdcff904ccd39"><a name="a6372f1e11d8a4bb2ae7bdcff904ccd39"></a><a name="a6372f1e11d8a4bb2ae7bdcff904ccd39"></a>12047</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="adf318ee2b07447afa72f0d2a6436d1b1"><a name="adf318ee2b07447afa72f0d2a6436d1b1"></a><a name="adf318ee2b07447afa72f0d2a6436d1b1"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="ab3b6065693c94181bee405fc550f2f42"><a name="ab3b6065693c94181bee405fc550f2f42"></a><a name="ab3b6065693c94181bee405fc550f2f42"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s95454354eb634c57971a371b442cd7f6"></a>

<a name="ta924e86c49b443708c98e254688706ad"></a>
<table><thead align="left"><tr id="re64fd5472732417db00984cce0b0e038"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="ae8d73aa520714d459c3f00f388466322"><a name="ae8d73aa520714d459c3f00f388466322"></a><a name="ae8d73aa520714d459c3f00f388466322"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="a7b63ede518b14ea897d7c87ecb7bbe1b"><a name="a7b63ede518b14ea897d7c87ecb7bbe1b"></a><a name="a7b63ede518b14ea897d7c87ecb7bbe1b"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="rfc104f06ec06435aa1862b774fd3ab9d"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="aeca56bd9ae1e44ecb5afb0a48a5610df"><a name="aeca56bd9ae1e44ecb5afb0a48a5610df"></a><a name="aeca56bd9ae1e44ecb5afb0a48a5610df"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="ac8ba6af521294f92a4e91dcb384894cb"><a name="ac8ba6af521294f92a4e91dcb384894cb"></a><a name="ac8ba6af521294f92a4e91dcb384894cb"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="r7b7689796b544dd5a32615393d824349"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a9c01823ae9b3487cb702f66b890782ef"><a name="a9c01823ae9b3487cb702f66b890782ef"></a><a name="a9c01823ae9b3487cb702f66b890782ef"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="ae27b9f96f5904a04bdb390e5364004f4"><a name="ae27b9f96f5904a04bdb390e5364004f4"></a><a name="ae27b9f96f5904a04bdb390e5364004f4"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="r0a3242c9dcbe48f8bb9adc560a1f5b2a"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="adcf75bfb81b24a1d91936f651910e28a"><a name="adcf75bfb81b24a1d91936f651910e28a"></a><a name="adcf75bfb81b24a1d91936f651910e28a"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a563b2d74c0974a799caa8e376850152f"><a name="a563b2d74c0974a799caa8e376850152f"></a><a name="a563b2d74c0974a799caa8e376850152f"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
<tr id="r827c2fc4b1734d03ab9e466493cf8aac"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a73dd12791e34451fbc56f44b8780fed3"><a name="a73dd12791e34451fbc56f44b8780fed3"></a><a name="a73dd12791e34451fbc56f44b8780fed3"></a>NetworkCardName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a1b56cd8a1bba49dfb176496e880b2baf"><a name="a1b56cd8a1bba49dfb176496e880b2baf"></a><a name="a1b56cd8a1bba49dfb176496e880b2baf"></a>Specifies the network port for which the alarm is generated.</p>
</td>
</tr>
<tr id="rd754dd9983854d80b0a6d1f6930c5bc3"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="ac523cbefe2fe4512b7b48974edf1c5d2"><a name="ac523cbefe2fe4512b7b48974edf1c5d2"></a><a name="ac523cbefe2fe4512b7b48974edf1c5d2"></a>Trigger Condition</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="abc6081578e7e4ca6a8af68597237bc57"><a name="abc6081578e7e4ca6a8af68597237bc57"></a><a name="abc6081578e7e4ca6a8af68597237bc57"></a>Generates an alarm when the actual indicator value exceeds the specified threshold.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s10b7a87c789442a592ff31e1a043619b"></a>

The communication interrupts intermittently and services time out.

## Possible Causes<a name="s2b481a9a75ac4ebc98e3d2d2869d34dc"></a>

-   The alarm threshold is set improperly.
-   The network is abnormal.

## Procedure<a name="s877cd81dd190402c82a80642749615af"></a>

**Check whether the threshold is set properly.**

1.  Log in to MRS Manager and check whether the alarm threshold is set properly. \(By default, 0.5% is a proper value. However, users can configure the value as required.\)
    -   If yes, go to  [4](#lb71210fbe5224d1a8278676f6292e7ec).
    -   If no, go to  [2](#lfad94473d8894d5ba723a990c92dc35a).

2.  <a name="lfad94473d8894d5ba723a990c92dc35a"></a>Based on actual usage condition, choose  **System** \> **Threshold Configuration** \> **Device** \> **Host** \> **Network Reading** \> **Network Read Packet Rate Information** \> **Read Packet Error Rate**  to modify the alarm threshold.
3.  Wait 5 minutes and check whether the alarm is cleared.
    -   If yes, no further action is required.
    -   If no, go to  [4](#lb71210fbe5224d1a8278676f6292e7ec).


**Check whether the network is normal.**

1.  <a name="lb71210fbe5224d1a8278676f6292e7ec"></a>Contact the system administrator to check whether the network is abnormal.
    -   If yes, go to  [5](#l34a9b6fd4a9548318dc9177a9b41da17)  to rectify the network fault.
    -   If no, go to  [7](#lff49dc7d51bb40238bc96f71de682091).

2.  <a name="l34a9b6fd4a9548318dc9177a9b41da17"></a>Wait 5 minutes and check whether the alarm is cleared.
    -   If yes, no further action is required.
    -   If no, go to  [7](#lff49dc7d51bb40238bc96f71de682091).


**Collect fault information.**

1.  On MRS Manager, choose  **System** \> **Export Log**.
2.  <a name="lff49dc7d51bb40238bc96f71de682091"></a>Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).

## Related Information<a name="s5bf9ebfd4a854b9cb0654eeeac05c43d"></a>

N/A


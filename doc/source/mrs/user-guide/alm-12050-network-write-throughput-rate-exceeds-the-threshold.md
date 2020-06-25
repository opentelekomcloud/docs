# ALM-12050 Network Write Throughput Rate Exceeds the Threshold<a name="EN-US_TOPIC_0125375548"></a>

## Description<a name="s9a3a9e8b92d04aa7b60d00eef028a45e"></a>

The system checks the network write throughput rate every 30 seconds and compares the actual throughput rate with the threshold \(the default threshold is 80%\). This alarm is generated when the system detects that the network write throughput rate exceeds the threshold for several times \(5 times by default\) consecutively.

To change the threshold, choose  **System** \> **Threshold Configuration** \> **Device** \> **Host** \> **Network Writing** \> **Network Write Throughput Rate** \> **Write Throughput Rate**.

When the  **hit number** is 1, this alarm is cleared when the network write throughput rate is less than or equal to the threshold. When the **hit number**  is greater than 1, this alarm is cleared when the network write throughput rate is less than or equal to 90% of the threshold.

## Attribute<a name="s1c195bd0bfd248198585979f53c10dbc"></a>

<a name="t984781be7ef04048a353d93cc6190671"></a>
<table><thead align="left"><tr id="r581147cd9f084f09ba8f5e37a579ad9d"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="aa153d5f524fc46dd9914855283c7b647"><a name="aa153d5f524fc46dd9914855283c7b647"></a><a name="aa153d5f524fc46dd9914855283c7b647"></a>Alarm ID</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="a7cfc0064d35e4de3ace6415a78457871"><a name="a7cfc0064d35e4de3ace6415a78457871"></a><a name="a7cfc0064d35e4de3ace6415a78457871"></a>Alarm Severity</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="a01103e4d9468415285e4d0b2f70cf765"><a name="a01103e4d9468415285e4d0b2f70cf765"></a><a name="a01103e4d9468415285e4d0b2f70cf765"></a>Automatically Cleared</p>
</th>
</tr>
</thead>
<tbody><tr id="rf0896cb22d5c496083a7214f770bf71c"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="aa2cede5c5fad4773a708d768e9fcfc37"><a name="aa2cede5c5fad4773a708d768e9fcfc37"></a><a name="aa2cede5c5fad4773a708d768e9fcfc37"></a>12050</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="ab54841d02d264da388671664fc491a8f"><a name="ab54841d02d264da388671664fc491a8f"></a><a name="ab54841d02d264da388671664fc491a8f"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="a61347a826b9f44d7bdef7a06f176fb9e"><a name="a61347a826b9f44d7bdef7a06f176fb9e"></a><a name="a61347a826b9f44d7bdef7a06f176fb9e"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="sfd0f7b8d9575492c845dec6fd39b826a"></a>

<a name="tf9830ea2c6c9463da221d1681e739f68"></a>
<table><thead align="left"><tr id="rb582b1d20138468285cf27472988e3ac"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="a0db1cc750388480e99d25e31af8585c1"><a name="a0db1cc750388480e99d25e31af8585c1"></a><a name="a0db1cc750388480e99d25e31af8585c1"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="aa58fc5dbf8874f8f90e8163495ee4d88"><a name="aa58fc5dbf8874f8f90e8163495ee4d88"></a><a name="aa58fc5dbf8874f8f90e8163495ee4d88"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="r8c785c3c00584c1fbe121944e5dff780"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a57bace411d3d436380ebc967bd0b22a3"><a name="a57bace411d3d436380ebc967bd0b22a3"></a><a name="a57bace411d3d436380ebc967bd0b22a3"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a172da7f498154ebba022e81205a2d3fa"><a name="a172da7f498154ebba022e81205a2d3fa"></a><a name="a172da7f498154ebba022e81205a2d3fa"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="r3f7097c0635d4d88ae6dcd0c2e5b326a"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="acf8209c8d4f046c8afd212757b313c71"><a name="acf8209c8d4f046c8afd212757b313c71"></a><a name="acf8209c8d4f046c8afd212757b313c71"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="ae21df5c6b2f54b12bfa5f888ef82decc"><a name="ae21df5c6b2f54b12bfa5f888ef82decc"></a><a name="ae21df5c6b2f54b12bfa5f888ef82decc"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="r743c3f02b2034266a145b2738ead8c38"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a317202a599b6433f911b3a1d197eb824"><a name="a317202a599b6433f911b3a1d197eb824"></a><a name="a317202a599b6433f911b3a1d197eb824"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a0632eba40fd44ca79b965d468d7d264f"><a name="a0632eba40fd44ca79b965d468d7d264f"></a><a name="a0632eba40fd44ca79b965d468d7d264f"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
<tr id="r9271b5de0da44622a956678fd6513750"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="ac8a6c159f8384c4ba96a14c43aca9fef"><a name="ac8a6c159f8384c4ba96a14c43aca9fef"></a><a name="ac8a6c159f8384c4ba96a14c43aca9fef"></a>NetworkCardName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a1461b44288ce40ffbee10a3e597325c8"><a name="a1461b44288ce40ffbee10a3e597325c8"></a><a name="a1461b44288ce40ffbee10a3e597325c8"></a>Specifies the network port for which the alarm is generated.</p>
</td>
</tr>
<tr id="rc752193ddca6406e9d48618458b1d104"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="ab423327e33da4e5da9584bb019366f3e"><a name="ab423327e33da4e5da9584bb019366f3e"></a><a name="ab423327e33da4e5da9584bb019366f3e"></a>Trigger Condition</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="aa9a3ddf5f1c546a1b236f32d6e56f76f"><a name="aa9a3ddf5f1c546a1b236f32d6e56f76f"></a><a name="aa9a3ddf5f1c546a1b236f32d6e56f76f"></a>Generates an alarm when the actual indicator value exceeds the specified threshold.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="sb4929091681c438c9f3652564d000d1e"></a>

The service system runs improperly or is unavailable.

## Possible Causes<a name="sfc06d4f73fdd48d399348d3230a1e0a2"></a>

-   The alarm threshold is set improperly.
-   The network port rate cannot meet the current service requirements.

## Procedure<a name="s6ab599d278ec48b7981b96c7a7153765"></a>

**Check whether the threshold is set properly.**

1.  Log in to MRS Manager and check whether the alarm threshold is set properly. \(By default, 80% is a proper value. However, users can configure the value as required.\)
    -   If yes, go to  [4](#l29d75f46243c4a36b73bafbc8f329306).
    -   If no, go to  [2](#l7a0e54fd360642d9a49dda4443f0cc77).

2.  <a name="l7a0e54fd360642d9a49dda4443f0cc77"></a>Based on actual usage condition, choose  **System** \> **Threshold Configuration** \> **Device** \> **Host** \> **Network Writing** \> **Network Write Throughput Rate** \> **Write Throughput Rate**  to modify the alarm threshold.
3.  Wait 5 minutes and check whether the alarm is cleared.
    -   If yes, no further action is required.
    -   If no, go to  [4](#l29d75f46243c4a36b73bafbc8f329306).


**Check whether the network port rate can meet the service requirements.**

1.  <a name="l29d75f46243c4a36b73bafbc8f329306"></a>On MRS Manager, click the alarm in the real-time alarm list. In the  **Alarm Details**  area, obtain the IP address of the host and the network port name for which the alarm is generated.
2.  Use PuTTY to log in to the host for which the alarm is generated as user  **root**.
3.  Run the  **ethtool** _network port name_  command to check the maximum speed of the current network port.

    >![](/images/icon-note.gif) **NOTE:**   
    >In the VM environment, you cannot run a command to query the network port rate. It is recommended that you contact the system administrator to confirm whether the network port rate meets the requirements.  

4.  If the network write throughput rate exceeds the threshold, contact the system administrator to increase the network port rate.
5.  Check whether the alarm is cleared.
    -   If yes, no further action is required.
    -   If no, go to  [10](#lc7d1b5ff13194cb6a0a95f5760168a9f).


**Collect fault information.**

1.  On MRS Manager, choose  **System** \> **Export Log**.
2.  <a name="lc7d1b5ff13194cb6a0a95f5760168a9f"></a>Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).

## Related Information<a name="s630cbaed013a4f7dadbdeb189f025a0f"></a>

N/A


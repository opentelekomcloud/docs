# ALM-12040 Insufficient System Entropy<a name="EN-US_TOPIC_0125375635"></a>

## Description<a name="s9d91acf5fd5e45afbd5f9cabda28df8a"></a>

At 00:00:00 every day, the system checks the entropy five times consecutively. First, the system checks whether either the rng-tools or haveged tool is enabled and correctly configured. If not, the system checks the current entropy. This alarm is generated when the entropy is less than 500 in the five checks.

This alarm is cleared in any of the following scenarios:

-   True random number mode is configured.
-   Random numbers are configured in pseudo-random number mode.
-   Neither the true random number mode nor pseudo-random number mode is configured but the entropy is greater than or equal to 500 in at least one of the five checks.

## Attribute<a name="s6d656ffea9ec4829ae0a18559cd0abf9"></a>

<a name="t6de205db7eeb4c7baeed9f4636872e2a"></a>
<table><thead align="left"><tr id="r636b3a0b4b1a48beb6d98c73e89d15d7"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="afa4ff73e34bb4c1bbb6e82f35dffd87b"><a name="afa4ff73e34bb4c1bbb6e82f35dffd87b"></a><a name="afa4ff73e34bb4c1bbb6e82f35dffd87b"></a><strong id="ab9ee382ceccf45a4ac9b90222435509a"><a name="ab9ee382ceccf45a4ac9b90222435509a"></a><a name="ab9ee382ceccf45a4ac9b90222435509a"></a>Alarm ID</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="en-us_topic_0035546890_p861763175025"><a name="en-us_topic_0035546890_p861763175025"></a><a name="en-us_topic_0035546890_p861763175025"></a><strong id="a6da88379403f475eb11ba416e18fc6f7"><a name="a6da88379403f475eb11ba416e18fc6f7"></a><a name="a6da88379403f475eb11ba416e18fc6f7"></a>Alarm Severity</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="aa28cc3e849204b428ac7431cd3743782"><a name="aa28cc3e849204b428ac7431cd3743782"></a><a name="aa28cc3e849204b428ac7431cd3743782"></a><strong id="a69f6410310544c27ad5e56245c4a5bc5"><a name="a69f6410310544c27ad5e56245c4a5bc5"></a><a name="a69f6410310544c27ad5e56245c4a5bc5"></a>Automatically Cleared</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="ra80111301f714cc8b77be4be2b48272c"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="a5d6049944f62499fbd94223bb35e304d"><a name="a5d6049944f62499fbd94223bb35e304d"></a><a name="a5d6049944f62499fbd94223bb35e304d"></a>12040</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="a0d423d0cbcf34fa3a35968e91cce37ec"><a name="a0d423d0cbcf34fa3a35968e91cce37ec"></a><a name="a0d423d0cbcf34fa3a35968e91cce37ec"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="a7f9329cac587471bb217cd5ef3870e78"><a name="a7f9329cac587471bb217cd5ef3870e78"></a><a name="a7f9329cac587471bb217cd5ef3870e78"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s9272876bdf14493089887ef787a4bf03"></a>

<a name="t51ebe063dbe24af781c90bab41abc9a4"></a>
<table><thead align="left"><tr id="r3d6d8c30923941258ab45e7d9e92638d"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0035546890_p572496175025"><a name="en-us_topic_0035546890_p572496175025"></a><a name="en-us_topic_0035546890_p572496175025"></a><strong id="a56317ab302344aec81f3af52aba80d26"><a name="a56317ab302344aec81f3af52aba80d26"></a><a name="a56317ab302344aec81f3af52aba80d26"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="a28856617ff354fecae2b6ddad5e85dd8"><a name="a28856617ff354fecae2b6ddad5e85dd8"></a><a name="a28856617ff354fecae2b6ddad5e85dd8"></a><strong id="a8c5bc3d07cad494eafcac76d8130ad89"><a name="a8c5bc3d07cad494eafcac76d8130ad89"></a><a name="a8c5bc3d07cad494eafcac76d8130ad89"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r90d21517768c4b5595b4356b62305ce7"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="ab2aefa8682c74a9dbe445731ad1394e8"><a name="ab2aefa8682c74a9dbe445731ad1394e8"></a><a name="ab2aefa8682c74a9dbe445731ad1394e8"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="ac3573d8d62aa416a9d78cb82212aaad2"><a name="ac3573d8d62aa416a9d78cb82212aaad2"></a><a name="ac3573d8d62aa416a9d78cb82212aaad2"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="r8eac8f94a3e443d9a936031a9910d02a"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a68172476b88b445298126194d397f007"><a name="a68172476b88b445298126194d397f007"></a><a name="a68172476b88b445298126194d397f007"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a93dc8c6d310c48c59885e8ad7933e440"><a name="a93dc8c6d310c48c59885e8ad7933e440"></a><a name="a93dc8c6d310c48c59885e8ad7933e440"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="r799a25632950477cb958bf2df86dd2e7"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="ad3e6766cff774fe2bf969436f812c9e7"><a name="ad3e6766cff774fe2bf969436f812c9e7"></a><a name="ad3e6766cff774fe2bf969436f812c9e7"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="af84e00c397ed451fa8c0f590f8f2e62f"><a name="af84e00c397ed451fa8c0f590f8f2e62f"></a><a name="af84e00c397ed451fa8c0f590f8f2e62f"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s18b4004b3d3e4b5b8aad5baae8780776"></a>

Decryption failures occur and functions related to decryption are affected, for example, DBService installation.

## Possible Causes<a name="sa36659ddbaa64bda95d61cd8b34b82d2"></a>

The haveged or rngd service is abnormal.

## Procedure<a name="s0971fd7568104827a1d9ca2ff0383cce"></a>

1.  On the MRS Manager portal, click  **Alarm**.
2.  View detailed alarm information to obtain the value of the  **HostName**  field.
3.  Log in to the node for which the alarm is generated. Run the  **sudo su - root**  command to switch the user.
4.  Run the  **/bin/rpm -qa | grep -w "haveged"**  command. If the command is executed successfully, run the  **/sbin/service haveged status |grep "running"**  command and view the command output.
    -   If the command is executed successfully, the haveged service is correctly installed and configured, and is running properly. Go to  [8](#l28aa9fc1853844259d1e16cd35625c7a).
    -   If the command is not executed successfully, the haveged service is not running properly. Go to  [5](#l58d13ea0fb1d4a9da8fdf921ee2b5123).

5.  <a name="l58d13ea0fb1d4a9da8fdf921ee2b5123"></a>Run the  **/bin/rpm -qa | grep -w "rng-tools"** command. If the command is executed successfully, run the **ps -ef | grep -v "grep" | grep rngd | tr -d " " | grep "\\-o/dev/random" | grep "\\-r/dev/urandom"**  command and view the command output.
    -   If the command is executed successfully, the rngd service is correctly installed and configured, and is running properly. Go to  [8](#l28aa9fc1853844259d1e16cd35625c7a).
    -   If the command is not executed successfully, the rngd service is not running properly. Go to  [6](#la98d753b10874ef49baf006263e56a99).

6.  <a name="la98d753b10874ef49baf006263e56a99"></a>Manually configure the system entropy. For details, see  [Related Information](#s1192d47413f2464fbf8f5330cbd55f85).
7.  Wait until 00:00:00, at which time the system checks the entropy again. Check whether the alarm is cleared automatically.
    -   If yes, no further action is required.
    -   If no, go to  [8](#l28aa9fc1853844259d1e16cd35625c7a).

8.  <a name="l28aa9fc1853844259d1e16cd35625c7a"></a>Collect fault information.
    1.  On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="s1192d47413f2464fbf8f5330cbd55f85"></a>

**Manually check the system entropy.**

Log in to the node and run the  **sudo su - root** command to switch the user. Run the **cat /proc/sys/kernel/random/entropy\_avail**  command to check whether the system entropy is greater than or equal to 500. If the system entropy is less than 500, you can reset it by using one of the following methods:

-   Using the haveged tool \(true random number mode\): Contact the public cloud O&M personnel to install the tool and start it.
-   Using the rng-tools tool \(pseudo-random number mode\): Contact the public cloud O&M personnel to install the tool.


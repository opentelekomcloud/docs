# ALM-12016 CPU Usage Exceeds the Threshold<a name="EN-US_TOPIC_0125375366"></a>

## Description<a name="s46cb8d291b2a44bca16fdcfbeaaab9a4"></a>

The system checks the CPU usage every 30 seconds and compares it with the threshold. This alarm is generated when the CPU usage exceeds the threshold several times \(configurable, 10 times by default\) consecutively.

This alarm is cleared when the average CPU usage is less than or equal to 90% of the threshold.

## **Attribute**<a name="s65eedc4596874ff3a3c469ddcd132005"></a>

<a name="te5a2dcee04c34f0a82430f0383ad353f"></a>
<table><thead align="left"><tr id="rd28a233721d54d84a091c63c7253da33"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="aa9d4417fd44f4ff692d82a26e981e66b"><a name="aa9d4417fd44f4ff692d82a26e981e66b"></a><a name="aa9d4417fd44f4ff692d82a26e981e66b"></a><strong id="a348afdb8385540318af5c7cf408cd5bb"><a name="a348afdb8385540318af5c7cf408cd5bb"></a><a name="a348afdb8385540318af5c7cf408cd5bb"></a>Alarm ID</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="ad87774d5c26a47fdb30eca53a3c9e447"><a name="ad87774d5c26a47fdb30eca53a3c9e447"></a><a name="ad87774d5c26a47fdb30eca53a3c9e447"></a><strong id="a2b50560fe57846a09788183fbf48c365"><a name="a2b50560fe57846a09788183fbf48c365"></a><a name="a2b50560fe57846a09788183fbf48c365"></a>Alarm Severity</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="ab4d3714923174578830c3f39ccd3c652"><a name="ab4d3714923174578830c3f39ccd3c652"></a><a name="ab4d3714923174578830c3f39ccd3c652"></a><strong id="ad8b9b7f1cb8b44558aa0939f5cf0ca95"><a name="ad8b9b7f1cb8b44558aa0939f5cf0ca95"></a><a name="ad8b9b7f1cb8b44558aa0939f5cf0ca95"></a>Automatically Cleared</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="rf7cc31cf08ef4738bce9746dc5b480c0"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="ac3f3722e963d4bd28f770ee9ef3a4a40"><a name="ac3f3722e963d4bd28f770ee9ef3a4a40"></a><a name="ac3f3722e963d4bd28f770ee9ef3a4a40"></a>12016</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="aa972e6f7c7a3423aa91e86c29f34f8e2"><a name="aa972e6f7c7a3423aa91e86c29f34f8e2"></a><a name="aa972e6f7c7a3423aa91e86c29f34f8e2"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="a48663e19a56b497c8c0d8a10346069f4"><a name="a48663e19a56b497c8c0d8a10346069f4"></a><a name="a48663e19a56b497c8c0d8a10346069f4"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s94b1824a6e2c4aa98470bcc05fb44782"></a>

<a name="t8d7b24233a4e4daa99a1672fe0d3cbb0"></a>
<table><thead align="left"><tr id="r82d724f3a7d9412bbe9a168b948bd17d"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="a977a41dcacf6463c9b12aede256f2ac9"><a name="a977a41dcacf6463c9b12aede256f2ac9"></a><a name="a977a41dcacf6463c9b12aede256f2ac9"></a><strong id="a58cbfe1bc9a64d44bc0b43d7ce971012"><a name="a58cbfe1bc9a64d44bc0b43d7ce971012"></a><a name="a58cbfe1bc9a64d44bc0b43d7ce971012"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="ae3f6108be6dc4c60b479650c235f38ce"><a name="ae3f6108be6dc4c60b479650c235f38ce"></a><a name="ae3f6108be6dc4c60b479650c235f38ce"></a><strong id="aa80b95fc5bad4551beff72a2174b7afe"><a name="aa80b95fc5bad4551beff72a2174b7afe"></a><a name="aa80b95fc5bad4551beff72a2174b7afe"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r05a9f33298f54abf85aca6c773c74ec2"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="ae368e4dd7c4e4879802526cd5fb7ac67"><a name="ae368e4dd7c4e4879802526cd5fb7ac67"></a><a name="ae368e4dd7c4e4879802526cd5fb7ac67"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="af40fed9758c54790920c32b827259adf"><a name="af40fed9758c54790920c32b827259adf"></a><a name="af40fed9758c54790920c32b827259adf"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="r5439e633fee740bea6965ac42d93ba7b"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a4710e64dec84416eb3c5adcd69fa675d"><a name="a4710e64dec84416eb3c5adcd69fa675d"></a><a name="a4710e64dec84416eb3c5adcd69fa675d"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a7f403db3dff444bc89623de473f82392"><a name="a7f403db3dff444bc89623de473f82392"></a><a name="a7f403db3dff444bc89623de473f82392"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="r9dc81892b4394678aa58004b6ab49044"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="af209fedd7fab47598f0ed21abe9b4001"><a name="af209fedd7fab47598f0ed21abe9b4001"></a><a name="af209fedd7fab47598f0ed21abe9b4001"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a90fbfc0ecdc242729e78dc78b3fc7058"><a name="a90fbfc0ecdc242729e78dc78b3fc7058"></a><a name="a90fbfc0ecdc242729e78dc78b3fc7058"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
<tr id="r827d6c8e3b8d469fbb86118e6b906bc1"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035469888_p377010104414"><a name="en-us_topic_0035469888_p377010104414"></a><a name="en-us_topic_0035469888_p377010104414"></a>Trigger Condition</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a2ace8e99ddec42628c79709238de3b48"><a name="a2ace8e99ddec42628c79709238de3b48"></a><a name="a2ace8e99ddec42628c79709238de3b48"></a>Generates an alarm when the actual indicator value exceeds the specified threshold.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s110660d78a57443c9cfe6902b4666136"></a>

Service processes respond slowly or become unavailable.

## Possible Causes<a name="s3b6dddeb37ea4a528eddd7503657dac2"></a>

-   The alarm threshold or  **Trigger Count**  is configured inappropriately.
-   The CPU configuration does not meet service requirements. As a result, the CPU usage reaches the upper limit.

## Procedure<a name="sf7ef6580d33a4d86bfae38d94f6a8d46"></a>

1.  Check whether the alarm threshold or  **Trigger Count**  is appropriate.
    1.  Log in to MRS Manager.
    2.  Choose  **System**  \>  **Configure Alarm Threshold**  \>  **Device**  \>  **Host**  \>  **CPU Usage**  \>  **CPU Usage**  and change the alarm threshold based on the actual CPU usage.
    3.  Choose  **System**  \>  **Configure Alarm Threshold**  \>  **Device**  \>  **Host**  \>  **CPU Usage**  \>  **CPU Usage** and change **Trigger Count**  based on the actual CPU usage.

        >![](/images/icon-note.gif) **NOTE:**   
        >This option defines the alarm check phase.  **Interval** indicates the alarm check period and **Trigger Count**  indicates the number of times the CPU usage exceeds the threshold. An alarm is generated if the CPU usage exceeds the threshold several times consecutively.  

    4.  Wait 2 minutes and check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [2](#l3623d196f8124ef89158a5577edf02f3).

2.  <a name="l3623d196f8124ef89158a5577edf02f3"></a>Expand the system capacity.
    1.  In the alarm list on MRS Manager, locate the row that contains the alarm, and view the IP address of the alarm node in the alarm details.
    2.  Log in to the alarm node.
    3.  Run the  **cat /proc/stat | awk 'NR==1'|awk '\{for\(i=2;i<=NF;i++\)j+=$i;print "" 100 - \($5+$6\) \* 100 / j;\}'**  command to check the system CPU usage.
    4.  If the CPU usage exceeds the threshold, expand the CPU capacity.
    5.  Check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [3](#l901ed97ca6dc4ee098890a11df51cec3).

3.  <a name="l901ed97ca6dc4ee098890a11df51cec3"></a>Collect fault information.
    1.  On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## **Related Information**<a name="s9ac55a2087664572951deebf2e7340b2"></a>

N/A


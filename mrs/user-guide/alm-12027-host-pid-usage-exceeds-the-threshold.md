# ALM-12027 Host PID Usage Exceeds the Threshold<a name="EN-US_TOPIC_0125375586"></a>

## Description<a name="s70db578ac1dc4ff09cb6f3aaddad4194"></a>

The system checks the PID usage every 30 seconds and compares it with the threshold. This alarm is generated when the PID usage exceeds the threshold and is cleared when it is less than or equal to the threshold.

## Attribute<a name="s96c31792562e45289dd16ab6bdd9d171"></a>

<a name="t18a90597435246b3984d50140b236fee"></a>
<table><thead align="left"><tr id="r9e00ef2cac4e4cba907c398e2c271cb1"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="en-us_topic_0035509085_p319458681142"><a name="en-us_topic_0035509085_p319458681142"></a><a name="en-us_topic_0035509085_p319458681142"></a><strong id="en-us_topic_0035509085_b190773561142"><a name="en-us_topic_0035509085_b190773561142"></a><a name="en-us_topic_0035509085_b190773561142"></a>Alarm ID</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="en-us_topic_0035509085_p17620221142"><a name="en-us_topic_0035509085_p17620221142"></a><a name="en-us_topic_0035509085_p17620221142"></a><strong id="en-us_topic_0035509085_b158582011142"><a name="en-us_topic_0035509085_b158582011142"></a><a name="en-us_topic_0035509085_b158582011142"></a>Alarm Severity</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="en-us_topic_0035509085_p94458961142"><a name="en-us_topic_0035509085_p94458961142"></a><a name="en-us_topic_0035509085_p94458961142"></a><strong id="en-us_topic_0035509085_b179042071142"><a name="en-us_topic_0035509085_b179042071142"></a><a name="en-us_topic_0035509085_b179042071142"></a>Automatically Cleared</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r2f5258e49cd54736be704fe594eac656"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0035509085_p330474251142"><a name="en-us_topic_0035509085_p330474251142"></a><a name="en-us_topic_0035509085_p330474251142"></a>12027</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0035509085_p595957381142"><a name="en-us_topic_0035509085_p595957381142"></a><a name="en-us_topic_0035509085_p595957381142"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0035509085_p625254351142"><a name="en-us_topic_0035509085_p625254351142"></a><a name="en-us_topic_0035509085_p625254351142"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="se034e3e220ab4d2ea41649d1fe464f3c"></a>

<a name="tc88a51409c2d4479b7e7940529cb391d"></a>
<table><thead align="left"><tr id="r62f0da56d08347be8aaedc14d33bd1b9"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0035509085_p170342011142"><a name="en-us_topic_0035509085_p170342011142"></a><a name="en-us_topic_0035509085_p170342011142"></a><strong id="a8e8ebffbf79947d38d4fd0fae3d01a56"><a name="a8e8ebffbf79947d38d4fd0fae3d01a56"></a><a name="a8e8ebffbf79947d38d4fd0fae3d01a56"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0035509085_p27933851142"><a name="en-us_topic_0035509085_p27933851142"></a><a name="en-us_topic_0035509085_p27933851142"></a><strong id="en-us_topic_0035509085_b251404671142"><a name="en-us_topic_0035509085_b251404671142"></a><a name="en-us_topic_0035509085_b251404671142"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r17d742d972a04238b07dbbfac2c97d2e"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035509085_p66807661142"><a name="en-us_topic_0035509085_p66807661142"></a><a name="en-us_topic_0035509085_p66807661142"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035509085_p42711391142"><a name="en-us_topic_0035509085_p42711391142"></a><a name="en-us_topic_0035509085_p42711391142"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="re66c0306bb4949ea98fcbb94cb7245ad"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035509085_p266527471142"><a name="en-us_topic_0035509085_p266527471142"></a><a name="en-us_topic_0035509085_p266527471142"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035509085_p113889311142"><a name="en-us_topic_0035509085_p113889311142"></a><a name="en-us_topic_0035509085_p113889311142"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="r3e792645a73545c6ad027814468dbb39"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035509085_p481406441142"><a name="en-us_topic_0035509085_p481406441142"></a><a name="en-us_topic_0035509085_p481406441142"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035509085_p70781201142"><a name="en-us_topic_0035509085_p70781201142"></a><a name="en-us_topic_0035509085_p70781201142"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
<tr id="ra93a853099a7430bacc036a18546e2f8"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035509085_p596761811142"><a name="en-us_topic_0035509085_p596761811142"></a><a name="en-us_topic_0035509085_p596761811142"></a>Trigger Condition</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035509085_p19325271142"><a name="en-us_topic_0035509085_p19325271142"></a><a name="en-us_topic_0035509085_p19325271142"></a>Generates an alarm when the actual indicator value exceeds the specified threshold.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s4d2d965176eb40fc8c54bbd89434d084"></a>

No PID is available for new processes and service processes are unavailable.

## Possible Causes<a name="se1116715a56e457dbce69d4443edf00f"></a>

-   Too many processes are running on the node.
-   The value of  **pid\_max**  needs to be increased.
-   The system is abnormal.

## Procedure<a name="sbf4375a924ca47528982057cf574d886"></a>

1.  Increase the value of  **pid\_max**.
    1.  On MRS Manager, click the alarm in the real-time alarm list. In the  **Alarm Details**  area, obtain the IP address of the host that generated the alarm.
    2.  Log in to the alarm node.
    3.  Run the  **cat /proc/sys/kernel/pid\_max** command to check the value of **pid\_max**.
    4.  If the PID usage exceeds the threshold, run the following command to double the value of pid\_max:

        **echo** _new pid\_max value_ **\> /proc/sys/kernel/pid\_max**.

        For example,

        **echo 65536 \> /proc/sys/kernel/pid\_max**

    5.  Wait 5 minutes and check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [2](#lb927f76fec0e471aaafc4093ee7c3292).

2.  <a name="lb927f76fec0e471aaafc4093ee7c3292"></a>Check whether the system environment is abnormal.
    1.  Contact the public cloud O&M personnel to check whether the operating system is abnormal.
        -   If yes, go to  [2](#lb927f76fec0e471aaafc4093ee7c3292)  to rectify the fault.
        -   If no, go to  [3](#l11c567f522484296803c67e563136e4d).

    2.  Wait 5 minutes and check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [3](#l11c567f522484296803c67e563136e4d).

3.  <a name="l11c567f522484296803c67e563136e4d"></a>Collect fault information.
    1.  On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## **Related Information**<a name="s3f7eb020b98343cf8bd98d808eb693cb"></a>

N/A


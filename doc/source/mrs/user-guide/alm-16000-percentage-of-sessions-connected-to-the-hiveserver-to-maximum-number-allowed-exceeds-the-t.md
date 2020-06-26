# ALM-16000 Percentage of Sessions Connected to the HiveServer to Maximum Number Allowed Exceeds the Threshold<a name="EN-US_TOPIC_0125375707"></a>

## Description<a name="s595b64f118cf41d79b0bb3c19ccf47cf"></a>

The system checks the percentage of sessions connected to the HiveServer to the maximum number allowed every 30 seconds. This indicator can be viewed on the Hive service monitoring page. This alarm is generated when the percentage exceeds the specified threshold and is automatically cleared when the percentage is less than or equal to the threshold.

## Attribute<a name="sf3eb6cd7924246868669de2cd2f311a1"></a>

<a name="en-us_topic_0035998732_table33142240"></a>
<table><thead align="left"><tr id="en-us_topic_0035998732_row21192109"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="en-us_topic_0035998732_p38839231"><a name="en-us_topic_0035998732_p38839231"></a><a name="en-us_topic_0035998732_p38839231"></a>Alarm ID</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="en-us_topic_0035998732_p58970022"><a name="en-us_topic_0035998732_p58970022"></a><a name="en-us_topic_0035998732_p58970022"></a>Alarm Severity</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="en-us_topic_0035998732_p11842506"><a name="en-us_topic_0035998732_p11842506"></a><a name="en-us_topic_0035998732_p11842506"></a>Automatically Cleared</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998732_row19718930"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0035998732_p53729511"><a name="en-us_topic_0035998732_p53729511"></a><a name="en-us_topic_0035998732_p53729511"></a>16000</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0035998732_p57123120"><a name="en-us_topic_0035998732_p57123120"></a><a name="en-us_topic_0035998732_p57123120"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0035998732_p63570006"><a name="en-us_topic_0035998732_p63570006"></a><a name="en-us_topic_0035998732_p63570006"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s388d9f6adf5a4c14a9df4fa244bc37c4"></a>

<a name="en-us_topic_0035998732_table48896832"></a>
<table><thead align="left"><tr id="en-us_topic_0035998732_row17284754"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0035998732_p57887863"><a name="en-us_topic_0035998732_p57887863"></a><a name="en-us_topic_0035998732_p57887863"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0035998732_p58405349"><a name="en-us_topic_0035998732_p58405349"></a><a name="en-us_topic_0035998732_p58405349"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998732_row33212803"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998732_p5882489"><a name="en-us_topic_0035998732_p5882489"></a><a name="en-us_topic_0035998732_p5882489"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998732_p6719600"><a name="en-us_topic_0035998732_p6719600"></a><a name="en-us_topic_0035998732_p6719600"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998732_row60476403"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998732_p66750478"><a name="en-us_topic_0035998732_p66750478"></a><a name="en-us_topic_0035998732_p66750478"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998732_p38079613"><a name="en-us_topic_0035998732_p38079613"></a><a name="en-us_topic_0035998732_p38079613"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998732_row7172200"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998732_p44077297"><a name="en-us_topic_0035998732_p44077297"></a><a name="en-us_topic_0035998732_p44077297"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998732_p13491266"><a name="en-us_topic_0035998732_p13491266"></a><a name="en-us_topic_0035998732_p13491266"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998732_row54312533"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998732_p37239078"><a name="en-us_topic_0035998732_p37239078"></a><a name="en-us_topic_0035998732_p37239078"></a>Trigger condition</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998732_p63575380"><a name="en-us_topic_0035998732_p63575380"></a><a name="en-us_topic_0035998732_p63575380"></a>Generates an alarm when the actual indicator value exceeds the specified threshold.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s8db9f246325b4b67880d02cf9866b318"></a>

New connections cannot be created.

## Possible Causes<a name="sf7ee83714e91409783e1e54121e0210b"></a>

Too many clients are connected to the HiveServer.

## Procedure<a name="sde40ef16971a4c408e79236877721d24"></a>

1.  Increase the maximum number of connections to Hive.
    1.  Log in to the MRS Manager portal.
    2.  Choose  **Service**  \>  **Hive**  \>  **Service Configuration**, and set **Type** to **All**.
    3.  Increase the value of the  **hive.server.session.control.maxconnections**  configuration item.

        Suppose the value of the configuration item is A, the threshold is B, and sessions connected to the HiveServer is C. Adjust the value of the configuration item according to A x B \> C. Sessions connected to the HiveServer can be viewed on the Hive service monitoring page.

    4.  Check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [2](#lbdffefe237de481d977793621186b966).

2.  <a name="lbdffefe237de481d977793621186b966"></a>Collect fault information.
    1.  On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="s8c1dbe7da2e141e3b543e132cd88a438"></a>

N/A


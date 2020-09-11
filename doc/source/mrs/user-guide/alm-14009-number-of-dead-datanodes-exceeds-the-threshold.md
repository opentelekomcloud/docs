# ALM-14009 Number of Dead DataNodes Exceeds the Threshold<a name="EN-US_TOPIC_0125375511"></a>

## Description<a name="s3230924ba1f6455f97694ffe9c71e015"></a>

The system checks the number of faulty DataNodes in the HDFS cluster every 30 seconds and compares it with the threshold. This alarm is generated when the number of faulty DataNodes in the HDFS cluster exceeds the threshold and is cleared when the number is less than or equal to the threshold.

## Attribute<a name="s2dd2b5d68da54b42a3d4606abfa18a78"></a>

<a name="en-us_topic_0035998728_table18759701"></a>
<table><thead align="left"><tr id="en-us_topic_0035998728_row48616240"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="en-us_topic_0035998728_p45601378"><a name="en-us_topic_0035998728_p45601378"></a><a name="en-us_topic_0035998728_p45601378"></a>Alarm ID</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="en-us_topic_0035998728_p2724161"><a name="en-us_topic_0035998728_p2724161"></a><a name="en-us_topic_0035998728_p2724161"></a>Alarm Severity</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="en-us_topic_0035998728_p19330484"><a name="en-us_topic_0035998728_p19330484"></a><a name="en-us_topic_0035998728_p19330484"></a>Automatically Cleared</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998728_row22265380"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0035998728_p58665336"><a name="en-us_topic_0035998728_p58665336"></a><a name="en-us_topic_0035998728_p58665336"></a>14009</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0035998728_p54271769"><a name="en-us_topic_0035998728_p54271769"></a><a name="en-us_topic_0035998728_p54271769"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0035998728_p33937134"><a name="en-us_topic_0035998728_p33937134"></a><a name="en-us_topic_0035998728_p33937134"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s1fce810ebbde48beb26d0f38491a4436"></a>

<a name="en-us_topic_0035998728_table64553311"></a>
<table><thead align="left"><tr id="en-us_topic_0035998728_row25037822"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0035998728_p14797678"><a name="en-us_topic_0035998728_p14797678"></a><a name="en-us_topic_0035998728_p14797678"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0035998728_p57761279"><a name="en-us_topic_0035998728_p57761279"></a><a name="en-us_topic_0035998728_p57761279"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998728_row48152024"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998728_p7999906"><a name="en-us_topic_0035998728_p7999906"></a><a name="en-us_topic_0035998728_p7999906"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998728_p44012677"><a name="en-us_topic_0035998728_p44012677"></a><a name="en-us_topic_0035998728_p44012677"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998728_row60569775"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998728_p7204713"><a name="en-us_topic_0035998728_p7204713"></a><a name="en-us_topic_0035998728_p7204713"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998728_p46710863"><a name="en-us_topic_0035998728_p46710863"></a><a name="en-us_topic_0035998728_p46710863"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998728_row17744591"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998728_p28025763"><a name="en-us_topic_0035998728_p28025763"></a><a name="en-us_topic_0035998728_p28025763"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998728_p55494360"><a name="en-us_topic_0035998728_p55494360"></a><a name="en-us_topic_0035998728_p55494360"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998728_row29687198"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998728_p55852871"><a name="en-us_topic_0035998728_p55852871"></a><a name="en-us_topic_0035998728_p55852871"></a>Trigger condition</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998728_p27788708"><a name="en-us_topic_0035998728_p27788708"></a><a name="en-us_topic_0035998728_p27788708"></a>Generates an alarm when the actual indicator value exceeds the specified threshold.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="scb09ac7900ec4d83b71d9cbda8afc4ee"></a>

Faulty DataNodes cannot provide HDFS services.

## Possible Causes<a name="s85040ecc001b4fdf8c5264748c4014a5"></a>

-   DataNodes are faulty or overloaded.
-   The network between the NameNode and the DataNode is disconnected or busy.
-   NameNodes are overloaded.

## Procedure<a name="s067131ebe078402487b8e0ceb687eec1"></a>

1.  Check whether DataNodes are faulty.
    1.  Use the client on the cluster node and run the  **hdfs dfsadmin -report**  command to check whether DataNodes are faulty.
        -   If yes, go to  [1.b](#lae0c2b7c4a7e4adda5ddda8b3554be61).
        -   If no, go to  [2.a](#lfdf7da325ac946149cce3c2e8c3010d8).

    2.  <a name="lae0c2b7c4a7e4adda5ddda8b3554be61"></a>On the MRS Manager portal, choose  **Service**  \>  **HDFS**  \>  **Instance**  to check whether any DataNode is stopped.
        -   If yes, go to  [1.c](#l64cba159022e44179b31a82685691d44).
        -   If no, go to  [2.a](#lfdf7da325ac946149cce3c2e8c3010d8).

    3.  <a name="l64cba159022e44179b31a82685691d44"></a>Select the DataNode instance, and choose  **More**  \>  **Restart Instance**  to restart it. Wait 5 minutes and check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [2.a](#lfdf7da325ac946149cce3c2e8c3010d8).

2.  Check the status of the network between the NameNode and the DataNode.
    1.  <a name="lfdf7da325ac946149cce3c2e8c3010d8"></a>Log in to the faulty DataNode using its service IP address. Run the  **ping** _IP address_ _of the_ _NameNode_  command to check whether the network between the DataNode and the NameNode is abnormal.
        -   If yes, go to  [2.b](#l99b13a80267945629f316520e7bbaa2d).
        -   If no, go to  [3.a](#l2f3f4319ac714251869d78716bee04bf).

    2.  <a name="l99b13a80267945629f316520e7bbaa2d"></a>Rectify the network fault. Wait 5 minutes and check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [3.a](#l2f3f4319ac714251869d78716bee04bf).

3.  Check whether the DataNode is overloaded.
    1.  <a name="l2f3f4319ac714251869d78716bee04bf"></a>On the MRS Manager portal, click  **Alarm**  and check whether alarm  **ALM-14008 HDFS DataNode Memory Usage Exceeds the Threshold**  exists.
        -   If yes, go to  [3.b](#lde21bd6b50d04ab2b8874945bf239d5c).
        -   If no, go to  [4.a](#en-us_topic_0035998728_step9).

    2.  <a name="lde21bd6b50d04ab2b8874945bf239d5c"></a>Follow the procedures in  [ALM-14008 HDFS DataNode Memory Usage Exceeds the Threshold](alm-14008-hdfs-datanode-memory-usage-exceeds-the-threshold.md)  to handle the alarm and check whether the alarm is cleared.
        -   If yes, go to  [3.c](#en-us_topic_0035998728_ss10).
        -   If no, go to  [4.a](#en-us_topic_0035998728_step9).

    3.  <a name="en-us_topic_0035998728_ss10"></a>Wait 5 minutes and check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [4.a](#en-us_topic_0035998728_step9).

4.  Check whether the NameNode is overloaded.
    1.  <a name="en-us_topic_0035998728_step9"></a>On the MRS Manager portal, click  **Alarm**  and check whether alarm  **ALM-14007 HDFS NameNode Memory Usage Exceeds the Threshold**  exists.
        -   If yes, go to  [4.b](#lb965e85aafde41c39e9b76cf640cae40).
        -   If no, go to  [5](#lddadffb2bf9d45ef8cd67b8b88f57f74).

    2.  <a name="lb965e85aafde41c39e9b76cf640cae40"></a>Follow the procedures in  [ALM-14007 HDFS NameNode Memory Usage Exceeds the Threshold](alm-14007-hdfs-namenode-memory-usage-exceeds-the-threshold.md)  to handle the alarm and check whether the alarm is cleared.
        -   If yes, go to  [4.c](#en-us_topic_0035998728_ss13).
        -   If no, go to  [5](#lddadffb2bf9d45ef8cd67b8b88f57f74).

    3.  <a name="en-us_topic_0035998728_ss13"></a>Wait 5 minutes and check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [5](#lddadffb2bf9d45ef8cd67b8b88f57f74).

5.  <a name="lddadffb2bf9d45ef8cd67b8b88f57f74"></a>Collect fault information.
    1.  On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="s89e73e1920f74c8bbe42ebd1a35ed2cb"></a>

N/A


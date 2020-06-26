# ALM-12052 TCP Temporary Port Usage Exceeds the Threshold<a name="EN-US_TOPIC_0125375874"></a>

## Description<a name="s0b099c1f9c1e4afcb123d05b7fb767a0"></a>

The system checks the TCP temporary port usage every 30 seconds and compares the actual usage with the threshold \(the default threshold is 80%\). This alarm is generated when the TCP temporary port usage exceeds the threshold for several times \(5 times by default\) consecutively.

To change the threshold, choose  **System** \> **Threshold Configuration** \> **Device** \> **Host** \> **Network Status** \> **TCP Ephemeral Port Usage** \> **TCP Ephemeral Port Usage**.

When the  **hit number** is 1, this alarm is cleared when the TCP temporary port usage is less than or equal to the threshold. When the **hit number**  is greater than 1, this alarm is cleared when the TCP temporary port usage is less than or equal to 90% of the threshold.

## Attribute<a name="s42cce9b330ed4d82b14fe74cf2fb26a2"></a>

<a name="t0332d10b49f1408b8973b8d72e3c55e7"></a>
<table><thead align="left"><tr id="rc4b4d4de63b84ec1ab2c5bc2954b636e"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="ad09653acd3fe4407a6e9a171d9693627"><a name="ad09653acd3fe4407a6e9a171d9693627"></a><a name="ad09653acd3fe4407a6e9a171d9693627"></a>Alarm ID</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="a3695e6a0196e45d1a1a459c700ab65f6"><a name="a3695e6a0196e45d1a1a459c700ab65f6"></a><a name="a3695e6a0196e45d1a1a459c700ab65f6"></a>Alarm Severity</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="a56f58b0cd3674a67a9e01e9b0434630f"><a name="a56f58b0cd3674a67a9e01e9b0434630f"></a><a name="a56f58b0cd3674a67a9e01e9b0434630f"></a>Automatically Cleared</p>
</th>
</tr>
</thead>
<tbody><tr id="ra1802112050e488eac6060e715108dad"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="aecfcfc65aac14a1c8d551f900eeac159"><a name="aecfcfc65aac14a1c8d551f900eeac159"></a><a name="aecfcfc65aac14a1c8d551f900eeac159"></a>12052</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="a30ef89c106484bd2939400b3f47647b0"><a name="a30ef89c106484bd2939400b3f47647b0"></a><a name="a30ef89c106484bd2939400b3f47647b0"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="ab06e043789e344fd974120d22065850e"><a name="ab06e043789e344fd974120d22065850e"></a><a name="ab06e043789e344fd974120d22065850e"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="s73fdf3dfc33145bc872c047d7090474c"></a>

<a name="tc92660539b3e4b67b9047c8b6444a3a3"></a>
<table><thead align="left"><tr id="r53240ba189344bd38c136c5518e609b9"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="a65b12a0375b94e36846b30e4dcad3e08"><a name="a65b12a0375b94e36846b30e4dcad3e08"></a><a name="a65b12a0375b94e36846b30e4dcad3e08"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="a6b272e48b2ce484c98f24316184785b0"><a name="a6b272e48b2ce484c98f24316184785b0"></a><a name="a6b272e48b2ce484c98f24316184785b0"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="r53925944d14441629125be820948f3f9"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a789b5932c04649f4aaf42d606aebba7d"><a name="a789b5932c04649f4aaf42d606aebba7d"></a><a name="a789b5932c04649f4aaf42d606aebba7d"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="ad0a509e61b50499db7b03bdb994c7625"><a name="ad0a509e61b50499db7b03bdb994c7625"></a><a name="ad0a509e61b50499db7b03bdb994c7625"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="rd76178a573f0472a9f3e02b54567c949"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a8ff17e47902549aa80114cd2a5fdc081"><a name="a8ff17e47902549aa80114cd2a5fdc081"></a><a name="a8ff17e47902549aa80114cd2a5fdc081"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a45c0c589a7bd415181e6f1b50094875b"><a name="a45c0c589a7bd415181e6f1b50094875b"></a><a name="a45c0c589a7bd415181e6f1b50094875b"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="r71e0e3370aaa4188ac35d3f30b3cf38d"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="ad94d9b292d6e4506ba01e407a5a02454"><a name="ad94d9b292d6e4506ba01e407a5a02454"></a><a name="ad94d9b292d6e4506ba01e407a5a02454"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="ab55c68cff70e48389df760ffd8cb5631"><a name="ab55c68cff70e48389df760ffd8cb5631"></a><a name="ab55c68cff70e48389df760ffd8cb5631"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
<tr id="r76bf7a55df864a9aaac8b7d19c0bb5fd"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a13cff876df2f4594a57b6ab290b64b25"><a name="a13cff876df2f4594a57b6ab290b64b25"></a><a name="a13cff876df2f4594a57b6ab290b64b25"></a>Trigger Condition</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a0ded3770709e4b3ca868150a7e1b4c41"><a name="a0ded3770709e4b3ca868150a7e1b4c41"></a><a name="a0ded3770709e4b3ca868150a7e1b4c41"></a>Generates an alarm when the actual indicator value exceeds the specified threshold.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="sd3fff323096744b9864109bbdc3327ff"></a>

Services on the host cannot establish external connections, and therefore they are interrupted.

## Possible Causes<a name="s9a41d4aab8bf457a8d6dd2a4acf985cd"></a>

-   The temporary port cannot meet the current service requirements.
-   The system is abnormal.

## Procedure<a name="sa1c9f6b13332405a9310db22b3df7355"></a>

**Expand the temporary port number range.**

1.  On MRS Manager, click the alarm in the real-time alarm list. In the  **Alarm Details**  area, obtain the IP address of the host for which the alarm is generated.
2.  Use PuTTY to log in to the host for which the alarm is generated as user  **omm**.
3.  Run the  **cat /proc/sys/net/ipv4/ip\_local\_port\_range |cut -f 1**  command to obtain the value of the start port and run the ****cat /proc/sys/net/ipv4/ip\_local\_port\_range**  |cut -f 2**  command to obtain the value of the end port. The total number of temporary ports is the value of the end port minus the value of the start port. If the total number of temporary ports is smaller than 28,232, the random port range of the OS is narrow. Contact the system administrator to increase the port range.
4.  Run the  **ss -ant 2\>/dev/null | grep -v LISTEN | awk 'NR \> 2 \{print $4\}'|cut -d ':' -f 2 | awk '$1 \>"**_Value of the start port_**" \{print $1\}' | sort -u | wc -l**  command to calculate the number of used temporary ports.
5.  The formula for calculating the usage of the temporary ports is: Usage of the temporary ports = \(Number of used temporary ports/Total number of temporary ports\) x 100%. Check whether the temporary port usage exceeds the threshold..
    -   If yes, go to  [7](#l78ae2f9436d64bcb947fa48599b6d33a).
    -   If no, go to  [6](#lfc71b64a61ba4231843fd0d9f73b6066).

6.  <a name="lfc71b64a61ba4231843fd0d9f73b6066"></a>Wait 5 minutes and check whether the alarm is cleared.
    -   If yes, no further action is required.
    -   If no, go to  [7](#l78ae2f9436d64bcb947fa48599b6d33a).


**Check whether the system environment is abnormal.**

1.  <a name="l78ae2f9436d64bcb947fa48599b6d33a"></a>Run the following command to import the temporary file and view the frequently used ports in the  **port\_result.txt file**:

    **netstat -tnp \> $BIGDATA\_HOME/tmp/port\_result.txt**

    ```
    netstat -tnp 
    
    Active Internet connections (w/o servers)
    
    Proto Recv Send LocalAddress ForeignAddress State PID/ProgramName tcp   0   0 10-120-85-154:45433  10-120-8:25009 CLOSE_WAIT 94237/java 
    tcp   0   0 10-120-85-154:45434  10-120-8:25009 CLOSE_WAIT 94237/java 
    tcp   0   0 10-120-85-154:45435  10-120-8:25009 CLOSE_WAIT 94237/java 
    ...
    ```

2.  Run the following command to view the processes that occupy a large number of ports:

    **ps -ef |grep** _PID_

    >![](/images/icon-note.gif) **NOTE:**   
    >-   PID is the processes ID queried in  [7](#l78ae2f9436d64bcb947fa48599b6d33a).  
    >-   Run the following command to collect information about all processes and check the processes that occupy a large number of ports:  
    >    **ps -ef \> $BIGDATA\_HOME/tmp/ps\_result.txt**  

3.  After obtaining the administrator's approval, clear the processes that occupy a large number of ports. Wait 5 minutes and check whether the alarm is cleared.
    -   If yes, no further action is required.
    -   If no, go to  [11](#l5c54471d266c4c9799718566186577e4).


**Collect fault information.**

1.  On MRS Manager, choose  **System** \> **Export Log**.
2.  <a name="l5c54471d266c4c9799718566186577e4"></a>Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).

## Related Information<a name="s0f3de21960c241e08f9ebe8455ba125f"></a>

N/A


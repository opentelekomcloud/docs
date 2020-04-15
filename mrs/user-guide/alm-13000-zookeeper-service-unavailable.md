# ALM-13000 ZooKeeper Service Unavailable<a name="EN-US_TOPIC_0125375978"></a>

## Description<a name="s7a26bdca38044c66b7c3a987535fb7f9"></a>

The system checks the ZooKeeper service status every 30 seconds. This alarm is generated when the ZooKeeper service is unavailable and is cleared when the ZooKeeper service recovers.

## Attribute<a name="s525b2a9e771b47a096948c33e6a0495a"></a>

<a name="en-us_topic_0035998717_table11808928"></a>
<table><thead align="left"><tr id="en-us_topic_0035998717_row63404869"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="en-us_topic_0035998717_p35520730"><a name="en-us_topic_0035998717_p35520730"></a><a name="en-us_topic_0035998717_p35520730"></a><strong id="ab7d139e5054246788a88581bfa705671"><a name="ab7d139e5054246788a88581bfa705671"></a><a name="ab7d139e5054246788a88581bfa705671"></a>Alarm ID</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="en-us_topic_0035998717_p58606859"><a name="en-us_topic_0035998717_p58606859"></a><a name="en-us_topic_0035998717_p58606859"></a><strong id="a8b7bbf33e85f419081552a11b0b87c27"><a name="a8b7bbf33e85f419081552a11b0b87c27"></a><a name="a8b7bbf33e85f419081552a11b0b87c27"></a>Alarm Severity</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="en-us_topic_0035998717_p49535170"><a name="en-us_topic_0035998717_p49535170"></a><a name="en-us_topic_0035998717_p49535170"></a><strong id="a320530552a084bac9d022c95b5d3c297"><a name="a320530552a084bac9d022c95b5d3c297"></a><a name="a320530552a084bac9d022c95b5d3c297"></a>Automatically Cleared</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998717_row52925796"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0035998717_p59131099"><a name="en-us_topic_0035998717_p59131099"></a><a name="en-us_topic_0035998717_p59131099"></a>13000</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0035998717_p24889743"><a name="en-us_topic_0035998717_p24889743"></a><a name="en-us_topic_0035998717_p24889743"></a>Critical</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0035998717_p2803303"><a name="en-us_topic_0035998717_p2803303"></a><a name="en-us_topic_0035998717_p2803303"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="en-us_topic_0035998717_section588929"></a>

<a name="en-us_topic_0035998717_table25741004"></a>
<table><thead align="left"><tr id="en-us_topic_0035998717_row31903028"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0035998717_p34008447"><a name="en-us_topic_0035998717_p34008447"></a><a name="en-us_topic_0035998717_p34008447"></a><strong id="a28de78d8906e417da340999f9f6992e0"><a name="a28de78d8906e417da340999f9f6992e0"></a><a name="a28de78d8906e417da340999f9f6992e0"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="en-us_topic_0035998717_p3220827"><a name="en-us_topic_0035998717_p3220827"></a><a name="en-us_topic_0035998717_p3220827"></a><strong id="en-us_topic_0035998717_b49755125041"><a name="en-us_topic_0035998717_b49755125041"></a><a name="en-us_topic_0035998717_b49755125041"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0035998717_row59560431"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998717_p59665636"><a name="en-us_topic_0035998717_p59665636"></a><a name="en-us_topic_0035998717_p59665636"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998717_p1078370"><a name="en-us_topic_0035998717_p1078370"></a><a name="en-us_topic_0035998717_p1078370"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998717_row9705331"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998717_p47934352"><a name="en-us_topic_0035998717_p47934352"></a><a name="en-us_topic_0035998717_p47934352"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998717_p57477322"><a name="en-us_topic_0035998717_p57477322"></a><a name="en-us_topic_0035998717_p57477322"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="en-us_topic_0035998717_row47533853"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="en-us_topic_0035998717_p25036876"><a name="en-us_topic_0035998717_p25036876"></a><a name="en-us_topic_0035998717_p25036876"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035998717_p14721100"><a name="en-us_topic_0035998717_p14721100"></a><a name="en-us_topic_0035998717_p14721100"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s16d87df03de74deba6023be4b52be979"></a>

-   ZooKeeper fails to provide coordination services for upper-layer components.
-   Components dependent on ZooKeeper may not run properly.

## Possible Causes<a name="s7cb7c874445245f09aca5acdd6bed3bf"></a>

-   A ZooKeeper instance is abnormal.
-   The disk capacity is insufficient.
-   The network is faulty.
-   The DNS is installed on the ZooKeeper node.

## Procedure<a name="s45192bfd7eab4e20a51dbcd629656a88"></a>

**Check the ZooKeeper service instance status.**

1.  On MRS Manager, choose  **Service**  \>  **ZooKeeper**  \>  **quorumpeer**.
2.  Check whether the ZooKeeper instances are normal.
    -   If yes, go to  [6](#lcd2f7e62528940c987a36b09bf129b38).
    -   If no, go to  [3](#lc8c9b3393366466cb65b77c21ade4585).

3.  <a name="lc8c9b3393366466cb65b77c21ade4585"></a>Select instances whose status is not good and choose  **More**  \>  **Restart Instance**.
4.  Check whether the instance status is good after restart.
    -   If yes, go to  [5](#lcebbcb41c0bf440dbe7f9d204e301820).
    -   If no, go to  [19](#l18ef2941c5af45cbac6e5065a70f6826).

5.  <a name="lcebbcb41c0bf440dbe7f9d204e301820"></a>On the  **Alarm**  tab, check whether the alarm is cleared.

    -   If yes, no further action is required.
    -   If no, go to  [6](#lcd2f7e62528940c987a36b09bf129b38).

    **Check the disk status.**

6.  <a name="lcd2f7e62528940c987a36b09bf129b38"></a>On MRS Manager, choose  **Service**  \>  **ZooKeeper**  \>  **quorumpeer**, and check the host information of the ZooKeeper instance on each node.
7.  On MRS Manager, click  **Host**.
8.  In the  **Disk Usage**  column, check whether the disk space of each node that contains ZooKeeper instances is insufficient \(where disk usage exceeds 80%\).
    -   If yes, go to  [9](#l55d1644c0c7943bdbf2adf5b1f67095f).
    -   If no, go to  [11](#lec42172498f64aa394387278e79a1cf1).

9.  <a name="l55d1644c0c7943bdbf2adf5b1f67095f"></a>Expand disk capacity. For details, see  [ALM-12017 Insufficient Disk Capacity](alm-12017-insufficient-disk-capacity.md).
10. On the  **Alarm**  tab, check whether the alarm is cleared.

    -   If yes, no further action is required.
    -   If no, go to  [11](#lec42172498f64aa394387278e79a1cf1).

    **Check the network status.**

11. <a name="lec42172498f64aa394387278e79a1cf1"></a>On the Linux node that contains the ZooKeeper instance, run the  **ping**  command to check whether the host names of other nodes that contain the ZooKeeper instance can be pinged successfully.
    -   If yes, go to  [15](#lc953b6e3734649cca407bdae0eb7457e).
    -   If no, go to  [12](#l78bda6803a444bd7988f2c6f946c2734).

12. <a name="l78bda6803a444bd7988f2c6f946c2734"></a>Modify the IP addresses in  **/etc/hosts**  and add the host name and IP address mapping.
13. Run the  **ping**  command again to check whether the host names of other nodes that contain the ZooKeeper instance can be pinged successfully.
    -   If yes, go to  [14](#l8dd5143571354289afac5287c828b03a).
    -   If no, go to  [19](#l18ef2941c5af45cbac6e5065a70f6826).

14. <a name="l8dd5143571354289afac5287c828b03a"></a>On the  **Alarm**  tab, check whether the alarm is cleared.

    -   If yes, no further action is required.
    -   If no, go to  [15](#lc953b6e3734649cca407bdae0eb7457e).

    **Check the DNS.**

15. <a name="lc953b6e3734649cca407bdae0eb7457e"></a>Check whether the DNS is installed on the node that contains the ZooKeeper instance. On the Linux node that contains the ZooKeeper instance, run the  **cat /etc/resolv.conf**  command to check whether the file is empty.
    -   If yes, go to  [16](#lc4aa5cd027e9444c99a7780659c3a9d6).
    -   If no, go to  [19](#l18ef2941c5af45cbac6e5065a70f6826).

16. <a name="lc4aa5cd027e9444c99a7780659c3a9d6"></a>Run the  **service named status**  command to check whether the DNS is started.
    -   If yes, go to  [17](#l4b862c39539f4af19cc75b731a25b3da).
    -   No, go to  [19](#l18ef2941c5af45cbac6e5065a70f6826).

17. <a name="l4b862c39539f4af19cc75b731a25b3da"></a>Run the  **service named stop**  command to stop the DNS service. If "Shutting down name server BIND waiting for named to shut down \(28s\)" is displayed, the DNS service is stopped successfully. Comment out any content in  **/etc/resolv.conf**.
18. On the  **Alarm**  tab, check whether the alarm is cleared.
    -   If yes, no further action is required.
    -   If no, go to  [19](#l18ef2941c5af45cbac6e5065a70f6826).

19. <a name="l18ef2941c5af45cbac6e5065a70f6826"></a>Collect fault information.
    1.  On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## Related Information<a name="s9f4070eafb864ca9ada34932212e9bf4"></a>

N/A


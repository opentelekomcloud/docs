# Configuring Redis-Specific Parameters<a name="EN-US_TOPIC_0237964718"></a>

On the DCS console, you can configure Redis-specific parameters to keep DCS instances performing optimally.

>![](/images/icon-note.gif) **NOTE:**   
>The default values are already optimized for typical use cases. Reconfiguring parameters is recommended only when necessary.  

## Prerequisites<a name="section45399024"></a>

The DCS instance you want to configure is in the  **Running**  state, and the instance type is single-node or master/standby \(Redis parameters of DCS instances in cluster mode are not modifiable\).

## Procedure<a name="section5938035"></a>

1.  Log in to the management console.
2.  Click![](figures/icon-region.png)  in the upper left corner of the management console and select a region and a project.
3.  Click  **Service List**, and choose  **Database**  \>  **Distributed Cache Service**  to launch the DCS console.
4.  In the navigation pane, choose  **Cache Manager**.
5.  On the  **Cache Manager**  page, click the name of the DCS instance you want to configure.

    A page with details of the DCS instance is displayed.

6.  On the instance details page, click the  **Parameters**  tab.
7.  On the  **Parameters**  tab page, click  **Modify**.
8.  Modify Redis-specific parameters based on your requirements.

    **Table  1**  Redis-specific parameters

    <a name="table53748798"></a>
    <table><thead align="left"><tr id="row66476022"><th class="cellrowborder" valign="top" width="12%" id="mcps1.2.5.1.1"><p id="p15848707"><a name="p15848707"></a><a name="p15848707"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="43%" id="mcps1.2.5.1.2"><p id="p8676909"><a name="p8676909"></a><a name="p8676909"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="31%" id="mcps1.2.5.1.3"><p id="p31741019"><a name="p31741019"></a><a name="p31741019"></a>Possible Values</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.4"><p id="p20885750"><a name="p20885750"></a><a name="p20885750"></a>Default Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row14024165"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.1 "><p id="p62215569"><a name="p62215569"></a><a name="p62215569"></a>maxmemory-policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.5.1.2 "><p id="p6296289"><a name="p6296289"></a><a name="p6296289"></a>How DCS will select what to remove when maxmemory is reached.</p>
    <p id="p56666602"><a name="p56666602"></a><a name="p56666602"></a>For more information about this parameter, see <a href="what-is-the-default-data-eviction-policy.md">What Is the Default Data Eviction Policy?</a></p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.5.1.3 "><p id="p38001806"><a name="p38001806"></a><a name="p38001806"></a>volatile-lru</p>
    <p id="p6471942"><a name="p6471942"></a><a name="p6471942"></a>allkeys-lru</p>
    <p id="p58247484"><a name="p58247484"></a><a name="p58247484"></a>volatile-random</p>
    <p id="p54465313"><a name="p54465313"></a><a name="p54465313"></a>allkeys-random</p>
    <p id="p20425774"><a name="p20425774"></a><a name="p20425774"></a>volatile-ttl</p>
    <p id="p49614245"><a name="p49614245"></a><a name="p49614245"></a>noeviction</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.4 "><p id="p59330872"><a name="p59330872"></a><a name="p59330872"></a>noeviction</p>
    </td>
    </tr>
    <tr id="row64215808"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.1 "><p id="p34097968"><a name="p34097968"></a><a name="p34097968"></a>hash-max-ziplist-entries</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.5.1.2 "><p id="p10472004"><a name="p10472004"></a><a name="p10472004"></a>When the number of entries in hashes is less than the value of this parameter, hashes are encoded using a memory efficient data structure.</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.5.1.3 "><p id="p42925989"><a name="p42925989"></a><a name="p42925989"></a>1 to 10000</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.4 "><p id="p54453050"><a name="p54453050"></a><a name="p54453050"></a>512</p>
    </td>
    </tr>
    <tr id="row20315403"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.1 "><p id="p34934986"><a name="p34934986"></a><a name="p34934986"></a>hash-max-ziplist-value</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.5.1.2 "><p id="p11161650"><a name="p11161650"></a><a name="p11161650"></a>When the biggest entry in hashes does not exceed the length threshold indicated by this parameter, hashes are encoded using a memory efficient data structure.</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.5.1.3 "><p id="p31678442"><a name="p31678442"></a><a name="p31678442"></a>1 to 10000</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.4 "><p id="p15816986"><a name="p15816986"></a><a name="p15816986"></a>64</p>
    </td>
    </tr>
    <tr id="row8135151"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.1 "><p id="p54967495"><a name="p54967495"></a><a name="p54967495"></a>list-max-ziplist-entries</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.5.1.2 "><p id="p23182124"><a name="p23182124"></a><a name="p23182124"></a>When the number of entries in lists is less than the value of this parameter, lists are encoded using a memory efficient data structure.</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.5.1.3 "><p id="p65812741"><a name="p65812741"></a><a name="p65812741"></a>1 to 10000</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.4 "><p id="p29231803"><a name="p29231803"></a><a name="p29231803"></a>512</p>
    </td>
    </tr>
    <tr id="row61759636"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.1 "><p id="p36474591"><a name="p36474591"></a><a name="p36474591"></a>list-max-ziplist-value</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.5.1.2 "><p id="p1651899"><a name="p1651899"></a><a name="p1651899"></a>When the biggest entry in lists does not exceed the length threshold indicated by this parameter, lists are encoded using a memory efficient data structure.</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.5.1.3 "><p id="p66694991"><a name="p66694991"></a><a name="p66694991"></a>1 to 10000</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.4 "><p id="p33585220"><a name="p33585220"></a><a name="p33585220"></a>64</p>
    </td>
    </tr>
    <tr id="row33831530"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.1 "><p id="p55999443"><a name="p55999443"></a><a name="p55999443"></a>set-max-intset-entries</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.5.1.2 "><p id="p39661040"><a name="p39661040"></a><a name="p39661040"></a>When a set is composed entirely of strings that happen to be integers in radix 10 in the range of 64 bit signed integers, sets are encoded using a memory efficient data structure.</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.5.1.3 "><p id="p58427690"><a name="p58427690"></a><a name="p58427690"></a>1 to 10000</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.4 "><p id="p35022440"><a name="p35022440"></a><a name="p35022440"></a>512</p>
    </td>
    </tr>
    <tr id="row46766508"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.1 "><p id="p29990828"><a name="p29990828"></a><a name="p29990828"></a>zset-max-ziplist-entries</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.5.1.2 "><p id="p13338021"><a name="p13338021"></a><a name="p13338021"></a>When the number of entries in sorted sets is less than the value of this parameter, sorted sets are encoded using a memory efficient data structure.</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.5.1.3 "><p id="p6637886"><a name="p6637886"></a><a name="p6637886"></a>1 to 10000</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.4 "><p id="p797855"><a name="p797855"></a><a name="p797855"></a>128</p>
    </td>
    </tr>
    <tr id="row7180698"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.1 "><p id="p44765691"><a name="p44765691"></a><a name="p44765691"></a>zset-max-ziplist-value</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.5.1.2 "><p id="p2142393"><a name="p2142393"></a><a name="p2142393"></a>When the biggest entry in sorted sets does not exceed the length threshold indicated by this parameter, sorted sets are encoded using a memory efficient data structure.</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.5.1.3 "><p id="p39316155"><a name="p39316155"></a><a name="p39316155"></a>1 to 10000</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.4 "><p id="p30492010"><a name="p30492010"></a><a name="p30492010"></a>64</p>
    </td>
    </tr>
    <tr id="row5992637"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.1 "><p id="p15641626"><a name="p15641626"></a><a name="p15641626"></a>latency-monitor-threshold</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.5.1.2 "><p id="p59012183"><a name="p59012183"></a><a name="p59012183"></a>Only events that run in more time than the configured latency-monitor-threshold will be logged as latency spikes.</p>
    <a name="ul61347601"></a><a name="ul61347601"></a><ul id="ul61347601"><li>If the latency-monitor-threshold is set to 0, latency monitoring is disabled.</li><li>If the latency-monitor-threshold is set to a value greater than 0, all events blocking the server for a time equal to or greater than the configured latency-monitor-threshold will be logged.</li></ul>
    <p id="p27898002"><a name="p27898002"></a><a name="p27898002"></a>By running the LATENCY command, you can perform operations related to latency monitoring, such as enabling latency monitoring, reporting the latest latency events logged, and obtaining statistical data.</p>
    <p id="p49755431"><a name="p49755431"></a><a name="p49755431"></a>For more information about the latency-monitor-threshold, visit <a href="https://redis.io/topics/latency-monitor" target="_blank" rel="noopener noreferrer">https://redis.io/topics/latency-monitor</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.5.1.3 "><p id="p32922799"><a name="p32922799"></a><a name="p32922799"></a>0 to 86400000 ms</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.4 "><p id="p49501095"><a name="p49501095"></a><a name="p49501095"></a>0</p>
    </td>
    </tr>
    <tr id="row42856673"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.1 "><p id="p48838504"><a name="p48838504"></a><a name="p48838504"></a>reserved-memory</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.5.1.2 "><p id="p63604780"><a name="p63604780"></a><a name="p63604780"></a>The number of megabytes reserved for the backend to perform internal processing such as persistence and master/standby replication.</p>
    <p id="p35572112"><a name="p35572112"></a><a name="p35572112"></a>This parameter is configurable only for master/standby instances.</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.5.1.3 "><p id="p62768825"><a name="p62768825"></a><a name="p62768825"></a>0% to 50% of maximum memory space initially available to the instance and below the current free memory space</p>
    <p id="p28048521"><a name="p28048521"></a><a name="p28048521"></a>NOTE: For more information about maximum available memory of each instance type, see <a href="dcs-instance-specifications.md#table2822601515717">Table 1</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.4 "><p id="p46277382"><a name="p46277382"></a><a name="p46277382"></a>0</p>
    </td>
    </tr>
    <tr id="row13843256"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.1 "><p id="p47561922"><a name="p47561922"></a><a name="p47561922"></a>timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.5.1.2 "><p id="p27310456"><a name="p27310456"></a><a name="p27310456"></a>Connection between the client and server (DCS instance) will be closed if the client is idle for the timeout period (measured in seconds). A timeout period of 0 seconds indicates that the timeout function is disabled.</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.5.1.3 "><p id="p64663364"><a name="p64663364"></a><a name="p64663364"></a>0 to 7200 seconds</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.4 "><p id="p3241099"><a name="p3241099"></a><a name="p3241099"></a>0</p>
    </td>
    </tr>
    <tr id="row29169897"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.1 "><p id="p13951479"><a name="p13951479"></a><a name="p13951479"></a>notify-keyspace-events</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.5.1.2 "><p id="p56327989"><a name="p56327989"></a><a name="p56327989"></a>Keyspace event notification. If this parameter is configured, the Redis Sub/Pub feature will allow clients to receive an event when a Redis data set is modified.</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.5.1.3 "><p id="p66273227"><a name="p66273227"></a><a name="p66273227"></a>If the parameter value is an empty character string, keyspace event notification is disabled.</p>
    <p id="p59588135"><a name="p59588135"></a><a name="p59588135"></a>If the parameter value is a string of multiple characters, keyspace event notification is enabled and each character identifies a class of keyspace events for which Redis will send notifications.</p>
    <div class="note" id="note66531170"><a name="note66531170"></a><a name="note66531170"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul61909621"></a><a name="ul61909621"></a><ul id="ul61909621"><li>The parameter value must contain either K or E.</li><li>A is an alias for "g$lshzxe"and cannot be used together with any of the characters "g$lshzxe".</li><li>For example, the value Kl means that Redis will notify Pub/Sub clients about keyspace events and list commands. The value AKE means Redis will notify Pub/Sub clients about all events.</li></ul>
    </div></div>
    <p id="p46181951"><a name="p46181951"></a><a name="p46181951"></a>K: Keyspace events, published with the __keyspace@__ prefix</p>
    <p id="p12984378"><a name="p12984378"></a><a name="p12984378"></a>E: Keyevent events, published with __keyevent@__ prefix</p>
    <p id="p49750539"><a name="p49750539"></a><a name="p49750539"></a>g: Generic commands (non-type specific) such as DEL, EXPIRE, and RENAME</p>
    <p id="p45101667"><a name="p45101667"></a><a name="p45101667"></a>$: String commands</p>
    <p id="p3261819"><a name="p3261819"></a><a name="p3261819"></a>l: List commands</p>
    <p id="p29356372"><a name="p29356372"></a><a name="p29356372"></a>s: Set commands</p>
    <p id="p62880759"><a name="p62880759"></a><a name="p62880759"></a>h: Hash commands</p>
    <p id="p29055926"><a name="p29055926"></a><a name="p29055926"></a>z: Sorted set commands</p>
    <p id="p60176744"><a name="p60176744"></a><a name="p60176744"></a>x: Expired events (events generated every time a key expires)</p>
    <p id="p4719792"><a name="p4719792"></a><a name="p4719792"></a>e: Evicted events (events generated when a key is evicted for maxmemory)</p>
    <p id="p42478134"><a name="p42478134"></a><a name="p42478134"></a>A: Alias for "g$lshzxe", so that the "AKE" string means all the events.</p>
    <p id="p46758891"><a name="p46758891"></a><a name="p46758891"></a>Note that the parameter value must contain either K or E.</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.4 "><p id="p29373839"><a name="p29373839"></a><a name="p29373839"></a>""</p>
    </td>
    </tr>
    </tbody>
    </table>

    >![](/images/icon-note.gif) **NOTE:**   
    >-   For more information about Redis-specific parameters, visit  [https://redis.io/topics/memory-optimization](https://redis.io/topics/memory-optimization).  
    >-   The latency-monitor-threshold parameter is usually used for fault location. After locating faults based on the latency information collected, change the value of  **latency-monitor-threshold**  to  **0**  to avoid unnecessary latency.  

9.  After you have finished setting parameters, click  **Save**.
10. Click  **OK**  to confirm.


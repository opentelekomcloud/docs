# Configuring Redis-Specific Parameters<a name="en-us_topic_0054235814"></a>

On the DCS console, you can configure Redis-specific parameters to keep DCS instances performing optimally.

>![](public_sys-resources/icon-note.gif) **NOTE:** 
>The default values are already optimized for typical use cases. Reconfiguring parameters is recommended only when necessary.

## Prerequisites<a name="section18805185243013"></a>

The DCS instance you want to configure is in the  **Running**  state, and the instance type is single-node or master/standby \(Redis parameters of DCS instances in Proxy Cluster mode are not modifiable\).

## Procedure<a name="section55365254"></a>

1.  Log in to the management console.
2.  Click  ![](figures/project.png) in the upper left corner of the management console and select a region and a project.
3.  Click  **Service List**, and choose **Database** \> **Distributed Cache Service**  to launch the DCS console.
4.  In the navigation pane, choose  **Cache Manager**.
5.  On the  **Cache Manager**  page, click the name of the DCS instance you want to configure.

    A page with details of the DCS instance is displayed.

6.  On the instance details page, click the  **Parameters**  tab.
7.  On the  **Parameters** tab page, click **Modify**.
8.  Modify Redis-specific parameters based on your requirements.

    >![](public_sys-resources/icon-note.gif) **NOTE:** 
    >The Redis parameters supported by single-node and master/standby instances are different. The following parameters are only supported by master/standby instances, but are not supported by single-node instances:
    >-   appendfsync
    >-   appendonly
    >-   repl-backlog-size
    >-   repl-backlog-ttl

    **Table  1**  Redis-specific parameters

    <a name="table112231941155916"></a>
    <table><thead align="left"><tr id="row821213415598"><th class="cellrowborder" valign="top" width="12%" id="mcps1.2.5.1.1"><p id="p12212441195915"><a name="p12212441195915"></a><a name="p12212441195915"></a><strong id="b5212641115915"><a name="b5212641115915"></a><a name="b5212641115915"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="43%" id="mcps1.2.5.1.2"><p id="p1121216414590"><a name="p1121216414590"></a><a name="p1121216414590"></a><strong id="b20212341125917"><a name="b20212341125917"></a><a name="b20212341125917"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="31%" id="mcps1.2.5.1.3"><p id="p17212114119596"><a name="p17212114119596"></a><a name="p17212114119596"></a><strong id="b14212141175913"><a name="b14212141175913"></a><a name="b14212141175913"></a>Possible Values</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.4"><p id="p1212104120598"><a name="p1212104120598"></a><a name="p1212104120598"></a><strong id="b521204113591"><a name="b521204113591"></a><a name="b521204113591"></a>Default Value</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row32141341135916"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.1 "><p id="p162131241125912"><a name="p162131241125912"></a><a name="p162131241125912"></a>appendfsync</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.5.1.2 "><p id="p9213841195915"><a name="p9213841195915"></a><a name="p9213841195915"></a>Controls how often fsync() transfers cached data to the disk. Note that some OSs will perform a complete data transfer but some others only make a "best-effort" attempt.</p>
    <p id="p172131141155913"><a name="p172131141155913"></a><a name="p172131141155913"></a>There are three settings:</p>
    <p id="p621314145918"><a name="p621314145918"></a><a name="p621314145918"></a>no: fsync() is never called. The OS will flush data when it is ready. This mode offers the highest performance.</p>
    <p id="p221311414597"><a name="p221311414597"></a><a name="p221311414597"></a>always: fsync() is called after every write to the AOF. This mode is very slow, but also very safe.</p>
    <p id="p1521384117594"><a name="p1521384117594"></a><a name="p1521384117594"></a>everysec: fsync() is called once per second. This mode provides a compromise between safety and performance.</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.5.1.3 "><a name="ul721334145919"></a><a name="ul721334145919"></a><ul id="ul721334145919"><li>no</li><li>always</li><li>everysec</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.4 "><p id="p2213114119595"><a name="p2213114119595"></a><a name="p2213114119595"></a>everysec</p>
    </td>
    </tr>
    <tr id="row42141941105911"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.1 "><p id="p1221414410592"><a name="p1221414410592"></a><a name="p1221414410592"></a>repl-backlog-size</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.5.1.2 "><p id="p121404195914"><a name="p121404195914"></a><a name="p121404195914"></a>The replication backlog size (bytes). The backlog is a buffer that accumulates replica data when replicas are disconnected from the master. When a replica reconnects, a partial synchronization is performed to synchronize the data that was missed while replicas were disconnected.</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.5.1.3 "><p id="p4214194185911"><a name="p4214194185911"></a><a name="p4214194185911"></a>16,384–1,073,741,824</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.4 "><p id="p92149417591"><a name="p92149417591"></a><a name="p92149417591"></a>1,048,576</p>
    </td>
    </tr>
    <tr id="row321554116595"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.1 "><p id="p19214164120595"><a name="p19214164120595"></a><a name="p19214164120595"></a>repl-backlog-ttl</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.5.1.2 "><p id="p721474115911"><a name="p721474115911"></a><a name="p721474115911"></a>The amount of time, in seconds, before the backlog buffer is released, starting from the last a replica was disconnected. The value <strong id="b1121414119596"><a name="b1121414119596"></a><a name="b1121414119596"></a>0</strong> indicates that the backlog is never released.</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.5.1.3 "><p id="p32143410591"><a name="p32143410591"></a><a name="p32143410591"></a>0–604,800</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.4 "><p id="p18214441185910"><a name="p18214441185910"></a><a name="p18214441185910"></a>3,600</p>
    </td>
    </tr>
    <tr id="row12216104185918"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.1 "><p id="p162151941185914"><a name="p162151941185914"></a><a name="p162151941185914"></a>appendonly</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.5.1.2 "><p id="p32155414599"><a name="p32155414599"></a><a name="p32155414599"></a>Indicates whether to log each modification of the instance. By default, data is written to disks asynchronously in Redis. If this function is disabled, recently-generated data might be lost in the event of a power failure. Options:</p>
    <p id="p6215941145916"><a name="p6215941145916"></a><a name="p6215941145916"></a>yes: enabled</p>
    <p id="p72151410595"><a name="p72151410595"></a><a name="p72151410595"></a>no: disabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.5.1.3 "><a name="ul1021614110590"></a><a name="ul1021614110590"></a><ul id="ul1021614110590"><li>yes</li><li>no</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.4 "><p id="p621694175915"><a name="p621694175915"></a><a name="p621694175915"></a>yes</p>
    </td>
    </tr>
    <tr id="row821844195916"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.1 "><p id="p12162412598"><a name="p12162412598"></a><a name="p12162412598"></a>maxmemory-policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.5.1.2 "><p id="p19217124118590"><a name="p19217124118590"></a><a name="p19217124118590"></a>How DCS will select what to remove when maxmemory is reached.</p>
    <p id="p1521714416591"><a name="p1521714416591"></a><a name="p1521714416591"></a>For more information about this parameter, see <a href="what-is-the-default-data-eviction-policy.md">What Is the Default Data Eviction Policy?</a></p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.5.1.3 "><p id="p1821717415594"><a name="p1821717415594"></a><a name="p1821717415594"></a>volatile-lru</p>
    <p id="p1521734195917"><a name="p1521734195917"></a><a name="p1521734195917"></a>allkeys-lru</p>
    <p id="p12217144185913"><a name="p12217144185913"></a><a name="p12217144185913"></a>volatile-random</p>
    <p id="p321715419590"><a name="p321715419590"></a><a name="p321715419590"></a>allkeys-random</p>
    <p id="p17217124119594"><a name="p17217124119594"></a><a name="p17217124119594"></a>volatile-ttl</p>
    <p id="p15217104113597"><a name="p15217104113597"></a><a name="p15217104113597"></a>noeviction</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.4 "><p id="p11218141105917"><a name="p11218141105917"></a><a name="p11218141105917"></a>noeviction</p>
    </td>
    </tr>
    <tr id="row2219241155912"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.1 "><p id="p92180418594"><a name="p92180418594"></a><a name="p92180418594"></a>hash-max-ziplist-entries</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.5.1.2 "><p id="p12181341165916"><a name="p12181341165916"></a><a name="p12181341165916"></a>When the number of entries in hashes is less than the value of this parameter, hashes are encoded using a memory efficient data structure.</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.5.1.3 "><p id="p2218144118598"><a name="p2218144118598"></a><a name="p2218144118598"></a>1 to 10000</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.4 "><p id="p1221817411599"><a name="p1221817411599"></a><a name="p1221817411599"></a>512</p>
    </td>
    </tr>
    <tr id="row82191641125914"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.1 "><p id="p10219144165920"><a name="p10219144165920"></a><a name="p10219144165920"></a>hash-max-ziplist-value</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.5.1.2 "><p id="p221974115591"><a name="p221974115591"></a><a name="p221974115591"></a>When the biggest entry in hashes does not exceed the length threshold indicated by this parameter, hashes are encoded using a memory efficient data structure.</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.5.1.3 "><p id="p72197411597"><a name="p72197411597"></a><a name="p72197411597"></a>1 to 10000</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.4 "><p id="p5219114120599"><a name="p5219114120599"></a><a name="p5219114120599"></a>64</p>
    </td>
    </tr>
    <tr id="row182191841135914"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.1 "><p id="p16219441145914"><a name="p16219441145914"></a><a name="p16219441145914"></a>list-max-ziplist-entries</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.5.1.2 "><p id="p162199419593"><a name="p162199419593"></a><a name="p162199419593"></a>When the number of entries in lists is less than the value of this parameter, lists are encoded using a memory efficient data structure.</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.5.1.3 "><p id="p19219194118598"><a name="p19219194118598"></a><a name="p19219194118598"></a>1 to 10000</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.4 "><p id="p8219041145911"><a name="p8219041145911"></a><a name="p8219041145911"></a>512</p>
    </td>
    </tr>
    <tr id="row1821944115598"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.1 "><p id="p721920412599"><a name="p721920412599"></a><a name="p721920412599"></a>list-max-ziplist-value</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.5.1.2 "><p id="p421915412590"><a name="p421915412590"></a><a name="p421915412590"></a>When the biggest entry in lists does not exceed the length threshold indicated by this parameter, lists are encoded using a memory efficient data structure.</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.5.1.3 "><p id="p182191541105912"><a name="p182191541105912"></a><a name="p182191541105912"></a>1 to 10000</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.4 "><p id="p7219144114597"><a name="p7219144114597"></a><a name="p7219144114597"></a>64</p>
    </td>
    </tr>
    <tr id="row10220154155911"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.1 "><p id="p72191141115919"><a name="p72191141115919"></a><a name="p72191141115919"></a>set-max-intset-entries</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.5.1.2 "><p id="p021917410590"><a name="p021917410590"></a><a name="p021917410590"></a>When a set is composed entirely of strings that happen to be integers in radix 10 in the range of 64 bit signed integers, sets are encoded using a memory efficient data structure.</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.5.1.3 "><p id="p19220241105911"><a name="p19220241105911"></a><a name="p19220241105911"></a>1 to 10000</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.4 "><p id="p162204415594"><a name="p162204415594"></a><a name="p162204415594"></a>512</p>
    </td>
    </tr>
    <tr id="row722016410592"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.1 "><p id="p3220194114595"><a name="p3220194114595"></a><a name="p3220194114595"></a>zset-max-ziplist-entries</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.5.1.2 "><p id="p4220154165912"><a name="p4220154165912"></a><a name="p4220154165912"></a>When the number of entries in sorted sets is less than the value of this parameter, sorted sets are encoded using a memory efficient data structure.</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.5.1.3 "><p id="p8220184135914"><a name="p8220184135914"></a><a name="p8220184135914"></a>1 to 10000</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.4 "><p id="p12220241145913"><a name="p12220241145913"></a><a name="p12220241145913"></a>128</p>
    </td>
    </tr>
    <tr id="row10220124135913"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.1 "><p id="p922017419593"><a name="p922017419593"></a><a name="p922017419593"></a>zset-max-ziplist-value</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.5.1.2 "><p id="p16220841125918"><a name="p16220841125918"></a><a name="p16220841125918"></a>When the biggest entry in sorted sets does not exceed the length threshold indicated by this parameter, sorted sets are encoded using a memory efficient data structure.</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.5.1.3 "><p id="p19220194125919"><a name="p19220194125919"></a><a name="p19220194125919"></a>1 to 10000</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.4 "><p id="p1722012414597"><a name="p1722012414597"></a><a name="p1722012414597"></a>64</p>
    </td>
    </tr>
    <tr id="row62211841155913"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.1 "><p id="p2220164175913"><a name="p2220164175913"></a><a name="p2220164175913"></a>latency-monitor-threshold</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.5.1.2 "><p id="p1122094115918"><a name="p1122094115918"></a><a name="p1122094115918"></a>Only events that run in more time than the configured latency-monitor-threshold will be logged as latency spikes.</p>
    <a name="ul162201241165910"></a><a name="ul162201241165910"></a><ul id="ul162201241165910"><li>If the latency-monitor-threshold is set to 0, latency monitoring is disabled.</li><li>If the latency-monitor-threshold is set to a value greater than 0, all events blocking the server for a time equal to or greater than the configured latency-monitor-threshold will be logged.</li></ul>
    <p id="p1422174125919"><a name="p1422174125919"></a><a name="p1422174125919"></a>By running the LATENCY command, you can perform operations related to latency monitoring, such as enabling latency monitoring, reporting the latest latency events logged, and obtaining statistical data.</p>
    <p id="p1822174125910"><a name="p1822174125910"></a><a name="p1822174125910"></a>For more information about the latency-monitor-threshold, visit <a href="https://redis.io/topics/latency-monitor" target="_blank" rel="noopener noreferrer">https://redis.io/topics/latency-monitor</a>.</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.5.1.3 "><p id="p5221174114597"><a name="p5221174114597"></a><a name="p5221174114597"></a>0 to 86400000 ms</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.4 "><p id="p1122144175911"><a name="p1122144175911"></a><a name="p1122144175911"></a>0</p>
    </td>
    </tr>
    <tr id="row622124195915"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.1 "><p id="p0221134155917"><a name="p0221134155917"></a><a name="p0221134155917"></a>reserved-memory-percent</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.5.1.2 "><p id="p4221104195912"><a name="p4221104195912"></a><a name="p4221104195912"></a>Percentage of the maximum available memory reserved for background processes, such as data persistence and replication.</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.5.1.3 "><p id="p2022194111593"><a name="p2022194111593"></a><a name="p2022194111593"></a>0–80</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.4 "><p id="p19221641195919"><a name="p19221641195919"></a><a name="p19221641195919"></a>0</p>
    </td>
    </tr>
    <tr id="row10221941165910"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.1 "><p id="p922134118591"><a name="p922134118591"></a><a name="p922134118591"></a>timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.5.1.2 "><p id="p022124195918"><a name="p022124195918"></a><a name="p022124195918"></a>Connection between the client and server (DCS instance) will be closed if the client is idle for the timeout period (measured in seconds). A timeout period of 0 seconds indicates that the timeout function is disabled.</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.5.1.3 "><p id="p8221144135910"><a name="p8221144135910"></a><a name="p8221144135910"></a>0 to 7200 seconds</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.4 "><p id="p722134125919"><a name="p722134125919"></a><a name="p722134125919"></a>0</p>
    </td>
    </tr>
    <tr id="row8222124105916"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.1 "><p id="p1922117417595"><a name="p1922117417595"></a><a name="p1922117417595"></a>notify-keyspace-events</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.5.1.2 "><p id="p172211141165910"><a name="p172211141165910"></a><a name="p172211141165910"></a>Keyspace event notification. If this parameter is configured, the Redis Sub/Pub feature will allow clients to receive an event when a Redis data set is modified.</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.5.1.3 "><p id="p102217419597"><a name="p102217419597"></a><a name="p102217419597"></a>If the parameter value is an empty character string, keyspace event notification is disabled.</p>
    <p id="p18221941115918"><a name="p18221941115918"></a><a name="p18221941115918"></a>If the parameter value is a string of multiple characters, keyspace event notification is enabled and each character identifies a class of keyspace events for which Redis will send notifications.</p>
    <div class="note" id="note42221341185920"><a name="note42221341185920"></a><a name="note42221341185920"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul622214118596"></a><a name="ul622214118596"></a><ul id="ul622214118596"><li>The parameter value must contain either K or E.</li><li>A is an alias for "g$lshzxe"and cannot be used together with any of the characters "g$lshzxe".</li><li>For example, the value Kl means that Redis will notify Pub/Sub clients about keyspace events and list commands. The value AKE means Redis will notify Pub/Sub clients about all events.</li></ul>
    </div></div>
    <p id="p522217416596"><a name="p522217416596"></a><a name="p522217416596"></a>K: Keyspace events, published with the __keyspace@__ prefix</p>
    <p id="p17222241115912"><a name="p17222241115912"></a><a name="p17222241115912"></a>E: Keyevent events, published with __keyevent@__ prefix</p>
    <p id="p82221241105912"><a name="p82221241105912"></a><a name="p82221241105912"></a>g: Generic commands (non-type specific) such as DEL, EXPIRE, and RENAME</p>
    <p id="p12221841195917"><a name="p12221841195917"></a><a name="p12221841195917"></a>$: String commands</p>
    <p id="p82228414597"><a name="p82228414597"></a><a name="p82228414597"></a>l: List commands</p>
    <p id="p1022219411593"><a name="p1022219411593"></a><a name="p1022219411593"></a>s: Set commands</p>
    <p id="p0222134110591"><a name="p0222134110591"></a><a name="p0222134110591"></a>h: Hash commands</p>
    <p id="p7222114115912"><a name="p7222114115912"></a><a name="p7222114115912"></a>z: Sorted set commands</p>
    <p id="p822274113595"><a name="p822274113595"></a><a name="p822274113595"></a>x: Expired events (events generated every time a key expires)</p>
    <p id="p1122254125914"><a name="p1122254125914"></a><a name="p1122254125914"></a>e: Evicted events (events generated when a key is evicted for maxmemory)</p>
    <p id="p8222184155915"><a name="p8222184155915"></a><a name="p8222184155915"></a>A: Alias for "g$lshzxe", so that the "AKE" string means all the events.</p>
    <p id="p82221841155915"><a name="p82221841155915"></a><a name="p82221841155915"></a>Note that the parameter value must contain either K or E.</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.4 "><p id="p12221541175916"><a name="p12221541175916"></a><a name="p12221541175916"></a>""</p>
    </td>
    </tr>
    <tr id="row722334175911"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.1 "><p id="p222217414595"><a name="p222217414595"></a><a name="p222217414595"></a>slowlog-log-slower-than</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.5.1.2 "><p id="p152231841175911"><a name="p152231841175911"></a><a name="p152231841175911"></a>The maximum amount of time allowed, in microseconds, for command execution. If this threshold is exceeded, Redis Slow Log will record the command.</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.5.1.3 "><p id="p122364125914"><a name="p122364125914"></a><a name="p122364125914"></a>0–1,000,000</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.4 "><p id="p20223174195914"><a name="p20223174195914"></a><a name="p20223174195914"></a>10,000</p>
    </td>
    </tr>
    <tr id="row722324175914"><td class="cellrowborder" valign="top" width="12%" headers="mcps1.2.5.1.1 "><p id="p102231841185912"><a name="p102231841185912"></a><a name="p102231841185912"></a>slowlog-max-len</p>
    </td>
    <td class="cellrowborder" valign="top" width="43%" headers="mcps1.2.5.1.2 "><p id="p1622344155910"><a name="p1622344155910"></a><a name="p1622344155910"></a>The maximum allowed length of the Redis Slow Log logs. Slow Log consumes memory, but you can reclaim this memory by running the SLOWLOG RESET command.</p>
    </td>
    <td class="cellrowborder" valign="top" width="31%" headers="mcps1.2.5.1.3 "><p id="p1022310413590"><a name="p1022310413590"></a><a name="p1022310413590"></a>0–1,000</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.4 "><p id="p822334120593"><a name="p822334120593"></a><a name="p822334120593"></a>128</p>
    </td>
    </tr>
    </tbody>
    </table>

    >![](public_sys-resources/icon-note.gif) **NOTE:** 
    >-   For more information about Redis-specific parameters, visit  [https://redis.io/topics/memory-optimization](https://redis.io/topics/memory-optimization).
    >-   The latency-monitor-threshold parameter is usually used for fault location. After locating faults based on the latency information collected, change the value of  **latency-monitor-threshold** to **0**  to avoid unnecessary latency.

9.  After you have finished setting parameters, click  **Save**.
10. Click  **Yes **to confirm.


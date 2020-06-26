# Introduction to Logs<a name="EN-US_TOPIC_0221415092"></a>

## Log Description<a name="section8415510499"></a>

**Log paths:**

-   Executor run log:  **"$\{BIGDATA\_DATA\_HOME\}/hadoop/data$\{i\}/nm/containerlogs/application\_$\{appid\}/container\_\{$contid\}"**

    >![](/images/icon-note.gif) **NOTE:**   
    >The logs of running tasks are stored in the preceding path. After the running is complete, the system determines whether to aggregate the logs to an HDFS directory based on the Yarn configuration.  

-   Other logs:  **"/var/log/Bigdata/flink/flinkResource"**

**Log archive rules:**

-   Executor log files are stored each time when the size of the log files reaches 50 MB by default. A maximum of 100 log files are retained without being compressed.
-   You can configure the log file size and the number of compressed files to be retained on MRS Manager.

**Table  1**  Flink log list

<a name="table4827184413920"></a>
<table><thead align="left"><tr id="row12866174413911"><th class="cellrowborder" valign="top" width="33.333333333333336%" id="mcps1.2.4.1.1"><p id="p38337129917"><a name="p38337129917"></a><a name="p38337129917"></a><strong id="en-us_topic_0026827806_b5757001183651"><a name="en-us_topic_0026827806_b5757001183651"></a><a name="en-us_topic_0026827806_b5757001183651"></a>Log Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.333333333333336%" id="mcps1.2.4.1.2"><p id="p1083318121914"><a name="p1083318121914"></a><a name="p1083318121914"></a><strong id="b1282183420919"><a name="b1282183420919"></a><a name="b1282183420919"></a>Log File Name</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.333333333333336%" id="mcps1.2.4.1.3"><p id="p083310122917"><a name="p083310122917"></a><a name="p083310122917"></a><strong id="b151793617920"><a name="b151793617920"></a><a name="b151793617920"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1786744410910"><td class="cellrowborder" rowspan="3" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.1 "><p id="p986774415915"><a name="p986774415915"></a><a name="p986774415915"></a>Flink service log</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.2 "><p id="p2086734412916"><a name="p2086734412916"></a><a name="p2086734412916"></a>postinstall.log</p>
</td>
<td class="cellrowborder" valign="top" width="33.333333333333336%" headers="mcps1.2.4.1.3 "><p id="p1867444492"><a name="p1867444492"></a><a name="p1867444492"></a>Service installation log</p>
</td>
</tr>
<tr id="row186712441916"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p2867134418910"><a name="p2867134418910"></a><a name="p2867134418910"></a>prestart.log</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p10867144994"><a name="p10867144994"></a><a name="p10867144994"></a>Log file of the <strong id="b184696111484"><a name="b184696111484"></a><a name="b184696111484"></a>prestart</strong> script</p>
</td>
</tr>
<tr id="row6867194417919"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="p158671744198"><a name="p158671744198"></a><a name="p158671744198"></a>cleanup.log</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="p13867164410915"><a name="p13867164410915"></a><a name="p13867164410915"></a>Cleanup log file for instance installation and uninstallation</p>
</td>
</tr>
</tbody>
</table>

## Log Levels<a name="section19463015192"></a>

[Table 2](#table63318572917)  describes the log levels supported by Flink. The priorities of log levels are ERROR, WARN, INFO, and DEBUG in descending order. Logs whose levels are higher than or equal to the specified level are printed. The number of printed logs decreases as the specified log level increases.

**Table  2**  Log levels

<a name="table63318572917"></a>
<table><thead align="left"><tr id="row12721657892"><th class="cellrowborder" valign="top" width="30%" id="mcps1.2.3.1.1"><p id="p1202134412918"><a name="p1202134412918"></a><a name="p1202134412918"></a><strong id="b842352706145743"><a name="b842352706145743"></a><a name="b842352706145743"></a>Log Level</strong></p>
</th>
<th class="cellrowborder" valign="top" width="70%" id="mcps1.2.3.1.2"><p id="p3202544891"><a name="p3202544891"></a><a name="p3202544891"></a><strong id="b14022601216"><a name="b14022601216"></a><a name="b14022601216"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row107314575911"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p57314576913"><a name="p57314576913"></a><a name="p57314576913"></a>ERROR</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p117385719912"><a name="p117385719912"></a><a name="p117385719912"></a>Logs of this level record error information about the current event processing.</p>
</td>
</tr>
<tr id="row0733571398"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p1731557595"><a name="p1731557595"></a><a name="p1731557595"></a>WARN</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p1273185720917"><a name="p1273185720917"></a><a name="p1273185720917"></a>Logs of this level record error information about the current event processing.</p>
</td>
</tr>
<tr id="row4733571694"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p9737578914"><a name="p9737578914"></a><a name="p9737578914"></a>INFO</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p073155711910"><a name="p073155711910"></a><a name="p073155711910"></a>Logs of this level record normal running status information about the system and events.</p>
</td>
</tr>
<tr id="row177320571996"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.3.1.1 "><p id="p197319571492"><a name="p197319571492"></a><a name="p197319571492"></a>DEBUG</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.2.3.1.2 "><p id="p137345716911"><a name="p137345716911"></a><a name="p137345716911"></a>Logs of this level record the system information and system debugging information.</p>
</td>
</tr>
</tbody>
</table>

To modify log levels, perform the following operations:

1.  On MRS Manager and choose  **Services**  \>  **Flink**  \>  **Service Configuration**.
2.  Set  **Type**  to  **All**.
3.  On the menu bar on the left, select the log menu of the target role.
4.  Select a desired log level.
5.  Click  **Save Configuration**. In the displayed dialog box, click  **OK**  to make configurations take effect.

    >![](/images/icon-note.gif) **NOTE:**   
    >The configurations take effect immediately without the need of restarting the service.  


## Log Format<a name="section1435319261199"></a>

**Table  3**  Log format

<a name="table131491213116"></a>
<table><thead align="left"><tr id="row12149112191110"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p683323501119"><a name="p683323501119"></a><a name="p683323501119"></a><strong id="b519329181512"><a name="b519329181512"></a><a name="b519329181512"></a>Log Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p13833173514110"><a name="p13833173514110"></a><a name="p13833173514110"></a><strong id="b936712589816"><a name="b936712589816"></a><a name="b936712589816"></a>Format</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p183373591114"><a name="p183373591114"></a><a name="p183373591114"></a><strong id="b1741321117158"><a name="b1741321117158"></a><a name="b1741321117158"></a>Example</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row181507210112"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p99601845151110"><a name="p99601845151110"></a><a name="p99601845151110"></a>Run log</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p10960114516118"><a name="p10960114516118"></a><a name="p10960114516118"></a>&lt;yyyy-MM-dd HH:mm:ss,SSS&gt;|&lt;Log Level&gt;|&lt;Name of the thread that generates the log&gt;|&lt;Message in the log&gt;|&lt;Location of the log event&gt;</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p996012457115"><a name="p996012457115"></a><a name="p996012457115"></a>2019-06-27 21:30:31,778 | INFO | [flink-akka.actor.default-dispatcher-3] | TaskManager container_e10_1498290698388_0004_02_000007 has started. | org.apache.flink.yarn.YarnFlinkResourceManager (FlinkResourceManager.java:368)</p>
</td>
</tr>
</tbody>
</table>


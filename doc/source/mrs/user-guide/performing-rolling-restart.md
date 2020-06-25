# Performing Rolling Restart<a name="EN-US_TOPIC_0221415066"></a>

After modifying the configuration items of a big data component, you need to restart the corresponding service to make new configurations take effect. If you use a normal restart mode, all services or instances are restarted concurrently, which may cause service interruption. To ensure that services are not affected during service restart, you can restart services or instances in batches by rolling restart. For instances in active/standby mode, a standby instance is restarted first and then an active instance is restarted. Rolling restart takes longer than normal restart.

[Table 1](#en-us_topic_0143479582_table054720341161)  provides services and instances that support or do not support rolling restart in the MRS cluster.

**Table  1**  Services and instances that support or do not support rolling restart

<a name="en-us_topic_0143479582_table054720341161"></a>
<table><thead align="left"><tr id="en-us_topic_0143479582_row254710343617"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="en-us_topic_0143479582_p1154743412613"><a name="en-us_topic_0143479582_p1154743412613"></a><a name="en-us_topic_0143479582_p1154743412613"></a>Service</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="en-us_topic_0143479582_p185471734868"><a name="en-us_topic_0143479582_p185471734868"></a><a name="en-us_topic_0143479582_p185471734868"></a>Instance</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="en-us_topic_0143479582_p1872382917393"><a name="en-us_topic_0143479582_p1872382917393"></a><a name="en-us_topic_0143479582_p1872382917393"></a>Whether to Support Rolling Restart</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0143479582_row1654716341963"><td class="cellrowborder" rowspan="5" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0143479582_p1554713341665"><a name="en-us_topic_0143479582_p1554713341665"></a><a name="en-us_topic_0143479582_p1554713341665"></a>HDFS</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0143479582_p1954711341668"><a name="en-us_topic_0143479582_p1954711341668"></a><a name="en-us_topic_0143479582_p1954711341668"></a>NameNode</p>
</td>
<td class="cellrowborder" rowspan="5" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0143479582_p143021054112"><a name="en-us_topic_0143479582_p143021054112"></a><a name="en-us_topic_0143479582_p143021054112"></a>Yes</p>
</td>
</tr>
<tr id="en-us_topic_0143479582_row14291659103919"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0143479582_p2249161464014"><a name="en-us_topic_0143479582_p2249161464014"></a><a name="en-us_topic_0143479582_p2249161464014"></a>ZKFC</p>
</td>
</tr>
<tr id="en-us_topic_0143479582_row1070911272409"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0143479582_p270922712400"><a name="en-us_topic_0143479582_p270922712400"></a><a name="en-us_topic_0143479582_p270922712400"></a>JournalNode</p>
</td>
</tr>
<tr id="en-us_topic_0143479582_row1958602464011"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0143479582_p205869246406"><a name="en-us_topic_0143479582_p205869246406"></a><a name="en-us_topic_0143479582_p205869246406"></a>HttpFS</p>
</td>
</tr>
<tr id="en-us_topic_0143479582_row185776644013"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0143479582_p15771163407"><a name="en-us_topic_0143479582_p15771163407"></a><a name="en-us_topic_0143479582_p15771163407"></a>DataNode</p>
</td>
</tr>
<tr id="en-us_topic_0143479582_row155471334661"><td class="cellrowborder" rowspan="2" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0143479582_p1554717341262"><a name="en-us_topic_0143479582_p1554717341262"></a><a name="en-us_topic_0143479582_p1554717341262"></a>Yarn</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0143479582_p181101130281"><a name="en-us_topic_0143479582_p181101130281"></a><a name="en-us_topic_0143479582_p181101130281"></a>ResourceManager</p>
</td>
<td class="cellrowborder" rowspan="2" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0143479582_p191971952154218"><a name="en-us_topic_0143479582_p191971952154218"></a><a name="en-us_topic_0143479582_p191971952154218"></a>Yes</p>
</td>
</tr>
<tr id="en-us_topic_0143479582_row5824641134217"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0143479582_p1582424116427"><a name="en-us_topic_0143479582_p1582424116427"></a><a name="en-us_topic_0143479582_p1582424116427"></a>NodeManager</p>
</td>
</tr>
<tr id="en-us_topic_0143479582_row754811341862"><td class="cellrowborder" rowspan="3" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0143479582_p156141727986"><a name="en-us_topic_0143479582_p156141727986"></a><a name="en-us_topic_0143479582_p156141727986"></a>Hive</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0143479582_p061118273815"><a name="en-us_topic_0143479582_p061118273815"></a><a name="en-us_topic_0143479582_p061118273815"></a>MetaStore</p>
</td>
<td class="cellrowborder" rowspan="3" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0143479582_p573472211437"><a name="en-us_topic_0143479582_p573472211437"></a><a name="en-us_topic_0143479582_p573472211437"></a>Yes</p>
</td>
</tr>
<tr id="en-us_topic_0143479582_row15685142164319"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0143479582_p66851925432"><a name="en-us_topic_0143479582_p66851925432"></a><a name="en-us_topic_0143479582_p66851925432"></a>WebHCat</p>
</td>
</tr>
<tr id="en-us_topic_0143479582_row199312513433"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0143479582_p119311594310"><a name="en-us_topic_0143479582_p119311594310"></a><a name="en-us_topic_0143479582_p119311594310"></a>HiveServer</p>
</td>
</tr>
<tr id="en-us_topic_0143479582_row195487341161"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0143479582_p65481434865"><a name="en-us_topic_0143479582_p65481434865"></a><a name="en-us_topic_0143479582_p65481434865"></a>MapReduce</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0143479582_p1548143419618"><a name="en-us_topic_0143479582_p1548143419618"></a><a name="en-us_topic_0143479582_p1548143419618"></a>JobHistoryServer</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0143479582_p5724829173914"><a name="en-us_topic_0143479582_p5724829173914"></a><a name="en-us_topic_0143479582_p5724829173914"></a>Yes</p>
</td>
</tr>
<tr id="en-us_topic_0143479582_row33934131017"><td class="cellrowborder" rowspan="4" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0143479582_p6417431019"><a name="en-us_topic_0143479582_p6417431019"></a><a name="en-us_topic_0143479582_p6417431019"></a>HBase</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0143479582_p84112413103"><a name="en-us_topic_0143479582_p84112413103"></a><a name="en-us_topic_0143479582_p84112413103"></a>HMaster</p>
</td>
<td class="cellrowborder" rowspan="4" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0143479582_p974311144449"><a name="en-us_topic_0143479582_p974311144449"></a><a name="en-us_topic_0143479582_p974311144449"></a>Yes</p>
</td>
</tr>
<tr id="en-us_topic_0143479582_row1179414611437"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0143479582_p2794146204316"><a name="en-us_topic_0143479582_p2794146204316"></a><a name="en-us_topic_0143479582_p2794146204316"></a>RegionServer</p>
</td>
</tr>
<tr id="en-us_topic_0143479582_row17566174414318"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0143479582_p7566194411437"><a name="en-us_topic_0143479582_p7566194411437"></a><a name="en-us_topic_0143479582_p7566194411437"></a>ThriftServer</p>
</td>
</tr>
<tr id="en-us_topic_0143479582_row73132421434"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0143479582_p10313124244311"><a name="en-us_topic_0143479582_p10313124244311"></a><a name="en-us_topic_0143479582_p10313124244311"></a>RESTServer</p>
</td>
</tr>
<tr id="en-us_topic_0143479582_row145652086106"><td class="cellrowborder" rowspan="3" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0143479582_p2056520821011"><a name="en-us_topic_0143479582_p2056520821011"></a><a name="en-us_topic_0143479582_p2056520821011"></a>Spark</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0143479582_p15655820106"><a name="en-us_topic_0143479582_p15655820106"></a><a name="en-us_topic_0143479582_p15655820106"></a>JobHistory</p>
</td>
<td class="cellrowborder" rowspan="2" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0143479582_p9445143974417"><a name="en-us_topic_0143479582_p9445143974417"></a><a name="en-us_topic_0143479582_p9445143974417"></a>Yes</p>
</td>
</tr>
<tr id="en-us_topic_0143479582_row85710234447"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0143479582_p35912235440"><a name="en-us_topic_0143479582_p35912235440"></a><a name="en-us_topic_0143479582_p35912235440"></a>JDBCServer</p>
</td>
</tr>
<tr id="en-us_topic_0143479582_row12947172010443"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0143479582_p109471201446"><a name="en-us_topic_0143479582_p109471201446"></a><a name="en-us_topic_0143479582_p109471201446"></a>SparkResource</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0143479582_p19470201449"><a name="en-us_topic_0143479582_p19470201449"></a><a name="en-us_topic_0143479582_p19470201449"></a>No</p>
</td>
</tr>
<tr id="en-us_topic_0143479582_row112153423415"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0143479582_p951410502419"><a name="en-us_topic_0143479582_p951410502419"></a><a name="en-us_topic_0143479582_p951410502419"></a>Hue</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0143479582_p175177505417"><a name="en-us_topic_0143479582_p175177505417"></a><a name="en-us_topic_0143479582_p175177505417"></a>Hue</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0143479582_p1221524214116"><a name="en-us_topic_0143479582_p1221524214116"></a><a name="en-us_topic_0143479582_p1221524214116"></a>No</p>
</td>
</tr>
<tr id="en-us_topic_0143479582_row42663354620"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0143479582_p82713315461"><a name="en-us_topic_0143479582_p82713315461"></a><a name="en-us_topic_0143479582_p82713315461"></a>Tez</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0143479582_p1827133144613"><a name="en-us_topic_0143479582_p1827133144613"></a><a name="en-us_topic_0143479582_p1827133144613"></a>TezUI</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0143479582_p102753318469"><a name="en-us_topic_0143479582_p102753318469"></a><a name="en-us_topic_0143479582_p102753318469"></a>No</p>
</td>
</tr>
<tr id="en-us_topic_0143479582_row51061153174119"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0143479582_p17962115914112"><a name="en-us_topic_0143479582_p17962115914112"></a><a name="en-us_topic_0143479582_p17962115914112"></a>Loader</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0143479582_p1496355954116"><a name="en-us_topic_0143479582_p1496355954116"></a><a name="en-us_topic_0143479582_p1496355954116"></a>Sqoop</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0143479582_p1810617536419"><a name="en-us_topic_0143479582_p1810617536419"></a><a name="en-us_topic_0143479582_p1810617536419"></a>No</p>
</td>
</tr>
<tr id="en-us_topic_0143479582_row522861311019"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0143479582_p8228613131010"><a name="en-us_topic_0143479582_p8228613131010"></a><a name="en-us_topic_0143479582_p8228613131010"></a>ZooKeeper</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0143479582_p19228213191020"><a name="en-us_topic_0143479582_p19228213191020"></a><a name="en-us_topic_0143479582_p19228213191020"></a>QuorumPeer</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0143479582_p57240293391"><a name="en-us_topic_0143479582_p57240293391"></a><a name="en-us_topic_0143479582_p57240293391"></a>Yes</p>
</td>
</tr>
<tr id="en-us_topic_0143479582_row19750194111013"><td class="cellrowborder" rowspan="2" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0143479582_p145494311122"><a name="en-us_topic_0143479582_p145494311122"></a><a name="en-us_topic_0143479582_p145494311122"></a>Kafka</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0143479582_p1475034131013"><a name="en-us_topic_0143479582_p1475034131013"></a><a name="en-us_topic_0143479582_p1475034131013"></a>Broker</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0143479582_p572412919398"><a name="en-us_topic_0143479582_p572412919398"></a><a name="en-us_topic_0143479582_p572412919398"></a>Yes</p>
</td>
</tr>
<tr id="en-us_topic_0143479582_row616512616458"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0143479582_p19165186184512"><a name="en-us_topic_0143479582_p19165186184512"></a><a name="en-us_topic_0143479582_p19165186184512"></a>MirrorMaker</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0143479582_p316518610456"><a name="en-us_topic_0143479582_p316518610456"></a><a name="en-us_topic_0143479582_p316518610456"></a>No</p>
</td>
</tr>
<tr id="en-us_topic_0143479582_row3834738121012"><td class="cellrowborder" rowspan="2" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0143479582_p75454331210"><a name="en-us_topic_0143479582_p75454331210"></a><a name="en-us_topic_0143479582_p75454331210"></a>Flume</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0143479582_p19834163811011"><a name="en-us_topic_0143479582_p19834163811011"></a><a name="en-us_topic_0143479582_p19834163811011"></a>Flume</p>
</td>
<td class="cellrowborder" rowspan="2" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0143479582_p1858732810452"><a name="en-us_topic_0143479582_p1858732810452"></a><a name="en-us_topic_0143479582_p1858732810452"></a>Yes</p>
</td>
</tr>
<tr id="en-us_topic_0143479582_row179322024519"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0143479582_p37931320144517"><a name="en-us_topic_0143479582_p37931320144517"></a><a name="en-us_topic_0143479582_p37931320144517"></a>MonitorServer</p>
</td>
</tr>
<tr id="en-us_topic_0143479582_row0423535131019"><td class="cellrowborder" rowspan="4" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0143479582_p1354154310122"><a name="en-us_topic_0143479582_p1354154310122"></a><a name="en-us_topic_0143479582_p1354154310122"></a>Storm</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0143479582_p16424193520106"><a name="en-us_topic_0143479582_p16424193520106"></a><a name="en-us_topic_0143479582_p16424193520106"></a>Nimbus</p>
</td>
<td class="cellrowborder" rowspan="4" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0143479582_p69901611104619"><a name="en-us_topic_0143479582_p69901611104619"></a><a name="en-us_topic_0143479582_p69901611104619"></a>Yes</p>
</td>
</tr>
<tr id="en-us_topic_0143479582_row8537042154519"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0143479582_p1953816425455"><a name="en-us_topic_0143479582_p1953816425455"></a><a name="en-us_topic_0143479582_p1953816425455"></a>UI</p>
</td>
</tr>
<tr id="en-us_topic_0143479582_row429754434517"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0143479582_p12298244144515"><a name="en-us_topic_0143479582_p12298244144515"></a><a name="en-us_topic_0143479582_p12298244144515"></a>Supervisor</p>
</td>
</tr>
<tr id="en-us_topic_0143479582_row11276134074514"><td class="cellrowborder" valign="top" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0143479582_p192761540184512"><a name="en-us_topic_0143479582_p192761540184512"></a><a name="en-us_topic_0143479582_p192761540184512"></a>LogViewer</p>
</td>
</tr>
</tbody>
</table>

## Restrictions<a name="section2092893416170"></a>

-   Perform a rolling restart during off-peak hours.
    -   Otherwise, a rolling restart failure may occur. For example, if the throughput of Kafka is high \(over 100 MB/s\) during the Kafka rolling restart, the Kafka rolling restart may fail.
    -   For example, if the requests per second of each RegionServer on the native interface exceed 10,000 during the HBase rolling restart, you need to increase the number of handles to prevent a RegionServer restart failure caused by heavy loads during the restart.

-   Before the restart, check the number of current requests of HBase. If requests of each RegionServer on the native interface exceeds 10,000, increase the number of handles to prevent a failure.
-   If the number of Core nodes in a cluster is less than six, services may be affected for a short period of time.
-   Preferentially perform a rolling instance or service restart and select  **Only restart instances whose configurations have expired**.

## Performing a Rolling Service Restart<a name="section10904115910327"></a>

1.  On MRS Manager, click  **Services**  and select a service for which you want to perform a rolling restart.
2.  On the  **Service Status**  tab page, click  **More**  and select  **Perform Rolling Service Restart**.
3.  After you enter the administrator password, the  **Perform Rolling Service Restart**  page is displayed. Select  **Only restart instances whose configurations have expired**  and click  **OK**  to perform rolling restart for the service.
4.  After the rolling restart task is complete, click  **Finish**.

## Performing a Rolling Instance Restart<a name="section7905115912322"></a>

1.  On MRS Manager, click  **Services**  and select a service for which you want to perform a rolling restart.
2.  On the  **Instance**  tab page, select the instance to be restarted. Click  **More**  and select  **Perform Rolling Instance Restart**.
3.  After you enter the administrator password, the  **Perform Rolling Instance Restart**  page is displayed. Select  **Only restart instances whose configurations have expired**  and click  **OK**  to perform rolling restart for the instance.
4.  After the rolling restart task is complete, click  **Finish**.

## Perform a Rolling Cluster Restart<a name="section590655943212"></a>

1.  On MRS Manager, click  **Services**. The  **Services**  page is displayed.
2.  Click  **More**  and select  **Perform Rolling Cluster Restart**.
3.  After you enter the administrator password, the  **Perform Rolling Cluster Restart**  page is displayed. Select  **Only restart instances whose configurations have expired**  and click  **OK**  to perform rolling restart for the cluster.
4.  After the rolling restart task is complete, click  **Finish**.

## Rolling Restart Parameter Description<a name="section289834562610"></a>

[Table 2](#table817615121520)  describes rolling restart parameters.

**Table  2**  Rolling restart parameter description

<a name="table817615121520"></a>
<table><thead align="left"><tr id="row10176131217216"><th class="cellrowborder" valign="top" width="24.560000000000002%" id="mcps1.2.3.1.1"><p id="p1617661219217"><a name="p1617661219217"></a><a name="p1617661219217"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="75.44%" id="mcps1.2.3.1.2"><p id="p1917610123214"><a name="p1917610123214"></a><a name="p1917610123214"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row8176712727"><td class="cellrowborder" valign="top" width="24.560000000000002%" headers="mcps1.2.3.1.1 "><p id="p12176612228"><a name="p12176612228"></a><a name="p12176612228"></a>Only restart instances whose configurations have expired</p>
</td>
<td class="cellrowborder" valign="top" width="75.44%" headers="mcps1.2.3.1.2 "><p id="p71761012122"><a name="p71761012122"></a><a name="p71761012122"></a>Specifies whether to restart only the modified instances in a cluster.</p>
</td>
</tr>
<tr id="row161761712825"><td class="cellrowborder" valign="top" width="24.560000000000002%" headers="mcps1.2.3.1.1 "><p id="p1517601214211"><a name="p1517601214211"></a><a name="p1517601214211"></a>Data Node Instances to Be Batch Restarted</p>
</td>
<td class="cellrowborder" valign="top" width="75.44%" headers="mcps1.2.3.1.2 "><p id="p1217614122025"><a name="p1217614122025"></a><a name="p1217614122025"></a>Specifies the number of instances that are restarted in each batch when the batch rolling restart strategy is used. The default value is <strong id="b132982083120"><a name="b132982083120"></a><a name="b132982083120"></a>1</strong>. The value ranges from 1 to 20. This parameter is valid only for data nodes.</p>
</td>
</tr>
<tr id="row1917710127217"><td class="cellrowborder" valign="top" width="24.560000000000002%" headers="mcps1.2.3.1.1 "><p id="p31771112423"><a name="p31771112423"></a><a name="p31771112423"></a>Batch Interval</p>
</td>
<td class="cellrowborder" valign="top" width="75.44%" headers="mcps1.2.3.1.2 "><p id="p1417714129215"><a name="p1417714129215"></a><a name="p1417714129215"></a>Specifies the interval between two batches of instances for rolling restart. The default value is <strong id="b3333132014315"><a name="b3333132014315"></a><a name="b3333132014315"></a>0</strong>. The value ranges from 0 to 2147483647. The unit is second.</p>
<p id="p10214171115194"><a name="p10214171115194"></a><a name="p10214171115194"></a>Note: Setting the batch interval parameter can increase the stability of the big data component process during the rolling restart. You are advised to set this parameter to a non-default value, for example, 10.</p>
</td>
</tr>
<tr id="row10177121219210"><td class="cellrowborder" valign="top" width="24.560000000000002%" headers="mcps1.2.3.1.1 "><p id="p101771612729"><a name="p101771612729"></a><a name="p101771612729"></a>Batch Fault Tolerance Threshold</p>
</td>
<td class="cellrowborder" valign="top" width="75.44%" headers="mcps1.2.3.1.2 "><p id="p11775123217"><a name="p11775123217"></a><a name="p11775123217"></a>Specifies the tolerance times when the rolling restart of instances fails to be executed in batches. The default value is <strong id="b8336420163117"><a name="b8336420163117"></a><a name="b8336420163117"></a>0</strong>, which indicates that the rolling restart task ends after any batch of instances fails to be restarted. The value ranges from 0 to 214748364.</p>
</td>
</tr>
</tbody>
</table>

## Procedure in a Typical Scenario<a name="section39091859183215"></a>

1.  On MRS Manager, click  **Services**  and select HBase. The HBase service page is displayed.
2.  Click the  **Service Configuration**  tab, and modify an HBase parameter. After the following dialog box is displayed, click  **OK**  to save the configurations.

    >![](/images/icon-note.gif) **NOTE:**   
    >Do not select  **Restart the affected services or instances**. This option indicates a normal restart. If you select this option, all services or instances will be restarted, which may cause service interruption.  

3.  After saving the configurations, click  **Finish**.
4.  Click the  **Service Status**  tab.
5.  On the  **Service Status**  tab page, click  **More**  and select  **Perform Rolling Service Restart**.
6.  After you enter the administrator password, the  **Perform Rolling Service Restart**  page is displayed. Select  **Only restart instances whose configurations have expired**  and click  **OK**  to perform rolling restart for the service.
7.  After the rolling restart task is complete, click  **Finish**.


# Viewing EVS Monitoring Data<a name="evs_01_0044"></a>

## Description<a name="section1745822015166"></a>

This topic describes monitored metrics reported by EVS to Cloud Eye as well as their namespaces and dimensions. You can use console or APIs provided by Cloud Eye to query the metrics of the monitored objects and alarms generated for EVS.

## Namespace<a name="section13533246161919"></a>

SYS.EVS

## Metrics<a name="section41057935193257"></a>

<a name="table1129854519446"></a>
<table><thead align="left"><tr id="row7299845174418"><th class="cellrowborder" valign="top" width="12.871287128712872%" id="mcps1.1.7.1.1"><p id="p169902186219"><a name="p169902186219"></a><a name="p169902186219"></a>Metric ID</p>
</th>
<th class="cellrowborder" valign="top" width="13.861386138613863%" id="mcps1.1.7.1.2"><p id="p7299164517441"><a name="p7299164517441"></a><a name="p7299164517441"></a>Metric Name</p>
</th>
<th class="cellrowborder" valign="top" width="29.7029702970297%" id="mcps1.1.7.1.3"><p id="p20300194510442"><a name="p20300194510442"></a><a name="p20300194510442"></a>Meaning</p>
</th>
<th class="cellrowborder" valign="top" width="14.85148514851485%" id="mcps1.1.7.1.4"><p id="p57868341081"><a name="p57868341081"></a><a name="p57868341081"></a>Value Range</p>
</th>
<th class="cellrowborder" valign="top" width="13.861386138613863%" id="mcps1.1.7.1.5"><p id="p1730013458445"><a name="p1730013458445"></a><a name="p1730013458445"></a>Monitored Object</p>
</th>
<th class="cellrowborder" valign="top" width="14.85148514851485%" id="mcps1.1.7.1.6"><p id="p1489034132517"><a name="p1489034132517"></a><a name="p1489034132517"></a>Monitoring Period (Raw Data)</p>
</th>
</tr>
</thead>
<tbody><tr id="row58713584313"><td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.1.7.1.1 "><p id="p18990718122112"><a name="p18990718122112"></a><a name="p18990718122112"></a>disk_device_read_bytes_rate</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.1.7.1.2 "><p id="p639293919437"><a name="p639293919437"></a><a name="p639293919437"></a>Disk Read Bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="29.7029702970297%" headers="mcps1.1.7.1.3 "><p id="p63947395438"><a name="p63947395438"></a><a name="p63947395438"></a>Number of bytes read from the monitored disk per second</p>
<p id="p19395103912436"><a name="p19395103912436"></a><a name="p19395103912436"></a>Unit: Bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.1.7.1.4 "><p id="p47878341989"><a name="p47878341989"></a><a name="p47878341989"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.1.7.1.5 "><p id="p75621043204313"><a name="p75621043204313"></a><a name="p75621043204313"></a>EVS disk</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.1.7.1.6 "><p id="p9607175712566"><a name="p9607175712566"></a><a name="p9607175712566"></a>5 minutes</p>
</td>
</tr>
<tr id="row79016514437"><td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.1.7.1.1 "><p id="p9990191819211"><a name="p9990191819211"></a><a name="p9990191819211"></a>disk_device_write_bytes_rate</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.1.7.1.2 "><p id="p1039719396437"><a name="p1039719396437"></a><a name="p1039719396437"></a>Disk Write Bandwidth</p>
</td>
<td class="cellrowborder" valign="top" width="29.7029702970297%" headers="mcps1.1.7.1.3 "><p id="p1439873904318"><a name="p1439873904318"></a><a name="p1439873904318"></a>Number of bytes written to the monitored disk per second</p>
<p id="p1040033904311"><a name="p1040033904311"></a><a name="p1040033904311"></a>Unit: Bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.1.7.1.4 "><p id="p14787934887"><a name="p14787934887"></a><a name="p14787934887"></a>≥ 0 bytes/s</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.1.7.1.5 "><p id="p1856324311438"><a name="p1856324311438"></a><a name="p1856324311438"></a>EVS disk</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.1.7.1.6 "><p id="p123718166583"><a name="p123718166583"></a><a name="p123718166583"></a>5 minutes</p>
</td>
</tr>
<tr id="row29018554320"><td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.1.7.1.1 "><p id="p1299021822118"><a name="p1299021822118"></a><a name="p1299021822118"></a>disk_device_read_requests_rate</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.1.7.1.2 "><p id="p16405193904316"><a name="p16405193904316"></a><a name="p16405193904316"></a>Disk Read IOPS</p>
</td>
<td class="cellrowborder" valign="top" width="29.7029702970297%" headers="mcps1.1.7.1.3 "><p id="p1440793924312"><a name="p1440793924312"></a><a name="p1440793924312"></a>Number of read requests sent to the monitored disk per second</p>
<p id="p2040873910435"><a name="p2040873910435"></a><a name="p2040873910435"></a>Unit: Requests/s</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.1.7.1.4 "><p id="p127874348815"><a name="p127874348815"></a><a name="p127874348815"></a>≥ 0 Requests/s</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.1.7.1.5 "><p id="p12567114314431"><a name="p12567114314431"></a><a name="p12567114314431"></a>EVS disk</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.1.7.1.6 "><p id="p152531220165818"><a name="p152531220165818"></a><a name="p152531220165818"></a>5 minutes</p>
</td>
</tr>
<tr id="row17904512439"><td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.1.7.1.1 "><p id="p17990101811218"><a name="p17990101811218"></a><a name="p17990101811218"></a>disk_device_write_requests_rate</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.1.7.1.2 "><p id="p1941163924310"><a name="p1941163924310"></a><a name="p1941163924310"></a>Disk Write IOPS</p>
</td>
<td class="cellrowborder" valign="top" width="29.7029702970297%" headers="mcps1.1.7.1.3 "><p id="p24133398432"><a name="p24133398432"></a><a name="p24133398432"></a>Number of write requests sent to the monitored disk per second</p>
<p id="p10123936182914"><a name="p10123936182914"></a><a name="p10123936182914"></a>Unit: Requests/s</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.1.7.1.4 "><p id="p878711347812"><a name="p878711347812"></a><a name="p878711347812"></a>≥ 0 Requests/s</p>
</td>
<td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.1.7.1.5 "><p id="p5569243174314"><a name="p5569243174314"></a><a name="p5569243174314"></a>EVS disk</p>
</td>
<td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.1.7.1.6 "><p id="p1197762312583"><a name="p1197762312583"></a><a name="p1197762312583"></a>5 minutes</p>
</td>
</tr>
</tbody>
</table>

## Dimension<a name="section14641124873613"></a>

<a name="table41401726183716"></a>
<table><thead align="left"><tr id="row514518264377"><th class="cellrowborder" valign="top" width="20.61%" id="mcps1.1.3.1.1"><p id="p111451726123710"><a name="p111451726123710"></a><a name="p111451726123710"></a>Key</p>
</th>
<th class="cellrowborder" valign="top" width="79.39%" id="mcps1.1.3.1.2"><p id="p1214522616377"><a name="p1214522616377"></a><a name="p1214522616377"></a>Value</p>
</th>
</tr>
</thead>
<tbody><tr id="row914532623717"><td class="cellrowborder" valign="top" width="20.61%" headers="mcps1.1.3.1.1 "><p id="p7145152618371"><a name="p7145152618371"></a><a name="p7145152618371"></a>disk_name</p>
</td>
<td class="cellrowborder" valign="top" width="79.39%" headers="mcps1.1.3.1.2 "><p id="p7146202619371"><a name="p7146202619371"></a><a name="p7146202619371"></a>Server ID-disk name, for example, 6f3c6f91-4b24-4e1b-b7d1-a94ac1cb011d-sda (sda is the disk name)</p>
</td>
</tr>
</tbody>
</table>

## Viewing Monitoring Data<a name="section54024495194114"></a>

1.  Log in to the management console.
2.  Under  **Storage**, click  **Elastic Volume Service**.

    The disk list page is displayed.

3.  In the EVS disk list, click the name of the disk you want to view the monitoring data.

    The disk details page is displayed.

4.  On the  **Attachments**  tab, locate the row that contains the server and click  **View Monitoring Data**  in the  **Operation**  column.

    The monitoring graphs page is displayed.

5.  You can view the disk monitoring data by metric or monitored duration.

    For more information about Cloud Eye, see the  _Cloud Eye User Guide_.



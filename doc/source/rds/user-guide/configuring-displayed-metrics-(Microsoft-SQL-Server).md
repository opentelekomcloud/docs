# Configuring Displayed Metrics<a name="rds_sqlserver_06_0001"></a>

## Description<a name="section3846020215313"></a>

This section describes namespaces, descriptions, and dimensions of monitoring metrics to be reported to Cloud Eye. Users can retrieve monitoring metrics and alarm information reported to Cloud Eye over its API.

## Namespace<a name="section1688213153437"></a>

SYS.RDS

## DB Instance Monitoring Metrics<a name="section758818457377"></a>

-   [Table 1](#en-us_topic_0171122394_table2501556415126)  lists details about ECS metrics.

    **Table  1**  ECS performance metrics

    <a name="en-us_topic_0171122394_table2501556415126"></a>
    <table><thead align="left"><tr id="en-us_topic_0171122394_row1227696315126"><th class="cellrowborder" valign="top" width="18.01%" id="mcps1.2.7.1.1"><p id="p3333174917503"><a name="p3333174917503"></a><a name="p3333174917503"></a><strong id="b770113292266"><a name="b770113292266"></a><a name="b770113292266"></a>Metric ID</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="10.32%" id="mcps1.2.7.1.2"><p id="en-us_topic_0171122394_p5084337715126"><a name="en-us_topic_0171122394_p5084337715126"></a><a name="en-us_topic_0171122394_p5084337715126"></a><strong id="b5884103262615"><a name="b5884103262615"></a><a name="b5884103262615"></a>Metric Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="30.48%" id="mcps1.2.7.1.3"><p id="en-us_topic_0171122394_p2467289315126"><a name="en-us_topic_0171122394_p2467289315126"></a><a name="en-us_topic_0171122394_p2467289315126"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="9.4%" id="mcps1.2.7.1.4"><p id="en-us_topic_0171122394_p5234735015126"><a name="en-us_topic_0171122394_p5234735015126"></a><a name="en-us_topic_0171122394_p5234735015126"></a>Value Range</p>
    </th>
    <th class="cellrowborder" valign="top" width="23.94%" id="mcps1.2.7.1.5"><p id="p10610125265116"><a name="p10610125265116"></a><a name="p10610125265116"></a>Monitored Object</p>
    </th>
    <th class="cellrowborder" valign="top" width="7.85%" id="mcps1.2.7.1.6"><p id="p3610195212511"><a name="p3610195212511"></a><a name="p3610195212511"></a>Monitoring Interval (Raw Data)</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0171122394_row5692358915126"><td class="cellrowborder" valign="top" width="18.01%" headers="mcps1.2.7.1.1 "><p id="p751061735110"><a name="p751061735110"></a><a name="p751061735110"></a>rds001_cpu_util</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.32%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0171122394_p5490996515126"><a name="en-us_topic_0171122394_p5490996515126"></a><a name="en-us_topic_0171122394_p5490996515126"></a>CPU Usage</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.48%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0171122394_p1852217115126"><a name="en-us_topic_0171122394_p1852217115126"></a><a name="en-us_topic_0171122394_p1852217115126"></a>CPU usage of the monitored object</p>
    </td>
    <td class="cellrowborder" valign="top" width="9.4%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0171122394_p2390088615126"><a name="en-us_topic_0171122394_p2390088615126"></a><a name="en-us_topic_0171122394_p2390088615126"></a>0%–100%</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.94%" headers="mcps1.2.7.1.5 "><p id="p15839192211539"><a name="p15839192211539"></a><a name="p15839192211539"></a>Monitored object: ECS</p>
    <p id="p12839152225312"><a name="p12839152225312"></a><a name="p12839152225312"></a>Monitored instance type: Microsoft SQL Server instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="7.85%" headers="mcps1.2.7.1.6 "><p id="p3839622135312"><a name="p3839622135312"></a><a name="p3839622135312"></a>1 minute</p>
    </td>
    </tr>
    <tr id="en-us_topic_0171122394_row21596471996"><td class="cellrowborder" valign="top" width="18.01%" headers="mcps1.2.7.1.1 "><p id="p1751031705114"><a name="p1751031705114"></a><a name="p1751031705114"></a>rds003_iops</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.32%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0171122394_p36363015126"><a name="en-us_topic_0171122394_p36363015126"></a><a name="en-us_topic_0171122394_p36363015126"></a>IOPS</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.48%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0171122394_p2945410815126"><a name="en-us_topic_0171122394_p2945410815126"></a><a name="en-us_topic_0171122394_p2945410815126"></a>Average number of I/O requests processed by the system in a specified period</p>
    </td>
    <td class="cellrowborder" valign="top" width="9.4%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0171122394_p3697255815126"><a name="en-us_topic_0171122394_p3697255815126"></a><a name="en-us_topic_0171122394_p3697255815126"></a>≥ 0 count/s</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.94%" headers="mcps1.2.7.1.5 "><p id="p5839102211536"><a name="p5839102211536"></a><a name="p5839102211536"></a>Monitored object: ECS</p>
    <p id="p883911222532"><a name="p883911222532"></a><a name="p883911222532"></a>Monitored instance type: Microsoft SQL Server instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="7.85%" headers="mcps1.2.7.1.6 "><p id="p1783912210536"><a name="p1783912210536"></a><a name="p1783912210536"></a>1 minute</p>
    </td>
    </tr>
    <tr id="en-us_topic_0171122394_row1323713512918"><td class="cellrowborder" valign="top" width="18.01%" headers="mcps1.2.7.1.1 "><p id="p451061715118"><a name="p451061715118"></a><a name="p451061715118"></a>rds039_disk_util</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.32%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0171122394_p3318453015126"><a name="en-us_topic_0171122394_p3318453015126"></a><a name="en-us_topic_0171122394_p3318453015126"></a>Storage Space Usage</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.48%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0171122394_p359239415126"><a name="en-us_topic_0171122394_p359239415126"></a><a name="en-us_topic_0171122394_p359239415126"></a>Storage space usage of the monitored object</p>
    </td>
    <td class="cellrowborder" valign="top" width="9.4%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0171122394_p2254847415126"><a name="en-us_topic_0171122394_p2254847415126"></a><a name="en-us_topic_0171122394_p2254847415126"></a>0%–100%</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.94%" headers="mcps1.2.7.1.5 "><p id="p483912222537"><a name="p483912222537"></a><a name="p483912222537"></a>Monitored object: ECS</p>
    <p id="p783917224533"><a name="p783917224533"></a><a name="p783917224533"></a>Monitored instance type: Microsoft SQL Server instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="7.85%" headers="mcps1.2.7.1.6 "><p id="p18839322115316"><a name="p18839322115316"></a><a name="p18839322115316"></a>1 minute</p>
    </td>
    </tr>
    <tr id="en-us_topic_0171122394_row1495348415126"><td class="cellrowborder" valign="top" width="18.01%" headers="mcps1.2.7.1.1 "><p id="p17510201712511"><a name="p17510201712511"></a><a name="p17510201712511"></a>rds002_mem_util</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.32%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0171122394_p4255025615126"><a name="en-us_topic_0171122394_p4255025615126"></a><a name="en-us_topic_0171122394_p4255025615126"></a>Memory Usage</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.48%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0171122394_p2401868115126"><a name="en-us_topic_0171122394_p2401868115126"></a><a name="en-us_topic_0171122394_p2401868115126"></a>Memory usage of the monitored object</p>
    </td>
    <td class="cellrowborder" valign="top" width="9.4%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0171122394_p6646497015126"><a name="en-us_topic_0171122394_p6646497015126"></a><a name="en-us_topic_0171122394_p6646497015126"></a>0%–100%</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.94%" headers="mcps1.2.7.1.5 "><p id="p583914222532"><a name="p583914222532"></a><a name="p583914222532"></a>Monitored object: ECS</p>
    <p id="p583942265310"><a name="p583942265310"></a><a name="p583942265310"></a>Monitored instance type: Microsoft SQL Server instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="7.85%" headers="mcps1.2.7.1.6 "><p id="p19839172285316"><a name="p19839172285316"></a><a name="p19839172285316"></a>1 minute</p>
    </td>
    </tr>
    <tr id="en-us_topic_0171122394_row1515911115126"><td class="cellrowborder" valign="top" width="18.01%" headers="mcps1.2.7.1.1 "><p id="p651001719518"><a name="p651001719518"></a><a name="p651001719518"></a>rds004_bytes_in</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.32%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0171122394_p4234088815126"><a name="en-us_topic_0171122394_p4234088815126"></a><a name="en-us_topic_0171122394_p4234088815126"></a>Network Input Throughput</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.48%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0171122394_p62108092162725"><a name="en-us_topic_0171122394_p62108092162725"></a><a name="en-us_topic_0171122394_p62108092162725"></a>Incoming traffic in bytes per second</p>
    </td>
    <td class="cellrowborder" valign="top" width="9.4%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0171122394_p3498433815126"><a name="en-us_topic_0171122394_p3498433815126"></a><a name="en-us_topic_0171122394_p3498433815126"></a>≥ 0 byte/s</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.94%" headers="mcps1.2.7.1.5 "><p id="p384032218537"><a name="p384032218537"></a><a name="p384032218537"></a>Monitored object: ECS</p>
    <p id="p2084042275315"><a name="p2084042275315"></a><a name="p2084042275315"></a>Monitored instance type: Microsoft SQL Server instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="7.85%" headers="mcps1.2.7.1.6 "><p id="p168401222125311"><a name="p168401222125311"></a><a name="p168401222125311"></a>1 minute</p>
    </td>
    </tr>
    <tr id="en-us_topic_0171122394_row368717015126"><td class="cellrowborder" valign="top" width="18.01%" headers="mcps1.2.7.1.1 "><p id="p14510101714517"><a name="p14510101714517"></a><a name="p14510101714517"></a>rds005_bytes_out</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.32%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0171122394_p221427715126"><a name="en-us_topic_0171122394_p221427715126"></a><a name="en-us_topic_0171122394_p221427715126"></a>Network Output Throughput</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.48%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0171122394_p4513871415126"><a name="en-us_topic_0171122394_p4513871415126"></a><a name="en-us_topic_0171122394_p4513871415126"></a>Outgoing traffic in bytes per second</p>
    </td>
    <td class="cellrowborder" valign="top" width="9.4%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0171122394_p3235719515126"><a name="en-us_topic_0171122394_p3235719515126"></a><a name="en-us_topic_0171122394_p3235719515126"></a>≥ 0 byte/s</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.94%" headers="mcps1.2.7.1.5 "><p id="p9840102265318"><a name="p9840102265318"></a><a name="p9840102265318"></a>Monitored object: ECS</p>
    <p id="p188401322105313"><a name="p188401322105313"></a><a name="p188401322105313"></a>Monitored instance type: Microsoft SQL Server instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="7.85%" headers="mcps1.2.7.1.6 "><p id="p15840192210538"><a name="p15840192210538"></a><a name="p15840192210538"></a>1 minute</p>
    </td>
    </tr>
    <tr id="en-us_topic_0171122394_row1357144291416"><td class="cellrowborder" valign="top" width="18.01%" headers="mcps1.2.7.1.1 "><p id="p13510417115110"><a name="p13510417115110"></a><a name="p13510417115110"></a>rds049_disk_read_throughput</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.32%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0171122394_p59436423162135"><a name="en-us_topic_0171122394_p59436423162135"></a><a name="en-us_topic_0171122394_p59436423162135"></a>Disk Read Throughput</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.48%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0171122394_p49620984162135"><a name="en-us_topic_0171122394_p49620984162135"></a><a name="en-us_topic_0171122394_p49620984162135"></a>Number of bytes read from the disk per second</p>
    </td>
    <td class="cellrowborder" valign="top" width="9.4%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0171122394_p59876806162135"><a name="en-us_topic_0171122394_p59876806162135"></a><a name="en-us_topic_0171122394_p59876806162135"></a>≥ 0 byte/s</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.94%" headers="mcps1.2.7.1.5 "><p id="p178401222185312"><a name="p178401222185312"></a><a name="p178401222185312"></a>Monitored object: ECS</p>
    <p id="p11840322165311"><a name="p11840322165311"></a><a name="p11840322165311"></a>Monitored instance type: Microsoft SQL Server instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="7.85%" headers="mcps1.2.7.1.6 "><p id="p1884052275314"><a name="p1884052275314"></a><a name="p1884052275314"></a>1 minute</p>
    </td>
    </tr>
    <tr id="en-us_topic_0171122394_row103958469147"><td class="cellrowborder" valign="top" width="18.01%" headers="mcps1.2.7.1.1 "><p id="p951061705116"><a name="p951061705116"></a><a name="p951061705116"></a>rds050_disk_write_throughput</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.32%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0171122394_p63245844162132"><a name="en-us_topic_0171122394_p63245844162132"></a><a name="en-us_topic_0171122394_p63245844162132"></a>Disk Write Throughput</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.48%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0171122394_p22639760162132"><a name="en-us_topic_0171122394_p22639760162132"></a><a name="en-us_topic_0171122394_p22639760162132"></a>Number of bytes written into the disk per second</p>
    </td>
    <td class="cellrowborder" valign="top" width="9.4%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0171122394_p21881305162132"><a name="en-us_topic_0171122394_p21881305162132"></a><a name="en-us_topic_0171122394_p21881305162132"></a>≥ 0 byte/s</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.94%" headers="mcps1.2.7.1.5 "><p id="p128408220533"><a name="p128408220533"></a><a name="p128408220533"></a>Monitored object: ECS</p>
    <p id="p18840922185312"><a name="p18840922185312"></a><a name="p18840922185312"></a>Monitored instance type: Microsoft SQL Server instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="7.85%" headers="mcps1.2.7.1.6 "><p id="p1684012225539"><a name="p1684012225539"></a><a name="p1684012225539"></a>1 minute</p>
    </td>
    </tr>
    <tr id="en-us_topic_0171122394_row1144519401149"><td class="cellrowborder" valign="top" width="18.01%" headers="mcps1.2.7.1.1 "><p id="p7510217135119"><a name="p7510217135119"></a><a name="p7510217135119"></a>rds051_avg_disk_sec_per_read</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.32%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0171122394_p52754676162127"><a name="en-us_topic_0171122394_p52754676162127"></a><a name="en-us_topic_0171122394_p52754676162127"></a>Disk Read Time</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.48%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0171122394_p45270338162127"><a name="en-us_topic_0171122394_p45270338162127"></a><a name="en-us_topic_0171122394_p45270338162127"></a>Average time required for each 1 KB disk read in a specified period</p>
    </td>
    <td class="cellrowborder" valign="top" width="9.4%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0171122394_p43018728162127"><a name="en-us_topic_0171122394_p43018728162127"></a><a name="en-us_topic_0171122394_p43018728162127"></a>≥ 0 ms</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.94%" headers="mcps1.2.7.1.5 "><p id="p0840422195312"><a name="p0840422195312"></a><a name="p0840422195312"></a>Monitored object: ECS</p>
    <p id="p1084010224532"><a name="p1084010224532"></a><a name="p1084010224532"></a>Monitored instance type: Microsoft SQL Server instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="7.85%" headers="mcps1.2.7.1.6 "><p id="p13840122216538"><a name="p13840122216538"></a><a name="p13840122216538"></a>1 minute</p>
    </td>
    </tr>
    <tr id="en-us_topic_0171122394_row1842903718149"><td class="cellrowborder" valign="top" width="18.01%" headers="mcps1.2.7.1.1 "><p id="p1451011171518"><a name="p1451011171518"></a><a name="p1451011171518"></a>rds052_avg_disk_sec_per_write</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.32%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0171122394_p50241145162111"><a name="en-us_topic_0171122394_p50241145162111"></a><a name="en-us_topic_0171122394_p50241145162111"></a>Disk Write Time</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.48%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0171122394_p43000972162111"><a name="en-us_topic_0171122394_p43000972162111"></a><a name="en-us_topic_0171122394_p43000972162111"></a>Average time required for each 1 KB disk write in a specified period</p>
    </td>
    <td class="cellrowborder" valign="top" width="9.4%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0171122394_p60526687162111"><a name="en-us_topic_0171122394_p60526687162111"></a><a name="en-us_topic_0171122394_p60526687162111"></a>≥ 0 ms</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.94%" headers="mcps1.2.7.1.5 "><p id="p484082219538"><a name="p484082219538"></a><a name="p484082219538"></a>Monitored object: ECS</p>
    <p id="p1484022225311"><a name="p1484022225311"></a><a name="p1484022225311"></a>Monitored instance type: Microsoft SQL Server instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="7.85%" headers="mcps1.2.7.1.6 "><p id="p10840122211535"><a name="p10840122211535"></a><a name="p10840122211535"></a>1 minute</p>
    </td>
    </tr>
    <tr id="en-us_topic_0171122394_row45617812162113"><td class="cellrowborder" valign="top" width="18.01%" headers="mcps1.2.7.1.1 "><p id="p751041795112"><a name="p751041795112"></a><a name="p751041795112"></a>rds047_disk_total_size</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.32%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0171122394_p4055305162113"><a name="en-us_topic_0171122394_p4055305162113"></a><a name="en-us_topic_0171122394_p4055305162113"></a>Total Storage Space</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.48%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0171122394_p60044274162113"><a name="en-us_topic_0171122394_p60044274162113"></a><a name="en-us_topic_0171122394_p60044274162113"></a>Total storage space of the monitored object</p>
    </td>
    <td class="cellrowborder" valign="top" width="9.4%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0171122394_p31748024162113"><a name="en-us_topic_0171122394_p31748024162113"></a><a name="en-us_topic_0171122394_p31748024162113"></a>40–4000 GB</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.94%" headers="mcps1.2.7.1.5 "><p id="p8840722145310"><a name="p8840722145310"></a><a name="p8840722145310"></a>Monitored object: ECS</p>
    <p id="p15840182225316"><a name="p15840182225316"></a><a name="p15840182225316"></a>Monitored instance type: Microsoft SQL Server instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="7.85%" headers="mcps1.2.7.1.6 "><p id="p4840182255319"><a name="p4840182255319"></a><a name="p4840182255319"></a>1 minute</p>
    </td>
    </tr>
    <tr id="en-us_topic_0171122394_row18847359162111"><td class="cellrowborder" valign="top" width="18.01%" headers="mcps1.2.7.1.1 "><p id="p1351081715114"><a name="p1351081715114"></a><a name="p1351081715114"></a>rds048_disk_used_size</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.32%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0171122394_p38243505162117"><a name="en-us_topic_0171122394_p38243505162117"></a><a name="en-us_topic_0171122394_p38243505162117"></a>Used Storage Space</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.48%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0171122394_p10716207162117"><a name="en-us_topic_0171122394_p10716207162117"></a><a name="en-us_topic_0171122394_p10716207162117"></a>Used storage space of the monitored object</p>
    </td>
    <td class="cellrowborder" valign="top" width="9.4%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0171122394_p62706478162117"><a name="en-us_topic_0171122394_p62706478162117"></a><a name="en-us_topic_0171122394_p62706478162117"></a>0–4000 GB</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.94%" headers="mcps1.2.7.1.5 "><p id="p12840102285318"><a name="p12840102285318"></a><a name="p12840102285318"></a>Monitored object: ECS</p>
    <p id="p208405228537"><a name="p208405228537"></a><a name="p208405228537"></a>Monitored instance type: Microsoft SQL Server instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="7.85%" headers="mcps1.2.7.1.6 "><p id="p98408223532"><a name="p98408223532"></a><a name="p98408223532"></a>1 minute</p>
    </td>
    </tr>
    <tr id="en-us_topic_0171122394_row1111897216238"><td class="cellrowborder" valign="top" width="18.01%" headers="mcps1.2.7.1.1 "><p id="p185101817165120"><a name="p185101817165120"></a><a name="p185101817165120"></a>rds053_avg_disk_queue_length</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.32%" headers="mcps1.2.7.1.2 "><p id="en-us_topic_0171122394_p2822150916238"><a name="en-us_topic_0171122394_p2822150916238"></a><a name="en-us_topic_0171122394_p2822150916238"></a>Average Disk Queue Length</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.48%" headers="mcps1.2.7.1.3 "><p id="en-us_topic_0171122394_p424085416238"><a name="en-us_topic_0171122394_p424085416238"></a><a name="en-us_topic_0171122394_p424085416238"></a>Number of processes to be written into the monitored object</p>
    </td>
    <td class="cellrowborder" valign="top" width="9.4%" headers="mcps1.2.7.1.4 "><p id="en-us_topic_0171122394_p796488816238"><a name="en-us_topic_0171122394_p796488816238"></a><a name="en-us_topic_0171122394_p796488816238"></a>≥ 0</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.94%" headers="mcps1.2.7.1.5 "><p id="p084020224533"><a name="p084020224533"></a><a name="p084020224533"></a>Monitored object: ECS</p>
    <p id="p1840122135313"><a name="p1840122135313"></a><a name="p1840122135313"></a>Monitored instance type: Microsoft SQL Server instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="7.85%" headers="mcps1.2.7.1.6 "><p id="p1284172216534"><a name="p1284172216534"></a><a name="p1284172216534"></a>1 minute</p>
    </td>
    </tr>
    </tbody>
    </table>

-   [Table 2](#table46701376141844)  lists the performance metrics of Microsoft SQL Server databases.

    **Table  2**  Database performance metrics

    <a name="table46701376141844"></a>
    <table><thead align="left"><tr id="re01f141cc21347af98381c27e1a5d524"><th class="cellrowborder" valign="top" width="13.131313131313133%" id="mcps1.2.7.1.1"><p id="a807246cff23b44219a7b4ecb8436420f"><a name="a807246cff23b44219a7b4ecb8436420f"></a><a name="a807246cff23b44219a7b4ecb8436420f"></a>Metric ID</p>
    </th>
    <th class="cellrowborder" valign="top" width="12.121212121212121%" id="mcps1.2.7.1.2"><p id="en-us_topic_0029128243_p468860223835"><a name="en-us_topic_0029128243_p468860223835"></a><a name="en-us_topic_0029128243_p468860223835"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.202020202020204%" id="mcps1.2.7.1.3"><p id="a8bcd5efa9ee44b9ea636cef5aa688a8f"><a name="a8bcd5efa9ee44b9ea636cef5aa688a8f"></a><a name="a8bcd5efa9ee44b9ea636cef5aa688a8f"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.131313131313133%" id="mcps1.2.7.1.4"><p id="a8653133d56124b96a4e0fff4e8f62019"><a name="a8653133d56124b96a4e0fff4e8f62019"></a><a name="a8653133d56124b96a4e0fff4e8f62019"></a>Value Range</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.21212121212121%" id="mcps1.2.7.1.5"><p id="a762d63ea73c943f5977b57d80ca121d7"><a name="a762d63ea73c943f5977b57d80ca121d7"></a><a name="a762d63ea73c943f5977b57d80ca121d7"></a>Monitored Object</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.202020202020204%" id="mcps1.2.7.1.6"><p id="p19014326319"><a name="p19014326319"></a><a name="p19014326319"></a>Monitoring Interval (Raw Data)</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="ra9c1d6eb3b56483d8a8838e74d31e642"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.7.1.1 "><p id="aa1c7ecf3758444d4bc8e8f06b897fa96"><a name="aa1c7ecf3758444d4bc8e8f06b897fa96"></a><a name="aa1c7ecf3758444d4bc8e8f06b897fa96"></a>rds001_cpu_util</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.7.1.2 "><p id="a47e9c5cfd53542d5ab746dd1f2cb090e"><a name="a47e9c5cfd53542d5ab746dd1f2cb090e"></a><a name="a47e9c5cfd53542d5ab746dd1f2cb090e"></a>CPU Usage</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.7.1.3 "><p id="a8bbe05cb232b4427b2447d1fc478222e"><a name="a8bbe05cb232b4427b2447d1fc478222e"></a><a name="a8bbe05cb232b4427b2447d1fc478222e"></a>CPU usage of the monitored object</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.7.1.4 "><p id="acc6eb79dd02047ffbc26cf17e20f38cb"><a name="acc6eb79dd02047ffbc26cf17e20f38cb"></a><a name="acc6eb79dd02047ffbc26cf17e20f38cb"></a>0-100%</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.7.1.5 "><p id="p661919306546"><a name="p661919306546"></a><a name="p661919306546"></a>Monitored object: ECS</p>
    <p id="p45641326164812"><a name="p45641326164812"></a><a name="p45641326164812"></a>Monitored instance type: Microsoft SQL Server instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.7.1.6 "><p id="p1190193215314"><a name="p1190193215314"></a><a name="p1190193215314"></a>1 minute</p>
    </td>
    </tr>
    <tr id="rbf6d226456694af083a40de12dbb93cd"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.7.1.1 "><p id="acfa39719774349a2b4be04f612b28e6e"><a name="acfa39719774349a2b4be04f612b28e6e"></a><a name="acfa39719774349a2b4be04f612b28e6e"></a>rds002_mem_util</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.7.1.2 "><p id="a17120aa5ab7448629c4828548e9ff996"><a name="a17120aa5ab7448629c4828548e9ff996"></a><a name="a17120aa5ab7448629c4828548e9ff996"></a>Memory Usage</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.7.1.3 "><p id="a775c60966f644266948c79c107fa37e8"><a name="a775c60966f644266948c79c107fa37e8"></a><a name="a775c60966f644266948c79c107fa37e8"></a>Memory usage of the monitored object</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.7.1.4 "><p id="a9c00a0a9619443a58af65a447c164a57"><a name="a9c00a0a9619443a58af65a447c164a57"></a><a name="a9c00a0a9619443a58af65a447c164a57"></a>0–1</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.7.1.5 "><p id="p426711115511"><a name="p426711115511"></a><a name="p426711115511"></a>Monitored object: ECS</p>
    <p id="p426701125517"><a name="p426701125517"></a><a name="p426701125517"></a>Monitored instance type: Microsoft SQL Server instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.7.1.6 "><p id="p69093263116"><a name="p69093263116"></a><a name="p69093263116"></a>1 minute</p>
    </td>
    </tr>
    <tr id="r3cea26498b3447b9a3ead17476c7c422"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.7.1.1 "><p id="abe14ba68980e460183ba7bfe0f78f493"><a name="abe14ba68980e460183ba7bfe0f78f493"></a><a name="abe14ba68980e460183ba7bfe0f78f493"></a>rds003_iops</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.7.1.2 "><p id="a8677e88f532e4667957cfe5c142c3eb4"><a name="a8677e88f532e4667957cfe5c142c3eb4"></a><a name="a8677e88f532e4667957cfe5c142c3eb4"></a>IOPS</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.7.1.3 "><p id="adcfc613b104e4bbdb236107c7983f544"><a name="adcfc613b104e4bbdb236107c7983f544"></a><a name="adcfc613b104e4bbdb236107c7983f544"></a>Average number of I/O requests processed by the system in a specified period</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.7.1.4 "><p id="a9bd3d08b7e79414c9b05faac03f0e760"><a name="a9bd3d08b7e79414c9b05faac03f0e760"></a><a name="a9bd3d08b7e79414c9b05faac03f0e760"></a>≥ 0 counts/s</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.7.1.5 "><p id="p06061714195512"><a name="p06061714195512"></a><a name="p06061714195512"></a>Monitored object: ECS</p>
    <p id="p1160616144558"><a name="p1160616144558"></a><a name="p1160616144558"></a>Monitored instance type: Microsoft SQL Server instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.7.1.6 "><p id="p1291632113116"><a name="p1291632113116"></a><a name="p1291632113116"></a>1 minute</p>
    </td>
    </tr>
    <tr id="r1069941e6a9b4463863c575cb9291d1e"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.7.1.1 "><p id="ae6176ccfa03a4e18a930e91c5e463fff"><a name="ae6176ccfa03a4e18a930e91c5e463fff"></a><a name="ae6176ccfa03a4e18a930e91c5e463fff"></a>rds004_bytes_in</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.7.1.2 "><p id="a065095b14e394d4b9d85d3b8d9006c0d"><a name="a065095b14e394d4b9d85d3b8d9006c0d"></a><a name="a065095b14e394d4b9d85d3b8d9006c0d"></a>Network Input Throughput</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.7.1.3 "><p id="ae29cadcafee44fd284f88747e1bab9ea"><a name="ae29cadcafee44fd284f88747e1bab9ea"></a><a name="ae29cadcafee44fd284f88747e1bab9ea"></a>Incoming traffic in bytes per second</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.7.1.4 "><p id="a3c8adbfbc01f412bb9b939d7cf4402b0"><a name="a3c8adbfbc01f412bb9b939d7cf4402b0"></a><a name="a3c8adbfbc01f412bb9b939d7cf4402b0"></a>≥ 0 bytes/s</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.7.1.5 "><p id="p1589016285555"><a name="p1589016285555"></a><a name="p1589016285555"></a>Monitored object: ECS</p>
    <p id="p1189062818559"><a name="p1189062818559"></a><a name="p1189062818559"></a>Monitored instance type: Microsoft SQL Server instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.7.1.6 "><p id="p1091932183113"><a name="p1091932183113"></a><a name="p1091932183113"></a>1 minute</p>
    </td>
    </tr>
    <tr id="r9fbd096305194e6b8fca4826a3b597cc"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.7.1.1 "><p id="af9938a4483844a73b9ac48e277dff019"><a name="af9938a4483844a73b9ac48e277dff019"></a><a name="af9938a4483844a73b9ac48e277dff019"></a>rds005_bytes_out</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.7.1.2 "><p id="a6850346c502e421eba00563c83bdc417"><a name="a6850346c502e421eba00563c83bdc417"></a><a name="a6850346c502e421eba00563c83bdc417"></a>Network Output Throughput</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.7.1.3 "><p id="a8a416bbf839a442a857e6e647144ee09"><a name="a8a416bbf839a442a857e6e647144ee09"></a><a name="a8a416bbf839a442a857e6e647144ee09"></a>Outgoing traffic in bytes per second</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.7.1.4 "><p id="abd516c021d294e9383dc76012e2a61bb"><a name="abd516c021d294e9383dc76012e2a61bb"></a><a name="abd516c021d294e9383dc76012e2a61bb"></a>≥ 0 bytes/s</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.7.1.5 "><p id="p213263235516"><a name="p213263235516"></a><a name="p213263235516"></a>Monitored object: ECS</p>
    <p id="p513223215517"><a name="p513223215517"></a><a name="p513223215517"></a>Monitored instance type: Microsoft SQL Server instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.7.1.6 "><p id="p2911232103114"><a name="p2911232103114"></a><a name="p2911232103114"></a>1 minute</p>
    </td>
    </tr>
    <tr id="r9f98434644aa4bb1bf05e67fdd90c7b2"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.7.1.1 "><p id="a64be8ded9a174fc2b638a645164bb00b"><a name="a64be8ded9a174fc2b638a645164bb00b"></a><a name="a64be8ded9a174fc2b638a645164bb00b"></a>rds039_disk_util</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.7.1.2 "><p id="ac056999825234a86aeb1bde58f13e3ac"><a name="ac056999825234a86aeb1bde58f13e3ac"></a><a name="ac056999825234a86aeb1bde58f13e3ac"></a>Storage Space Usage</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.7.1.3 "><p id="a227244818c874d2bb5a6f63923d3a22b"><a name="a227244818c874d2bb5a6f63923d3a22b"></a><a name="a227244818c874d2bb5a6f63923d3a22b"></a>Storage space usage of the monitored object</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.7.1.4 "><p id="a621089c91a5e48b9a70bd2dc3b5ee82e"><a name="a621089c91a5e48b9a70bd2dc3b5ee82e"></a><a name="a621089c91a5e48b9a70bd2dc3b5ee82e"></a>0–1</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.7.1.5 "><p id="p553524320578"><a name="p553524320578"></a><a name="p553524320578"></a>Monitored object: ECS</p>
    <p id="p13535114335717"><a name="p13535114335717"></a><a name="p13535114335717"></a>Monitored instance type: Microsoft SQL Server instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.7.1.6 "><p id="p189117326313"><a name="p189117326313"></a><a name="p189117326313"></a>1 minute</p>
    </td>
    </tr>
    <tr id="row5950517415252"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.7.1.1 "><p id="p33965557151411"><a name="p33965557151411"></a><a name="p33965557151411"></a>rds047_disk_total_size</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.7.1.2 "><p id="p4325656715335"><a name="p4325656715335"></a><a name="p4325656715335"></a>Total Storage Space</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.7.1.3 "><p id="p1412103815335"><a name="p1412103815335"></a><a name="p1412103815335"></a>Total storage space of the monitored object</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.7.1.4 "><p id="p1878135135412"><a name="p1878135135412"></a><a name="p1878135135412"></a>40–4000 GB</p>
    <p id="p8725181468"><a name="p8725181468"></a><a name="p8725181468"></a></p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.7.1.5 "><p id="p17275995818"><a name="p17275995818"></a><a name="p17275995818"></a>Monitored object: ECS</p>
    <p id="p18727129105818"><a name="p18727129105818"></a><a name="p18727129105818"></a>Monitored instance type: Microsoft SQL Server instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.7.1.6 "><p id="p49133211312"><a name="p49133211312"></a><a name="p49133211312"></a>1 minute</p>
    </td>
    </tr>
    <tr id="row661168615252"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.7.1.1 "><p id="p64829489151411"><a name="p64829489151411"></a><a name="p64829489151411"></a>rds048_disk_used_size</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.7.1.2 "><p id="p556084315335"><a name="p556084315335"></a><a name="p556084315335"></a>Used Storage Space</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.7.1.3 "><p id="p4777512715335"><a name="p4777512715335"></a><a name="p4777512715335"></a>Used storage space of the monitored object</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.7.1.4 "><p id="p119971303217"><a name="p119971303217"></a><a name="p119971303217"></a>0–4000 GB</p>
    <p id="p26517211311"><a name="p26517211311"></a><a name="p26517211311"></a></p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.7.1.5 "><p id="p166871314125810"><a name="p166871314125810"></a><a name="p166871314125810"></a>Monitored object: ECS</p>
    <p id="p1768771435810"><a name="p1768771435810"></a><a name="p1768771435810"></a>Monitored instance type: Microsoft SQL Server instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.7.1.6 "><p id="p149119321317"><a name="p149119321317"></a><a name="p149119321317"></a>1 minute</p>
    </td>
    </tr>
    <tr id="row73463115252"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.7.1.1 "><p id="p16057739151411"><a name="p16057739151411"></a><a name="p16057739151411"></a>rds049_disk_read_throughput</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.7.1.2 "><p id="p1815837015335"><a name="p1815837015335"></a><a name="p1815837015335"></a>Disk Read Throughput</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.7.1.3 "><p id="p6154185215335"><a name="p6154185215335"></a><a name="p6154185215335"></a>Number of bytes read from the disk per second</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.7.1.4 "><p id="p1883413515335"><a name="p1883413515335"></a><a name="p1883413515335"></a>≥ 0 bytes/s</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.7.1.5 "><p id="p1642711895813"><a name="p1642711895813"></a><a name="p1642711895813"></a>Monitored object: ECS</p>
    <p id="p54273188583"><a name="p54273188583"></a><a name="p54273188583"></a>Monitored instance type: Microsoft SQL Server instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.7.1.6 "><p id="p4917320319"><a name="p4917320319"></a><a name="p4917320319"></a>1 minute</p>
    </td>
    </tr>
    <tr id="row1499470615252"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.7.1.1 "><p id="p29149396151411"><a name="p29149396151411"></a><a name="p29149396151411"></a>rds050_disk_write_throughput</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.7.1.2 "><p id="p3987662715335"><a name="p3987662715335"></a><a name="p3987662715335"></a>Disk Write Throughput</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.7.1.3 "><p id="p878135015335"><a name="p878135015335"></a><a name="p878135015335"></a>Number of bytes written into the disk per second</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.7.1.4 "><p id="p4020075815335"><a name="p4020075815335"></a><a name="p4020075815335"></a>≥ 0 bytes/s</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.7.1.5 "><p id="p239813222583"><a name="p239813222583"></a><a name="p239813222583"></a>Monitored object: ECS</p>
    <p id="p23989221585"><a name="p23989221585"></a><a name="p23989221585"></a>Monitored instance type: Microsoft SQL Server instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.7.1.6 "><p id="p9911322315"><a name="p9911322315"></a><a name="p9911322315"></a>1 minute</p>
    </td>
    </tr>
    <tr id="row5386186115252"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.7.1.1 "><p id="p43508968151411"><a name="p43508968151411"></a><a name="p43508968151411"></a>rds075_avg_disk_sec_per_read</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.7.1.2 "><p id="p4688806115335"><a name="p4688806115335"></a><a name="p4688806115335"></a>Disk Read Time</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.7.1.3 "><p id="p3983661115335"><a name="p3983661115335"></a><a name="p3983661115335"></a>Average time required for each disk read in a specified period</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.7.1.4 "><p id="p554006515335"><a name="p554006515335"></a><a name="p554006515335"></a>&gt; 0 ms</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.7.1.5 "><p id="p2454202518583"><a name="p2454202518583"></a><a name="p2454202518583"></a>Monitored object: ECS</p>
    <p id="p174541625185817"><a name="p174541625185817"></a><a name="p174541625185817"></a>Monitored instance type: Microsoft SQL Server instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.7.1.6 "><p id="p11911326313"><a name="p11911326313"></a><a name="p11911326313"></a>1 minute</p>
    </td>
    </tr>
    <tr id="row1344119115252"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.7.1.1 "><p id="p42654571151411"><a name="p42654571151411"></a><a name="p42654571151411"></a>rds052_avg_disk_sec_per_write</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.7.1.2 "><p id="p1217626415335"><a name="p1217626415335"></a><a name="p1217626415335"></a>Disk Write Time</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.7.1.3 "><p id="p4675329015335"><a name="p4675329015335"></a><a name="p4675329015335"></a>Average time required for each disk write in a specified period</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.7.1.4 "><p id="p2892016115335"><a name="p2892016115335"></a><a name="p2892016115335"></a>&gt; 0s</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.7.1.5 "><p id="p33991929125817"><a name="p33991929125817"></a><a name="p33991929125817"></a>Monitored object: ECS</p>
    <p id="p193991229155817"><a name="p193991229155817"></a><a name="p193991229155817"></a>Monitored instance type: Microsoft SQL Server instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.7.1.6 "><p id="p18919326316"><a name="p18919326316"></a><a name="p18919326316"></a>1 minute</p>
    </td>
    </tr>
    <tr id="row3877616715252"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.7.1.1 "><p id="p23778695151411"><a name="p23778695151411"></a><a name="p23778695151411"></a>rds053_avg_disk_queue_length</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.7.1.2 "><p id="p1061468915335"><a name="p1061468915335"></a><a name="p1061468915335"></a>Average Disk Queue Length</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.7.1.3 "><p id="p5448348215335"><a name="p5448348215335"></a><a name="p5448348215335"></a>Number of processes to be written into the monitored object</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.7.1.4 "><p id="p5108595615335"><a name="p5108595615335"></a><a name="p5108595615335"></a>≥ 0</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.7.1.5 "><p id="p16246742115814"><a name="p16246742115814"></a><a name="p16246742115814"></a>Monitored object: ECS</p>
    <p id="p1124615427585"><a name="p1124615427585"></a><a name="p1124615427585"></a>Monitored instance type: Microsoft SQL Server instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.7.1.6 "><p id="p591123293120"><a name="p591123293120"></a><a name="p591123293120"></a>1 minute</p>
    </td>
    </tr>
    <tr id="row47120437144253"><td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.7.1.1 "><p id="p58659062144253"><a name="p58659062144253"></a><a name="p58659062144253"></a>rds054_db_connections_in_use</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.121212121212121%" headers="mcps1.2.7.1.2 "><p id="p33440013144342"><a name="p33440013144342"></a><a name="p33440013144342"></a>Database Connections in Use</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.7.1.3 "><p id="p24286561144342"><a name="p24286561144342"></a><a name="p24286561144342"></a>Number of database connections in use</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.7.1.4 "><p id="p21054425144342"><a name="p21054425144342"></a><a name="p21054425144342"></a>≥0 counts</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.21212121212121%" headers="mcps1.2.7.1.5 "><p id="p42739298144436"><a name="p42739298144436"></a><a name="p42739298144436"></a>Monitored object: database</p>
    <p id="p49109367144436"><a name="p49109367144436"></a><a name="p49109367144436"></a>Monitored instance type: Microsoft SQL Server instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.202020202020204%" headers="mcps1.2.7.1.6 "><p id="p1191153216316"><a name="p1191153216316"></a><a name="p1191153216316"></a>1 minute</p>
    </td>
    </tr>
    </tbody>
    </table>


## Dimension<a name="section0114351005"></a>

<a name="table20447661154756"></a>
<table><thead align="left"><tr id="row58418561154756"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p34282994154756"><a name="p34282994154756"></a><a name="p34282994154756"></a>Key</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p25459095154756"><a name="p25459095154756"></a><a name="p25459095154756"></a>Value</p>
</th>
</tr>
</thead>
<tbody><tr id="row66237070144518"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p63602487144518"><a name="p63602487144518"></a><a name="p63602487144518"></a>rds_instance_sqlserver_id</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p51527828144518"><a name="p51527828144518"></a><a name="p51527828144518"></a>Microsoft SQL Server DB instance ID</p>
</td>
</tr>
</tbody>
</table>


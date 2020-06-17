# Querying Monitoring Data<a name="EN-US_TOPIC_0171212608"></a>

## Function<a name="section66578044"></a>

This API is used to query the monitoring data at a specified granularity for a specified metric in a specified period of time. You can specify the dimension of data to be queried.

## URI<a name="section62331491"></a>

GET /V1.0/\{project\_id\}/metric-data?namespace=\{namespace\}&metric\_name=\{metric\_name\}&dim.\{i\}=key,value&from=\{from\}&to=\{to\}&period=\{period\}&filter=\{filter\}

-   Parameter description

    **Table  1**  Parameter description

    <a name="table75058417558"></a>
    <table><thead align="left"><tr id="row6325008217558"><th class="cellrowborder" valign="top" width="18.67%" id="mcps1.2.4.1.1"><p id="p2298303317558"><a name="p2298303317558"></a><a name="p2298303317558"></a><strong id="b842352706181027"><a name="b842352706181027"></a><a name="b842352706181027"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="30.520000000000003%" id="mcps1.2.4.1.2"><p id="p4968641317558"><a name="p4968641317558"></a><a name="p4968641317558"></a><strong id="b842352706181047"><a name="b842352706181047"></a><a name="b842352706181047"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.81%" id="mcps1.2.4.1.3"><p id="p6517651717558"><a name="p6517651717558"></a><a name="p6517651717558"></a><strong id="b842352706181042"><a name="b842352706181042"></a><a name="b842352706181042"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4480653817558"><td class="cellrowborder" valign="top" width="18.67%" headers="mcps1.2.4.1.1 "><p id="p545094717558"><a name="p545094717558"></a><a name="p545094717558"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.520000000000003%" headers="mcps1.2.4.1.2 "><p id="p3887356117558"><a name="p3887356117558"></a><a name="p3887356117558"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.81%" headers="mcps1.2.4.1.3 "><p id="p6175070717558"><a name="p6175070717558"></a><a name="p6175070717558"></a>Specifies the project ID.</p>
    <p id="p875712401269"><a name="p875712401269"></a><a name="p875712401269"></a>For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  Query parameter description

    <a name="table35416756"></a>
    <table><thead align="left"><tr id="row27598891"><th class="cellrowborder" valign="top" width="18.610000000000003%" id="mcps1.2.5.1.1"><p id="p20917673"><a name="p20917673"></a><a name="p20917673"></a><strong id="b842352706181055"><a name="b842352706181055"></a><a name="b842352706181055"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15.610000000000001%" id="mcps1.2.5.1.2"><p id="p16609919"><a name="p16609919"></a><a name="p16609919"></a><strong id="b84235270618110"><a name="b84235270618110"></a><a name="b84235270618110"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.470000000000002%" id="mcps1.2.5.1.3"><p id="p29058925163547"><a name="p29058925163547"></a><a name="p29058925163547"></a><strong id="b84235270618114"><a name="b84235270618114"></a><a name="b84235270618114"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="48.31%" id="mcps1.2.5.1.4"><p id="p3226198"><a name="p3226198"></a><a name="p3226198"></a><strong id="b84235270618118"><a name="b84235270618118"></a><a name="b84235270618118"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row59995477"><td class="cellrowborder" valign="top" width="18.610000000000003%" headers="mcps1.2.5.1.1 "><p id="p3900147595641"><a name="p3900147595641"></a><a name="p3900147595641"></a>namespace</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.610000000000001%" headers="mcps1.2.5.1.2 "><p id="p500289695641"><a name="p500289695641"></a><a name="p500289695641"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.470000000000002%" headers="mcps1.2.5.1.3 "><p id="p4962713163547"><a name="p4962713163547"></a><a name="p4962713163547"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.31%" headers="mcps1.2.5.1.4 "><p id="p12933146104119"><a name="p12933146104119"></a><a name="p12933146104119"></a>Specifies the namespace of a service. For example, see <a href="ecs-metrics.md#en-us_topic_0022067719_section24282572112133">Namespace</a> for ECS namespace.</p>
    <p id="p1529914911223"><a name="p1529914911223"></a><a name="p1529914911223"></a>The value must be in the <strong id="b764416333813"><a name="b764416333813"></a><a name="b764416333813"></a>service.item</strong> format and can contain 3 to 32 characters. <strong id="b1364443315817"><a name="b1364443315817"></a><a name="b1364443315817"></a>service</strong> and <strong id="b26453333818"><a name="b26453333818"></a><a name="b26453333818"></a>item</strong> must be a string that starts with a letter and contains only uppercase letters, lowercase letters, digits, and underscores (_).</p>
    </td>
    </tr>
    <tr id="row14620943"><td class="cellrowborder" valign="top" width="18.610000000000003%" headers="mcps1.2.5.1.1 "><p id="p280237695641"><a name="p280237695641"></a><a name="p280237695641"></a>metric_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.610000000000001%" headers="mcps1.2.5.1.2 "><p id="p2566588195641"><a name="p2566588195641"></a><a name="p2566588195641"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.470000000000002%" headers="mcps1.2.5.1.3 "><p id="p123650473169"><a name="p123650473169"></a><a name="p123650473169"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.31%" headers="mcps1.2.5.1.4 "><p id="p35943562"><a name="p35943562"></a><a name="p35943562"></a>Specifies the metric name. You can obtain the metric names of existing alarm rules by referring to <a href="querying-the-metric-list.md">Querying the Metric List</a>.</p>
    </td>
    </tr>
    <tr id="row55056607"><td class="cellrowborder" valign="top" width="18.610000000000003%" headers="mcps1.2.5.1.1 "><p id="p2518324095641"><a name="p2518324095641"></a><a name="p2518324095641"></a>from</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.610000000000001%" headers="mcps1.2.5.1.2 "><p id="p2657653695641"><a name="p2657653695641"></a><a name="p2657653695641"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.470000000000002%" headers="mcps1.2.5.1.3 "><p id="p12560965163547"><a name="p12560965163547"></a><a name="p12560965163547"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.31%" headers="mcps1.2.5.1.4 "><p id="p2108412215949"><a name="p2108412215949"></a><a name="p2108412215949"></a>Specifies the start time of the query.</p>
    <p id="p1203182115952"><a name="p1203182115952"></a><a name="p1203182115952"></a>The value is a UNIX timestamp and the unit is ms.</p>
    <p id="p2001192015106"><a name="p2001192015106"></a><a name="p2001192015106"></a>Set the value of <strong id="b3101363915106"><a name="b3101363915106"></a><a name="b3101363915106"></a>from</strong> to at least one period earlier than the current time.</p>
    <p id="p618971015101"><a name="p618971015101"></a><a name="p618971015101"></a>Rollup aggregates the raw data generated within a period to the start time of the period. Therefore, if values of <strong id="b5623298615101"><a name="b5623298615101"></a><a name="b5623298615101"></a>from</strong> and <strong id="b3633482715101"><a name="b3633482715101"></a><a name="b3633482715101"></a>to</strong> are within a period, the query result will be empty due to the rollup failure.</p>
    <p id="p34920383151010"><a name="p34920383151010"></a><a name="p34920383151010"></a>Take the 5-minute period as an example. If it is 10:35 now, the raw data generated between 10:30 and 10:35 will be aggregated to 10:30. Therefore, in this example, if the value of <strong id="b842352706171230"><a name="b842352706171230"></a><a name="b842352706171230"></a>period</strong> is 5 minutes, the value of <strong id="b842352706171445"><a name="b842352706171445"></a><a name="b842352706171445"></a>from</strong> should be 10:30 or earlier.</p>
    <div class="note" id="note9599005105534"><a name="note9599005105534"></a><a name="note9599005105534"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p19282181105534"><a name="p19282181105534"></a><a name="p19282181105534"></a>Cloud Eye rounds up the value of <strong id="b842352706171848"><a name="b842352706171848"></a><a name="b842352706171848"></a>from</strong> based on the level of granularity required to perform the rollup.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row6114302"><td class="cellrowborder" valign="top" width="18.610000000000003%" headers="mcps1.2.5.1.1 "><p id="p4423458695641"><a name="p4423458695641"></a><a name="p4423458695641"></a>to</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.610000000000001%" headers="mcps1.2.5.1.2 "><p id="p2623169995641"><a name="p2623169995641"></a><a name="p2623169995641"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.470000000000002%" headers="mcps1.2.5.1.3 "><p id="p10805270163547"><a name="p10805270163547"></a><a name="p10805270163547"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.31%" headers="mcps1.2.5.1.4 "><p id="p15132095151021"><a name="p15132095151021"></a><a name="p15132095151021"></a>Specifies the end time of the query.</p>
    <p id="p14253410151029"><a name="p14253410151029"></a><a name="p14253410151029"></a>The value is a UNIX timestamp and the unit is ms.</p>
    <p id="p22491901151010"><a name="p22491901151010"></a><a name="p22491901151010"></a>The value of parameter <strong id="b5146242315922"><a name="b5146242315922"></a><a name="b5146242315922"></a>from</strong> must be earlier than that of parameter <strong id="b6050863115922"><a name="b6050863115922"></a><a name="b6050863115922"></a>to</strong>.</p>
    </td>
    </tr>
    <tr id="row18700393"><td class="cellrowborder" valign="top" width="18.610000000000003%" headers="mcps1.2.5.1.1 "><p id="p1593206195641"><a name="p1593206195641"></a><a name="p1593206195641"></a>period</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.610000000000001%" headers="mcps1.2.5.1.2 "><p id="p1542856995641"><a name="p1542856995641"></a><a name="p1542856995641"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.470000000000002%" headers="mcps1.2.5.1.3 "><p id="p1276519458171"><a name="p1276519458171"></a><a name="p1276519458171"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.31%" headers="mcps1.2.5.1.4 "><p id="p4175457395641"><a name="p4175457395641"></a><a name="p4175457395641"></a>Specifies the data monitoring granularity.</p>
    <p id="p4024684495641"><a name="p4024684495641"></a><a name="p4024684495641"></a>The value can be:</p>
    <a name="ul22530818141337"></a><a name="ul22530818141337"></a><ul id="ul22530818141337"><li><strong id="b66448307151643"><a name="b66448307151643"></a><a name="b66448307151643"></a>1</strong>: The data is monitored in real time.</li></ul>
    <a name="ul5025435916374"></a><a name="ul5025435916374"></a><ul id="ul5025435916374"><li><strong id="b62644269151643"><a name="b62644269151643"></a><a name="b62644269151643"></a>300</strong>: The data monitoring granularity is 5 minutes.</li><li><strong id="b32331302151643"><a name="b32331302151643"></a><a name="b32331302151643"></a>1200</strong>: The data monitoring granularity is 20 minutes.</li><li><strong id="b5763828151838"><a name="b5763828151838"></a><a name="b5763828151838"></a>3600</strong>: The data monitoring granularity is 1 hour.</li><li><strong id="b62926040151853"><a name="b62926040151853"></a><a name="b62926040151853"></a>14400</strong>: The data monitoring granularity is 4 hours.</li><li><strong id="b48617980151911"><a name="b48617980151911"></a><a name="b48617980151911"></a>86400</strong>: The data monitoring granularity is 1 day.</li></ul>
    </td>
    </tr>
    <tr id="row21724664"><td class="cellrowborder" valign="top" width="18.610000000000003%" headers="mcps1.2.5.1.1 "><p id="p5033039295641"><a name="p5033039295641"></a><a name="p5033039295641"></a>filter</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.610000000000001%" headers="mcps1.2.5.1.2 "><p id="p5022994295641"><a name="p5022994295641"></a><a name="p5022994295641"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.470000000000002%" headers="mcps1.2.5.1.3 "><p id="p95857523172"><a name="p95857523172"></a><a name="p95857523172"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.31%" headers="mcps1.2.5.1.4 "><p id="p4209350595641"><a name="p4209350595641"></a><a name="p4209350595641"></a>Specifies the data rollup method. The following methods are supported:</p>
    <a name="en-us_topic_0046434864_ul7891893153925"></a><a name="en-us_topic_0046434864_ul7891893153925"></a><ul id="en-us_topic_0046434864_ul7891893153925"><li>If <strong id="en-us_topic_0046434864_b5330590614237"><a name="en-us_topic_0046434864_b5330590614237"></a><a name="en-us_topic_0046434864_b5330590614237"></a>Avg.</strong> is selected for <strong id="en-us_topic_0046434864_b842352706111146"><a name="en-us_topic_0046434864_b842352706111146"></a><a name="en-us_topic_0046434864_b842352706111146"></a>Statistic</strong>, Cloud Eye calculates the average value of metric data within a rollup period.</li><li>If <strong id="b3999694114240"><a name="b3999694114240"></a><a name="b3999694114240"></a>Max.</strong> is selected for <strong id="b84235270611127"><a name="b84235270611127"></a><a name="b84235270611127"></a>Statistic</strong>, Cloud Eye calculates the maximum value of metric data within a rollup period.</li><li>If <strong id="en-us_topic_0046434864_b6277481514244"><a name="en-us_topic_0046434864_b6277481514244"></a><a name="en-us_topic_0046434864_b6277481514244"></a>Min.</strong> is selected for <strong id="en-us_topic_0046434864_b44016678184214"><a name="en-us_topic_0046434864_b44016678184214"></a><a name="en-us_topic_0046434864_b44016678184214"></a>Statistic</strong>, Cloud Eye calculates the minimum value of metric data within a rollup period.</li><li>If <strong id="b17306269184214"><a name="b17306269184214"></a><a name="b17306269184214"></a>Sum</strong> is selected for <strong id="b21538696184214"><a name="b21538696184214"></a><a name="b21538696184214"></a>Statistic</strong>, Cloud Eye calculates the sum of metric data within a rollup period.</li><li>If <strong id="b842352706111313"><a name="b842352706111313"></a><a name="b842352706111313"></a>Variance</strong> is selected for <strong id="b842352706111316"><a name="b842352706111316"></a><a name="b842352706111316"></a>Statistic</strong>, Cloud Eye calculates the variance value of metric data within a rollup period.</li></ul>
    <div class="note" id="en-us_topic_0046434864_note4729782611523"><a name="en-us_topic_0046434864_note4729782611523"></a><a name="en-us_topic_0046434864_note4729782611523"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0046434864_p42043046195213"><a name="en-us_topic_0046434864_p42043046195213"></a><a name="en-us_topic_0046434864_p42043046195213"></a>Rollup uses a rollup method to aggregate raw data generated within a specific period. Take the 5-minute period as an example. If it is 10:35 now, the raw data generated between 10:30 and 10:35 will be aggregated to 10:30.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row6189824095632"><td class="cellrowborder" valign="top" width="18.610000000000003%" headers="mcps1.2.5.1.1 "><p id="p6296468095641"><a name="p6296468095641"></a><a name="p6296468095641"></a>dim</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.610000000000001%" headers="mcps1.2.5.1.2 "><p id="p6697434595641"><a name="p6697434595641"></a><a name="p6697434595641"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.470000000000002%" headers="mcps1.2.5.1.3 "><p id="p136772055161716"><a name="p136772055161716"></a><a name="p136772055161716"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.31%" headers="mcps1.2.5.1.4 "><p id="p5555162513185"><a name="p5555162513185"></a><a name="p5555162513185"></a>Currently, a maximum of three metric dimensions are supported, and the dimensions are numbered from 0 in the <strong id="b945954991816"><a name="b945954991816"></a><a name="b945954991816"></a>dim.{i}=key,value</strong> format. The <strong id="b7459949111818"><a name="b7459949111818"></a><a name="b7459949111818"></a>key</strong> cannot exceed 32 characters and the <strong id="b645974951818"><a name="b645974951818"></a><a name="b645974951818"></a>value</strong> cannot exceed 256 characters.</p>
    <p id="p8712204312479"><a name="p8712204312479"></a><a name="p8712204312479"></a>The following dimensions are only examples. For details about dimensions of each service, see the description of each service, for example, instance_id of the ECS in <a href="ecs-metrics.md#en-us_topic_0022067719_section36963297112133">Dimension</a>.</p>
    <p id="p5621290395641"><a name="p5621290395641"></a><a name="p5621290395641"></a>Single dimension: <strong id="b334134417119"><a name="b334134417119"></a><a name="b334134417119"></a>dim.0=instance_id,i-12345</strong></p>
    <p id="p20992145915"><a name="p20992145915"></a><a name="p20992145915"></a>Multiple dimensions: <strong id="b6401112910594"><a name="b6401112910594"></a><a name="b6401112910594"></a>dim.0=instance_id,i-12345&amp;dim.1=instance_name,i-1234</strong></p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example:

    Request example 1: View the CPU usage of ECS whose ID is  **6f3c6f91-4b24-4e1b-b7d1-a94ac1cb011d**  from 2019-04-30 20:00:00 to 2019-04-30 22:00:00. The monitoring interval is 20 minutes.

    ```
    GET https://{Cloud Eye endpoint}/V1.0/{project_id}/metric-data?namespace=SYS.ECS&metric_name=cpu_util&dim.0=instance_id,6f3c6f91-4b24-4e1b-b7d1-a94ac1cb011d&from=1556625600000&to=1556632800000&period=1200&filter=min
    ```


## Request<a name="section24112512"></a>

None

## Response<a name="section15686020"></a>

-   Response parameters

    **Table  3**  Response parameters

    <a name="table6357015152815"></a>
    <table><thead align="left"><tr id="row57952149152815"><th class="cellrowborder" valign="top" width="21.40785921407859%" id="mcps1.2.4.1.1"><p id="p63612496152815"><a name="p63612496152815"></a><a name="p63612496152815"></a><strong id="b842352706181120"><a name="b842352706181120"></a><a name="b842352706181120"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15.14848515148485%" id="mcps1.2.4.1.2"><p id="p11562283152815"><a name="p11562283152815"></a><a name="p11562283152815"></a><strong id="b842352706181128"><a name="b842352706181128"></a><a name="b842352706181128"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="63.44365563443656%" id="mcps1.2.4.1.3"><p id="p64129691152815"><a name="p64129691152815"></a><a name="p64129691152815"></a><strong id="b842352706181132"><a name="b842352706181132"></a><a name="b842352706181132"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row27122455152815"><td class="cellrowborder" valign="top" width="21.40785921407859%" headers="mcps1.2.4.1.1 "><p id="p49435272152815"><a name="p49435272152815"></a><a name="p49435272152815"></a>datapoints</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.14848515148485%" headers="mcps1.2.4.1.2 "><p id="p18618155512194"><a name="p18618155512194"></a><a name="p18618155512194"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.44365563443656%" headers="mcps1.2.4.1.3 "><p id="p226620208334"><a name="p226620208334"></a><a name="p226620208334"></a>Specifies the metric data list. For details, see <a href="#table1017018361914">Table 4</a>.</p>
    <p id="p40931000151127"><a name="p40931000151127"></a><a name="p40931000151127"></a></p>
    <p id="p12932214151010"><a name="p12932214151010"></a><a name="p12932214151010"></a>Since Cloud Eye rounds up the value of <strong id="b1473920010172743"><a name="b1473920010172743"></a><a name="b1473920010172743"></a>from</strong> based on the level of granularity for data query, <strong id="b842352706173039"><a name="b842352706173039"></a><a name="b842352706173039"></a>datapoints</strong> may contain more data points than expected.</p>
    </td>
    </tr>
    <tr id="row13930709152815"><td class="cellrowborder" valign="top" width="21.40785921407859%" headers="mcps1.2.4.1.1 "><p id="p54645615152815"><a name="p54645615152815"></a><a name="p54645615152815"></a>metric_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.14848515148485%" headers="mcps1.2.4.1.2 "><p id="p34330385152815"><a name="p34330385152815"></a><a name="p34330385152815"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.44365563443656%" headers="mcps1.2.4.1.3 "><p id="p686919215492"><a name="p686919215492"></a><a name="p686919215492"></a>Specifies the metric ID. For example, if the <a href="ecs-metrics.md">monitoring metric</a> of an ECS is CPU usage, <strong id="b67869407135"><a name="b67869407135"></a><a name="b67869407135"></a>metric_name</strong> is <strong id="b12786740201319"><a name="b12786740201319"></a><a name="b12786740201319"></a>cpu_util</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **datapoints**  field data structure description

    <a name="table1017018361914"></a>
    <table><thead align="left"><tr id="row191717367119"><th class="cellrowborder" valign="top" width="21.40785921407859%" id="mcps1.2.4.1.1"><p id="p121712368117"><a name="p121712368117"></a><a name="p121712368117"></a><strong id="b842352706181027_1"><a name="b842352706181027_1"></a><a name="b842352706181027_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15.14848515148485%" id="mcps1.2.4.1.2"><p id="p817112361619"><a name="p817112361619"></a><a name="p817112361619"></a><strong id="b842352706181128_1"><a name="b842352706181128_1"></a><a name="b842352706181128_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="63.44365563443656%" id="mcps1.2.4.1.3"><p id="p1117115361718"><a name="p1117115361718"></a><a name="p1117115361718"></a><strong id="b842352706181042_1"><a name="b842352706181042_1"></a><a name="b842352706181042_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row151712361114"><td class="cellrowborder" valign="top" width="21.40785921407859%" headers="mcps1.2.4.1.1 "><p id="p1417110364118"><a name="p1417110364118"></a><a name="p1417110364118"></a>max/min/average/sum/variance</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.14848515148485%" headers="mcps1.2.4.1.2 "><p id="p8319164091818"><a name="p8319164091818"></a><a name="p8319164091818"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.44365563443656%" headers="mcps1.2.4.1.3 "><p id="p121723361416"><a name="p121723361416"></a><a name="p121723361416"></a>Specifies the metric value. The value of this parameter is the same as that of parameter <strong id="b2580930427"><a name="b2580930427"></a><a name="b2580930427"></a>filter</strong>.</p>
    </td>
    </tr>
    <tr id="row717213617112"><td class="cellrowborder" valign="top" width="21.40785921407859%" headers="mcps1.2.4.1.1 "><p id="p111724365117"><a name="p111724365117"></a><a name="p111724365117"></a>timestamp</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.14848515148485%" headers="mcps1.2.4.1.2 "><p id="p733112331188"><a name="p733112331188"></a><a name="p733112331188"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.44365563443656%" headers="mcps1.2.4.1.3 "><p id="p141721536817"><a name="p141721536817"></a><a name="p141721536817"></a>Specifies the time when the metric is collected. It is a UNIX timestamp in milliseconds.</p>
    </td>
    </tr>
    <tr id="row1317218367116"><td class="cellrowborder" valign="top" width="21.40785921407859%" headers="mcps1.2.4.1.1 "><p id="p717211364117"><a name="p717211364117"></a><a name="p717211364117"></a>unit</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.14848515148485%" headers="mcps1.2.4.1.2 "><p id="p317219361713"><a name="p317219361713"></a><a name="p317219361713"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.44365563443656%" headers="mcps1.2.4.1.3 "><p id="p617218361216"><a name="p617218361216"></a><a name="p617218361216"></a>Specifies the metric unit.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "datapoints": [
            {
                "average": 0, 
                "timestamp": 1442341200000, 
                "unit": "Count"
            }
        ], 
        "metric_name": "cpu_util"
    }
    ```


## Returned Values<a name="section6956456"></a>

-   Normal

    200

-   Abnormal

    <a name="table46793998"></a>
    <table><thead align="left"><tr id="row65573909"><th class="cellrowborder" valign="top" width="33.08%" id="mcps1.1.3.1.1"><p id="p1849030182924"><a name="p1849030182924"></a><a name="p1849030182924"></a><strong id="b842352706181143"><a name="b842352706181143"></a><a name="b842352706181143"></a>Returned Values</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="66.92%" id="mcps1.1.3.1.2"><p id="p15553712182924"><a name="p15553712182924"></a><a name="p15553712182924"></a><strong id="b842352706181147"><a name="b842352706181147"></a><a name="b842352706181147"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row37564172"><td class="cellrowborder" valign="top" width="33.08%" headers="mcps1.1.3.1.1 "><p id="p581987519168"><a name="p581987519168"></a><a name="p581987519168"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.92%" headers="mcps1.1.3.1.2 "><p id="p164784039168"><a name="p164784039168"></a><a name="p164784039168"></a>Request error</p>
    </td>
    </tr>
    <tr id="row66248115"><td class="cellrowborder" valign="top" width="33.08%" headers="mcps1.1.3.1.1 "><p id="p2691669168"><a name="p2691669168"></a><a name="p2691669168"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.92%" headers="mcps1.1.3.1.2 "><p id="p218024949168"><a name="p218024949168"></a><a name="p218024949168"></a>The authentication information is not provided or is incorrect.</p>
    </td>
    </tr>
    <tr id="row44282627"><td class="cellrowborder" valign="top" width="33.08%" headers="mcps1.1.3.1.1 "><p id="p563264059168"><a name="p563264059168"></a><a name="p563264059168"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.92%" headers="mcps1.1.3.1.2 "><p id="p661449719168"><a name="p661449719168"></a><a name="p661449719168"></a>You are forbidden to access the page requested.</p>
    </td>
    </tr>
    <tr id="row1815156"><td class="cellrowborder" valign="top" width="33.08%" headers="mcps1.1.3.1.1 "><p id="p355199299168"><a name="p355199299168"></a><a name="p355199299168"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.92%" headers="mcps1.1.3.1.2 "><p id="p585420329168"><a name="p585420329168"></a><a name="p585420329168"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row25675773"><td class="cellrowborder" valign="top" width="33.08%" headers="mcps1.1.3.1.1 "><p id="p630127129168"><a name="p630127129168"></a><a name="p630127129168"></a>429 Too Many Requests</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.92%" headers="mcps1.1.3.1.2 "><p id="p37560249168"><a name="p37560249168"></a><a name="p37560249168"></a>Concurrent requests are excessive.</p>
    </td>
    </tr>
    <tr id="row47530006"><td class="cellrowborder" valign="top" width="33.08%" headers="mcps1.1.3.1.1 "><p id="p537873819168"><a name="p537873819168"></a><a name="p537873819168"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.92%" headers="mcps1.1.3.1.2 "><p id="p618106189168"><a name="p618106189168"></a><a name="p618106189168"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row20561848"><td class="cellrowborder" valign="top" width="33.08%" headers="mcps1.1.3.1.1 "><p id="p298930079168"><a name="p298930079168"></a><a name="p298930079168"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.92%" headers="mcps1.1.3.1.2 "><p id="p54144829168"><a name="p54144829168"></a><a name="p54144829168"></a>The service is currently unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Code<a name="section18702135964612"></a>

For details, see  [Error Codes](error-codes.md).


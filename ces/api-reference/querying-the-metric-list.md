# Querying the Metric List<a name="EN-US_TOPIC_0171212593"></a>

## Function<a name="section66578044"></a>

This API is used to query the metric list. You can specify the namespace, metric, dimension, sorting order, start records, and the maximum number of records when using this API to query metrics.

## URI<a name="section62331491"></a>

GET /V1.0/\{project\_id\}/metrics

-   Parameter description

    **Table  1**  Parameter description

    <a name="table35298993175334"></a>
    <table><thead align="left"><tr id="row56207076175334"><th class="cellrowborder" valign="top" width="20.792079207920793%" id="mcps1.2.4.1.1"><p id="p56479321175334"><a name="p56479321175334"></a><a name="p56479321175334"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.841584158415841%" id="mcps1.2.4.1.2"><p id="p11422274175334"><a name="p11422274175334"></a><a name="p11422274175334"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="63.366336633663366%" id="mcps1.2.4.1.3"><p id="p52789000175334"><a name="p52789000175334"></a><a name="p52789000175334"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row48050578175334"><td class="cellrowborder" valign="top" width="20.792079207920793%" headers="mcps1.2.4.1.1 "><p id="p66891592175334"><a name="p66891592175334"></a><a name="p66891592175334"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.2.4.1.2 "><p id="p49509908175334"><a name="p49509908175334"></a><a name="p49509908175334"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.366336633663366%" headers="mcps1.2.4.1.3 "><p id="p50879579175334"><a name="p50879579175334"></a><a name="p50879579175334"></a>Specifies the project ID.</p>
    <p id="p35013331952"><a name="p35013331952"></a><a name="p35013331952"></a>For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  Query parameter description

    <a name="table35416756"></a>
    <table><thead align="left"><tr id="row27598891"><th class="cellrowborder" valign="top" width="20.3%" id="mcps1.2.5.1.1"><p id="p20917673"><a name="p20917673"></a><a name="p20917673"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.6%" id="mcps1.2.5.1.2"><p id="p16609919"><a name="p16609919"></a><a name="p16609919"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.919999999999998%" id="mcps1.2.5.1.3"><p id="p3884242163044"><a name="p3884242163044"></a><a name="p3884242163044"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="47.18%" id="mcps1.2.5.1.4"><p id="p3226198"><a name="p3226198"></a><a name="p3226198"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row59995477"><td class="cellrowborder" valign="top" width="20.3%" headers="mcps1.2.5.1.1 "><p id="p27795493"><a name="p27795493"></a><a name="p27795493"></a>namespace</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.6%" headers="mcps1.2.5.1.2 "><p id="p36842478"><a name="p36842478"></a><a name="p36842478"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.5.1.3 "><p id="p46188171163044"><a name="p46188171163044"></a><a name="p46188171163044"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.18%" headers="mcps1.2.5.1.4 "><p id="p12933146104119"><a name="p12933146104119"></a><a name="p12933146104119"></a>Query the namespace of a service. For example, see <a href="ecs-metrics.md#en-us_topic_0022067719_section24282572112133">Namespace</a> for ECS namespace.</p>
    <p id="p1529914911223"><a name="p1529914911223"></a><a name="p1529914911223"></a>The value must be in the <strong id="b842352706195615"><a name="b842352706195615"></a><a name="b842352706195615"></a>service.item</strong> format and can contain 3 to 32 characters. <strong id="b842352706195450"><a name="b842352706195450"></a><a name="b842352706195450"></a>service</strong> and <strong id="b842352706195455"><a name="b842352706195455"></a><a name="b842352706195455"></a>item</strong> must be a string that starts with a letter and contains only uppercase letters, lowercase letters, digits, and underscores (_). </p>
    </td>
    </tr>
    <tr id="row14620943"><td class="cellrowborder" valign="top" width="20.3%" headers="mcps1.2.5.1.1 "><p id="p43445707"><a name="p43445707"></a><a name="p43445707"></a>metric_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.6%" headers="mcps1.2.5.1.2 "><p id="p29441404"><a name="p29441404"></a><a name="p29441404"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.5.1.3 "><p id="p50254369163044"><a name="p50254369163044"></a><a name="p50254369163044"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.18%" headers="mcps1.2.5.1.4 "><p id="p686919215492"><a name="p686919215492"></a><a name="p686919215492"></a>Specifies the metric ID. For example, if the <a href="ecs-metrics.md">monitoring metric</a> of an ECS is CPU usage, <strong id="b1235691017513"><a name="b1235691017513"></a><a name="b1235691017513"></a>metric_name</strong> is <strong id="b83568101353"><a name="b83568101353"></a><a name="b83568101353"></a>cpu_util</strong>.</p>
    </td>
    </tr>
    <tr id="row55056607"><td class="cellrowborder" valign="top" width="20.3%" headers="mcps1.2.5.1.1 "><p id="p30400195"><a name="p30400195"></a><a name="p30400195"></a>dim</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.6%" headers="mcps1.2.5.1.2 "><p id="p46496694"><a name="p46496694"></a><a name="p46496694"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.5.1.3 "><p id="p44072059163044"><a name="p44072059163044"></a><a name="p44072059163044"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.18%" headers="mcps1.2.5.1.4 "><p id="p132891013125316"><a name="p132891013125316"></a><a name="p132891013125316"></a>Specifies the monitoring dimension. For example, the <a href="ecs-metrics.md">monitoring dimension</a> of an ECS is instance_id.</p>
    <p id="p19158445162638"><a name="p19158445162638"></a><a name="p19158445162638"></a>Currently, a maximum of three metric dimensions are supported, and the dimensions are numbered from 0 in the <strong id="b15916112071517"><a name="b15916112071517"></a><a name="b15916112071517"></a>dim.{i}=key,value</strong> format. The <strong id="b10515162815168"><a name="b10515162815168"></a><a name="b10515162815168"></a>key</strong> cannot exceed 32 characters and the <strong id="b14722366168"><a name="b14722366168"></a><a name="b14722366168"></a>value</strong> cannot exceed 256 characters.</p>
    <p id="p8135907"><a name="p8135907"></a><a name="p8135907"></a>Single dimension: <strong id="b916844495712"><a name="b916844495712"></a><a name="b916844495712"></a>dim.0=instance_id,6f3c6f91-4b24-4e1b-b7d1-a94ac1cb011d</strong></p>
    <p id="p134693117211"><a name="p134693117211"></a><a name="p134693117211"></a>Multiple dimensions: <strong id="b35998583577"><a name="b35998583577"></a><a name="b35998583577"></a>dim.0=key,value&amp;dim.1=key,value</strong></p>
    </td>
    </tr>
    <tr id="row6114302"><td class="cellrowborder" valign="top" width="20.3%" headers="mcps1.2.5.1.1 "><p id="p25496434"><a name="p25496434"></a><a name="p25496434"></a>start</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.6%" headers="mcps1.2.5.1.2 "><p id="p51945267"><a name="p51945267"></a><a name="p51945267"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.5.1.3 "><p id="p13067009163044"><a name="p13067009163044"></a><a name="p13067009163044"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.18%" headers="mcps1.2.5.1.4 "><p id="p53938779205119"><a name="p53938779205119"></a><a name="p53938779205119"></a>Specifies the paging start value.</p>
    <p id="p3308015715032"><a name="p3308015715032"></a><a name="p3308015715032"></a>The format is <strong id="b27794473205024"><a name="b27794473205024"></a><a name="b27794473205024"></a>namespace.metric_name.key:value</strong>.</p>
    <p id="p62847380164456"><a name="p62847380164456"></a><a name="p62847380164456"></a>Example: <strong id="b33318075145433"><a name="b33318075145433"></a><a name="b33318075145433"></a>start=SYS.ECS.cpu_util.instance_id:d9112af5-6913-4f3b-bd0a-3f96711e004d</strong>.</p>
    </td>
    </tr>
    <tr id="row18700393"><td class="cellrowborder" valign="top" width="20.3%" headers="mcps1.2.5.1.1 "><p id="p38336904"><a name="p38336904"></a><a name="p38336904"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.6%" headers="mcps1.2.5.1.2 "><p id="p18281552"><a name="p18281552"></a><a name="p18281552"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.5.1.3 "><p id="p51794845163044"><a name="p51794845163044"></a><a name="p51794845163044"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.18%" headers="mcps1.2.5.1.4 "><p id="p4410728"><a name="p4410728"></a><a name="p4410728"></a>The value ranges from <strong id="b6013100620539"><a name="b6013100620539"></a><a name="b6013100620539"></a>1</strong> to <strong id="b25293232205313"><a name="b25293232205313"></a><a name="b25293232205313"></a>1000</strong>, and is <strong id="b6520879205318"><a name="b6520879205318"></a><a name="b6520879205318"></a>1000</strong> by default.</p>
    <p id="p39696553"><a name="p39696553"></a><a name="p39696553"></a>This parameter is used to limit the number of query results.</p>
    </td>
    </tr>
    <tr id="row21724664"><td class="cellrowborder" valign="top" width="20.3%" headers="mcps1.2.5.1.1 "><p id="p14867369"><a name="p14867369"></a><a name="p14867369"></a>order</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.6%" headers="mcps1.2.5.1.2 "><p id="p63406242"><a name="p63406242"></a><a name="p63406242"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.5.1.3 "><p id="p34632884163044"><a name="p34632884163044"></a><a name="p34632884163044"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.18%" headers="mcps1.2.5.1.4 "><p id="p35632012"><a name="p35632012"></a><a name="p35632012"></a>Specifies the result sorting method, which is sorted by timestamp.</p>
    <p id="p52252659"><a name="p52252659"></a><a name="p52252659"></a>The default value is <strong id="b27407972205024"><a name="b27407972205024"></a><a name="b27407972205024"></a>desc</strong>.</p>
    <a name="ul4241055916271"></a><a name="ul4241055916271"></a><ul id="ul4241055916271"><li><strong id="b56442258145930"><a name="b56442258145930"></a><a name="b56442258145930"></a>asc</strong>: The query results are displayed in the ascending order.</li><li><strong id="b54242000145945"><a name="b54242000145945"></a><a name="b54242000145945"></a>desc</strong>: The query results are displayed in the descending order.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    Request example 1: Query the list of all metrics that can be monitored.

    ```
    GET https://{Cloud Eye endpoint}/V1.0/{project_id}/metrics
    ```

    Request example 2: Query the CPU usage of the ECS whose ID is  **6f3c6f91-4b24-4e1b-b7d1-a94ac1cb011d**. Retain 10 records in descending order by timestamp.

    ```
    GET https://{Cloud Eye endpoint}/V1.0/{project_id}/metrics?namespace=SYS.ECS&metric_name=cpu_util&dim.0=instance_id,6f3c6f91-4b24-4e1b-b7d1-a94ac1cb011d&limit=10&order=desc
    ```


## Request<a name="section24112512"></a>

None

## Response<a name="section15686020"></a>

-   Response parameters

    **Table  3**  Response parameters

    <a name="table26246518152631"></a>
    <table><thead align="left"><tr id="row29602547152631"><th class="cellrowborder" valign="top" width="22.66%" id="mcps1.2.4.1.1"><p id="p48996072152631"><a name="p48996072152631"></a><a name="p48996072152631"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.869999999999997%" id="mcps1.2.4.1.2"><p id="p11771280152631"><a name="p11771280152631"></a><a name="p11771280152631"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="60.47%" id="mcps1.2.4.1.3"><p id="p13949586152631"><a name="p13949586152631"></a><a name="p13949586152631"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row39341340152631"><td class="cellrowborder" valign="top" width="22.66%" headers="mcps1.2.4.1.1 "><p id="p32531944152631"><a name="p32531944152631"></a><a name="p32531944152631"></a>metrics</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.869999999999997%" headers="mcps1.2.4.1.2 "><p id="p35902407152631"><a name="p35902407152631"></a><a name="p35902407152631"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.47%" headers="mcps1.2.4.1.3 "><p id="p22413865152631"><a name="p22413865152631"></a><a name="p22413865152631"></a>Specifies the list of metric objects.</p>
    <p id="p9149533195013"><a name="p9149533195013"></a><a name="p9149533195013"></a>For details, see <a href="#table363011386367">Table 4</a>.</p>
    </td>
    </tr>
    <tr id="row398200152631"><td class="cellrowborder" valign="top" width="22.66%" headers="mcps1.2.4.1.1 "><p id="p185733280374"><a name="p185733280374"></a><a name="p185733280374"></a>meta_data</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.869999999999997%" headers="mcps1.2.4.1.2 "><p id="p20573192843719"><a name="p20573192843719"></a><a name="p20573192843719"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.47%" headers="mcps1.2.4.1.3 "><p id="p8573192811378"><a name="p8573192811378"></a><a name="p8573192811378"></a>Specifies the metadata of query results, including the paging information.</p>
    <p id="p1991019716501"><a name="p1991019716501"></a><a name="p1991019716501"></a>For details, see <a href="#table2048015400368">Table 6</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **metrics**  field data structure description

    <a name="table363011386367"></a>
    <table><thead align="left"><tr id="row1463018384369"><th class="cellrowborder" valign="top" width="22.66%" id="mcps1.2.4.1.1"><p id="p8630738103611"><a name="p8630738103611"></a><a name="p8630738103611"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.869999999999997%" id="mcps1.2.4.1.2"><p id="p263020388366"><a name="p263020388366"></a><a name="p263020388366"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="60.47%" id="mcps1.2.4.1.3"><p id="p13630438133618"><a name="p13630438133618"></a><a name="p13630438133618"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row9632338163613"><td class="cellrowborder" valign="top" width="22.66%" headers="mcps1.2.4.1.1 "><p id="p2632938193619"><a name="p2632938193619"></a><a name="p2632938193619"></a>namespace</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.869999999999997%" headers="mcps1.2.4.1.2 "><p id="p8632538113612"><a name="p8632538113612"></a><a name="p8632538113612"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.47%" headers="mcps1.2.4.1.3 "><p id="p1163253814361"><a name="p1163253814361"></a><a name="p1163253814361"></a>Specifies the metric namespace.</p>
    </td>
    </tr>
    <tr id="row863393813366"><td class="cellrowborder" valign="top" width="22.66%" headers="mcps1.2.4.1.1 "><p id="p13633173883611"><a name="p13633173883611"></a><a name="p13633173883611"></a>dimensions</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.869999999999997%" headers="mcps1.2.4.1.2 "><p id="p17633238143612"><a name="p17633238143612"></a><a name="p17633238143612"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.47%" headers="mcps1.2.4.1.3 "><p id="p86333383365"><a name="p86333383365"></a><a name="p86333383365"></a>Specifies the list of the metric dimensions.</p>
    <p id="p034915531507"><a name="p034915531507"></a><a name="p034915531507"></a>For details, see <a href="#table2024213426364">Table 5</a>.</p>
    </td>
    </tr>
    <tr id="row131721037132313"><td class="cellrowborder" valign="top" width="22.66%" headers="mcps1.2.4.1.1 "><p id="p1632163814369"><a name="p1632163814369"></a><a name="p1632163814369"></a>metric_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.869999999999997%" headers="mcps1.2.4.1.2 "><p id="p17632143883613"><a name="p17632143883613"></a><a name="p17632143883613"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.47%" headers="mcps1.2.4.1.3 "><p id="p1963218384362"><a name="p1963218384362"></a><a name="p1963218384362"></a>Specifies the metric name, such as <strong id="b443035911204"><a name="b443035911204"></a><a name="b443035911204"></a>cpu_util</strong>.</p>
    </td>
    </tr>
    <tr id="row136801240152316"><td class="cellrowborder" valign="top" width="22.66%" headers="mcps1.2.4.1.1 "><p id="p76326384363"><a name="p76326384363"></a><a name="p76326384363"></a>unit</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.869999999999997%" headers="mcps1.2.4.1.2 "><p id="p86324389363"><a name="p86324389363"></a><a name="p86324389363"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.47%" headers="mcps1.2.4.1.3 "><p id="p156324389368"><a name="p156324389368"></a><a name="p156324389368"></a>Specifies the metric unit.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5** **dimensions**  field data structure description

    <a name="table2024213426364"></a>
    <table><thead align="left"><tr id="row1224234213619"><th class="cellrowborder" valign="top" width="22.66%" id="mcps1.2.4.1.1"><p id="p1524215426367"><a name="p1524215426367"></a><a name="p1524215426367"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.869999999999997%" id="mcps1.2.4.1.2"><p id="p1424394213614"><a name="p1424394213614"></a><a name="p1424394213614"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="60.47%" id="mcps1.2.4.1.3"><p id="p1324394263611"><a name="p1324394263611"></a><a name="p1324394263611"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2024612424367"><td class="cellrowborder" valign="top" width="22.66%" headers="mcps1.2.4.1.1 "><p id="p824618425365"><a name="p824618425365"></a><a name="p824618425365"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.869999999999997%" headers="mcps1.2.4.1.2 "><p id="p3246194283614"><a name="p3246194283614"></a><a name="p3246194283614"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.47%" headers="mcps1.2.4.1.3 "><p id="p19551520125012"><a name="p19551520125012"></a><a name="p19551520125012"></a>Specifies the monitoring dimension name. For example, the monitoring dimension of an ECS is <strong id="b16152043151920"><a name="b16152043151920"></a><a name="b16152043151920"></a>instance_id</strong>. For details, see the <strong id="b4152114391917"><a name="b4152114391917"></a><a name="b4152114391917"></a>key</strong> field in <a href="ecs-metrics.md#en-us_topic_0022067719_section36963297112133">Dimension</a>.</p>
    </td>
    </tr>
    <tr id="row20547244255"><td class="cellrowborder" valign="top" width="22.66%" headers="mcps1.2.4.1.1 "><p id="p5547124122511"><a name="p5547124122511"></a><a name="p5547124122511"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.869999999999997%" headers="mcps1.2.4.1.2 "><p id="p19547154122519"><a name="p19547154122519"></a><a name="p19547154122519"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.47%" headers="mcps1.2.4.1.3 "><p id="p11371113251615"><a name="p11371113251615"></a><a name="p11371113251615"></a>Specifies the dimension value, for example, an ECS ID.</p>
    <p id="p12480161492518"><a name="p12480161492518"></a><a name="p12480161492518"></a>The value is a string of one to 256 characters.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6** **meta\_data**  field data structure description

    <a name="table2048015400368"></a>
    <table><thead align="left"><tr id="row16481164019363"><th class="cellrowborder" valign="top" width="22.66%" id="mcps1.2.4.1.1"><p id="p14481194083615"><a name="p14481194083615"></a><a name="p14481194083615"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.869999999999997%" id="mcps1.2.4.1.2"><p id="p5481134019368"><a name="p5481134019368"></a><a name="p5481134019368"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="60.47%" id="mcps1.2.4.1.3"><p id="p3481740153611"><a name="p3481740153611"></a><a name="p3481740153611"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8481540153615"><td class="cellrowborder" valign="top" width="22.66%" headers="mcps1.2.4.1.1 "><p id="p13481174011361"><a name="p13481174011361"></a><a name="p13481174011361"></a>count</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.869999999999997%" headers="mcps1.2.4.1.2 "><p id="p134811140133617"><a name="p134811140133617"></a><a name="p134811140133617"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.47%" headers="mcps1.2.4.1.3 "><p id="p9481104053612"><a name="p9481104053612"></a><a name="p9481104053612"></a>Specifies the number of returned results.</p>
    </td>
    </tr>
    <tr id="row1248220406364"><td class="cellrowborder" valign="top" width="22.66%" headers="mcps1.2.4.1.1 "><p id="p748214015361"><a name="p748214015361"></a><a name="p748214015361"></a>marker</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.869999999999997%" headers="mcps1.2.4.1.2 "><p id="p13750151725818"><a name="p13750151725818"></a><a name="p13750151725818"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.47%" headers="mcps1.2.4.1.3 "><p id="p4482104043610"><a name="p4482104043610"></a><a name="p4482104043610"></a>Specifies the pagination marker.</p>
    <p id="p632235322917"><a name="p632235322917"></a><a name="p632235322917"></a>For example, you have queried 10 records this time and the tenth record is about <strong id="b20648210143212"><a name="b20648210143212"></a><a name="b20648210143212"></a>cpu_util</strong>. In your next query, if <strong id="b364411189325"><a name="b364411189325"></a><a name="b364411189325"></a>start</strong> is set to <strong id="b159981522193214"><a name="b159981522193214"></a><a name="b159981522193214"></a>cpu_util</strong>, you can start your query from the next metric of <strong id="b574315653219"><a name="b574315653219"></a><a name="b574315653219"></a>cpu_util</strong>.</p>
    </td>
    </tr>
    <tr id="row20477125219253"><td class="cellrowborder" valign="top" width="22.66%" headers="mcps1.2.4.1.1 "><p id="p44811040173612"><a name="p44811040173612"></a><a name="p44811040173612"></a>total</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.869999999999997%" headers="mcps1.2.4.1.2 "><p id="p1348113409364"><a name="p1348113409364"></a><a name="p1348113409364"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.47%" headers="mcps1.2.4.1.3 "><p id="p448244013616"><a name="p448244013616"></a><a name="p448244013616"></a>Specifies the total number of metrics.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "metrics": [
            {
                "namespace": "SYS.ECS", 
                "dimensions": [
                    {
                        "name": "instance_id", 
                        "value": "d9112af5-6913-4f3b-bd0a-3f96711e004d"
                    }
                ], 
                "metric_name": "cpu_util", 
                "unit": "%"
            }
        ], 
        "meta_data": {
            "count": 1, 
            "marker": "SYS.ECS.cpu_util.instance_id:d9112af5-6913-4f3b-bd0a-3f96711e004d", 
            "total": 7
        }
    }
    ```


## Returned Values<a name="section6956456"></a>

-   Normal

    200

-   Abnormal

    <a name="table46793998"></a>
    <table><thead align="left"><tr id="row65573909"><th class="cellrowborder" valign="top" width="37.41%" id="mcps1.1.3.1.1"><p id="p9886408"><a name="p9886408"></a><a name="p9886408"></a>Returned Values</p>
    </th>
    <th class="cellrowborder" valign="top" width="62.59%" id="mcps1.1.3.1.2"><p id="p62601592"><a name="p62601592"></a><a name="p62601592"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row37564172"><td class="cellrowborder" valign="top" width="37.41%" headers="mcps1.1.3.1.1 "><p id="p22799085"><a name="p22799085"></a><a name="p22799085"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.59%" headers="mcps1.1.3.1.2 "><p id="p44643603"><a name="p44643603"></a><a name="p44643603"></a>Request error</p>
    </td>
    </tr>
    <tr id="row66248115"><td class="cellrowborder" valign="top" width="37.41%" headers="mcps1.1.3.1.1 "><p id="p64497130"><a name="p64497130"></a><a name="p64497130"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.59%" headers="mcps1.1.3.1.2 "><p id="p42202994"><a name="p42202994"></a><a name="p42202994"></a>The authentication information is not provided or is incorrect.</p>
    </td>
    </tr>
    <tr id="row44282627"><td class="cellrowborder" valign="top" width="37.41%" headers="mcps1.1.3.1.1 "><p id="p30123063"><a name="p30123063"></a><a name="p30123063"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.59%" headers="mcps1.1.3.1.2 "><p id="p15114764"><a name="p15114764"></a><a name="p15114764"></a>You are forbidden to access the page requested.</p>
    </td>
    </tr>
    <tr id="row1815156"><td class="cellrowborder" valign="top" width="37.41%" headers="mcps1.1.3.1.1 "><p id="p12809933"><a name="p12809933"></a><a name="p12809933"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.59%" headers="mcps1.1.3.1.2 "><p id="p10309404"><a name="p10309404"></a><a name="p10309404"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row25675773"><td class="cellrowborder" valign="top" width="37.41%" headers="mcps1.1.3.1.1 "><p id="p66471715"><a name="p66471715"></a><a name="p66471715"></a>429 Too Many Requests</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.59%" headers="mcps1.1.3.1.2 "><p id="p5281111"><a name="p5281111"></a><a name="p5281111"></a>Concurrent requests are excessive.</p>
    </td>
    </tr>
    <tr id="row47530006"><td class="cellrowborder" valign="top" width="37.41%" headers="mcps1.1.3.1.1 "><p id="p24725298"><a name="p24725298"></a><a name="p24725298"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.59%" headers="mcps1.1.3.1.2 "><p id="p39567352"><a name="p39567352"></a><a name="p39567352"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row20561848"><td class="cellrowborder" valign="top" width="37.41%" headers="mcps1.1.3.1.1 "><p id="p54897010"><a name="p54897010"></a><a name="p54897010"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.59%" headers="mcps1.1.3.1.2 "><p id="p1451523117958"><a name="p1451523117958"></a><a name="p1451523117958"></a>The service is currently unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Code<a name="section4614115614510"></a>

For details, see  [Error Codes](error-codes.md).


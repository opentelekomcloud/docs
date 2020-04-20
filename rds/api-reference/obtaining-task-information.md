# Obtaining Task Information<a name="rds_01_0009"></a>

## Function<a name="section6603527917262"></a>

This API is used to obtain task information of the task center.

-   Learn how to  [authorize and authenticate](authentication.md)  this API before using it.
-   Before calling this API, obtain the required  [region and endpoint](https://docs.otc.t-systems.com/en-us/endpoint/index.html).

## Constraints<a name="section1995103535418"></a>

-   This API is used to query only asynchronous tasks in the task center within one month.
-   Information of the following asynchronous tasks can be obtained: creating single or primary/standby DB instances, creating read replicas, changing single DB instances to primary/standby instances, switching primary/standby DB instances, scaling up storage space, and binding or unbinding EIPs.

## URI<a name="section47568069103438"></a>

-   URI format

    GET https://\{_Endpoint_\}/v3/\{project\_id\}/jobs?id=\{id\}

-   Example

    https://rds.eu-de.otc.t-systems.com/v3/0483b6b16e954cb88930a360d2c4e663/jobs?id=a9767ede-fe0f-4888-9003-e843a4c90514


-   Parameter description

    **Table  1**  Parameter description

    <a name="table37593651103438"></a>
    <table><thead align="left"><tr id="row58913670103438"><th class="cellrowborder" valign="top" width="23.45%" id="mcps1.2.4.1.1"><p id="p7277976103438"><a name="p7277976103438"></a><a name="p7277976103438"></a><strong id="b656317391493"><a name="b656317391493"></a><a name="b656317391493"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="29.360000000000003%" id="mcps1.2.4.1.2"><p id="p52645207103438"><a name="p52645207103438"></a><a name="p52645207103438"></a><strong id="b056414398915"><a name="b056414398915"></a><a name="b056414398915"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="47.19%" id="mcps1.2.4.1.3"><p id="p36403370103438"><a name="p36403370103438"></a><a name="p36403370103438"></a><strong id="b125663391093"><a name="b125663391093"></a><a name="b125663391093"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row62991866103438"><td class="cellrowborder" valign="top" width="23.45%" headers="mcps1.2.4.1.1 "><p id="p902364145258"><a name="p902364145258"></a><a name="p902364145258"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.360000000000003%" headers="mcps1.2.4.1.2 "><p id="p5982632145258"><a name="p5982632145258"></a><a name="p5982632145258"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.19%" headers="mcps1.2.4.1.3 "><p id="p14831209145258"><a name="p14831209145258"></a><a name="p14831209145258"></a>Specifies the project ID of a tenant in a region.</p>
    <p id="p19455113121011"><a name="p19455113121011"></a><a name="p19455113121011"></a>For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row64285464517"><td class="cellrowborder" valign="top" width="23.45%" headers="mcps1.2.4.1.1 "><p id="p74292461953"><a name="p74292461953"></a><a name="p74292461953"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.360000000000003%" headers="mcps1.2.4.1.2 "><p id="p60181840"><a name="p60181840"></a><a name="p60181840"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.19%" headers="mcps1.2.4.1.3 "><p id="p16429184614514"><a name="p16429184614514"></a><a name="p16429184614514"></a>Specifies the task ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section3074340117316"></a>

None

## Response<a name="section4828447917262"></a>

-   Normal response

    **Table  2**  Parameter description

    <a name="table54571314103317"></a>
    <table><thead align="left"><tr id="row3459121463318"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.4.1.1"><p id="p91816414334"><a name="p91816414334"></a><a name="p91816414334"></a><strong id="b135941639093"><a name="b135941639093"></a><a name="b135941639093"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="30%" id="mcps1.2.4.1.2"><p id="p123216414335"><a name="p123216414335"></a><a name="p123216414335"></a><strong id="b359517395913"><a name="b359517395913"></a><a name="b359517395913"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="45%" id="mcps1.2.4.1.3"><p id="p440144113310"><a name="p440144113310"></a><a name="p440144113310"></a><strong id="b17596439294"><a name="b17596439294"></a><a name="b17596439294"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row16459161403314"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p12459414153315"><a name="p12459414153315"></a><a name="p12459414153315"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.2 "><p id="p945941483315"><a name="p945941483315"></a><a name="p945941483315"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.4.1.3 "><p id="p10459614163315"><a name="p10459614163315"></a><a name="p10459614163315"></a>Indicates the task ID.</p>
    </td>
    </tr>
    <tr id="row2367713135211"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p2036712135529"><a name="p2036712135529"></a><a name="p2036712135529"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.2 "><p id="p1136761311525"><a name="p1136761311525"></a><a name="p1136761311525"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.4.1.3 "><p id="p3367141316527"><a name="p3367141316527"></a><a name="p3367141316527"></a>Indicates the task name.</p>
    </td>
    </tr>
    <tr id="row98211748533"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p11821164185319"><a name="p11821164185319"></a><a name="p11821164185319"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.2 "><p id="p178212410537"><a name="p178212410537"></a><a name="p178212410537"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.4.1.3 "><p id="p20821194165310"><a name="p20821194165310"></a><a name="p20821194165310"></a>Indicates the task execution status.</p>
    <div class="p" id="p12167194625317"><a name="p12167194625317"></a><a name="p12167194625317"></a>Value:<a name="ul1116724610533"></a><a name="ul1116724610533"></a><ul id="ul1116724610533"><li><strong id="b84235270616558"><a name="b84235270616558"></a><a name="b84235270616558"></a>Running</strong>: The task is being executed.</li><li><strong id="b842352706165522"><a name="b842352706165522"></a><a name="b842352706165522"></a>Completed</strong>: The task is successfully executed.</li><li><strong id="b842352706165534"><a name="b842352706165534"></a><a name="b842352706165534"></a>Failed</strong>: The task fails to be executed.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="row8137184445520"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1137944165511"><a name="p1137944165511"></a><a name="p1137944165511"></a>created</p>
    </td>
    <td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.2 "><p id="p10137164414554"><a name="p10137164414554"></a><a name="p10137164414554"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.4.1.3 "><p id="p740512805712"><a name="p740512805712"></a><a name="p740512805712"></a>Indicates the creation time in the "yyyy-mm-ddThh:mm:ssZ" format.</p>
    <p id="p174057816579"><a name="p174057816579"></a><a name="p174057816579"></a><strong id="b1562363918912"><a name="b1562363918912"></a><a name="b1562363918912"></a>T</strong> is the separator between the calendar and the hourly notation of time. <strong id="b762319391794"><a name="b762319391794"></a><a name="b762319391794"></a>Z</strong> indicates the time zone offset.</p>
    </td>
    </tr>
    <tr id="row113911711165717"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p183911211105719"><a name="p183911211105719"></a><a name="p183911211105719"></a>process</p>
    </td>
    <td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.2 "><p id="p1839115119578"><a name="p1839115119578"></a><a name="p1839115119578"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.4.1.3 "><p id="p739131112579"><a name="p739131112579"></a><a name="p739131112579"></a>Indicates the task execution progress.</p>
    <div class="note" id="note93961953175813"><a name="note93961953175813"></a><a name="note93961953175813"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p11412175314581"><a name="p11412175314581"></a><a name="p11412175314581"></a>The execution progress (such as 60%) is displayed only when the task is being executed. Otherwise, <strong id="b842352706173440"><a name="b842352706173440"></a><a name="b842352706173440"></a>""</strong> is returned.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row38251071027"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p782547326"><a name="p782547326"></a><a name="p782547326"></a>instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.2 "><p id="p12825171522"><a name="p12825171522"></a><a name="p12825171522"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.4.1.3 "><p id="p148251371722"><a name="p148251371722"></a><a name="p148251371722"></a>Indicates information of the DB instance on which the task is executed.</p>
    <p id="p176261414190"><a name="p176261414190"></a><a name="p176261414190"></a>For details, see <a href="#table4062895917262">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="row5281748549"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p15281144816414"><a name="p15281144816414"></a><a name="p15281144816414"></a>entities</p>
    </td>
    <td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.2 "><p id="p828117481940"><a name="p828117481940"></a><a name="p828117481940"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.4.1.3 "><p id="p152810481047"><a name="p152810481047"></a><a name="p152810481047"></a>The displayed information varies depending on the tasks.</p>
    <p id="p597415316194"><a name="p597415316194"></a><a name="p597415316194"></a>Refer to the following:</p>
    <a name="ul3554342192"></a><a name="ul3554342192"></a><ul id="ul3554342192"><li><a href="#table1014617554138">Table 4</a></li><li><a href="#table7391102412203">Table 7</a></li><li><a href="#table148754542012">Table 9</a></li><li><a href="#table2098817407217">Table 10</a></li></ul>
    <div class="note" id="note1546714962017"><a name="note1546714962017"></a><a name="note1546714962017"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p9467189102011"><a name="p9467189102011"></a><a name="p9467189102011"></a>For asynchronous tasks without the <strong id="b842352706173418"><a name="b842352706173418"></a><a name="b842352706173418"></a>entities</strong> field description, <strong id="b842352706173445"><a name="b842352706173445"></a><a name="b842352706173445"></a>{}</strong> is returned.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row135472431958"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.4.1.1 "><p id="p1954711436518"><a name="p1954711436518"></a><a name="p1954711436518"></a>fail_reason</p>
    </td>
    <td class="cellrowborder" valign="top" width="30%" headers="mcps1.2.4.1.2 "><p id="p95478437512"><a name="p95478437512"></a><a name="p95478437512"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45%" headers="mcps1.2.4.1.3 "><p id="p1654711431756"><a name="p1654711431756"></a><a name="p1654711431756"></a>Indicates the error information displayed when a task failed.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  instances field data structure description

    <a name="table4062895917262"></a>
    <table><thead align="left"><tr id="row2045312717262"><th class="cellrowborder" valign="top" width="23.527647235276476%" id="mcps1.2.4.1.1"><p id="p4609059717262"><a name="p4609059717262"></a><a name="p4609059717262"></a><strong id="b06745392919"><a name="b06745392919"></a><a name="b06745392919"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="31.36686331366863%" id="mcps1.2.4.1.2"><p id="p4235091617262"><a name="p4235091617262"></a><a name="p4235091617262"></a><strong id="b15675183918920"><a name="b15675183918920"></a><a name="b15675183918920"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="45.1054894510549%" id="mcps1.2.4.1.3"><p id="p787220417262"><a name="p787220417262"></a><a name="p787220417262"></a><strong id="b467614391095"><a name="b467614391095"></a><a name="b467614391095"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3366877217262"><td class="cellrowborder" valign="top" width="23.527647235276476%" headers="mcps1.2.4.1.1 "><p id="p4281598817262"><a name="p4281598817262"></a><a name="p4281598817262"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.36686331366863%" headers="mcps1.2.4.1.2 "><p id="p4554301317262"><a name="p4554301317262"></a><a name="p4554301317262"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.1054894510549%" headers="mcps1.2.4.1.3 "><p id="p6510543817262"><a name="p6510543817262"></a><a name="p6510543817262"></a>Indicates the DB instance ID.</p>
    </td>
    </tr>
    <tr id="row964613217262"><td class="cellrowborder" valign="top" width="23.527647235276476%" headers="mcps1.2.4.1.1 "><p id="p4313926117262"><a name="p4313926117262"></a><a name="p4313926117262"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.36686331366863%" headers="mcps1.2.4.1.2 "><p id="p461925817262"><a name="p461925817262"></a><a name="p461925817262"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.1054894510549%" headers="mcps1.2.4.1.3 "><p id="p3861563617262"><a name="p3861563617262"></a><a name="p3861563617262"></a>Indicates the DB instance name.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  entities field data structure description \(creating DB instances, changing single DB instances to primary/standby, or creating read replicas\)

    <a name="table1014617554138"></a>
    <table><thead align="left"><tr id="row81461455201310"><th class="cellrowborder" valign="top" width="24%" id="mcps1.2.4.1.1"><p id="p1014655516139"><a name="p1014655516139"></a><a name="p1014655516139"></a><strong id="b176871839398"><a name="b176871839398"></a><a name="b176871839398"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="32%" id="mcps1.2.4.1.2"><p id="p4162655101313"><a name="p4162655101313"></a><a name="p4162655101313"></a><strong id="b1568943912911"><a name="b1568943912911"></a><a name="b1568943912911"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44%" id="mcps1.2.4.1.3"><p id="p12162105561317"><a name="p12162105561317"></a><a name="p12162105561317"></a><strong id="b156901139593"><a name="b156901139593"></a><a name="b156901139593"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row9162185517134"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p616225516136"><a name="p616225516136"></a><a name="p616225516136"></a>instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="p01623557138"><a name="p01623557138"></a><a name="p01623557138"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.4.1.3 "><p id="p1716255591313"><a name="p1716255591313"></a><a name="p1716255591313"></a>Indicates the DB instance information to be implemented by a task.</p>
    <p id="p34731051101811"><a name="p34731051101811"></a><a name="p34731051101811"></a>For details, see <a href="#table975183423611">Table 5</a>.</p>
    </td>
    </tr>
    <tr id="row1516215514138"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p71781255151318"><a name="p71781255151318"></a><a name="p71781255151318"></a>resource_ids</p>
    </td>
    <td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="p817875511311"><a name="p817875511311"></a><a name="p817875511311"></a>List&lt;String&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.4.1.3 "><p id="p7178155521312"><a name="p7178155521312"></a><a name="p7178155521312"></a>Indicates the resource ID involved in a task.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5**  entities.instance field data structure description

    <a name="table975183423611"></a>
    <table><thead align="left"><tr id="row576603417366"><th class="cellrowborder" valign="top" width="23.762376237623766%" id="mcps1.2.4.1.1"><p id="p15782934123618"><a name="p15782934123618"></a><a name="p15782934123618"></a><strong id="b167041539597"><a name="b167041539597"></a><a name="b167041539597"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="29.7029702970297%" id="mcps1.2.4.1.2"><p id="p1978243473620"><a name="p1978243473620"></a><a name="p1978243473620"></a><strong id="b17051139791"><a name="b17051139791"></a><a name="b17051139791"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="46.53465346534653%" id="mcps1.2.4.1.3"><p id="p19782113413362"><a name="p19782113413362"></a><a name="p19782113413362"></a><strong id="b67061539197"><a name="b67061539197"></a><a name="b67061539197"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row14782133414367"><td class="cellrowborder" valign="top" width="23.762376237623766%" headers="mcps1.2.4.1.1 "><p id="p1079713453618"><a name="p1079713453618"></a><a name="p1079713453618"></a>endpoint</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.7029702970297%" headers="mcps1.2.4.1.2 "><p id="p1279743463620"><a name="p1279743463620"></a><a name="p1279743463620"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.53465346534653%" headers="mcps1.2.4.1.3 "><p id="p1379773419364"><a name="p1379773419364"></a><a name="p1379773419364"></a>Indicates the DB instance connection address.</p>
    </td>
    </tr>
    <tr id="row127971434193613"><td class="cellrowborder" valign="top" width="23.762376237623766%" headers="mcps1.2.4.1.1 "><p id="p138135341363"><a name="p138135341363"></a><a name="p138135341363"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.7029702970297%" headers="mcps1.2.4.1.2 "><p id="p68130343364"><a name="p68130343364"></a><a name="p68130343364"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.53465346534653%" headers="mcps1.2.4.1.3 "><p id="p17813163410363"><a name="p17813163410363"></a><a name="p17813163410363"></a>The value is <strong id="b271615391599"><a name="b271615391599"></a><a name="b271615391599"></a>Single</strong>, <strong id="b171616391895"><a name="b171616391895"></a><a name="b171616391895"></a>Ha</strong>, or <strong id="b1571611399916"><a name="b1571611399916"></a><a name="b1571611399916"></a>Replica</strong>, indicating the single DB instance, primary/standby DB instances, and read replica, respectively.</p>
    </td>
    </tr>
    <tr id="row765018449559"><td class="cellrowborder" valign="top" width="23.762376237623766%" headers="mcps1.2.4.1.1 "><p id="p106501444165514"><a name="p106501444165514"></a><a name="p106501444165514"></a>datastore</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.7029702970297%" headers="mcps1.2.4.1.2 "><p id="p156507445552"><a name="p156507445552"></a><a name="p156507445552"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.53465346534653%" headers="mcps1.2.4.1.3 "><p id="p1261414318189"><a name="p1261414318189"></a><a name="p1261414318189"></a>Data structure. For details, see <a href="#table173094268581">Table 6</a>.</p>
    </td>
    </tr>
    <tr id="row065719580010"><td class="cellrowborder" valign="top" width="23.762376237623766%" headers="mcps1.2.4.1.1 "><p id="p7657125811020"><a name="p7657125811020"></a><a name="p7657125811020"></a>replica_of</p>
    </td>
    <td class="cellrowborder" valign="top" width="29.7029702970297%" headers="mcps1.2.4.1.2 "><p id="p5657058607"><a name="p5657058607"></a><a name="p5657058607"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.53465346534653%" headers="mcps1.2.4.1.3 "><p id="p181921914311"><a name="p181921914311"></a><a name="p181921914311"></a>Indicates the primary DB instance ID. This parameter is returned only when a read replica is created.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6**  datastore field data structure description

    <a name="table173094268581"></a>
    <table><thead align="left"><tr id="row153243260580"><th class="cellrowborder" valign="top" width="24%" id="mcps1.2.4.1.1"><p id="p11324142645814"><a name="p11324142645814"></a><a name="p11324142645814"></a><strong id="b197337391591"><a name="b197337391591"></a><a name="b197337391591"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="32%" id="mcps1.2.4.1.2"><p id="p1533910267583"><a name="p1533910267583"></a><a name="p1533910267583"></a><strong id="b147347398914"><a name="b147347398914"></a><a name="b147347398914"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44%" id="mcps1.2.4.1.3"><p id="p3339526125813"><a name="p3339526125813"></a><a name="p3339526125813"></a><strong id="b3736839199"><a name="b3736839199"></a><a name="b3736839199"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row0339102625817"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p1833918260580"><a name="p1833918260580"></a><a name="p1833918260580"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="p3356182625820"><a name="p3356182625820"></a><a name="p3356182625820"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.4.1.3 "><p id="p163562026185813"><a name="p163562026185813"></a><a name="p163562026185813"></a>Indicates the DB engine.</p>
    </td>
    </tr>
    <tr id="row1335614267583"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p16356132625815"><a name="p16356132625815"></a><a name="p16356132625815"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="p3356162665817"><a name="p3356162665817"></a><a name="p3356162665817"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.4.1.3 "><p id="p1437111268582"><a name="p1437111268582"></a><a name="p1437111268582"></a>Indicates the database version.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  7**  entities field data structure description \(resizing a DB instance\)

    <a name="table7391102412203"></a>
    <table><thead align="left"><tr id="row83911224122019"><th class="cellrowborder" valign="top" width="23.527647235276476%" id="mcps1.2.4.1.1"><p id="p15391192422011"><a name="p15391192422011"></a><a name="p15391192422011"></a><strong id="b475214391791"><a name="b475214391791"></a><a name="b475214391791"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="31.36686331366863%" id="mcps1.2.4.1.2"><p id="p164051024152015"><a name="p164051024152015"></a><a name="p164051024152015"></a><strong id="b57531939791"><a name="b57531939791"></a><a name="b57531939791"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="45.1054894510549%" id="mcps1.2.4.1.3"><p id="p16405132422010"><a name="p16405132422010"></a><a name="p16405132422010"></a><strong id="b177548396910"><a name="b177548396910"></a><a name="b177548396910"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row54055240202"><td class="cellrowborder" valign="top" width="23.527647235276476%" headers="mcps1.2.4.1.1 "><p id="p54054245204"><a name="p54054245204"></a><a name="p54054245204"></a>volume</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.36686331366863%" headers="mcps1.2.4.1.2 "><p id="p10405142432016"><a name="p10405142432016"></a><a name="p10405142432016"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.1054894510549%" headers="mcps1.2.4.1.3 "><p id="p9422824202013"><a name="p9422824202013"></a><a name="p9422824202013"></a>Indicates the resized disk information.</p>
    <p id="p149159521756"><a name="p149159521756"></a><a name="p149159521756"></a>For details, see <a href="#table624912591398">Table 8</a>.</p>
    </td>
    </tr>
    <tr id="row94221324102019"><td class="cellrowborder" valign="top" width="23.527647235276476%" headers="mcps1.2.4.1.1 "><p id="p237213231997"><a name="p237213231997"></a><a name="p237213231997"></a>resource_ids</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.36686331366863%" headers="mcps1.2.4.1.2 "><p id="p9372102310911"><a name="p9372102310911"></a><a name="p9372102310911"></a>List&lt;String&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.1054894510549%" headers="mcps1.2.4.1.3 "><p id="p537218231798"><a name="p537218231798"></a><a name="p537218231798"></a>Indicates the resource ID involved in a task.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  8**  volume field data structure description

    <a name="table624912591398"></a>
    <table><thead align="left"><tr id="row1526545915917"><th class="cellrowborder" valign="top" width="24%" id="mcps1.2.4.1.1"><p id="p026555914920"><a name="p026555914920"></a><a name="p026555914920"></a><strong id="b117745395920"><a name="b117745395920"></a><a name="b117745395920"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="32%" id="mcps1.2.4.1.2"><p id="p22657595911"><a name="p22657595911"></a><a name="p22657595911"></a><strong id="b17752398919"><a name="b17752398919"></a><a name="b17752398919"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44%" id="mcps1.2.4.1.3"><p id="p20280125917911"><a name="p20280125917911"></a><a name="p20280125917911"></a><strong id="b197761439394"><a name="b197761439394"></a><a name="b197761439394"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row628020591792"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p122803593917"><a name="p122803593917"></a><a name="p122803593917"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="p229719593916"><a name="p229719593916"></a><a name="p229719593916"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.4.1.3 "><p id="p12979591199"><a name="p12979591199"></a><a name="p12979591199"></a>Indicates the volume type.</p>
    </td>
    </tr>
    <tr id="row1829725910918"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p1729713591493"><a name="p1729713591493"></a><a name="p1729713591493"></a>original_size</p>
    </td>
    <td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="p1431115917919"><a name="p1431115917919"></a><a name="p1431115917919"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.4.1.3 "><p id="p4311759893"><a name="p4311759893"></a><a name="p4311759893"></a>Indicates the original disk size of the DB instance.</p>
    </td>
    </tr>
    <tr id="row14459456111318"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.4.1.1 "><p id="p1459155691316"><a name="p1459155691316"></a><a name="p1459155691316"></a>target_size</p>
    </td>
    <td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.4.1.2 "><p id="p4459256171317"><a name="p4459256171317"></a><a name="p4459256171317"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="44%" headers="mcps1.2.4.1.3 "><p id="p1645925616135"><a name="p1645925616135"></a><a name="p1645925616135"></a>Indicates the target disk size of the DB instance.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  9**  entities field data structure description \(binding/unbinding EIPs or enabling/disabling remote access\)

    <a name="table148754542012"></a>
    <table><thead align="left"><tr id="row15011345202020"><th class="cellrowborder" valign="top" width="23.527647235276476%" id="mcps1.2.4.1.1"><p id="p1350164512014"><a name="p1350164512014"></a><a name="p1350164512014"></a><strong id="b1879563919913"><a name="b1879563919913"></a><a name="b1879563919913"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="31.36686331366863%" id="mcps1.2.4.1.2"><p id="p250114522010"><a name="p250114522010"></a><a name="p250114522010"></a><strong id="b279653913912"><a name="b279653913912"></a><a name="b279653913912"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="45.1054894510549%" id="mcps1.2.4.1.3"><p id="p45182453209"><a name="p45182453209"></a><a name="p45182453209"></a><strong id="b2079812391694"><a name="b2079812391694"></a><a name="b2079812391694"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2518144517203"><td class="cellrowborder" valign="top" width="23.527647235276476%" headers="mcps1.2.4.1.1 "><p id="p9518174562016"><a name="p9518174562016"></a><a name="p9518174562016"></a>public_ip</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.36686331366863%" headers="mcps1.2.4.1.2 "><p id="p651844514208"><a name="p651844514208"></a><a name="p651844514208"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.1054894510549%" headers="mcps1.2.4.1.3 "><p id="p8518144517204"><a name="p8518144517204"></a><a name="p8518144517204"></a>Indicates the EIP implemented by the task.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  10**  entities field data structure description \(primary/standby switchover\)

    <a name="table2098817407217"></a>
    <table><thead align="left"><tr id="row1839410219"><th class="cellrowborder" valign="top" width="23.527647235276476%" id="mcps1.2.4.1.1"><p id="p6314417215"><a name="p6314417215"></a><a name="p6314417215"></a><strong id="b198086391896"><a name="b198086391896"></a><a name="b198086391896"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="31.36686331366863%" id="mcps1.2.4.1.2"><p id="p6324172113"><a name="p6324172113"></a><a name="p6324172113"></a><strong id="b1480915397911"><a name="b1480915397911"></a><a name="b1480915397911"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="45.1054894510549%" id="mcps1.2.4.1.3"><p id="p437415216"><a name="p437415216"></a><a name="p437415216"></a><strong id="b1181063915916"><a name="b1181063915916"></a><a name="b1181063915916"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row161912414215"><td class="cellrowborder" valign="top" width="23.527647235276476%" headers="mcps1.2.4.1.1 "><p id="p53554182113"><a name="p53554182113"></a><a name="p53554182113"></a>switch_strategy</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.36686331366863%" headers="mcps1.2.4.1.2 "><p id="p18351441192115"><a name="p18351441192115"></a><a name="p18351441192115"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.1054894510549%" headers="mcps1.2.4.1.3 "><p id="p1935174122111"><a name="p1935174122111"></a><a name="p1935174122111"></a>Indicates the primary/standby switchover policy.</p>
    </td>
    </tr>
    </tbody>
    </table>

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >In the response example, some tasks in the task center are used as examples.  


-   Example normal response

    Creating a DB instance:

    ```
    {
    	"job": {
    		"id": "31b8ae23-c687-4d80-b7b4-42a66c9bb886",
    		"name": "CreateMysqlSingleHAInstance",
    		"status": "Completed",
    		"created": "2018-08-06T10:41:14+0000",
    		"process": "",
    		"instance": {
    			"id": "a48e43ff268f4c0e879652d65e63d0fbin01",
    			"name": "DO-NOT-TOUCH-mgr2-mysql-single"
    		},
    		"entities": {
    			"instance": {
    				"endpoint": "192.168.1.203:3306",
    				"type": "Single",
    				"datastore": {
    					"type": "mysql",
    					"version": "5.7"
    				}
    			},
    			"resource_id": ["a48e43ff268f4c0e879652d65e63d0fbin01.vm", "a48e43ff268f4c0e879652d65e63d0fbin01.volume"]
    		}
    	}
    }
    ```

    Creating a read replica:

    ```
    {
    	"job": {
    		"id": "31b8ae23-c687-4d80-b7b4-42a66c9bb886",
    		"name": " CreateMysqlReplicaInstance",
    		"status": "Completed",
    		"created": "2018-08-06T10:41:14+0000",
    		"process": "",
    		"instance": {
    			"id": "288caaa9d05f4ec1a1f58de2e0945685in01",
    			"name": "mysql-replica"
    		},
    		"entities": {
    			"instance": {
    				"endpoint": "192.168 .1 .203: 3306",
    				"type": "replica",
    				"datastore": {
    					"type": "mysql",
    					"version": "5.7"
    				},
    				"replica_of": "a48e43ff268f4c0e879652d65e63d0fbin01"
    			},
    			"resource_ids": ["288caaa9d05f4ec1a1f58de2e0945685in01.vm", "288caaa9d05f4ec1a1f58de2e0945685in01.volume"]
    		}
    	}
    }
    ```

    Binding an EIP:

    ```
    {
    	"job": {
    		"id": "31b8ae23-c687-4d80-b7b4-42a66c9bb886",
    		"name": "MysqlBindEIP",
    		"status": "Completed",
    		"created": "2018-08-06T10:41:14+0000",
    		"process": "",
    		"instance": {
    			"id": "a48e43ff268f4c0e879652d65e63d0fbin01",
    			"name": "DO-NOT-TOUCH-mgr2-mysql-single"
    		},
    		"entities": {
    			"public_ip": "10.154 .218 .254"
    		}
    	}
    }
    ```

    Rebooting a DB instance:

    ```
    {
    	"job": {
    		"id": "31b8ae23-c687-4d80-b7b4-42a66c9bb886",
    		"name": " RestartMysqlInstance",
    		"status": "Completed",
    		"created": "2018-08-06T10:41:14+0000",
    		"process": "",
    		"instance": {
    			"id": "a48e43ff268f4c0e879652d65e63d0fbin01",
    			"name": "DO-NOT-TOUCH-mgr2-mysql-single"
    		},
    		"entities": {}
    	}
    }
    ```

    Task being executed:

    ```
    {
    	"job": {
    		"id": "31 b8ae23 - c687 - 4 d80 - b7b4 - 42 a66c9bb886",
    		"name": "CreateMysqlSingleHAInstance"," status": "Running",
    		"created": "2018-08-06T10:41:14+0000",
    		"process": "60 % ",
    		"instance": {
    			"id": "a48e43ff268f4c0e879652d65e63d0fbin01",
    			"name": "DO-NOT-TOUCH-mgr2-mysql-single"
    		},
    		"entities": {
    			"instance": {
    				"type": "Single",
    				"datastore": {
    					"type": "mysql",
    					"version": "5.7"
    				}
    			}
    		}
    	}
    }
    ```

    Task fails to be executed:

    ```
    {
    	"job": {
    		"id": "31 b8ae23 - c687 - 4 d80 - b7b4 - 42 a66c9bb886",
    		"name": "CreateMysqlSingleHAInstance",
    		"status": "Failed",
    		"created": "2018-08-06T10:41:14+0000",
    		"process": "",
    		"instance": {
    			"id": "a48e43ff268f4c0e879652d65e63d0fbin01",
    			"name": "DO-NOT-TOUCH-mgr2-mysql-single"
    		},
    		"entities": {
    			"instance": {
    				"type": "Single",
    				"datastore": {
    					"type": "mysql",
    					"version": "5.7"
    				}
    			}
    		},
    		"fail_reason": "createVM failed."
    	}
    }
    ```

-   Abnormal Response

    For details, see  [Abnormal Request Results](abnormal-request-results.md).


## Status Code<a name="section4778540915440"></a>

For details, see  [Status Codes](status-codes.md).

## Error Code<a name="section946032144017"></a>

For details, see  [Error Codes](error-codes.md).


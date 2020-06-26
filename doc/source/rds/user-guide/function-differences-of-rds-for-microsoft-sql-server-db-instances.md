# Function Differences of RDS for Microsoft SQL Server DB Instances<a name="rds_01_0018"></a>

This section describes function differences between single and primary/standby DB instances as well as function differences among Microsoft SQL Server editions.

-   For details about  differences of basic functions, see  [Table 1](#table45712140181049).
-   For details about  differences of product functions, see  [Table 1](db-instance-introduction.md#table15359933192816).
-   For details about  differences of database migration functions, see  [Table 2](#table51069553181111).
-   For details about  differences of database security functions, see  [Table 3](#table12903168181132).

**Table  1**  Differences of basic functions

<a name="table45712140181049"></a>
<table><thead align="left"><tr id="row11706050181049"><th class="cellrowborder" valign="top" width="19.67%" id="mcps1.2.5.1.1"><p id="p8665955181049"><a name="p8665955181049"></a><a name="p8665955181049"></a>Module</p>
</th>
<th class="cellrowborder" valign="top" width="26.57%" id="mcps1.2.5.1.2"><p id="p9248287181049"><a name="p9248287181049"></a><a name="p9248287181049"></a><strong>Function Item</strong></p>
</th>
<th class="cellrowborder" valign="top" width="25.19%" id="mcps1.2.5.1.3"><p id="p31115530181049"><a name="p31115530181049"></a><a name="p31115530181049"></a><strong id="b310575814451"><a name="b310575814451"></a><a name="b310575814451"></a>Primary/Standby</strong></p>
</th>
<th class="cellrowborder" valign="top" width="28.57%" id="mcps1.2.5.1.4"><p id="p41977438181049"><a name="p41977438181049"></a><a name="p41977438181049"></a><strong id="b18711394610"><a name="b18711394610"></a><a name="b18711394610"></a>Single</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row4363144152617"><td class="cellrowborder" rowspan="8" valign="top" width="19.67%" headers="mcps1.2.5.1.1 "><p id="p5333112414278"><a name="p5333112414278"></a><a name="p5333112414278"></a>Life cycle</p>
</td>
<td class="cellrowborder" valign="top" width="26.57%" headers="mcps1.2.5.1.2 "><p id="p647601062716"><a name="p647601062716"></a><a name="p647601062716"></a>Create a DB instance</p>
</td>
<td class="cellrowborder" valign="top" width="25.19%" headers="mcps1.2.5.1.3 "><p id="p10476121022719"><a name="p10476121022719"></a><a name="p10476121022719"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.2.5.1.4 "><p id="p104761710122711"><a name="p104761710122711"></a><a name="p104761710122711"></a>Supported</p>
</td>
</tr>
<tr id="row186939122613"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p9476710122718"><a name="p9476710122718"></a><a name="p9476710122718"></a>Reboot a DB instance</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p124763108273"><a name="p124763108273"></a><a name="p124763108273"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p8476510182717"><a name="p8476510182717"></a><a name="p8476510182717"></a>Supported</p>
</td>
</tr>
<tr id="row125123133268"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p0476310122718"><a name="p0476310122718"></a><a name="p0476310122718"></a>Auto-renewal</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p6477210142713"><a name="p6477210142713"></a><a name="p6477210142713"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p44772010142710"><a name="p44772010142710"></a><a name="p44772010142710"></a>Supported</p>
</td>
</tr>
<tr id="row1892182552611"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p1644371612279"><a name="p1644371612279"></a><a name="p1644371612279"></a>Change the instance class</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p44441916122717"><a name="p44441916122717"></a><a name="p44441916122717"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p1444201613278"><a name="p1444201613278"></a><a name="p1444201613278"></a>Supported</p>
</td>
</tr>
<tr id="row3579112322614"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p1444101614271"><a name="p1444101614271"></a><a name="p1444101614271"></a>Delete a DB instance</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p1344415160273"><a name="p1344415160273"></a><a name="p1344415160273"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p6444171652719"><a name="p6444171652719"></a><a name="p6444171652719"></a>Supported</p>
</td>
</tr>
<tr id="row2745122013263"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p1844411682718"><a name="p1844411682718"></a><a name="p1844411682718"></a>Upgrade the DB engine version</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p18444101617272"><a name="p18444101617272"></a><a name="p18444101617272"></a>Not supported</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p64441116202711"><a name="p64441116202711"></a><a name="p64441116202711"></a>Not supported</p>
</td>
</tr>
<tr id="row1373173418263"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p1244441682718"><a name="p1244441682718"></a><a name="p1244441682718"></a>Restore to a new DB instance</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p1044421612278"><a name="p1044421612278"></a><a name="p1044421612278"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p544421611275"><a name="p544421611275"></a><a name="p544421611275"></a>Supported</p>
</td>
</tr>
<tr id="row1941191711263"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p1944431612713"><a name="p1944431612713"></a><a name="p1944431612713"></a>Create a read replica</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p2444191619272"><a name="p2444191619272"></a><a name="p2444191619272"></a>Not supported</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p1044411168277"><a name="p1044411168277"></a><a name="p1044411168277"></a>Not supported</p>
</td>
</tr>
<tr id="row19760112912297"><td class="cellrowborder" rowspan="5" valign="top" width="19.67%" headers="mcps1.2.5.1.1 "><p id="p11213547192914"><a name="p11213547192914"></a><a name="p11213547192914"></a>DB instance properties</p>
</td>
<td class="cellrowborder" valign="top" width="26.57%" headers="mcps1.2.5.1.2 "><p id="p10599736112917"><a name="p10599736112917"></a><a name="p10599736112917"></a>View the DB instance list</p>
</td>
<td class="cellrowborder" valign="top" width="25.19%" headers="mcps1.2.5.1.3 "><p id="p55991236172912"><a name="p55991236172912"></a><a name="p55991236172912"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.2.5.1.4 "><p id="p1559917367299"><a name="p1559917367299"></a><a name="p1559917367299"></a>Supported</p>
</td>
</tr>
<tr id="row158981226102918"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p1759933615291"><a name="p1759933615291"></a><a name="p1759933615291"></a>View DB instance details</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p7599133602910"><a name="p7599133602910"></a><a name="p7599133602910"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p2599123611297"><a name="p2599123611297"></a><a name="p2599123611297"></a>Supported</p>
</td>
</tr>
<tr id="row0260122452917"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p1459953611298"><a name="p1459953611298"></a><a name="p1459953611298"></a>Modify the DB instance description</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p5599136122911"><a name="p5599136122911"></a><a name="p5599136122911"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p65991236112916"><a name="p65991236112916"></a><a name="p65991236112916"></a>Supported</p>
</td>
</tr>
<tr id="row3870421122919"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p135995361297"><a name="p135995361297"></a><a name="p135995361297"></a>Change the maintenance window</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p359915361297"><a name="p359915361297"></a><a name="p359915361297"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p15600193616294"><a name="p15600193616294"></a><a name="p15600193616294"></a>Supported</p>
</td>
</tr>
<tr id="row19706141722913"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p1600123612299"><a name="p1600123612299"></a><a name="p1600123612299"></a>Manage tags</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p760016361291"><a name="p760016361291"></a><a name="p760016361291"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p12600103662911"><a name="p12600103662911"></a><a name="p12600103662911"></a>Supported</p>
</td>
</tr>
<tr id="row30025958181049"><td class="cellrowborder" rowspan="3" valign="top" width="19.67%" headers="mcps1.2.5.1.1 "><p id="p16183562181049"><a name="p16183562181049"></a><a name="p16183562181049"></a>Database connection</p>
</td>
<td class="cellrowborder" valign="top" width="26.57%" headers="mcps1.2.5.1.2 "><p id="p35800146181049"><a name="p35800146181049"></a><a name="p35800146181049"></a>Internal access through a VPC</p>
</td>
<td class="cellrowborder" valign="top" width="25.19%" headers="mcps1.2.5.1.3 "><p id="p3738224181049"><a name="p3738224181049"></a><a name="p3738224181049"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.2.5.1.4 "><p id="p34360726181049"><a name="p34360726181049"></a><a name="p34360726181049"></a>Supported</p>
</td>
</tr>
<tr id="row40811079181049"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p64231758181049"><a name="p64231758181049"></a><a name="p64231758181049"></a>Public accessibility</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p35389906181049"><a name="p35389906181049"></a><a name="p35389906181049"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p48010167181049"><a name="p48010167181049"></a><a name="p48010167181049"></a>Supported</p>
</td>
</tr>
<tr id="row29438325181049"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p5545691181049"><a name="p5545691181049"></a><a name="p5545691181049"></a>Read/write splitting address</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p46547845181049"><a name="p46547845181049"></a><a name="p46547845181049"></a>Not supported</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p12279091181049"><a name="p12279091181049"></a><a name="p12279091181049"></a>Not supported</p>
</td>
</tr>
<tr id="row27253779181049"><td class="cellrowborder" rowspan="7" valign="top" width="19.67%" headers="mcps1.2.5.1.1 "><p id="p60072461181049"><a name="p60072461181049"></a><a name="p60072461181049"></a>Backups and restorations</p>
</td>
<td class="cellrowborder" valign="top" width="26.57%" headers="mcps1.2.5.1.2 "><p id="p34031155181049"><a name="p34031155181049"></a><a name="p34031155181049"></a>Full backup</p>
</td>
<td class="cellrowborder" valign="top" width="25.19%" headers="mcps1.2.5.1.3 "><p id="p5060207181049"><a name="p5060207181049"></a><a name="p5060207181049"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.2.5.1.4 "><p id="p7223590181049"><a name="p7223590181049"></a><a name="p7223590181049"></a>Supported</p>
</td>
</tr>
<tr id="row65012316181049"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p1870728181049"><a name="p1870728181049"></a><a name="p1870728181049"></a>Log backup</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p17311246181049"><a name="p17311246181049"></a><a name="p17311246181049"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p60033685181049"><a name="p60033685181049"></a><a name="p60033685181049"></a>Supported</p>
</td>
</tr>
<tr id="row3432256181049"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p37565674181049"><a name="p37565674181049"></a><a name="p37565674181049"></a>Customize a backup policy</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p22920742181049"><a name="p22920742181049"></a><a name="p22920742181049"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p44640774181049"><a name="p44640774181049"></a><a name="p44640774181049"></a>Supported</p>
</td>
</tr>
<tr id="row66222647181049"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p24004211181049"><a name="p24004211181049"></a><a name="p24004211181049"></a>Restore from automated backups</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p65292958181049"><a name="p65292958181049"></a><a name="p65292958181049"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p54238258181049"><a name="p54238258181049"></a><a name="p54238258181049"></a>Supported</p>
</td>
</tr>
<tr id="row18382274181049"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p11473989181049"><a name="p11473989181049"></a><a name="p11473989181049"></a>Point in time recovery</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p56977897181049"><a name="p56977897181049"></a><a name="p56977897181049"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p51806938181049"><a name="p51806938181049"></a><a name="p51806938181049"></a>Supported</p>
</td>
</tr>
<tr id="row42008478181049"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p1521260181049"><a name="p1521260181049"></a><a name="p1521260181049"></a>Partial backup</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p56113240181049"><a name="p56113240181049"></a><a name="p56113240181049"></a>Not supported</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p48878588181049"><a name="p48878588181049"></a><a name="p48878588181049"></a>Not supported</p>
</td>
</tr>
<tr id="row37254115181049"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p13770760181049"><a name="p13770760181049"></a><a name="p13770760181049"></a>Partial restore</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p41689781181049"><a name="p41689781181049"></a><a name="p41689781181049"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p21429119181049"><a name="p21429119181049"></a><a name="p21429119181049"></a>Supported</p>
</td>
</tr>
<tr id="row58644346181049"><td class="cellrowborder" rowspan="4" valign="top" width="19.67%" headers="mcps1.2.5.1.1 "><p id="p52571577181049"><a name="p52571577181049"></a><a name="p52571577181049"></a>Monitoring and alarms</p>
</td>
<td class="cellrowborder" valign="top" width="26.57%" headers="mcps1.2.5.1.2 "><p id="p30439369181049"><a name="p30439369181049"></a><a name="p30439369181049"></a>Resource monitoring</p>
</td>
<td class="cellrowborder" valign="top" width="25.19%" headers="mcps1.2.5.1.3 "><p id="p49669842181049"><a name="p49669842181049"></a><a name="p49669842181049"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.2.5.1.4 "><p id="p63834235181049"><a name="p63834235181049"></a><a name="p63834235181049"></a>Supported</p>
</td>
</tr>
<tr id="row37637203181049"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p44179264181049"><a name="p44179264181049"></a><a name="p44179264181049"></a>DB engine monitoring</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p21750670181049"><a name="p21750670181049"></a><a name="p21750670181049"></a>Not supported</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p16973856181049"><a name="p16973856181049"></a><a name="p16973856181049"></a>Not supported</p>
</td>
</tr>
<tr id="row18546983181049"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p18385351181049"><a name="p18385351181049"></a><a name="p18385351181049"></a>Customize monitoring policies</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p12818452181049"><a name="p12818452181049"></a><a name="p12818452181049"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p31661673181049"><a name="p31661673181049"></a><a name="p31661673181049"></a>Supported</p>
</td>
</tr>
<tr id="row16519607181049"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p4326589181049"><a name="p4326589181049"></a><a name="p4326589181049"></a>Aggregate monitoring items</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p14909460181049"><a name="p14909460181049"></a><a name="p14909460181049"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p66815574181049"><a name="p66815574181049"></a><a name="p66815574181049"></a>Supported</p>
</td>
</tr>
<tr id="row64469260181049"><td class="cellrowborder" rowspan="2" valign="top" width="19.67%" headers="mcps1.2.5.1.1 "><p id="p54627548181049"><a name="p54627548181049"></a><a name="p54627548181049"></a>Parameter management</p>
</td>
<td class="cellrowborder" valign="top" width="26.57%" headers="mcps1.2.5.1.2 "><p id="p62755277181049"><a name="p62755277181049"></a><a name="p62755277181049"></a>Parameter update</p>
</td>
<td class="cellrowborder" valign="top" width="25.19%" headers="mcps1.2.5.1.3 "><p id="p50012678181049"><a name="p50012678181049"></a><a name="p50012678181049"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.2.5.1.4 "><p id="p24495152181049"><a name="p24495152181049"></a><a name="p24495152181049"></a>Supported</p>
</td>
</tr>
<tr id="row19129783181049"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p16933671181049"><a name="p16933671181049"></a><a name="p16933671181049"></a>Parameter template</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p29450093181049"><a name="p29450093181049"></a><a name="p29450093181049"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p36647369181049"><a name="p36647369181049"></a><a name="p36647369181049"></a>Supported</p>
</td>
</tr>
<tr id="row61390865181049"><td class="cellrowborder" rowspan="2" valign="top" width="19.67%" headers="mcps1.2.5.1.1 "><p id="p6604198181049"><a name="p6604198181049"></a><a name="p6604198181049"></a>Log management</p>
</td>
<td class="cellrowborder" valign="top" width="26.57%" headers="mcps1.2.5.1.2 "><p id="p65178052181049"><a name="p65178052181049"></a><a name="p65178052181049"></a>Error logs</p>
</td>
<td class="cellrowborder" valign="top" width="25.19%" headers="mcps1.2.5.1.3 "><p id="p44930834181049"><a name="p44930834181049"></a><a name="p44930834181049"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.2.5.1.4 "><p id="p15518904181049"><a name="p15518904181049"></a><a name="p15518904181049"></a>Supported</p>
</td>
</tr>
<tr id="row5452412181049"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p4253093181049"><a name="p4253093181049"></a><a name="p4253093181049"></a>System running logs</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p8956228181049"><a name="p8956228181049"></a><a name="p8956228181049"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p54365856181049"><a name="p54365856181049"></a><a name="p54365856181049"></a>Supported</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  Differences of database migration

<a name="table51069553181111"></a>
<table><thead align="left"><tr id="row19335080181111"><th class="cellrowborder" valign="top" width="23.3%" id="mcps1.2.4.1.1"><p id="p22637641181111"><a name="p22637641181111"></a><a name="p22637641181111"></a><strong>Function Item</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.65%" id="mcps1.2.4.1.2"><p id="p61168655181111"><a name="p61168655181111"></a><a name="p61168655181111"></a><strong id="b65389415469"><a name="b65389415469"></a><a name="b65389415469"></a>Primary/Standby</strong></p>
</th>
<th class="cellrowborder" valign="top" width="37.05%" id="mcps1.2.4.1.3"><p id="p31664518181111"><a name="p31664518181111"></a><a name="p31664518181111"></a><strong id="b1456364462"><a name="b1456364462"></a><a name="b1456364462"></a>Single</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row37470290181111"><td class="cellrowborder" valign="top" width="23.3%" headers="mcps1.2.4.1.1 "><p id="p15194677181111"><a name="p15194677181111"></a><a name="p15194677181111"></a>Homogeneous data migration</p>
</td>
<td class="cellrowborder" valign="top" width="39.65%" headers="mcps1.2.4.1.2 "><p id="p22809304181111"><a name="p22809304181111"></a><a name="p22809304181111"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="37.05%" headers="mcps1.2.4.1.3 "><p id="p35614307181111"><a name="p35614307181111"></a><a name="p35614307181111"></a>Supported</p>
</td>
</tr>
<tr id="row52093311181111"><td class="cellrowborder" valign="top" width="23.3%" headers="mcps1.2.4.1.1 "><p id="p58808699181111"><a name="p58808699181111"></a><a name="p58808699181111"></a>Heterogeneous data migration</p>
</td>
<td class="cellrowborder" valign="top" width="39.65%" headers="mcps1.2.4.1.2 "><p id="p65884146181111"><a name="p65884146181111"></a><a name="p65884146181111"></a>Not supported</p>
</td>
<td class="cellrowborder" valign="top" width="37.05%" headers="mcps1.2.4.1.3 "><p id="p35015630181111"><a name="p35015630181111"></a><a name="p35015630181111"></a>Not supported</p>
</td>
</tr>
<tr id="row46705222181111"><td class="cellrowborder" valign="top" width="23.3%" headers="mcps1.2.4.1.1 "><p id="p25026612181111"><a name="p25026612181111"></a><a name="p25026612181111"></a>Data synchronization</p>
</td>
<td class="cellrowborder" valign="top" width="39.65%" headers="mcps1.2.4.1.2 "><p id="p13889658181111"><a name="p13889658181111"></a><a name="p13889658181111"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="37.05%" headers="mcps1.2.4.1.3 "><p id="p51320513181111"><a name="p51320513181111"></a><a name="p51320513181111"></a>Supported</p>
</td>
</tr>
</tbody>
</table>

**Table  3**  Differences of database security

<a name="table12903168181132"></a>
<table><thead align="left"><tr id="row21881336181132"><th class="cellrowborder" valign="top" width="23.11%" id="mcps1.2.4.1.1"><p id="p27557761181132"><a name="p27557761181132"></a><a name="p27557761181132"></a><strong>Function Item</strong></p>
</th>
<th class="cellrowborder" valign="top" width="39.839999999999996%" id="mcps1.2.4.1.2"><p id="p45956389151058"><a name="p45956389151058"></a><a name="p45956389151058"></a><strong id="b103389744616"><a name="b103389744616"></a><a name="b103389744616"></a>Primary/Standby</strong></p>
</th>
<th class="cellrowborder" valign="top" width="37.05%" id="mcps1.2.4.1.3"><p id="p66854331151058"><a name="p66854331151058"></a><a name="p66854331151058"></a><strong id="b139617864619"><a name="b139617864619"></a><a name="b139617864619"></a>Single</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row22873626181132"><td class="cellrowborder" valign="top" width="23.11%" headers="mcps1.2.4.1.1 "><p id="p40824399181132"><a name="p40824399181132"></a><a name="p40824399181132"></a>IP address whitelist</p>
</td>
<td class="cellrowborder" valign="top" width="39.839999999999996%" headers="mcps1.2.4.1.2 "><p id="p17410035181132"><a name="p17410035181132"></a><a name="p17410035181132"></a>Not supported</p>
</td>
<td class="cellrowborder" valign="top" width="37.05%" headers="mcps1.2.4.1.3 "><p id="p926770181132"><a name="p926770181132"></a><a name="p926770181132"></a>Not supported</p>
</td>
</tr>
<tr id="row8340938181132"><td class="cellrowborder" valign="top" width="23.11%" headers="mcps1.2.4.1.1 "><p id="p4527340181132"><a name="p4527340181132"></a><a name="p4527340181132"></a>Management audit</p>
</td>
<td class="cellrowborder" valign="top" width="39.839999999999996%" headers="mcps1.2.4.1.2 "><p id="p31170275181132"><a name="p31170275181132"></a><a name="p31170275181132"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="37.05%" headers="mcps1.2.4.1.3 "><p id="p41764375181132"><a name="p41764375181132"></a><a name="p41764375181132"></a>Supported</p>
</td>
</tr>
<tr id="row45746829181132"><td class="cellrowborder" valign="top" width="23.11%" headers="mcps1.2.4.1.1 "><p id="p14505638181132"><a name="p14505638181132"></a><a name="p14505638181132"></a>Storage encryption</p>
</td>
<td class="cellrowborder" valign="top" width="39.839999999999996%" headers="mcps1.2.4.1.2 "><p id="p34105991181132"><a name="p34105991181132"></a><a name="p34105991181132"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="37.05%" headers="mcps1.2.4.1.3 "><p id="p11121881181132"><a name="p11121881181132"></a><a name="p11121881181132"></a>Supported</p>
</td>
</tr>
<tr id="row32988067181132"><td class="cellrowborder" valign="top" width="23.11%" headers="mcps1.2.4.1.1 "><p id="p54787809181132"><a name="p54787809181132"></a><a name="p54787809181132"></a>Network encryption</p>
</td>
<td class="cellrowborder" valign="top" width="39.839999999999996%" headers="mcps1.2.4.1.2 "><p id="p8627555181132"><a name="p8627555181132"></a><a name="p8627555181132"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="37.05%" headers="mcps1.2.4.1.3 "><p id="p27743378181132"><a name="p27743378181132"></a><a name="p27743378181132"></a>Supported</p>
</td>
</tr>
<tr id="row48363813181132"><td class="cellrowborder" valign="top" width="23.11%" headers="mcps1.2.4.1.1 "><p id="p25154818181132"><a name="p25154818181132"></a><a name="p25154818181132"></a>Security group management</p>
</td>
<td class="cellrowborder" valign="top" width="39.839999999999996%" headers="mcps1.2.4.1.2 "><p id="p24274367181132"><a name="p24274367181132"></a><a name="p24274367181132"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="37.05%" headers="mcps1.2.4.1.3 "><p id="p20066692181132"><a name="p20066692181132"></a><a name="p20066692181132"></a>Supported</p>
</td>
</tr>
<tr id="row46382506181132"><td class="cellrowborder" valign="top" width="23.11%" headers="mcps1.2.4.1.1 "><p id="p65995471181132"><a name="p65995471181132"></a><a name="p65995471181132"></a>Transparent Data Encryption (TDE) encryption</p>
</td>
<td class="cellrowborder" valign="top" width="39.839999999999996%" headers="mcps1.2.4.1.2 "><p id="p9896151181132"><a name="p9896151181132"></a><a name="p9896151181132"></a>Supported (Enterprise Edition)</p>
</td>
<td class="cellrowborder" valign="top" width="37.05%" headers="mcps1.2.4.1.3 "><p id="p63390729181132"><a name="p63390729181132"></a><a name="p63390729181132"></a>Supported (Enterprise Edition)</p>
</td>
</tr>
</tbody>
</table>

[Table 4](#table38343542181154)  lists the major differences of the Microsoft SQL Server official editions.

For more information about function differences among Microsoft SQL Server 2014 official editions, see  [official documents](https://docs.microsoft.com/en-us/sql/getting-started/features-supported-by-the-editions-of-sql-server-2014?view=sql-server-2014).

**Table  4**  Differences of SQL Server editions

<a name="table38343542181154"></a>
<table><thead align="left"><tr id="row59652841181154"><th class="cellrowborder" valign="top" width="32.05128205128205%" id="mcps1.2.4.1.1"><p id="p41985181154"><a name="p41985181154"></a><a name="p41985181154"></a><strong>Function Item</strong></p>
</th>
<th class="cellrowborder" valign="top" width="41.02564102564102%" id="mcps1.2.4.1.2"><p id="p30607282181154"><a name="p30607282181154"></a><a name="p30607282181154"></a>Standard Edition</p>
</th>
<th class="cellrowborder" valign="top" width="26.923076923076923%" id="mcps1.2.4.1.3"><p id="p32566346181154"><a name="p32566346181154"></a><a name="p32566346181154"></a>Enterprise Edition</p>
</th>
</tr>
</thead>
<tbody><tr id="row20628371181154"><td class="cellrowborder" valign="top" width="32.05128205128205%" headers="mcps1.2.4.1.1 "><p id="p60285389181154"><a name="p60285389181154"></a><a name="p60285389181154"></a>Instance class</p>
</td>
<td class="cellrowborder" valign="top" width="41.02564102564102%" headers="mcps1.2.4.1.2 "><p id="p51278368181154"><a name="p51278368181154"></a><a name="p51278368181154"></a>16 vCPUs | 128 GB</p>
</td>
<td class="cellrowborder" valign="top" width="26.923076923076923%" headers="mcps1.2.4.1.3 "><p id="p51531170181154"><a name="p51531170181154"></a><a name="p51531170181154"></a>N/A</p>
</td>
</tr>
<tr id="row61127354181154"><td class="cellrowborder" valign="top" width="32.05128205128205%" headers="mcps1.2.4.1.1 "><p id="p52368638181154"><a name="p52368638181154"></a><a name="p52368638181154"></a>High availability</p>
</td>
<td class="cellrowborder" valign="top" width="41.02564102564102%" headers="mcps1.2.4.1.2 "><p id="p14001315181154"><a name="p14001315181154"></a><a name="p14001315181154"></a>Mirror HA</p>
</td>
<td class="cellrowborder" valign="top" width="26.923076923076923%" headers="mcps1.2.4.1.3 "><p id="p1527222931319"><a name="p1527222931319"></a><a name="p1527222931319"></a>Mirror HA</p>
<a name="ul17194171818149"></a><a name="ul17194171818149"></a>
</td>
</tr>
<tr id="row49599143181154"><td class="cellrowborder" valign="top" width="32.05128205128205%" headers="mcps1.2.4.1.1 "><p id="p58107665181154"><a name="p58107665181154"></a><a name="p58107665181154"></a>Data compression</p>
</td>
<td class="cellrowborder" valign="top" width="41.02564102564102%" headers="mcps1.2.4.1.2 "><p id="p9100415181154"><a name="p9100415181154"></a><a name="p9100415181154"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="26.923076923076923%" headers="mcps1.2.4.1.3 "><p id="p66045018181154"><a name="p66045018181154"></a><a name="p66045018181154"></a>Supported</p>
</td>
</tr>
<tr id="row57534251181154"><td class="cellrowborder" valign="top" width="32.05128205128205%" headers="mcps1.2.4.1.1 "><p id="p29762772181154"><a name="p29762772181154"></a><a name="p29762772181154"></a>SQL Profiler</p>
</td>
<td class="cellrowborder" valign="top" width="41.02564102564102%" headers="mcps1.2.4.1.2 "><p id="p61974301181154"><a name="p61974301181154"></a><a name="p61974301181154"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="26.923076923076923%" headers="mcps1.2.4.1.3 "><p id="p53862446181154"><a name="p53862446181154"></a><a name="p53862446181154"></a>Supported</p>
</td>
</tr>
<tr id="row14999969181154"><td class="cellrowborder" valign="top" width="32.05128205128205%" headers="mcps1.2.4.1.1 "><p id="p7038002181154"><a name="p7038002181154"></a><a name="p7038002181154"></a>Column index</p>
</td>
<td class="cellrowborder" valign="top" width="41.02564102564102%" headers="mcps1.2.4.1.2 "><p id="p33207328181154"><a name="p33207328181154"></a><a name="p33207328181154"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="26.923076923076923%" headers="mcps1.2.4.1.3 "><p id="p5439058181154"><a name="p5439058181154"></a><a name="p5439058181154"></a>Supported</p>
</td>
</tr>
<tr id="row48951529181154"><td class="cellrowborder" valign="top" width="32.05128205128205%" headers="mcps1.2.4.1.1 "><p id="p5650876181154"><a name="p5650876181154"></a><a name="p5650876181154"></a>Table/index partitioning</p>
</td>
<td class="cellrowborder" valign="top" width="41.02564102564102%" headers="mcps1.2.4.1.2 "><p id="p19703586312"><a name="p19703586312"></a><a name="p19703586312"></a>Supported by Microsoft SQL Server 2014</p>
</td>
<td class="cellrowborder" valign="top" width="26.923076923076923%" headers="mcps1.2.4.1.3 "><p id="p62672078181154"><a name="p62672078181154"></a><a name="p62672078181154"></a>Supported</p>
</td>
</tr>
<tr id="row27177798181154"><td class="cellrowborder" valign="top" width="32.05128205128205%" headers="mcps1.2.4.1.1 "><p id="p53917992181154"><a name="p53917992181154"></a><a name="p53917992181154"></a>Change Data Capture (CDC)</p>
</td>
<td class="cellrowborder" valign="top" width="41.02564102564102%" headers="mcps1.2.4.1.2 "><p id="p5281247181154"><a name="p5281247181154"></a><a name="p5281247181154"></a>Supported</p>
</td>
<td class="cellrowborder" valign="top" width="26.923076923076923%" headers="mcps1.2.4.1.3 "><p id="p25127891181154"><a name="p25127891181154"></a><a name="p25127891181154"></a>Supported</p>
</td>
</tr>
<tr id="row24824431181154"><td class="cellrowborder" valign="top" width="32.05128205128205%" headers="mcps1.2.4.1.1 "><p id="p64621896181154"><a name="p64621896181154"></a><a name="p64621896181154"></a>Online DDL</p>
</td>
<td class="cellrowborder" valign="top" width="41.02564102564102%" headers="mcps1.2.4.1.2 "><p id="p57571829181154"><a name="p57571829181154"></a><a name="p57571829181154"></a>Not supported</p>
</td>
<td class="cellrowborder" valign="top" width="26.923076923076923%" headers="mcps1.2.4.1.3 "><p id="p32806552181154"><a name="p32806552181154"></a><a name="p32806552181154"></a>Supported</p>
</td>
</tr>
<tr id="row26823513181154"><td class="cellrowborder" valign="top" width="32.05128205128205%" headers="mcps1.2.4.1.1 "><p id="p25220927181154"><a name="p25220927181154"></a><a name="p25220927181154"></a>Parallel searches</p>
</td>
<td class="cellrowborder" valign="top" width="41.02564102564102%" headers="mcps1.2.4.1.2 "><p id="p29629243181154"><a name="p29629243181154"></a><a name="p29629243181154"></a>Not supported</p>
</td>
<td class="cellrowborder" valign="top" width="26.923076923076923%" headers="mcps1.2.4.1.3 "><p id="p51158450181154"><a name="p51158450181154"></a><a name="p51158450181154"></a>Supported</p>
</td>
</tr>
<tr id="row57772872181154"><td class="cellrowborder" valign="top" width="32.05128205128205%" headers="mcps1.2.4.1.1 "><p id="p49091078181154"><a name="p49091078181154"></a><a name="p49091078181154"></a>Adjustment of partitioned table parallelism</p>
</td>
<td class="cellrowborder" valign="top" width="41.02564102564102%" headers="mcps1.2.4.1.2 "><p id="p16954356181154"><a name="p16954356181154"></a><a name="p16954356181154"></a>Not supported</p>
</td>
<td class="cellrowborder" valign="top" width="26.923076923076923%" headers="mcps1.2.4.1.3 "><p id="p31125562181154"><a name="p31125562181154"></a><a name="p31125562181154"></a>Supported</p>
</td>
</tr>
<tr id="row11694606181154"><td class="cellrowborder" valign="top" width="32.05128205128205%" headers="mcps1.2.4.1.1 "><p id="p7739020181154"><a name="p7739020181154"></a><a name="p7739020181154"></a>TDE</p>
</td>
<td class="cellrowborder" valign="top" width="41.02564102564102%" headers="mcps1.2.4.1.2 "><p id="p22880887181154"><a name="p22880887181154"></a><a name="p22880887181154"></a>Not supported</p>
</td>
<td class="cellrowborder" valign="top" width="26.923076923076923%" headers="mcps1.2.4.1.3 "><p id="p41412534181154"><a name="p41412534181154"></a><a name="p41412534181154"></a>Supported</p>
</td>
</tr>
<tr id="row37168489181154"><td class="cellrowborder" valign="top" width="32.05128205128205%" headers="mcps1.2.4.1.1 "><p id="p57857602181154"><a name="p57857602181154"></a><a name="p57857602181154"></a>Integration of advanced R</p>
</td>
<td class="cellrowborder" valign="top" width="41.02564102564102%" headers="mcps1.2.4.1.2 "><p id="p55493023181154"><a name="p55493023181154"></a><a name="p55493023181154"></a>Not supported</p>
</td>
<td class="cellrowborder" valign="top" width="26.923076923076923%" headers="mcps1.2.4.1.3 "><p id="p65749917181154"><a name="p65749917181154"></a><a name="p65749917181154"></a>Supported</p>
</td>
</tr>
</tbody>
</table>


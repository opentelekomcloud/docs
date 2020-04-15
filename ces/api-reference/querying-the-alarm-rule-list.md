# Querying the Alarm Rule List<a name="EN-US_TOPIC_0171212605"></a>

## Function<a name="section66578044"></a>

This API is used to query the alarm rule list. You can specify the paging parameters to limit the number of query results displayed on a page. You can also set the sorting order of query results.

## URI<a name="section62331491"></a>

GET /V1.0/\{project\_id\}/alarms

-   Parameter description

    **Table  1**  Parameter description

    <a name="table31681753175455"></a>
    <table><thead align="left"><tr id="row39882175175455"><th class="cellrowborder" valign="top" width="18.68%" id="mcps1.2.4.1.1"><p id="p9230722175455"><a name="p9230722175455"></a><a name="p9230722175455"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.52%" id="mcps1.2.4.1.2"><p id="p9490989175455"><a name="p9490989175455"></a><a name="p9490989175455"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="47.8%" id="mcps1.2.4.1.3"><p id="p30572649175455"><a name="p30572649175455"></a><a name="p30572649175455"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row60465501175455"><td class="cellrowborder" valign="top" width="18.68%" headers="mcps1.2.4.1.1 "><p id="p65867442175455"><a name="p65867442175455"></a><a name="p65867442175455"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.52%" headers="mcps1.2.4.1.2 "><p id="p33662608175455"><a name="p33662608175455"></a><a name="p33662608175455"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.8%" headers="mcps1.2.4.1.3 "><p id="p42316702175455"><a name="p42316702175455"></a><a name="p42316702175455"></a>Specifies the project ID.</p>
    <p id="p191415137612"><a name="p191415137612"></a><a name="p191415137612"></a>For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  Query parameter description

    <a name="table35416756"></a>
    <table><thead align="left"><tr id="row27598891"><th class="cellrowborder" valign="top" width="18.61186118611861%" id="mcps1.2.5.1.1"><p id="p20917673"><a name="p20917673"></a><a name="p20917673"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.981598159815983%" id="mcps1.2.5.1.2"><p id="p16609919"><a name="p16609919"></a><a name="p16609919"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.85178517851785%" id="mcps1.2.5.1.3"><p id="p1305739116331"><a name="p1305739116331"></a><a name="p1305739116331"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="47.55475547554755%" id="mcps1.2.5.1.4"><p id="p3226198"><a name="p3226198"></a><a name="p3226198"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row59995477"><td class="cellrowborder" valign="top" width="18.61186118611861%" headers="mcps1.2.5.1.1 "><p id="p3210854694927"><a name="p3210854694927"></a><a name="p3210854694927"></a>start</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.981598159815983%" headers="mcps1.2.5.1.2 "><p id="p5065546194927"><a name="p5065546194927"></a><a name="p5065546194927"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.85178517851785%" headers="mcps1.2.5.1.3 "><p id="p5101571116331"><a name="p5101571116331"></a><a name="p5101571116331"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.55475547554755%" headers="mcps1.2.5.1.4 "><p id="p3030830020621"><a name="p3030830020621"></a><a name="p3030830020621"></a>Specifies the first queried alarm to be displayed on a page.</p>
    <p id="p2670812615612"><a name="p2670812615612"></a><a name="p2670812615612"></a>The value is <strong id="b39912972067"><a name="b39912972067"></a><a name="b39912972067"></a>alarm_id</strong>.</p>
    </td>
    </tr>
    <tr id="row14620943"><td class="cellrowborder" valign="top" width="18.61186118611861%" headers="mcps1.2.5.1.1 "><p id="p372561594927"><a name="p372561594927"></a><a name="p372561594927"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.981598159815983%" headers="mcps1.2.5.1.2 "><p id="p3333939594927"><a name="p3333939594927"></a><a name="p3333939594927"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.85178517851785%" headers="mcps1.2.5.1.3 "><p id="p865595815514"><a name="p865595815514"></a><a name="p865595815514"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.55475547554755%" headers="mcps1.2.5.1.4 "><p id="p1613650494927"><a name="p1613650494927"></a><a name="p1613650494927"></a>The value ranges from <strong id="b842352706185456"><a name="b842352706185456"></a><a name="b842352706185456"></a>1</strong> to <strong id="b84235270618550"><a name="b84235270618550"></a><a name="b84235270618550"></a>100</strong>, and is <strong id="b84235270618553"><a name="b84235270618553"></a><a name="b84235270618553"></a>100</strong> by default.</p>
    <p id="p1101081494927"><a name="p1101081494927"></a><a name="p1101081494927"></a>This parameter is used to limit the number of query results.</p>
    </td>
    </tr>
    <tr id="row55056607"><td class="cellrowborder" valign="top" width="18.61186118611861%" headers="mcps1.2.5.1.1 "><p id="p4092925294927"><a name="p4092925294927"></a><a name="p4092925294927"></a>order</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.981598159815983%" headers="mcps1.2.5.1.2 "><p id="p2693508294927"><a name="p2693508294927"></a><a name="p2693508294927"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.85178517851785%" headers="mcps1.2.5.1.3 "><p id="p4217614016331"><a name="p4217614016331"></a><a name="p4217614016331"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="47.55475547554755%" headers="mcps1.2.5.1.4 "><p id="p3425803394927"><a name="p3425803394927"></a><a name="p3425803394927"></a>Specifies the result sorting method, which is sorted by timestamp.</p>
    <p id="p3988684494927"><a name="p3988684494927"></a><a name="p3988684494927"></a>The default value is <strong>desc</strong>.</p>
    <a name="ul27034705141026"></a><a name="ul27034705141026"></a><ul id="ul27034705141026"><li><strong id="b2483023315742"><a name="b2483023315742"></a><a name="b2483023315742"></a>asc</strong>: The query results are displayed in the ascending order.</li><li><strong id="b4315414215754"><a name="b4315414215754"></a><a name="b4315414215754"></a>desc</strong>: The query results are displayed in the descending order.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Example

    Request example 1: Query the current alarm rule list.

    ```
    GET https://{Cloud Eye endpoint}/V1.0/{project_id}/alarms
    ```

    Request example 2: Query the alarm rule list. Start by setting  **alarm\_id**  to  **al1441967036681YkazZ0deN**  and retain 10 records in the descending order of time stamps.

    ```
    GET https://{Cloud Eye endpoint}/V1.0/{project_id}/alarms?start=al1441967036681YkazZ0deN&limit=10&order=desc
    ```


## Request<a name="section24112512"></a>

None

## Response<a name="section15686020"></a>

-   Response parameters

    **Table  3**  Response parameters

    <a name="table42286344152742"></a>
    <table><thead align="left"><tr id="row38095364152742"><th class="cellrowborder" valign="top" width="20.53%" id="mcps1.2.4.1.1"><p id="p65825661152742"><a name="p65825661152742"></a><a name="p65825661152742"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.770000000000001%" id="mcps1.2.4.1.2"><p id="p36622711152742"><a name="p36622711152742"></a><a name="p36622711152742"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="63.7%" id="mcps1.2.4.1.3"><p id="p13649609152742"><a name="p13649609152742"></a><a name="p13649609152742"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row48913836152742"><td class="cellrowborder" valign="top" width="20.53%" headers="mcps1.2.4.1.1 "><p id="p2597784152742"><a name="p2597784152742"></a><a name="p2597784152742"></a>metric_alarms</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.770000000000001%" headers="mcps1.2.4.1.2 "><p id="p65521217152742"><a name="p65521217152742"></a><a name="p65521217152742"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.7%" headers="mcps1.2.4.1.3 "><p id="p5618383152742"><a name="p5618383152742"></a><a name="p5618383152742"></a>Specifies the list of alarm objects.</p>
    <p id="p493519491135"><a name="p493519491135"></a><a name="p493519491135"></a>For details, see <a href="#table10571837131516">Table 4</a>.</p>
    </td>
    </tr>
    <tr id="row185671917132310"><td class="cellrowborder" valign="top" width="20.53%" headers="mcps1.2.4.1.1 "><p id="p244163712152"><a name="p244163712152"></a><a name="p244163712152"></a>meta_data</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.770000000000001%" headers="mcps1.2.4.1.2 "><p id="p64523721512"><a name="p64523721512"></a><a name="p64523721512"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.7%" headers="mcps1.2.4.1.3 "><p id="p645113791514"><a name="p645113791514"></a><a name="p645113791514"></a>Specifies the metadata of query results, including the paging information.</p>
    <p id="p39125515320"><a name="p39125515320"></a><a name="p39125515320"></a>For details, see <a href="#table1933614411408">Table 10</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **metric\_alarms**  field data structure description

    <a name="table10571837131516"></a>
    <table><thead align="left"><tr id="row134453716156"><th class="cellrowborder" valign="top" width="20.53%" id="mcps1.2.4.1.1"><p id="p124463713153"><a name="p124463713153"></a><a name="p124463713153"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.770000000000001%" id="mcps1.2.4.1.2"><p id="p104453761519"><a name="p104453761519"></a><a name="p104453761519"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="63.7%" id="mcps1.2.4.1.3"><p id="p74433718157"><a name="p74433718157"></a><a name="p74433718157"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row248153712151"><td class="cellrowborder" valign="top" width="20.53%" headers="mcps1.2.4.1.1 "><p id="p154723714155"><a name="p154723714155"></a><a name="p154723714155"></a>alarm_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.770000000000001%" headers="mcps1.2.4.1.2 "><p id="p9471437161516"><a name="p9471437161516"></a><a name="p9471437161516"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.7%" headers="mcps1.2.4.1.3 "><p id="p1947193719153"><a name="p1947193719153"></a><a name="p1947193719153"></a>Specifies the name of the alarm.</p>
    </td>
    </tr>
    <tr id="row1748203712158"><td class="cellrowborder" valign="top" width="20.53%" headers="mcps1.2.4.1.1 "><p id="p648113717154"><a name="p648113717154"></a><a name="p648113717154"></a>alarm_description</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.770000000000001%" headers="mcps1.2.4.1.2 "><p id="p1481237151518"><a name="p1481237151518"></a><a name="p1481237151518"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.7%" headers="mcps1.2.4.1.3 "><p id="p124853771516"><a name="p124853771516"></a><a name="p124853771516"></a>Provides supplementary information about the alarm.</p>
    </td>
    </tr>
    <tr id="row19488375152"><td class="cellrowborder" valign="top" width="20.53%" headers="mcps1.2.4.1.1 "><p id="p12481237171510"><a name="p12481237171510"></a><a name="p12481237171510"></a>metric</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.770000000000001%" headers="mcps1.2.4.1.2 "><p id="p984318421173"><a name="p984318421173"></a><a name="p984318421173"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.7%" headers="mcps1.2.4.1.3 "><p id="p124813371158"><a name="p124813371158"></a><a name="p124813371158"></a>Specifies the alarm metric.</p>
    <p id="p15984161314122"><a name="p15984161314122"></a><a name="p15984161314122"></a>For details, see <a href="#table19174559133918">Table 5</a>.</p>
    </td>
    </tr>
    <tr id="row1501437181511"><td class="cellrowborder" valign="top" width="20.53%" headers="mcps1.2.4.1.1 "><p id="p0501937171510"><a name="p0501937171510"></a><a name="p0501937171510"></a>condition</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.770000000000001%" headers="mcps1.2.4.1.2 "><p id="p98879491178"><a name="p98879491178"></a><a name="p98879491178"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.7%" headers="mcps1.2.4.1.3 "><p id="p450143711158"><a name="p450143711158"></a><a name="p450143711158"></a>Specifies the alarm triggering condition.</p>
    <p id="p1099762313419"><a name="p1099762313419"></a><a name="p1099762313419"></a>For details, see <a href="#table1473091124015">Table 9</a>.</p>
    </td>
    </tr>
    <tr id="row8350858143220"><td class="cellrowborder" valign="top" width="20.53%" headers="mcps1.2.4.1.1 "><p id="p65515377157"><a name="p65515377157"></a><a name="p65515377157"></a>alarm_enabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.770000000000001%" headers="mcps1.2.4.1.2 "><p id="p2552377158"><a name="p2552377158"></a><a name="p2552377158"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.7%" headers="mcps1.2.4.1.3 "><p id="p65583771510"><a name="p65583771510"></a><a name="p65583771510"></a>Specifies whether to enable the alarm rule.</p>
    </td>
    </tr>
    <tr id="row12949160173313"><td class="cellrowborder" valign="top" width="20.53%" headers="mcps1.2.4.1.1 "><p id="p1955037121518"><a name="p1955037121518"></a><a name="p1955037121518"></a>alarm_level</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.770000000000001%" headers="mcps1.2.4.1.2 "><p id="p185510371158"><a name="p185510371158"></a><a name="p185510371158"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.7%" headers="mcps1.2.4.1.3 "><p id="p13551237101518"><a name="p13551237101518"></a><a name="p13551237101518"></a>Specifies the alarm severity. The value can be <strong id="b84235270610925"><a name="b84235270610925"></a><a name="b84235270610925"></a>1</strong>, <strong id="b84235270610928"><a name="b84235270610928"></a><a name="b84235270610928"></a>2</strong>, <strong id="b84235270610931"><a name="b84235270610931"></a><a name="b84235270610931"></a>3</strong> or <strong id="b84235270610934"><a name="b84235270610934"></a><a name="b84235270610934"></a>4</strong>, which indicates critical, major, minor, and informational, respectively.</p>
    </td>
    </tr>
    <tr id="row1287162520368"><td class="cellrowborder" valign="top" width="20.53%" headers="mcps1.2.4.1.1 "><p id="p1986042612363"><a name="p1986042612363"></a><a name="p1986042612363"></a>alarm_action_enabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.770000000000001%" headers="mcps1.2.4.1.2 "><p id="p886052617366"><a name="p886052617366"></a><a name="p886052617366"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.7%" headers="mcps1.2.4.1.3 "><p id="p886016267365"><a name="p886016267365"></a><a name="p886016267365"></a>Specifies whether to enable the action to be triggered by an alarm.</p>
    </td>
    </tr>
    <tr id="row253103713155"><td class="cellrowborder" valign="top" width="20.53%" headers="mcps1.2.4.1.1 "><p id="p105217374156"><a name="p105217374156"></a><a name="p105217374156"></a>alarm_actions</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.770000000000001%" headers="mcps1.2.4.1.2 "><p id="p25263719151"><a name="p25263719151"></a><a name="p25263719151"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.7%" headers="mcps1.2.4.1.3 "><p id="p1753183711155"><a name="p1753183711155"></a><a name="p1753183711155"></a>Specifies the action triggered by an alarm.</p>
    <p id="p1783765741713"><a name="p1783765741713"></a><a name="p1783765741713"></a>For details, see <a href="#table569133710159">Table 7</a>.</p>
    </td>
    </tr>
    <tr id="row1755173741512"><td class="cellrowborder" valign="top" width="20.53%" headers="mcps1.2.4.1.1 "><p id="p35410376153"><a name="p35410376153"></a><a name="p35410376153"></a>ok_actions</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.770000000000001%" headers="mcps1.2.4.1.2 "><p id="p105403717151"><a name="p105403717151"></a><a name="p105403717151"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.7%" headers="mcps1.2.4.1.3 "><p id="p1854123711153"><a name="p1854123711153"></a><a name="p1854123711153"></a>Specifies the action triggered by clearing an alarm.</p>
    <p id="p2551537141517"><a name="p2551537141517"></a><a name="p2551537141517"></a>For details, see <a href="#table1819115871510">Table 8</a>.</p>
    </td>
    </tr>
    <tr id="row656837171519"><td class="cellrowborder" valign="top" width="20.53%" headers="mcps1.2.4.1.1 "><p id="p9561337191516"><a name="p9561337191516"></a><a name="p9561337191516"></a>alarm_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.770000000000001%" headers="mcps1.2.4.1.2 "><p id="p55623716158"><a name="p55623716158"></a><a name="p55623716158"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.7%" headers="mcps1.2.4.1.3 "><p id="p756737131515"><a name="p756737131515"></a><a name="p756737131515"></a>Specifies the alarm rule ID.</p>
    </td>
    </tr>
    <tr id="row145720371155"><td class="cellrowborder" valign="top" width="20.53%" headers="mcps1.2.4.1.1 "><p id="p14561537101512"><a name="p14561537101512"></a><a name="p14561537101512"></a>update_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.770000000000001%" headers="mcps1.2.4.1.2 "><p id="p115613719157"><a name="p115613719157"></a><a name="p115613719157"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.7%" headers="mcps1.2.4.1.3 "><p id="p115753721520"><a name="p115753721520"></a><a name="p115753721520"></a>Specifies the time when the alarm status changed. The value is a UNIX timestamp and the unit is ms.</p>
    </td>
    </tr>
    <tr id="row175723717154"><td class="cellrowborder" valign="top" width="20.53%" headers="mcps1.2.4.1.1 "><p id="p1057143761515"><a name="p1057143761515"></a><a name="p1057143761515"></a>alarm_state</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.770000000000001%" headers="mcps1.2.4.1.2 "><p id="p75793721513"><a name="p75793721513"></a><a name="p75793721513"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.7%" headers="mcps1.2.4.1.3 "><p id="p1957143751513"><a name="p1957143751513"></a><a name="p1957143751513"></a>Specifies the alarm status. The value can be:</p>
    <a name="ul195793741513"></a><a name="ul195793741513"></a><ul id="ul195793741513"><li><strong id="b64892893151459"><a name="b64892893151459"></a><a name="b64892893151459"></a>ok</strong>: The alarm status is normal.</li><li><strong id="b51598041151512"><a name="b51598041151512"></a><a name="b51598041151512"></a>alarm</strong>: An alarm is generated.</li><li><strong id="b23034997151525"><a name="b23034997151525"></a><a name="b23034997151525"></a>insufficient_data</strong>: The required data is insufficient.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5**  Field  **metric**  data structure description

    <a name="table19174559133918"></a>
    <table><thead align="left"><tr id="row10174145923910"><th class="cellrowborder" valign="top" width="20.53%" id="mcps1.2.4.1.1"><p id="p117455973917"><a name="p117455973917"></a><a name="p117455973917"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.770000000000001%" id="mcps1.2.4.1.2"><p id="p21751659193910"><a name="p21751659193910"></a><a name="p21751659193910"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="63.7%" id="mcps1.2.4.1.3"><p id="p317575993911"><a name="p317575993911"></a><a name="p317575993911"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1017713594391"><td class="cellrowborder" valign="top" width="20.53%" headers="mcps1.2.4.1.1 "><p id="p31773593392"><a name="p31773593392"></a><a name="p31773593392"></a>namespace</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.770000000000001%" headers="mcps1.2.4.1.2 "><p id="p017765910397"><a name="p017765910397"></a><a name="p017765910397"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.7%" headers="mcps1.2.4.1.3 "><p id="p12933146104119"><a name="p12933146104119"></a><a name="p12933146104119"></a>Query the namespace of a service. For example, see <a href="ecs-metrics.md#en-us_topic_0022067719_section24282572112133">Namespace</a> for ECS namespace.</p>
    </td>
    </tr>
    <tr id="row717815917396"><td class="cellrowborder" valign="top" width="20.53%" headers="mcps1.2.4.1.1 "><p id="p1517812598392"><a name="p1517812598392"></a><a name="p1517812598392"></a>dimensions</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.770000000000001%" headers="mcps1.2.4.1.2 "><p id="p1117805912397"><a name="p1117805912397"></a><a name="p1117805912397"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.7%" headers="mcps1.2.4.1.3 "><p id="p0178195943915"><a name="p0178195943915"></a><a name="p0178195943915"></a>Specifies the list of the metric dimensions.</p>
    <p id="p2613429127"><a name="p2613429127"></a><a name="p2613429127"></a>For details, see <a href="#table7554143164419">Table 6</a>.</p>
    </td>
    </tr>
    <tr id="row95521942102915"><td class="cellrowborder" valign="top" width="20.53%" headers="mcps1.2.4.1.1 "><p id="p13623999153639"><a name="p13623999153639"></a><a name="p13623999153639"></a>metric_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.770000000000001%" headers="mcps1.2.4.1.2 "><p id="p136841954153011"><a name="p136841954153011"></a><a name="p136841954153011"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.7%" headers="mcps1.2.4.1.3 "><p id="p686919215492"><a name="p686919215492"></a><a name="p686919215492"></a>Specifies the metric ID. For example, if the <a href="ecs-metrics.md">monitoring metric</a> of an ECS is CPU usage, <strong id="b1760384213277"><a name="b1760384213277"></a><a name="b1760384213277"></a>metric_name</strong> is <strong id="b196031442112719"><a name="b196031442112719"></a><a name="b196031442112719"></a>cpu_util</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6** **dimensions**  field data structure description

    <a name="table7554143164419"></a>
    <table><thead align="left"><tr id="row1555516374419"><th class="cellrowborder" valign="top" width="20.53%" id="mcps1.2.4.1.1"><p id="p6555193144417"><a name="p6555193144417"></a><a name="p6555193144417"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.770000000000001%" id="mcps1.2.4.1.2"><p id="p125551734448"><a name="p125551734448"></a><a name="p125551734448"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="63.7%" id="mcps1.2.4.1.3"><p id="p1755533204413"><a name="p1755533204413"></a><a name="p1755533204413"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row9558183144414"><td class="cellrowborder" valign="top" width="20.53%" headers="mcps1.2.4.1.1 "><p id="p824618425365"><a name="p824618425365"></a><a name="p824618425365"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.770000000000001%" headers="mcps1.2.4.1.2 "><p id="p3246194283614"><a name="p3246194283614"></a><a name="p3246194283614"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.7%" headers="mcps1.2.4.1.3 "><p id="p132891013125316"><a name="p132891013125316"></a><a name="p132891013125316"></a>Specifies the monitoring dimension. For example, the monitoring dimension of an ECS is <strong id="b1920310112914"><a name="b1920310112914"></a><a name="b1920310112914"></a>instance_id</strong>, which is listed in the <strong id="b132011072915"><a name="b132011072915"></a><a name="b132011072915"></a>key</strong> column in <a href="ecs-metrics.md#en-us_topic_0022067719_section36963297112133">Dimension</a>.</p>
    </td>
    </tr>
    <tr id="row19559235443"><td class="cellrowborder" valign="top" width="20.53%" headers="mcps1.2.4.1.1 "><p id="p5547124122511"><a name="p5547124122511"></a><a name="p5547124122511"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.770000000000001%" headers="mcps1.2.4.1.2 "><p id="p19547154122519"><a name="p19547154122519"></a><a name="p19547154122519"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.7%" headers="mcps1.2.4.1.3 "><p id="p11371113251615"><a name="p11371113251615"></a><a name="p11371113251615"></a>Specifies the dimension value, for example, an ECS ID.</p>
    <p id="p22011213201614"><a name="p22011213201614"></a><a name="p22011213201614"></a>The value is a string of 1 to 256 characters.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  7** **alarm\_actions**  field data structure description

    <a name="table569133710159"></a>
    <table><thead align="left"><tr id="row758183741514"><th class="cellrowborder" valign="top" width="20.53%" id="mcps1.2.4.1.1"><p id="p75815379159"><a name="p75815379159"></a><a name="p75815379159"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.770000000000001%" id="mcps1.2.4.1.2"><p id="p12581537191518"><a name="p12581537191518"></a><a name="p12581537191518"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="63.7%" id="mcps1.2.4.1.3"><p id="p65818370158"><a name="p65818370158"></a><a name="p65818370158"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1565203771511"><td class="cellrowborder" valign="top" width="20.53%" headers="mcps1.2.4.1.1 "><p id="p125751020181418"><a name="p125751020181418"></a><a name="p125751020181418"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.770000000000001%" headers="mcps1.2.4.1.2 "><p id="p96443712157"><a name="p96443712157"></a><a name="p96443712157"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.7%" headers="mcps1.2.4.1.3 "><div class="p" id="p56512371155"><a name="p56512371155"></a><a name="p56512371155"></a>Specifies the alarm notification type.<a name="ul14659377150"></a><a name="ul14659377150"></a><ul id="ul14659377150"><li><strong id="b842352706173134"><a name="b842352706173134"></a><a name="b842352706173134"></a>notification</strong>: indicates that a notification will be sent to the user.</li><li><strong id="b842352706173149"><a name="b842352706173149"></a><a name="b842352706173149"></a>autoscaling</strong>: indicates that a scaling action will be triggered.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="row367193716157"><td class="cellrowborder" valign="top" width="20.53%" headers="mcps1.2.4.1.1 "><p id="p18668378158"><a name="p18668378158"></a><a name="p18668378158"></a>notificationList</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.770000000000001%" headers="mcps1.2.4.1.2 "><p id="p66616375152"><a name="p66616375152"></a><a name="p66616375152"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.7%" headers="mcps1.2.4.1.3 "><p id="p167173715151"><a name="p167173715151"></a><a name="p167173715151"></a>Specifies the list of objects to be notified if the alarm status changes.</p>
    <div class="note" id="note16816125412261"><a name="note16816125412261"></a><a name="note16816125412261"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p18161354152615"><a name="p18161354152615"></a><a name="p18161354152615"></a>The IDs in the list are character strings.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  8** **ok\_actions**  field data structure description

    <a name="table1819115871510"></a>
    <table><thead align="left"><tr id="row18819195814154"><th class="cellrowborder" valign="top" width="20.53%" id="mcps1.2.4.1.1"><p id="p1581985818154"><a name="p1581985818154"></a><a name="p1581985818154"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.770000000000001%" id="mcps1.2.4.1.2"><p id="p1819125819158"><a name="p1819125819158"></a><a name="p1819125819158"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="63.7%" id="mcps1.2.4.1.3"><p id="p1181935841519"><a name="p1181935841519"></a><a name="p1181935841519"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row482075819154"><td class="cellrowborder" valign="top" width="20.53%" headers="mcps1.2.4.1.1 "><p id="p3820558101519"><a name="p3820558101519"></a><a name="p3820558101519"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.770000000000001%" headers="mcps1.2.4.1.2 "><p id="p1682015819157"><a name="p1682015819157"></a><a name="p1682015819157"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.7%" headers="mcps1.2.4.1.3 "><div class="p" id="p68201858141515"><a name="p68201858141515"></a><a name="p68201858141515"></a>Specifies the notification type when an alarm is triggered.<a name="ul108209583156"></a><a name="ul108209583156"></a><ul id="ul108209583156"><li><strong id="b173335218333"><a name="b173335218333"></a><a name="b173335218333"></a>notification</strong>: indicates that a notification will be sent to the user.</li><li><strong id="b154155414336"><a name="b154155414336"></a><a name="b154155414336"></a>autoscaling</strong>: indicates that a scaling action will be triggered.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="row9820115881519"><td class="cellrowborder" valign="top" width="20.53%" headers="mcps1.2.4.1.1 "><p id="p182010585151"><a name="p182010585151"></a><a name="p182010585151"></a>notificationList</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.770000000000001%" headers="mcps1.2.4.1.2 "><p id="p98201858151514"><a name="p98201858151514"></a><a name="p98201858151514"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.7%" headers="mcps1.2.4.1.3 "><p id="p9346141372110"><a name="p9346141372110"></a><a name="p9346141372110"></a>Specifies the ID list of objects to be notified if the alarm status changes.</p>
    <div class="note" id="note1578161452512"><a name="note1578161452512"></a><a name="note1578161452512"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p19791914112518"><a name="p19791914112518"></a><a name="p19791914112518"></a>The IDs in the list are character strings.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  9** **condition**  field data structure description

    <a name="table1473091124015"></a>
    <table><thead align="left"><tr id="row12731417403"><th class="cellrowborder" valign="top" width="20.53%" id="mcps1.2.4.1.1"><p id="p273141134017"><a name="p273141134017"></a><a name="p273141134017"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.770000000000001%" id="mcps1.2.4.1.2"><p id="p673151194014"><a name="p673151194014"></a><a name="p673151194014"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="63.7%" id="mcps1.2.4.1.3"><p id="p273171144015"><a name="p273171144015"></a><a name="p273171144015"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row17351511406"><td class="cellrowborder" valign="top" width="20.53%" headers="mcps1.2.4.1.1 "><p id="p873512116408"><a name="p873512116408"></a><a name="p873512116408"></a>period</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.770000000000001%" headers="mcps1.2.4.1.2 "><p id="p473515110403"><a name="p473515110403"></a><a name="p473515110403"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.7%" headers="mcps1.2.4.1.3 "><p id="p1473517154015"><a name="p1473517154015"></a><a name="p1473517154015"></a>Specifies the interval (seconds) for checking whether the configured alarm rules are met.</p>
    </td>
    </tr>
    <tr id="row573513194010"><td class="cellrowborder" valign="top" width="20.53%" headers="mcps1.2.4.1.1 "><p id="p07357119405"><a name="p07357119405"></a><a name="p07357119405"></a>filter</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.770000000000001%" headers="mcps1.2.4.1.2 "><p id="p167351915402"><a name="p167351915402"></a><a name="p167351915402"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.7%" headers="mcps1.2.4.1.3 "><p id="p2735918404"><a name="p2735918404"></a><a name="p2735918404"></a>Specifies the data rollup method. The following methods are supported:</p>
    <a name="en-us_topic_0046434864_ul7891893153925"></a><a name="en-us_topic_0046434864_ul7891893153925"></a><ul id="en-us_topic_0046434864_ul7891893153925"><li>If <strong id="b92601259788"><a name="b92601259788"></a><a name="b92601259788"></a>Avg.</strong> is selected for <strong id="b162601591584"><a name="b162601591584"></a><a name="b162601591584"></a>Statistic</strong>, Cloud Eye calculates the average value of metric data within a rollup period.</li><li>If <strong id="b103320892"><a name="b103320892"></a><a name="b103320892"></a>Max.</strong> is selected for <strong id="b1034101916"><a name="b1034101916"></a><a name="b1034101916"></a>Statistic</strong>, Cloud Eye calculates the maximum value of metric data within a rollup period.</li><li>If <strong id="b178757017911"><a name="b178757017911"></a><a name="b178757017911"></a>Min.</strong> is selected for <strong id="b28756016916"><a name="b28756016916"></a><a name="b28756016916"></a>Statistic</strong>, Cloud Eye calculates the minimum value of metric data within a rollup period.</li><li>If <strong id="b27407111917"><a name="b27407111917"></a><a name="b27407111917"></a>Sum</strong> is selected for <strong id="b1574110116913"><a name="b1574110116913"></a><a name="b1574110116913"></a>Statistic</strong>, Cloud Eye calculates the sum of metric data within a rollup period.</li><li>If <strong id="b1852602798"><a name="b1852602798"></a><a name="b1852602798"></a>Variance</strong> is selected for <strong id="b152762997"><a name="b152762997"></a><a name="b152762997"></a>Statistic</strong>, Cloud Eye calculates the variance value of metric data within a rollup period.</li></ul>
    </td>
    </tr>
    <tr id="row19735111144010"><td class="cellrowborder" valign="top" width="20.53%" headers="mcps1.2.4.1.1 "><p id="p373614194018"><a name="p373614194018"></a><a name="p373614194018"></a>comparison_operator</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.770000000000001%" headers="mcps1.2.4.1.2 "><p id="p15736191144014"><a name="p15736191144014"></a><a name="p15736191144014"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.7%" headers="mcps1.2.4.1.3 "><p id="p1073613104013"><a name="p1073613104013"></a><a name="p1073613104013"></a>Specifies the comparison condition of alarm thresholds. The value can be <strong id="b1381702318348"><a name="b1381702318348"></a><a name="b1381702318348"></a>&gt;</strong>, <strong id="b4817192353416"><a name="b4817192353416"></a><a name="b4817192353416"></a>=</strong>, <strong id="b168184238345"><a name="b168184238345"></a><a name="b168184238345"></a>&lt;</strong>, <strong id="b188181023143416"><a name="b188181023143416"></a><a name="b188181023143416"></a>≥</strong>, or <strong id="b108197235348"><a name="b108197235348"></a><a name="b108197235348"></a>≤</strong>.</p>
    </td>
    </tr>
    <tr id="row11736131194014"><td class="cellrowborder" valign="top" width="20.53%" headers="mcps1.2.4.1.1 "><p id="p177362134014"><a name="p177362134014"></a><a name="p177362134014"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.770000000000001%" headers="mcps1.2.4.1.2 "><p id="p87361817402"><a name="p87361817402"></a><a name="p87361817402"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.7%" headers="mcps1.2.4.1.3 "><p id="p073611144017"><a name="p073611144017"></a><a name="p073611144017"></a>Specifies the alarm threshold.</p>
    </td>
    </tr>
    <tr id="row873611164014"><td class="cellrowborder" valign="top" width="20.53%" headers="mcps1.2.4.1.1 "><p id="p177361174018"><a name="p177361174018"></a><a name="p177361174018"></a>unit</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.770000000000001%" headers="mcps1.2.4.1.2 "><p id="p137369116403"><a name="p137369116403"></a><a name="p137369116403"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.7%" headers="mcps1.2.4.1.3 "><p id="p197361919403"><a name="p197361919403"></a><a name="p197361919403"></a>Specifies the data unit.</p>
    </td>
    </tr>
    <tr id="row1173614104018"><td class="cellrowborder" valign="top" width="20.53%" headers="mcps1.2.4.1.1 "><p id="p157368134013"><a name="p157368134013"></a><a name="p157368134013"></a>count</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.770000000000001%" headers="mcps1.2.4.1.2 "><p id="p1973711164020"><a name="p1973711164020"></a><a name="p1973711164020"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.7%" headers="mcps1.2.4.1.3 "><p id="p273713184014"><a name="p273713184014"></a><a name="p273713184014"></a>Specifies the number of consecutive times that an alarm is triggered.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  10** **meta\_data**  field data structure description

    <a name="table1933614411408"></a>
    <table><thead align="left"><tr id="row23364419409"><th class="cellrowborder" valign="top" width="20.53%" id="mcps1.2.4.1.1"><p id="p33366416402"><a name="p33366416402"></a><a name="p33366416402"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.770000000000001%" id="mcps1.2.4.1.2"><p id="p163365419400"><a name="p163365419400"></a><a name="p163365419400"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="63.7%" id="mcps1.2.4.1.3"><p id="p5336149404"><a name="p5336149404"></a><a name="p5336149404"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1533794184019"><td class="cellrowborder" valign="top" width="20.53%" headers="mcps1.2.4.1.1 "><p id="p103371641407"><a name="p103371641407"></a><a name="p103371641407"></a>count</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.770000000000001%" headers="mcps1.2.4.1.2 "><p id="p133370434010"><a name="p133370434010"></a><a name="p133370434010"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.7%" headers="mcps1.2.4.1.3 "><p id="p1933717404020"><a name="p1933717404020"></a><a name="p1933717404020"></a>Specifies the number of returned results.</p>
    </td>
    </tr>
    <tr id="row2305156104015"><td class="cellrowborder" valign="top" width="20.53%" headers="mcps1.2.4.1.1 "><p id="p617265794014"><a name="p617265794014"></a><a name="p617265794014"></a>marker</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.770000000000001%" headers="mcps1.2.4.1.2 "><p id="p1172957154015"><a name="p1172957154015"></a><a name="p1172957154015"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.7%" headers="mcps1.2.4.1.3 "><p id="p1817211579405"><a name="p1817211579405"></a><a name="p1817211579405"></a>Specifies the pagination marker.</p>
    <p id="p692093911581"><a name="p692093911581"></a><a name="p692093911581"></a>For example, you have queried 10 records this time and <strong id="b8525107103913"><a name="b8525107103913"></a><a name="b8525107103913"></a>alarm_id</strong> of the tenth record is <strong id="b177335238391"><a name="b177335238391"></a><a name="b177335238391"></a>1441967036681YkazZ0deN</strong>. In your next query, if <strong id="b13527172613810"><a name="b13527172613810"></a><a name="b13527172613810"></a>start</strong> is set to <strong id="b51171648144020"><a name="b51171648144020"></a><a name="b51171648144020"></a>al1441967036681YkazZ0deN</strong>, you can start your query from the next alarm rule ID of <strong id="b15281426103811"><a name="b15281426103811"></a><a name="b15281426103811"></a>al1441967036681YkazZ0deN</strong>.</p>
    </td>
    </tr>
    <tr id="row13379417402"><td class="cellrowborder" valign="top" width="20.53%" headers="mcps1.2.4.1.1 "><p id="p333712424012"><a name="p333712424012"></a><a name="p333712424012"></a>total</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.770000000000001%" headers="mcps1.2.4.1.2 "><p id="p113375414010"><a name="p113375414010"></a><a name="p113375414010"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="63.7%" headers="mcps1.2.4.1.3 "><p id="p233718413401"><a name="p233718413401"></a><a name="p233718413401"></a>Specifies the total number of query results.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "metric_alarms": [
            {
                "alarm_name": "alarm-ttttttt",
                "alarm_description": "",
                "metric": {
                    "namespace": "SYS.ECS",
                    "dimensions": [
                        {
                            "name": "instance_id",
                            "value": "07814c0e-59a1-4fcd-a6fb-56f2f6923046"
                        }
                    ],
                    "metric_name": "cpu_util"
                },
                "condition": {
                    "period": 300,
                    "filter": "average",
                    "comparison_operator": ">=",
                    "value": 0,
                    "unit": "%",
                    "count": 3                
                },
                "alarm_enabled": true,
                "alarm_level": 2,
                "alarm_action_enabled": false,
                "alarm_id": "al15330507498596W7vmlGKL",
                "update_time": 1533050749992,
                "alarm_state": "alarm"
            },
            {
                "alarm_name": "alarm-m5rwxxxxxxx",
                "alarm_description": "",
                "metric": {
                    "namespace": "SYS.ECS",
                    "dimensions": [
                        {
                            "name": "instance_id",
                            "value": "30f3858d-4377-4514-9081-be5bdbf1392e"
                        }
                    ],
                    "metric_name": "network_incoming_bytes_aggregate_rate"
                },
                "condition": {
                    "period": 300,
                    "filter": "average",
                    "comparison_operator": ">=",
                    "value": 12,
                    "unit": "B/s",
                    "count": 3                
                },
                "alarm_enabled": true,
                "alarm_level": 2,
                "alarm_action_enabled": true,
                "alarm_actions": [
                    {
                        "type": "notification",
                        "notificationList": [
                            "urn:smn:region:68438a86d98e427e907e0097b7e35d48:test0315"
                        ]
                    }
                ],
                "ok_actions": [
                    {
                        "type": "notification",
                        "notificationList": [
                            "urn:smn:region:68438a86d98e427e907e0097b7e35d48:test0315"
                        ]
                    }
                ],            
                "alarm_id": "al1533031226533nKJexAlbq",
                "update_time": 1533204036276,
                "alarm_state": "ok"
            }
        ],
        "meta_data": {
            "count": 2,
            "marker": "al1533031226533nKJexAlbq",
            "total": 389
        }
    }
    ```


## Returned Values<a name="section6956456"></a>

-   Normal

    200

-   Abnormal

    <a name="table46793998"></a>
    <table><thead align="left"><tr id="row65573909"><th class="cellrowborder" valign="top" width="31.39%" id="mcps1.1.3.1.1"><p id="p9886408"><a name="p9886408"></a><a name="p9886408"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="68.61%" id="mcps1.1.3.1.2"><p id="p62601592"><a name="p62601592"></a><a name="p62601592"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row37564172"><td class="cellrowborder" valign="top" width="31.39%" headers="mcps1.1.3.1.1 "><p id="p5034751391559"><a name="p5034751391559"></a><a name="p5034751391559"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="68.61%" headers="mcps1.1.3.1.2 "><p id="p5161672091559"><a name="p5161672091559"></a><a name="p5161672091559"></a>Request error</p>
    </td>
    </tr>
    <tr id="row66248115"><td class="cellrowborder" valign="top" width="31.39%" headers="mcps1.1.3.1.1 "><p id="p4762558891559"><a name="p4762558891559"></a><a name="p4762558891559"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="68.61%" headers="mcps1.1.3.1.2 "><p id="p3246739491559"><a name="p3246739491559"></a><a name="p3246739491559"></a>The authentication information is not provided or is incorrect.</p>
    </td>
    </tr>
    <tr id="row44282627"><td class="cellrowborder" valign="top" width="31.39%" headers="mcps1.1.3.1.1 "><p id="p4641015691559"><a name="p4641015691559"></a><a name="p4641015691559"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="68.61%" headers="mcps1.1.3.1.2 "><p id="p112628291559"><a name="p112628291559"></a><a name="p112628291559"></a>You are forbidden to access the page requested.</p>
    </td>
    </tr>
    <tr id="row1815156"><td class="cellrowborder" valign="top" width="31.39%" headers="mcps1.1.3.1.1 "><p id="p1575359891559"><a name="p1575359891559"></a><a name="p1575359891559"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="68.61%" headers="mcps1.1.3.1.2 "><p id="p97307991559"><a name="p97307991559"></a><a name="p97307991559"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row25675773"><td class="cellrowborder" valign="top" width="31.39%" headers="mcps1.1.3.1.1 "><p id="p3828603291559"><a name="p3828603291559"></a><a name="p3828603291559"></a>429 Too Many Requests</p>
    </td>
    <td class="cellrowborder" valign="top" width="68.61%" headers="mcps1.1.3.1.2 "><p id="p1416086091559"><a name="p1416086091559"></a><a name="p1416086091559"></a>Concurrent requests are excessive.</p>
    </td>
    </tr>
    <tr id="row47530006"><td class="cellrowborder" valign="top" width="31.39%" headers="mcps1.1.3.1.1 "><p id="p5561134191559"><a name="p5561134191559"></a><a name="p5561134191559"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="68.61%" headers="mcps1.1.3.1.2 "><p id="p822479291559"><a name="p822479291559"></a><a name="p822479291559"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row20561848"><td class="cellrowborder" valign="top" width="31.39%" headers="mcps1.1.3.1.1 "><p id="p2318494091559"><a name="p2318494091559"></a><a name="p2318494091559"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="68.61%" headers="mcps1.1.3.1.2 "><p id="p6604084791559"><a name="p6604084791559"></a><a name="p6604084791559"></a>The service is currently unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Code<a name="section121612204463"></a>

For details, see  [Error Codes](error-codes.md).


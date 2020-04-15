# Querying Details About a Protected Instance<a name="sdrs_05_0504"></a>

## Function<a name="en-us_topic_0079693002_section34649765"></a>

This API is used to query the details about a protected instance, such as the protected instance ID and name.

## Constraints and Limitations<a name="section11919721173610"></a>

None

## URI<a name="en-us_topic_0079693002_section39390935"></a>

-   URI format

    GET /v1/\{project\_id\}/protected-instances/\{protected\_instance\_id\}

-   Parameter description

    <a name="en-us_topic_0079693002_table63321005"></a>
    <table><thead align="left"><tr id="en-us_topic_0079693002_row37593218"><th class="cellrowborder" valign="top" width="19.801980198019802%" id="mcps1.1.5.1.1"><p id="p12357172051911"><a name="p12357172051911"></a><a name="p12357172051911"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.85148514851485%" id="mcps1.1.5.1.2"><p id="p2357132017191"><a name="p2357132017191"></a><a name="p2357132017191"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.841584158415841%" id="mcps1.1.5.1.3"><p id="p336018202195"><a name="p336018202195"></a><a name="p336018202195"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="49.504950495049506%" id="mcps1.1.5.1.4"><p id="p12360720181917"><a name="p12360720181917"></a><a name="p12360720181917"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0079693002_row29123463"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.1.5.1.1 "><p id="p153601520131916"><a name="p153601520131916"></a><a name="p153601520131916"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.1.5.1.2 "><p id="p3360920181914"><a name="p3360920181914"></a><a name="p3360920181914"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.1.5.1.3 "><p id="p7360172041919"><a name="p7360172041919"></a><a name="p7360172041919"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.504950495049506%" headers="mcps1.1.5.1.4 "><p id="p83606200194"><a name="p83606200194"></a><a name="p83606200194"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row36505554367"><td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.1.5.1.1 "><p id="p173602206193"><a name="p173602206193"></a><a name="p173602206193"></a>protected_instance_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.1.5.1.2 "><p id="p1360192001914"><a name="p1360192001914"></a><a name="p1360192001914"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.1.5.1.3 "><p id="p13606201197"><a name="p13606201197"></a><a name="p13606201197"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.504950495049506%" headers="mcps1.1.5.1.4 "><p id="p336052015194"><a name="p336052015194"></a><a name="p336052015194"></a>Specifies the ID of a protected instance.</p>
    <p id="p431715368536"><a name="p431715368536"></a><a name="p431715368536"></a>You can obtain this value by calling the API described in <a href="querying-protected-instances.md">Querying Protected Instances</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="en-us_topic_0079693002_section18974100"></a>

-   Request parameters

    None

-   Example request

    GET https://\{Endpoint\}/v1/\{project\_id\}/protected-instances/50f5091e-9e9e-473c-a932-2a2cbcbeb1ff


## Response<a name="en-us_topic_0079693002_section36549175"></a>

-   Parameter description

    <a name="table155991608555"></a>
    <table><thead align="left"><tr id="row460510055518"><th class="cellrowborder" valign="top" width="29.07%" id="mcps1.1.4.1.1"><p id="p14250742111914"><a name="p14250742111914"></a><a name="p14250742111914"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.44%" id="mcps1.1.4.1.2"><p id="p15250184231911"><a name="p15250184231911"></a><a name="p15250184231911"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.49%" id="mcps1.1.4.1.3"><p id="p13250154213194"><a name="p13250154213194"></a><a name="p13250154213194"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row86164025512"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.1.4.1.1 "><p id="p825044241918"><a name="p825044241918"></a><a name="p825044241918"></a>protected_instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.1.4.1.2 "><p id="p725034219195"><a name="p725034219195"></a><a name="p725034219195"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.1.4.1.3 "><p id="p625024241915"><a name="p625024241915"></a><a name="p625024241915"></a>Specifies the details about a protected instance.</p>
    <p id="p17342112914428"><a name="p17342112914428"></a><a name="p17342112914428"></a>For details, see <a href="#table503353570">Table 1</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  1** **protected\_instance**  field description

    <a name="table503353570"></a>
    <table><thead align="left"><tr id="row131163505710"><th class="cellrowborder" valign="top" width="29.07%" id="mcps1.2.4.1.1"><p id="p03441519152018"><a name="p03441519152018"></a><a name="p03441519152018"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.44%" id="mcps1.2.4.1.2"><p id="p163442199204"><a name="p163442199204"></a><a name="p163442199204"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.49%" id="mcps1.2.4.1.3"><p id="p23441019192017"><a name="p23441019192017"></a><a name="p23441019192017"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1829133585715"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p334481919202"><a name="p334481919202"></a><a name="p334481919202"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p1534471916207"><a name="p1534471916207"></a><a name="p1534471916207"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p334410198202"><a name="p334410198202"></a><a name="p334410198202"></a>Specifies the ID of a protected instance.</p>
    </td>
    </tr>
    <tr id="row1472144614199"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p634411195205"><a name="p634411195205"></a><a name="p634411195205"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p193462197201"><a name="p193462197201"></a><a name="p193462197201"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p1134651919204"><a name="p1134651919204"></a><a name="p1134651919204"></a>Specifies the name of a protected instance.</p>
    </td>
    </tr>
    <tr id="row1845264811918"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p728082303815"><a name="p728082303815"></a><a name="p728082303815"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p10281152311381"><a name="p10281152311381"></a><a name="p10281152311381"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p13938102503810"><a name="p13938102503810"></a><a name="p13938102503810"></a>Specifies the description of a protected instance.</p>
    </td>
    </tr>
    <tr id="row17518129211"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p2346181922016"><a name="p2346181922016"></a><a name="p2346181922016"></a>server_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p17346181962015"><a name="p17346181962015"></a><a name="p17346181962015"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p434610198206"><a name="p434610198206"></a><a name="p434610198206"></a>Specifies the ID of a protection group.</p>
    </td>
    </tr>
    <tr id="row2503145051917"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p33460190209"><a name="p33460190209"></a><a name="p33460190209"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p934641914204"><a name="p934641914204"></a><a name="p934641914204"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p178191229125515"><a name="p178191229125515"></a><a name="p178191229125515"></a>Specifies the status of a protected instance.</p>
    <p id="p5346101912203"><a name="p5346101912203"></a><a name="p5346101912203"></a>For details, see <a href="protected-instance-status.md">Protected Instance Status</a>.</p>
    </td>
    </tr>
    <tr id="row48001133192112"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p14745142282317"><a name="p14745142282317"></a><a name="p14745142282317"></a>progress</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p1830712716181"><a name="p1830712716181"></a><a name="p1830712716181"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p1330727191818"><a name="p1330727191818"></a><a name="p1330727191818"></a>Specifies the synchronization progress of a protected instance.</p>
    <p id="p12307127121818"><a name="p12307127121818"></a><a name="p12307127121818"></a>Unit: %</p>
    </td>
    </tr>
    <tr id="row3249105663714"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p434641919209"><a name="p434641919209"></a><a name="p434641919209"></a>source_server</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p6346619152016"><a name="p6346619152016"></a><a name="p6346619152016"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p63468191204"><a name="p63468191204"></a><a name="p63468191204"></a>Specifies the production site server ID.</p>
    </td>
    </tr>
    <tr id="row9260185815378"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p9346181902015"><a name="p9346181902015"></a><a name="p9346181902015"></a>target_server</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p1234691982014"><a name="p1234691982014"></a><a name="p1234691982014"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p13460195209"><a name="p13460195209"></a><a name="p13460195209"></a>Specifies the DR site server ID.</p>
    </td>
    </tr>
    <tr id="row5347324382"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p18346181912018"><a name="p18346181912018"></a><a name="p18346181912018"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p1934661932015"><a name="p1934661932015"></a><a name="p1934661932015"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p13346819162010"><a name="p13346819162010"></a><a name="p13346819162010"></a>Specifies the time when a protected instance was created.</p>
    <p id="p1238764484715"><a name="p1238764484715"></a><a name="p1238764484715"></a>The default format is as follows: "yyyy-MM-dd HH:mm:ss.SSS", for example, <strong id="b206451829102020"><a name="b206451829102020"></a><a name="b206451829102020"></a>2019-04-01 12:00:00.000</strong>.</p>
    </td>
    </tr>
    <tr id="row1554004153812"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p19346141972015"><a name="p19346141972015"></a><a name="p19346141972015"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p20346111915205"><a name="p20346111915205"></a><a name="p20346111915205"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p834631914201"><a name="p834631914201"></a><a name="p834631914201"></a>Specifies the time when a protected instance was updated.</p>
    <p id="p161491348164710"><a name="p161491348164710"></a><a name="p161491348164710"></a>The default format is as follows: "yyyy-MM-dd HH:mm:ss.SSS", for example, <strong id="b1913136152014"><a name="b1913136152014"></a><a name="b1913136152014"></a>2019-04-01 12:00:00.000</strong>.</p>
    </td>
    </tr>
    <tr id="row1105164182213"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p10235944142418"><a name="p10235944142418"></a><a name="p10235944142418"></a>priority_station</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p10235154410245"><a name="p10235154410245"></a><a name="p10235154410245"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p382553192519"><a name="p382553192519"></a><a name="p382553192519"></a>Specifies the current production site AZ of the protection group containing the protected instance.</p>
    <a name="ul782135312518"></a><a name="ul782135312518"></a><ul id="ul782135312518"><li><strong id="b1692613418249"><a name="b1692613418249"></a><a name="b1692613418249"></a>source</strong>: indicates that the current production site AZ is the <strong id="b2092783492417"><a name="b2092783492417"></a><a name="b2092783492417"></a>source_availability_zone</strong> value.</li><li><strong id="b3960194018246"><a name="b3960194018246"></a><a name="b3960194018246"></a>target</strong>: indicates that the current production site AZ is the <strong id="b1796254020248"><a name="b1796254020248"></a><a name="b1796254020248"></a>target_availability_zone</strong> value.</li></ul>
    </td>
    </tr>
    <tr id="row438192514586"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1374517342565"><a name="p1374517342565"></a><a name="p1374517342565"></a>attachment</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p474543475616"><a name="p474543475616"></a><a name="p474543475616"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p1674513345564"><a name="p1674513345564"></a><a name="p1674513345564"></a>Specifies the attached replication pairs.</p>
    <p id="p694373217614"><a name="p694373217614"></a><a name="p694373217614"></a>For details, see <a href="#table179273775819">Table 2</a>.</p>
    </td>
    </tr>
    <tr id="row1778712421624"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p198281231145613"><a name="p198281231145613"></a><a name="p198281231145613"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p20771154912569"><a name="p20771154912569"></a><a name="p20771154912569"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p15241635617"><a name="p15241635617"></a><a name="p15241635617"></a>Specifies the tag list.</p>
    <p id="p1374110263247"><a name="p1374110263247"></a><a name="p1374110263247"></a>For details, see <a href="#table537215313717">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="row107854424217"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p6472615185719"><a name="p6472615185719"></a><a name="p6472615185719"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p10709144620575"><a name="p10709144620575"></a><a name="p10709144620575"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p370974645720"><a name="p370974645720"></a><a name="p370974645720"></a>Specifies the metadata of a protected instance.</p>
    <p id="p47468535551"><a name="p47468535551"></a><a name="p47468535551"></a>For details, see <a href="#table18286124016331">Table 4</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2** **attachment**  field description

    <a name="table179273775819"></a>
    <table><thead align="left"><tr id="row1492813755816"><th class="cellrowborder" valign="top" width="28.9028902890289%" id="mcps1.2.4.1.1"><p id="p292811711582"><a name="p292811711582"></a><a name="p292811711582"></a><strong id="b105701169456"><a name="b105701169456"></a><a name="b105701169456"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.331733173317332%" id="mcps1.2.4.1.2"><p id="p11928107165814"><a name="p11928107165814"></a><a name="p11928107165814"></a><strong id="b15968197194515"><a name="b15968197194515"></a><a name="b15968197194515"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.765376537653765%" id="mcps1.2.4.1.3"><p id="p129289712588"><a name="p129289712588"></a><a name="p129289712588"></a><strong id="b20831594456"><a name="b20831594456"></a><a name="b20831594456"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row792810795814"><td class="cellrowborder" valign="top" width="28.9028902890289%" headers="mcps1.2.4.1.1 "><p id="p392816745818"><a name="p392816745818"></a><a name="p392816745818"></a>replication</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.331733173317332%" headers="mcps1.2.4.1.2 "><p id="p69286711582"><a name="p69286711582"></a><a name="p69286711582"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.765376537653765%" headers="mcps1.2.4.1.3 "><p id="p14719113310"><a name="p14719113310"></a><a name="p14719113310"></a>Specifies the ID of a replication pair.</p>
    </td>
    </tr>
    <tr id="row69284725813"><td class="cellrowborder" valign="top" width="28.9028902890289%" headers="mcps1.2.4.1.1 "><p id="p139281074588"><a name="p139281074588"></a><a name="p139281074588"></a>device</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.331733173317332%" headers="mcps1.2.4.1.2 "><p id="p1192813705820"><a name="p1192813705820"></a><a name="p1192813705820"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.765376537653765%" headers="mcps1.2.4.1.3 "><p id="p99281876589"><a name="p99281876589"></a><a name="p99281876589"></a>Specifies the device name.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **tags**  field description

    <a name="table537215313717"></a>
    <table><thead align="left"><tr id="row133739314717"><th class="cellrowborder" valign="top" width="29.13291329132913%" id="mcps1.2.4.1.1"><p id="p23731337718"><a name="p23731337718"></a><a name="p23731337718"></a><strong id="b3346101513459"><a name="b3346101513459"></a><a name="b3346101513459"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.071707170717072%" id="mcps1.2.4.1.2"><p id="p53739312717"><a name="p53739312717"></a><a name="p53739312717"></a><strong id="b95027161456"><a name="b95027161456"></a><a name="b95027161456"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.7953795379538%" id="mcps1.2.4.1.3"><p id="p193731731972"><a name="p193731731972"></a><a name="p193731731972"></a><strong id="b17293917194510"><a name="b17293917194510"></a><a name="b17293917194510"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row12373831710"><td class="cellrowborder" valign="top" width="29.13291329132913%" headers="mcps1.2.4.1.1 "><p id="p1337323171"><a name="p1337323171"></a><a name="p1337323171"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.071707170717072%" headers="mcps1.2.4.1.2 "><p id="p5373831670"><a name="p5373831670"></a><a name="p5373831670"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.7953795379538%" headers="mcps1.2.4.1.3 "><p id="p1688242248"><a name="p1688242248"></a><a name="p1688242248"></a>Specifies the tag key.</p>
    </td>
    </tr>
    <tr id="row163731831173"><td class="cellrowborder" valign="top" width="29.13291329132913%" headers="mcps1.2.4.1.1 "><p id="p1237315315710"><a name="p1237315315710"></a><a name="p1237315315710"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.071707170717072%" headers="mcps1.2.4.1.2 "><p id="p163731338716"><a name="p163731338716"></a><a name="p163731338716"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.7953795379538%" headers="mcps1.2.4.1.3 "><p id="p1237320316714"><a name="p1237320316714"></a><a name="p1237320316714"></a>Specifies the tag value.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  Field  **metadata**  description

    <a name="table18286124016331"></a>
    <table><thead align="left"><tr id="row1228734016335"><th class="cellrowborder" valign="top" width="29.14291429142914%" id="mcps1.2.4.1.1"><p id="p18958174419296"><a name="p18958174419296"></a><a name="p18958174419296"></a><strong id="b02071348152010"><a name="b02071348152010"></a><a name="b02071348152010"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.511751175117514%" id="mcps1.2.4.1.2"><p id="p12958154420296"><a name="p12958154420296"></a><a name="p12958154420296"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.34533453345335%" id="mcps1.2.4.1.3"><p id="p395816448297"><a name="p395816448297"></a><a name="p395816448297"></a><strong id="b105591313192412"><a name="b105591313192412"></a><a name="b105591313192412"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row132895406331"><td class="cellrowborder" valign="top" width="29.14291429142914%" headers="mcps1.2.4.1.1 "><p id="p1558353082720"><a name="p1558353082720"></a><a name="p1558353082720"></a>__system__frozen</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.511751175117514%" headers="mcps1.2.4.1.2 "><p id="p11583730102710"><a name="p11583730102710"></a><a name="p11583730102710"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.34533453345335%" headers="mcps1.2.4.1.3 "><p id="p958313303271"><a name="p958313303271"></a><a name="p958313303271"></a>Specifies whether the resource is frozen.</p>
    <a name="ul529114370311"></a><a name="ul529114370311"></a><ul id="ul529114370311"><li><strong id="b13821111715247"><a name="b13821111715247"></a><a name="b13821111715247"></a>true</strong>: indicates that the resource is frozen.</li><li>Empty: indicates that the resource is not frozen.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
        "protected_instance": {
            "id": "50f5091e-9e9e-473c-a932-2a2cbcbeb1ff",
            "name": "ecs_sdrs_test",
            "description": "1111",
            "server_group_id": "943c7d15-0371-4b89-b1a6-db1ef35c9263",
            "status": "available",
            "progress": 0,
            "source_server": "5fb92d6c-b0cb-46c9-824b-b90ec5500ae6",
            "target_server": "c6c0ff54-fa1f-43ef-9ccc-1774e40c8745",
            "created_at": "2018-11-06 09:27:52.258",
            "updated_at": "2018-11-06 09:44:59.853",
            "priority_station": "target",
            "attachment": [
                {
                    "replication": "6568f7c4-0510-4f39-929d-8ffccbd4fd47",
                    "device": "/dev/vda"
                }
            ],
            "tags": [
                {                   
                    "key": "aaaaaaa",                   
                    "value": "01234567889"               
                 },                
                 {                   
                    "key": "ffffff",                   
                    "value": "dddd"
                  }
                ],
             "metadata": {} 
        }
    }
    
    ```

    Or

    ```
    { 
         "error": { 
             "message": "XXXX",  
             "code": "XXX" 
         } 
     }
    ```

    In this example,  **error**  represents a general error, including  **badrequest**  \(shown below\) and  **itemNotFound**.

    ```
    { 
         "badrequest": { 
             "message": "XXXX",  
             "code": "XXX" 
         } 
     }
    ```


## Returned Values<a name="en-us_topic_0079693002_section60507121"></a>

-   Normal

    <a name="sdrs_05_0101_table4315991194956"></a>
    <table><thead align="left"><tr id="sdrs_05_0101_row2336641294956"><th class="cellrowborder" valign="top" width="42.59%" id="mcps1.1.3.1.1"><p id="sdrs_05_0101_p1363125894956"><a name="sdrs_05_0101_p1363125894956"></a><a name="sdrs_05_0101_p1363125894956"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.410000000000004%" id="mcps1.1.3.1.2"><p id="sdrs_05_0101_p3039012494956"><a name="sdrs_05_0101_p3039012494956"></a><a name="sdrs_05_0101_p3039012494956"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="sdrs_05_0101_row507566794956"><td class="cellrowborder" valign="top" width="42.59%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p847584694956"><a name="sdrs_05_0101_p847584694956"></a><a name="sdrs_05_0101_p847584694956"></a>200</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.410000000000004%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p1545496394956"><a name="sdrs_05_0101_p1545496394956"></a><a name="sdrs_05_0101_p1545496394956"></a>The server has accepted the request.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    <a name="sdrs_05_0101_table22458872203835"></a>
    <table><thead align="left"><tr id="sdrs_05_0101_row35704554203835"><th class="cellrowborder" valign="top" width="43.419999999999995%" id="mcps1.1.3.1.1"><p id="sdrs_05_0101_p6387753203835"><a name="sdrs_05_0101_p6387753203835"></a><a name="sdrs_05_0101_p6387753203835"></a>Returned Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="56.58%" id="mcps1.1.3.1.2"><p id="sdrs_05_0101_p47646009203835"><a name="sdrs_05_0101_p47646009203835"></a><a name="sdrs_05_0101_p47646009203835"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="sdrs_05_0101_row34121538203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p12381163203835"><a name="sdrs_05_0101_p12381163203835"></a><a name="sdrs_05_0101_p12381163203835"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p63350108203835"><a name="sdrs_05_0101_p63350108203835"></a><a name="sdrs_05_0101_p63350108203835"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row33280063203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p11330608203835"><a name="sdrs_05_0101_p11330608203835"></a><a name="sdrs_05_0101_p11330608203835"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p45364094203835"><a name="sdrs_05_0101_p45364094203835"></a><a name="sdrs_05_0101_p45364094203835"></a>You must enter a username and the password to access the requested page.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row5623667203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p52863895203835"><a name="sdrs_05_0101_p52863895203835"></a><a name="sdrs_05_0101_p52863895203835"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p54117066203835"><a name="sdrs_05_0101_p54117066203835"></a><a name="sdrs_05_0101_p54117066203835"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row17291554203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p58438642203835"><a name="sdrs_05_0101_p58438642203835"></a><a name="sdrs_05_0101_p58438642203835"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p35909542203835"><a name="sdrs_05_0101_p35909542203835"></a><a name="sdrs_05_0101_p35909542203835"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row54750425203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p5599455203835"><a name="sdrs_05_0101_p5599455203835"></a><a name="sdrs_05_0101_p5599455203835"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p50902717203835"><a name="sdrs_05_0101_p50902717203835"></a><a name="sdrs_05_0101_p50902717203835"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row55471277203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p63988484203835"><a name="sdrs_05_0101_p63988484203835"></a><a name="sdrs_05_0101_p63988484203835"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p15684678203835"><a name="sdrs_05_0101_p15684678203835"></a><a name="sdrs_05_0101_p15684678203835"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row6944380203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p25623884203835"><a name="sdrs_05_0101_p25623884203835"></a><a name="sdrs_05_0101_p25623884203835"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p62268733203835"><a name="sdrs_05_0101_p62268733203835"></a><a name="sdrs_05_0101_p62268733203835"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row23547689203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p28314670203835"><a name="sdrs_05_0101_p28314670203835"></a><a name="sdrs_05_0101_p28314670203835"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p11786919203835"><a name="sdrs_05_0101_p11786919203835"></a><a name="sdrs_05_0101_p11786919203835"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row38973411203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p2729702203835"><a name="sdrs_05_0101_p2729702203835"></a><a name="sdrs_05_0101_p2729702203835"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p19779281203835"><a name="sdrs_05_0101_p19779281203835"></a><a name="sdrs_05_0101_p19779281203835"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row43795805203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p57799353203835"><a name="sdrs_05_0101_p57799353203835"></a><a name="sdrs_05_0101_p57799353203835"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p51235984203835"><a name="sdrs_05_0101_p51235984203835"></a><a name="sdrs_05_0101_p51235984203835"></a>Failed to complete the request because of a service error.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row58470678203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p38504500203835"><a name="sdrs_05_0101_p38504500203835"></a><a name="sdrs_05_0101_p38504500203835"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p31856770203835"><a name="sdrs_05_0101_p31856770203835"></a><a name="sdrs_05_0101_p31856770203835"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row18275474203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p3918444203835"><a name="sdrs_05_0101_p3918444203835"></a><a name="sdrs_05_0101_p3918444203835"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p48958538203835"><a name="sdrs_05_0101_p48958538203835"></a><a name="sdrs_05_0101_p48958538203835"></a>Failed to complete the request because the server receives an invalid response from an upstream server.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row37973662203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p55967806203835"><a name="sdrs_05_0101_p55967806203835"></a><a name="sdrs_05_0101_p55967806203835"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p37098455203835"><a name="sdrs_05_0101_p37098455203835"></a><a name="sdrs_05_0101_p37098455203835"></a>Failed to complete the request because the system is unavailable.</p>
    </td>
    </tr>
    <tr id="sdrs_05_0101_row65450640203835"><td class="cellrowborder" valign="top" width="43.419999999999995%" headers="mcps1.1.3.1.1 "><p id="sdrs_05_0101_p67010448203835"><a name="sdrs_05_0101_p67010448203835"></a><a name="sdrs_05_0101_p67010448203835"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.58%" headers="mcps1.1.3.1.2 "><p id="sdrs_05_0101_p59137180203835"><a name="sdrs_05_0101_p59137180203835"></a><a name="sdrs_05_0101_p59137180203835"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>



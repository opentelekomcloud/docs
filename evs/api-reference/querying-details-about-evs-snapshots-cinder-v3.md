# Querying Details About EVS Snapshots<a name="evs_04_3060"></a>

## Function<a name="section63129217111110"></a>

This API is used to query details about the EVS snapshots.

## URI<a name="section21460443111127"></a>

-   URI format

    GET /v3/\{project\_id\}/snapshots/detail

-   Parameter description

    <a name="table9361875111127"></a>
    <table><thead align="left"><tr id="row34794340111127"><th class="cellrowborder" valign="top" width="28.57%" id="mcps1.1.4.1.1"><p id="p66878179111127"><a name="p66878179111127"></a><a name="p66878179111127"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="26.529999999999998%" id="mcps1.1.4.1.2"><p id="p48423414111127"><a name="p48423414111127"></a><a name="p48423414111127"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="44.9%" id="mcps1.1.4.1.3"><p id="p147761015152112"><a name="p147761015152112"></a><a name="p147761015152112"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row12660986111127"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p18906939111127"><a name="p18906939111127"></a><a name="p18906939111127"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.1.4.1.2 "><p id="p55067056111127"><a name="p55067056111127"></a><a name="p55067056111127"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.9%" headers="mcps1.1.4.1.3 "><p id="p31246529111127"><a name="p31246529111127"></a><a name="p31246529111127"></a>Specifies the project ID.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Request filter parameters

    <a name="en-us_topic_0051408627_table49657902111140"></a>
    <table><thead align="left"><tr id="en-us_topic_0051408627_row47265217111140"><th class="cellrowborder" valign="top" width="17%" id="mcps1.1.5.1.1"><p id="en-us_topic_0051408627_p3277402111140"><a name="en-us_topic_0051408627_p3277402111140"></a><a name="en-us_topic_0051408627_p3277402111140"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="19%" id="mcps1.1.5.1.2"><p id="en-us_topic_0051408627_p64143015111140"><a name="en-us_topic_0051408627_p64143015111140"></a><a name="en-us_topic_0051408627_p64143015111140"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.1.5.1.3"><p id="en-us_topic_0051408627_p28201745111140"><a name="en-us_topic_0051408627_p28201745111140"></a><a name="en-us_topic_0051408627_p28201745111140"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="49%" id="mcps1.1.5.1.4"><p id="en-us_topic_0051408627_p2639999111140"><a name="en-us_topic_0051408627_p2639999111140"></a><a name="en-us_topic_0051408627_p2639999111140"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row19129165444110"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0058762430_p49168107152914"><a name="en-us_topic_0058762430_p49168107152914"></a><a name="en-us_topic_0058762430_p49168107152914"></a>marker</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0058762430_p23193765152914"><a name="en-us_topic_0058762430_p23193765152914"></a><a name="en-us_topic_0058762430_p23193765152914"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0058762430_p66755704152914"><a name="en-us_topic_0058762430_p66755704152914"></a><a name="en-us_topic_0058762430_p66755704152914"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0058762430_p38502923152914"><a name="en-us_topic_0058762430_p38502923152914"></a><a name="en-us_topic_0058762430_p38502923152914"></a><span id="text127381323152311"><a name="text127381323152311"></a><a name="text127381323152311"></a>Specifies the ID of the last record on the previous page. The returned value is the value of the item after this one.</span></p>
    </td>
    </tr>
    <tr id="en-us_topic_0051408627_row23759995111140"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0051408627_p45511467111140"><a name="en-us_topic_0051408627_p45511467111140"></a><a name="en-us_topic_0051408627_p45511467111140"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0051408627_p62550228111140"><a name="en-us_topic_0051408627_p62550228111140"></a><a name="en-us_topic_0051408627_p62550228111140"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0051408627_p33403677111140"><a name="en-us_topic_0051408627_p33403677111140"></a><a name="en-us_topic_0051408627_p33403677111140"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0051408627_p21343278111140"><a name="en-us_topic_0051408627_p21343278111140"></a><a name="en-us_topic_0051408627_p21343278111140"></a>Specifies the offset.</p>
    <div class="note" id="en-us_topic_0051408627_note6490498915441"><a name="en-us_topic_0051408627_note6490498915441"></a><a name="en-us_topic_0051408627_note6490498915441"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0051408627_p4727398915441"><a name="en-us_topic_0051408627_p4727398915441"></a><a name="en-us_topic_0051408627_p4727398915441"></a>This parameter is used when snapshots are queried by page and is used together with the <strong id="b842352706185037"><a name="b842352706185037"></a><a name="b842352706185037"></a>limit</strong> parameter. For example, there are a total of 30 snapshots. If you set <strong id="b84235270618483"><a name="b84235270618483"></a><a name="b84235270618483"></a>offset</strong> to <strong id="b84235270618488"><a name="b84235270618488"></a><a name="b84235270618488"></a>11</strong> and <strong id="b842352706184813"><a name="b842352706184813"></a><a name="b842352706184813"></a>limit</strong> to <strong id="b842352706184818"><a name="b842352706184818"></a><a name="b842352706184818"></a>10</strong>, the queried snapshot starts from the twelfth snapshot, and at most 10 snapshots can be queried at a time.</p>
    </div></div>
    </td>
    </tr>
    <tr id="en-us_topic_0051408627_row57871777111140"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0051408627_p57102386111140"><a name="en-us_topic_0051408627_p57102386111140"></a><a name="en-us_topic_0051408627_p57102386111140"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0051408627_p61890592111140"><a name="en-us_topic_0051408627_p61890592111140"></a><a name="en-us_topic_0051408627_p61890592111140"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0051408627_p47082066111140"><a name="en-us_topic_0051408627_p47082066111140"></a><a name="en-us_topic_0051408627_p47082066111140"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0051408627_p55551025111140"><a name="en-us_topic_0051408627_p55551025111140"></a><a name="en-us_topic_0051408627_p55551025111140"></a>Specifies the maximum number of query results that can be returned.</p>
    <p id="p12396191941414"><a name="p12396191941414"></a><a name="p12396191941414"></a><span id="text138349551887"><a name="text138349551887"></a><a name="text138349551887"></a>The value ranges from 1 to 1000, and the default value is 1000. The returned value cannot exceed this limit.</span></p>
    <p id="en-us_topic_0051408627_p14657115572511"><a name="en-us_topic_0051408627_p14657115572511"></a><a name="en-us_topic_0051408627_p14657115572511"></a>If the tenant has more than 50 snapshots in total, you are advised to use this parameter and set its value to <strong id="b8423527069161"><a name="b8423527069161"></a><a name="b8423527069161"></a>50</strong> to improve the query efficiency. Examples are provided as follows:</p>
    <p id="en-us_topic_0051408627_p1233994321914"><a name="en-us_topic_0051408627_p1233994321914"></a><a name="en-us_topic_0051408627_p1233994321914"></a><strong id="b1616195497104021"><a name="b1616195497104021"></a><a name="b1616195497104021"></a>GET /v3/</strong><em id="i198955286104021"><a name="i198955286104021"></a><a name="i198955286104021"></a>xxx</em><strong id="b1630661680104021"><a name="b1630661680104021"></a><a name="b1630661680104021"></a>/snapshots/detail?limit=50</strong>: Queries the 1–50 snapshots. <strong id="b842352706104032"><a name="b842352706104032"></a><a name="b842352706104032"></a>GET /v3/</strong><em id="i1290684130104029"><a name="i1290684130104029"></a><a name="i1290684130104029"></a>xxx</em><strong id="b842352706104037"><a name="b842352706104037"></a><a name="b842352706104037"></a>/snapshots/detail?offset=50&amp;limit=50</strong>: Queries the 51–100 snapshots.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0051408627_row30197180111140"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0051408627_p30052553111140"><a name="en-us_topic_0051408627_p30052553111140"></a><a name="en-us_topic_0051408627_p30052553111140"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0051408627_p18337718111140"><a name="en-us_topic_0051408627_p18337718111140"></a><a name="en-us_topic_0051408627_p18337718111140"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0051408627_p8960171111140"><a name="en-us_topic_0051408627_p8960171111140"></a><a name="en-us_topic_0051408627_p8960171111140"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0051408627_p54685265111140"><a name="en-us_topic_0051408627_p54685265111140"></a><a name="en-us_topic_0051408627_p54685265111140"></a>Specifies the snapshot name. The value can contain a maximum of 255 bytes.</p>
    </td>
    </tr>
    <tr id="row475111724717"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.1 "><p id="p463319195457"><a name="p463319195457"></a><a name="p463319195457"></a>sort_dir</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.5.1.2 "><p id="p1163321984520"><a name="p1163321984520"></a><a name="p1163321984520"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.3 "><p id="p663321934517"><a name="p663321934517"></a><a name="p663321934517"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49%" headers="mcps1.1.5.1.4 "><div class="p" id="p2030231013183"><a name="p2030231013183"></a><a name="p2030231013183"></a>Specifies the result sorting order. The default value is <strong id="b82711154299"><a name="b82711154299"></a><a name="b82711154299"></a>desc</strong>.<a name="ul66131813171815"></a><a name="ul66131813171815"></a><ul id="ul66131813171815"><li><strong id="b163431692919"><a name="b163431692919"></a><a name="b163431692919"></a>desc</strong>: indicates the descending order.</li><li><strong id="b13867141642912"><a name="b13867141642912"></a><a name="b13867141642912"></a>asc</strong>: indicates the ascending order.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="en-us_topic_0051408627_row22405342111140"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0051408627_p2893391111140"><a name="en-us_topic_0051408627_p2893391111140"></a><a name="en-us_topic_0051408627_p2893391111140"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0051408627_p33038150111140"><a name="en-us_topic_0051408627_p33038150111140"></a><a name="en-us_topic_0051408627_p33038150111140"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0051408627_p58844456111140"><a name="en-us_topic_0051408627_p58844456111140"></a><a name="en-us_topic_0051408627_p58844456111140"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0051408627_p1671647111140"><a name="en-us_topic_0051408627_p1671647111140"></a><a name="en-us_topic_0051408627_p1671647111140"></a>Specifies the snapshot status. For details, see <a href="evs-snapshot-status.md">EVS Snapshot Status</a>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0051408627_row15044830111140"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0051408627_p10671727111140"><a name="en-us_topic_0051408627_p10671727111140"></a><a name="en-us_topic_0051408627_p10671727111140"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0051408627_p59103560111140"><a name="en-us_topic_0051408627_p59103560111140"></a><a name="en-us_topic_0051408627_p59103560111140"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0051408627_p22659090111140"><a name="en-us_topic_0051408627_p22659090111140"></a><a name="en-us_topic_0051408627_p22659090111140"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0051408627_p23447029111140"><a name="en-us_topic_0051408627_p23447029111140"></a><a name="en-us_topic_0051408627_p23447029111140"></a>Specifies the ID of the snapshot's source disk.</p>
    </td>
    </tr>
    <tr id="row117612774718"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.1 "><p id="p5719104616512"><a name="p5719104616512"></a><a name="p5719104616512"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.5.1.2 "><p id="p871944695111"><a name="p871944695111"></a><a name="p871944695111"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.3 "><p id="p12719134675113"><a name="p12719134675113"></a><a name="p12719134675113"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49%" headers="mcps1.1.5.1.4 "><p id="p77601351115119"><a name="p77601351115119"></a><a name="p77601351115119"></a>Specifies the metadata filtered query in the {'key':'value'} format.</p>
    <p id="p971944611514"><a name="p971944611514"></a><a name="p971944611514"></a>This parameter is supported when the request version is 3.22 or later.</p>
    </td>
    </tr>
    <tr id="row876327144712"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.1 "><p id="p1355262793315"><a name="p1355262793315"></a><a name="p1355262793315"></a>name~</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.5.1.2 "><p id="p15552102720334"><a name="p15552102720334"></a><a name="p15552102720334"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.3 "><p id="p12552102719334"><a name="p12552102719334"></a><a name="p12552102719334"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49%" headers="mcps1.1.5.1.4 "><p id="p11552182715331"><a name="p11552182715331"></a><a name="p11552182715331"></a>Specifies the fuzzy search by disk name. This parameter is supported when the request version is 3.31 or later.</p>
    </td>
    </tr>
    <tr id="row0763117134717"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.1 "><p id="p555232714335"><a name="p555232714335"></a><a name="p555232714335"></a>status~</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.5.1.2 "><p id="p11553122753313"><a name="p11553122753313"></a><a name="p11553122753313"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.3 "><p id="p1955322717338"><a name="p1955322717338"></a><a name="p1955322717338"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49%" headers="mcps1.1.5.1.4 "><p id="p25531427163315"><a name="p25531427163315"></a><a name="p25531427163315"></a>Specifies the fuzzy search by disk status. This parameter is supported when the request version is 3.31 or later.</p>
    </td>
    </tr>
    <tr id="row476310716477"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.1 "><p id="p1268088124912"><a name="p1268088124912"></a><a name="p1268088124912"></a>volume_id~</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.5.1.2 "><p id="p1668012820493"><a name="p1668012820493"></a><a name="p1668012820493"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.3 "><p id="p1968058154912"><a name="p1968058154912"></a><a name="p1968058154912"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49%" headers="mcps1.1.5.1.4 "><p id="p768018824914"><a name="p768018824914"></a><a name="p768018824914"></a>Specifies the fuzzy search by the ID of the disk that corresponds to the snapshot. This parameter is supported when the request version is 3.31 or later.</p>
    </td>
    </tr>
    <tr id="row47631575476"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.1 "><p id="p668115818494"><a name="p668115818494"></a><a name="p668115818494"></a>sort_key</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.5.1.2 "><p id="p176812811492"><a name="p176812811492"></a><a name="p176812811492"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.3 "><p id="p468111819494"><a name="p468111819494"></a><a name="p468111819494"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49%" headers="mcps1.1.5.1.4 "><p id="p2068120884920"><a name="p2068120884920"></a><a name="p2068120884920"></a>Specifies the sorting query by name (sort_key=name). This parameter is supported when the request version is 3.30 or later. The default sorting order is the descending order.</p>
    </td>
    </tr>
    <tr id="row147636754711"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.5.1.1 "><p id="p155547276337"><a name="p155547276337"></a><a name="p155547276337"></a>with_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="19%" headers="mcps1.1.5.1.2 "><p id="p855442773311"><a name="p855442773311"></a><a name="p855442773311"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.3 "><p id="p1055420271339"><a name="p1055420271339"></a><a name="p1055420271339"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49%" headers="mcps1.1.5.1.4 "><p id="p355419276334"><a name="p355419276334"></a><a name="p355419276334"></a>Specifies to return parameter <strong id="b842352706111032"><a name="b842352706111032"></a><a name="b842352706111032"></a>counts</strong> in the response. This parameter indicates the number of snapshots queried. This parameter is in the <em id="i842352697111123"><a name="i842352697111123"></a><a name="i842352697111123"></a>with_count=true</em> format and is supported when the request version is 3.45 or later.</p>
    <p id="p1459918123014"><a name="p1459918123014"></a><a name="p1459918123014"></a>This parameter can be used together with parameters <strong id="evs_04_3032_b842352706155655"><a name="evs_04_3032_b842352706155655"></a><a name="evs_04_3032_b842352706155655"></a>marker</strong>, <strong id="evs_04_3032_b842352706155659"><a name="evs_04_3032_b842352706155659"></a><a name="evs_04_3032_b842352706155659"></a>limit</strong>, <strong id="evs_04_3032_b84235270615572"><a name="evs_04_3032_b84235270615572"></a><a name="evs_04_3032_b84235270615572"></a>sort_key</strong>, <strong id="evs_04_3032_b84235270615576"><a name="evs_04_3032_b84235270615576"></a><a name="evs_04_3032_b84235270615576"></a>sort_dir</strong>, or <strong id="evs_04_3032_b842352706155718"><a name="evs_04_3032_b842352706155718"></a><a name="evs_04_3032_b842352706155718"></a>offset</strong> in the table. It cannot be used with other filter parameters.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section45527389"></a>

The following example shows how to query details of the snapshots in the  **available**  state.

-   Example request

    ```
    GET https://{endpoint}/v3/{project_id}/snapshots/detail?status=available
    ```


## Response<a name="section3672851111434"></a>

-   Parameter description

    <a name="table410874917199"></a>
    <table><thead align="left"><tr id="row191081949171912"><th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.1"><p id="p910894918193"><a name="p910894918193"></a><a name="p910894918193"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.2"><p id="p10108124917198"><a name="p10108124917198"></a><a name="p10108124917198"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.14%" id="mcps1.1.4.1.3"><p id="p21092049111914"><a name="p21092049111914"></a><a name="p21092049111914"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row210984917198"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="p1110918496191"><a name="p1110918496191"></a><a name="p1110918496191"></a>snapshots</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p71092049171917"><a name="p71092049171917"></a><a name="p71092049171917"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p1510954919191"><a name="p1510954919191"></a><a name="p1510954919191"></a>Specifies the snapshot information. For details, see <a href="#en-us_topic_0051408627_li60262741111434">Parameters in the snapshots field</a>.</p>
    </td>
    </tr>
    <tr id="row423792912203"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="p13109154941914"><a name="p13109154941914"></a><a name="p13109154941914"></a>snapshots_links</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p19109154931910"><a name="p19109154931910"></a><a name="p19109154931910"></a>list&lt;map&lt;String,String&gt;&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p9109649111919"><a name="p9109649111919"></a><a name="p9109649111919"></a>Specifies the query position marker in the snapshot list. This parameter is at the same level as parameter <strong id="b8408616173112"><a name="b8408616173112"></a><a name="b8408616173112"></a>snapshots</strong> in the response body. This parameter is returned only when parameter <strong id="b12408131613313"><a name="b12408131613313"></a><a name="b12408131613313"></a>limit</strong> is specified in the request, and this parameter indicates that only some snapshots are returned in this query.</p>
    </td>
    </tr>
    <tr id="row41117491194"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="p611224941917"><a name="p611224941917"></a><a name="p611224941917"></a>count</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p1911211493192"><a name="p1911211493192"></a><a name="p1911211493192"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p6112184910193"><a name="p6112184910193"></a><a name="p6112184910193"></a>Specifies the number of records returned in this query.</p>
    </td>
    </tr>
    <tr id="row203891619182012"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="p129522216412"><a name="p129522216412"></a><a name="p129522216412"></a>error</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p1595262111415"><a name="p1595262111415"></a><a name="p1595262111415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p109527215417"><a name="p109527215417"></a><a name="p109527215417"></a>Specifies the error message returned when an error occurs. For details, see <a href="#li0419202382514">Parameters in the error field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   <a name="en-us_topic_0051408627_li60262741111434"></a>Parameters in the  **snapshots**  field

    <a name="en-us_topic_0051408627_table5493760111434"></a>
    <table><thead align="left"><tr id="en-us_topic_0051408627_row9951929111434"><th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.1"><p id="en-us_topic_0051408627_p799881111434"><a name="en-us_topic_0051408627_p799881111434"></a><a name="en-us_topic_0051408627_p799881111434"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.2"><p id="en-us_topic_0051408627_p64790373111434"><a name="en-us_topic_0051408627_p64790373111434"></a><a name="en-us_topic_0051408627_p64790373111434"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.14%" id="mcps1.1.4.1.3"><p id="en-us_topic_0051408627_p22098020111434"><a name="en-us_topic_0051408627_p22098020111434"></a><a name="en-us_topic_0051408627_p22098020111434"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0051408627_row30338895111434"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0051408627_p41531445111434"><a name="en-us_topic_0051408627_p41531445111434"></a><a name="en-us_topic_0051408627_p41531445111434"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0051408627_p8603891111434"><a name="en-us_topic_0051408627_p8603891111434"></a><a name="en-us_topic_0051408627_p8603891111434"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0051408627_p11580698111434"><a name="en-us_topic_0051408627_p11580698111434"></a><a name="en-us_topic_0051408627_p11580698111434"></a>Specifies the snapshot ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0051408627_row37117420111434"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0051408627_p53721059111434"><a name="en-us_topic_0051408627_p53721059111434"></a><a name="en-us_topic_0051408627_p53721059111434"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0051408627_p56438551111434"><a name="en-us_topic_0051408627_p56438551111434"></a><a name="en-us_topic_0051408627_p56438551111434"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0051408627_p53733716111434"><a name="en-us_topic_0051408627_p53733716111434"></a><a name="en-us_topic_0051408627_p53733716111434"></a>Specifies the snapshot status. For details, see <a href="evs-snapshot-status.md">EVS Snapshot Status</a>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0051408627_row13841398111434"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0051408627_p47411481111434"><a name="en-us_topic_0051408627_p47411481111434"></a><a name="en-us_topic_0051408627_p47411481111434"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0051408627_p15124732111434"><a name="en-us_topic_0051408627_p15124732111434"></a><a name="en-us_topic_0051408627_p15124732111434"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0051408627_p46466595111434"><a name="en-us_topic_0051408627_p46466595111434"></a><a name="en-us_topic_0051408627_p46466595111434"></a>Specifies the snapshot name.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0051408627_row15546175111434"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0051408627_p51280630111434"><a name="en-us_topic_0051408627_p51280630111434"></a><a name="en-us_topic_0051408627_p51280630111434"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0051408627_p60090386111434"><a name="en-us_topic_0051408627_p60090386111434"></a><a name="en-us_topic_0051408627_p60090386111434"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0051408627_p55561368111434"><a name="en-us_topic_0051408627_p55561368111434"></a><a name="en-us_topic_0051408627_p55561368111434"></a>Specifies the snapshot description.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0051408627_row30290270111434"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0051408627_p37592805111434"><a name="en-us_topic_0051408627_p37592805111434"></a><a name="en-us_topic_0051408627_p37592805111434"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0051408627_p25118356111434"><a name="en-us_topic_0051408627_p25118356111434"></a><a name="en-us_topic_0051408627_p25118356111434"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0051408627_p49277837111434"><a name="en-us_topic_0051408627_p49277837111434"></a><a name="en-us_topic_0051408627_p49277837111434"></a>Specifies the time when the snapshot was created.</p>
    <p id="p191521633192117"><a name="p191521633192117"></a><a name="p191521633192117"></a><span id="text152359383212"><a name="text152359383212"></a><a name="text152359383212"></a>Time format: UTC YYYY-MM-DDTHH:MM:SS.XXXXXX</span></p>
    </td>
    </tr>
    <tr id="en-us_topic_0051408627_row62090946113559"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0051408627_p4553543411364"><a name="en-us_topic_0051408627_p4553543411364"></a><a name="en-us_topic_0051408627_p4553543411364"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0051408627_p6449156711364"><a name="en-us_topic_0051408627_p6449156711364"></a><a name="en-us_topic_0051408627_p6449156711364"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0051408627_p778860311364"><a name="en-us_topic_0051408627_p778860311364"></a><a name="en-us_topic_0051408627_p778860311364"></a>Specifies the time when the snapshot was updated.</p>
    <p id="p17722194212116"><a name="p17722194212116"></a><a name="p17722194212116"></a><span id="text1096915422211"><a name="text1096915422211"></a><a name="text1096915422211"></a>Time format: UTC YYYY-MM-DDTHH:MM:SS.XXXXXX</span></p>
    </td>
    </tr>
    <tr id="en-us_topic_0051408627_row40847350111434"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0051408627_p20301014111434"><a name="en-us_topic_0051408627_p20301014111434"></a><a name="en-us_topic_0051408627_p20301014111434"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0051408627_p33769410111434"><a name="en-us_topic_0051408627_p33769410111434"></a><a name="en-us_topic_0051408627_p33769410111434"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0051408627_p34744289111434"><a name="en-us_topic_0051408627_p34744289111434"></a><a name="en-us_topic_0051408627_p34744289111434"></a>Specifies the snapshot metadata.</p>
    <p id="p1678772717473"><a name="p1678772717473"></a><a name="p1678772717473"></a>If <strong id="b842352706193018"><a name="b842352706193018"></a><a name="b842352706193018"></a>metadata</strong> contains the <strong id="b842352706193021"><a name="b842352706193021"></a><a name="b842352706193021"></a>__system__enableActive</strong> field, the snapshot is automatically created during the backup of a server.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0051408627_row44263150111434"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0051408627_p28545410111434"><a name="en-us_topic_0051408627_p28545410111434"></a><a name="en-us_topic_0051408627_p28545410111434"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0051408627_p30476837111434"><a name="en-us_topic_0051408627_p30476837111434"></a><a name="en-us_topic_0051408627_p30476837111434"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0051408627_p41227967111434"><a name="en-us_topic_0051408627_p41227967111434"></a><a name="en-us_topic_0051408627_p41227967111434"></a>Specifies the ID of the snapshot's source disk.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0051408627_row35507385111434"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0051408627_p57525930111434"><a name="en-us_topic_0051408627_p57525930111434"></a><a name="en-us_topic_0051408627_p57525930111434"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0051408627_p29088719111434"><a name="en-us_topic_0051408627_p29088719111434"></a><a name="en-us_topic_0051408627_p29088719111434"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0051408627_p60586455111434"><a name="en-us_topic_0051408627_p60586455111434"></a><a name="en-us_topic_0051408627_p60586455111434"></a>Specifies the snapshot size, in GB.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0051408627_row8407183111434"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0051408627_p9893207111434"><a name="en-us_topic_0051408627_p9893207111434"></a><a name="en-us_topic_0051408627_p9893207111434"></a>os-extended-snapshot-attributes:project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0051408627_p63152279111434"><a name="en-us_topic_0051408627_p63152279111434"></a><a name="en-us_topic_0051408627_p63152279111434"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0051408627_p11980193111434"><a name="en-us_topic_0051408627_p11980193111434"></a><a name="en-us_topic_0051408627_p11980193111434"></a>Specifies the tenant ID. <span id="text19941457165313"><a name="text19941457165313"></a><a name="text19941457165313"></a>The tenant ID is actually the project ID.</span></p>
    </td>
    </tr>
    <tr id="en-us_topic_0051408627_row40712881111434"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0051408627_p9409050111434"><a name="en-us_topic_0051408627_p9409050111434"></a><a name="en-us_topic_0051408627_p9409050111434"></a>os-extended-snapshot-attributes:progress</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0051408627_p23935584111434"><a name="en-us_topic_0051408627_p23935584111434"></a><a name="en-us_topic_0051408627_p23935584111434"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0051408627_p6625696111434"><a name="en-us_topic_0051408627_p6625696111434"></a><a name="en-us_topic_0051408627_p6625696111434"></a><span id="text4730642777"><a name="text4730642777"></a><a name="text4730642777"></a>Reserved field</span></p>
    </td>
    </tr>
    <tr id="row11295723102014"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="p95423280203"><a name="p95423280203"></a><a name="p95423280203"></a>user_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p1354218288209"><a name="p1354218288209"></a><a name="p1354218288209"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p845483673211"><a name="p845483673211"></a><a name="p845483673211"></a>Reserved field</p>
    </td>
    </tr>
    </tbody>
    </table>


-   <a name="li0419202382514"></a>Parameters in the  **error**  field

    <a name="evs_04_2013_table15441099103019"></a>
    <table><thead align="left"><tr id="evs_04_2013_row54094047103019"><th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.1"><p id="evs_04_2013_p19541716103019"><a name="evs_04_2013_p19541716103019"></a><a name="evs_04_2013_p19541716103019"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.2"><p id="evs_04_2013_p39375186103019"><a name="evs_04_2013_p39375186103019"></a><a name="evs_04_2013_p39375186103019"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.64423557644236%" id="mcps1.1.4.1.3"><p id="evs_04_2013_p38578950103019"><a name="evs_04_2013_p38578950103019"></a><a name="evs_04_2013_p38578950103019"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="evs_04_2013_row59401790103019"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="evs_04_2013_p46815658103019"><a name="evs_04_2013_p46815658103019"></a><a name="evs_04_2013_p46815658103019"></a>message</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="evs_04_2013_p33971979103019"><a name="evs_04_2013_p33971979103019"></a><a name="evs_04_2013_p33971979103019"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="evs_04_2013_p21623243103019"><a name="evs_04_2013_p21623243103019"></a><a name="evs_04_2013_p21623243103019"></a>Specifies the error message returned when an error occurs.</p>
    </td>
    </tr>
    <tr id="evs_04_2013_row60391466103019"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="evs_04_2013_p59870541103019"><a name="evs_04_2013_p59870541103019"></a><a name="evs_04_2013_p59870541103019"></a>code</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="evs_04_2013_p17675690103019"><a name="evs_04_2013_p17675690103019"></a><a name="evs_04_2013_p17675690103019"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="evs_04_2013_p6087468103019"><a name="evs_04_2013_p6087468103019"></a><a name="evs_04_2013_p6087468103019"></a>Specifies the error code returned when an error occurs.</p>
    <p id="evs_04_2013_p54787218103019"><a name="evs_04_2013_p54787218103019"></a><a name="evs_04_2013_p54787218103019"></a>For details about the error code, see <a href="error-codes.md">Error Codes</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "count": 2, 
        "snapshots": [
            {
                "status": "available", 
                "os-extended-snapshot-attributes:progress": "100%", 
                "description": null, 
                "created_at": "2013-06-19T07:15:29.000000", 
                "metadata": { }, 
                "volume_id": "ae11e59c-bd56-434a-a00c-04757e1c066d", 
                "os-extended-snapshot-attributes:project_id": "d6c277ba8820452e83df36f33c9fa561", 
                "size": 5, 
                "id": "6cd26877-3ca3-4f4e-ae2a-38cc3d6183fa", 
                "name": "name_xx2-snap", 
                "updated_at": null, 
                "user_id": "48d70679b8644035846b2cb53633c256"
            }, 
            {
                "status": "available", 
                "os-extended-snapshot-attributes:progress": "100%", 
                "description": null, 
                "created_at": "2013-06-19T09:08:08.000000", 
                "metadata": { }, 
                "volume_id": "ae11e59c-bd56-434a-a00c-04757e1c066d", 
                "os-extended-snapshot-attributes:project_id": "d6c277ba8820452e83df36f33c9fa561", 
                "size": 5, 
                "id": "b3253e26-5c37-48dd-8bf2-8795dd1e848f", 
                "name": "name_xx2-snap", 
                "updated_at": null, 
                "user_id": "48d70679b8644035846b2cb53633c256"
            }
        ]
    }
    ```

    or

    ```
    {
        "error": {
            "message": "XXXX", 
            "code": "XXX"
        }
    }
    ```

    In the preceding example,  **error**  indicates a general error, for example,  **badRequest**  or  **itemNotFound**. An example is provided as follows:

    ```
    {
        "itemNotFound": {
            "message": "XXXX", 
            "code": "XXX"
        }
    }
    ```


## Status Codes<a name="section7038241111643"></a>

-   Normal

    200


## Error Codes<a name="section431317151242"></a>

For details, see  [Error Codes](error-codes.md).


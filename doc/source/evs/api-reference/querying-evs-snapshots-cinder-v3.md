# Querying EVS Snapshots<a name="evs_04_3059"></a>

## Function<a name="section5262172611544"></a>

This API is used to query the EVS snapshots.

## URI<a name="section1511931811555"></a>

-   URI format

    GET /v3/\{project\_id\}/snapshots

-   Parameter description

    <a name="table1448127211555"></a>
    <table><thead align="left"><tr id="row3175017111555"><th class="cellrowborder" valign="top" width="28.57%" id="mcps1.1.4.1.1"><p id="p2162703411555"><a name="p2162703411555"></a><a name="p2162703411555"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="26.529999999999998%" id="mcps1.1.4.1.2"><p id="p695931811555"><a name="p695931811555"></a><a name="p695931811555"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="44.9%" id="mcps1.1.4.1.3"><p id="p2683384611555"><a name="p2683384611555"></a><a name="p2683384611555"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2605789011555"><td class="cellrowborder" valign="top" width="28.57%" headers="mcps1.1.4.1.1 "><p id="p3031437111555"><a name="p3031437111555"></a><a name="p3031437111555"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.529999999999998%" headers="mcps1.1.4.1.2 "><p id="p3954502511555"><a name="p3954502511555"></a><a name="p3954502511555"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.9%" headers="mcps1.1.4.1.3 "><p id="p4903046711555"><a name="p4903046711555"></a><a name="p4903046711555"></a>Specifies the project ID.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Request filter parameters

    <a name="en-us_topic_0051408626_table633033061168"></a>
    <table><thead align="left"><tr id="en-us_topic_0051408626_row57109071168"><th class="cellrowborder" valign="top" width="16.831683168316832%" id="mcps1.1.5.1.1"><p id="en-us_topic_0051408626_p599303181168"><a name="en-us_topic_0051408626_p599303181168"></a><a name="en-us_topic_0051408626_p599303181168"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.81188118811881%" id="mcps1.1.5.1.2"><p id="en-us_topic_0051408626_p225175981168"><a name="en-us_topic_0051408626_p225175981168"></a><a name="en-us_topic_0051408626_p225175981168"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.841584158415841%" id="mcps1.1.5.1.3"><p id="en-us_topic_0051408626_p119861301168"><a name="en-us_topic_0051408626_p119861301168"></a><a name="en-us_topic_0051408626_p119861301168"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="48.51485148514851%" id="mcps1.1.5.1.4"><p id="en-us_topic_0051408626_p313524671168"><a name="en-us_topic_0051408626_p313524671168"></a><a name="en-us_topic_0051408626_p313524671168"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1869818449417"><td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0058762430_p49168107152914"><a name="en-us_topic_0058762430_p49168107152914"></a><a name="en-us_topic_0058762430_p49168107152914"></a>marker</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0058762430_p23193765152914"><a name="en-us_topic_0058762430_p23193765152914"></a><a name="en-us_topic_0058762430_p23193765152914"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0058762430_p66755704152914"><a name="en-us_topic_0058762430_p66755704152914"></a><a name="en-us_topic_0058762430_p66755704152914"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0058762430_p38502923152914"><a name="en-us_topic_0058762430_p38502923152914"></a><a name="en-us_topic_0058762430_p38502923152914"></a><span id="text127381323152311"><a name="text127381323152311"></a><a name="text127381323152311"></a>Specifies the ID of the last record on the previous page. The returned value is the value of the item after this one.</span></p>
    </td>
    </tr>
    <tr id="en-us_topic_0051408626_row137367471168"><td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0051408626_p389347291168"><a name="en-us_topic_0051408626_p389347291168"></a><a name="en-us_topic_0051408626_p389347291168"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0051408626_p667053841168"><a name="en-us_topic_0051408626_p667053841168"></a><a name="en-us_topic_0051408626_p667053841168"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0051408626_p344270561168"><a name="en-us_topic_0051408626_p344270561168"></a><a name="en-us_topic_0051408626_p344270561168"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0051408626_p371281361168"><a name="en-us_topic_0051408626_p371281361168"></a><a name="en-us_topic_0051408626_p371281361168"></a>Specifies the offset.</p>
    <div class="note" id="en-us_topic_0051408626_note6490498915441"><a name="en-us_topic_0051408626_note6490498915441"></a><a name="en-us_topic_0051408626_note6490498915441"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0051408626_p4727398915441"><a name="en-us_topic_0051408626_p4727398915441"></a><a name="en-us_topic_0051408626_p4727398915441"></a>This parameter is used when snapshots are queried by page and is used together with the <strong id="b842352706185037"><a name="b842352706185037"></a><a name="b842352706185037"></a>limit</strong> parameter. For example, there are a total of 30 snapshots. If you set <strong id="b84235270618483"><a name="b84235270618483"></a><a name="b84235270618483"></a>offset</strong> to <strong id="b84235270618488"><a name="b84235270618488"></a><a name="b84235270618488"></a>11</strong> and <strong id="b842352706184813"><a name="b842352706184813"></a><a name="b842352706184813"></a>limit</strong> to <strong id="b842352706184818"><a name="b842352706184818"></a><a name="b842352706184818"></a>10</strong>, the queried snapshot starts from the twelfth snapshot, and at most 10 snapshots can be queried at a time.</p>
    </div></div>
    </td>
    </tr>
    <tr id="en-us_topic_0051408626_row657177691168"><td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0051408626_p215391011168"><a name="en-us_topic_0051408626_p215391011168"></a><a name="en-us_topic_0051408626_p215391011168"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0051408626_p669456211168"><a name="en-us_topic_0051408626_p669456211168"></a><a name="en-us_topic_0051408626_p669456211168"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0051408626_p538862341168"><a name="en-us_topic_0051408626_p538862341168"></a><a name="en-us_topic_0051408626_p538862341168"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0051408626_p27088191168"><a name="en-us_topic_0051408626_p27088191168"></a><a name="en-us_topic_0051408626_p27088191168"></a>Specifies the maximum number of query results that can be returned.</p>
    <p id="p283195819137"><a name="p283195819137"></a><a name="p283195819137"></a><span id="text138349551887"><a name="text138349551887"></a><a name="text138349551887"></a>The value ranges from 1 to 1000, and the default value is 1000. The returned value cannot exceed this limit.</span></p>
    <p id="en-us_topic_0051408626_p14657115572511"><a name="en-us_topic_0051408626_p14657115572511"></a><a name="en-us_topic_0051408626_p14657115572511"></a>If the tenant has more than 50 snapshots in total, you are advised to use this parameter and set its value to <strong id="b8423527069161"><a name="b8423527069161"></a><a name="b8423527069161"></a>50</strong> to improve the query efficiency. Examples are provided as follows:</p>
    <p id="en-us_topic_0051408626_p1233994321914"><a name="en-us_topic_0051408626_p1233994321914"></a><a name="en-us_topic_0051408626_p1233994321914"></a><strong id="b1293145333103912"><a name="b1293145333103912"></a><a name="b1293145333103912"></a>GET /v3/</strong><em id="i994780625103912"><a name="i994780625103912"></a><a name="i994780625103912"></a>xxx</em><strong id="b1828569207103912"><a name="b1828569207103912"></a><a name="b1828569207103912"></a>/snapshots?limit=50</strong>: Queries the 1–50 snapshots. <strong id="b842352706103924"><a name="b842352706103924"></a><a name="b842352706103924"></a>GET /v3/</strong><em id="i1514360640103921"><a name="i1514360640103921"></a><a name="i1514360640103921"></a>xxx</em><strong id="b842352706103930"><a name="b842352706103930"></a><a name="b842352706103930"></a>/snapshots?offset=50&amp;limit=50</strong>: Queries the 51–100 snapshots.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0051408626_row243793751168"><td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0051408626_p285723381168"><a name="en-us_topic_0051408626_p285723381168"></a><a name="en-us_topic_0051408626_p285723381168"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0051408626_p326580131168"><a name="en-us_topic_0051408626_p326580131168"></a><a name="en-us_topic_0051408626_p326580131168"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0051408626_p280534011168"><a name="en-us_topic_0051408626_p280534011168"></a><a name="en-us_topic_0051408626_p280534011168"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0051408626_p577330051168"><a name="en-us_topic_0051408626_p577330051168"></a><a name="en-us_topic_0051408626_p577330051168"></a>Specifies the snapshot name. This parameter does not support fuzzy search. <span id="text700391859194046"><a name="text700391859194046"></a><a name="text700391859194046"></a>The value can contain a maximum of 255 bytes.</span></p>
    </td>
    </tr>
    <tr id="row288521214459"><td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.1.5.1.1 "><p id="p463319195457"><a name="p463319195457"></a><a name="p463319195457"></a>sort_dir</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.1.5.1.2 "><p id="p1163321984520"><a name="p1163321984520"></a><a name="p1163321984520"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.1.5.1.3 "><p id="p663321934517"><a name="p663321934517"></a><a name="p663321934517"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.1.5.1.4 "><div class="p" id="p1751520421266"><a name="p1751520421266"></a><a name="p1751520421266"></a>Specifies the result sorting order. The default value is <strong id="b729920359318"><a name="b729920359318"></a><a name="b729920359318"></a>desc</strong>.<a name="ul1729318471065"></a><a name="ul1729318471065"></a><ul id="ul1729318471065"><li><strong id="b81691371532"><a name="b81691371532"></a><a name="b81691371532"></a>desc</strong>: indicates the descending order.</li><li><strong id="b1311012381339"><a name="b1311012381339"></a><a name="b1311012381339"></a>asc</strong>: indicates the ascending order.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="en-us_topic_0051408626_row498350041168"><td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0051408626_p101035441168"><a name="en-us_topic_0051408626_p101035441168"></a><a name="en-us_topic_0051408626_p101035441168"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0051408626_p130807691168"><a name="en-us_topic_0051408626_p130807691168"></a><a name="en-us_topic_0051408626_p130807691168"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0051408626_p529093741168"><a name="en-us_topic_0051408626_p529093741168"></a><a name="en-us_topic_0051408626_p529093741168"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0051408626_p578009201168"><a name="en-us_topic_0051408626_p578009201168"></a><a name="en-us_topic_0051408626_p578009201168"></a>Specifies the snapshot status. For details, see <a href="evs-snapshot-status.md">EVS Snapshot Status</a>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0051408626_row504462351168"><td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0051408626_p596132261168"><a name="en-us_topic_0051408626_p596132261168"></a><a name="en-us_topic_0051408626_p596132261168"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0051408626_p639420261168"><a name="en-us_topic_0051408626_p639420261168"></a><a name="en-us_topic_0051408626_p639420261168"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0051408626_p119216351168"><a name="en-us_topic_0051408626_p119216351168"></a><a name="en-us_topic_0051408626_p119216351168"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0051408626_p261283481168"><a name="en-us_topic_0051408626_p261283481168"></a><a name="en-us_topic_0051408626_p261283481168"></a>Specifies the ID of the snapshot's source disk.</p>
    </td>
    </tr>
    <tr id="row3561144994516"><td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.1.5.1.1 "><p id="p1355262793315"><a name="p1355262793315"></a><a name="p1355262793315"></a>name~</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.1.5.1.2 "><p id="p15552102720334"><a name="p15552102720334"></a><a name="p15552102720334"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.1.5.1.3 "><p id="p12552102719334"><a name="p12552102719334"></a><a name="p12552102719334"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.1.5.1.4 "><p id="p11552182715331"><a name="p11552182715331"></a><a name="p11552182715331"></a>Specifies the fuzzy search by disk name. This parameter is supported when the request version is 3.31 or later.</p>
    </td>
    </tr>
    <tr id="row9561144912457"><td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.1.5.1.1 "><p id="p555232714335"><a name="p555232714335"></a><a name="p555232714335"></a>status~</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.1.5.1.2 "><p id="p11553122753313"><a name="p11553122753313"></a><a name="p11553122753313"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.1.5.1.3 "><p id="p1955322717338"><a name="p1955322717338"></a><a name="p1955322717338"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.1.5.1.4 "><p id="p25531427163315"><a name="p25531427163315"></a><a name="p25531427163315"></a>Specifies the fuzzy search by disk status. This parameter is supported when the request version is 3.31 or later.</p>
    </td>
    </tr>
    <tr id="row16561104944515"><td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.1.5.1.1 "><p id="p1268088124912"><a name="p1268088124912"></a><a name="p1268088124912"></a>volume_id~</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.1.5.1.2 "><p id="p1668012820493"><a name="p1668012820493"></a><a name="p1668012820493"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.1.5.1.3 "><p id="p1968058154912"><a name="p1968058154912"></a><a name="p1968058154912"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.1.5.1.4 "><p id="p768018824914"><a name="p768018824914"></a><a name="p768018824914"></a>Specifies the fuzzy search by the ID of the disk that corresponds to the snapshot. This parameter is supported when the request version is 3.31 or later.</p>
    </td>
    </tr>
    <tr id="row1561249144519"><td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.1.5.1.1 "><p id="p668115818494"><a name="p668115818494"></a><a name="p668115818494"></a>sort_key</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.1.5.1.2 "><p id="p176812811492"><a name="p176812811492"></a><a name="p176812811492"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.1.5.1.3 "><p id="p468111819494"><a name="p468111819494"></a><a name="p468111819494"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.1.5.1.4 "><p id="p2068120884920"><a name="p2068120884920"></a><a name="p2068120884920"></a>Specifies the sorting query by name (sort_key=name). This parameter is supported when the request version is 3.30 or later. The default sorting order is the descending order.</p>
    </td>
    </tr>
    <tr id="row3563124984516"><td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.1.5.1.1 "><p id="p155547276337"><a name="p155547276337"></a><a name="p155547276337"></a>with_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.81188118811881%" headers="mcps1.1.5.1.2 "><p id="p855442773311"><a name="p855442773311"></a><a name="p855442773311"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.1.5.1.3 "><p id="p1055420271339"><a name="p1055420271339"></a><a name="p1055420271339"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="48.51485148514851%" headers="mcps1.1.5.1.4 "><p id="p26217111246"><a name="p26217111246"></a><a name="p26217111246"></a>Specifies to return parameter <strong id="b842352706111032"><a name="b842352706111032"></a><a name="b842352706111032"></a>counts</strong> in the response. This parameter indicates the number of snapshots queried. This parameter is in the <em id="i842352697111123"><a name="i842352697111123"></a><a name="i842352697111123"></a>with_count=true</em> format and is supported when the request version is 3.45 or later.</p>
    <p id="p355419276334"><a name="p355419276334"></a><a name="p355419276334"></a>This parameter can be used together with parameters <strong id="evs_04_3032_b842352706155655"><a name="evs_04_3032_b842352706155655"></a><a name="evs_04_3032_b842352706155655"></a>marker</strong>, <strong id="evs_04_3032_b842352706155659"><a name="evs_04_3032_b842352706155659"></a><a name="evs_04_3032_b842352706155659"></a>limit</strong>, <strong id="evs_04_3032_b84235270615572"><a name="evs_04_3032_b84235270615572"></a><a name="evs_04_3032_b84235270615572"></a>sort_key</strong>, <strong id="evs_04_3032_b84235270615576"><a name="evs_04_3032_b84235270615576"></a><a name="evs_04_3032_b84235270615576"></a>sort_dir</strong>, or <strong id="evs_04_3032_b842352706155718"><a name="evs_04_3032_b842352706155718"></a><a name="evs_04_3032_b842352706155718"></a>offset</strong> in the table. It cannot be used with other filter parameters.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section45527389"></a>

The following example shows how to query the snapshots in the  **available**  state.

-   Example request

    ```
    GET https://{endpoint}/v3/{project_id}/snapshots?status=available
    ```


## Response<a name="section539031881175"></a>

-   Parameter description

    <a name="table16791124318811"></a>
    <table><thead align="left"><tr id="row279119431881"><th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.1"><p id="p147912431813"><a name="p147912431813"></a><a name="p147912431813"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.2"><p id="p6791134320813"><a name="p6791134320813"></a><a name="p6791134320813"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.64423557644236%" id="mcps1.1.4.1.3"><p id="p147911943187"><a name="p147911943187"></a><a name="p147911943187"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row11792943087"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p279264316818"><a name="p279264316818"></a><a name="p279264316818"></a>snapshots</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p1379218434810"><a name="p1379218434810"></a><a name="p1379218434810"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p879218431681"><a name="p879218431681"></a><a name="p879218431681"></a>Specifies the snapshot information. For details, see <a href="#en-us_topic_0051408626_li367387041175">Parameters in the snapshots field</a>.</p>
    </td>
    </tr>
    <tr id="row19562135513816"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p147911431788"><a name="p147911431788"></a><a name="p147911431788"></a>snapshots_links</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p1279210431813"><a name="p1279210431813"></a><a name="p1279210431813"></a>list&lt;map&lt;String,String&gt;&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p163671041196"><a name="p163671041196"></a><a name="p163671041196"></a>Specifies the query position marker in the snapshot list. This parameter is at the same level as parameter <strong id="b18842436161"><a name="b18842436161"></a><a name="b18842436161"></a>snapshots</strong> in the response body. This parameter is returned only when parameter <strong id="b1484253612619"><a name="b1484253612619"></a><a name="b1484253612619"></a>limit</strong> is specified in the request, and this parameter indicates that only some snapshots are returned in this query.</p>
    </td>
    </tr>
    <tr id="row1579418431988"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p1779412431788"><a name="p1779412431788"></a><a name="p1779412431788"></a>count</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0098680634_p159017261855"><a name="en-us_topic_0098680634_p159017261855"></a><a name="en-us_topic_0098680634_p159017261855"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p57949436815"><a name="p57949436815"></a><a name="p57949436815"></a>Specifies the number of records returned in this query.</p>
    </td>
    </tr>
    <tr id="row67494216911"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p129522216412"><a name="p129522216412"></a><a name="p129522216412"></a>error</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p1595262111415"><a name="p1595262111415"></a><a name="p1595262111415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p109527215417"><a name="p109527215417"></a><a name="p109527215417"></a>Specifies the error message returned when an error occurs. For details, see <a href="#li0419202382514">Parameters in the error field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="en-us_topic_0051408626_li367387041175"></a>Parameters in the  **snapshots**  field

    <a name="en-us_topic_0051408626_table622128841175"></a>
    <table><thead align="left"><tr id="en-us_topic_0051408626_row535860991175"><th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.1"><p id="en-us_topic_0051408626_p455067371175"><a name="en-us_topic_0051408626_p455067371175"></a><a name="en-us_topic_0051408626_p455067371175"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.2"><p id="en-us_topic_0051408626_p621670471175"><a name="en-us_topic_0051408626_p621670471175"></a><a name="en-us_topic_0051408626_p621670471175"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.64423557644236%" id="mcps1.1.4.1.3"><p id="en-us_topic_0051408626_p574320291175"><a name="en-us_topic_0051408626_p574320291175"></a><a name="en-us_topic_0051408626_p574320291175"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0051408626_row505356201175"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0051408626_p668534581175"><a name="en-us_topic_0051408626_p668534581175"></a><a name="en-us_topic_0051408626_p668534581175"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0051408626_p464210281175"><a name="en-us_topic_0051408626_p464210281175"></a><a name="en-us_topic_0051408626_p464210281175"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0051408626_p283450141175"><a name="en-us_topic_0051408626_p283450141175"></a><a name="en-us_topic_0051408626_p283450141175"></a>Specifies the snapshot ID.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0051408626_row537785391175"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0051408626_p610943921175"><a name="en-us_topic_0051408626_p610943921175"></a><a name="en-us_topic_0051408626_p610943921175"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0051408626_p496987011175"><a name="en-us_topic_0051408626_p496987011175"></a><a name="en-us_topic_0051408626_p496987011175"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0051408626_p583203691175"><a name="en-us_topic_0051408626_p583203691175"></a><a name="en-us_topic_0051408626_p583203691175"></a>Specifies the snapshot status. For details, see <a href="evs-snapshot-status.md">EVS Snapshot Status</a>.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0051408626_row551212811175"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0051408626_p356388081175"><a name="en-us_topic_0051408626_p356388081175"></a><a name="en-us_topic_0051408626_p356388081175"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0051408626_p10622981175"><a name="en-us_topic_0051408626_p10622981175"></a><a name="en-us_topic_0051408626_p10622981175"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0051408626_p575287091175"><a name="en-us_topic_0051408626_p575287091175"></a><a name="en-us_topic_0051408626_p575287091175"></a>Specifies the snapshot name.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0051408626_row479963371175"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0051408626_p624980901175"><a name="en-us_topic_0051408626_p624980901175"></a><a name="en-us_topic_0051408626_p624980901175"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0051408626_p291805641175"><a name="en-us_topic_0051408626_p291805641175"></a><a name="en-us_topic_0051408626_p291805641175"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0051408626_p592057221175"><a name="en-us_topic_0051408626_p592057221175"></a><a name="en-us_topic_0051408626_p592057221175"></a>Specifies the snapshot description.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0051408626_row630894511175"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0051408626_p99718891175"><a name="en-us_topic_0051408626_p99718891175"></a><a name="en-us_topic_0051408626_p99718891175"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0051408626_p24167171175"><a name="en-us_topic_0051408626_p24167171175"></a><a name="en-us_topic_0051408626_p24167171175"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0051408626_p183889601175"><a name="en-us_topic_0051408626_p183889601175"></a><a name="en-us_topic_0051408626_p183889601175"></a>Specifies the time when the snapshot was created.</p>
    <p id="p181121789819"><a name="p181121789819"></a><a name="p181121789819"></a><span id="text1271511210811"><a name="text1271511210811"></a><a name="text1271511210811"></a>Time format: UTC YYYY-MM-DDTHH:MM:SS.XXXXXX</span></p>
    </td>
    </tr>
    <tr id="en-us_topic_0051408626_row312829201175"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0051408626_p508885661175"><a name="en-us_topic_0051408626_p508885661175"></a><a name="en-us_topic_0051408626_p508885661175"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0051408626_p283331481175"><a name="en-us_topic_0051408626_p283331481175"></a><a name="en-us_topic_0051408626_p283331481175"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0051408626_p22339381175"><a name="en-us_topic_0051408626_p22339381175"></a><a name="en-us_topic_0051408626_p22339381175"></a>Specifies the snapshot metadata.</p>
    <p id="p1678772717473"><a name="p1678772717473"></a><a name="p1678772717473"></a>If <strong id="b842352706193018"><a name="b842352706193018"></a><a name="b842352706193018"></a>metadata</strong> contains the <strong id="b842352706193021"><a name="b842352706193021"></a><a name="b842352706193021"></a>__system__enableActive</strong> field, the snapshot is automatically created during the backup of a server.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0051408626_row201054491175"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0051408626_p179286481175"><a name="en-us_topic_0051408626_p179286481175"></a><a name="en-us_topic_0051408626_p179286481175"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0051408626_p429343721175"><a name="en-us_topic_0051408626_p429343721175"></a><a name="en-us_topic_0051408626_p429343721175"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0051408626_p365124961175"><a name="en-us_topic_0051408626_p365124961175"></a><a name="en-us_topic_0051408626_p365124961175"></a>Specifies the ID of the snapshot's source disk.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0051408626_row601770151175"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0051408626_p425000331175"><a name="en-us_topic_0051408626_p425000331175"></a><a name="en-us_topic_0051408626_p425000331175"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0051408626_p199506681175"><a name="en-us_topic_0051408626_p199506681175"></a><a name="en-us_topic_0051408626_p199506681175"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0051408626_p340521631175"><a name="en-us_topic_0051408626_p340521631175"></a><a name="en-us_topic_0051408626_p340521631175"></a>Specifies the snapshot size, in GB.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0051408626_row380340191175"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0051408626_p608567071175"><a name="en-us_topic_0051408626_p608567071175"></a><a name="en-us_topic_0051408626_p608567071175"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0051408626_p304462151175"><a name="en-us_topic_0051408626_p304462151175"></a><a name="en-us_topic_0051408626_p304462151175"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0051408626_p416400291175"><a name="en-us_topic_0051408626_p416400291175"></a><a name="en-us_topic_0051408626_p416400291175"></a>Specifies the time when the snapshot was updated.</p>
    <p id="p133850207816"><a name="p133850207816"></a><a name="p133850207816"></a><span id="text186649201488"><a name="text186649201488"></a><a name="text186649201488"></a>Time format: UTC YYYY-MM-DDTHH:MM:SS.XXXXXX</span></p>
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
        "count": 4, 
        "snapshots": [
            {
                "created_at": "2016-02-16T16:54:14.981520", 
                "description": null, 
                "id": "b836dc3d-4e10-4ea4-a34c-8f6b0460a583", 
                "metadata": { }, 
                "name": "test01", 
                "size": 1, 
                "status": "available", 
                "volume_id": "ba5730ea-8621-4ae8-b702-ff0ffc12c209", 
                "updated_at": null
            }, 
            {
                "created_at": "2016-02-16T16:54:19.475397", 
                "description": null, 
                "id": "83be494d-329e-4a78-8ac5-9af900f48b95", 
                "metadata": { }, 
                "name": "test02", 
                "size": 1, 
                "status": "available", 
                "volume_id": "ba5730ea-8621-4ae8-b702-ff0ffc12c209", 
                "updated_at": null
            }, 
            {
                "created_at": "2016-02-16T16:54:24.367414", 
                "description": null, 
                "id": "dd360f46-7593-4d35-8f2c-5566fd0bd79e", 
                "metadata": { }, 
                "name": "test03", 
                "size": 1, 
                "status": "available", 
                "volume_id": "ba5730ea-8621-4ae8-b702-ff0ffc12c209", 
                "updated_at": null
            }, 
            {
                "created_at": "2016-02-16T16:54:29.766740", 
                "description": null, 
                "id": "4c29796a-8cf4-4482-9afc-e66da9a81240", 
                "metadata": { }, 
                "name": "test04", 
                "size": 1, 
                "status": "available", 
                "volume_id": "ba5730ea-8621-4ae8-b702-ff0ffc12c209", 
                "updated_at": null
            }
        ], 
        "snapshots_links": null
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


## Status Codes<a name="section4644965111956"></a>

-   Normal

    200


## Error Codes<a name="section431317151242"></a>

For details, see  [Error Codes](error-codes.md).


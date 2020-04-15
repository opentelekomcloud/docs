# Querying EVS Snapshots<a name="evs_04_2096"></a>

## Function<a name="section5262172611544"></a>

This API is used to query the EVS snapshots.

## URI<a name="section1511931811555"></a>

-   URI format

    GET /v2/\{project\_id\}/snapshots

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

    <a name="table633033061168"></a>
    <table><thead align="left"><tr id="row57109071168"><th class="cellrowborder" valign="top" width="17.169999999999998%" id="mcps1.1.5.1.1"><p id="p599303181168"><a name="p599303181168"></a><a name="p599303181168"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.15%" id="mcps1.1.5.1.2"><p id="p225175981168"><a name="p225175981168"></a><a name="p225175981168"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.34%" id="mcps1.1.5.1.3"><p id="p119861301168"><a name="p119861301168"></a><a name="p119861301168"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="50.339999999999996%" id="mcps1.1.5.1.4"><p id="p313524671168"><a name="p313524671168"></a><a name="p313524671168"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row12128142617596"><td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0058762430_p49168107152914"><a name="en-us_topic_0058762430_p49168107152914"></a><a name="en-us_topic_0058762430_p49168107152914"></a>marker</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0058762430_p23193765152914"><a name="en-us_topic_0058762430_p23193765152914"></a><a name="en-us_topic_0058762430_p23193765152914"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.34%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0058762430_p66755704152914"><a name="en-us_topic_0058762430_p66755704152914"></a><a name="en-us_topic_0058762430_p66755704152914"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.339999999999996%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0058762430_p38502923152914"><a name="en-us_topic_0058762430_p38502923152914"></a><a name="en-us_topic_0058762430_p38502923152914"></a><span id="text127381323152311"><a name="text127381323152311"></a><a name="text127381323152311"></a>Specifies the ID of the last record on the previous page. The returned value is the value of the item after this one.</span></p>
    </td>
    </tr>
    <tr id="row137367471168"><td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.1.5.1.1 "><p id="p389347291168"><a name="p389347291168"></a><a name="p389347291168"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.1.5.1.2 "><p id="p667053841168"><a name="p667053841168"></a><a name="p667053841168"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.34%" headers="mcps1.1.5.1.3 "><p id="p344270561168"><a name="p344270561168"></a><a name="p344270561168"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.339999999999996%" headers="mcps1.1.5.1.4 "><p id="p371281361168"><a name="p371281361168"></a><a name="p371281361168"></a>Specifies the offset.</p>
    <div class="note" id="note6490498915441"><a name="note6490498915441"></a><a name="note6490498915441"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p4727398915441"><a name="p4727398915441"></a><a name="p4727398915441"></a>This parameter is used when snapshots are queried by page and is used together with the <strong id="b842352706185037"><a name="b842352706185037"></a><a name="b842352706185037"></a>limit</strong> parameter. For example, there are a total of 30 snapshots. If you set <strong id="b84235270618483"><a name="b84235270618483"></a><a name="b84235270618483"></a>offset</strong> to <strong id="b84235270618488"><a name="b84235270618488"></a><a name="b84235270618488"></a>11</strong> and <strong id="b842352706184813"><a name="b842352706184813"></a><a name="b842352706184813"></a>limit</strong> to <strong id="b842352706184818"><a name="b842352706184818"></a><a name="b842352706184818"></a>10</strong>, the queried snapshot starts from the twelfth snapshot, and at most 10 snapshots can be queried at a time.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row657177691168"><td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.1.5.1.1 "><p id="p215391011168"><a name="p215391011168"></a><a name="p215391011168"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.1.5.1.2 "><p id="p669456211168"><a name="p669456211168"></a><a name="p669456211168"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.34%" headers="mcps1.1.5.1.3 "><p id="p538862341168"><a name="p538862341168"></a><a name="p538862341168"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.339999999999996%" headers="mcps1.1.5.1.4 "><p id="p27088191168"><a name="p27088191168"></a><a name="p27088191168"></a>Specifies the maximum number of query results that can be returned.</p>
    <p id="p116811542151"><a name="p116811542151"></a><a name="p116811542151"></a><span id="text138349551887"><a name="text138349551887"></a><a name="text138349551887"></a>The value ranges from 1 to 1000, and the default value is 1000. The returned value cannot exceed this limit.</span></p>
    <p id="p14657115572511"><a name="p14657115572511"></a><a name="p14657115572511"></a>If the tenant has more than 50 snapshots in total, you are advised to use this parameter and set its value to <strong id="b8423527069161"><a name="b8423527069161"></a><a name="b8423527069161"></a>50</strong> to improve the query efficiency. Examples are provided as follows:</p>
    <p id="p1233994321914"><a name="p1233994321914"></a><a name="p1233994321914"></a><strong id="b1293145333103912"><a name="b1293145333103912"></a><a name="b1293145333103912"></a>GET /v2/</strong><em id="i994780625103912"><a name="i994780625103912"></a><a name="i994780625103912"></a>xxx</em><strong id="b1828569207103912"><a name="b1828569207103912"></a><a name="b1828569207103912"></a>/snapshots?limit=50</strong>: Queries the 1–50 snapshots. <strong id="b842352706103924"><a name="b842352706103924"></a><a name="b842352706103924"></a>GET /v2/</strong><em id="i1514360640103921"><a name="i1514360640103921"></a><a name="i1514360640103921"></a>xxx</em><strong id="b842352706103930"><a name="b842352706103930"></a><a name="b842352706103930"></a>/snapshots?offset=50&amp;limit=50</strong>: Queries the 51–100 snapshots.</p>
    </td>
    </tr>
    <tr id="row243793751168"><td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.1.5.1.1 "><p id="p285723381168"><a name="p285723381168"></a><a name="p285723381168"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.1.5.1.2 "><p id="p326580131168"><a name="p326580131168"></a><a name="p326580131168"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.34%" headers="mcps1.1.5.1.3 "><p id="p280534011168"><a name="p280534011168"></a><a name="p280534011168"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.339999999999996%" headers="mcps1.1.5.1.4 "><p id="p577330051168"><a name="p577330051168"></a><a name="p577330051168"></a>Specifies the snapshot name. This parameter does not support fuzzy search. <span id="text894491124201851"><a name="text894491124201851"></a><a name="text894491124201851"></a>The value can contain a maximum of 255 bytes.</span></p>
    </td>
    </tr>
    <tr id="row498350041168"><td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.1.5.1.1 "><p id="p101035441168"><a name="p101035441168"></a><a name="p101035441168"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.1.5.1.2 "><p id="p130807691168"><a name="p130807691168"></a><a name="p130807691168"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.34%" headers="mcps1.1.5.1.3 "><p id="p529093741168"><a name="p529093741168"></a><a name="p529093741168"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.339999999999996%" headers="mcps1.1.5.1.4 "><p id="p578009201168"><a name="p578009201168"></a><a name="p578009201168"></a>Specifies the snapshot status. For details, see <a href="evs-snapshot-status.md">EVS Snapshot Status</a>.</p>
    </td>
    </tr>
    <tr id="row504462351168"><td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.1.5.1.1 "><p id="p596132261168"><a name="p596132261168"></a><a name="p596132261168"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.1.5.1.2 "><p id="p639420261168"><a name="p639420261168"></a><a name="p639420261168"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.34%" headers="mcps1.1.5.1.3 "><p id="p119216351168"><a name="p119216351168"></a><a name="p119216351168"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.339999999999996%" headers="mcps1.1.5.1.4 "><p id="p261283481168"><a name="p261283481168"></a><a name="p261283481168"></a>Specifies the ID of the snapshot's source disk.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section45527389"></a>

The following example shows how to query the snapshots in the  **available**  state.

-   Example request

    ```
    GET https://{endpoint}/v2/{project_id}/snapshots?status=available
    ```


## Response<a name="section539031881175"></a>

-   Parameter description

    <a name="table139122611716"></a>
    <table><thead align="left"><tr id="row139212261178"><th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.1"><p id="p592132601710"><a name="p592132601710"></a><a name="p592132601710"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.2"><p id="p492026161714"><a name="p492026161714"></a><a name="p492026161714"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.64423557644236%" id="mcps1.1.4.1.3"><p id="p9928266175"><a name="p9928266175"></a><a name="p9928266175"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2925156111719"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p623850141175"><a name="p623850141175"></a><a name="p623850141175"></a>snapshots</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p200213431175"><a name="p200213431175"></a><a name="p200213431175"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p279846901175"><a name="p279846901175"></a><a name="p279846901175"></a>Specifies the snapshot information. For details, see <a href="#li367387041175">Parameters in the snapshots field</a>.</p>
    </td>
    </tr>
    <tr id="row892172614170"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p59292621716"><a name="p59292621716"></a><a name="p59292621716"></a>snapshots_links</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p9921026101717"><a name="p9921026101717"></a><a name="p9921026101717"></a>list&lt;map&lt;String,String&gt;&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p693112661716"><a name="p693112661716"></a><a name="p693112661716"></a>Specifies the query position marker in the snapshot list. This parameter is at the same level as parameter <strong id="b17920052202515"><a name="b17920052202515"></a><a name="b17920052202515"></a>snapshots</strong> in the response body. This parameter is returned only when parameter <strong id="b192135232519"><a name="b192135232519"></a><a name="b192135232519"></a>limit</strong> is specified in the request, and this parameter indicates that only some snapshots are returned in this query.</p>
    </td>
    </tr>
    <tr id="row7894718155410"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p129522216412"><a name="p129522216412"></a><a name="p129522216412"></a>error</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p1595262111415"><a name="p1595262111415"></a><a name="p1595262111415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p109527215417"><a name="p109527215417"></a><a name="p109527215417"></a>Specifies the error message returned when an error occurs. For details, see <a href="#li0419202382514">Parameters in the error field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li367387041175"></a>Parameters in the  **snapshots**  field

    <a name="table622128841175"></a>
    <table><thead align="left"><tr id="row535860991175"><th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.1"><p id="p455067371175"><a name="p455067371175"></a><a name="p455067371175"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.17788221177882%" id="mcps1.1.4.1.2"><p id="p621670471175"><a name="p621670471175"></a><a name="p621670471175"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.64423557644236%" id="mcps1.1.4.1.3"><p id="p574320291175"><a name="p574320291175"></a><a name="p574320291175"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row505356201175"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p668534581175"><a name="p668534581175"></a><a name="p668534581175"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p464210281175"><a name="p464210281175"></a><a name="p464210281175"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p283450141175"><a name="p283450141175"></a><a name="p283450141175"></a>Specifies the snapshot ID.</p>
    </td>
    </tr>
    <tr id="row537785391175"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p610943921175"><a name="p610943921175"></a><a name="p610943921175"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p496987011175"><a name="p496987011175"></a><a name="p496987011175"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p583203691175"><a name="p583203691175"></a><a name="p583203691175"></a>Specifies the snapshot status. For details, see <a href="evs-snapshot-status.md">EVS Snapshot Status</a>.</p>
    </td>
    </tr>
    <tr id="row551212811175"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p356388081175"><a name="p356388081175"></a><a name="p356388081175"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p10622981175"><a name="p10622981175"></a><a name="p10622981175"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p575287091175"><a name="p575287091175"></a><a name="p575287091175"></a>Specifies the snapshot name.</p>
    </td>
    </tr>
    <tr id="row479963371175"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p624980901175"><a name="p624980901175"></a><a name="p624980901175"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p291805641175"><a name="p291805641175"></a><a name="p291805641175"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p592057221175"><a name="p592057221175"></a><a name="p592057221175"></a>Specifies the snapshot description.</p>
    </td>
    </tr>
    <tr id="row630894511175"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p99718891175"><a name="p99718891175"></a><a name="p99718891175"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p24167171175"><a name="p24167171175"></a><a name="p24167171175"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p183889601175"><a name="p183889601175"></a><a name="p183889601175"></a>Specifies the time when the snapshot was created.</p>
    <p id="p16450449115618"><a name="p16450449115618"></a><a name="p16450449115618"></a><span id="text8188185355614"><a name="text8188185355614"></a><a name="text8188185355614"></a>Time format: UTC YYYY-MM-DDTHH:MM:SS.XXXXXX</span></p>
    </td>
    </tr>
    <tr id="row312829201175"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p508885661175"><a name="p508885661175"></a><a name="p508885661175"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p283331481175"><a name="p283331481175"></a><a name="p283331481175"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p22339381175"><a name="p22339381175"></a><a name="p22339381175"></a>Specifies the snapshot metadata.</p>
    <p id="p1678772717473"><a name="p1678772717473"></a><a name="p1678772717473"></a>If <strong id="b842352706193018"><a name="b842352706193018"></a><a name="b842352706193018"></a>metadata</strong> contains the <strong id="b842352706193021"><a name="b842352706193021"></a><a name="b842352706193021"></a>__system__enableActive</strong> field, the snapshot is automatically created during the backup of a server.</p>
    </td>
    </tr>
    <tr id="row201054491175"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p179286481175"><a name="p179286481175"></a><a name="p179286481175"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p429343721175"><a name="p429343721175"></a><a name="p429343721175"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p365124961175"><a name="p365124961175"></a><a name="p365124961175"></a>Specifies the ID of the snapshot's source disk.</p>
    </td>
    </tr>
    <tr id="row601770151175"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p425000331175"><a name="p425000331175"></a><a name="p425000331175"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p199506681175"><a name="p199506681175"></a><a name="p199506681175"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p340521631175"><a name="p340521631175"></a><a name="p340521631175"></a>Specifies the snapshot size, in GB.</p>
    </td>
    </tr>
    <tr id="row380340191175"><td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.1 "><p id="p608567071175"><a name="p608567071175"></a><a name="p608567071175"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.17788221177882%" headers="mcps1.1.4.1.2 "><p id="p304462151175"><a name="p304462151175"></a><a name="p304462151175"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.64423557644236%" headers="mcps1.1.4.1.3 "><p id="p416400291175"><a name="p416400291175"></a><a name="p416400291175"></a>Specifies the time when the snapshot was updated.</p>
    <p id="p835995905612"><a name="p835995905612"></a><a name="p835995905612"></a><span id="text7360459195618"><a name="text7360459195618"></a><a name="text7360459195618"></a>Time format: UTC YYYY-MM-DDTHH:MM:SS.XXXXXX</span></p>
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


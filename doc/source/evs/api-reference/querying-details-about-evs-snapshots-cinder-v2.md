# Querying Details About EVS Snapshots<a name="evs_04_2097"></a>

## Function<a name="section63129217111110"></a>

This API is used to query details about the EVS snapshots.

## URI<a name="section21460443111127"></a>

-   URI format

    GET /v2/\{project\_id\}/snapshots/detail

-   Parameter description

    <a name="table9361875111127"></a>
    <table><thead align="left"><tr id="row34794340111127"><th class="cellrowborder" valign="top" width="28.57%" id="mcps1.1.4.1.1"><p id="p1481016775815"><a name="p1481016775815"></a><a name="p1481016775815"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="26.529999999999998%" id="mcps1.1.4.1.2"><p id="p48423414111127"><a name="p48423414111127"></a><a name="p48423414111127"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="44.9%" id="mcps1.1.4.1.3"><p id="p29982470111127"><a name="p29982470111127"></a><a name="p29982470111127"></a>Description</p>
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

    <a name="table49657902111140"></a>
    <table><thead align="left"><tr id="row47265217111140"><th class="cellrowborder" valign="top" width="17.169999999999998%" id="mcps1.1.5.1.1"><p id="p3277402111140"><a name="p3277402111140"></a><a name="p3277402111140"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.15%" id="mcps1.1.5.1.2"><p id="p64143015111140"><a name="p64143015111140"></a><a name="p64143015111140"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.9%" id="mcps1.1.5.1.3"><p id="p28201745111140"><a name="p28201745111140"></a><a name="p28201745111140"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="49.78%" id="mcps1.1.5.1.4"><p id="p2639999111140"><a name="p2639999111140"></a><a name="p2639999111140"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row15925102920245"><td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.1.5.1.1 "><p id="en-us_topic_0058762430_p49168107152914"><a name="en-us_topic_0058762430_p49168107152914"></a><a name="en-us_topic_0058762430_p49168107152914"></a>marker</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.1.5.1.2 "><p id="en-us_topic_0058762430_p23193765152914"><a name="en-us_topic_0058762430_p23193765152914"></a><a name="en-us_topic_0058762430_p23193765152914"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.9%" headers="mcps1.1.5.1.3 "><p id="en-us_topic_0058762430_p66755704152914"><a name="en-us_topic_0058762430_p66755704152914"></a><a name="en-us_topic_0058762430_p66755704152914"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.78%" headers="mcps1.1.5.1.4 "><p id="en-us_topic_0058762430_p38502923152914"><a name="en-us_topic_0058762430_p38502923152914"></a><a name="en-us_topic_0058762430_p38502923152914"></a><span id="text127381323152311"><a name="text127381323152311"></a><a name="text127381323152311"></a>Specifies the ID of the last record on the previous page. The returned value is the value of the item after this one.</span></p>
    </td>
    </tr>
    <tr id="row23759995111140"><td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.1.5.1.1 "><p id="p45511467111140"><a name="p45511467111140"></a><a name="p45511467111140"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.1.5.1.2 "><p id="p62550228111140"><a name="p62550228111140"></a><a name="p62550228111140"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.9%" headers="mcps1.1.5.1.3 "><p id="p33403677111140"><a name="p33403677111140"></a><a name="p33403677111140"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.78%" headers="mcps1.1.5.1.4 "><p id="p21343278111140"><a name="p21343278111140"></a><a name="p21343278111140"></a>Specifies the offset.</p>
    <div class="note" id="note6490498915441"><a name="note6490498915441"></a><a name="note6490498915441"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p4727398915441"><a name="p4727398915441"></a><a name="p4727398915441"></a>This parameter is used when snapshots are queried by page and is used together with the <strong id="b842352706185037"><a name="b842352706185037"></a><a name="b842352706185037"></a>limit</strong> parameter. For example, there are a total of 30 snapshots. If you set <strong id="b84235270618483"><a name="b84235270618483"></a><a name="b84235270618483"></a>offset</strong> to <strong id="b84235270618488"><a name="b84235270618488"></a><a name="b84235270618488"></a>11</strong> and <strong id="b842352706184813"><a name="b842352706184813"></a><a name="b842352706184813"></a>limit</strong> to <strong id="b842352706184818"><a name="b842352706184818"></a><a name="b842352706184818"></a>10</strong>, the queried snapshot starts from the twelfth snapshot, and at most 10 snapshots can be queried at a time.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row57871777111140"><td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.1.5.1.1 "><p id="p57102386111140"><a name="p57102386111140"></a><a name="p57102386111140"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.1.5.1.2 "><p id="p61890592111140"><a name="p61890592111140"></a><a name="p61890592111140"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.9%" headers="mcps1.1.5.1.3 "><p id="p47082066111140"><a name="p47082066111140"></a><a name="p47082066111140"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.78%" headers="mcps1.1.5.1.4 "><p id="p55551025111140"><a name="p55551025111140"></a><a name="p55551025111140"></a>Specifies the maximum number of query results that can be returned.</p>
    <p id="p8961131111161"><a name="p8961131111161"></a><a name="p8961131111161"></a><span id="text138349551887"><a name="text138349551887"></a><a name="text138349551887"></a>The value ranges from 1 to 1000, and the default value is 1000. The returned value cannot exceed this limit.</span></p>
    <p id="p14657115572511"><a name="p14657115572511"></a><a name="p14657115572511"></a>If the tenant has more than 50 snapshots in total, you are advised to use this parameter and set its value to <strong id="b8423527069161"><a name="b8423527069161"></a><a name="b8423527069161"></a>50</strong> to improve the query efficiency. Examples are provided as follows:</p>
    <p id="p1233994321914"><a name="p1233994321914"></a><a name="p1233994321914"></a><strong id="b1616195497104021"><a name="b1616195497104021"></a><a name="b1616195497104021"></a>GET /v2/</strong><em id="i198955286104021"><a name="i198955286104021"></a><a name="i198955286104021"></a>xxx</em><strong id="b1630661680104021"><a name="b1630661680104021"></a><a name="b1630661680104021"></a>/snapshots/detail?limit=50</strong>: Queries the 1–50 snapshots. <strong id="b842352706104032"><a name="b842352706104032"></a><a name="b842352706104032"></a>GET /v2/</strong><em id="i1290684130104029"><a name="i1290684130104029"></a><a name="i1290684130104029"></a>xxx</em><strong id="b842352706104037"><a name="b842352706104037"></a><a name="b842352706104037"></a>/snapshots/detail?offset=50&amp;limit=50</strong>: Queries the 51–100 snapshots.</p>
    </td>
    </tr>
    <tr id="row30197180111140"><td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.1.5.1.1 "><p id="p30052553111140"><a name="p30052553111140"></a><a name="p30052553111140"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.1.5.1.2 "><p id="p18337718111140"><a name="p18337718111140"></a><a name="p18337718111140"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.9%" headers="mcps1.1.5.1.3 "><p id="p8960171111140"><a name="p8960171111140"></a><a name="p8960171111140"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.78%" headers="mcps1.1.5.1.4 "><p id="p54685265111140"><a name="p54685265111140"></a><a name="p54685265111140"></a>Specifies the snapshot name. The value can contain a maximum of 255 bytes.</p>
    </td>
    </tr>
    <tr id="row22405342111140"><td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.1.5.1.1 "><p id="p2893391111140"><a name="p2893391111140"></a><a name="p2893391111140"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.1.5.1.2 "><p id="p33038150111140"><a name="p33038150111140"></a><a name="p33038150111140"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.9%" headers="mcps1.1.5.1.3 "><p id="p58844456111140"><a name="p58844456111140"></a><a name="p58844456111140"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.78%" headers="mcps1.1.5.1.4 "><p id="p1671647111140"><a name="p1671647111140"></a><a name="p1671647111140"></a>Specifies the snapshot status. For details, see <a href="evs-snapshot-status.md">EVS Snapshot Status</a>.</p>
    </td>
    </tr>
    <tr id="row15044830111140"><td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.1.5.1.1 "><p id="p10671727111140"><a name="p10671727111140"></a><a name="p10671727111140"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.15%" headers="mcps1.1.5.1.2 "><p id="p59103560111140"><a name="p59103560111140"></a><a name="p59103560111140"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.9%" headers="mcps1.1.5.1.3 "><p id="p22659090111140"><a name="p22659090111140"></a><a name="p22659090111140"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.78%" headers="mcps1.1.5.1.4 "><p id="p23447029111140"><a name="p23447029111140"></a><a name="p23447029111140"></a>Specifies the ID of the snapshot's source disk.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section45527389"></a>

The following example shows how to query details of the snapshots in the  **available**  state.

-   Example request

    ```
    GET https://{endpoint}/v2/{project_id}/snapshots/detail?status=available
    ```


## Response<a name="section3672851111434"></a>

-   Parameter description

    <a name="table1216812421519"></a>
    <table><thead align="left"><tr id="row191683423115"><th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.1"><p id="p816844211113"><a name="p816844211113"></a><a name="p816844211113"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.2"><p id="p316813421914"><a name="p316813421914"></a><a name="p316813421914"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.14%" id="mcps1.1.4.1.3"><p id="p71681426114"><a name="p71681426114"></a><a name="p71681426114"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row19169242411"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="p91690422118"><a name="p91690422118"></a><a name="p91690422118"></a>snapshots</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p816964217110"><a name="p816964217110"></a><a name="p816964217110"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p19169114217115"><a name="p19169114217115"></a><a name="p19169114217115"></a>Specifies the snapshot information. For details, see <a href="#li60262741111434">Parameters in the snapshots field</a>.</p>
    </td>
    </tr>
    <tr id="row5430105519414"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="p41699425112"><a name="p41699425112"></a><a name="p41699425112"></a>snapshots_links</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p1116954219116"><a name="p1116954219116"></a><a name="p1116954219116"></a>list&lt;map&lt;String,String&gt;&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p171691426114"><a name="p171691426114"></a><a name="p171691426114"></a>Specifies the query position marker in the snapshot list. This parameter is at the same level as parameter <strong id="b1948273352713"><a name="b1948273352713"></a><a name="b1948273352713"></a>snapshots</strong> in the response body. This parameter is returned only when parameter <strong id="b19483113362711"><a name="b19483113362711"></a><a name="b19483113362711"></a>limit</strong> is specified in the request, and this parameter indicates that only some snapshots are returned in this query.</p>
    </td>
    </tr>
    <tr id="row2016914421012"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="p129522216412"><a name="p129522216412"></a><a name="p129522216412"></a>error</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p1595262111415"><a name="p1595262111415"></a><a name="p1595262111415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p109527215417"><a name="p109527215417"></a><a name="p109527215417"></a>Specifies the error message returned when an error occurs. For details, see <a href="#li0419202382514">Parameters in the error field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   <a name="li60262741111434"></a>Parameters in the  **snapshots**  field

    <a name="table5493760111434"></a>
    <table><thead align="left"><tr id="row9951929111434"><th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.1"><p id="p799881111434"><a name="p799881111434"></a><a name="p799881111434"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.43%" id="mcps1.1.4.1.2"><p id="p64790373111434"><a name="p64790373111434"></a><a name="p64790373111434"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.14%" id="mcps1.1.4.1.3"><p id="p22098020111434"><a name="p22098020111434"></a><a name="p22098020111434"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row30338895111434"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="p41531445111434"><a name="p41531445111434"></a><a name="p41531445111434"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p8603891111434"><a name="p8603891111434"></a><a name="p8603891111434"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p11580698111434"><a name="p11580698111434"></a><a name="p11580698111434"></a>Specifies the snapshot ID.</p>
    </td>
    </tr>
    <tr id="row37117420111434"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="p53721059111434"><a name="p53721059111434"></a><a name="p53721059111434"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p56438551111434"><a name="p56438551111434"></a><a name="p56438551111434"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p53733716111434"><a name="p53733716111434"></a><a name="p53733716111434"></a>Specifies the snapshot status. For details, see <a href="evs-snapshot-status.md">EVS Snapshot Status</a>.</p>
    </td>
    </tr>
    <tr id="row13841398111434"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="p47411481111434"><a name="p47411481111434"></a><a name="p47411481111434"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p15124732111434"><a name="p15124732111434"></a><a name="p15124732111434"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p46466595111434"><a name="p46466595111434"></a><a name="p46466595111434"></a>Specifies the snapshot name.</p>
    </td>
    </tr>
    <tr id="row15546175111434"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="p51280630111434"><a name="p51280630111434"></a><a name="p51280630111434"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p60090386111434"><a name="p60090386111434"></a><a name="p60090386111434"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p55561368111434"><a name="p55561368111434"></a><a name="p55561368111434"></a>Specifies the snapshot description.</p>
    </td>
    </tr>
    <tr id="row30290270111434"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="p37592805111434"><a name="p37592805111434"></a><a name="p37592805111434"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p25118356111434"><a name="p25118356111434"></a><a name="p25118356111434"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p49277837111434"><a name="p49277837111434"></a><a name="p49277837111434"></a>Specifies the time when the snapshot was created.</p>
    <p id="p122996220414"><a name="p122996220414"></a><a name="p122996220414"></a><span id="text1292720311749"><a name="text1292720311749"></a><a name="text1292720311749"></a>Time format: UTC YYYY-MM-DDTHH:MM:SS.XXXXXX</span></p>
    </td>
    </tr>
    <tr id="row62090946113559"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="p4553543411364"><a name="p4553543411364"></a><a name="p4553543411364"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p6449156711364"><a name="p6449156711364"></a><a name="p6449156711364"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p778860311364"><a name="p778860311364"></a><a name="p778860311364"></a>Specifies the time when the snapshot was updated.</p>
    <p id="p932912241842"><a name="p932912241842"></a><a name="p932912241842"></a><span id="text1710311361547"><a name="text1710311361547"></a><a name="text1710311361547"></a>Time format: UTC YYYY-MM-DDTHH:MM:SS.XXXXXX</span></p>
    </td>
    </tr>
    <tr id="row40847350111434"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="p20301014111434"><a name="p20301014111434"></a><a name="p20301014111434"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p33769410111434"><a name="p33769410111434"></a><a name="p33769410111434"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p34744289111434"><a name="p34744289111434"></a><a name="p34744289111434"></a>Specifies the snapshot metadata.</p>
    <p id="p1961415054619"><a name="p1961415054619"></a><a name="p1961415054619"></a>If <strong id="b842352706193018"><a name="b842352706193018"></a><a name="b842352706193018"></a>metadata</strong> contains the <strong id="b842352706193021"><a name="b842352706193021"></a><a name="b842352706193021"></a>__system__enableActive</strong> field, the snapshot is automatically created during the backup of a server.</p>
    </td>
    </tr>
    <tr id="row44263150111434"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="p28545410111434"><a name="p28545410111434"></a><a name="p28545410111434"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p30476837111434"><a name="p30476837111434"></a><a name="p30476837111434"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p41227967111434"><a name="p41227967111434"></a><a name="p41227967111434"></a>Specifies the ID of the snapshot's source disk.</p>
    </td>
    </tr>
    <tr id="row35507385111434"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="p57525930111434"><a name="p57525930111434"></a><a name="p57525930111434"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p29088719111434"><a name="p29088719111434"></a><a name="p29088719111434"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p60586455111434"><a name="p60586455111434"></a><a name="p60586455111434"></a>Specifies the snapshot size, in GB.</p>
    </td>
    </tr>
    <tr id="row8407183111434"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="p9893207111434"><a name="p9893207111434"></a><a name="p9893207111434"></a>os-extended-snapshot-attributes:project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p63152279111434"><a name="p63152279111434"></a><a name="p63152279111434"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p11980193111434"><a name="p11980193111434"></a><a name="p11980193111434"></a>Specifies the tenant ID. <span id="text19941457165313"><a name="text19941457165313"></a><a name="text19941457165313"></a>The tenant ID is actually the project ID.</span></p>
    </td>
    </tr>
    <tr id="row40712881111434"><td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.1 "><p id="p9409050111434"><a name="p9409050111434"></a><a name="p9409050111434"></a>os-extended-snapshot-attributes:progress</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.43%" headers="mcps1.1.4.1.2 "><p id="p23935584111434"><a name="p23935584111434"></a><a name="p23935584111434"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p6625696111434"><a name="p6625696111434"></a><a name="p6625696111434"></a><span id="text4730642777"><a name="text4730642777"></a><a name="text4730642777"></a>Reserved field</span></p>
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
                "updated_at": null
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
                "updated_at": null
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


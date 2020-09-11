# Querying EVS Disks \(Deprecated\)<a name="evs_04_2012"></a>

## Function<a name="section39223476"></a>

This API is used to query EVS disks and display the query results in a list.

>![](/images/icon-notice.gif) **NOTICE:**   
>This API has been deprecated. Use another API. For details, see  [Querying EVS Disks](querying-evs-disks-cinder-v2.md).  

## URI<a name="section17466967"></a>

-   URI format

    GET /v2/\{project\_id\}/cloudvolumes

-   Parameter description

    <a name="table27773751"></a>
    <table><thead align="left"><tr id="row52589099"><th class="cellrowborder" valign="top" width="33.33%" id="mcps1.1.4.1.1"><p id="p31858597"><a name="p31858597"></a><a name="p31858597"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21.12%" id="mcps1.1.4.1.2"><p id="p30409547"><a name="p30409547"></a><a name="p30409547"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.550000000000004%" id="mcps1.1.4.1.3"><p id="p47254279"><a name="p47254279"></a><a name="p47254279"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row2391358"><td class="cellrowborder" valign="top" width="33.33%" headers="mcps1.1.4.1.1 "><p id="p59482330"><a name="p59482330"></a><a name="p59482330"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.12%" headers="mcps1.1.4.1.2 "><p id="p53339459"><a name="p53339459"></a><a name="p53339459"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.550000000000004%" headers="mcps1.1.4.1.3 "><p id="p25528928"><a name="p25528928"></a><a name="p25528928"></a>Specifies the project ID.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Request filter parameters

    <a name="table54577306"></a>
    <table><thead align="left"><tr id="row28922261"><th class="cellrowborder" valign="top" width="15.409999999999998%" id="mcps1.1.5.1.1"><p id="p61001774"><a name="p61001774"></a><a name="p61001774"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.040000000000001%" id="mcps1.1.5.1.2"><p id="p42196623"><a name="p42196623"></a><a name="p42196623"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.1%" id="mcps1.1.5.1.3"><p id="p62483297"><a name="p62483297"></a><a name="p62483297"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="52.449999999999996%" id="mcps1.1.5.1.4"><p id="p27982283"><a name="p27982283"></a><a name="p27982283"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row50513961"><td class="cellrowborder" valign="top" width="15.409999999999998%" headers="mcps1.1.5.1.1 "><p id="p65099051"><a name="p65099051"></a><a name="p65099051"></a>marker</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.040000000000001%" headers="mcps1.1.5.1.2 "><p id="p38531802"><a name="p38531802"></a><a name="p38531802"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.1%" headers="mcps1.1.5.1.3 "><p id="p34068253"><a name="p34068253"></a><a name="p34068253"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.449999999999996%" headers="mcps1.1.5.1.4 "><p id="p6854112574418"><a name="p6854112574418"></a><a name="p6854112574418"></a><span id="text18485131104414"><a name="text18485131104414"></a><a name="text18485131104414"></a>Specifies the ID of the last record on the previous page. The returned value is the value of the item after this one.</span></p>
    </td>
    </tr>
    <tr id="row5477191"><td class="cellrowborder" valign="top" width="15.409999999999998%" headers="mcps1.1.5.1.1 "><p id="p40999308"><a name="p40999308"></a><a name="p40999308"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.040000000000001%" headers="mcps1.1.5.1.2 "><p id="p32609666"><a name="p32609666"></a><a name="p32609666"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.1%" headers="mcps1.1.5.1.3 "><p id="p24137296"><a name="p24137296"></a><a name="p24137296"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.449999999999996%" headers="mcps1.1.5.1.4 "><p id="p8963999"><a name="p8963999"></a><a name="p8963999"></a>Specifies the disk name. <span id="text203621657720153"><a name="text203621657720153"></a><a name="text203621657720153"></a>The value can contain a maximum of 255 bytes.</span></p>
    </td>
    </tr>
    <tr id="row38858233"><td class="cellrowborder" valign="top" width="15.409999999999998%" headers="mcps1.1.5.1.1 "><p id="p60509154"><a name="p60509154"></a><a name="p60509154"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.040000000000001%" headers="mcps1.1.5.1.2 "><p id="p2294440"><a name="p2294440"></a><a name="p2294440"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.1%" headers="mcps1.1.5.1.3 "><p id="p51631922"><a name="p51631922"></a><a name="p51631922"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.449999999999996%" headers="mcps1.1.5.1.4 "><p id="p21436136"><a name="p21436136"></a><a name="p21436136"></a>Specifies the disk status. For details, see <a href="evs-disk-status.md">EVS Disk Status</a>.</p>
    </td>
    </tr>
    <tr id="row865613"><td class="cellrowborder" valign="top" width="15.409999999999998%" headers="mcps1.1.5.1.1 "><p id="p3005847"><a name="p3005847"></a><a name="p3005847"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.040000000000001%" headers="mcps1.1.5.1.2 "><p id="p42147045"><a name="p42147045"></a><a name="p42147045"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.1%" headers="mcps1.1.5.1.3 "><p id="p58467488"><a name="p58467488"></a><a name="p58467488"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.449999999999996%" headers="mcps1.1.5.1.4 "><p id="p38246063"><a name="p38246063"></a><a name="p38246063"></a>Specifies the maximum number of query results that can be returned.</p>
    <p id="p16741112820713"><a name="p16741112820713"></a><a name="p16741112820713"></a><span id="text138349551887"><a name="text138349551887"></a><a name="text138349551887"></a>The value ranges from 1 to 1000, and the default value is 1000. The returned value cannot exceed this limit.</span></p>
    </td>
    </tr>
    <tr id="row10287623152326"><td class="cellrowborder" valign="top" width="15.409999999999998%" headers="mcps1.1.5.1.1 "><p id="p32487930152359"><a name="p32487930152359"></a><a name="p32487930152359"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.040000000000001%" headers="mcps1.1.5.1.2 "><p id="p45998507152413"><a name="p45998507152413"></a><a name="p45998507152413"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.1%" headers="mcps1.1.5.1.3 "><p id="p4433089152326"><a name="p4433089152326"></a><a name="p4433089152326"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.449999999999996%" headers="mcps1.1.5.1.4 "><p id="p2252276152425"><a name="p2252276152425"></a><a name="p2252276152425"></a>Specifies the AZ.</p>
    </td>
    </tr>
    <tr id="row8670250"><td class="cellrowborder" valign="top" width="15.409999999999998%" headers="mcps1.1.5.1.1 "><p id="p31201619"><a name="p31201619"></a><a name="p31201619"></a>sort_key</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.040000000000001%" headers="mcps1.1.5.1.2 "><p id="p44303172"><a name="p44303172"></a><a name="p44303172"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.1%" headers="mcps1.1.5.1.3 "><p id="p31787174"><a name="p31787174"></a><a name="p31787174"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.449999999999996%" headers="mcps1.1.5.1.4 "><p id="p24624288"><a name="p24624288"></a><a name="p24624288"></a>Specifies the keyword based on which the returned results are sorted. The value can be <strong id="b842352706101941"><a name="b842352706101941"></a><a name="b842352706101941"></a>id</strong>, <strong id="b842352706101934"><a name="b842352706101934"></a><a name="b842352706101934"></a>status</strong>, <strong id="b842352706101930"><a name="b842352706101930"></a><a name="b842352706101930"></a>size</strong>, or <strong id="b842352706101927"><a name="b842352706101927"></a><a name="b842352706101927"></a>created_at</strong>, and the default value is <strong id="b2063116951191130"><a name="b2063116951191130"></a><a name="b2063116951191130"></a>created_at</strong>.</p>
    </td>
    </tr>
    <tr id="row20292006"><td class="cellrowborder" valign="top" width="15.409999999999998%" headers="mcps1.1.5.1.1 "><p id="p33039800"><a name="p33039800"></a><a name="p33039800"></a>sort_dir</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.040000000000001%" headers="mcps1.1.5.1.2 "><p id="p58978167"><a name="p58978167"></a><a name="p58978167"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.1%" headers="mcps1.1.5.1.3 "><p id="p12502218"><a name="p12502218"></a><a name="p12502218"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.449999999999996%" headers="mcps1.1.5.1.4 "><div class="p" id="p85141444124814"><a name="p85141444124814"></a><a name="p85141444124814"></a>Specifies the result sorting order. The default value is <strong id="b2389162645518"><a name="b2389162645518"></a><a name="b2389162645518"></a>desc</strong>.<a name="ul1097217103492"></a><a name="ul1097217103492"></a><ul id="ul1097217103492"><li><strong id="b1060114360556"><a name="b1060114360556"></a><a name="b1060114360556"></a>desc</strong>: indicates the descending order.</li><li><strong id="b12949195016552"><a name="b12949195016552"></a><a name="b12949195016552"></a>asc</strong>: indicates the ascending order.</li></ul>
    </div>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section22984981"></a>

The following example shows how to query the disks in the  **available**  state.

-   Example request

    ```
    GET https://{endpoint}/v2/{project_id}/cloudvolumes?status=available
    ```


## Response<a name="section5538237"></a>

-   Parameter description

    <a name="table8965192583315"></a>
    <table><thead align="left"><tr id="row189651825203318"><th class="cellrowborder" valign="top" width="19.05%" id="mcps1.1.4.1.1"><p id="p12965142517332"><a name="p12965142517332"></a><a name="p12965142517332"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="23.810000000000002%" id="mcps1.1.4.1.2"><p id="p19966725183314"><a name="p19966725183314"></a><a name="p19966725183314"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.14%" id="mcps1.1.4.1.3"><p id="p99661225203313"><a name="p99661225203313"></a><a name="p99661225203313"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8966102513315"><td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.1.4.1.1 "><p id="p1496610254332"><a name="p1496610254332"></a><a name="p1496610254332"></a>volumes</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.1.4.1.2 "><p id="p13966825183314"><a name="p13966825183314"></a><a name="p13966825183314"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p11966112563318"><a name="p11966112563318"></a><a name="p11966112563318"></a>Specifies the list of queried disks. For details, see <a href="#li53362106201054">Parameters in the volumes field</a>.</p>
    </td>
    </tr>
    <tr id="row6512145111532"><td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.1.4.1.1 "><p id="p129522216412"><a name="p129522216412"></a><a name="p129522216412"></a>error</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.1.4.1.2 "><p id="p1595262111415"><a name="p1595262111415"></a><a name="p1595262111415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p109527215417"><a name="p109527215417"></a><a name="p109527215417"></a>Specifies the error message returned when an error occurs. For details, see <a href="#li0419202382514">Parameters in the error field</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li53362106201054"></a>Parameters in the  **volumes**  field

    <a name="table10496911201054"></a>
    <table><thead align="left"><tr id="row64825509201054"><th class="cellrowborder" valign="top" width="19.05%" id="mcps1.1.4.1.1"><p id="p16374875201054"><a name="p16374875201054"></a><a name="p16374875201054"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="23.810000000000002%" id="mcps1.1.4.1.2"><p id="p24701246105647"><a name="p24701246105647"></a><a name="p24701246105647"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.14%" id="mcps1.1.4.1.3"><p id="p61373307201054"><a name="p61373307201054"></a><a name="p61373307201054"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row45417071201117"><td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.1.4.1.1 "><p id="p400084720126"><a name="p400084720126"></a><a name="p400084720126"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.1.4.1.2 "><p id="p54643919105647"><a name="p54643919105647"></a><a name="p54643919105647"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p999473820126"><a name="p999473820126"></a><a name="p999473820126"></a><span id="text193761052172315"><a name="text193761052172315"></a><a name="text193761052172315"></a>Specifies the disk ID.</span></p>
    </td>
    </tr>
    <tr id="row62684597201122"><td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.1.4.1.1 "><p id="p3840729520126"><a name="p3840729520126"></a><a name="p3840729520126"></a>links</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.1.4.1.2 "><p id="p64081320105647"><a name="p64081320105647"></a><a name="p64081320105647"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p6358787120126"><a name="p6358787120126"></a><a name="p6358787120126"></a>Specifies the disk URI. For details, see <a href="#li1284243594910">Parameters in the links field</a>.</p>
    </td>
    </tr>
    <tr id="row2970331117233"><td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.1.4.1.1 "><p id="p5715796117233"><a name="p5715796117233"></a><a name="p5715796117233"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.1.4.1.2 "><p id="p23204466105647"><a name="p23204466105647"></a><a name="p23204466105647"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p905194717233"><a name="p905194717233"></a><a name="p905194717233"></a>Specifies the disk name. <span id="text1325308373201513"><a name="text1325308373201513"></a><a name="text1325308373201513"></a>The value can contain a maximum of 255 bytes.</span></p>
    </td>
    </tr>
    </tbody>
    </table>

-   <a name="li1284243594910"></a>Parameters in the  **links**  field

    <a name="table4847305294910"></a>
    <table><thead align="left"><tr id="row2164964594910"><th class="cellrowborder" valign="top" width="19.05%" id="mcps1.1.4.1.1"><p id="p879084594910"><a name="p879084594910"></a><a name="p879084594910"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="23.810000000000002%" id="mcps1.1.4.1.2"><p id="p4096986294910"><a name="p4096986294910"></a><a name="p4096986294910"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.14%" id="mcps1.1.4.1.3"><p id="p190818586519"><a name="p190818586519"></a><a name="p190818586519"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6332755494910"><td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.1.4.1.1 "><p id="p2925823694910"><a name="p2925823694910"></a><a name="p2925823694910"></a>href</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.1.4.1.2 "><p id="p2110693594910"><a name="p2110693594910"></a><a name="p2110693594910"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p3701831894910"><a name="p3701831894910"></a><a name="p3701831894910"></a>Specifies the corresponding shortcut link.</p>
    </td>
    </tr>
    <tr id="row6472941494910"><td class="cellrowborder" valign="top" width="19.05%" headers="mcps1.1.4.1.1 "><p id="p859119094910"><a name="p859119094910"></a><a name="p859119094910"></a>rel</p>
    </td>
    <td class="cellrowborder" valign="top" width="23.810000000000002%" headers="mcps1.1.4.1.2 "><p id="p2479777094910"><a name="p2479777094910"></a><a name="p2479777094910"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.14%" headers="mcps1.1.4.1.3 "><p id="p2628531294910"><a name="p2628531294910"></a><a name="p2628531294910"></a>Specifies the shortcut link marker name.</p>
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
        "volumes": [
            {
                "id": "e6cf4401-15f6-44bd-ae2b-cff4dc9523e6", 
                "links": [
                    {
                        "href": "https://volume.az0.dc1.domainname.com/v2/cd631140887d4b6e9c786b67a6dd4c02/volumes/e6cf4401-15f6-44bd-ae2b-cff4dc9523e6", 
                        "rel": "self"
                    }, 
                    {
                        "href": "https://volume.az0.dc1.domainname.com/cd631140887d4b6e9c786b67a6dd4c02/volumes/e6cf4401-15f6-44bd-ae2b-cff4dc9523e6", 
                        "rel": "bookmark"
                    }
                ], 
                "name": "hallo5"
            }, 
            {
                "id": "4c5e8203-f70e-4717-90cd-4a8f636888d1", 
                "links": [
                    {
                        "href": "https://volume.az0.dc1.domainname.com/v2/cd631140887d4b6e9c786b67a6dd4c02/volumes/4c5e8203-f70e-4717-90cd-4a8f636888d1", 
                        "rel": "self"
                    }, 
                    {
                        "href": "https://volume.az0.dc1.domainname.com/cd631140887d4b6e9c786b67a6dd4c02/volumes/4c5e8203-f70e-4717-90cd-4a8f636888d1", 
                        "rel": "bookmark"
                    }
                ], 
                "name": "hallo4"
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


## Status Codes<a name="section49844138"></a>

-   Normal

    200


## Error Codes<a name="section431317151242"></a>

For details, see  [Error Codes](error-codes.md).


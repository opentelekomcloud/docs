# Querying ECSs on a DeH<a name="EN-US_TOPIC_0087389318"></a>

## Function<a name="section34213098"></a>

This API is used to query information about deployed ECSs on a DeH.

## URI<a name="section39482434"></a>

GET /v1.0/\{project\_id\}/dedicated-hosts/\{dedicated\_host\_id\}/servers

[Table 1](#table572214121015)  describes the parameters.

**Table  1**  Parameters description

<a name="table572214121015"></a>
<table><thead align="left"><tr id="row572516410109"><th class="cellrowborder" valign="top" width="21.23787621237876%" id="mcps1.2.5.1.1"><p id="p107252049107"><a name="p107252049107"></a><a name="p107252049107"></a><strong id="b1384105117371"><a name="b1384105117371"></a><a name="b1384105117371"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="23.44765523447655%" id="mcps1.2.5.1.2"><p id="p726975522919"><a name="p726975522919"></a><a name="p726975522919"></a><strong id="b45169521371"><a name="b45169521371"></a><a name="b45169521371"></a>Type</strong></p>
</th>
<th class="cellrowborder" valign="top" width="24.48755124487551%" id="mcps1.2.5.1.3"><p id="p072564201017"><a name="p072564201017"></a><a name="p072564201017"></a><strong id="b19376153153714"><a name="b19376153153714"></a><a name="b19376153153714"></a>Mandatory</strong></p>
</th>
<th class="cellrowborder" valign="top" width="30.826917308269174%" id="mcps1.2.5.1.4"><p id="p47253421017"><a name="p47253421017"></a><a name="p47253421017"></a><strong id="b1465915423717"><a name="b1465915423717"></a><a name="b1465915423717"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row107256481017"><td class="cellrowborder" valign="top" width="21.23787621237876%" headers="mcps1.2.5.1.1 "><p id="p1872514451016"><a name="p1872514451016"></a><a name="p1872514451016"></a>project_id</p>
</td>
<td class="cellrowborder" valign="top" width="23.44765523447655%" headers="mcps1.2.5.1.2 "><p id="p12269175511291"><a name="p12269175511291"></a><a name="p12269175511291"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="24.48755124487551%" headers="mcps1.2.5.1.3 "><p id="p147251646108"><a name="p147251646108"></a><a name="p147251646108"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.4 "><p id="p6725747104"><a name="p6725747104"></a><a name="p6725747104"></a>Specifies the project ID.</p>
<p id="p7376194915119"><a name="p7376194915119"></a><a name="p7376194915119"></a>For details about how to obtain the project ID, see <a href="https://docs.otc.t-systems.com/en-us/api/apiug/apig-en-api-180328009.html" target="_blank" rel="noopener noreferrer">Obtaining Required Information</a>.</p>
</td>
</tr>
<tr id="row184436404555"><td class="cellrowborder" valign="top" width="21.23787621237876%" headers="mcps1.2.5.1.1 "><p id="p164455404556"><a name="p164455404556"></a><a name="p164455404556"></a>dedicated_host_id</p>
</td>
<td class="cellrowborder" valign="top" width="23.44765523447655%" headers="mcps1.2.5.1.2 "><p id="p29241051175512"><a name="p29241051175512"></a><a name="p29241051175512"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="24.48755124487551%" headers="mcps1.2.5.1.3 "><p id="p1592535185519"><a name="p1592535185519"></a><a name="p1592535185519"></a>Yes</p>
</td>
<td class="cellrowborder" valign="top" width="30.826917308269174%" headers="mcps1.2.5.1.4 "><p id="p1544524011550"><a name="p1544524011550"></a><a name="p1544524011550"></a>Specifies the DeH ID.</p>
<p id="p858154817367"><a name="p858154817367"></a><a name="p858154817367"></a>You can obtain the DeH ID from the DeH console or using the <a href="querying-dehs.md">Querying DeHs</a> API.</p>
</td>
</tr>
</tbody>
</table>

## Request<a name="section60100823"></a>

-   Request parameters

    <a name="table46685187"></a>
    <table><thead align="left"><tr id="row4798296"><th class="cellrowborder" valign="top" width="16.831683168316832%" id="mcps1.1.6.1.1"><p id="p53117702"><a name="p53117702"></a><a name="p53117702"></a><strong id="b10668203213382"><a name="b10668203213382"></a><a name="b10668203213382"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15.841584158415841%" id="mcps1.1.6.1.2"><p id="p7566645"><a name="p7566645"></a><a name="p7566645"></a><strong id="b14694733183813"><a name="b14694733183813"></a><a name="b14694733183813"></a>In</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.85148514851485%" id="mcps1.1.6.1.3"><p id="p8918541"><a name="p8918541"></a><a name="p8918541"></a><strong id="b775353410384"><a name="b775353410384"></a><a name="b775353410384"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.831683168316832%" id="mcps1.1.6.1.4"><p id="p51313205"><a name="p51313205"></a><a name="p51313205"></a><strong id="b1884817351387"><a name="b1884817351387"></a><a name="b1884817351387"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="35.64356435643564%" id="mcps1.1.6.1.5"><p id="p62728917"><a name="p62728917"></a><a name="p62728917"></a><strong id="b19418183673813"><a name="b19418183673813"></a><a name="b19418183673813"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row57201619"><td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.1.6.1.1 "><p id="p2819581"><a name="p2819581"></a><a name="p2819581"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.1.6.1.2 "><p id="p27059499"><a name="p27059499"></a><a name="p27059499"></a>query</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.1.6.1.3 "><p id="p44335814"><a name="p44335814"></a><a name="p44335814"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.1.6.1.4 "><p id="p34431157"><a name="p34431157"></a><a name="p34431157"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.64356435643564%" headers="mcps1.1.6.1.5 "><p id="p37460321"><a name="p37460321"></a><a name="p37460321"></a>Specifies the number of records displayed per page.</p>
    </td>
    </tr>
    <tr id="row1598569"><td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.1.6.1.1 "><p id="p62375226"><a name="p62375226"></a><a name="p62375226"></a>marker</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.1.6.1.2 "><p id="p19228540"><a name="p19228540"></a><a name="p19228540"></a>query</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.1.6.1.3 "><p id="p14007894"><a name="p14007894"></a><a name="p14007894"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.1.6.1.4 "><p id="p60897649"><a name="p60897649"></a><a name="p60897649"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="35.64356435643564%" headers="mcps1.1.6.1.5 "><p id="p33762549"><a name="p33762549"></a><a name="p33762549"></a>Specifies the ID of the last record on the previous page. If the <strong id="b5191173710123"><a name="b5191173710123"></a><a name="b5191173710123"></a>marker</strong> value is invalid, status code 400 is returned.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    GET https://{Endpoint}/v1.0/9c53a566cb3443ab910cf0daebca90c4/dedicated-hosts/ab910cf0daebca90c4001/servers
    ```


## Response<a name="section4036497"></a>

-   Response parameters

    <a name="table56833109"></a>
    <table><thead align="left"><tr id="row65077851"><th class="cellrowborder" valign="top" width="21.767823217678234%" id="mcps1.1.5.1.1"><p id="p12547111620810"><a name="p12547111620810"></a><a name="p12547111620810"></a><strong id="b1893867141310"><a name="b1893867141310"></a><a name="b1893867141310"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="21.08789121087891%" id="mcps1.1.5.1.2"><p id="p135494166816"><a name="p135494166816"></a><a name="p135494166816"></a><strong id="b52413901320"><a name="b52413901320"></a><a name="b52413901320"></a>In</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="19.04809519048095%" id="mcps1.1.5.1.3"><p id="p55508161784"><a name="p55508161784"></a><a name="p55508161784"></a><strong id="b5621110101318"><a name="b5621110101318"></a><a name="b5621110101318"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="38.0961903809619%" id="mcps1.1.5.1.4"><p id="p35534164818"><a name="p35534164818"></a><a name="p35534164818"></a><strong id="b446881121312"><a name="b446881121312"></a><a name="b446881121312"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row56607127"><td class="cellrowborder" valign="top" width="21.767823217678234%" headers="mcps1.1.5.1.1 "><p id="p21774588"><a name="p21774588"></a><a name="p21774588"></a>servers</p>
    </td>
    <td class="cellrowborder" valign="top" width="21.08789121087891%" headers="mcps1.1.5.1.2 "><p id="p18911189"><a name="p18911189"></a><a name="p18911189"></a>body</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.04809519048095%" headers="mcps1.1.5.1.3 "><p id="p55411339"><a name="p55411339"></a><a name="p55411339"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="38.0961903809619%" headers="mcps1.1.5.1.4 "><p id="p25079723"><a name="p25079723"></a><a name="p25079723"></a>Specifies the server object.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **server**  field description

    <a name="en-us_topic_0057972887_table23553967"></a>
    <table><thead align="left"><tr id="en-us_topic_0057972887_row13724749"><th class="cellrowborder" valign="top" width="28.742874287428744%" id="mcps1.1.4.1.1"><p id="p87136551517"><a name="p87136551517"></a><a name="p87136551517"></a><strong id="b4333344013"><a name="b4333344013"></a><a name="b4333344013"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="28.742874287428744%" id="mcps1.1.4.1.2"><p id="p9713155210"><a name="p9713155210"></a><a name="p9713155210"></a><strong id="b1498116513018"><a name="b1498116513018"></a><a name="b1498116513018"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="42.51425142514251%" id="mcps1.1.4.1.3"><p id="p1272913555114"><a name="p1272913555114"></a><a name="p1272913555114"></a><strong id="b236410713016"><a name="b236410713016"></a><a name="b236410713016"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0057972887_row12502855"><td class="cellrowborder" valign="top" width="28.742874287428744%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0057972887_p6098369"><a name="en-us_topic_0057972887_p6098369"></a><a name="en-us_topic_0057972887_p6098369"></a>addresses</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.742874287428744%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0057972887_p24205908"><a name="en-us_topic_0057972887_p24205908"></a><a name="en-us_topic_0057972887_p24205908"></a>Object (string:array)</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.51425142514251%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0057972887_p34282735"><a name="en-us_topic_0057972887_p34282735"></a><a name="en-us_topic_0057972887_p34282735"></a>Specifies the network attribute of the ECS.</p>
    <p id="p188671212105711"><a name="p188671212105711"></a><a name="p188671212105711"></a>For details, see the <strong id="b8524955191716"><a name="b8524955191716"></a><a name="b8524955191716"></a>addresses</strong> field description.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057972887_row50089974"><td class="cellrowborder" valign="top" width="28.742874287428744%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0057972887_p30756130"><a name="en-us_topic_0057972887_p30756130"></a><a name="en-us_topic_0057972887_p30756130"></a>created</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.742874287428744%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0057972887_p8218569"><a name="en-us_topic_0057972887_p8218569"></a><a name="en-us_topic_0057972887_p8218569"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.51425142514251%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0057972887_p43492568"><a name="en-us_topic_0057972887_p43492568"></a><a name="en-us_topic_0057972887_p43492568"></a>Specifies the time when the ECS was created.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057972887_row34129699"><td class="cellrowborder" valign="top" width="28.742874287428744%" headers="mcps1.1.4.1.1 "><p id="en-us_topic_0057972887_p13042201"><a name="en-us_topic_0057972887_p13042201"></a><a name="en-us_topic_0057972887_p13042201"></a>flavor</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.742874287428744%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0057972887_p49785360"><a name="en-us_topic_0057972887_p49785360"></a><a name="en-us_topic_0057972887_p49785360"></a>Object (string:string)</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.51425142514251%" headers="mcps1.1.4.1.3 "><p id="p14311029546"><a name="p14311029546"></a><a name="p14311029546"></a>Specifies the ECS flavor.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0057972887_row4849437"><td class="cellrowborder" valign="top" width="28.742874287428744%" headers="mcps1.1.4.1.1 "><p id="p181047478413"><a name="p181047478413"></a><a name="p181047478413"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.742874287428744%" headers="mcps1.1.4.1.2 "><p id="en-us_topic_0057972887_p7556889"><a name="en-us_topic_0057972887_p7556889"></a><a name="en-us_topic_0057972887_p7556889"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.51425142514251%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0057972887_p40125999"><a name="en-us_topic_0057972887_p40125999"></a><a name="en-us_topic_0057972887_p40125999"></a>Specifies the ECS ID in UUID format.</p>
    </td>
    </tr>
    <tr id="row188521741520"><td class="cellrowborder" valign="top" width="28.742874287428744%" headers="mcps1.1.4.1.1 "><p id="p11852144359"><a name="p11852144359"></a><a name="p11852144359"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.742874287428744%" headers="mcps1.1.4.1.2 "><p id="p5405634373"><a name="p5405634373"></a><a name="p5405634373"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.51425142514251%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0057972887_p8356340"><a name="en-us_topic_0057972887_p8356340"></a><a name="en-us_topic_0057972887_p8356340"></a>Specifies the ECS name.</p>
    </td>
    </tr>
    <tr id="row5799511652"><td class="cellrowborder" valign="top" width="28.742874287428744%" headers="mcps1.1.4.1.1 "><p id="p118001715513"><a name="p118001715513"></a><a name="p118001715513"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.742874287428744%" headers="mcps1.1.4.1.2 "><p id="p240453512711"><a name="p240453512711"></a><a name="p240453512711"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.51425142514251%" headers="mcps1.1.4.1.3 "><p id="p13456536381"><a name="p13456536381"></a><a name="p13456536381"></a>Specifies the ECS status.</p>
    <p id="p15881842982"><a name="p15881842982"></a><a name="p15881842982"></a>Options:</p>
    <p id="p1495018549811"><a name="p1495018549811"></a><a name="p1495018549811"></a><strong id="b45471440141818"><a name="b45471440141818"></a><a name="b45471440141818"></a>ACTIVE</strong>, <strong id="b11548640121810"><a name="b11548640121810"></a><a name="b11548640121810"></a>BUILD</strong>, <strong id="b1854924061820"><a name="b1854924061820"></a><a name="b1854924061820"></a>DELETED</strong>, <strong id="b15552240121819"><a name="b15552240121819"></a><a name="b15552240121819"></a>ERROR</strong>, <strong id="b155531440101814"><a name="b155531440101814"></a><a name="b155531440101814"></a>HARD_REBOOT</strong>, <strong id="b355413405185"><a name="b355413405185"></a><a name="b355413405185"></a>MIGRATING</strong>, <strong id="b9555174011188"><a name="b9555174011188"></a><a name="b9555174011188"></a>PASSWORD</strong>, <strong id="b755654061816"><a name="b755654061816"></a><a name="b755654061816"></a>PAUSED</strong>, <strong id="b185571140191819"><a name="b185571140191819"></a><a name="b185571140191819"></a>REBOOT</strong>, <strong id="b1155864071814"><a name="b1155864071814"></a><a name="b1155864071814"></a>REBUILD</strong>, <strong id="b16559144011183"><a name="b16559144011183"></a><a name="b16559144011183"></a>RESIZE</strong>, <strong id="b856014051812"><a name="b856014051812"></a><a name="b856014051812"></a>REVERT_RESIZE</strong>, <strong id="b256184081816"><a name="b256184081816"></a><a name="b256184081816"></a>SHUTOFF</strong>, <strong id="b856219409187"><a name="b856219409187"></a><a name="b856219409187"></a>SHELVED</strong>, <strong id="b6563184071811"><a name="b6563184071811"></a><a name="b6563184071811"></a>SHELVED_OFFLOADED</strong>, <strong id="b95641940141820"><a name="b95641940141820"></a><a name="b95641940141820"></a>SOFT_DELETED</strong>, <strong id="b65652401188"><a name="b65652401188"></a><a name="b65652401188"></a>SUSPENDED</strong>, and <strong id="b115661403187"><a name="b115661403187"></a><a name="b115661403187"></a>VERIFY_RESIZE</strong></p>
    </td>
    </tr>
    <tr id="row19339527955"><td class="cellrowborder" valign="top" width="28.742874287428744%" headers="mcps1.1.4.1.1 "><p id="p1033910271353"><a name="p1033910271353"></a><a name="p1033910271353"></a>tenant_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.742874287428744%" headers="mcps1.1.4.1.2 "><p id="p1341611362718"><a name="p1341611362718"></a><a name="p1341611362718"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.51425142514251%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0057972887_p23872421"><a name="en-us_topic_0057972887_p23872421"></a><a name="en-us_topic_0057972887_p23872421"></a>Specifies the ECS tenant ID in UUID format.</p>
    </td>
    </tr>
    <tr id="row194588241158"><td class="cellrowborder" valign="top" width="28.742874287428744%" headers="mcps1.1.4.1.1 "><p id="p2458182417515"><a name="p2458182417515"></a><a name="p2458182417515"></a>updated</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.742874287428744%" headers="mcps1.1.4.1.2 "><p id="p43661037772"><a name="p43661037772"></a><a name="p43661037772"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.51425142514251%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0057972887_p30736267"><a name="en-us_topic_0057972887_p30736267"></a><a name="en-us_topic_0057972887_p30736267"></a>Specifies the time when the ECS was updated last time.</p>
    </td>
    </tr>
    <tr id="row568319495510"><td class="cellrowborder" valign="top" width="28.742874287428744%" headers="mcps1.1.4.1.1 "><p id="p26834495514"><a name="p26834495514"></a><a name="p26834495514"></a>user_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.742874287428744%" headers="mcps1.1.4.1.2 "><p id="p23225381276"><a name="p23225381276"></a><a name="p23225381276"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.51425142514251%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0057972887_p24677321"><a name="en-us_topic_0057972887_p24677321"></a><a name="en-us_topic_0057972887_p24677321"></a>Specifies the ID of the user creating the ECS. The value is in UUID format.</p>
    </td>
    </tr>
    <tr id="row754114820710"><td class="cellrowborder" valign="top" width="28.742874287428744%" headers="mcps1.1.4.1.1 "><p id="p35411081711"><a name="p35411081711"></a><a name="p35411081711"></a>task_state</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.742874287428744%" headers="mcps1.1.4.1.2 "><p id="p411783912711"><a name="p411783912711"></a><a name="p411783912711"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.51425142514251%" headers="mcps1.1.4.1.3 "><p id="p7541178674"><a name="p7541178674"></a><a name="p7541178674"></a>Specifies the ECS task status.</p>
    </td>
    </tr>
    <tr id="row1192313471267"><td class="cellrowborder" valign="top" width="28.742874287428744%" headers="mcps1.1.4.1.1 "><p id="p5923154719615"><a name="p5923154719615"></a><a name="p5923154719615"></a>image</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.742874287428744%" headers="mcps1.1.4.1.2 "><p id="p13923123915714"><a name="p13923123915714"></a><a name="p13923123915714"></a>Object (string:string)</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.51425142514251%" headers="mcps1.1.4.1.3 "><p id="p179234479620"><a name="p179234479620"></a><a name="p179234479620"></a>Specifies the ECS image.</p>
    </td>
    </tr>
    <tr id="row17508182373712"><td class="cellrowborder" valign="top" width="28.742874287428744%" headers="mcps1.1.4.1.1 "><p id="p10604175714410"><a name="p10604175714410"></a><a name="p10604175714410"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="28.742874287428744%" headers="mcps1.1.4.1.2 "><p id="p850942393715"><a name="p850942393715"></a><a name="p850942393715"></a>Object (string:string)</p>
    </td>
    <td class="cellrowborder" valign="top" width="42.51425142514251%" headers="mcps1.1.4.1.3 "><p id="p14509192313375"><a name="p14509192313375"></a><a name="p14509192313375"></a>Specifies the ECS metadata.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
        "servers": [
            {
                "addresses": {
                    "68269e6e-4a27-441b-8029-35373ad50bd9": [
                        {
                            "addr": "192.168.0.3", 
                            "version": 4
                        }
                    ]
                }, 
                "created": "2012-09-07T16:56:37Z", 
                "flavor": {
                    "id": "1"
                },
                "id": "05184ba3-00ba-4fbc-b7a2-03b62b884931",
                "metadata": {
                    "os_type": "Linux"
                }, 
                "name": "new-server-test", 
                "status": "ACTIVE", 
                "tenant_id": "openstack", 
                "updated": "2012-09-07T16:56:37Z", 
                "user_id": "fake",
                "task_state": "",
                "image": {
                    "id": "1ce5800a-e487-4c1b-b264-3353a39e2b4b"
                }
            }
        ]
    }
    ```


## Status Code<a name="section56925253"></a>

See  [Status Codes](status-codes.md).


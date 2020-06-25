# Changing the Name of a Protection Group<a name="sdrs_05_0405"></a>

## Function<a name="en-us_topic_0079693002_section34649765"></a>

This API is used to change the name of a protection group.

## Constraints and Limitations<a name="section11875456142718"></a>

None

## URI<a name="en-us_topic_0079693002_section39390935"></a>

-   URI format

    PUT /v1/\{project\_id\}/server-groups/\{server\_group\_id\}


-   Parameter description

    <a name="table8630114993720"></a>
    <table><thead align="left"><tr id="row6630749163718"><th class="cellrowborder" valign="top" width="21.782178217821784%" id="mcps1.1.5.1.1"><p id="p1963034919376"><a name="p1963034919376"></a><a name="p1963034919376"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.85148514851485%" id="mcps1.1.5.1.2"><p id="p26301649183717"><a name="p26301649183717"></a><a name="p26301649183717"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.861386138613863%" id="mcps1.1.5.1.3"><p id="p96303494377"><a name="p96303494377"></a><a name="p96303494377"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="49.504950495049506%" id="mcps1.1.5.1.4"><p id="p0630949113716"><a name="p0630949113716"></a><a name="p0630949113716"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row19630154953719"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.1.5.1.1 "><p id="p8630174916372"><a name="p8630174916372"></a><a name="p8630174916372"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.1.5.1.2 "><p id="p11630134917371"><a name="p11630134917371"></a><a name="p11630134917371"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.1.5.1.3 "><p id="p563084963711"><a name="p563084963711"></a><a name="p563084963711"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.504950495049506%" headers="mcps1.1.5.1.4 "><p id="p176305490372"><a name="p176305490372"></a><a name="p176305490372"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row2630649143712"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.1.5.1.1 "><p id="p863024910375"><a name="p863024910375"></a><a name="p863024910375"></a>server_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.1.5.1.2 "><p id="p6630124963715"><a name="p6630124963715"></a><a name="p6630124963715"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.1.5.1.3 "><p id="p563034953714"><a name="p563034953714"></a><a name="p563034953714"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.504950495049506%" headers="mcps1.1.5.1.4 "><p id="p6630849173711"><a name="p6630849173711"></a><a name="p6630849173711"></a>Specifies the ID of a protection group.</p>
    <p id="p8819185417466"><a name="p8819185417466"></a><a name="p8819185417466"></a>For details, see <a href="querying-protection-groups.md">Querying Protection Groups</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="en-us_topic_0079693002_section18974100"></a>

-   Parameter description

    <a name="table99621031133818"></a>
    <table><thead align="left"><tr id="row1696263111387"><th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.1"><p id="p29621431163815"><a name="p29621431163815"></a><a name="p29621431163815"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.1.5.1.2"><p id="p189621310385"><a name="p189621310385"></a><a name="p189621310385"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.1.5.1.3"><p id="p596215312382"><a name="p596215312382"></a><a name="p596215312382"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.1.5.1.4"><p id="p69621313389"><a name="p69621313389"></a><a name="p69621313389"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row39624311385"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p18962631153813"><a name="p18962631153813"></a><a name="p18962631153813"></a>server_group</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.2 "><p id="p89621031123811"><a name="p89621031123811"></a><a name="p89621031123811"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.3 "><p id="p9962133112381"><a name="p9962133112381"></a><a name="p9962133112381"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.5.1.4 "><p id="p138072222014"><a name="p138072222014"></a><a name="p138072222014"></a>Specifies the information about a protection group.</p>
    <p id="p3962143193810"><a name="p3962143193810"></a><a name="p3962143193810"></a>For details, see <a href="#table920673314542">Table 1</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  1** **server\_group**  field description

    <a name="table920673314542"></a>
    <table><thead align="left"><tr id="row1320623313547"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p162061733155416"><a name="p162061733155416"></a><a name="p162061733155416"></a><strong id="b672732542120"><a name="b672732542120"></a><a name="b672732542120"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.2"><p id="p1820613311541"><a name="p1820613311541"></a><a name="p1820613311541"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.91%" id="mcps1.2.5.1.3"><p id="p17206143375412"><a name="p17206143375412"></a><a name="p17206143375412"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.089999999999996%" id="mcps1.2.5.1.4"><p id="p14207193345412"><a name="p14207193345412"></a><a name="p14207193345412"></a><strong id="b692810203213"><a name="b692810203213"></a><a name="b692810203213"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row122071033105418"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1120719339543"><a name="p1120719339543"></a><a name="p1120719339543"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p7207103355415"><a name="p7207103355415"></a><a name="p7207103355415"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.91%" headers="mcps1.2.5.1.3 "><p id="p112071633145415"><a name="p112071633145415"></a><a name="p112071633145415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.089999999999996%" headers="mcps1.2.5.1.4 "><p id="p889918475203"><a name="p889918475203"></a><a name="p889918475203"></a>Specifies the name of a protection group.</p>
    <a name="ul14976121672314"></a><a name="ul14976121672314"></a><ul id="ul14976121672314"><li>The name can contain a maximum of 64 bytes.</li><li>The value can contain only letters (a to z and A to Z), digits (0 to 9), decimal points (.), underscores (_), and hyphens (-).</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    PUT https://\{endpoint\}/v1/\{project\_id\}/server-groups/ e98cefcd-2398-4a4d-8c52-c79f00e21484

    ```
    { 
         "server_group": { 
             "name": "my_test_server_group" 
         } 
     }
    ```


## Response<a name="section11170547164"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table0406165111820"></a>
    <table><thead align="left"><tr id="row440719519187"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p125481835111815"><a name="p125481835111815"></a><a name="p125481835111815"></a><strong id="b842352706151210"><a name="b842352706151210"></a><a name="b842352706151210"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p19555143581814"><a name="p19555143581814"></a><a name="p19555143581814"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p756043501813"><a name="p756043501813"></a><a name="p756043501813"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row164074518182"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p956473581815"><a name="p956473581815"></a><a name="p956473581815"></a>server_group</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p17570153513187"><a name="p17570153513187"></a><a name="p17570153513187"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p8573183511815"><a name="p8573183511815"></a><a name="p8573183511815"></a>Specifies the details of a protection group.</p>
    <p id="p640013352346"><a name="p640013352346"></a><a name="p640013352346"></a>For details, see <a href="#table1757415616184">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **server\_group**  field description

    <a name="table1757415616184"></a>
    <table><thead align="left"><tr id="row5583195631810"><th class="cellrowborder" valign="top" width="29.07%" id="mcps1.2.4.1.1"><p id="p20585145611180"><a name="p20585145611180"></a><a name="p20585145611180"></a><strong id="b842352706162023"><a name="b842352706162023"></a><a name="b842352706162023"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="16.3%" id="mcps1.2.4.1.2"><p id="p1659095671813"><a name="p1659095671813"></a><a name="p1659095671813"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="54.63%" id="mcps1.2.4.1.3"><p id="p45949566185"><a name="p45949566185"></a><a name="p45949566185"></a><strong id="b84235270615457"><a name="b84235270615457"></a><a name="b84235270615457"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row115979563182"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p115981056131819"><a name="p115981056131819"></a><a name="p115981056131819"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.3%" headers="mcps1.2.4.1.2 "><p id="p56047567189"><a name="p56047567189"></a><a name="p56047567189"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.63%" headers="mcps1.2.4.1.3 "><p id="p136061156191810"><a name="p136061156191810"></a><a name="p136061156191810"></a>Specifies the ID of a protection group.</p>
    </td>
    </tr>
    <tr id="row16608105610188"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1461045613183"><a name="p1461045613183"></a><a name="p1461045613183"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.3%" headers="mcps1.2.4.1.2 "><p id="p1361511566187"><a name="p1361511566187"></a><a name="p1361511566187"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.63%" headers="mcps1.2.4.1.3 "><p id="p146182564189"><a name="p146182564189"></a><a name="p146182564189"></a>Specifies the name of a protection group. The name can contain a maximum of 64 bytes. The value can contain only letters (a to z and A to Z), digits (0 to 9), decimal points (.), underscores (_), and hyphens (-).</p>
    </td>
    </tr>
    <tr id="row186211756181818"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p56241456121818"><a name="p56241456121818"></a><a name="p56241456121818"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.3%" headers="mcps1.2.4.1.2 "><p id="p1163155661810"><a name="p1163155661810"></a><a name="p1163155661810"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.63%" headers="mcps1.2.4.1.3 "><p id="p863295615183"><a name="p863295615183"></a><a name="p863295615183"></a>Specifies the description of a protection group.</p>
    </td>
    </tr>
    <tr id="row063410569183"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p963813562188"><a name="p963813562188"></a><a name="p963813562188"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.3%" headers="mcps1.2.4.1.2 "><p id="p36431156151811"><a name="p36431156151811"></a><a name="p36431156151811"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.63%" headers="mcps1.2.4.1.3 "><p id="p11647456181810"><a name="p11647456181810"></a><a name="p11647456181810"></a>Specifies the status of a protection group.</p>
    <p id="p1451122214538"><a name="p1451122214538"></a><a name="p1451122214538"></a>For details, see <a href="protection-group-status.md">Protection Group Status</a>.</p>
    </td>
    </tr>
    <tr id="row0648115619182"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1565275691819"><a name="p1565275691819"></a><a name="p1565275691819"></a>progress</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.3%" headers="mcps1.2.4.1.2 "><p id="p17657135671811"><a name="p17657135671811"></a><a name="p17657135671811"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.63%" headers="mcps1.2.4.1.3 "><p id="p1866185616181"><a name="p1866185616181"></a><a name="p1866185616181"></a>Specifies the synchronization progress of a protection group.</p>
    <p id="p166205616188"><a name="p166205616188"></a><a name="p166205616188"></a>Unit: %</p>
    </td>
    </tr>
    <tr id="row16621056181812"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p766635617183"><a name="p766635617183"></a><a name="p766635617183"></a>source_availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.3%" headers="mcps1.2.4.1.2 "><p id="p1867345691819"><a name="p1867345691819"></a><a name="p1867345691819"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.63%" headers="mcps1.2.4.1.3 "><p id="p1924824245820"><a name="p1924824245820"></a><a name="p1924824245820"></a>Specifies the production site AZ configured when a protection group is created.</p>
    <p id="p17155343195615"><a name="p17155343195615"></a><a name="p17155343195615"></a>The value does not change after a planned failover or failover.</p>
    </td>
    </tr>
    <tr id="row176761556131814"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1468065641818"><a name="p1468065641818"></a><a name="p1468065641818"></a>target_availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.3%" headers="mcps1.2.4.1.2 "><p id="p46871656101819"><a name="p46871656101819"></a><a name="p46871656101819"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.63%" headers="mcps1.2.4.1.3 "><p id="p17420515169"><a name="p17420515169"></a><a name="p17420515169"></a>Specifies the DR site AZ configured when a protection group is created.</p>
    <p id="p57426515169"><a name="p57426515169"></a><a name="p57426515169"></a>The value does not change after a planned failover or failover.</p>
    </td>
    </tr>
    <tr id="row1469112565186"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1969305651810"><a name="p1969305651810"></a><a name="p1969305651810"></a>domain_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.3%" headers="mcps1.2.4.1.2 "><p id="p1470175641818"><a name="p1470175641818"></a><a name="p1470175641818"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.63%" headers="mcps1.2.4.1.3 "><p id="p9703145618188"><a name="p9703145618188"></a><a name="p9703145618188"></a>Specifies the ID of an active-active domain.</p>
    </td>
    </tr>
    <tr id="row1570635612181"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p14707156151818"><a name="p14707156151818"></a><a name="p14707156151818"></a>domain_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.3%" headers="mcps1.2.4.1.2 "><p id="p8714756141817"><a name="p8714756141817"></a><a name="p8714756141817"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.63%" headers="mcps1.2.4.1.3 "><p id="p67181656191815"><a name="p67181656191815"></a><a name="p67181656191815"></a>Specifies the name of an active-active domain.</p>
    </td>
    </tr>
    <tr id="row17556104203519"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1178319563187"><a name="p1178319563187"></a><a name="p1178319563187"></a>protected_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.3%" headers="mcps1.2.4.1.2 "><p id="p77901456111817"><a name="p77901456111817"></a><a name="p77901456111817"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.63%" headers="mcps1.2.4.1.3 "><p id="p1879445681812"><a name="p1879445681812"></a><a name="p1879445681812"></a>Specifies whether protection is enabled or not.</p>
    <a name="ul14795125619185"></a><a name="ul14795125619185"></a><ul id="ul14795125619185"><li><strong id="b1415212501284"><a name="b1415212501284"></a><a name="b1415212501284"></a>started</strong>: Protection is enabled.</li><li><strong id="b136645542817"><a name="b136645542817"></a><a name="b136645542817"></a>stopped</strong>: Protection is disabled.</li></ul>
    </td>
    </tr>
    <tr id="row577216515367"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p481005619182"><a name="p481005619182"></a><a name="p481005619182"></a>replication_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.3%" headers="mcps1.2.4.1.2 "><p id="p8816175661815"><a name="p8816175661815"></a><a name="p8816175661815"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.63%" headers="mcps1.2.4.1.3 "><p id="p1881710568184"><a name="p1881710568184"></a><a name="p1881710568184"></a>Specifies the data synchronization status.</p>
    <a name="ul8820125601814"></a><a name="ul8820125601814"></a><ul id="ul8820125601814"><li><strong id="b45671721496"><a name="b45671721496"></a><a name="b45671721496"></a>active</strong>: Data has been synchronized.</li><li><strong id="b1479811519913"><a name="b1479811519913"></a><a name="b1479811519913"></a>inactive</strong>: Data is not synchronized.</li><li><strong>copying</strong>: Data is being synchronized.</li><li><strong id="b873942274910"><a name="b873942274910"></a><a name="b873942274910"></a>active-stopped</strong>: Data synchronization is stopped.</li></ul>
    </td>
    </tr>
    <tr id="row1927895683616"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1783517561182"><a name="p1783517561182"></a><a name="p1783517561182"></a>health_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.3%" headers="mcps1.2.4.1.2 "><p id="p784175618187"><a name="p784175618187"></a><a name="p784175618187"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.63%" headers="mcps1.2.4.1.3 "><p id="p148467566188"><a name="p148467566188"></a><a name="p148467566188"></a>Specifies the health status of a protection group.</p>
    <a name="ul128473565188"></a><a name="ul128473565188"></a><ul id="ul128473565188"><li><strong id="b573101420919"><a name="b573101420919"></a><a name="b573101420919"></a>normal</strong>: The protection group is normal.</li><li><strong id="b556914181493"><a name="b556914181493"></a><a name="b556914181493"></a>abnormal</strong>: The protection group is abnormal.</li></ul>
    </td>
    </tr>
    <tr id="row1271845616186"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p8723125621819"><a name="p8723125621819"></a><a name="p8723125621819"></a>priority_station</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.3%" headers="mcps1.2.4.1.2 "><p id="p15728155616189"><a name="p15728155616189"></a><a name="p15728155616189"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.63%" headers="mcps1.2.4.1.3 "><p id="p127311956101816"><a name="p127311956101816"></a><a name="p127311956101816"></a>Specifies the current production site of a protection group.</p>
    <a name="ul473195641813"></a><a name="ul473195641813"></a><ul id="ul473195641813"><li><strong id="b1684915276476"><a name="b1684915276476"></a><a name="b1684915276476"></a>source</strong>: indicates that the current production site AZ is the <strong id="b1085012276479"><a name="b1085012276479"></a><a name="b1085012276479"></a>source_availability_zone</strong> value.</li><li><strong id="b227194564711"><a name="b227194564711"></a><a name="b227194564711"></a>target</strong>: indicates that the current production site AZ is the <strong id="b328114512471"><a name="b328114512471"></a><a name="b328114512471"></a>target_availability_zone</strong> value.</li></ul>
    </td>
    </tr>
    <tr id="row1074145651817"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1674545651819"><a name="p1674545651819"></a><a name="p1674545651819"></a>protected_instance_num</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.3%" headers="mcps1.2.4.1.2 "><p id="p1475115616184"><a name="p1475115616184"></a><a name="p1475115616184"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.63%" headers="mcps1.2.4.1.3 "><p id="p1575417567185"><a name="p1575417567185"></a><a name="p1575417567185"></a>Specifies the number of protected instances in a protection group.</p>
    </td>
    </tr>
    <tr id="row1275516561186"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p107589561186"><a name="p107589561186"></a><a name="p107589561186"></a>replication_num</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.3%" headers="mcps1.2.4.1.2 "><p id="p17636564184"><a name="p17636564184"></a><a name="p17636564184"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.63%" headers="mcps1.2.4.1.3 "><p id="p6766456181810"><a name="p6766456181810"></a><a name="p6766456181810"></a>Specifies the number of replication pairs in a protection group.</p>
    </td>
    </tr>
    <tr id="row8769115641812"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p677110568188"><a name="p677110568188"></a><a name="p677110568188"></a>disaster_recovery_drill_num</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.3%" headers="mcps1.2.4.1.2 "><p id="p14775185612185"><a name="p14775185612185"></a><a name="p14775185612185"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.63%" headers="mcps1.2.4.1.3 "><p id="p11779185616187"><a name="p11779185616187"></a><a name="p11779185616187"></a>Specifies the number of DR drills in a protection group.</p>
    </td>
    </tr>
    <tr id="row38536562186"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1785705612189"><a name="p1785705612189"></a><a name="p1785705612189"></a>source_vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.3%" headers="mcps1.2.4.1.2 "><p id="p9863155681814"><a name="p9863155681814"></a><a name="p9863155681814"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.63%" headers="mcps1.2.4.1.3 "><p id="p88658561184"><a name="p88658561184"></a><a name="p88658561184"></a>Specifies the ID of the VPC for the production site.</p>
    </td>
    </tr>
    <tr id="row9866956191813"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1087015691816"><a name="p1087015691816"></a><a name="p1087015691816"></a>target_vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.3%" headers="mcps1.2.4.1.2 "><p id="p19876175613181"><a name="p19876175613181"></a><a name="p19876175613181"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.63%" headers="mcps1.2.4.1.3 "><p id="p1588010563181"><a name="p1588010563181"></a><a name="p1588010563181"></a>Specifies the ID of the VPC for the DR site.</p>
    </td>
    </tr>
    <tr id="row1788175661816"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p98851656181818"><a name="p98851656181818"></a><a name="p98851656181818"></a>test_vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.3%" headers="mcps1.2.4.1.2 "><p id="p88918566189"><a name="p88918566189"></a><a name="p88918566189"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.63%" headers="mcps1.2.4.1.3 "><p id="p138941156161818"><a name="p138941156161818"></a><a name="p138941156161818"></a>Specifies the ID of the VPC used for a DR drill.</p>
    </td>
    </tr>
    <tr id="row1389555641815"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p188981956111819"><a name="p188981956111819"></a><a name="p188981956111819"></a>dr_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.3%" headers="mcps1.2.4.1.2 "><p id="p1390615561185"><a name="p1390615561185"></a><a name="p1390615561185"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.63%" headers="mcps1.2.4.1.3 "><p id="p9910125610189"><a name="p9910125610189"></a><a name="p9910125610189"></a>Specifies the deployment model. The default value is <strong id="b1963647298"><a name="b1963647298"></a><a name="b1963647298"></a>migration</strong>, indicating migration within a VPC.</p>
    </td>
    </tr>
    <tr id="row5919155610184"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p29231256121812"><a name="p29231256121812"></a><a name="p29231256121812"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.3%" headers="mcps1.2.4.1.2 "><p id="p1792712563181"><a name="p1792712563181"></a><a name="p1792712563181"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.63%" headers="mcps1.2.4.1.3 "><p id="p199305564189"><a name="p199305564189"></a><a name="p199305564189"></a>Specifies the time when a protection group was created.</p>
    <p id="p924015916177"><a name="p924015916177"></a><a name="p924015916177"></a>The default format is as follows: "yyyy-MM-dd'T'HH:mm:ss.SSSZ", for example, <strong id="b37602377324"><a name="b37602377324"></a><a name="b37602377324"></a>2019-04-01T12:00:00.000Z</strong>.</p>
    </td>
    </tr>
    <tr id="row593295641816"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1593614562188"><a name="p1593614562188"></a><a name="p1593614562188"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.3%" headers="mcps1.2.4.1.2 "><p id="p18941756111814"><a name="p18941756111814"></a><a name="p18941756111814"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.63%" headers="mcps1.2.4.1.3 "><p id="p1994413563184"><a name="p1994413563184"></a><a name="p1994413563184"></a>Specifies the time when a protection group was updated.</p>
    <p id="p0724191312174"><a name="p0724191312174"></a><a name="p0724191312174"></a>The default format is as follows: "yyyy-MM-dd'T'HH:mm:ss.SSSZ", for example, <strong id="b1522693963215"><a name="b1522693963215"></a><a name="b1522693963215"></a>2019-04-01T12:00:00.000Z</strong>.</p>
    </td>
    </tr>
    <tr id="row1282310771117"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1416763219184"><a name="p1416763219184"></a><a name="p1416763219184"></a>protection_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.3%" headers="mcps1.2.4.1.2 "><p id="p101678327184"><a name="p101678327184"></a><a name="p101678327184"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.63%" headers="mcps1.2.4.1.3 "><p id="p137228404418"><a name="p137228404418"></a><a name="p137228404418"></a>Specifies the protection mode.</p>
    <a name="ul1022812151351"></a><a name="ul1022812151351"></a><ul id="ul1022812151351"><li><strong id="b1164910134166"><a name="b1164910134166"></a><a name="b1164910134166"></a>null</strong>: indicates that data synchronization is performed at the replication consistency group level. No partial synchronization failure will occur.</li><li><strong id="b159451252231"><a name="b159451252231"></a><a name="b159451252231"></a>replication-pair</strong>: indicates that data synchronization is performed at the replication pair level.</li></ul>
    </td>
    </tr>
    <tr id="row28241716119"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p261318522911"><a name="p261318522911"></a><a name="p261318522911"></a>replication_model</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.3%" headers="mcps1.2.4.1.2 "><p id="p96152525910"><a name="p96152525910"></a><a name="p96152525910"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.63%" headers="mcps1.2.4.1.3 "><p id="p96158524910"><a name="p96158524910"></a><a name="p96158524910"></a>Specifies the protection mode.</p>
    <div class="note" id="note86150521919"><a name="note86150521919"></a><a name="note86150521919"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p161511521693"><a name="p161511521693"></a><a name="p161511521693"></a>This parameter is reserved.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {
       "server_group": {
           "id": "e98cefcd-2398-4a4d-8c52-c79f00e21484",
           "name": "my_test_server_group",
           "description": "test_server_group_sdrs",
           "status": "available",
           "progress": 0,
           "source_availability_zone": "eu-de-01",
           "target_availability_zone": "eu-de-02",
           "domain_id": "523ab8ad-3759-4933-9436-4cf4ebb20867",
           "domain_name": "my domain",
           "protected_status": "stopped",
           "replication_status": "active-stopped",
           "health_status": "normal",
           "priority_station": "source",
           "protected_instance_num": 0,
           "replication_num": 0,
           "disaster_recovery_drill_num": 0,  
           "source_vpc_id": "ac784bd6-a79c-4def-9ff8-dc87940d5335",
           "target_vpc_id": "ac784bd6-a79c-4def-9ff8-dc87940d5335",
           "test_vpc_id": null,
           "dr_type": "migration",
           "server_type":"ECS",
           "created_at": "2018-05-09 22:11:45.0",
           "updated_at": "2018-05-09 22:11:54.0",
           "protection_type": "replication-pair",
           "replication_model": null
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



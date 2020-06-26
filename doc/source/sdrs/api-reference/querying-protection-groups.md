# Querying Protection Groups<a name="sdrs_05_0402"></a>

## Function<a name="en-us_topic_0079693002_section34649765"></a>

This API is used to query all protection groups of the current tenant.

## Constraints and Limitations<a name="section15178131662310"></a>

None

## URI<a name="en-us_topic_0079693002_section39390935"></a>

-   URI format

    GET /v1/\{project\_id\}/server-groups

-   Parameter description

    <a name="en-us_topic_0079693002_table63321005"></a>
    <table><thead align="left"><tr id="en-us_topic_0079693002_row37593218"><th class="cellrowborder" valign="top" width="21.782178217821784%" id="mcps1.1.5.1.1"><p id="p161751519115617"><a name="p161751519115617"></a><a name="p161751519115617"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="12.871287128712872%" id="mcps1.1.5.1.2"><p id="p19175131913564"><a name="p19175131913564"></a><a name="p19175131913564"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.841584158415841%" id="mcps1.1.5.1.3"><p id="p17175151916562"><a name="p17175151916562"></a><a name="p17175151916562"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="49.504950495049506%" id="mcps1.1.5.1.4"><p id="p817511935618"><a name="p817511935618"></a><a name="p817511935618"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0079693002_row29123463"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.1.5.1.1 "><p id="p15175121945618"><a name="p15175121945618"></a><a name="p15175121945618"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.1.5.1.2 "><p id="p917561965616"><a name="p917561965616"></a><a name="p917561965616"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.1.5.1.3 "><p id="p917531975612"><a name="p917531975612"></a><a name="p917531975612"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.504950495049506%" headers="mcps1.1.5.1.4 "><p id="p11176619125614"><a name="p11176619125614"></a><a name="p11176619125614"></a>Specifies the project ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   **Request filter**  field description

    <a name="en-us_topic_0079693002_table54932709"></a>
    <table><thead align="left"><tr id="en-us_topic_0079693002_row41882373"><th class="cellrowborder" valign="top" width="21.5%" id="mcps1.1.5.1.1"><p id="p2363104375614"><a name="p2363104375614"></a><a name="p2363104375614"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.25%" id="mcps1.1.5.1.2"><p id="p7363843115616"><a name="p7363843115616"></a><a name="p7363843115616"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.690000000000001%" id="mcps1.1.5.1.3"><p id="p636311434569"><a name="p636311434569"></a><a name="p636311434569"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="49.559999999999995%" id="mcps1.1.5.1.4"><p id="p736314315560"><a name="p736314315560"></a><a name="p736314315560"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0079693002_row27990155"><td class="cellrowborder" valign="top" width="21.5%" headers="mcps1.1.5.1.1 "><p id="p636364345612"><a name="p636364345612"></a><a name="p636364345612"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.25%" headers="mcps1.1.5.1.2 "><p id="p15363174385611"><a name="p15363174385611"></a><a name="p15363174385611"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.690000000000001%" headers="mcps1.1.5.1.3 "><p id="p183631643115620"><a name="p183631643115620"></a><a name="p183631643115620"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.559999999999995%" headers="mcps1.1.5.1.4 "><p id="p3363194365615"><a name="p3363194365615"></a><a name="p3363194365615"></a>Specifies the maximum number of results returned each time. The value is a positive integer from 0 to 1000. The default value is <strong id="b842352706161435"><a name="b842352706161435"></a><a name="b842352706161435"></a>1000</strong>.</p>
    </td>
    </tr>
    <tr id="row49112572514"><td class="cellrowborder" valign="top" width="21.5%" headers="mcps1.1.5.1.1 "><p id="p736344317569"><a name="p736344317569"></a><a name="p736344317569"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.25%" headers="mcps1.1.5.1.2 "><p id="p2363543145612"><a name="p2363543145612"></a><a name="p2363543145612"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.690000000000001%" headers="mcps1.1.5.1.3 "><p id="p836316436564"><a name="p836316436564"></a><a name="p836316436564"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.559999999999995%" headers="mcps1.1.5.1.4 "><p id="p1752104119595"><a name="p1752104119595"></a><a name="p1752104119595"></a>Specifies the offset of each request. The default value is <strong id="b74201644142916"><a name="b74201644142916"></a><a name="b74201644142916"></a>0</strong>. The value must be a number and cannot be negative.</p>
    </td>
    </tr>
    <tr id="row14277596517"><td class="cellrowborder" valign="top" width="21.5%" headers="mcps1.1.5.1.1 "><p id="p33631043105615"><a name="p33631043105615"></a><a name="p33631043105615"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.25%" headers="mcps1.1.5.1.2 "><p id="p193637436561"><a name="p193637436561"></a><a name="p193637436561"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.690000000000001%" headers="mcps1.1.5.1.3 "><p id="p2363174355610"><a name="p2363174355610"></a><a name="p2363174355610"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.559999999999995%" headers="mcps1.1.5.1.4 "><p id="p6363134316569"><a name="p6363134316569"></a><a name="p6363134316569"></a>Specifies the protection group status.</p>
    <p id="p188093812119"><a name="p188093812119"></a><a name="p188093812119"></a>For details, see <a href="protection-group-status.md">Protection Group Status</a>.</p>
    </td>
    </tr>
    <tr id="row971182745318"><td class="cellrowborder" valign="top" width="21.5%" headers="mcps1.1.5.1.1 "><p id="p851015142419"><a name="p851015142419"></a><a name="p851015142419"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.25%" headers="mcps1.1.5.1.2 "><p id="p1951385152415"><a name="p1951385152415"></a><a name="p1951385152415"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.690000000000001%" headers="mcps1.1.5.1.3 "><p id="p115154512243"><a name="p115154512243"></a><a name="p115154512243"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.559999999999995%" headers="mcps1.1.5.1.4 "><p id="p1050811402318"><a name="p1050811402318"></a><a name="p1050811402318"></a>Specifies the name of a protection group.</p>
    <p id="p15171251182415"><a name="p15171251182415"></a><a name="p15171251182415"></a>Fuzzy search is supported.</p>
    </td>
    </tr>
    <tr id="row1015215241616"><td class="cellrowborder" valign="top" width="21.5%" headers="mcps1.1.5.1.1 "><p id="p1315305251611"><a name="p1315305251611"></a><a name="p1315305251611"></a>query_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.25%" headers="mcps1.1.5.1.2 "><p id="p41537522160"><a name="p41537522160"></a><a name="p41537522160"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.690000000000001%" headers="mcps1.1.5.1.3 "><p id="p18153205216167"><a name="p18153205216167"></a><a name="p18153205216167"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.559999999999995%" headers="mcps1.1.5.1.4 "><p id="p1415405216161"><a name="p1415405216161"></a><a name="p1415405216161"></a>Specifies the query type.</p>
    <a name="ul650863217178"></a><a name="ul650863217178"></a><ul id="ul650863217178"><li><strong id="b84235270615149"><a name="b84235270615149"></a><a name="b84235270615149"></a>status_abnormal</strong>: indicates to query protection groups in the abnormal status.</li><li><strong id="b842352706152610"><a name="b842352706152610"></a><a name="b842352706152610"></a>stop_protected</strong>: indicates to query protection groups for which the protection is disabled.</li><li><strong id="b842352706153222"><a name="b842352706153222"></a><a name="b842352706153222"></a>period_no_dr_drill</strong>: indicates to query the protection groups for which the no DR drills have been performed in a specified duration. The default duration is 3 months.</li><li>This parameter is invalid when the value is set to <strong id="b1875917596293"><a name="b1875917596293"></a><a name="b1875917596293"></a>general</strong> or left empty.</li></ul>
    </td>
    </tr>
    <tr id="row077375717164"><td class="cellrowborder" valign="top" width="21.5%" headers="mcps1.1.5.1.1 "><p id="p13773157191611"><a name="p13773157191611"></a><a name="p13773157191611"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.25%" headers="mcps1.1.5.1.2 "><p id="p3773957151611"><a name="p3773957151611"></a><a name="p3773957151611"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.690000000000001%" headers="mcps1.1.5.1.3 "><p id="p1177518571167"><a name="p1177518571167"></a><a name="p1177518571167"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.559999999999995%" headers="mcps1.1.5.1.4 "><p id="p1577510578162"><a name="p1577510578162"></a><a name="p1577510578162"></a>Specifies the current production site AZ of a protection group.</p>
    <p id="p05331671261"><a name="p05331671261"></a><a name="p05331671261"></a>You can obtain this value by calling the API described in <a href="querying-an-active-active-domain.md">Querying an Active-Active Domain</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section16159204210425"></a>

-   Request parameters

    None

-   Example request

    GET https://\{Endpoint\}/v1/\{project\_id\}/server-groups


## Response<a name="en-us_topic_0079693002_section36549175"></a>

-   Parameter description

    <a name="table155991608555"></a>
    <table><thead align="left"><tr id="row460510055518"><th class="cellrowborder" valign="top" width="29.07%" id="mcps1.1.4.1.1"><p id="p56078010555"><a name="p56078010555"></a><a name="p56078010555"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.44%" id="mcps1.1.4.1.2"><p id="p961219016552"><a name="p961219016552"></a><a name="p961219016552"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.49%" id="mcps1.1.4.1.3"><p id="p186139012557"><a name="p186139012557"></a><a name="p186139012557"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row86164025512"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.1.4.1.1 "><p id="p21991181583"><a name="p21991181583"></a><a name="p21991181583"></a>server_groups</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.1.4.1.2 "><p id="p91992895813"><a name="p91992895813"></a><a name="p91992895813"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.1.4.1.3 "><p id="p21995845812"><a name="p21995845812"></a><a name="p21995845812"></a>Specifies the information about protection groups.</p>
    <p id="p18318112734312"><a name="p18318112734312"></a><a name="p18318112734312"></a>For details, see <a href="#table503353570">Table 1</a>.</p>
    </td>
    </tr>
    <tr id="row166368013553"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.1.4.1.1 "><p id="p1919910835818"><a name="p1919910835818"></a><a name="p1919910835818"></a>count</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.1.4.1.2 "><p id="p91992084588"><a name="p91992084588"></a><a name="p91992084588"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.1.4.1.3 "><p id="p1396517382372"><a name="p1396517382372"></a><a name="p1396517382372"></a>Specifies the number of protection groups that meet the filtering criteria.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  1** **server\_groups**  field description

    <a name="table503353570"></a>
    <table><thead align="left"><tr id="row131163505710"><th class="cellrowborder" valign="top" width="29.07%" id="mcps1.2.4.1.1"><p id="p8131435155711"><a name="p8131435155711"></a><a name="p8131435155711"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.44%" id="mcps1.2.4.1.2"><p id="p6251035195718"><a name="p6251035195718"></a><a name="p6251035195718"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.49%" id="mcps1.2.4.1.3"><p id="p1727173517574"><a name="p1727173517574"></a><a name="p1727173517574"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1829133585715"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1087412444534"><a name="p1087412444534"></a><a name="p1087412444534"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p4248442145818"><a name="p4248442145818"></a><a name="p4248442145818"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p1124834213585"><a name="p1124834213585"></a><a name="p1124834213585"></a>Specifies the ID of a protection group.</p>
    </td>
    </tr>
    <tr id="row1472144614199"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p8874044105311"><a name="p8874044105311"></a><a name="p8874044105311"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p132481142125812"><a name="p132481142125812"></a><a name="p132481142125812"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p82481642175811"><a name="p82481642175811"></a><a name="p82481642175811"></a>Specifies the name of a protection group.</p>
    </td>
    </tr>
    <tr id="row1845264811918"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1587444415317"><a name="p1587444415317"></a><a name="p1587444415317"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p12481042145818"><a name="p12481042145818"></a><a name="p12481042145818"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p024804218583"><a name="p024804218583"></a><a name="p024804218583"></a>Specifies the description of a protection group.</p>
    </td>
    </tr>
    <tr id="row2503145051917"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p5874194411539"><a name="p5874194411539"></a><a name="p5874194411539"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p1524814423585"><a name="p1524814423585"></a><a name="p1524814423585"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p15248104219583"><a name="p15248104219583"></a><a name="p15248104219583"></a>Specifies the status of a protection group. For details, see <a href="protection-group-status.md">Protection Group Status</a>.</p>
    </td>
    </tr>
    <tr id="row16933782536"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p0874164405317"><a name="p0874164405317"></a><a name="p0874164405317"></a>progress</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p9248442195815"><a name="p9248442195815"></a><a name="p9248442195815"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p14248342105814"><a name="p14248342105814"></a><a name="p14248342105814"></a>Specifies the synchronization progress of a protection group.</p>
    <p id="p224894275817"><a name="p224894275817"></a><a name="p224894275817"></a>Unit: %</p>
    </td>
    </tr>
    <tr id="row3104111145312"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p12874114435314"><a name="p12874114435314"></a><a name="p12874114435314"></a>source_availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p1324815426585"><a name="p1324815426585"></a><a name="p1324815426585"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p1924824245820"><a name="p1924824245820"></a><a name="p1924824245820"></a>Specifies the production site AZ configured when a protection group is created.</p>
    <p id="p17155343195615"><a name="p17155343195615"></a><a name="p17155343195615"></a>The value does not change after a planned failover or failover.</p>
    </td>
    </tr>
    <tr id="row18947413145310"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p9874444205313"><a name="p9874444205313"></a><a name="p9874444205313"></a>target_availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p11248174275815"><a name="p11248174275815"></a><a name="p11248174275815"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p1324834217585"><a name="p1324834217585"></a><a name="p1324834217585"></a>Specifies the DR site AZ configured when a protection group is created.</p>
    <p id="p17776141625919"><a name="p17776141625919"></a><a name="p17776141625919"></a>The value does not change after a planned failover or failover.</p>
    </td>
    </tr>
    <tr id="row782074891315"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p17789205818138"><a name="p17789205818138"></a><a name="p17789205818138"></a>domain_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p15789155817133"><a name="p15789155817133"></a><a name="p15789155817133"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p13789205861313"><a name="p13789205861313"></a><a name="p13789205861313"></a>Specifies the ID of an active-active domain.</p>
    </td>
    </tr>
    <tr id="row35312512135"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1278910583138"><a name="p1278910583138"></a><a name="p1278910583138"></a>domain_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p378945814139"><a name="p378945814139"></a><a name="p378945814139"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p15789258191318"><a name="p15789258191318"></a><a name="p15789258191318"></a>Specifies the name of an active-active domain.</p>
    </td>
    </tr>
    <tr id="row156967172533"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p19876144455310"><a name="p19876144455310"></a><a name="p19876144455310"></a>priority_station</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p1248144285818"><a name="p1248144285818"></a><a name="p1248144285818"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p382553192519"><a name="p382553192519"></a><a name="p382553192519"></a>Specifies the current production site of a protection group.</p>
    <a name="ul782135312518"></a><a name="ul782135312518"></a><ul id="ul782135312518"><li><strong id="b1241312361603"><a name="b1241312361603"></a><a name="b1241312361603"></a>source</strong>: indicates that the current production site AZ is the <strong id="b5221711564"><a name="b5221711564"></a><a name="b5221711564"></a>source_availability_zone</strong> value.</li><li><strong id="b11621141219617"><a name="b11621141219617"></a><a name="b11621141219617"></a>target</strong>: indicates that the current production site AZ is the <strong id="b16437102318617"><a name="b16437102318617"></a><a name="b16437102318617"></a>target_availability_zone</strong> value.</li></ul>
    </td>
    </tr>
    <tr id="row73041920185318"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1187618449533"><a name="p1187618449533"></a><a name="p1187618449533"></a>protected_instance_num</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p2248174218581"><a name="p2248174218581"></a><a name="p2248174218581"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p8248194212586"><a name="p8248194212586"></a><a name="p8248194212586"></a>Specifies the number of protected instances in a protection group.</p>
    </td>
    </tr>
    <tr id="row1352214231535"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1987664475314"><a name="p1987664475314"></a><a name="p1987664475314"></a>replication_num</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p162481142165815"><a name="p162481142165815"></a><a name="p162481142165815"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p1824854205812"><a name="p1824854205812"></a><a name="p1824854205812"></a>Specifies the number of replication pairs in a protection group.</p>
    </td>
    </tr>
    <tr id="row1347012381149"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p16257946131414"><a name="p16257946131414"></a><a name="p16257946131414"></a>disaster_recovery_drill_num</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p1825717467145"><a name="p1825717467145"></a><a name="p1825717467145"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p82571646201410"><a name="p82571646201410"></a><a name="p82571646201410"></a>Specifies the number of DR drills in a protection group.</p>
    </td>
    </tr>
    <tr id="row20709202565319"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p987618443532"><a name="p987618443532"></a><a name="p987618443532"></a>protected_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p2248134225814"><a name="p2248134225814"></a><a name="p2248134225814"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p524820427584"><a name="p524820427584"></a><a name="p524820427584"></a>Specifies whether protection is enabled or not.</p>
    <a name="ul124792165914"></a><a name="ul124792165914"></a><ul id="ul124792165914"><li><strong id="b8929261229"><a name="b8929261229"></a><a name="b8929261229"></a>started</strong>: Protection is enabled.</li><li><strong id="b1661142816219"><a name="b1661142816219"></a><a name="b1661142816219"></a>stopped</strong>: Protection is disabled.</li></ul>
    <div class="note" id="note6413165811363"><a name="note6413165811363"></a><a name="note6413165811363"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1041435815367"><a name="p1041435815367"></a><a name="p1041435815367"></a>The system has been upgraded. For newly protection groups, the value of this parameter is <strong id="b16984252153816"><a name="b16984252153816"></a><a name="b16984252153816"></a>null</strong>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row64521828105318"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p087724425313"><a name="p087724425313"></a><a name="p087724425313"></a>replication_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p1248442115811"><a name="p1248442115811"></a><a name="p1248442115811"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p18248114218589"><a name="p18248114218589"></a><a name="p18248114218589"></a>Specifies the data synchronization status.</p>
    <a name="ul7844153212592"></a><a name="ul7844153212592"></a><ul id="ul7844153212592"><li><strong id="b1549615266319"><a name="b1549615266319"></a><a name="b1549615266319"></a>active</strong>: Data has been synchronized.</li><li><strong id="b11863114211317"><a name="b11863114211317"></a><a name="b11863114211317"></a>inactive</strong>: Data is not synchronized.</li><li><strong>copying</strong>: Data is being synchronized.</li><li><strong id="b1951934910477"><a name="b1951934910477"></a><a name="b1951934910477"></a>active-stopped</strong>: Data synchronization is stopped.</li></ul>
    <div class="note" id="note16650143918462"><a name="note16650143918462"></a><a name="note16650143918462"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="sdrs_05_0402_p1041435815367"><a name="sdrs_05_0402_p1041435815367"></a><a name="sdrs_05_0402_p1041435815367"></a>The system has been upgraded. For newly protection groups, the value of this parameter is <strong id="sdrs_05_0402_b16984252153816"><a name="sdrs_05_0402_b16984252153816"></a><a name="sdrs_05_0402_b16984252153816"></a>null</strong>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row16827830185314"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p108776449538"><a name="p108776449538"></a><a name="p108776449538"></a>health_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p524813424581"><a name="p524813424581"></a><a name="p524813424581"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p724817427589"><a name="p724817427589"></a><a name="p724817427589"></a>Specifies the health status of a protection group.</p>
    <a name="ul956211372595"></a><a name="ul956211372595"></a><ul id="ul956211372595"><li><strong id="b14711151947"><a name="b14711151947"></a><a name="b14711151947"></a>normal</strong>: The protection group is normal.</li><li><strong id="b198721543418"><a name="b198721543418"></a><a name="b198721543418"></a>abnormal</strong>: The protection group is abnormal.</li></ul>
    <div class="note" id="note1530717186521"><a name="note1530717186521"></a><a name="note1530717186521"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="sdrs_05_0403_p162255319523"><a name="sdrs_05_0403_p162255319523"></a><a name="sdrs_05_0403_p162255319523"></a>The system is upgraded recently. For protection groups created after the upgrade, the value of this parameter is <strong id="sdrs_05_0403_b16984252153816"><a name="sdrs_05_0403_b16984252153816"></a><a name="sdrs_05_0403_b16984252153816"></a>null</strong>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row1421529191417"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1922774618148"><a name="p1922774618148"></a><a name="p1922774618148"></a>source_vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p13227104661410"><a name="p13227104661410"></a><a name="p13227104661410"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p13227124614144"><a name="p13227124614144"></a><a name="p13227124614144"></a>Specifies the ID of the VPC for the production site.</p>
    </td>
    </tr>
    <tr id="row54162311142"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p172271946121416"><a name="p172271946121416"></a><a name="p172271946121416"></a>target_vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p822764691417"><a name="p822764691417"></a><a name="p822764691417"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p16227246191420"><a name="p16227246191420"></a><a name="p16227246191420"></a>Specifies the ID of the VPC for the DR site.</p>
    </td>
    </tr>
    <tr id="row374313339144"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p8227246121415"><a name="p8227246121415"></a><a name="p8227246121415"></a>test_vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p32272462143"><a name="p32272462143"></a><a name="p32272462143"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p3227546181414"><a name="p3227546181414"></a><a name="p3227546181414"></a>Specifies the ID of the VPC used for a DR drill. This parameter is not used in the current version.</p>
    </td>
    </tr>
    <tr id="row4777133521415"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p722794691412"><a name="p722794691412"></a><a name="p722794691412"></a>dr_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p17227184611143"><a name="p17227184611143"></a><a name="p17227184611143"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p72270468140"><a name="p72270468140"></a><a name="p72270468140"></a>Specifies the deployment model. The default value is <strong id="b1963647298"><a name="b1963647298"></a><a name="b1963647298"></a>migration</strong>, indicating migration within a VPC.</p>
    </td>
    </tr>
    <tr id="row4130183355311"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p188777444534"><a name="p188777444534"></a><a name="p188777444534"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p1024894275819"><a name="p1024894275819"></a><a name="p1024894275819"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p1248342175814"><a name="p1248342175814"></a><a name="p1248342175814"></a>Specifies the time when a protection group was created.</p>
    <p id="p1078620139012"><a name="p1078620139012"></a><a name="p1078620139012"></a>The default format is as follows: "yyyy-MM-dd'T'HH:mm:ss.SSSZ", for example, <strong id="b128366104114"><a name="b128366104114"></a><a name="b128366104114"></a>2019-04-01T12:00:00.000Z</strong>.</p>
    </td>
    </tr>
    <tr id="row838919355539"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p118776443530"><a name="p118776443530"></a><a name="p118776443530"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p11248204217584"><a name="p11248204217584"></a><a name="p11248204217584"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p32481425582"><a name="p32481425582"></a><a name="p32481425582"></a>Specifies the time when a protection group was updated.</p>
    <p id="p475015226013"><a name="p475015226013"></a><a name="p475015226013"></a>The default format is as follows: "yyyy-MM-dd'T'HH:mm:ss.SSSZ", for example, <strong id="b8545112016417"><a name="b8545112016417"></a><a name="b8545112016417"></a>2019-04-01T12:00:00.000Z</strong>.</p>
    </td>
    </tr>
    <tr id="row17721194018416"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p9721104012413"><a name="p9721104012413"></a><a name="p9721104012413"></a>protection_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p17214401413"><a name="p17214401413"></a><a name="p17214401413"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p137228404418"><a name="p137228404418"></a><a name="p137228404418"></a>Specifies the protection mode.</p>
    <a name="ul1022812151351"></a><a name="ul1022812151351"></a><ul id="ul1022812151351"><li><strong id="b1491594953813"><a name="b1491594953813"></a><a name="b1491594953813"></a>replication-pair</strong>: indicates that data synchronization is performed at the replication pair level.</li><li><strong id="b1164910134166"><a name="b1164910134166"></a><a name="b1164910134166"></a>null</strong>: indicates that data synchronization is performed at the replication consistency group level. </li></ul>
    <div class="note" id="note712463314011"><a name="note712463314011"></a><a name="note712463314011"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1225719174361"><a name="p1225719174361"></a><a name="p1225719174361"></a>The system has been upgraded. Data synchronization is performed at the replication pair level for all resources, and the returned value is <strong id="b9692864477"><a name="b9692864477"></a><a name="b9692864477"></a>replication-pair</strong>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row19417152220194"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p261318522911"><a name="p261318522911"></a><a name="p261318522911"></a>replication_model</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p17615165210912"><a name="p17615165210912"></a><a name="p17615165210912"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p96158524910"><a name="p96158524910"></a><a name="p96158524910"></a>Specifies the protection mode.</p>
    <div class="note" id="note86150521919"><a name="note86150521919"></a><a name="note86150521919"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p161511521693"><a name="p161511521693"></a><a name="p161511521693"></a>This parameter is reserved.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    { 
       "count": 2, 
       "server_groups": [ 
            {
                "id": "40df180b-9fe2-471a-8c64-1b758dc84189",
                "name": "testname",
                "description": "description",
                "source_availability_zone": "eu-de-01",
                "target_availability_zone": "eu-de-02",
                "domain_id": "fb4bb8e3-a574-4437-a156-78c916aeea4d",
                "domain_name": "ActiveactiveDomain",
                "status": "available",
                "protected_status": null,
                "replication_status": null,
                "health_status": null,
                "progress": 0,
                "priority_station": "source",
                "protected_instance_num": 0,
                "replication_num": 0,
                "disaster_recovery_drill_num": 0,
                "source_vpc_id": "046852ef-c49d-409b-8389-546aaaa5701f",
                "target_vpc_id": "046852ef-c49d-409b-8389-546aaaa5701f",
                "test_vpc_id": null,
                "dr_type": "migration",
                
                "created_at": "2019-05-23 03:51:58.256",
                "updated_at": "2019-05-23 07:48:12.484",
                "protection_type": "replication-pair",
                "replication_model": null
            },
            {
                "id": "decf224d-87fe-403a-8721-037a1a45c287",
                "name": "Protection-Group-lwx",
                "description": null,
                "source_availability_zone": "eu-de-01",
                "target_availability_zone": "eu-de-02",
                "domain_id": "fb4bb8e3-a574-4437-a156-78c916aeea4d",
                "domain_name": "ActiveactiveDomain",
                "status": "available",
                "protected_status": null,
                "replication_status": null,
                "health_status": null,
                "progress": 0,
                "priority_station": "source",
                "protected_instance_num": 0,
                "replication_num": 0,
                "disaster_recovery_drill_num": 0,
                "source_vpc_id": "046852ef-c49d-409b-8389-546aaaa5701f",
                "target_vpc_id": "046852ef-c49d-409b-8389-546aaaa5701f",
                "test_vpc_id": null,
                "dr_type": "migration",
                ,
                "created_at": "2019-05-22 08:16:54.413",
                "updated_at": "2019-05-23 07:48:12.493",
                "protection_type": "replication-pair",
                "replication_model": null
            }
       ] 
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



# Querying the Details of a Protection Group<a name="sdrs_05_0403"></a>

## Function<a name="en-us_topic_0079693002_section34649765"></a>

This API is used to query the details about a protection group, such as the protection group ID and name.

## Constraints and Limitations<a name="section1786733742514"></a>

None

## URI<a name="en-us_topic_0079693002_section39390935"></a>

-   URI format

    GET /v1/\{project\_id\}/server-groups/\{server\_group\_id\}

-   Parameter description

    <a name="en-us_topic_0079693002_table63321005"></a>
    <table><thead align="left"><tr id="en-us_topic_0079693002_row37593218"><th class="cellrowborder" valign="top" width="21.782178217821784%" id="mcps1.1.5.1.1"><p id="p196932036702"><a name="p196932036702"></a><a name="p196932036702"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="15.841584158415841%" id="mcps1.1.5.1.2"><p id="p7693736605"><a name="p7693736605"></a><a name="p7693736605"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="12.871287128712872%" id="mcps1.1.5.1.3"><p id="p7693123615017"><a name="p7693123615017"></a><a name="p7693123615017"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="49.504950495049506%" id="mcps1.1.5.1.4"><p id="p16693103614011"><a name="p16693103614011"></a><a name="p16693103614011"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0079693002_row29123463"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.1.5.1.1 "><p id="p1693173618016"><a name="p1693173618016"></a><a name="p1693173618016"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.1.5.1.2 "><p id="p1169314369015"><a name="p1169314369015"></a><a name="p1169314369015"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.1.5.1.3 "><p id="p869333614015"><a name="p869333614015"></a><a name="p869333614015"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.504950495049506%" headers="mcps1.1.5.1.4 "><p id="p186931736008"><a name="p186931736008"></a><a name="p186931736008"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row641619276586"><td class="cellrowborder" valign="top" width="21.782178217821784%" headers="mcps1.1.5.1.1 "><p id="p116934369015"><a name="p116934369015"></a><a name="p116934369015"></a>server_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="15.841584158415841%" headers="mcps1.1.5.1.2 "><p id="p6693133618014"><a name="p6693133618014"></a><a name="p6693133618014"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.871287128712872%" headers="mcps1.1.5.1.3 "><p id="p26930362014"><a name="p26930362014"></a><a name="p26930362014"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.504950495049506%" headers="mcps1.1.5.1.4 "><p id="p206933364011"><a name="p206933364011"></a><a name="p206933364011"></a>Specifies the ID of a protection group.</p>
    <p id="p1214719284341"><a name="p1214719284341"></a><a name="p1214719284341"></a>For details, see <a href="querying-protection-groups.md">Querying Protection Groups</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="en-us_topic_0079693002_section18974100"></a>

-   Request parameters

    None

-   Example request

    GET https://\{Endpoint\}/v1/\{project\_id\}/server-groups/decf224d-87fe-403a-8721-037a1a45c287


## Response<a name="en-us_topic_0079693002_section36549175"></a>

-   Parameter description

    <a name="table196985615184"></a>
    <table><thead align="left"><tr id="row5304167101814"><th class="cellrowborder" valign="top" width="29.07%" id="mcps1.1.4.1.1"><p id="p15304077181"><a name="p15304077181"></a><a name="p15304077181"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.44%" id="mcps1.1.4.1.2"><p id="p10304197101814"><a name="p10304197101814"></a><a name="p10304197101814"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.49%" id="mcps1.1.4.1.3"><p id="p1305127141811"><a name="p1305127141811"></a><a name="p1305127141811"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row17305107191820"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.1.4.1.1 "><p id="p1130516781816"><a name="p1130516781816"></a><a name="p1130516781816"></a>server_group</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.1.4.1.2 "><p id="p5305479182"><a name="p5305479182"></a><a name="p5305479182"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.1.4.1.3 "><p id="p1430516717182"><a name="p1430516717182"></a><a name="p1430516717182"></a>Specifies the details of a protection group.</p>
    <p id="p0854195513214"><a name="p0854195513214"></a><a name="p0854195513214"></a>For details, see <a href="#table137214610187">Table 1</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  1** **server\_group**  field description

    <a name="table137214610187"></a>
    <table><thead align="left"><tr id="row1130511721816"><th class="cellrowborder" valign="top" width="29.07%" id="mcps1.2.4.1.1"><p id="p183059712186"><a name="p183059712186"></a><a name="p183059712186"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.509999999999998%" id="mcps1.2.4.1.2"><p id="p23051875185"><a name="p23051875185"></a><a name="p23051875185"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="54.42%" id="mcps1.2.4.1.3"><p id="p2305177171819"><a name="p2305177171819"></a><a name="p2305177171819"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row43053721816"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p4305572182"><a name="p4305572182"></a><a name="p4305572182"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.509999999999998%" headers="mcps1.2.4.1.2 "><p id="p1305157191815"><a name="p1305157191815"></a><a name="p1305157191815"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.42%" headers="mcps1.2.4.1.3 "><p id="p730567191810"><a name="p730567191810"></a><a name="p730567191810"></a>Specifies the ID of a protection group.</p>
    </td>
    </tr>
    <tr id="row1630619761819"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p133061675183"><a name="p133061675183"></a><a name="p133061675183"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.509999999999998%" headers="mcps1.2.4.1.2 "><p id="p113066713185"><a name="p113066713185"></a><a name="p113066713185"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.42%" headers="mcps1.2.4.1.3 "><p id="p18306207121820"><a name="p18306207121820"></a><a name="p18306207121820"></a>Specifies the name of a protection group.</p>
    </td>
    </tr>
    <tr id="row9306575181"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p6306197101817"><a name="p6306197101817"></a><a name="p6306197101817"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.509999999999998%" headers="mcps1.2.4.1.2 "><p id="p133060719181"><a name="p133060719181"></a><a name="p133060719181"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.42%" headers="mcps1.2.4.1.3 "><p id="p1930647121816"><a name="p1930647121816"></a><a name="p1930647121816"></a>Specifies the description of a protection group.</p>
    </td>
    </tr>
    <tr id="row163061701813"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p63062076187"><a name="p63062076187"></a><a name="p63062076187"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.509999999999998%" headers="mcps1.2.4.1.2 "><p id="p10306167101820"><a name="p10306167101820"></a><a name="p10306167101820"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.42%" headers="mcps1.2.4.1.3 "><p id="p3306197181814"><a name="p3306197181814"></a><a name="p3306197181814"></a>Specifies the status of a protection group.</p>
    <p id="p22471848111518"><a name="p22471848111518"></a><a name="p22471848111518"></a>For details, see <a href="protection-group-status.md">Protection Group Status</a>.</p>
    </td>
    </tr>
    <tr id="row1730615713189"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p113062720188"><a name="p113062720188"></a><a name="p113062720188"></a>progress</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.509999999999998%" headers="mcps1.2.4.1.2 "><p id="p1830712716181"><a name="p1830712716181"></a><a name="p1830712716181"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.42%" headers="mcps1.2.4.1.3 "><p id="p1330727191818"><a name="p1330727191818"></a><a name="p1330727191818"></a>Specifies the synchronization progress of a protection group.</p>
    <p id="p12307127121818"><a name="p12307127121818"></a><a name="p12307127121818"></a>Unit: %</p>
    </td>
    </tr>
    <tr id="row0307975181"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p930712741820"><a name="p930712741820"></a><a name="p930712741820"></a>source_availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.509999999999998%" headers="mcps1.2.4.1.2 "><p id="p2307187201810"><a name="p2307187201810"></a><a name="p2307187201810"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.42%" headers="mcps1.2.4.1.3 "><p id="p1924824245820"><a name="p1924824245820"></a><a name="p1924824245820"></a>Specifies the production site AZ configured when a protection group is created.</p>
    <p id="p17155343195615"><a name="p17155343195615"></a><a name="p17155343195615"></a>The value does not change after a planned failover or failover.</p>
    </td>
    </tr>
    <tr id="row133074741820"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p23071473186"><a name="p23071473186"></a><a name="p23071473186"></a>target_availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.509999999999998%" headers="mcps1.2.4.1.2 "><p id="p13074710185"><a name="p13074710185"></a><a name="p13074710185"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.42%" headers="mcps1.2.4.1.3 "><p id="p1324834217585"><a name="p1324834217585"></a><a name="p1324834217585"></a>Specifies the DR site AZ configured when a protection group is created.</p>
    <p id="p17776141625919"><a name="p17776141625919"></a><a name="p17776141625919"></a>The value does not change after a planned failover or failover.</p>
    </td>
    </tr>
    <tr id="row173070741817"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p7307197131813"><a name="p7307197131813"></a><a name="p7307197131813"></a>domain_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.509999999999998%" headers="mcps1.2.4.1.2 "><p id="p1030716741814"><a name="p1030716741814"></a><a name="p1030716741814"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.42%" headers="mcps1.2.4.1.3 "><p id="p14307127171813"><a name="p14307127171813"></a><a name="p14307127171813"></a>Specifies the ID of an active-active domain.</p>
    </td>
    </tr>
    <tr id="row43071177184"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p530720717188"><a name="p530720717188"></a><a name="p530720717188"></a>domain_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.509999999999998%" headers="mcps1.2.4.1.2 "><p id="p13307078184"><a name="p13307078184"></a><a name="p13307078184"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.42%" headers="mcps1.2.4.1.3 "><p id="p6307187191819"><a name="p6307187191819"></a><a name="p6307187191819"></a>Specifies the name of an active-active domain.</p>
    </td>
    </tr>
    <tr id="row33071473183"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p20307776181"><a name="p20307776181"></a><a name="p20307776181"></a>priority_station</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.509999999999998%" headers="mcps1.2.4.1.2 "><p id="p13097721818"><a name="p13097721818"></a><a name="p13097721818"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.42%" headers="mcps1.2.4.1.3 "><p id="p131071535152615"><a name="p131071535152615"></a><a name="p131071535152615"></a>Specifies the current production site of a protection group.</p>
    <a name="ul1610773522614"></a><a name="ul1610773522614"></a><ul id="ul1610773522614"><li><strong id="b112131138183817"><a name="b112131138183817"></a><a name="b112131138183817"></a>source</strong>: indicates that the current production site AZ is the <strong id="b18213238203816"><a name="b18213238203816"></a><a name="b18213238203816"></a>source_availability_zone</strong> value.</li><li><strong id="b26381540153815"><a name="b26381540153815"></a><a name="b26381540153815"></a>target</strong>: indicates that the current production site AZ is the <strong id="b263924019387"><a name="b263924019387"></a><a name="b263924019387"></a>target_availability_zone</strong> value.</li></ul>
    </td>
    </tr>
    <tr id="row730997181811"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1030967161815"><a name="p1030967161815"></a><a name="p1030967161815"></a>protected_instance_num</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.509999999999998%" headers="mcps1.2.4.1.2 "><p id="p1230927121811"><a name="p1230927121811"></a><a name="p1230927121811"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.42%" headers="mcps1.2.4.1.3 "><p id="p630910719185"><a name="p630910719185"></a><a name="p630910719185"></a>Specifies the number of protected instances in a protection group.</p>
    </td>
    </tr>
    <tr id="row33091771811"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p83096710185"><a name="p83096710185"></a><a name="p83096710185"></a>replication_num</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.509999999999998%" headers="mcps1.2.4.1.2 "><p id="p8309579186"><a name="p8309579186"></a><a name="p8309579186"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.42%" headers="mcps1.2.4.1.3 "><p id="p102251831191914"><a name="p102251831191914"></a><a name="p102251831191914"></a>Specifies the number of replication pairs in a protection group.</p>
    </td>
    </tr>
    <tr id="row142115237160"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p19950730121614"><a name="p19950730121614"></a><a name="p19950730121614"></a>disaster_recovery_drill_num</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.509999999999998%" headers="mcps1.2.4.1.2 "><p id="p19950123010166"><a name="p19950123010166"></a><a name="p19950123010166"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.42%" headers="mcps1.2.4.1.3 "><p id="p179501630181613"><a name="p179501630181613"></a><a name="p179501630181613"></a>Specifies the number of DR drills in a protection group.</p>
    </td>
    </tr>
    <tr id="row33091373185"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p43098714185"><a name="p43098714185"></a><a name="p43098714185"></a>protected_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.509999999999998%" headers="mcps1.2.4.1.2 "><p id="p2030916710184"><a name="p2030916710184"></a><a name="p2030916710184"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.42%" headers="mcps1.2.4.1.3 "><p id="p730947201815"><a name="p730947201815"></a><a name="p730947201815"></a>Specifies whether protection is enabled or not.</p>
    <a name="ul11309167101820"></a><a name="ul11309167101820"></a><ul id="ul11309167101820"><li><strong id="b1415212501284"><a name="b1415212501284"></a><a name="b1415212501284"></a>started</strong>: Protection is enabled.</li><li><strong id="b136645542817"><a name="b136645542817"></a><a name="b136645542817"></a>stopped</strong>: Protection is disabled.</li></ul>
    <div class="note" id="note76221353195215"><a name="note76221353195215"></a><a name="note76221353195215"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p162255319523"><a name="p162255319523"></a><a name="p162255319523"></a>The system is upgraded recently. For protection groups created after the upgrade, the value of this parameter is <strong id="b16984252153816"><a name="b16984252153816"></a><a name="b16984252153816"></a>null</strong>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row13107791817"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1931012731819"><a name="p1931012731819"></a><a name="p1931012731819"></a>replication_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.509999999999998%" headers="mcps1.2.4.1.2 "><p id="p17310197171819"><a name="p17310197171819"></a><a name="p17310197171819"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.42%" headers="mcps1.2.4.1.3 "><p id="p17310171185"><a name="p17310171185"></a><a name="p17310171185"></a>Specifies the data synchronization status.</p>
    <a name="ul1231014717183"></a><a name="ul1231014717183"></a><ul id="ul1231014717183"><li><strong id="b45671721496"><a name="b45671721496"></a><a name="b45671721496"></a>active</strong>: Data has been synchronized.</li><li><strong id="b1479811519913"><a name="b1479811519913"></a><a name="b1479811519913"></a>inactive</strong>: Data is not synchronized.</li><li><strong>copying</strong>: Data is being synchronized.</li><li><strong id="b873942274910"><a name="b873942274910"></a><a name="b873942274910"></a>active-stopped</strong>: Data synchronization is stopped.</li></ul>
    <div class="note" id="note6413165811363"><a name="note6413165811363"></a><a name="note6413165811363"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1041435815367"><a name="p1041435815367"></a><a name="p1041435815367"></a>The system is upgraded recently. For protection groups created after the upgrade, the value of this parameter is <strong id="b867518823610"><a name="b867518823610"></a><a name="b867518823610"></a>null</strong>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row123104715180"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1731018713187"><a name="p1731018713187"></a><a name="p1731018713187"></a>health_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.509999999999998%" headers="mcps1.2.4.1.2 "><p id="p183104716183"><a name="p183104716183"></a><a name="p183104716183"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.42%" headers="mcps1.2.4.1.3 "><p id="p173104711182"><a name="p173104711182"></a><a name="p173104711182"></a>Specifies the health status of a protection group.</p>
    <a name="ul1431027201816"></a><a name="ul1431027201816"></a><ul id="ul1431027201816"><li><strong id="b573101420919"><a name="b573101420919"></a><a name="b573101420919"></a>normal</strong>: The protection group is normal.</li><li><strong id="b556914181493"><a name="b556914181493"></a><a name="b556914181493"></a>abnormal</strong>: The protection group is abnormal.</li></ul>
    <div class="note" id="note5601173317499"><a name="note5601173317499"></a><a name="note5601173317499"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p16601133164914"><a name="p16601133164914"></a><a name="p16601133164914"></a>The system is upgraded recently. For protection groups created after the upgrade, the value of this parameter is <strong id="b14427113274018"><a name="b14427113274018"></a><a name="b14427113274018"></a>null</strong>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row8310187101813"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p13108716184"><a name="p13108716184"></a><a name="p13108716184"></a>source_vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.509999999999998%" headers="mcps1.2.4.1.2 "><p id="p11310877188"><a name="p11310877188"></a><a name="p11310877188"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.42%" headers="mcps1.2.4.1.3 "><p id="p031019714182"><a name="p031019714182"></a><a name="p031019714182"></a>Specifies the ID of the VPC for the production site.</p>
    </td>
    </tr>
    <tr id="row143108714185"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p6310167151820"><a name="p6310167151820"></a><a name="p6310167151820"></a>target_vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.509999999999998%" headers="mcps1.2.4.1.2 "><p id="p831019715189"><a name="p831019715189"></a><a name="p831019715189"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.42%" headers="mcps1.2.4.1.3 "><p id="p73107761816"><a name="p73107761816"></a><a name="p73107761816"></a>Specifies the ID of the VPC for the DR site.</p>
    </td>
    </tr>
    <tr id="row203106761813"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p123108731810"><a name="p123108731810"></a><a name="p123108731810"></a>test_vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.509999999999998%" headers="mcps1.2.4.1.2 "><p id="p1631014717187"><a name="p1631014717187"></a><a name="p1631014717187"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.42%" headers="mcps1.2.4.1.3 "><p id="p679912462113"><a name="p679912462113"></a><a name="p679912462113"></a>Specifies the ID of the VPC used for a DR drill.</p>
    <div class="note" id="note37861924172113"><a name="note37861924172113"></a><a name="note37861924172113"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1378616248213"><a name="p1378616248213"></a><a name="p1378616248213"></a>This parameter is reserved.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row63104751811"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p18311107101814"><a name="p18311107101814"></a><a name="p18311107101814"></a>dr_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.509999999999998%" headers="mcps1.2.4.1.2 "><p id="p5311167121818"><a name="p5311167121818"></a><a name="p5311167121818"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.42%" headers="mcps1.2.4.1.3 "><p id="p431112731818"><a name="p431112731818"></a><a name="p431112731818"></a>Specifies the deployment model. The default value is <strong id="b1963647298"><a name="b1963647298"></a><a name="b1963647298"></a>migration</strong>, indicating migration within a VPC.</p>
    </td>
    </tr>
    <tr id="row33111781814"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p5311197141811"><a name="p5311197141811"></a><a name="p5311197141811"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.509999999999998%" headers="mcps1.2.4.1.2 "><p id="p1331116701814"><a name="p1331116701814"></a><a name="p1331116701814"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.42%" headers="mcps1.2.4.1.3 "><p id="p142344961915"><a name="p142344961915"></a><a name="p142344961915"></a>Specifies the time when a protection group was created.</p>
    <p id="p956113341684"><a name="p956113341684"></a><a name="p956113341684"></a>The default format is as follows: "yyyy-MM-dd'T'HH:mm:ss.SSSZ", for example, <strong id="b13531651428"><a name="b13531651428"></a><a name="b13531651428"></a>2019-04-01T12:00:00.000Z</strong>.</p>
    </td>
    </tr>
    <tr id="row173111778187"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1331116741817"><a name="p1331116741817"></a><a name="p1331116741817"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.509999999999998%" headers="mcps1.2.4.1.2 "><p id="p17311127131810"><a name="p17311127131810"></a><a name="p17311127131810"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.42%" headers="mcps1.2.4.1.3 "><p id="p4937194917196"><a name="p4937194917196"></a><a name="p4937194917196"></a>Specifies the time when a protection group was updated.</p>
    <p id="p5750101910918"><a name="p5750101910918"></a><a name="p5750101910918"></a>The default format is as follows: "yyyy-MM-dd'THH:mm:ss.SSSZ", for example, <strong id="b793211612429"><a name="b793211612429"></a><a name="b793211612429"></a>2019-04-01T12:00:00.000Z</strong>.</p>
    </td>
    </tr>
    <tr id="row141671032161819"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1416763219184"><a name="p1416763219184"></a><a name="p1416763219184"></a>protection_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.509999999999998%" headers="mcps1.2.4.1.2 "><p id="p101678327184"><a name="p101678327184"></a><a name="p101678327184"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.42%" headers="mcps1.2.4.1.3 "><p id="p137228404418"><a name="p137228404418"></a><a name="p137228404418"></a>Specifies the protection mode.</p>
    <a name="ul1022812151351"></a><a name="ul1022812151351"></a><ul id="ul1022812151351"><li><strong id="b187503498152"><a name="b187503498152"></a><a name="b187503498152"></a>null</strong>: indicates that data synchronization is performed at the replication consistency group level. No partial synchronization failure will occur.</li><li><strong id="b2971738164"><a name="b2971738164"></a><a name="b2971738164"></a>replication-pair</strong>: indicates that data synchronization is performed at the replication pair level.</li></ul>
    </td>
    </tr>
    <tr id="row108144414914"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p261318522911"><a name="p261318522911"></a><a name="p261318522911"></a>replication_model</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.509999999999998%" headers="mcps1.2.4.1.2 "><p id="p96152525910"><a name="p96152525910"></a><a name="p96152525910"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.42%" headers="mcps1.2.4.1.3 "><p id="p96158524910"><a name="p96158524910"></a><a name="p96158524910"></a>Specifies the protection mode.</p>
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
            "server_type": "ECS",
            "created_at": "2019-05-22 08:16:54.413",
            "updated_at": "2019-05-23 09:11:10.856",
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

    In the preceding example,  **error**  indicates a general error, for example,  **badrequest**  or  **itemNotFound**. An example is provided as follows:

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



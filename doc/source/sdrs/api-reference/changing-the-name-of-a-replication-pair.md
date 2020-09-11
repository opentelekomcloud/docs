# Changing the Name of a Replication Pair<a name="sdrs_05_0606"></a>

## Function<a name="en-us_topic_0079693002_section34649765"></a>

This API is used to change the name of a replication pair.

## Constraints and Limitations<a name="section11660716431"></a>

None

## URI<a name="en-us_topic_0079693002_section39390935"></a>

-   URI format

    PUT /v1/\{project\_id\}/replications/\{replication\_id\}

-   Parameter description

    <a name="en-us_topic_0079693002_table63321005"></a>
    <table><thead align="left"><tr id="en-us_topic_0079693002_row37593218"><th class="cellrowborder" valign="top" width="16.831683168316832%" id="mcps1.1.5.1.1"><p id="p16123418165411"><a name="p16123418165411"></a><a name="p16123418165411"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.861386138613863%" id="mcps1.1.5.1.2"><p id="p1212317182542"><a name="p1212317182542"></a><a name="p1212317182542"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.801980198019802%" id="mcps1.1.5.1.3"><p id="p13123418125418"><a name="p13123418125418"></a><a name="p13123418125418"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="49.504950495049506%" id="mcps1.1.5.1.4"><p id="p16123191814545"><a name="p16123191814545"></a><a name="p16123191814545"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0079693002_row29123463"><td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.1.5.1.1 "><p id="p312316183544"><a name="p312316183544"></a><a name="p312316183544"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.1.5.1.2 "><p id="p16123018145414"><a name="p16123018145414"></a><a name="p16123018145414"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.1.5.1.3 "><p id="p121231183546"><a name="p121231183546"></a><a name="p121231183546"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.504950495049506%" headers="mcps1.1.5.1.4 "><p id="p1612441818547"><a name="p1612441818547"></a><a name="p1612441818547"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row14685154914717"><td class="cellrowborder" valign="top" width="16.831683168316832%" headers="mcps1.1.5.1.1 "><p id="p11241181541"><a name="p11241181541"></a><a name="p11241181541"></a>replication_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.1.5.1.2 "><p id="p3124111835412"><a name="p3124111835412"></a><a name="p3124111835412"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.801980198019802%" headers="mcps1.1.5.1.3 "><p id="p2124181885411"><a name="p2124181885411"></a><a name="p2124181885411"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="49.504950495049506%" headers="mcps1.1.5.1.4 "><p id="p1512420181549"><a name="p1512420181549"></a><a name="p1512420181549"></a>Specifies the ID of a replication pair.</p>
    <p id="p521381043819"><a name="p521381043819"></a><a name="p521381043819"></a>You can obtain this value by calling the API described in <a href="querying-replication-pairs.md">Querying Replication Pairs</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="en-us_topic_0079693002_section18974100"></a>

-   Parameter description

    <a name="en-us_topic_0079693002_table54932709"></a>
    <table><thead align="left"><tr id="en-us_topic_0079693002_row41882373"><th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.1"><p id="p209793875410"><a name="p209793875410"></a><a name="p209793875410"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.1.5.1.2"><p id="p10973388546"><a name="p10973388546"></a><a name="p10973388546"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.1.5.1.3"><p id="p1497173815542"><a name="p1497173815542"></a><a name="p1497173815542"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.1.5.1.4"><p id="p697103820548"><a name="p697103820548"></a><a name="p697103820548"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0079693002_row27990155"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p19818381546"><a name="p19818381546"></a><a name="p19818381546"></a>replication</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.2 "><p id="p1498183817546"><a name="p1498183817546"></a><a name="p1498183817546"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.3 "><p id="p16968235172711"><a name="p16968235172711"></a><a name="p16968235172711"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.5.1.4 "><p id="p6775152192218"><a name="p6775152192218"></a><a name="p6775152192218"></a>Specifies the information about a replication pair.</p>
    <p id="p89681835132715"><a name="p89681835132715"></a><a name="p89681835132715"></a>For details, see <a href="#table920673314542">Table 1</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  1** **replication**  field description

    <a name="table920673314542"></a>
    <table><thead align="left"><tr id="row1320623313547"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p162061733155416"><a name="p162061733155416"></a><a name="p162061733155416"></a><strong id="b114146194273"><a name="b114146194273"></a><a name="b114146194273"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.2"><p id="p1820613311541"><a name="p1820613311541"></a><a name="p1820613311541"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.91%" id="mcps1.2.5.1.3"><p id="p17206143375412"><a name="p17206143375412"></a><a name="p17206143375412"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.089999999999996%" id="mcps1.2.5.1.4"><p id="p14207193345412"><a name="p14207193345412"></a><a name="p14207193345412"></a><strong id="b1310516216273"><a name="b1310516216273"></a><a name="b1310516216273"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row122071033105418"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1120719339543"><a name="p1120719339543"></a><a name="p1120719339543"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p7207103355415"><a name="p7207103355415"></a><a name="p7207103355415"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.91%" headers="mcps1.2.5.1.3 "><p id="p112071633145415"><a name="p112071633145415"></a><a name="p112071633145415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.089999999999996%" headers="mcps1.2.5.1.4 "><p id="p1479716315228"><a name="p1479716315228"></a><a name="p1479716315228"></a>Specifies the name of a replication pair.</p>
    <a name="ul5614124172319"></a><a name="ul5614124172319"></a><ul id="ul5614124172319"><li>The name can contain a maximum of 64 bytes.</li><li>The value can contain only letters (a to z and A to Z), digits (0 to 9), decimal points (.), underscores (_), and hyphens (-).</li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    PUT https://\{Endpoint\}/v1/\{project\_id\}/replications/b93bc1c4-67ee-45a1-bc8a-d022fdd28811

    ```
    {   
         "replication": {  
             "name": "new_name"
         }  
     }
    ```


## Response<a name="en-us_topic_0079693002_section36549175"></a>

-   Parameter description

    <a name="table465215219513"></a>
    <table><thead align="left"><tr id="row126963528514"><th class="cellrowborder" valign="top" width="29.07%" id="mcps1.1.4.1.1"><p id="p1265619171555"><a name="p1265619171555"></a><a name="p1265619171555"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.44%" id="mcps1.1.4.1.2"><p id="p10656161785513"><a name="p10656161785513"></a><a name="p10656161785513"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.49%" id="mcps1.1.4.1.3"><p id="p176561817195512"><a name="p176561817195512"></a><a name="p176561817195512"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1069615213516"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.1.4.1.1 "><p id="p119971152102712"><a name="p119971152102712"></a><a name="p119971152102712"></a>replication</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.1.4.1.2 "><p id="p1599775252718"><a name="p1599775252718"></a><a name="p1599775252718"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.1.4.1.3 "><p id="p14997125292713"><a name="p14997125292713"></a><a name="p14997125292713"></a>Specifies the information about a replication pair.</p>
    <p id="p397194617589"><a name="p397194617589"></a><a name="p397194617589"></a>For details, see <a href="#table19857114112554">Table 2</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2** **replication**  field description

    <a name="table19857114112554"></a>
    <table><thead align="left"><tr id="row17512428557"><th class="cellrowborder" valign="top" width="29.07%" id="mcps1.2.4.1.1"><p id="p051342115511"><a name="p051342115511"></a><a name="p051342115511"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.44%" id="mcps1.2.4.1.2"><p id="p3511142205512"><a name="p3511142205512"></a><a name="p3511142205512"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.49%" id="mcps1.2.4.1.3"><p id="p1251194212554"><a name="p1251194212554"></a><a name="p1251194212554"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1051442105519"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p15184285510"><a name="p15184285510"></a><a name="p15184285510"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p165115421558"><a name="p165115421558"></a><a name="p165115421558"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p175114424552"><a name="p175114424552"></a><a name="p175114424552"></a>Specifies the ID of a replication pair.</p>
    </td>
    </tr>
    <tr id="row151174218555"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p751742165511"><a name="p751742165511"></a><a name="p751742165511"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p6511842145517"><a name="p6511842145517"></a><a name="p6511842145517"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p165114285516"><a name="p165114285516"></a><a name="p165114285516"></a>Specifies the name of a replication pair. Specifies the name of a replication pair. The name can contain a maximum of 64 bytes. The value can contain only letters (a to z and A to Z), digits (0 to 9), decimal points (.), underscores (_), and hyphens (-).</p>
    </td>
    </tr>
    <tr id="row85114212551"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1451442145513"><a name="p1451442145513"></a><a name="p1451442145513"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p251174235515"><a name="p251174235515"></a><a name="p251174235515"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p1651842145517"><a name="p1651842145517"></a><a name="p1651842145517"></a>Specifies the description of a replication pair.</p>
    </td>
    </tr>
    <tr id="row15540543125112"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1953204265514"><a name="p1953204265514"></a><a name="p1953204265514"></a>replication_model</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p053134218554"><a name="p053134218554"></a><a name="p053134218554"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p20538424553"><a name="p20538424553"></a><a name="p20538424553"></a>Specifies the replication mode of a replication pair. The default value is <strong id="b84235270610245"><a name="b84235270610245"></a><a name="b84235270610245"></a>hypermetro</strong>, indicating synchronous replication.</p>
    </td>
    </tr>
    <tr id="row3511142135516"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1651194225510"><a name="p1651194225510"></a><a name="p1651194225510"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p1511842165515"><a name="p1511842165515"></a><a name="p1511842165515"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p97513911413"><a name="p97513911413"></a><a name="p97513911413"></a>Specifies the status of a replication pair.</p>
    <p id="p1151164225514"><a name="p1151164225514"></a><a name="p1151164225514"></a>For details, see <a href="replication-pair-status.md">Replication Pair Status</a>.</p>
    </td>
    </tr>
    <tr id="row633971219514"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p85324212551"><a name="p85324212551"></a><a name="p85324212551"></a>progress</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p45314275512"><a name="p45314275512"></a><a name="p45314275512"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p85310428558"><a name="p85310428558"></a><a name="p85310428558"></a>Specifies the synchronization progress of a replication pair.</p>
    <p id="p19531426552"><a name="p19531426552"></a><a name="p19531426552"></a>Unit: %</p>
    </td>
    </tr>
    <tr id="row19831727145111"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1931012731819"><a name="p1931012731819"></a><a name="p1931012731819"></a>replication_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p19589849375"><a name="p19589849375"></a><a name="p19589849375"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p17310171185"><a name="p17310171185"></a><a name="p17310171185"></a>Specifies the data synchronization status.</p>
    <a name="ul1231014717183"></a><a name="ul1231014717183"></a><ul id="ul1231014717183"><li><strong id="b1074474953511"><a name="b1074474953511"></a><a name="b1074474953511"></a>active</strong>: Data has been synchronized.</li><li><strong id="b11862565353"><a name="b11862565353"></a><a name="b11862565353"></a>inactive</strong>: Data is not synchronized.</li><li><strong id="b2558185793513"><a name="b2558185793513"></a><a name="b2558185793513"></a>copying</strong>: Data is being synchronized.</li><li><strong id="b1346365915355"><a name="b1346365915355"></a><a name="b1346365915355"></a>active-stopped</strong>: Data synchronization is stopped.</li></ul>
    </td>
    </tr>
    <tr id="row419515154521"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p251154214553"><a name="p251154214553"></a><a name="p251154214553"></a>attachment</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p95116425551"><a name="p95116425551"></a><a name="p95116425551"></a>Null</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p16511421551"><a name="p16511421551"></a><a name="p16511421551"></a>Specifies the device name.</p>
    <p id="p165287287598"><a name="p165287287598"></a><a name="p165287287598"></a>For details, see <a href="#table474813685911">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="row85184219559"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p16512426555"><a name="p16512426555"></a><a name="p16512426555"></a>volume_ids</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p12511442175519"><a name="p12511442175519"></a><a name="p12511442175519"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p135194255510"><a name="p135194255510"></a><a name="p135194255510"></a>Specifies the ID of the disk used to create a replication pair.</p>
    </td>
    </tr>
    <tr id="row85164215555"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1310134114816"><a name="p1310134114816"></a><a name="p1310134114816"></a>server_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p171011454814"><a name="p171011454814"></a><a name="p171011454814"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p181074144815"><a name="p181074144815"></a><a name="p181074144815"></a>Specifies the ID of a protection group.</p>
    </td>
    </tr>
    <tr id="row5642444135216"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p210940487"><a name="p210940487"></a><a name="p210940487"></a>priority_station</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p910134174818"><a name="p910134174818"></a><a name="p910134174818"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p14104484816"><a name="p14104484816"></a><a name="p14104484816"></a>Specifies the current production site AZ of the protection group containing the replication pair.</p>
    <a name="ul3102418482"></a><a name="ul3102418482"></a><ul id="ul3102418482"><li><strong id="b12296144565810"><a name="b12296144565810"></a><a name="b12296144565810"></a>source</strong>: indicates that the current production site AZ is the <strong id="b9298194585815"><a name="b9298194585815"></a><a name="b9298194585815"></a>source_availability_zone</strong> value.</li><li><strong id="b7392174745819"><a name="b7392174745819"></a><a name="b7392174745819"></a>target</strong>: indicates that the current production site AZ is the <strong id="b739364715586"><a name="b739364715586"></a><a name="b739364715586"></a>target_availability_zone</strong> value.</li></ul>
    </td>
    </tr>
    <tr id="row1789201395311"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p75317421552"><a name="p75317421552"></a><a name="p75317421552"></a>fault_level</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p1536421553"><a name="p1536421553"></a><a name="p1536421553"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p1953242125513"><a name="p1953242125513"></a><a name="p1953242125513"></a>Specifies the fault level of a replication pair.</p>
    <a name="ul115384210552"></a><a name="ul115384210552"></a><ul id="ul115384210552"><li><strong id="b132010410187"><a name="b132010410187"></a><a name="b132010410187"></a>0</strong>: No fault occurs.</li><li><strong id="b161231612125710"><a name="b161231612125710"></a><a name="b161231612125710"></a>2</strong>: The disk of the current production site does not have read/write permissions. In this case, you are advised to perform a failover.</li><li><strong id="b7782174810189"><a name="b7782174810189"></a><a name="b7782174810189"></a>5</strong>: The replication link is disconnected. In this case, a failover is not allowed. Contact the <span id="text1533123393119"><a name="text1533123393119"></a><a name="text1533123393119"></a>customer service</span> to obtain technical support.</li></ul>
    </td>
    </tr>
    <tr id="row85124265512"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p145116420555"><a name="p145116420555"></a><a name="p145116420555"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p1451154217557"><a name="p1451154217557"></a><a name="p1451154217557"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p2512042195514"><a name="p2512042195514"></a><a name="p2512042195514"></a>Specifies the time when a replication pair was created.</p>
    <p id="p5259113654815"><a name="p5259113654815"></a><a name="p5259113654815"></a>The default format is as follows: ""yyyy-MM-ddTHH:mm:ss.SSSSSS", for example, <strong id="b823117472273"><a name="b823117472273"></a><a name="b823117472273"></a>2019-04-01T12:00:00.000000</strong>.</p>
    </td>
    </tr>
    <tr id="row651142195514"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p151124245510"><a name="p151124245510"></a><a name="p151124245510"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p135184215512"><a name="p135184215512"></a><a name="p135184215512"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p251164205513"><a name="p251164205513"></a><a name="p251164205513"></a>Specifies the time when a replication pair was updated.</p>
    <p id="p1347144974817"><a name="p1347144974817"></a><a name="p1347144974817"></a>The default format is as follows: "yyyy-MM-ddTHH:mm:ss.SSSSSS", for example, <strong id="b1820591318283"><a name="b1820591318283"></a><a name="b1820591318283"></a>2019-04-01T12:00:00.000000</strong>.</p>
    </td>
    </tr>
    <tr id="row35116426555"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1753194285515"><a name="p1753194285515"></a><a name="p1753194285515"></a>record_metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p125324215559"><a name="p125324215559"></a><a name="p125324215559"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p953194225513"><a name="p953194225513"></a><a name="p953194225513"></a>Specifies the SDR data of a replication pair.</p>
    <p id="p1986818451009"><a name="p1986818451009"></a><a name="p1986818451009"></a>For details, see <a href="#table177491965597">Table 4</a>.</p>
    </td>
    </tr>
    <tr id="row5531042175517"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p17531842175511"><a name="p17531842175511"></a><a name="p17531842175511"></a>failure_detail</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p75344285516"><a name="p75344285516"></a><a name="p75344285516"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p145354215513"><a name="p145354215513"></a><a name="p145354215513"></a>Specifies the error code returned only when <strong id="b136121118251"><a name="b136121118251"></a><a name="b136121118251"></a>status</strong> of a replication pair is <strong id="b1561917119254"><a name="b1561917119254"></a><a name="b1561917119254"></a>error</strong>.</p>
    <p id="p1834655318519"><a name="p1834655318519"></a><a name="p1834655318519"></a>For details, see the returned value in <a href="error-code-description.md">Error Code Description</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **attachment**  field description

    <a name="table474813685911"></a>
    <table><thead align="left"><tr id="row1074710645910"><th class="cellrowborder" valign="top" width="29.07%" id="mcps1.2.4.1.1"><p id="p14747264599"><a name="p14747264599"></a><a name="p14747264599"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.44%" id="mcps1.2.4.1.2"><p id="p157470685911"><a name="p157470685911"></a><a name="p157470685911"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.49%" id="mcps1.2.4.1.3"><p id="p127475617596"><a name="p127475617596"></a><a name="p127475617596"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row187473617593"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p8747962590"><a name="p8747962590"></a><a name="p8747962590"></a>protected_instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p9747364597"><a name="p9747364597"></a><a name="p9747364597"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p474712615914"><a name="p474712615914"></a><a name="p474712615914"></a>Specifies the ID of the protected instance to which the replication pair is attached.</p>
    </td>
    </tr>
    <tr id="row37484645917"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p2747663593"><a name="p2747663593"></a><a name="p2747663593"></a>device</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p177478611591"><a name="p177478611591"></a><a name="p177478611591"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p7748463593"><a name="p7748463593"></a><a name="p7748463593"></a>Specifies the device name.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **record\_metadata**  field description

    <a name="table177491965597"></a>
    <table><thead align="left"><tr id="row1748362590"><th class="cellrowborder" valign="top" width="29.07%" id="mcps1.2.4.1.1"><p id="p1774846155915"><a name="p1774846155915"></a><a name="p1774846155915"></a><strong id="b842352706151210"><a name="b842352706151210"></a><a name="b842352706151210"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.44%" id="mcps1.2.4.1.2"><p id="p9748361595"><a name="p9748361595"></a><a name="p9748361595"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.49%" id="mcps1.2.4.1.3"><p id="p374856125918"><a name="p374856125918"></a><a name="p374856125918"></a><strong id="b84235270615457"><a name="b84235270615457"></a><a name="b84235270615457"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row77485611596"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1574820619597"><a name="p1574820619597"></a><a name="p1574820619597"></a>multiattach</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p1874819614597"><a name="p1874819614597"></a><a name="p1874819614597"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p117480635915"><a name="p117480635915"></a><a name="p117480635915"></a>Specifies whether the disk in a replication pair is a shared disk.</p>
    </td>
    </tr>
    <tr id="row14748969598"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p87486614594"><a name="p87486614594"></a><a name="p87486614594"></a>bootable</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p197483615917"><a name="p197483615917"></a><a name="p197483615917"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p774819695914"><a name="p774819695914"></a><a name="p774819695914"></a>Specifies whether the disk in a replication pair is a system disk.</p>
    </td>
    </tr>
    <tr id="row97490655917"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p187499615591"><a name="p187499615591"></a><a name="p187499615591"></a>volume_size</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p174996155910"><a name="p174996155910"></a><a name="p174996155910"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p137491266599"><a name="p137491266599"></a><a name="p137491266599"></a>Specifies the size of the disk in a replication pair. Unit: GB</p>
    </td>
    </tr>
    <tr id="row77499610590"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p187491461596"><a name="p187491461596"></a><a name="p187491461596"></a>volume_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p11749116115918"><a name="p11749116115918"></a><a name="p11749116115918"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p1274917611595"><a name="p1274917611595"></a><a name="p1274917611595"></a>Specifies the type of the disk in a replication pair.</p>
    <a name="ul188853197144"></a><a name="ul188853197144"></a><ul id="ul188853197144"><li><strong id="b185015119298"><a name="b185015119298"></a><a name="b185015119298"></a>SATA</strong>: common I/O</li><li><strong id="b213920310298"><a name="b213920310298"></a><a name="b213920310298"></a>SAS</strong>: high I/O</li><li><strong id="b147601844297"><a name="b147601844297"></a><a name="b147601844297"></a>SSD</strong>: ultra-high I/O</li><li><strong id="b1269416142914"><a name="b1269416142914"></a><a name="b1269416142914"></a>co-p1</strong>: high I/O (performance-optimized I)</li><li><strong id="b1860417812916"><a name="b1860417812916"></a><a name="b1860417812916"></a>uh-l1</strong>: ultra-high I/O (latency-optimized)<p id="p159027562599"><a name="p159027562599"></a><a name="p159027562599"></a>Disks of the co-p1 and uh-l1 types can be used on servers of the HANA, HL1, and HL2 types only.</p>
    </li></ul>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    { 
         "replication":  
             { 
                 "id": "b93bc1c4-67ee-45a1-bc8a-d022fdd28811", 
                 "name": "new_name", 
                 "description": "test_description", 
                 "replication_model": "hypermetro", 
                 "status": "available", 
                 "progress": 0, 
                 "replication_status": "active",
                 "attachment": null, 
                 "volume_ids": "48dda0c0-c800-46f2-9728-a519ff783d35,388b324a-a9d1-44a4-a00d-42085f22a9bc", 
                 "server_group_id": "0000000062d194520162d196f0fe0007", 
                 "priority_station": "source", 
                 "fault_level": "0", 
                 "created_at": "2018-05-04T03:43:24.108526", 
                 "updated_at": "2018-05-04T03:44:28.322873", 
                 "record_metadata": { 
                     "multiattach": false, 
                     "bootable": false, 
                     "volume_size": "10", 
                     "volume_type": "SATA" 
                 } 
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



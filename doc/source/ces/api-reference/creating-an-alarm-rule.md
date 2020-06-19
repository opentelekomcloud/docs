# Creating an Alarm Rule<a name="EN-US_TOPIC_0171212622"></a>

## Function<a name="section690717184830"></a>

This API is used to create an alarm rule.

## URI<a name="section33770965184830"></a>

POST /V1.0/\{project\_id\}/alarms

-   Parameter description

    **Table  1**  Parameter description

    <a name="table16558749184830"></a>
    <table><thead align="left"><tr id="row13099266184830"><th class="cellrowborder" valign="top" width="19.39%" id="mcps1.2.4.1.1"><p id="p54407610184830"><a name="p54407610184830"></a><a name="p54407610184830"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.41%" id="mcps1.2.4.1.2"><p id="p44940266184830"><a name="p44940266184830"></a><a name="p44940266184830"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="60.199999999999996%" id="mcps1.2.4.1.3"><p id="p16282939184830"><a name="p16282939184830"></a><a name="p16282939184830"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row43849684184830"><td class="cellrowborder" valign="top" width="19.39%" headers="mcps1.2.4.1.1 "><p id="p62163550184830"><a name="p62163550184830"></a><a name="p62163550184830"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.41%" headers="mcps1.2.4.1.2 "><p id="p2082817184830"><a name="p2082817184830"></a><a name="p2082817184830"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.199999999999996%" headers="mcps1.2.4.1.3 "><p id="p34490468184830"><a name="p34490468184830"></a><a name="p34490468184830"></a>Specifies the project ID.</p>
    <p id="p297103313620"><a name="p297103313620"></a><a name="p297103313620"></a>For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example

    ```
    POST https://{Cloud Eye endpoint}/V1.0/{project_id}/alarms
    ```


## Request<a name="section7848679184830"></a>

-   Request parameters

    **Table  2**  Request parameters

    <a name="table22684858184830"></a>
    <table><thead align="left"><tr id="row36700749184830"><th class="cellrowborder" valign="top" width="22%" id="mcps1.2.5.1.1"><p id="p19970684184830"><a name="p19970684184830"></a><a name="p19970684184830"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="21%" id="mcps1.2.5.1.2"><p id="p7012732184830"><a name="p7012732184830"></a><a name="p7012732184830"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.3"><p id="p31160437184830"><a name="p31160437184830"></a><a name="p31160437184830"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="42%" id="mcps1.2.5.1.4"><p id="p40967438184830"><a name="p40967438184830"></a><a name="p40967438184830"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row30028143184830"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.1 "><p id="p16360513184830"><a name="p16360513184830"></a><a name="p16360513184830"></a>alarm_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.2 "><p id="p50133163184830"><a name="p50133163184830"></a><a name="p50133163184830"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p34254422184830"><a name="p34254422184830"></a><a name="p34254422184830"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.5.1.4 "><p id="p1343492116295"><a name="p1343492116295"></a><a name="p1343492116295"></a>Specifies the alarm rule name.</p>
    <p id="p5367528415826"><a name="p5367528415826"></a><a name="p5367528415826"></a>The value can be a string of 1 to 128 characters that can contain only digits, lowercase letters, uppercase letters, underscores (_), and hyphens (-).</p>
    </td>
    </tr>
    <tr id="row6976698184830"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.1 "><p id="p28241661184830"><a name="p28241661184830"></a><a name="p28241661184830"></a>alarm_description</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.2 "><p id="p5873213184830"><a name="p5873213184830"></a><a name="p5873213184830"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p37551225183318"><a name="p37551225183318"></a><a name="p37551225183318"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.5.1.4 "><p id="p13664210184830"><a name="p13664210184830"></a><a name="p13664210184830"></a>Alarm description. The length is 0-256.</p>
    </td>
    </tr>
    <tr id="row55869026184830"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.1 "><p id="p29097264184830"><a name="p29097264184830"></a><a name="p29097264184830"></a>metric</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.2 "><p id="p8068223184830"><a name="p8068223184830"></a><a name="p8068223184830"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p49546359184830"><a name="p49546359184830"></a><a name="p49546359184830"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.5.1.4 "><p id="p53832127184830"><a name="p53832127184830"></a><a name="p53832127184830"></a>Specifies the alarm metrics.</p>
    <p id="p1786753174815"><a name="p1786753174815"></a><a name="p1786753174815"></a>For details, see <a href="#table1358724013016">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="row52573824184830"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.1 "><p id="p30621327184830"><a name="p30621327184830"></a><a name="p30621327184830"></a>condition</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.2 "><p id="p64408411184830"><a name="p64408411184830"></a><a name="p64408411184830"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p640316326148"><a name="p640316326148"></a><a name="p640316326148"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.5.1.4 "><p id="p66176839184830"><a name="p66176839184830"></a><a name="p66176839184830"></a>Specifies the alarm triggering condition.</p>
    <p id="p096312292486"><a name="p096312292486"></a><a name="p096312292486"></a>For details, see <a href="#table159417407300">Table 8</a>.</p>
    </td>
    </tr>
    <tr id="row33885327184830"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.1 "><p id="p60356933184830"><a name="p60356933184830"></a><a name="p60356933184830"></a>alarm_enabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.2 "><p id="p57073404184830"><a name="p57073404184830"></a><a name="p57073404184830"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p59543003184830"><a name="p59543003184830"></a><a name="p59543003184830"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.5.1.4 "><p id="p37412483163151"><a name="p37412483163151"></a><a name="p37412483163151"></a>Specifies whether to enable the alarm.</p>
    <p id="p189105215826"><a name="p189105215826"></a><a name="p189105215826"></a>The default value is <strong id="b842352706151625"><a name="b842352706151625"></a><a name="b842352706151625"></a>true</strong>.</p>
    </td>
    </tr>
    <tr id="row12209165924615"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.1 "><p id="p54337493184830"><a name="p54337493184830"></a><a name="p54337493184830"></a>alarm_action_enabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.2 "><p id="p39260773184830"><a name="p39260773184830"></a><a name="p39260773184830"></a>Mandatory under certain conditions</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p26006017184830"><a name="p26006017184830"></a><a name="p26006017184830"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.5.1.4 "><p id="p943645314418"><a name="p943645314418"></a><a name="p943645314418"></a>Specifies whether to enable the action to be triggered by an alarm. The default value is <strong id="b1224551225151640"><a name="b1224551225151640"></a><a name="b1224551225151640"></a>true</strong>.</p>
    <div class="note" id="note11299541449"><a name="note11299541449"></a><a name="note11299541449"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p163612549420"><a name="p163612549420"></a><a name="p163612549420"></a>If <strong id="b209261732153318"><a name="b209261732153318"></a><a name="b209261732153318"></a>alarm_action_enabled</strong> is set to <strong id="b14927832153317"><a name="b14927832153317"></a><a name="b14927832153317"></a>true</strong>, at least one of <strong id="b12927153243319"><a name="b12927153243319"></a><a name="b12927153243319"></a>alarm_actions</strong>, <strong id="b1492810329332"><a name="b1492810329332"></a><a name="b1492810329332"></a>insufficientdata_actions</strong> (deprecated, no need to configure), and <strong id="b11928153213315"><a name="b11928153213315"></a><a name="b11928153213315"></a>ok_actions</strong> cannot be empty.</p>
    <p id="p53917546419"><a name="p53917546419"></a><a name="p53917546419"></a>If <strong id="b14284192333810"><a name="b14284192333810"></a><a name="b14284192333810"></a>alarm_actions</strong>, <strong id="b10285123173819"><a name="b10285123173819"></a><a name="b10285123173819"></a>insufficientdata_actions</strong> (deprecated, no need to configure), and <strong id="b122851123173818"><a name="b122851123173818"></a><a name="b122851123173818"></a>ok_actions</strong> exist at the same time, the values of <strong id="b428611231382"><a name="b428611231382"></a><a name="b428611231382"></a>notificationList</strong> in the three parameters must be the same.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row1681846154417"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.1 "><p id="p712670102310"><a name="p712670102310"></a><a name="p712670102310"></a>alarm_level</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.2 "><p id="p557794642212"><a name="p557794642212"></a><a name="p557794642212"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p579215515141"><a name="p579215515141"></a><a name="p579215515141"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.5.1.4 "><p id="p8577114613229"><a name="p8577114613229"></a><a name="p8577114613229"></a>Specifies the alarm severity. The value can be <strong id="b84235270610925"><a name="b84235270610925"></a><a name="b84235270610925"></a>1</strong>, <strong id="b84235270610928"><a name="b84235270610928"></a><a name="b84235270610928"></a>2</strong>, <strong id="b84235270610931"><a name="b84235270610931"></a><a name="b84235270610931"></a>3</strong> or <strong id="b84235270610934"><a name="b84235270610934"></a><a name="b84235270610934"></a>4</strong>, which indicates critical, major, minor, and informational, respectively.</p>
    </td>
    </tr>
    <tr id="row2110161020462"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.1 "><p id="p27735430184830"><a name="p27735430184830"></a><a name="p27735430184830"></a>alarm_actions</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.2 "><p id="p4949951171213"><a name="p4949951171213"></a><a name="p4949951171213"></a>Mandatory under certain conditions</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p40030552184830"><a name="p40030552184830"></a><a name="p40030552184830"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.5.1.4 "><p id="p21249241184830"><a name="p21249241184830"></a><a name="p21249241184830"></a>Specifies the action triggered by an alarm.</p>
    <p id="p51591767173216"><a name="p51591767173216"></a><a name="p51591767173216"></a>An example structure is as follows:</p>
    <p id="p61672725173216"><a name="p61672725173216"></a><a name="p61672725173216"></a>{</p>
    <p id="p18183618173216"><a name="p18183618173216"></a><a name="p18183618173216"></a>"type": "notification","notificationList": ["urn:smn:region:68438a86d98e427e907e0097b7e35d47:sd"]</p>
    <p id="p29434839173216"><a name="p29434839173216"></a><a name="p29434839173216"></a>}</p>
    <p id="p12410155017487"><a name="p12410155017487"></a><a name="p12410155017487"></a>For details, see <a href="#table359064073020">Table 5</a>.</p>
    </td>
    </tr>
    <tr id="row16804132918465"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.1 "><p id="p40375810184830"><a name="p40375810184830"></a><a name="p40375810184830"></a>ok_actions</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.2 "><p id="p1228810557317"><a name="p1228810557317"></a><a name="p1228810557317"></a>Mandatory under certain conditions</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p27009365184830"><a name="p27009365184830"></a><a name="p27009365184830"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.5.1.4 "><p id="p40274977184830"><a name="p40274977184830"></a><a name="p40274977184830"></a>Specifies the action triggered by clearing an alarm.</p>
    <p id="p26930481184830"><a name="p26930481184830"></a><a name="p26930481184830"></a>Its structure is:</p>
    <p id="p22364435194918"><a name="p22364435194918"></a><a name="p22364435194918"></a>{ "type": "notification","notificationList": ["urn:smn:region:68438a86d98e427e907e0097b7e35d47:sd"] }</p>
    <p id="p3642155304811"><a name="p3642155304811"></a><a name="p3642155304811"></a>For details, see <a href="#table1859144073012">Table 6</a>.</p>
    </td>
    </tr>
    <tr id="row2042813209462"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.2.5.1.1 "><p id="p6521770184830"><a name="p6521770184830"></a><a name="p6521770184830"></a>insufficientdata_actions</p>
    </td>
    <td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.5.1.2 "><p id="p15290541945"><a name="p15290541945"></a><a name="p15290541945"></a>Mandatory under certain conditions</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.3 "><p id="p73211825151513"><a name="p73211825151513"></a><a name="p73211825151513"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="42%" headers="mcps1.2.5.1.4 "><p id="p31855488184830"><a name="p31855488184830"></a><a name="p31855488184830"></a>Specifies the action triggered by the alarm of insufficient data. (This parameter has been discarded. You are advised not to configure this parameter.)</p>
    <p id="p718113231307"><a name="p718113231307"></a><a name="p718113231307"></a>Its structure is:</p>
    <p id="p14181423706"><a name="p14181423706"></a><a name="p14181423706"></a>{ "type": "notification","notificationList": ["urn:smn:region:68438a86d98e427e907e0097b7e35d47:sd"] }</p>
    <p id="p718113231000"><a name="p718113231000"></a><a name="p718113231000"></a>For details, see <a href="#table7354162865816">Table 7</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **metric**  field data structure description

    <a name="table1358724013016"></a>
    <table><thead align="left"><tr id="row9586104013016"><th class="cellrowborder" valign="top" width="15.151515151515152%" id="mcps1.2.5.1.1"><p id="p1858674016307"><a name="p1858674016307"></a><a name="p1858674016307"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.131313131313133%" id="mcps1.2.5.1.2"><p id="p16694057179"><a name="p16694057179"></a><a name="p16694057179"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="10.101010101010102%" id="mcps1.2.5.1.3"><p id="p1958684013306"><a name="p1958684013306"></a><a name="p1958684013306"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="61.61616161616161%" id="mcps1.2.5.1.4"><p id="p16586840173017"><a name="p16586840173017"></a><a name="p16586840173017"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row058694020301"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.1 "><p id="p1458611403306"><a name="p1458611403306"></a><a name="p1458611403306"></a>namespace</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.2 "><p id="p869411512173"><a name="p869411512173"></a><a name="p869411512173"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.101010101010102%" headers="mcps1.2.5.1.3 "><p id="p7428193883310"><a name="p7428193883310"></a><a name="p7428193883310"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.61616161616161%" headers="mcps1.2.5.1.4 "><p id="p12933146104119"><a name="p12933146104119"></a><a name="p12933146104119"></a>Specifies the namespace of a service. For example, see <a href="ecs-metrics.md#en-us_topic_0022067719_section24282572112133">Namespace</a> for ECS namespace.</p>
    <p id="p17148866184830"><a name="p17148866184830"></a><a name="p17148866184830"></a>The value must be in the <strong id="b189629281058"><a name="b189629281058"></a><a name="b189629281058"></a>service.item</strong> format and can contain 3 to 32 characters. <strong id="b20962028956"><a name="b20962028956"></a><a name="b20962028956"></a>service</strong> and <strong id="b89630287510"><a name="b89630287510"></a><a name="b89630287510"></a>item</strong> must be a string that starts with a letter and contains only uppercase letters, lowercase letters, digits, and underscores (_).</p>
    </td>
    </tr>
    <tr id="row35879403303"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.1 "><p id="p75865406307"><a name="p75865406307"></a><a name="p75865406307"></a>dimensions</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.2 "><p id="p7864836151819"><a name="p7864836151819"></a><a name="p7864836151819"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.101010101010102%" headers="mcps1.2.5.1.3 "><p id="p19586164043017"><a name="p19586164043017"></a><a name="p19586164043017"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.61616161616161%" headers="mcps1.2.5.1.4 "><p id="p55861740143019"><a name="p55861740143019"></a><a name="p55861740143019"></a>Specifies the list of the metric dimensions.</p>
    <p id="p9586154053018"><a name="p9586154053018"></a><a name="p9586154053018"></a>For details, see <a href="#table15589124016303">Table 4</a>.</p>
    </td>
    </tr>
    <tr id="row1866844315406"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.1 "><p id="p19274953184830"><a name="p19274953184830"></a><a name="p19274953184830"></a>metric_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.2 "><p id="p17767332184830"><a name="p17767332184830"></a><a name="p17767332184830"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.101010101010102%" headers="mcps1.2.5.1.3 "><p id="p1671144213316"><a name="p1671144213316"></a><a name="p1671144213316"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.61616161616161%" headers="mcps1.2.5.1.4 "><p id="p23711684162943"><a name="p23711684162943"></a><a name="p23711684162943"></a>Specifies the metric name.</p>
    <p id="p1779204015826"><a name="p1779204015826"></a><a name="p1779204015826"></a>The value can be a string of 1 to 64 characters and must start with a letter and contain only uppercase letters, lowercase letters, digits, and underscores (_).</p>
    <p id="p2932950152517"><a name="p2932950152517"></a><a name="p2932950152517"></a>For details, see the metric name queried in <a href="querying-the-metric-list.md">Querying the Metric List</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4** **dimensions**  field data structure description

    <a name="table15589124016303"></a>
    <table><thead align="left"><tr id="row95871840183019"><th class="cellrowborder" valign="top" width="15.151515151515152%" id="mcps1.2.5.1.1"><p id="p155871640123019"><a name="p155871640123019"></a><a name="p155871640123019"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.131313131313133%" id="mcps1.2.5.1.2"><p id="p1941162013172"><a name="p1941162013172"></a><a name="p1941162013172"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="10.101010101010102%" id="mcps1.2.5.1.3"><p id="p758714013304"><a name="p758714013304"></a><a name="p758714013304"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="61.61616161616161%" id="mcps1.2.5.1.4"><p id="p1958714018307"><a name="p1958714018307"></a><a name="p1958714018307"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3588194053014"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.1 "><p id="p9588164019308"><a name="p9588164019308"></a><a name="p9588164019308"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.2 "><p id="p54112020151715"><a name="p54112020151715"></a><a name="p54112020151715"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.101010101010102%" headers="mcps1.2.5.1.3 "><p id="p42461077349"><a name="p42461077349"></a><a name="p42461077349"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.61616161616161%" headers="mcps1.2.5.1.4 "><p id="p132891013125316"><a name="p132891013125316"></a><a name="p132891013125316"></a>Specifies the monitoring dimension. For example, the monitoring dimension of an ECS is <strong id="b134021728135313"><a name="b134021728135313"></a><a name="b134021728135313"></a>instance_id</strong>, which is listed in the <strong id="b2403112814538"><a name="b2403112814538"></a><a name="b2403112814538"></a>key</strong> column in <a href="ecs-metrics.md#en-us_topic_0022067719_section36963297112133">Dimension</a>.</p>
    <p id="p46761848125214"><a name="p46761848125214"></a><a name="p46761848125214"></a>The value can be a string of 1 to 32 characters and must start with a letter and contain only uppercase letters, lowercase letters, digits, underscores (_), and hyphens (-).</p>
    </td>
    </tr>
    <tr id="row6589124015301"><td class="cellrowborder" valign="top" width="15.151515151515152%" headers="mcps1.2.5.1.1 "><p id="p19588184023011"><a name="p19588184023011"></a><a name="p19588184023011"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.131313131313133%" headers="mcps1.2.5.1.2 "><p id="p34111720161711"><a name="p34111720161711"></a><a name="p34111720161711"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.101010101010102%" headers="mcps1.2.5.1.3 "><p id="p62671010193418"><a name="p62671010193418"></a><a name="p62671010193418"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="61.61616161616161%" headers="mcps1.2.5.1.4 "><p id="p11371113251615"><a name="p11371113251615"></a><a name="p11371113251615"></a>Specifies the dimension value, for example, an ECS ID.</p>
    <p id="p1865644545312"><a name="p1865644545312"></a><a name="p1865644545312"></a>The value can be a string of 1 to 256 characters and must start with a letter or a digit and contain only uppercase letters, lowercase letters, digits, underscores (_), and hyphens (-).</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5** **alarm\_actions**  field data structure description

    <a name="table359064073020"></a>
    <table><thead align="left"><tr id="row1258924033017"><th class="cellrowborder" valign="top" width="15%" id="mcps1.2.5.1.1"><p id="p135896407302"><a name="p135896407302"></a><a name="p135896407302"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.2"><p id="p14181533151718"><a name="p14181533151718"></a><a name="p14181533151718"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="10%" id="mcps1.2.5.1.3"><p id="p6589194012309"><a name="p6589194012309"></a><a name="p6589194012309"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="61%" id="mcps1.2.5.1.4"><p id="p7589340173016"><a name="p7589340173016"></a><a name="p7589340173016"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row18590840153020"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="p4589154053013"><a name="p4589154053013"></a><a name="p4589154053013"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p17806823205"><a name="p17806823205"></a><a name="p17806823205"></a>Mandatory under certain conditions</p>
    </td>
    <td class="cellrowborder" valign="top" width="10%" headers="mcps1.2.5.1.3 "><p id="p1258919407308"><a name="p1258919407308"></a><a name="p1258919407308"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.5.1.4 "><div class="p" id="p2059034043019"><a name="p2059034043019"></a><a name="p2059034043019"></a>Specifies the alarm notification type.<a name="ul10590940153014"></a><a name="ul10590940153014"></a><ul id="ul10590940153014"><li><strong id="b9631112722010"><a name="b9631112722010"></a><a name="b9631112722010"></a>notification</strong>: indicates that a notification will be sent to the user.</li><li><strong id="b4268828202018"><a name="b4268828202018"></a><a name="b4268828202018"></a>autoscaling</strong>: indicates that a scaling action will be triggered.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="row1859074017305"><td class="cellrowborder" valign="top" width="15%" headers="mcps1.2.5.1.1 "><p id="p1459014406307"><a name="p1459014406307"></a><a name="p1459014406307"></a>notificationList</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p1580611215205"><a name="p1580611215205"></a><a name="p1580611215205"></a>Mandatory under certain conditions</p>
    </td>
    <td class="cellrowborder" valign="top" width="10%" headers="mcps1.2.5.1.3 "><p id="p158120523224"><a name="p158120523224"></a><a name="p158120523224"></a>Array of strings</p>
    </td>
    <td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.5.1.4 "><p id="p15808149648"><a name="p15808149648"></a><a name="p15808149648"></a>Specifies the list of objects to be notified if the alarm status changes. You can configure a maximum of 5 object IDs. <strong id="b842352706121543"><a name="b842352706121543"></a><a name="b842352706121543"></a>topicUrn</strong> is obtained from SMN and in the format of urn:smn:([a-z]|[A-Z]|[0-9]|\-){1,32}:([a-z]|[A-Z]|[0-9]){32}:([a-z]|[A-Z]|[0-9]|\-|\_){1,256}.</p>
    <p id="p35901840113013"><a name="p35901840113013"></a><a name="p35901840113013"></a>If <strong id="b84235270615753"><a name="b84235270615753"></a><a name="b84235270615753"></a>type</strong> is set to <strong id="b84235270615758"><a name="b84235270615758"></a><a name="b84235270615758"></a>notification</strong>, the value of <strong id="b84235270615816"><a name="b84235270615816"></a><a name="b84235270615816"></a>notificationList</strong> cannot be empty. If <strong id="b84235270615831"><a name="b84235270615831"></a><a name="b84235270615831"></a>type</strong> is set to <strong id="b84235270615835"><a name="b84235270615835"></a><a name="b84235270615835"></a>autoscaling</strong>, the value of <strong id="b2144678271151010"><a name="b2144678271151010"></a><a name="b2144678271151010"></a>notificationList</strong> must be <strong id="b84235270610178"><a name="b84235270610178"></a><a name="b84235270610178"></a>[]</strong>.</p>
    <div class="note" id="note3631127095920"><a name="note3631127095920"></a><a name="note3631127095920"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul13371203915152"></a><a name="ul13371203915152"></a><ul id="ul13371203915152"><li>To make the AS alarm rules take effect, you must bind scaling policies. For details, see the <em id="i782913610133"><a name="i782913610133"></a><a name="i782913610133"></a>Auto Scaling API Reference</em>.</li><li>If <strong id="b1347314547285"><a name="b1347314547285"></a><a name="b1347314547285"></a>alarm_action_enabled</strong> is set to <strong id="b514614118296"><a name="b514614118296"></a><a name="b514614118296"></a>true</strong>, at least one of <strong id="b17848114152917"><a name="b17848114152917"></a><a name="b17848114152917"></a>alarm_actions</strong>, <strong id="b676172019295"><a name="b676172019295"></a><a name="b676172019295"></a>insufficientdata_actions</strong> (deprecated, no need to configure), and <strong id="b9225325132918"><a name="b9225325132918"></a><a name="b9225325132918"></a>ok_actions</strong> cannot be empty.</li><li>If <strong id="b1398452267"><a name="b1398452267"></a><a name="b1398452267"></a>alarm_actions</strong>, <strong id="b61188564"><a name="b61188564"></a><a name="b61188564"></a>insufficientdata_actions</strong> (deprecated, no need to configure), and <strong id="b1396910120"><a name="b1396910120"></a><a name="b1396910120"></a>ok_actions</strong> exist at the same time, the values of <strong id="b452584844"><a name="b452584844"></a><a name="b452584844"></a>notificationList</strong> in the three parameters must be the same.</li><li>The IDs in the list are character strings.</li></ul>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6** **ok\_actions**  field data structure description

    <a name="table1859144073012"></a>
    <table><thead align="left"><tr id="row1159014401302"><th class="cellrowborder" valign="top" width="14.85148514851485%" id="mcps1.2.5.1.1"><p id="p659084020309"><a name="p659084020309"></a><a name="p659084020309"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.861386138613863%" id="mcps1.2.5.1.2"><p id="p8604948181717"><a name="p8604948181717"></a><a name="p8604948181717"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="10.891089108910892%" id="mcps1.2.5.1.3"><p id="p13590144073018"><a name="p13590144073018"></a><a name="p13590144073018"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="60.396039603960396%" id="mcps1.2.5.1.4"><p id="p559024053012"><a name="p559024053012"></a><a name="p559024053012"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1259134016305"><td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.1 "><p id="p1659024013014"><a name="p1659024013014"></a><a name="p1659024013014"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.2 "><p id="p065914542016"><a name="p065914542016"></a><a name="p065914542016"></a>Mandatory under certain conditions</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.2.5.1.3 "><p id="p15911940183012"><a name="p15911940183012"></a><a name="p15911940183012"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.396039603960396%" headers="mcps1.2.5.1.4 "><div class="p" id="p165918407306"><a name="p165918407306"></a><a name="p165918407306"></a>Specifies the notification type when an alarm is triggered.<a name="ul10591184093013"></a><a name="ul10591184093013"></a><ul id="ul10591184093013"><li><strong id="b38811986265"><a name="b38811986265"></a><a name="b38811986265"></a>notification</strong>: indicates that a notification will be sent to the user.</li><li><strong id="b756613962613"><a name="b756613962613"></a><a name="b756613962613"></a>autoscaling</strong>: indicates that a scaling action will be triggered.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="row195911940183017"><td class="cellrowborder" valign="top" width="14.85148514851485%" headers="mcps1.2.5.1.1 "><p id="p115912405301"><a name="p115912405301"></a><a name="p115912405301"></a>notificationList</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.861386138613863%" headers="mcps1.2.5.1.2 "><p id="p19659175192011"><a name="p19659175192011"></a><a name="p19659175192011"></a>Mandatory under certain conditions</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.891089108910892%" headers="mcps1.2.5.1.3 "><p id="p8444165672211"><a name="p8444165672211"></a><a name="p8444165672211"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="60.396039603960396%" headers="mcps1.2.5.1.4 "><p id="p11714622193"><a name="p11714622193"></a><a name="p11714622193"></a>Specifies the list of objects to be notified if the alarm status changes. You can configure a maximum of 5 object IDs. <strong id="b10356113111818"><a name="b10356113111818"></a><a name="b10356113111818"></a>topicUrn</strong> is obtained from SMN and in the format of urn:smn:([a-z]|[A-Z]|[0-9]|\-){1,32}:([a-z]|[A-Z]|[0-9]){32}:([a-z]|[A-Z]|[0-9]|\-|\_){1,256}.</p>
    <div class="note" id="note33010441244"><a name="note33010441244"></a><a name="note33010441244"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p483516202151"><a name="p483516202151"></a><a name="p483516202151"></a>If <strong id="b668051012331"><a name="b668051012331"></a><a name="b668051012331"></a>alarm_action_enabled</strong> is set to <strong id="b2068151010335"><a name="b2068151010335"></a><a name="b2068151010335"></a>true</strong>, at least one of <strong id="b668151016339"><a name="b668151016339"></a><a name="b668151016339"></a>alarm_actions</strong>, <strong id="b1068281073316"><a name="b1068281073316"></a><a name="b1068281073316"></a>insufficientdata_actions</strong> (deprecated, no need to configure), and <strong id="b1868211016336"><a name="b1868211016336"></a><a name="b1868211016336"></a>ok_actions</strong> cannot be empty.</p>
    <p id="p15836820181517"><a name="p15836820181517"></a><a name="p15836820181517"></a>If <strong id="b8943101833819"><a name="b8943101833819"></a><a name="b8943101833819"></a>alarm_actions</strong>, <strong id="b1494421816383"><a name="b1494421816383"></a><a name="b1494421816383"></a>insufficientdata_actions</strong> (deprecated, no need to configure), and <strong id="b594451823814"><a name="b594451823814"></a><a name="b594451823814"></a>ok_actions</strong> exist at the same time, the values of <strong id="b109452018143819"><a name="b109452018143819"></a><a name="b109452018143819"></a>notificationList</strong> in the three parameters must be the same.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  7** **insufficientdata\_actions**  field data structure description

    <a name="table7354162865816"></a>
    <table><thead align="left"><tr id="row123555289589"><th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.1"><p id="p1735582811587"><a name="p1735582811587"></a><a name="p1735582811587"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.2"><p id="p1746122111818"><a name="p1746122111818"></a><a name="p1746122111818"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="11%" id="mcps1.2.5.1.3"><p id="p7355172815810"><a name="p7355172815810"></a><a name="p7355172815810"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="61%" id="mcps1.2.5.1.4"><p id="p1355128195812"><a name="p1355128195812"></a><a name="p1355128195812"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row235552855814"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="p73554280581"><a name="p73554280581"></a><a name="p73554280581"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p775981016203"><a name="p775981016203"></a><a name="p775981016203"></a>Mandatory under certain conditions</p>
    </td>
    <td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.3 "><p id="p1992732116346"><a name="p1992732116346"></a><a name="p1992732116346"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.5.1.4 "><div class="p" id="p835592845817"><a name="p835592845817"></a><a name="p835592845817"></a>Specifies the notification type when an alarm is triggered.<a name="ul143551028185815"></a><a name="ul143551028185815"></a><ul id="ul143551028185815"><li><strong id="b172771720132615"><a name="b172771720132615"></a><a name="b172771720132615"></a>notification</strong>: indicates that a notification will be sent to the user.</li><li><strong id="b1729112342618"><a name="b1729112342618"></a><a name="b1729112342618"></a>autoscaling</strong>: indicates that a scaling action will be triggered.</li></ul>
    </div>
    </td>
    </tr>
    <tr id="row1356122815818"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="p183562286585"><a name="p183562286585"></a><a name="p183562286585"></a>notificationList</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p19760310152010"><a name="p19760310152010"></a><a name="p19760310152010"></a>Mandatory under certain conditions</p>
    </td>
    <td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.3 "><p id="p8518102517168"><a name="p8518102517168"></a><a name="p8518102517168"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.5.1.4 "><p id="p134411927598"><a name="p134411927598"></a><a name="p134411927598"></a>Specifies the list of objects to be notified if the alarm status changes. At most 5 objects are supported. The value of <strong id="b1152944122815"><a name="b1152944122815"></a><a name="b1152944122815"></a>topicUrn</strong> can be obtained from SMN in the following format: urn:smn:([a-z]|[A-Z]|[0-9]|\-){1,32}:([a-z]|[A-Z]|[0-9]){32}:([a-z]|[A-Z]|[0-9]|\-|\_){1,256}.</p>
    <div class="note" id="note1535612865817"><a name="note1535612865817"></a><a name="note1535612865817"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul10380152715262"></a><a name="ul10380152715262"></a><ul id="ul10380152715262"><li>If <strong id="b1465699217"><a name="b1465699217"></a><a name="b1465699217"></a>alarm_action_enabled</strong> is set to <strong id="b453557004"><a name="b453557004"></a><a name="b453557004"></a>true</strong>, at least one of <strong id="b1423540794"><a name="b1423540794"></a><a name="b1423540794"></a>alarm_actions</strong>, <strong id="b2056537172"><a name="b2056537172"></a><a name="b2056537172"></a>insufficientdata_actions</strong> (deprecated, no need to configure), and <strong id="b211597185"><a name="b211597185"></a><a name="b211597185"></a>ok_actions</strong> cannot be empty.</li><li>If <strong id="b15462397814"><a name="b15462397814"></a><a name="b15462397814"></a>alarm_actions</strong>, <strong id="b14471639581"><a name="b14471639581"></a><a name="b14471639581"></a>insufficientdata_actions</strong> (deprecated, no need to configure), and <strong id="b24714392817"><a name="b24714392817"></a><a name="b24714392817"></a>ok_actions</strong> exist at the same time, the values of <strong id="b184818391583"><a name="b184818391583"></a><a name="b184818391583"></a>notificationList</strong> in the three parameters must be the same.</li><li>The IDs in the list are character strings.</li></ul>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  8** **condition**  field data structure description

    <a name="table159417407300"></a>
    <table><thead align="left"><tr id="row175923401303"><th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.1"><p id="p8592184020306"><a name="p8592184020306"></a><a name="p8592184020306"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.2"><p id="p4552182712016"><a name="p4552182712016"></a><a name="p4552182712016"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="11%" id="mcps1.2.5.1.3"><p id="p759220403308"><a name="p759220403308"></a><a name="p759220403308"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="61%" id="mcps1.2.5.1.4"><p id="p1592124010305"><a name="p1592124010305"></a><a name="p1592124010305"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row859212406308"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="p14592164013013"><a name="p14592164013013"></a><a name="p14592164013013"></a>period</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p61281211184830"><a name="p61281211184830"></a><a name="p61281211184830"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.3 "><p id="p1592540163016"><a name="p1592540163016"></a><a name="p1592540163016"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.5.1.4 "><p id="p59336618163033"><a name="p59336618163033"></a><a name="p59336618163033"></a>Specifies the alarm checking period in seconds.</p>
    <p id="p3506996615826"><a name="p3506996615826"></a><a name="p3506996615826"></a>The value can be <strong id="b84235270614561"><a name="b84235270614561"></a><a name="b84235270614561"></a>1</strong>, <strong id="b84235270614566"><a name="b84235270614566"></a><a name="b84235270614566"></a>300</strong>, <strong id="b842352706145610"><a name="b842352706145610"></a><a name="b842352706145610"></a>1200</strong>, <strong id="b842352706145615"><a name="b842352706145615"></a><a name="b842352706145615"></a>3600</strong>, <strong id="b842352706145619"><a name="b842352706145619"></a><a name="b842352706145619"></a>14400</strong>, and <strong id="b842352706145623"><a name="b842352706145623"></a><a name="b842352706145623"></a>86400</strong>.</p>
    <div class="note" id="note24513792172954"><a name="note24513792172954"></a><a name="note24513792172954"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul445821775119"></a><a name="ul445821775119"></a><ul id="ul445821775119"><li>If <strong id="b842352706145730"><a name="b842352706145730"></a><a name="b842352706145730"></a>period</strong> is set to <strong id="b842352706145723"><a name="b842352706145723"></a><a name="b842352706145723"></a>1</strong>, the raw monitoring data is used to determine whether to generate an alarm.</li></ul>
    </div></div>
    </td>
    </tr>
    <tr id="row12593134013307"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="p75931140123014"><a name="p75931140123014"></a><a name="p75931140123014"></a>filter</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p41234478184830"><a name="p41234478184830"></a><a name="p41234478184830"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.3 "><p id="p18409122743418"><a name="p18409122743418"></a><a name="p18409122743418"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.5.1.4 "><p id="p48422044163043"><a name="p48422044163043"></a><a name="p48422044163043"></a>Specifies the data rollup method.</p>
    <p id="p3113774115826"><a name="p3113774115826"></a><a name="p3113774115826"></a>The value can be <strong id="b33978976115232"><a name="b33978976115232"></a><a name="b33978976115232"></a>Max.</strong>, <strong id="b45429468115236"><a name="b45429468115236"></a><a name="b45429468115236"></a>Min.</strong>, <strong id="b49903148115244"><a name="b49903148115244"></a><a name="b49903148115244"></a>Avg.</strong>, <strong id="b6359880115251"><a name="b6359880115251"></a><a name="b6359880115251"></a>Sum</strong>, or <strong id="b42328221115255"><a name="b42328221115255"></a><a name="b42328221115255"></a>Variance</strong>.</p>
    </td>
    </tr>
    <tr id="row11593174014301"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="p15593194018309"><a name="p15593194018309"></a><a name="p15593194018309"></a>comparison_operator</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p54782444184830"><a name="p54782444184830"></a><a name="p54782444184830"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.3 "><p id="p7843029113415"><a name="p7843029113415"></a><a name="p7843029113415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.5.1.4 "><p id="p12749146163055"><a name="p12749146163055"></a><a name="p12749146163055"></a>Specifies the operator.</p>
    <p id="p4278497915826"><a name="p4278497915826"></a><a name="p4278497915826"></a>The value can be <strong id="b2449208162820"><a name="b2449208162820"></a><a name="b2449208162820"></a>&gt;</strong>, <strong id="b22042877162820"><a name="b22042877162820"></a><a name="b22042877162820"></a>=</strong>, <strong id="b64168165162820"><a name="b64168165162820"></a><a name="b64168165162820"></a>&lt;</strong>, <strong id="b40642579162820"><a name="b40642579162820"></a><a name="b40642579162820"></a>≥</strong>, or <strong id="b30238895162820"><a name="b30238895162820"></a><a name="b30238895162820"></a>≤</strong>.</p>
    </td>
    </tr>
    <tr id="row1593040153018"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="p759394033014"><a name="p759394033014"></a><a name="p759394033014"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p16182070184830"><a name="p16182070184830"></a><a name="p16182070184830"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.3 "><p id="p1165182154518"><a name="p1165182154518"></a><a name="p1165182154518"></a>Integer or Float</p>
    </td>
    <td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.5.1.4 "><p id="p3139888416313"><a name="p3139888416313"></a><a name="p3139888416313"></a>Specifies the alarm threshold.</p>
    <p id="p6664421215826"><a name="p6664421215826"></a><a name="p6664421215826"></a>The value ranges from <strong id="b84235270615612"><a name="b84235270615612"></a><a name="b84235270615612"></a>0</strong> to <strong id="b84235270615617"><a name="b84235270615617"></a><a name="b84235270615617"></a>Number. MAX_VALUE (1.7976931348623157e+108)</strong>.</p>
    <p id="p15745192055314"><a name="p15745192055314"></a><a name="p15745192055314"></a>For details about the thresholds, see the value range of each metric in the appendix. For example, the value of <strong id="b842352706121214"><a name="b842352706121214"></a><a name="b842352706121214"></a>cpu_util</strong> in <a href="ecs-metrics.md#en-us_topic_0022067719_section52364133112133">Metrics</a> can be 80.</p>
    </td>
    </tr>
    <tr id="row25941440173013"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="p105931440173016"><a name="p105931440173016"></a><a name="p105931440173016"></a>unit</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p12554645184830"><a name="p12554645184830"></a><a name="p12554645184830"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.3 "><p id="p1149973211349"><a name="p1149973211349"></a><a name="p1149973211349"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.5.1.4 "><p id="p28452702184830"><a name="p28452702184830"></a><a name="p28452702184830"></a>Specifies the data unit. The value contains a maximum of 32 characters.</p>
    </td>
    </tr>
    <tr id="row35945402309"><td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.1 "><p id="p20594124010304"><a name="p20594124010304"></a><a name="p20594124010304"></a>count</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p33235482184830"><a name="p33235482184830"></a><a name="p33235482184830"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="11%" headers="mcps1.2.5.1.3 "><p id="p1533910445344"><a name="p1533910445344"></a><a name="p1533910445344"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="61%" headers="mcps1.2.5.1.4 "><p id="p15204447163111"><a name="p15204447163111"></a><a name="p15204447163111"></a>Specifies the number of consecutive occurrence times.</p>
    <p id="p457803915826"><a name="p457803915826"></a><a name="p457803915826"></a>The value ranges from <strong id="b84235270615719"><a name="b84235270615719"></a><a name="b84235270615719"></a>1</strong> to <strong id="b84235270615722"><a name="b84235270615722"></a><a name="b84235270615722"></a>5</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    {
        "alarm_name": "alarm-rp0E", 
        "alarm_description": "", 
        "metric": {
            "namespace": "SYS.ECS", 
            "dimensions": [
                {
                    "name": "instance_id", 
                    "value": "33328f02-3814-422e-b688-bfdba93d4051"
                }
            ], 
            "metric_name": "network_outgoing_bytes_rate_inband"
        }, 
        "condition": {
            "period": 300, 
            "filter": "average", 
            "comparison_operator": ">=", 
            "value": 6, 
            "unit": "B/s", 
            "count": 1        
       }, 
        "alarm_enabled": true, 
        "alarm_action_enabled": true, 
        "alarm_level": 2,
        "alarm_actions": [
            {
                "type": "notification", 
                "notificationList": ["urn:smn:region:68438a86d98e427e907e0097b7e35d48:sd"]
            }
        ], 
        "ok_actions": [
            {
                "type": "notification", 
                "notificationList": ["urn:smn:region:68438a86d98e427e907e0097b7e35d48:sd"]
            }
        ],
        "insufficientdata_actions": [
            {
                "type": "notification", 
                "notificationList": ["urn:smn:region:68438a86d98e427e907e0097b7e35d48:sd"]
            }
        ]
    }
    ```


## Response<a name="section41088852184830"></a>

-   Response parameters

    **Table  9**  Response parameters

    <a name="table7651809184830"></a>
    <table><thead align="left"><tr id="row11265298184830"><th class="cellrowborder" valign="top" width="16.919999999999998%" id="mcps1.2.4.1.1"><p id="p40073906184830"><a name="p40073906184830"></a><a name="p40073906184830"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="13.04%" id="mcps1.2.4.1.2"><p id="p59478015184830"><a name="p59478015184830"></a><a name="p59478015184830"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="70.04%" id="mcps1.2.4.1.3"><p id="p52989949184830"><a name="p52989949184830"></a><a name="p52989949184830"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row64327487184830"><td class="cellrowborder" valign="top" width="16.919999999999998%" headers="mcps1.2.4.1.1 "><p id="p43143982184830"><a name="p43143982184830"></a><a name="p43143982184830"></a>alarm_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="13.04%" headers="mcps1.2.4.1.2 "><p id="p15981046115616"><a name="p15981046115616"></a><a name="p15981046115616"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="70.04%" headers="mcps1.2.4.1.3 "><p id="p66697365184830"><a name="p66697365184830"></a><a name="p66697365184830"></a>Specifies the alarm rule ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    { 
        "alarm_id":"al1450321795427dR8p5mQBo"
    }
    ```


## Returned Values<a name="section55124147184830"></a>

-   Normal

    201

-   Abnormal

    <a name="table65203824184830"></a>
    <table><thead align="left"><tr id="row50887607184830"><th class="cellrowborder" valign="top" width="33.650000000000006%" id="mcps1.1.3.1.1"><p id="p28255530184830"><a name="p28255530184830"></a><a name="p28255530184830"></a>Returned Values</p>
    </th>
    <th class="cellrowborder" valign="top" width="66.35%" id="mcps1.1.3.1.2"><p id="p6996573184830"><a name="p6996573184830"></a><a name="p6996573184830"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row29851512184830"><td class="cellrowborder" valign="top" width="33.650000000000006%" headers="mcps1.1.3.1.1 "><p id="p2053412184830"><a name="p2053412184830"></a><a name="p2053412184830"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.35%" headers="mcps1.1.3.1.2 "><p id="p32108680184830"><a name="p32108680184830"></a><a name="p32108680184830"></a>Request error</p>
    </td>
    </tr>
    <tr id="row20542671184830"><td class="cellrowborder" valign="top" width="33.650000000000006%" headers="mcps1.1.3.1.1 "><p id="p53343675184830"><a name="p53343675184830"></a><a name="p53343675184830"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.35%" headers="mcps1.1.3.1.2 "><p id="p25870452184830"><a name="p25870452184830"></a><a name="p25870452184830"></a>The authentication information is not provided or is incorrect.</p>
    </td>
    </tr>
    <tr id="row31507481184830"><td class="cellrowborder" valign="top" width="33.650000000000006%" headers="mcps1.1.3.1.1 "><p id="p1969135184830"><a name="p1969135184830"></a><a name="p1969135184830"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.35%" headers="mcps1.1.3.1.2 "><p id="p25282246184830"><a name="p25282246184830"></a><a name="p25282246184830"></a>You are forbidden to access the page requested.</p>
    </td>
    </tr>
    <tr id="row26213625184830"><td class="cellrowborder" valign="top" width="33.650000000000006%" headers="mcps1.1.3.1.1 "><p id="p42928884184830"><a name="p42928884184830"></a><a name="p42928884184830"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.35%" headers="mcps1.1.3.1.2 "><p id="p54687555184830"><a name="p54687555184830"></a><a name="p54687555184830"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row22425950184830"><td class="cellrowborder" valign="top" width="33.650000000000006%" headers="mcps1.1.3.1.1 "><p id="p4562631184830"><a name="p4562631184830"></a><a name="p4562631184830"></a>429 Too Many Requests</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.35%" headers="mcps1.1.3.1.2 "><p id="p34028792184830"><a name="p34028792184830"></a><a name="p34028792184830"></a>Concurrent requests are excessive.</p>
    </td>
    </tr>
    <tr id="row37823675184830"><td class="cellrowborder" valign="top" width="33.650000000000006%" headers="mcps1.1.3.1.1 "><p id="p43818860184830"><a name="p43818860184830"></a><a name="p43818860184830"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.35%" headers="mcps1.1.3.1.2 "><p id="p59666810184830"><a name="p59666810184830"></a><a name="p59666810184830"></a>Failed to complete the request because of an internal service error.</p>
    </td>
    </tr>
    <tr id="row130383184830"><td class="cellrowborder" valign="top" width="33.650000000000006%" headers="mcps1.1.3.1.1 "><p id="p10561075184830"><a name="p10561075184830"></a><a name="p10561075184830"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="66.35%" headers="mcps1.1.3.1.2 "><p id="p50140710184830"><a name="p50140710184830"></a><a name="p50140710184830"></a>The service is currently unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Code<a name="section1618385104615"></a>

For details, see  [Error Codes](error-codes.md).


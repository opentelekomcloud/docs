# Querying a Single Backup<a name="EN-US_TOPIC_0059304234"></a>

## Function<a name="section37966355"></a>

This API is used to query the backup of a specific ID.

## URI<a name="section6152882"></a>

-   URI format

    GET https://\{endpoint\}/v1/\{project\_id\}/checkpoint\_items/\{checkpoint\_item\_id\}

-   Parameter description

    **Table  1**  Parameter description

    <a name="table53605075"></a>
    <table><thead align="left"><tr id="row53075243"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p45356064"><a name="p45356064"></a><a name="p45356064"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p49962569"><a name="p49962569"></a><a name="p49962569"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p20436323"><a name="p20436323"></a><a name="p20436323"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p44729494"><a name="p44729494"></a><a name="p44729494"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row49612778"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p59212070"><a name="p59212070"></a><a name="p59212070"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p31448326"><a name="p31448326"></a><a name="p31448326"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p64286450"><a name="p64286450"></a><a name="p64286450"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p65779720"><a name="p65779720"></a><a name="p65779720"></a>Project ID</p>
    </td>
    </tr>
    <tr id="row22835571"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p37741982"><a name="p37741982"></a><a name="p37741982"></a>checkpoint_item_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p37201714"><a name="p37201714"></a><a name="p37201714"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p60548821"><a name="p60548821"></a><a name="p60548821"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p5507506"><a name="p5507506"></a><a name="p5507506"></a>Backup ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section55375943"></a>

-   Parameter description

    None


-   Example request

    ```
    GET https://{endpoint}/v1/{project_id}/checkpoint_items/{checkpoint_item_id}
    ```


## Response<a name="section28621443"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table35300871"></a>
    <table><thead align="left"><tr id="row22790824"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p108841358145215"><a name="p108841358145215"></a><a name="p108841358145215"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p98991958185213"><a name="p98991958185213"></a><a name="p98991958185213"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p14899458165215"><a name="p14899458165215"></a><a name="p14899458165215"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row20070764"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p15119192"><a name="p15119192"></a><a name="p15119192"></a>checkpoint_item</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p10120705"><a name="p10120705"></a><a name="p10120705"></a>checkpoint_item</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p14470799"><a name="p14470799"></a><a name="p14470799"></a>For details, see <a href="#table31284045">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **checkpoint\_item**

    **Table  3**  Parameter description of field  **checkpoint\_item**

    <a name="table31284045"></a>
    <table><thead align="left"><tr id="row64126600"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p358732175317"><a name="p358732175317"></a><a name="p358732175317"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p17602112135318"><a name="p17602112135318"></a><a name="p17602112135318"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p3602102165316"><a name="p3602102165316"></a><a name="p3602102165316"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row26325568"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p51996302"><a name="p51996302"></a><a name="p51996302"></a>checkpoint_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p33385823"><a name="p33385823"></a><a name="p33385823"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p19897138"><a name="p19897138"></a><a name="p19897138"></a>Backup record ID</p>
    </td>
    </tr>
    <tr id="row44856519"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p9499412"><a name="p9499412"></a><a name="p9499412"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p48618095"><a name="p48618095"></a><a name="p48618095"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p45751629"><a name="p45751629"></a><a name="p45751629"></a>Creation time, for example, <strong id="b344382912146"><a name="b344382912146"></a><a name="b344382912146"></a>2017-04-18T01:21:52.701973</strong></p>
    </td>
    </tr>
    <tr id="row9111485"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p66941716"><a name="p66941716"></a><a name="p66941716"></a>extend_info</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p44192877"><a name="p44192877"></a><a name="p44192877"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p22853313"><a name="p22853313"></a><a name="p22853313"></a>Extension information</p>
    </td>
    </tr>
    <tr id="row4353229"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p17067270"><a name="p17067270"></a><a name="p17067270"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p40779379"><a name="p40779379"></a><a name="p40779379"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p14795382"><a name="p14795382"></a><a name="p14795382"></a>Backup ID</p>
    </td>
    </tr>
    <tr id="row66049575"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p48415341"><a name="p48415341"></a><a name="p48415341"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p26805152"><a name="p26805152"></a><a name="p26805152"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p23733724"><a name="p23733724"></a><a name="p23733724"></a>Backup name</p>
    </td>
    </tr>
    <tr id="row12276932"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p54907410"><a name="p54907410"></a><a name="p54907410"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p7135583"><a name="p7135583"></a><a name="p7135583"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p41111342"><a name="p41111342"></a><a name="p41111342"></a>ID of the object to be backed up</p>
    </td>
    </tr>
    <tr id="row34457765"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p39615556"><a name="p39615556"></a><a name="p39615556"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p5034912"><a name="p5034912"></a><a name="p5034912"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p5174700"><a name="p5174700"></a><a name="p5174700"></a>Backup status. Possible values are <strong id="b842352706203643"><a name="b842352706203643"></a><a name="b842352706203643"></a>waiting_protect</strong>, <strong id="b842352706203651"><a name="b842352706203651"></a><a name="b842352706203651"></a>protecting</strong>, <strong id="b842352706203654"><a name="b842352706203654"></a><a name="b842352706203654"></a>available</strong>, <strong id="b842352706203659"><a name="b842352706203659"></a><a name="b842352706203659"></a>waiting_restore</strong>, <strong id="b84235270620372"><a name="b84235270620372"></a><a name="b84235270620372"></a>restoring</strong>, <strong id="b84235270620378"><a name="b84235270620378"></a><a name="b84235270620378"></a>error</strong>, <strong id="b842352706203714"><a name="b842352706203714"></a><a name="b842352706203714"></a>waiting_delete</strong>, <strong id="b842352706203327"><a name="b842352706203327"></a><a name="b842352706203327"></a>deleting</strong>, and <strong id="b510230562203250"><a name="b510230562203250"></a><a name="b510230562203250"></a>deleted</strong>.</p>
    <p id="p199923219255"><a name="p199923219255"></a><a name="p199923219255"></a>Enum:[ waiting_protect, protecting, available, waiting_restore, restoring, error, waiting_delete, deleting,deleted]</p>
    </td>
    </tr>
    <tr id="row16497581"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p61235723"><a name="p61235723"></a><a name="p61235723"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p53922812"><a name="p53922812"></a><a name="p53922812"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p5671647"><a name="p5671647"></a><a name="p5671647"></a>Modification time, for example, <strong id="b3787930121412"><a name="b3787930121412"></a><a name="b3787930121412"></a>2017-04-18T01:21:52.701973</strong></p>
    </td>
    </tr>
    <tr id="row51044828"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p40990393"><a name="p40990393"></a><a name="p40990393"></a>backup_data</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p32752180"><a name="p32752180"></a><a name="p32752180"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p35680930"><a name="p35680930"></a><a name="p35680930"></a>VM metadata</p>
    </td>
    </tr>
    <tr id="row7523923353"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p2052319231152"><a name="p2052319231152"></a><a name="p2052319231152"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p25231123550"><a name="p25231123550"></a><a name="p25231123550"></a>string</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p1452312318520"><a name="p1452312318520"></a><a name="p1452312318520"></a>Backup description</p>
    </td>
    </tr>
    <tr id="row1483112381346"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p583173853411"><a name="p583173853411"></a><a name="p583173853411"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p12831193833415"><a name="p12831193833415"></a><a name="p12831193833415"></a>List&lt;resource_tag&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p448733435210"><a name="p448733435210"></a><a name="p448733435210"></a>List of backup tags</p>
    <p id="p7831173883410"><a name="p7831173883410"></a><a name="p7831173883410"></a>Keys in the tag list must be unique.</p>
    </td>
    </tr>
    <tr id="row186965413101"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p1430747161018"><a name="p1430747161018"></a><a name="p1430747161018"></a>resource_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p133205712103"><a name="p133205712103"></a><a name="p133205712103"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p83271175104"><a name="p83271175104"></a><a name="p83271175104"></a>Type of the backup object</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **extend\_info**

    **Table  4**  Parameter description of field  **extend\_info**

    <a name="table4474257"></a>
    <table><thead align="left"><tr id="row25374974"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p3337529105312"><a name="p3337529105312"></a><a name="p3337529105312"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p0352142925311"><a name="p0352142925311"></a><a name="p0352142925311"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p8368429165320"><a name="p8368429165320"></a><a name="p8368429165320"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row35881396"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p20711946"><a name="p20711946"></a><a name="p20711946"></a>auto_trigger</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p62743133"><a name="p62743133"></a><a name="p62743133"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p49029033"><a name="p49029033"></a><a name="p49029033"></a>Whether automatic trigger is enabled</p>
    </td>
    </tr>
    <tr id="row38608121"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p40250071"><a name="p40250071"></a><a name="p40250071"></a>average_speed</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p7336516"><a name="p7336516"></a><a name="p7336516"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p57386915"><a name="p57386915"></a><a name="p57386915"></a>Average rate. The unit is kb/s</p>
    </td>
    </tr>
    <tr id="row46720194"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p26239345"><a name="p26239345"></a><a name="p26239345"></a>copy_from</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p22108653"><a name="p22108653"></a><a name="p22108653"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p45970441"><a name="p45970441"></a><a name="p45970441"></a>The destination region of a backup replication. The default value is empty.</p>
    </td>
    </tr>
    <tr id="row11080792"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p5700168"><a name="p5700168"></a><a name="p5700168"></a>copy_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p19168703"><a name="p19168703"></a><a name="p19168703"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p112911849103111"><a name="p112911849103111"></a><a name="p112911849103111"></a>Backup replication status. The default value is <strong id="b75876111958"><a name="b75876111958"></a><a name="b75876111958"></a>na</strong>.</p>
    <p id="p173113381512"><a name="p173113381512"></a><a name="p173113381512"></a>Possible values are <strong id="b17503147113010"><a name="b17503147113010"></a><a name="b17503147113010"></a>na</strong>, <strong id="b18503174783014"><a name="b18503174783014"></a><a name="b18503174783014"></a>waiting_copy</strong>, <strong id="b17504114716304"><a name="b17504114716304"></a><a name="b17504114716304"></a>copying</strong>, <strong id="b15504184783012"><a name="b15504184783012"></a><a name="b15504184783012"></a>success</strong>, or <strong id="b850564713304"><a name="b850564713304"></a><a name="b850564713304"></a>fail</strong>.</p>
    </td>
    </tr>
    <tr id="row40063217"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p23895134"><a name="p23895134"></a><a name="p23895134"></a>fail_code</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p9669625"><a name="p9669625"></a><a name="p9669625"></a>fail_code</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p45042167"><a name="p45042167"></a><a name="p45042167"></a>Error code</p>
    </td>
    </tr>
    <tr id="row2726327"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p19505966"><a name="p19505966"></a><a name="p19505966"></a>fail_op</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p2039495"><a name="p2039495"></a><a name="p2039495"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p30981435"><a name="p30981435"></a><a name="p30981435"></a>Type of the failed operation</p>
    <p id="p10397463"><a name="p10397463"></a><a name="p10397463"></a>Enum: [backup, restore, delete]</p>
    </td>
    </tr>
    <tr id="row26468307"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p63558136"><a name="p63558136"></a><a name="p63558136"></a>fail_reason</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p57560327"><a name="p57560327"></a><a name="p57560327"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p31874881"><a name="p31874881"></a><a name="p31874881"></a>Description of the failure cause</p>
    </td>
    </tr>
    <tr id="row18438475"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p17121511"><a name="p17121511"></a><a name="p17121511"></a>image_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p61107184"><a name="p61107184"></a><a name="p61107184"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p50734894"><a name="p50734894"></a><a name="p50734894"></a>Backup type. For example, <strong id="b916517281253"><a name="b916517281253"></a><a name="b916517281253"></a>backup</strong></p>
    </td>
    </tr>
    <tr id="row53960863"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p8753788"><a name="p8753788"></a><a name="p8753788"></a>incremental</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p55529076"><a name="p55529076"></a><a name="p55529076"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p1561311"><a name="p1561311"></a><a name="p1561311"></a>Whether the backup is an enhanced backup</p>
    </td>
    </tr>
    <tr id="row14051800"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p64454033"><a name="p64454033"></a><a name="p64454033"></a>progress</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p29959179"><a name="p29959179"></a><a name="p29959179"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p10774429"><a name="p10774429"></a><a name="p10774429"></a>Backup progress. The value is an integer ranging from 0 to 100.</p>
    </td>
    </tr>
    <tr id="row29860999"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p2821893"><a name="p2821893"></a><a name="p2821893"></a>resource_az</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p59506486"><a name="p59506486"></a><a name="p59506486"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p55296057"><a name="p55296057"></a><a name="p55296057"></a>AZ to which the backup resource belongs</p>
    </td>
    </tr>
    <tr id="row27902470"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p45507587"><a name="p45507587"></a><a name="p45507587"></a>resource_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p7944126"><a name="p7944126"></a><a name="p7944126"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p39494476"><a name="p39494476"></a><a name="p39494476"></a>Backup object name</p>
    </td>
    </tr>
    <tr id="row611222610436"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p149812204222"><a name="p149812204222"></a><a name="p149812204222"></a>resource_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p998142020221"><a name="p998142020221"></a><a name="p998142020221"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p09822022216"><a name="p09822022216"></a><a name="p09822022216"></a>Type of the backup object. For example, <strong id="b169851814616"><a name="b169851814616"></a><a name="b169851814616"></a>OS::Nova::Server</strong></p>
    </td>
    </tr>
    <tr id="row19905972"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p1771067"><a name="p1771067"></a><a name="p1771067"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p10137332"><a name="p10137332"></a><a name="p10137332"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p15817592"><a name="p15817592"></a><a name="p15817592"></a>Backup capacity. The unit is MB.</p>
    </td>
    </tr>
    <tr id="row8140604"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p55409189"><a name="p55409189"></a><a name="p55409189"></a>space_saving_ratio</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p10978802"><a name="p10978802"></a><a name="p10978802"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p16867749"><a name="p16867749"></a><a name="p16867749"></a>Space saving rate</p>
    </td>
    </tr>
    <tr id="row17592014"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p15667012"><a name="p15667012"></a><a name="p15667012"></a>volume_backups</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p47601111"><a name="p47601111"></a><a name="p47601111"></a>List&lt;volume_backup&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p30484803"><a name="p30484803"></a><a name="p30484803"></a>Volume backup list</p>
    </td>
    </tr>
    <tr id="row5927779"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p10388065"><a name="p10388065"></a><a name="p10388065"></a>finished_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p40598030"><a name="p40598030"></a><a name="p40598030"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p106125"><a name="p106125"></a><a name="p106125"></a>Backup completion time, for example, <strong id="b866388191513"><a name="b866388191513"></a><a name="b866388191513"></a>2017-04-18T01:21:52.701973</strong></p>
    </td>
    </tr>
    <tr id="row1878614674719"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p14691120181216"><a name="p14691120181216"></a><a name="p14691120181216"></a>supported_restore_mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p204691920121214"><a name="p204691920121214"></a><a name="p204691920121214"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p18728201715"><a name="p18728201715"></a><a name="p18728201715"></a>Restoration mode. Possible values are <strong id="b46774915241"><a name="b46774915241"></a><a name="b46774915241"></a>na</strong>, <strong id="b8823182419241"><a name="b8823182419241"></a><a name="b8823182419241"></a>snapshot</strong>, and <strong id="b667817919244"><a name="b667817919244"></a><a name="b667817919244"></a>backup</strong>.</p>
    <p id="p8166816173"><a name="p8166816173"></a><a name="p8166816173"></a><strong id="b84235270610831"><a name="b84235270610831"></a><a name="b84235270610831"></a>backup</strong>: Data is restored from backups of the EVS disks of the server.</p>
    <p id="p11211554424"><a name="p11211554424"></a><a name="p11211554424"></a><strong id="b84235270610912"><a name="b84235270610912"></a><a name="b84235270610912"></a>na</strong>: Restoration is not supported.</p>
    </td>
    </tr>
    <tr id="row227118084815"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p76063254014"><a name="p76063254014"></a><a name="p76063254014"></a>os_images_data</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p860103213408"><a name="p860103213408"></a><a name="p860103213408"></a>List&lt;image_data&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p18603325403"><a name="p18603325403"></a><a name="p18603325403"></a>Image data. This parameter has a value if an image has been created for the VM.</p>
    </td>
    </tr>
    <tr id="row14392013145013"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p19986193041010"><a name="p19986193041010"></a><a name="p19986193041010"></a>support_lld</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p898783012102"><a name="p898783012102"></a><a name="p898783012102"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p14987330181013"><a name="p14987330181013"></a><a name="p14987330181013"></a>Whether to allow lazyloading for fast restoration</p>
    </td>
    </tr>
    <tr id="row8909163111020"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p189025313106"><a name="p189025313106"></a><a name="p189025313106"></a>taskid</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p11902123114103"><a name="p11902123114103"></a><a name="p11902123114103"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p690212311100"><a name="p690212311100"></a><a name="p690212311100"></a>Job ID</p>
    </td>
    </tr>
    <tr id="row59081931161020"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p990283111013"><a name="p990283111013"></a><a name="p990283111013"></a>hypervisor_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p11902163113108"><a name="p11902163113108"></a><a name="p11902163113108"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p17903133181016"><a name="p17903133181016"></a><a name="p17903133181016"></a>Virtualization type</p>
    <p id="p78814320472"><a name="p78814320472"></a><a name="p78814320472"></a>The value is fixed at <strong id="b132411816133111"><a name="b132411816133111"></a><a name="b132411816133111"></a>QEMU</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **backup\_data**

    **Table  5**  Parameter description of field  **backup\_data**

    <a name="table8596189"></a>
    <table><thead align="left"><tr id="row56714947"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p8227122710547"><a name="p8227122710547"></a><a name="p8227122710547"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p152422278549"><a name="p152422278549"></a><a name="p152422278549"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p6242152712542"><a name="p6242152712542"></a><a name="p6242152712542"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row63047142"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p6544886"><a name="p6544886"></a><a name="p6544886"></a>__openstack_region_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p58434603"><a name="p58434603"></a><a name="p58434603"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p35582368"><a name="p35582368"></a><a name="p35582368"></a>Name of the AZ where the server is located. If this parameter is left blank, such information about the server has not been obtained.</p>
    </td>
    </tr>
    <tr id="row51805857"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p35524928"><a name="p35524928"></a><a name="p35524928"></a>cloudservicetype</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p9973792"><a name="p9973792"></a><a name="p9973792"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p2570800"><a name="p2570800"></a><a name="p2570800"></a>Server type</p>
    <p id="p16315123095611"><a name="p16315123095611"></a><a name="p16315123095611"></a>The value is fixed at <strong id="b15296113993514"><a name="b15296113993514"></a><a name="b15296113993514"></a>server</strong> (ECSs).</p>
    </td>
    </tr>
    <tr id="row23137205"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p62174317"><a name="p62174317"></a><a name="p62174317"></a>disk</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p38022763"><a name="p38022763"></a><a name="p38022763"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p59944961"><a name="p59944961"></a><a name="p59944961"></a>System disk size corresponding to the server specifications</p>
    </td>
    </tr>
    <tr id="row2633738"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p12006197"><a name="p12006197"></a><a name="p12006197"></a>imagetype</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p53964645"><a name="p53964645"></a><a name="p53964645"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p34827724172525"><a name="p34827724172525"></a><a name="p34827724172525"></a>Image type</p>
    <p id="p53936227172521"><a name="p53936227172521"></a><a name="p53936227172521"></a>The value can be:</p>
    <p id="p58292001172520"><a name="p58292001172520"></a><a name="p58292001172520"></a><strong id="b406533172520"><a name="b406533172520"></a><a name="b406533172520"></a>gold</strong>: public image</p>
    <p id="p19620176172519"><a name="p19620176172519"></a><a name="p19620176172519"></a><strong id="b60702406172519"><a name="b60702406172519"></a><a name="b60702406172519"></a>private</strong>: private image</p>
    <p id="p8318888165816"><a name="p8318888165816"></a><a name="p8318888165816"></a><strong id="b316142575171853"><a name="b316142575171853"></a><a name="b316142575171853"></a>market</strong>: market image</p>
    </td>
    </tr>
    <tr id="row62783896"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p52330790"><a name="p52330790"></a><a name="p52330790"></a>ram</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p47221276438"><a name="p47221276438"></a><a name="p47221276438"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p8862978"><a name="p8862978"></a><a name="p8862978"></a>Memory size of the server, in MB</p>
    </td>
    </tr>
    <tr id="row12657945"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p18660600"><a name="p18660600"></a><a name="p18660600"></a>vcpus</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p27451615134318"><a name="p27451615134318"></a><a name="p27451615134318"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p62839584"><a name="p62839584"></a><a name="p62839584"></a>CPU cores corresponding to the server</p>
    </td>
    </tr>
    <tr id="row28685351"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p41812081"><a name="p41812081"></a><a name="p41812081"></a>eip</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p55141104"><a name="p55141104"></a><a name="p55141104"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p37244403"><a name="p37244403"></a><a name="p37244403"></a>Elastic IP address of the server. If this parameter is left blank, such information about the server has not been obtained.</p>
    </td>
    </tr>
    <tr id="row66764179"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p39189427"><a name="p39189427"></a><a name="p39189427"></a>private_ip</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p27774216"><a name="p27774216"></a><a name="p27774216"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p35118989"><a name="p35118989"></a><a name="p35118989"></a>Internal IP address of the server. If this parameter is left blank, such information about the server has not been obtained.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **image\_data**

    <a name="table17665422205719"></a>
    <table><thead align="left"><tr id="row156851122175719"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.1.4.1.1"><p id="p4940215576"><a name="p4940215576"></a><a name="p4940215576"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.1.4.1.2"><p id="p149462145712"><a name="p149462145712"></a><a name="p149462145712"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.1.4.1.3"><p id="p811019214572"><a name="p811019214572"></a><a name="p811019214572"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6718112212576"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.1.4.1.1 "><p id="p11724172211573"><a name="p11724172211573"></a><a name="p11724172211573"></a>image_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.1.4.1.2 "><p id="p173310227573"><a name="p173310227573"></a><a name="p173310227573"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.1.4.1.3 "><p id="p3739112205719"><a name="p3739112205719"></a><a name="p3739112205719"></a>Image ID</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **fail\_code**

    **Table  6**  Parameter description of field  **fail\_code**

    <a name="table13384103111117"></a>
    <table><thead align="left"><tr id="row173845314115"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p25471729115712"><a name="p25471729115712"></a><a name="p25471729115712"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p656332925713"><a name="p656332925713"></a><a name="p656332925713"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p11563129145715"><a name="p11563129145715"></a><a name="p11563129145715"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1838415319115"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p14384103120115"><a name="p14384103120115"></a><a name="p14384103120115"></a>Code</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p13384113115116"><a name="p13384113115116"></a><a name="p13384113115116"></a>Long</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p23846311716"><a name="p23846311716"></a><a name="p23846311716"></a>Error code</p>
    </td>
    </tr>
    <tr id="row20384231212"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p838433113119"><a name="p838433113119"></a><a name="p838433113119"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p23849318116"><a name="p23849318116"></a><a name="p23849318116"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p163844311713"><a name="p163844311713"></a><a name="p163844311713"></a>Error description</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field** volume\_backup**

    **Table  7**  Parameter description of field** volume\_backup**

    <a name="table26065838"></a>
    <table><thead align="left"><tr id="row3231685"><th class="cellrowborder" valign="top" width="30.23%" id="mcps1.2.4.1.1"><p id="p18379154413571"><a name="p18379154413571"></a><a name="p18379154413571"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.28%" id="mcps1.2.4.1.2"><p id="p6395104425713"><a name="p6395104425713"></a><a name="p6395104425713"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.49%" id="mcps1.2.4.1.3"><p id="p183957444571"><a name="p183957444571"></a><a name="p183957444571"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8986735"><td class="cellrowborder" valign="top" width="30.23%" headers="mcps1.2.4.1.1 "><p id="p56836906"><a name="p56836906"></a><a name="p56836906"></a>average_speed</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.2.4.1.2 "><p id="p50095482"><a name="p50095482"></a><a name="p50095482"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p31202271"><a name="p31202271"></a><a name="p31202271"></a>Average rate, in MB/s</p>
    </td>
    </tr>
    <tr id="row12384989"><td class="cellrowborder" valign="top" width="30.23%" headers="mcps1.2.4.1.1 "><p id="p63660086"><a name="p63660086"></a><a name="p63660086"></a>bootable</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.2.4.1.2 "><p id="p55367277"><a name="p55367277"></a><a name="p55367277"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p55564443"><a name="p55564443"></a><a name="p55564443"></a>Whether the disk is bootable</p>
    <p id="p16852144118620"><a name="p16852144118620"></a><a name="p16852144118620"></a>The value can be <strong id="b1378425815460"><a name="b1378425815460"></a><a name="b1378425815460"></a>true</strong> or <strong id="b3785135820461"><a name="b3785135820461"></a><a name="b3785135820461"></a>false</strong>.</p>
    </td>
    </tr>
    <tr id="row30317943"><td class="cellrowborder" valign="top" width="30.23%" headers="mcps1.2.4.1.1 "><p id="p39834343"><a name="p39834343"></a><a name="p39834343"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.2.4.1.2 "><p id="p31212633"><a name="p31212633"></a><a name="p31212633"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p45195306"><a name="p45195306"></a><a name="p45195306"></a>Cinder backup ID</p>
    </td>
    </tr>
    <tr id="row4104573"><td class="cellrowborder" valign="top" width="30.23%" headers="mcps1.2.4.1.1 "><p id="p64035022"><a name="p64035022"></a><a name="p64035022"></a>image_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.2.4.1.2 "><p id="p32297070"><a name="p32297070"></a><a name="p32297070"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p65925901"><a name="p65925901"></a><a name="p65925901"></a>Backup set type: backup</p>
    <p id="p56462200"><a name="p56462200"></a><a name="p56462200"></a>Enum:[ backup]</p>
    </td>
    </tr>
    <tr id="row38397760"><td class="cellrowborder" valign="top" width="30.23%" headers="mcps1.2.4.1.1 "><p id="p23210864"><a name="p23210864"></a><a name="p23210864"></a>incremental</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.2.4.1.2 "><p id="p16467941"><a name="p16467941"></a><a name="p16467941"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p58834810"><a name="p58834810"></a><a name="p58834810"></a>Whether incremental backup is used</p>
    </td>
    </tr>
    <tr id="row59751243"><td class="cellrowborder" valign="top" width="30.23%" headers="mcps1.2.4.1.1 "><p id="p8012554"><a name="p8012554"></a><a name="p8012554"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.2.4.1.2 "><p id="p24132138"><a name="p24132138"></a><a name="p24132138"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p8546138"><a name="p8546138"></a><a name="p8546138"></a>EVS disk backup name</p>
    </td>
    </tr>
    <tr id="row9806383"><td class="cellrowborder" valign="top" width="30.23%" headers="mcps1.2.4.1.1 "><p id="p56119559"><a name="p56119559"></a><a name="p56119559"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.2.4.1.2 "><p id="p41203013"><a name="p41203013"></a><a name="p41203013"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p49109755"><a name="p49109755"></a><a name="p49109755"></a>Accumulated size (MB) of backups</p>
    </td>
    </tr>
    <tr id="row39334612"><td class="cellrowborder" valign="top" width="30.23%" headers="mcps1.2.4.1.1 "><p id="p31986975"><a name="p31986975"></a><a name="p31986975"></a>source_volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.2.4.1.2 "><p id="p17128847"><a name="p17128847"></a><a name="p17128847"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p45259396"><a name="p45259396"></a><a name="p45259396"></a>Source disk ID</p>
    </td>
    </tr>
    <tr id="row4681386"><td class="cellrowborder" valign="top" width="30.23%" headers="mcps1.2.4.1.1 "><p id="p43648019"><a name="p43648019"></a><a name="p43648019"></a>source_volume_size</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.2.4.1.2 "><p id="p21133674"><a name="p21133674"></a><a name="p21133674"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p34106024"><a name="p34106024"></a><a name="p34106024"></a>Source volume size in GB</p>
    </td>
    </tr>
    <tr id="row38518764"><td class="cellrowborder" valign="top" width="30.23%" headers="mcps1.2.4.1.1 "><p id="p33012204"><a name="p33012204"></a><a name="p33012204"></a>space_saving_ratio</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.2.4.1.2 "><p id="p32770942"><a name="p32770942"></a><a name="p32770942"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p37200607"><a name="p37200607"></a><a name="p37200607"></a>Space saving rate</p>
    </td>
    </tr>
    <tr id="row66370010"><td class="cellrowborder" valign="top" width="30.23%" headers="mcps1.2.4.1.1 "><p id="p7261755"><a name="p7261755"></a><a name="p7261755"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.2.4.1.2 "><p id="p64196347"><a name="p64196347"></a><a name="p64196347"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p32521642"><a name="p32521642"></a><a name="p32521642"></a>Status</p>
    </td>
    </tr>
    <tr id="row24259325"><td class="cellrowborder" valign="top" width="30.23%" headers="mcps1.2.4.1.1 "><p id="p18848346"><a name="p18848346"></a><a name="p18848346"></a>source_volume_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.2.4.1.2 "><p id="p49472988"><a name="p49472988"></a><a name="p49472988"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p47889106"><a name="p47889106"></a><a name="p47889106"></a>Source volume name</p>
    </td>
    </tr>
    <tr id="row0397855134916"><td class="cellrowborder" valign="top" width="30.23%" headers="mcps1.2.4.1.1 "><p id="p18739530979"><a name="p18739530979"></a><a name="p18739530979"></a>snapshot_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.2.4.1.2 "><p id="p773917301975"><a name="p773917301975"></a><a name="p773917301975"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p3739143011716"><a name="p3739143011716"></a><a name="p3739143011716"></a>ID of the snapshot from which the backup is generated</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **resource\_tag**

    **Table  8**  Parameter description of field  **resource\_tag**

    <a name="table1431115645119"></a>
    <table><thead align="left"><tr id="row4339106155119"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p342655335719"><a name="p342655335719"></a><a name="p342655335719"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p34261953135718"><a name="p34261953135718"></a><a name="p34261953135718"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p5442253135717"><a name="p5442253135717"></a><a name="p5442253135717"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row63768665110"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p10380567512"><a name="p10380567512"></a><a name="p10380567512"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p1739414617517"><a name="p1739414617517"></a><a name="p1739414617517"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p13925135105714"><a name="p13925135105714"></a><a name="p13925135105714"></a>Tag key</p>
    <p id="p7327206587"><a name="p7327206587"></a><a name="p7327206587"></a>It consists of up to 36 characters.</p>
    <p id="p145821075819"><a name="p145821075819"></a><a name="p145821075819"></a>It cannot be an empty string.</p>
    <p id="p14766132412516"><a name="p14766132412516"></a><a name="p14766132412516"></a>It can contain only letters, digits, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    <tr id="row1116111556513"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p1816118554511"><a name="p1816118554511"></a><a name="p1816118554511"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p1116145519518"><a name="p1116145519518"></a><a name="p1116145519518"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p1966153512589"><a name="p1966153512589"></a><a name="p1966153512589"></a>Tag value</p>
    <p id="p8808725135910"><a name="p8808725135910"></a><a name="p8808725135910"></a>It consists of up to 43 characters.</p>
    <p id="p919321595"><a name="p919321595"></a><a name="p919321595"></a>It can be an empty string.</p>
    <p id="p5975131663719"><a name="p5975131663719"></a><a name="p5975131663719"></a>It can contain only letters, digits, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
      "checkpoint_item": {
        "status": "available",
        "backup_data": {
          "eip": "",
          "cloudservicetype": "",
          "ram": 4096,
          "vcpus": 4,
          "__openstack_region_name": "",
          "private_ip": "",
          "disk": 0,
          "imagetype": ""
        },
        "name": "backup_d32c",
        "resource_id": "f45c477a-57e5-465f-999f-d845083962db",
        "created_at": "2017-04-15T04:20:37.277880",
        "checkpoint_id": "f672a1bb-6912-446a-816c-72792c5263e0",
        "updated_at": "2017-04-15T04:25:38.680638",
        "resource_type": "OS::Nova::Server",
        "extend_info": {
          "auto_trigger": false,
          "space_saving_ratio": 0,
          "copy_status": "na",
          "fail_reason": "",
          "resource_az": "az1.dc1",
          "image_type": "backup",
          "finished_at": "2017-04-15T04:25:38.675478",
          "average_speed": 0,
          "copy_from": "",
          "supported_restore_mode": "backup",
          "support_lld": false,
          "os_images_data": [
                {
                    "image_id": "fe84dd80-0229-4918-8d3d-cbb33154b565"
                }
            ],
          "volume_backups": [
            {
              "status": "available",
              "space_saving_ratio": 0,
              "name": "manualbk_47222",
              "bootable": true,
              "average_speed": 0,
              "source_volume_size": 20,
              "source_volume_id": "ee27f809-6fb5-40ae-ac46-c932bb4ee8fe",
              "incremental": false,
              "image_type": "backup",
              "source_volume_name": "karbor_02",
              "id": "70675cbc-d3a8-43a7-9f81-c8b6bc3f5d6d",
              "size": 0,
              "snapshot_id": "36f520e1-d2ea-4907-956a-3d9cd53e2d38"
            },
            {
              "status": "available",
              "space_saving_ratio": 0,
              "name": "manualbk_47222",
              "bootable": true,
              "average_speed": 0,
              "source_volume_size": 20,
              "source_volume_id": "e7f48980-927c-48de-afd4-f0245d2e5100",
              "incremental": false,
              "image_type": "backup",
              "source_volume_name": "karbor_01",
              "id": "8eb98e91-8924-4d4b-b6d6-28fb7b751e9c",
              "size": 0,
              "snapshot_id": "36f520e1-d2ea-4907-956a-3d9cd53e2d38"
            }
          ],
          "fail_code": {},
          "incremental": false,
          "taskid": "e0a21692-2192-11e7-bf23-0242ac110007",
          "hypervisor_type": "QEMU",
          "progress": 100,
          "fail_op": "",
          "resource_name": "karbor_02",
          "size": 0
        },
        "id": "90c1d5fa-1b9f-4aeb-b2f4-81c806e98190"
      }
    }
    ```


## Status Codes<a name="section56266399"></a>

-   Normal

    <a name="table29990020"></a>
    <table><thead align="left"><tr id="row12023846"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p34407455"><a name="p34407455"></a><a name="p34407455"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p35540469"><a name="p35540469"></a><a name="p35540469"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row60205711"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p44824405"><a name="p44824405"></a><a name="p44824405"></a>200</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p6898225"><a name="p6898225"></a><a name="p6898225"></a>OK</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    <a name="table21885320"></a>
    <table><thead align="left"><tr id="row58019898"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p1991264"><a name="p1991264"></a><a name="p1991264"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p27074695"><a name="p27074695"></a><a name="p27074695"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row45566678"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p67022326"><a name="p67022326"></a><a name="p67022326"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p60099343"><a name="p60099343"></a><a name="p60099343"></a>Invalid request parameters.</p>
    </td>
    </tr>
    <tr id="row4023176"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p57441800"><a name="p57441800"></a><a name="p57441800"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p22274196"><a name="p22274196"></a><a name="p22274196"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row66250043"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p64653253"><a name="p64653253"></a><a name="p64653253"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p2422160"><a name="p2422160"></a><a name="p2422160"></a>No operation permission.</p>
    </td>
    </tr>
    <tr id="row21799445"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p20924644"><a name="p20924644"></a><a name="p20924644"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p17174599"><a name="p17174599"></a><a name="p17174599"></a>Requested object not found.</p>
    </td>
    </tr>
    <tr id="row20353668"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p38034401"><a name="p38034401"></a><a name="p38034401"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p60887622"><a name="p60887622"></a><a name="p60887622"></a>Service unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section61541938486"></a>

For details, see  [Error Codes](error-codes.md).


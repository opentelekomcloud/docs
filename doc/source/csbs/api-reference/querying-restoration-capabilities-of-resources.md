# Querying Restoration Capabilities of Resources<a name="EN-US_TOPIC_0059304221"></a>

## Function<a name="section60828768"></a>

This API is used to check whether target resources can be restored.

## URI<a name="section10588005"></a>

-   URI format

    POST https://\{endpoint\}/v1/\{project\_id\}/providers/\{provider\_id\}/resources/action

-   Parameter description

    **Table  1**  Parameter description

    <a name="table38853252"></a>
    <table><thead align="left"><tr id="row62235384"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.5.1.1"><p id="p7901367"><a name="p7901367"></a><a name="p7901367"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.2"><p id="p36030986"><a name="p36030986"></a><a name="p36030986"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p32828762"><a name="p32828762"></a><a name="p32828762"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.2.5.1.4"><p id="p41884046"><a name="p41884046"></a><a name="p41884046"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row37164559"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.1 "><p id="p57539268"><a name="p57539268"></a><a name="p57539268"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p30169109"><a name="p30169109"></a><a name="p30169109"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p27778796"><a name="p27778796"></a><a name="p27778796"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p65779720"><a name="p65779720"></a><a name="p65779720"></a>Project ID</p>
    </td>
    </tr>
    <tr id="row50974244"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.1 "><p id="p35273076"><a name="p35273076"></a><a name="p35273076"></a>provider_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p38546917"><a name="p38546917"></a><a name="p38546917"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p35292574"><a name="p35292574"></a><a name="p35292574"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p58434680"><a name="p58434680"></a><a name="p58434680"></a>Backup provider ID, which specifies whether the backup object is a server or disk. This parameter has a fixed value. For CSBS, the value is <strong id="b64907295339"><a name="b64907295339"></a><a name="b64907295339"></a>fc4d5750-22e7-4798-8a46-f48f62c4c1da</strong>. </p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section28183181"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table455054"></a>
    <table><thead align="left"><tr id="row35180024"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.5.1.1"><p id="p31009716"><a name="p31009716"></a><a name="p31009716"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.2"><p id="p28759101"><a name="p28759101"></a><a name="p28759101"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p47785850"><a name="p47785850"></a><a name="p47785850"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.2.5.1.4"><p id="p45448660"><a name="p45448660"></a><a name="p45448660"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row57462834"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.1 "><p id="p23977981"><a name="p23977981"></a><a name="p23977981"></a>check_restorable</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p63168284"><a name="p63168284"></a><a name="p63168284"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p16357368"><a name="p16357368"></a><a name="p16357368"></a>List&lt;restorable_param&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p49878392"><a name="p49878392"></a><a name="p49878392"></a>Query parameter list</p>
    <p id="p1268982420503"><a name="p1268982420503"></a><a name="p1268982420503"></a>For details, see <a href="#table13617924">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **restorable\_param**

    **Table  3**  Parameter description of field  **restorable\_param**

    <a name="table13617924"></a>
    <table><thead align="left"><tr id="row60772788"><th class="cellrowborder" valign="top" width="23.232323232323235%" id="mcps1.2.5.1.1"><p id="p23648759"><a name="p23648759"></a><a name="p23648759"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.161616161616163%" id="mcps1.2.5.1.2"><p id="p36501364"><a name="p36501364"></a><a name="p36501364"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.141414141414144%" id="mcps1.2.5.1.3"><p id="p3820497"><a name="p3820497"></a><a name="p3820497"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46.46464646464647%" id="mcps1.2.5.1.4"><p id="p41024822"><a name="p41024822"></a><a name="p41024822"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row34676300"><td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.5.1.1 "><p id="p57316922"><a name="p57316922"></a><a name="p57316922"></a>checkpoint_item_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.2 "><p id="p12159145"><a name="p12159145"></a><a name="p12159145"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.3 "><p id="p45366721"><a name="p45366721"></a><a name="p45366721"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.46464646464647%" headers="mcps1.2.5.1.4 "><p id="p50825769"><a name="p50825769"></a><a name="p50825769"></a>ID of the backup used to restore data</p>
    </td>
    </tr>
    <tr id="row54778738"><td class="cellrowborder" valign="top" width="23.232323232323235%" headers="mcps1.2.5.1.1 "><p id="p7892822"><a name="p7892822"></a><a name="p7892822"></a>target</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.161616161616163%" headers="mcps1.2.5.1.2 "><p id="p35338846"><a name="p35338846"></a><a name="p35338846"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.141414141414144%" headers="mcps1.2.5.1.3 "><p id="p43874291"><a name="p43874291"></a><a name="p43874291"></a>restorable_target</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.46464646464647%" headers="mcps1.2.5.1.4 "><p id="p64156668"><a name="p64156668"></a><a name="p64156668"></a>Restoration target</p>
    <p id="p46241633185512"><a name="p46241633185512"></a><a name="p46241633185512"></a>For details, see <a href="#table29307618">Table 4</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **restorable\_target**

    **Table  4**  Parameter description of field  **restorable\_target**

    <a name="table29307618"></a>
    <table><thead align="left"><tr id="row31188670"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.5.1.1"><p id="p43254371"><a name="p43254371"></a><a name="p43254371"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.2"><p id="p13943185"><a name="p13943185"></a><a name="p13943185"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p55656175"><a name="p55656175"></a><a name="p55656175"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.2.5.1.4"><p id="p11856293"><a name="p11856293"></a><a name="p11856293"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row20835676"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.1 "><p id="p9968187"><a name="p9968187"></a><a name="p9968187"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p2116843"><a name="p2116843"></a><a name="p2116843"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p37246612"><a name="p37246612"></a><a name="p37246612"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p64185565"><a name="p64185565"></a><a name="p64185565"></a>ID of the resource to which the backup is restored</p>
    </td>
    </tr>
    <tr id="row15677191352"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.1 "><p id="p29702147354"><a name="p29702147354"></a><a name="p29702147354"></a>resource_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p097011483517"><a name="p097011483517"></a><a name="p097011483517"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p397071417357"><a name="p397071417357"></a><a name="p397071417357"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p13970201443514"><a name="p13970201443514"></a><a name="p13970201443514"></a>Type of the target to which the backup is restored, for example, <strong id="b842352706105620"><a name="b842352706105620"></a><a name="b842352706105620"></a>OS::Nova::Server</strong> for an ECS</p>
    </td>
    </tr>
    <tr id="row699049"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.5.1.1 "><p id="p56622972"><a name="p56622972"></a><a name="p56622972"></a>volumes</p>
    </td>
    <td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.2 "><p id="p23058057"><a name="p23058057"></a><a name="p23058057"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p55763318"><a name="p55763318"></a><a name="p55763318"></a>List&lt;restore_volume_mapping&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p20534891"><a name="p20534891"></a><a name="p20534891"></a>Disk mapping list for restoring an ECS. Enter the mapping between disks and backups based on the actual situation.</p>
    <p id="p11429445426"><a name="p11429445426"></a><a name="p11429445426"></a>For details, see <a href="#table52713489">Table 5</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **restore\_volume\_mapping**

    **Table  5**  Parameter description of field  **restore\_volume\_mapping**

    <a name="table52713489"></a>
    <table><thead align="left"><tr id="row58237160"><th class="cellrowborder" valign="top" width="24%" id="mcps1.2.5.1.1"><p id="p19589535"><a name="p19589535"></a><a name="p19589535"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16%" id="mcps1.2.5.1.2"><p id="p43248531"><a name="p43248531"></a><a name="p43248531"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.3"><p id="p13470123"><a name="p13470123"></a><a name="p13470123"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.2.5.1.4"><p id="p17338192"><a name="p17338192"></a><a name="p17338192"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row62216297"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.5.1.1 "><p id="p6355295"><a name="p6355295"></a><a name="p6355295"></a>backup_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p45016857"><a name="p45016857"></a><a name="p45016857"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p22486783"><a name="p22486783"></a><a name="p22486783"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p9490171"><a name="p9490171"></a><a name="p9490171"></a>Disk backup ID. Use the API in <a href="querying-a-single-backup.md">Querying a Single Backup</a> to obtain the disk backup ID.</p>
    </td>
    </tr>
    <tr id="row18302675"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.5.1.1 "><p id="p6121736"><a name="p6121736"></a><a name="p6121736"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.5.1.2 "><p id="p26098630"><a name="p26098630"></a><a name="p26098630"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.3 "><p id="p33614260"><a name="p33614260"></a><a name="p33614260"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.5.1.4 "><p id="p38400506"><a name="p38400506"></a><a name="p38400506"></a>ID of the destination EVS disk for the restoration</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    POST https://{endpoint}/v1/{project_id}/providers/{provider_id}/resources/action
    {
      "check_restorable" : [ {
        "checkpoint_item_id" : "8986ce68-3da7-4d29-9cc2-1921e9504975",
        "target" : {
          "resource_type" : "OS::Nova::Server",
          "resource_id" : "5aa119a8-d25b-45a7-8d1b-88e127885635",
          "volumes" : [ {
            "backup_id" : "7ea119a8-d25b-43a7-8d1b-88e12788513a",
            "volume_id" : "45baf976-c20a-4894-a7c3-c94b7376bf55"
          } ]
        }
      } ]
    }
    ```


## Response<a name="section52322043"></a>

-   Parameter description

    **Table  6**  Parameter description

    <a name="table50512031"></a>
    <table><thead align="left"><tr id="row1710363"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p4321696"><a name="p4321696"></a><a name="p4321696"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p34711268"><a name="p34711268"></a><a name="p34711268"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p60149363"><a name="p60149363"></a><a name="p60149363"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row40260267"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p39856179"><a name="p39856179"></a><a name="p39856179"></a>restorable</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p40257620"><a name="p40257620"></a><a name="p40257620"></a>List&lt;check_resp&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p39641789"><a name="p39641789"></a><a name="p39641789"></a>Response parameter list</p>
    <p id="p69311451934"><a name="p69311451934"></a><a name="p69311451934"></a>For details, see <a href="#table56868375">Table 7</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **check\_resp**

    **Table  7**  Parameter description of field  **check\_resp**

    <a name="table56868375"></a>
    <table><thead align="left"><tr id="row3799708"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p39340968"><a name="p39340968"></a><a name="p39340968"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p15400731"><a name="p15400731"></a><a name="p15400731"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p39499732"><a name="p39499732"></a><a name="p39499732"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row45361729"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p50421451"><a name="p50421451"></a><a name="p50421451"></a>result</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p35551828"><a name="p35551828"></a><a name="p35551828"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p61125795"><a name="p61125795"></a><a name="p61125795"></a>Whether restoration is supported</p>
    </td>
    </tr>
    <tr id="row13261246"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p419111"><a name="p419111"></a><a name="p419111"></a>resource_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p65432826"><a name="p65432826"></a><a name="p65432826"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p65567540"><a name="p65567540"></a><a name="p65567540"></a>Resource type</p>
    </td>
    </tr>
    <tr id="row53236954"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p17226028"><a name="p17226028"></a><a name="p17226028"></a>error_code</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p8647870"><a name="p8647870"></a><a name="p8647870"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p29388878"><a name="p29388878"></a><a name="p29388878"></a>Error code</p>
    </td>
    </tr>
    <tr id="row63173312"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p16764629"><a name="p16764629"></a><a name="p16764629"></a>error_msg</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p1307193"><a name="p1307193"></a><a name="p1307193"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p38773848"><a name="p38773848"></a><a name="p38773848"></a>Error reason</p>
    </td>
    </tr>
    <tr id="row13420320"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p13304098"><a name="p13304098"></a><a name="p13304098"></a>resource_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p46668301"><a name="p46668301"></a><a name="p46668301"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p22036037"><a name="p22036037"></a><a name="p22036037"></a>Resource ID</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
      "restorable" : [ {
        "resource_id" : "6507cb66-90dc-4a12-a573-c9f3398f899d",
        "resource_type" : "OS::Nova::Server",
        "result" : true,
        "error_msg" : "",
        "error_code" : ""
      } ]
    }
    ```


## Status Codes<a name="section1136343"></a>

-   Normal

    <a name="table27948268"></a>
    <table><thead align="left"><tr id="row43246910"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p13338788"><a name="p13338788"></a><a name="p13338788"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p6700043"><a name="p6700043"></a><a name="p6700043"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5832602"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p2678778"><a name="p2678778"></a><a name="p2678778"></a>200</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p15654483"><a name="p15654483"></a><a name="p15654483"></a>OK</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    <a name="table60053580"></a>
    <table><thead align="left"><tr id="row4363833"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p17926231"><a name="p17926231"></a><a name="p17926231"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p42738617"><a name="p42738617"></a><a name="p42738617"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row39275976"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p27237483"><a name="p27237483"></a><a name="p27237483"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p58752523"><a name="p58752523"></a><a name="p58752523"></a>Invalid request parameters.</p>
    </td>
    </tr>
    <tr id="row59010661"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p15134218"><a name="p15134218"></a><a name="p15134218"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p17912160"><a name="p17912160"></a><a name="p17912160"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row26991717"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p38845446"><a name="p38845446"></a><a name="p38845446"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p59473453"><a name="p59473453"></a><a name="p59473453"></a>No operation permission.</p>
    </td>
    </tr>
    <tr id="row65499029"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p3821117"><a name="p3821117"></a><a name="p3821117"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p41075037"><a name="p41075037"></a><a name="p41075037"></a>Requested object not found.</p>
    </td>
    </tr>
    <tr id="row34131018"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p13149074"><a name="p13149074"></a><a name="p13149074"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p58442087"><a name="p58442087"></a><a name="p58442087"></a>Service internal error.</p>
    </td>
    </tr>
    <tr id="row56216737"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p57261876"><a name="p57261876"></a><a name="p57261876"></a>503</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p7700359"><a name="p7700359"></a><a name="p7700359"></a>Service unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section61541938486"></a>

For details, see  [Error Codes](error-codes.md).


# Creating a Restoration Task<a name="EN-US_TOPIC_0059304237"></a>

## Function<a name="section47319991"></a>

This API is used to perform backup-based restoration.

## URI<a name="section23226740"></a>

-   URI format

    POST https://\{endpoint\}/v1/\{project\_id\}/restores

-   Parameter description

    **Table  1**  Parameter description

    <a name="table12661318"></a>
    <table><thead align="left"><tr id="row56776745"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p209623317216"><a name="p209623317216"></a><a name="p209623317216"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p15962193221"><a name="p15962193221"></a><a name="p15962193221"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p99783315213"><a name="p99783315213"></a><a name="p99783315213"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p6978835213"><a name="p6978835213"></a><a name="p6978835213"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row17050458"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p38909824"><a name="p38909824"></a><a name="p38909824"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p64688039"><a name="p64688039"></a><a name="p64688039"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p5239798"><a name="p5239798"></a><a name="p5239798"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p65779720"><a name="p65779720"></a><a name="p65779720"></a>Project ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section7714069"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table28710632"></a>
    <table><thead align="left"><tr id="row13079571"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p2234010161013"><a name="p2234010161013"></a><a name="p2234010161013"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p12234010111010"><a name="p12234010111010"></a><a name="p12234010111010"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p423421081017"><a name="p423421081017"></a><a name="p423421081017"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p20234111011014"><a name="p20234111011014"></a><a name="p20234111011014"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row11623179"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p1953436"><a name="p1953436"></a><a name="p1953436"></a>restore</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p24010593"><a name="p24010593"></a><a name="p24010593"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p65809858"><a name="p65809858"></a><a name="p65809858"></a>restore_req</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p28998313"><a name="p28998313"></a><a name="p28998313"></a>Restoration request</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **restore\_req**

    **Table  3**  Parameter description of field  **restore\_req**

    <a name="table53115"></a>
    <table><thead align="left"><tr id="row43645827"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p6925179107"><a name="p6925179107"></a><a name="p6925179107"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p8109117161014"><a name="p8109117161014"></a><a name="p8109117161014"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p111094177106"><a name="p111094177106"></a><a name="p111094177106"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p21098172106"><a name="p21098172106"></a><a name="p21098172106"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3783082"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p37994222"><a name="p37994222"></a><a name="p37994222"></a>checkpoint_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p57633171"><a name="p57633171"></a><a name="p57633171"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p37775297"><a name="p37775297"></a><a name="p37775297"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p39900191"><a name="p39900191"></a><a name="p39900191"></a>Backup record ID</p>
    </td>
    </tr>
    <tr id="row23557399"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p29101185"><a name="p29101185"></a><a name="p29101185"></a>parameters</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p8385775"><a name="p8385775"></a><a name="p8385775"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p8159178"><a name="p8159178"></a><a name="p8159178"></a>restore_param</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p56913657"><a name="p56913657"></a><a name="p56913657"></a>Restoration parameters</p>
    </td>
    </tr>
    <tr id="row42460868"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p16778253"><a name="p16778253"></a><a name="p16778253"></a>provider_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p16861214"><a name="p16861214"></a><a name="p16861214"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p23581088"><a name="p23581088"></a><a name="p23581088"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p31019962"><a name="p31019962"></a><a name="p31019962"></a>Backup provider ID, which specifies whether the backup object is a server or disk. This parameter has a fixed value. For CSBS, the value is <strong id="b137258248421"><a name="b137258248421"></a><a name="b137258248421"></a>fc4d5750-22e7-4798-8a46-f48f62c4c1da</strong>. </p>
    </td>
    </tr>
    <tr id="row10744208"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p64974530"><a name="p64974530"></a><a name="p64974530"></a>restore_target</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p28445601"><a name="p28445601"></a><a name="p28445601"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p22392340"><a name="p22392340"></a><a name="p22392340"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p1840260"><a name="p1840260"></a><a name="p1840260"></a>Restoration target</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **restore\_param **

    **Table  4**  Parameter description of field  **restore\_param **

    <a name="table14843352"></a>
    <table><thead align="left"><tr id="row21892542"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p1611420131013"><a name="p1611420131013"></a><a name="p1611420131013"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p777162081017"><a name="p777162081017"></a><a name="p777162081017"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p8771420171011"><a name="p8771420171011"></a><a name="p8771420171011"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p277172011107"><a name="p277172011107"></a><a name="p277172011107"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row25273656"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p33900290"><a name="p33900290"></a><a name="p33900290"></a>checkpoint_item_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p61568997"><a name="p61568997"></a><a name="p61568997"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p21032840"><a name="p21032840"></a><a name="p21032840"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p25938451"><a name="p25938451"></a><a name="p25938451"></a>Backup ID</p>
    </td>
    </tr>
    <tr id="row32119471"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p51540395"><a name="p51540395"></a><a name="p51540395"></a>power_on</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p14022434"><a name="p14022434"></a><a name="p14022434"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p62075390"><a name="p62075390"></a><a name="p62075390"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p62050727"><a name="p62050727"></a><a name="p62050727"></a>Whether to instantly power on the VM after restoration</p>
    </td>
    </tr>
    <tr id="row21585636"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p3606058"><a name="p3606058"></a><a name="p3606058"></a>targets</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p23655281"><a name="p23655281"></a><a name="p23655281"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p37029600"><a name="p37029600"></a><a name="p37029600"></a>restore_target</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p46607648"><a name="p46607648"></a><a name="p46607648"></a>Restoration target</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **restore\_target**

    **Table  5**  Parameter description of field  **restore\_target**

    <a name="table17123161"></a>
    <table><thead align="left"><tr id="row25369615"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p1781112221012"><a name="p1781112221012"></a><a name="p1781112221012"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p158111228104"><a name="p158111228104"></a><a name="p158111228104"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p38111222171010"><a name="p38111222171010"></a><a name="p38111222171010"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p12828422161011"><a name="p12828422161011"></a><a name="p12828422161011"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row39968321"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p16208549"><a name="p16208549"></a><a name="p16208549"></a>server_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p37824086"><a name="p37824086"></a><a name="p37824086"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p43852091"><a name="p43852091"></a><a name="p43852091"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p62358460"><a name="p62358460"></a><a name="p62358460"></a>ID of the ECS to be restored</p>
    </td>
    </tr>
    <tr id="row24355235"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p26617051"><a name="p26617051"></a><a name="p26617051"></a>volumes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p8497507"><a name="p8497507"></a><a name="p8497507"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p17209443"><a name="p17209443"></a><a name="p17209443"></a>List&lt;restore_volume_mapping&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p51787652"><a name="p51787652"></a><a name="p51787652"></a>List of the mappings between disk backups and target disks</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **restore\_volume\_mapping**

    **Table  6**  Parameter description of field  **restore\_volume\_mapping**

    <a name="table34050285"></a>
    <table><thead align="left"><tr id="row60246870"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p573432501019"><a name="p573432501019"></a><a name="p573432501019"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p776510252102"><a name="p776510252102"></a><a name="p776510252102"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p676502501013"><a name="p676502501013"></a><a name="p676502501013"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p15765162591010"><a name="p15765162591010"></a><a name="p15765162591010"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row28790660"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p50342129"><a name="p50342129"></a><a name="p50342129"></a>backup_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p51180667"><a name="p51180667"></a><a name="p51180667"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p51993353"><a name="p51993353"></a><a name="p51993353"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p50712068"><a name="p50712068"></a><a name="p50712068"></a>EVS disk backup ID</p>
    </td>
    </tr>
    <tr id="row53755429"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p59222510"><a name="p59222510"></a><a name="p59222510"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p32293975"><a name="p32293975"></a><a name="p32293975"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p65675144"><a name="p65675144"></a><a name="p65675144"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p18086442"><a name="p18086442"></a><a name="p18086442"></a>ID of the destination EVS disk for the restoration</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    POST https://{endpoint}/v1/{project_id}/restores
    {
      "restore" : {
        "provider_id" : "fc4d5750-22e7-4798-8a46-f48f62c4c1da",
        "checkpoint_id" : "a2b9fb53-2770-4fcd-9bad-6cadd56e6c09",
        "parameters" : {
          "checkpoint_item_id" : "504b7d59-c361-411f-9ed3-814f35d08e3d",
          "power_on" : true,
          "targets" : {
            "server_id" : "f45c477a-57e5-465f-999f-d845083962db",
            "volumes" : [ {
              "backup_id" : "bc118c24-3234-4afd-8423-d66d3d677649",
              "volume_id" : "ee27f809-6fb5-40ae-ac46-c932bb4ee8fe"
            }]
          }
        }
      }
    }
    ```


## Response<a name="section2317765"></a>

-   Parameter description

    **Table  7**  Parameter description

    <a name="table66415464"></a>
    <table><thead align="left"><tr id="row10335162"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p567111297101"><a name="p567111297101"></a><a name="p567111297101"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p4671102912102"><a name="p4671102912102"></a><a name="p4671102912102"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p66712299101"><a name="p66712299101"></a><a name="p66712299101"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row11115781"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p27963036"><a name="p27963036"></a><a name="p27963036"></a>restore</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p56958817"><a name="p56958817"></a><a name="p56958817"></a>restore_resp</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p50261470"><a name="p50261470"></a><a name="p50261470"></a>Restoration response</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **restore\_resp **

    **Table  8**  Parameter description of field  **restore\_resp **

    <a name="table44647288"></a>
    <table><thead align="left"><tr id="row16977539"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p15124123817104"><a name="p15124123817104"></a><a name="p15124123817104"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p1124113810109"><a name="p1124113810109"></a><a name="p1124113810109"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p11391138181010"><a name="p11391138181010"></a><a name="p11391138181010"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row31598148"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p9313208"><a name="p9313208"></a><a name="p9313208"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p34891768"><a name="p34891768"></a><a name="p34891768"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p7660949"><a name="p7660949"></a><a name="p7660949"></a>Restoration ID</p>
    </td>
    </tr>
    <tr id="row1839679"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p14796304"><a name="p14796304"></a><a name="p14796304"></a>checkpoint_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p39133622"><a name="p39133622"></a><a name="p39133622"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p15706845"><a name="p15706845"></a><a name="p15706845"></a>Backup record ID</p>
    </td>
    </tr>
    <tr id="row7143877"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p41783149"><a name="p41783149"></a><a name="p41783149"></a>parameters</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p66641358"><a name="p66641358"></a><a name="p66641358"></a>restore_param</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p29240919"><a name="p29240919"></a><a name="p29240919"></a>Restoration parameters</p>
    </td>
    </tr>
    <tr id="row61841687"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p43120736"><a name="p43120736"></a><a name="p43120736"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p51290224"><a name="p51290224"></a><a name="p51290224"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p1145961812578"><a name="p1145961812578"></a><a name="p1145961812578"></a>Project ID</p>
    </td>
    </tr>
    <tr id="row10936254"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p13421378"><a name="p13421378"></a><a name="p13421378"></a>provider_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p10837141"><a name="p10837141"></a><a name="p10837141"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p5393203"><a name="p5393203"></a><a name="p5393203"></a>Backup provider ID, which specifies whether the backup object is a server or disk. This parameter has a fixed value. For CSBS, the value is <strong id="b12591927124216"><a name="b12591927124216"></a><a name="b12591927124216"></a>fc4d5750-22e7-4798-8a46-f48f62c4c1da</strong>. </p>
    </td>
    </tr>
    <tr id="row48538827"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p39330933"><a name="p39330933"></a><a name="p39330933"></a>resources_reason</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p16671806"><a name="p16671806"></a><a name="p16671806"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p8239021"><a name="p8239021"></a><a name="p8239021"></a>Cause of the resource restoration failure</p>
    </td>
    </tr>
    <tr id="row7042328"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p33557665"><a name="p33557665"></a><a name="p33557665"></a>resources_status</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p54766260"><a name="p54766260"></a><a name="p54766260"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p6882062"><a name="p6882062"></a><a name="p6882062"></a>Resource status after the resource is restored, for example, <strong id="b12867144242218"><a name="b12867144242218"></a><a name="b12867144242218"></a>available</strong></p>
    </td>
    </tr>
    <tr id="row61938564"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p50967798"><a name="p50967798"></a><a name="p50967798"></a>restore_target</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p63367368"><a name="p63367368"></a><a name="p63367368"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p32483192"><a name="p32483192"></a><a name="p32483192"></a>Restoration target</p>
    </td>
    </tr>
    <tr id="row23913274"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p57927023"><a name="p57927023"></a><a name="p57927023"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p21705491"><a name="p21705491"></a><a name="p21705491"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p13314386"><a name="p13314386"></a><a name="p13314386"></a>Status</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **restore\_param **

    **Table  9**  Parameter description of field  **restore\_param **

    <a name="table4723514"></a>
    <table><thead align="left"><tr id="row22070159"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p382894716109"><a name="p382894716109"></a><a name="p382894716109"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p4828204781017"><a name="p4828204781017"></a><a name="p4828204781017"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p9828247171020"><a name="p9828247171020"></a><a name="p9828247171020"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row60159267"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p41062495"><a name="p41062495"></a><a name="p41062495"></a>checkpoint_item_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p36050226"><a name="p36050226"></a><a name="p36050226"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p34387227"><a name="p34387227"></a><a name="p34387227"></a>Backup ID</p>
    </td>
    </tr>
    <tr id="row41049592"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p36682622"><a name="p36682622"></a><a name="p36682622"></a>power_on</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p22299828"><a name="p22299828"></a><a name="p22299828"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p61455668"><a name="p61455668"></a><a name="p61455668"></a>Whether to power on the VM after restoration</p>
    </td>
    </tr>
    <tr id="row16230106"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p39570198"><a name="p39570198"></a><a name="p39570198"></a>targets</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p42983138"><a name="p42983138"></a><a name="p42983138"></a>restore_target</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p59082179"><a name="p59082179"></a><a name="p59082179"></a>Restoration target</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **restore\_target**

    **Table  10**  Parameter description of field  **restore\_target**

    <a name="table20927233"></a>
    <table><thead align="left"><tr id="row29751330"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p5498105641013"><a name="p5498105641013"></a><a name="p5498105641013"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p74981156131013"><a name="p74981156131013"></a><a name="p74981156131013"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p16498356191012"><a name="p16498356191012"></a><a name="p16498356191012"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row59589943"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p62056111"><a name="p62056111"></a><a name="p62056111"></a>server_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p668343"><a name="p668343"></a><a name="p668343"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p54135832"><a name="p54135832"></a><a name="p54135832"></a>ID of the ECS to be restored</p>
    </td>
    </tr>
    <tr id="row17460444"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p5009873"><a name="p5009873"></a><a name="p5009873"></a>volumes</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p53544320"><a name="p53544320"></a><a name="p53544320"></a>List&lt;restore_volume_mapping&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p42122634"><a name="p42122634"></a><a name="p42122634"></a>List of the mappings between disk backups and target disks</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field** restore\_volume\_mapping**

    **Table  11**  Parameter description of field  **restore\_volume\_mapping**

    <a name="table56490176"></a>
    <table><thead align="left"><tr id="row9659135"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p52219317117"><a name="p52219317117"></a><a name="p52219317117"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p12214381118"><a name="p12214381118"></a><a name="p12214381118"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p122378371111"><a name="p122378371111"></a><a name="p122378371111"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row54023737"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p13846594"><a name="p13846594"></a><a name="p13846594"></a>backup_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p49210972"><a name="p49210972"></a><a name="p49210972"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p26665790"><a name="p26665790"></a><a name="p26665790"></a>EVS disk ID</p>
    </td>
    </tr>
    <tr id="row38665520"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p44899454"><a name="p44899454"></a><a name="p44899454"></a>volume_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p44517711"><a name="p44517711"></a><a name="p44517711"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p49164834"><a name="p49164834"></a><a name="p49164834"></a>ID of the disk to which data is restored</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
      "restore" : {
        "restore_target" : "http://192.168.1.2:35357/v2.0/",
        "status" : "in_progress",
        "provider_id" : "fc4d5750-22e7-4798-8a46-f48f62c4c1da",
        "resources_status" : in_progress,
        "parameters" : {
          "power_on" : true,
          "targets" : {
            "server_id" : "f45c477a-57e5-465f-999f-d845083962db",
            "volumes" : [ {
              "backup_id" : "bc118c24-3234-4afd-8423-d66d3d677649",
              "volume_id" : "ee27f809-6fb5-40ae-ac46-c932bb4ee8fe"
            } ]
          },
          "checkpoint_item_id" : "504b7d59-c361-411f-9ed3-814f35d08e3d"
        },
        "checkpoint_id" : "a2b9fb53-2770-4fcd-9bad-6cadd56e6c09",
        "project_id" : "b942cc8342734d15bcb246babb1953cf",
        "id" : "d3a54e80-6483-485d-98f6-c0409e6f2e0a",
        "resources_reason" : { }
      }
    }
    ```


## Status Codes<a name="section20859892"></a>

-   Normal

    <a name="table47027991"></a>
    <table><thead align="left"><tr id="row58173825"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p14459414"><a name="p14459414"></a><a name="p14459414"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p30361908"><a name="p30361908"></a><a name="p30361908"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row43395458"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p25371176"><a name="p25371176"></a><a name="p25371176"></a>200</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p41799375"><a name="p41799375"></a><a name="p41799375"></a>OK</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    <a name="table30306206"></a>
    <table><thead align="left"><tr id="row26237840"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p44890256"><a name="p44890256"></a><a name="p44890256"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p12232092"><a name="p12232092"></a><a name="p12232092"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row51275421"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p59668475"><a name="p59668475"></a><a name="p59668475"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p1308317"><a name="p1308317"></a><a name="p1308317"></a>Invalid request parameters.</p>
    </td>
    </tr>
    <tr id="row11774860"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p14239567"><a name="p14239567"></a><a name="p14239567"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p12554316"><a name="p12554316"></a><a name="p12554316"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row45879983"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p25291123"><a name="p25291123"></a><a name="p25291123"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p35315076"><a name="p35315076"></a><a name="p35315076"></a>No operation permission.</p>
    </td>
    </tr>
    <tr id="row49400228"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p41995538"><a name="p41995538"></a><a name="p41995538"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p46195457"><a name="p46195457"></a><a name="p46195457"></a>Requested object not found.</p>
    </td>
    </tr>
    <tr id="row13105937"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p54947939"><a name="p54947939"></a><a name="p54947939"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p21598090"><a name="p21598090"></a><a name="p21598090"></a>Service internal error.</p>
    </td>
    </tr>
    <tr id="row60165089"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p41534050"><a name="p41534050"></a><a name="p41534050"></a>503</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p8814891"><a name="p8814891"></a><a name="p8814891"></a>Service unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section61541938486"></a>

For details, see  [Error Codes](error-codes.md).


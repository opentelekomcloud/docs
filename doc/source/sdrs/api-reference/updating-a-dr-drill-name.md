# Updating a DR Drill Name<a name="sdrs_05_0705"></a>

## Function<a name="section1810962253512"></a>

This API is used to update a DR drill name.

## Constraints and Limitations<a name="section141111422123517"></a>

None

## URI<a name="section191111522133517"></a>

-   URI format

    PUT /v1/\{project\_id\}/disaster-recovery-drills/\{disaster\_recovery\_drill\_id\}

-   Parameter description

    <a name="table171141220353"></a>
    <table><thead align="left"><tr id="row6824922123519"><th class="cellrowborder" valign="top" width="32.32%" id="mcps1.1.4.1.1"><p id="p9824132253519"><a name="p9824132253519"></a><a name="p9824132253519"></a><strong id="b84235270615443"><a name="b84235270615443"></a><a name="b84235270615443"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.169999999999998%" id="mcps1.1.4.1.2"><p id="p1824122133515"><a name="p1824122133515"></a><a name="p1824122133515"></a><strong id="b84235270615447"><a name="b84235270615447"></a><a name="b84235270615447"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.51%" id="mcps1.1.4.1.3"><p id="p2082442213358"><a name="p2082442213358"></a><a name="p2082442213358"></a><strong id="b84235270615457"><a name="b84235270615457"></a><a name="b84235270615457"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row168241522123517"><td class="cellrowborder" valign="top" width="32.32%" headers="mcps1.1.4.1.1 "><p id="p282412220353"><a name="p282412220353"></a><a name="p282412220353"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.1.4.1.2 "><p id="p19824722183516"><a name="p19824722183516"></a><a name="p19824722183516"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.51%" headers="mcps1.1.4.1.3 "><p id="p168240224354"><a name="p168240224354"></a><a name="p168240224354"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row6824182219356"><td class="cellrowborder" valign="top" width="32.32%" headers="mcps1.1.4.1.1 "><p id="p38241522173517"><a name="p38241522173517"></a><a name="p38241522173517"></a>disaster_recovery_drill_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.1.4.1.2 "><p id="p1982418229355"><a name="p1982418229355"></a><a name="p1982418229355"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.51%" headers="mcps1.1.4.1.3 "><p id="p1882414229359"><a name="p1882414229359"></a><a name="p1882414229359"></a>Specifies the DR drill ID.</p>
    <p id="p161148302521"><a name="p161148302521"></a><a name="p161148302521"></a>To query details, see <a href="querying-dr-drills.md">Querying DR Drills</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section9126922193518"></a>

-   Parameter description

    <a name="table58502114422"></a>
    <table><thead align="left"><tr id="row1785021111425"><th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.1"><p id="p1884919112427"><a name="p1884919112427"></a><a name="p1884919112427"></a><strong id="b84235270615443_1"><a name="b84235270615443_1"></a><a name="b84235270615443_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.1.5.1.2"><p id="p5850121117421"><a name="p5850121117421"></a><a name="p5850121117421"></a><strong id="b84235270615447_1"><a name="b84235270615447_1"></a><a name="b84235270615447_1"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.1.5.1.3"><p id="p58501114428"><a name="p58501114428"></a><a name="p58501114428"></a><strong id="b84235270615453"><a name="b84235270615453"></a><a name="b84235270615453"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.1.5.1.4"><p id="p16850141174211"><a name="p16850141174211"></a><a name="p16850141174211"></a><strong id="b84235270615457_1"><a name="b84235270615457_1"></a><a name="b84235270615457_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5850121110425"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p18850511154212"><a name="p18850511154212"></a><a name="p18850511154212"></a>disaster_recovery_drill</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.2 "><p id="p385031115428"><a name="p385031115428"></a><a name="p385031115428"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.3 "><p id="p1985021110428"><a name="p1985021110428"></a><a name="p1985021110428"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.5.1.4 "><p id="p1490014169318"><a name="p1490014169318"></a><a name="p1490014169318"></a>Specifies the information about a DR drill.</p>
    <p id="p1385031174212"><a name="p1385031174212"></a><a name="p1385031174212"></a>For details, see <a href="#table920673314542">Table 1</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  1** **disaster\_recovery\_dril**  field description

    <a name="table920673314542"></a>
    <table><thead align="left"><tr id="row1320623313547"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p162061733155416"><a name="p162061733155416"></a><a name="p162061733155416"></a><strong id="b15931757113514"><a name="b15931757113514"></a><a name="b15931757113514"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.2.5.1.2"><p id="p1820613311541"><a name="p1820613311541"></a><a name="p1820613311541"></a><strong id="b390515863511"><a name="b390515863511"></a><a name="b390515863511"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.91%" id="mcps1.2.5.1.3"><p id="p17206143375412"><a name="p17206143375412"></a><a name="p17206143375412"></a><strong id="b84235270615453_1"><a name="b84235270615453_1"></a><a name="b84235270615453_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="46.089999999999996%" id="mcps1.2.5.1.4"><p id="p14207193345412"><a name="p14207193345412"></a><a name="p14207193345412"></a><strong id="b7945145973515"><a name="b7945145973515"></a><a name="b7945145973515"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row122071033105418"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p1120719339543"><a name="p1120719339543"></a><a name="p1120719339543"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.2.5.1.2 "><p id="p7207103355415"><a name="p7207103355415"></a><a name="p7207103355415"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.91%" headers="mcps1.2.5.1.3 "><p id="p112071633145415"><a name="p112071633145415"></a><a name="p112071633145415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46.089999999999996%" headers="mcps1.2.5.1.4 "><p id="p686715461316"><a name="p686715461316"></a><a name="p686715461316"></a>Specifies the DR drill name.</p>
    <a name="ul8402195483111"></a><a name="ul8402195483111"></a><ul id="ul8402195483111"><li>The name can contain a maximum of 64 bytes.</li><li>The value can contain only letters (a to z and A to Z), digits (0 to 9), decimal points (.), underscores (_), and hyphens (-).</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    PUT https://\{Endpoint\}/v1/\{project\_id\}/disaster-recovery-drills/e472d26f-9624-42fb-8bfc-717d4714c225

    ```
    {    
          "disaster_recovery_drill": {   
              "name": "new_dr_drill_name" 
          }   
      }
    ```


## Response<a name="section151401222173512"></a>

-   Parameter description

    <a name="table1091191716422"></a>
    <table><thead align="left"><tr id="row591121724218"><th class="cellrowborder" valign="top" width="29.07%" id="mcps1.1.4.1.1"><p id="p58971710428"><a name="p58971710428"></a><a name="p58971710428"></a><strong id="b842352706151210"><a name="b842352706151210"></a><a name="b842352706151210"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.44%" id="mcps1.1.4.1.2"><p id="p691131744213"><a name="p691131744213"></a><a name="p691131744213"></a><strong id="b84235270615453_2"><a name="b84235270615453_2"></a><a name="b84235270615453_2"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.49%" id="mcps1.1.4.1.3"><p id="p109113175422"><a name="p109113175422"></a><a name="p109113175422"></a><strong id="b84235270615457_2"><a name="b84235270615457_2"></a><a name="b84235270615457_2"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row7912017144215"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.1.4.1.1 "><p id="p4911717164215"><a name="p4911717164215"></a><a name="p4911717164215"></a>disaster_recovery_drill</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.1.4.1.2 "><p id="p291817154212"><a name="p291817154212"></a><a name="p291817154212"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.1.4.1.3 "><p id="p169161715424"><a name="p169161715424"></a><a name="p169161715424"></a>Specifies the information about a DR drill.</p>
    <p id="p19416934171"><a name="p19416934171"></a><a name="p19416934171"></a>For details, see <a href="#table12967181813422">Table 2</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2** **disaster\_recovery\_drill**  field description

    <a name="table12967181813422"></a>
    <table><thead align="left"><tr id="row996431844217"><th class="cellrowborder" valign="top" width="29.07%" id="mcps1.2.4.1.1"><p id="p1964181864212"><a name="p1964181864212"></a><a name="p1964181864212"></a><strong id="b842352706151210_1"><a name="b842352706151210_1"></a><a name="b842352706151210_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.44%" id="mcps1.2.4.1.2"><p id="p11964171813427"><a name="p11964171813427"></a><a name="p11964171813427"></a><strong id="b84235270615453_3"><a name="b84235270615453_3"></a><a name="b84235270615453_3"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.49%" id="mcps1.2.4.1.3"><p id="p1496411854218"><a name="p1496411854218"></a><a name="p1496411854218"></a><strong id="b84235270615457_3"><a name="b84235270615457_3"></a><a name="b84235270615457_3"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3964101844210"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p10964141810428"><a name="p10964141810428"></a><a name="p10964141810428"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p18964218154214"><a name="p18964218154214"></a><a name="p18964218154214"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p1496415181427"><a name="p1496415181427"></a><a name="p1496415181427"></a>Specifies the DR drill ID.</p>
    </td>
    </tr>
    <tr id="row89657183423"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p396416182426"><a name="p396416182426"></a><a name="p396416182426"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p159643187427"><a name="p159643187427"></a><a name="p159643187427"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p196511182424"><a name="p196511182424"></a><a name="p196511182424"></a>Specifies the DR drill name. Specifies the name of a DR drill. The name can contain a maximum of 64 bytes. The value can contain only letters (a to z and A to Z), digits (0 to 9), decimal points (.), underscores (_), and hyphens (-).</p>
    </td>
    </tr>
    <tr id="row4965201817423"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p11965111844220"><a name="p11965111844220"></a><a name="p11965111844220"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p17965151817429"><a name="p17965151817429"></a><a name="p17965151817429"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p396517188428"><a name="p396517188428"></a><a name="p396517188428"></a>Specifies the DR drill status.</p>
    <p id="p1502102110589"><a name="p1502102110589"></a><a name="p1502102110589"></a>For details, see <a href="dr-drill-status.md">DR Drill Status</a>.</p>
    </td>
    </tr>
    <tr id="row17965141834215"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p7965818184220"><a name="p7965818184220"></a><a name="p7965818184220"></a>drill_vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p169651318134220"><a name="p169651318134220"></a><a name="p169651318134220"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p1296501816428"><a name="p1296501816428"></a><a name="p1296501816428"></a>Specifies the ID of the VPC used for a DR drill.</p>
    </td>
    </tr>
    <tr id="row99651118204212"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p13965201813425"><a name="p13965201813425"></a><a name="p13965201813425"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p196581815428"><a name="p196581815428"></a><a name="p196581815428"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p1496551812422"><a name="p1496551812422"></a><a name="p1496551812422"></a>Specifies the time when a DR drill was created.</p>
    <p id="p693611475818"><a name="p693611475818"></a><a name="p693611475818"></a>The default format is as follows: "yyyy-MM-dd HH:mm:ss.SSS", for example, <strong id="b15465131813620"><a name="b15465131813620"></a><a name="b15465131813620"></a>2019-04-01 12:00:00.000</strong>.</p>
    </td>
    </tr>
    <tr id="row17965418184219"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p139651918124216"><a name="p139651918124216"></a><a name="p139651918124216"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p596581813421"><a name="p596581813421"></a><a name="p596581813421"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p39651018154210"><a name="p39651018154210"></a><a name="p39651018154210"></a>Specifies the time when a DR drill was updated.</p>
    <p id="p14372548407"><a name="p14372548407"></a><a name="p14372548407"></a>The default format is as follows: "yyyy-MM-dd HH:mm:ss.SSS", for example, <strong id="b88901425103617"><a name="b88901425103617"></a><a name="b88901425103617"></a>2019-04-01 12:00:00.000</strong>.</p>
    </td>
    </tr>
    <tr id="row496711874219"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p119657184423"><a name="p119657184423"></a><a name="p119657184423"></a>server_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p296751814212"><a name="p296751814212"></a><a name="p296751814212"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p496716185421"><a name="p496716185421"></a><a name="p496716185421"></a>Specifies the ID of a protection group.</p>
    </td>
    </tr>
    <tr id="row4967191804215"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p14967181813426"><a name="p14967181813426"></a><a name="p14967181813426"></a>drill_servers</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p16967131811427"><a name="p16967131811427"></a><a name="p16967131811427"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p119671518194215"><a name="p119671518194215"></a><a name="p119671518194215"></a>Specifies the drill servers.</p>
    <p id="p17111727387"><a name="p17111727387"></a><a name="p17111727387"></a>For details, see <a href="#table10595165111719">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3** **drill\_servers**  field description

    <a name="table10595165111719"></a>
    <table><thead align="left"><tr id="row25945515710"><th class="cellrowborder" valign="top" width="29.07%" id="mcps1.2.4.1.1"><p id="p559415110716"><a name="p559415110716"></a><a name="p559415110716"></a><strong id="b842352706151210_2"><a name="b842352706151210_2"></a><a name="b842352706151210_2"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.44%" id="mcps1.2.4.1.2"><p id="p9594185114710"><a name="p9594185114710"></a><a name="p9594185114710"></a><strong id="b84235270615453_4"><a name="b84235270615453_4"></a><a name="b84235270615453_4"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.49%" id="mcps1.2.4.1.3"><p id="p5594951877"><a name="p5594951877"></a><a name="p5594951877"></a><strong id="b84235270615457_4"><a name="b84235270615457_4"></a><a name="b84235270615457_4"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1259511515717"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p5595051675"><a name="p5595051675"></a><a name="p5595051675"></a>protected_instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p14595175114711"><a name="p14595175114711"></a><a name="p14595175114711"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p2595125120718"><a name="p2595125120718"></a><a name="p2595125120718"></a>Specifies the protected instance ID of the drill server.</p>
    </td>
    </tr>
    <tr id="row859515117710"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p145951517715"><a name="p145951517715"></a><a name="p145951517715"></a>drill_server_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p65951511876"><a name="p65951511876"></a><a name="p65951511876"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p1959515118718"><a name="p1959515118718"></a><a name="p1959515118718"></a>Specifies the drill server ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    {  
          "disaster_recovery_drill":  
             { 
                 "id": "e472d26f-9624-42fb-8bfc-717d4714c225",
                "name": "new_dr_drill_name",
                "status": "available",
                "server_group_id": "c2aee29a-2959-4d01-9755-01cc76a4d17d",
                "drill_vpc_id": "7881f1d2-1f41-419c-873a-14ac620bc46e",
                "created_at": "2018-07-18 06:41:58.681",
                "updated_at": "2018-07-18 00:41:14.677",
                "drill_servers": [
                    {
                        "protected_instance": "d08ca8d7-a784-41ae-b32a-c592943f5dfc",
                        "drill_server_id": "9de0439a-4ee4-4199-919a-44afd20952dc"
                    },
                    {
                        "protected_instance": "ea308e8b-043c-4fc6-a53c-856eae137b13",
                        "drill_server_id": "3eaa1c70-9719-4eb5-b577-cb92ddbffd03"
                    }
                ]
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


## **Returned Value**<a name="section019272213513"></a>

-   Normal

    <a name="table13195172211353"></a>
    <table><thead align="left"><tr id="row48315223355"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p12831182283510"><a name="p12831182283510"></a><a name="p12831182283510"></a><strong id="b842352706175024_1"><a name="b842352706175024_1"></a><a name="b842352706175024_1"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p1583152219355"><a name="p1583152219355"></a><a name="p1583152219355"></a><strong id="b84235270615457_5"><a name="b84235270615457_5"></a><a name="b84235270615457_5"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1283119227359"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p6831222173518"><a name="p6831222173518"></a><a name="p6831222173518"></a>200</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p14831112211359"><a name="p14831112211359"></a><a name="p14831112211359"></a>The server has accepted the request.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    <a name="table101981922113512"></a>
    <table><thead align="left"><tr id="row1283152283510"><th class="cellrowborder" valign="top" width="43.43%" id="mcps1.1.3.1.1"><p id="p8831182283519"><a name="p8831182283519"></a><a name="p8831182283519"></a><strong id="b842352706175024_2"><a name="b842352706175024_2"></a><a name="b842352706175024_2"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="56.57%" id="mcps1.1.3.1.2"><p id="p1831182218356"><a name="p1831182218356"></a><a name="p1831182218356"></a><strong id="b84235270615457_6"><a name="b84235270615457_6"></a><a name="b84235270615457_6"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row783112217351"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p1283182218359"><a name="p1283182218359"></a><a name="p1283182218359"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p483172211350"><a name="p483172211350"></a><a name="p483172211350"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row1883462213359"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p13834182219352"><a name="p13834182219352"></a><a name="p13834182219352"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p1883472215356"><a name="p1883472215356"></a><a name="p1883472215356"></a>You must enter a username and the password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row1583414223357"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p58343224351"><a name="p58343224351"></a><a name="p58343224351"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p1834322143518"><a name="p1834322143518"></a><a name="p1834322143518"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row9834112211356"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p08341022183514"><a name="p08341022183514"></a><a name="p08341022183514"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p683412223510"><a name="p683412223510"></a><a name="p683412223510"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row19834122217352"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p683412243516"><a name="p683412243516"></a><a name="p683412243516"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p1483415224355"><a name="p1483415224355"></a><a name="p1483415224355"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row883432214355"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p168341322163519"><a name="p168341322163519"></a><a name="p168341322163519"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p5834422143512"><a name="p5834422143512"></a><a name="p5834422143512"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row128341422203514"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p1483422213517"><a name="p1483422213517"></a><a name="p1483422213517"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p138341822133520"><a name="p138341822133520"></a><a name="p138341822133520"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row683415226355"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p88348228356"><a name="p88348228356"></a><a name="p88348228356"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p12834152218355"><a name="p12834152218355"></a><a name="p12834152218355"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row183412228356"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p178347228359"><a name="p178347228359"></a><a name="p178347228359"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p11834152217358"><a name="p11834152217358"></a><a name="p11834152217358"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row17834102253510"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p28347227351"><a name="p28347227351"></a><a name="p28347227351"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p6834112233519"><a name="p6834112233519"></a><a name="p6834112233519"></a>Failed to complete the request because of a service error.</p>
    </td>
    </tr>
    <tr id="row128347228351"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p1283452263513"><a name="p1283452263513"></a><a name="p1283452263513"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p58341422163513"><a name="p58341422163513"></a><a name="p58341422163513"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row3834182217352"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p5834182273519"><a name="p5834182273519"></a><a name="p5834182273519"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p1583492212355"><a name="p1583492212355"></a><a name="p1583492212355"></a>Failed to complete the request because the server receives an invalid response from an upstream server.</p>
    </td>
    </tr>
    <tr id="row108341322133515"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p18341222173511"><a name="p18341222173511"></a><a name="p18341222173511"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p483462217357"><a name="p483462217357"></a><a name="p483462217357"></a>Failed to complete the request because the system is unavailable.</p>
    </td>
    </tr>
    <tr id="row9834172216357"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p8834142212354"><a name="p8834142212354"></a><a name="p8834142212354"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p13835122223510"><a name="p13835122223510"></a><a name="p13835122223510"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>



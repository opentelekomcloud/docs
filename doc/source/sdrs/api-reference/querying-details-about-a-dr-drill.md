# Querying Details About a DR Drill<a name="sdrs_05_0704"></a>

## Function<a name="section5101722123513"></a>

This API is used to query the details about a DR drill.

## Constraints and Limitations<a name="section71092211351"></a>

None

## URI<a name="section71072283515"></a>

-   URI format

    GET /v1/\{project\_id\}/disaster-recovery-drills/\{disaster\_recovery\_drill\_id\}

-   Parameter description

    <a name="table161302217358"></a>
    <table><thead align="left"><tr id="row682032216357"><th class="cellrowborder" valign="top" width="32.32%" id="mcps1.1.4.1.1"><p id="p1282022210353"><a name="p1282022210353"></a><a name="p1282022210353"></a><strong id="b84235270615443"><a name="b84235270615443"></a><a name="b84235270615443"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.169999999999998%" id="mcps1.1.4.1.2"><p id="p13820622133515"><a name="p13820622133515"></a><a name="p13820622133515"></a><strong id="b84235270615447"><a name="b84235270615447"></a><a name="b84235270615447"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.51%" id="mcps1.1.4.1.3"><p id="p138201122123514"><a name="p138201122123514"></a><a name="p138201122123514"></a><strong id="b84235270615457"><a name="b84235270615457"></a><a name="b84235270615457"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row98201722143512"><td class="cellrowborder" valign="top" width="32.32%" headers="mcps1.1.4.1.1 "><p id="p68205222355"><a name="p68205222355"></a><a name="p68205222355"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.1.4.1.2 "><p id="p482062214357"><a name="p482062214357"></a><a name="p482062214357"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.51%" headers="mcps1.1.4.1.3 "><p id="p20820162219355"><a name="p20820162219355"></a><a name="p20820162219355"></a>Specifies the project ID.</p>
    </td>
    </tr>
    <tr id="row12820122263510"><td class="cellrowborder" valign="top" width="32.32%" headers="mcps1.1.4.1.1 "><p id="p15820122263513"><a name="p15820122263513"></a><a name="p15820122263513"></a>disaster_recovery_drill_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.1.4.1.2 "><p id="p7820142213517"><a name="p7820142213517"></a><a name="p7820142213517"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.51%" headers="mcps1.1.4.1.3 "><p id="p6820112293511"><a name="p6820112293511"></a><a name="p6820112293511"></a>Specifies the DR drill ID.</p>
    <p id="p12992142133810"><a name="p12992142133810"></a><a name="p12992142133810"></a>To query details, see <a href="querying-dr-drills.md">Querying DR Drills</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section19237224357"></a>

-   Request parameters

    None

-   Example request

    GET https://\{Endpoint\}/v1/\{project\_id\}/disaster-recovery-drills/e472d26f-9624-42fb-8bfc-717d4714c225


## Response<a name="section223162283516"></a>

-   Parameter description

    <a name="table12331122133512"></a>
    <table><thead align="left"><tr id="row1382082217355"><th class="cellrowborder" valign="top" width="29.07%" id="mcps1.1.4.1.1"><p id="p5820822113517"><a name="p5820822113517"></a><a name="p5820822113517"></a><strong id="b842352706151210"><a name="b842352706151210"></a><a name="b842352706151210"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.44%" id="mcps1.1.4.1.2"><p id="p17820162203519"><a name="p17820162203519"></a><a name="p17820162203519"></a><strong id="b84235270615453"><a name="b84235270615453"></a><a name="b84235270615453"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.49%" id="mcps1.1.4.1.3"><p id="p1482016225358"><a name="p1482016225358"></a><a name="p1482016225358"></a><strong id="b84235270615457_1"><a name="b84235270615457_1"></a><a name="b84235270615457_1"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1282012263513"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.1.4.1.1 "><p id="p182886316324"><a name="p182886316324"></a><a name="p182886316324"></a>disaster_recovery_drill</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.1.4.1.2 "><p id="p682010221356"><a name="p682010221356"></a><a name="p682010221356"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.1.4.1.3 "><p id="p148206225358"><a name="p148206225358"></a><a name="p148206225358"></a>Specifies the information about a DR drill.</p>
    <p id="p922205918411"><a name="p922205918411"></a><a name="p922205918411"></a>For details, see <a href="#table1540192213355">Table 1</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  1** **disaster\_recovery\_drill**  field description

    <a name="table1540192213355"></a>
    <table><thead align="left"><tr id="row28210229357"><th class="cellrowborder" valign="top" width="29.07%" id="mcps1.2.4.1.1"><p id="p14821622113510"><a name="p14821622113510"></a><a name="p14821622113510"></a><strong id="b842352706151210_1"><a name="b842352706151210_1"></a><a name="b842352706151210_1"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.44%" id="mcps1.2.4.1.2"><p id="p7821102293514"><a name="p7821102293514"></a><a name="p7821102293514"></a><strong id="b84235270615453_1"><a name="b84235270615453_1"></a><a name="b84235270615453_1"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.49%" id="mcps1.2.4.1.3"><p id="p6821122212359"><a name="p6821122212359"></a><a name="p6821122212359"></a><strong id="b84235270615457_2"><a name="b84235270615457_2"></a><a name="b84235270615457_2"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row482111222359"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p6821152233514"><a name="p6821152233514"></a><a name="p6821152233514"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p15821822173516"><a name="p15821822173516"></a><a name="p15821822173516"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p188211227358"><a name="p188211227358"></a><a name="p188211227358"></a>Specifies the DR drill ID.</p>
    </td>
    </tr>
    <tr id="row682117227355"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p182118228354"><a name="p182118228354"></a><a name="p182118228354"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p11821922123519"><a name="p11821922123519"></a><a name="p11821922123519"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p282122215357"><a name="p282122215357"></a><a name="p282122215357"></a>Specifies the DR drill name.</p>
    </td>
    </tr>
    <tr id="row8821922123517"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1082132213352"><a name="p1082132213352"></a><a name="p1082132213352"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p882111224359"><a name="p882111224359"></a><a name="p882111224359"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p2821722183515"><a name="p2821722183515"></a><a name="p2821722183515"></a>Specifies the DR drill status. For details, see <a href="dr-drill-status.md">DR Drill Status</a>.</p>
    </td>
    </tr>
    <tr id="row17821822153516"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p9821922143516"><a name="p9821922143516"></a><a name="p9821922143516"></a>drill_vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p7821152203517"><a name="p7821152203517"></a><a name="p7821152203517"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p9821102211354"><a name="p9821102211354"></a><a name="p9821102211354"></a>Specifies the ID of the VPC used for a DR drill.</p>
    </td>
    </tr>
    <tr id="row982152216351"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p158211922153515"><a name="p158211922153515"></a><a name="p158211922153515"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p6821622173515"><a name="p6821622173515"></a><a name="p6821622173515"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p8821102283512"><a name="p8821102283512"></a><a name="p8821102283512"></a>Specifies the time when a DR drill was created.</p>
    <p id="p136073351516"><a name="p136073351516"></a><a name="p136073351516"></a>The default format is as follows: "yyyy-MM-dd HH:mm:ss.SSS", for example, <strong id="b764420107351"><a name="b764420107351"></a><a name="b764420107351"></a>2019-04-01 12:00:00.000</strong>.</p>
    </td>
    </tr>
    <tr id="row15821182220351"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p9821922143510"><a name="p9821922143510"></a><a name="p9821922143510"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p15821222113515"><a name="p15821222113515"></a><a name="p15821222113515"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p1282162214358"><a name="p1282162214358"></a><a name="p1282162214358"></a>Specifies the time when a DR drill was updated.</p>
    <p id="p351861705213"><a name="p351861705213"></a><a name="p351861705213"></a>The default format is as follows: "yyyy-MM-dd HH:mm:ss.SSS", for example, <strong id="b208731712193518"><a name="b208731712193518"></a><a name="b208731712193518"></a>2019-04-01 12:00:00.000</strong>.</p>
    </td>
    </tr>
    <tr id="row20821142243517"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p08214221355"><a name="p08214221355"></a><a name="p08214221355"></a>server_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p1782192218350"><a name="p1782192218350"></a><a name="p1782192218350"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p19823132293516"><a name="p19823132293516"></a><a name="p19823132293516"></a>Specifies the ID of a protection group.</p>
    </td>
    </tr>
    <tr id="row08233224356"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p4823122113512"><a name="p4823122113512"></a><a name="p4823122113512"></a>drill_servers</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p9823192273511"><a name="p9823192273511"></a><a name="p9823192273511"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p382392213353"><a name="p382392213353"></a><a name="p382392213353"></a>Specifies the drill servers.</p>
    <p id="p1962813489610"><a name="p1962813489610"></a><a name="p1962813489610"></a>For details, see <a href="#table469122153514">Table 2</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2** **drill\_servers**  field description

    <a name="table469122153514"></a>
    <table><thead align="left"><tr id="row1882392243513"><th class="cellrowborder" valign="top" width="29.07%" id="mcps1.2.4.1.1"><p id="p158231222203517"><a name="p158231222203517"></a><a name="p158231222203517"></a><strong id="b842352706151210_2"><a name="b842352706151210_2"></a><a name="b842352706151210_2"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.44%" id="mcps1.2.4.1.2"><p id="p782392233520"><a name="p782392233520"></a><a name="p782392233520"></a><strong id="b84235270615453_2"><a name="b84235270615453_2"></a><a name="b84235270615453_2"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.49%" id="mcps1.2.4.1.3"><p id="p1382319222352"><a name="p1382319222352"></a><a name="p1382319222352"></a><strong id="b84235270615457_3"><a name="b84235270615457_3"></a><a name="b84235270615457_3"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row9823822193514"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p0823132218357"><a name="p0823132218357"></a><a name="p0823132218357"></a>protected_instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p1082311222351"><a name="p1082311222351"></a><a name="p1082311222351"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p16823102211353"><a name="p16823102211353"></a><a name="p16823102211353"></a>Specifies the protected instance ID of the drill server.</p>
    </td>
    </tr>
    <tr id="row1182352253516"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p882322215359"><a name="p882322215359"></a><a name="p882322215359"></a>drill_server_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p4823132233514"><a name="p4823132233514"></a><a name="p4823132233514"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p10823172293510"><a name="p10823172293510"></a><a name="p10823172293510"></a>Specifies the drill server ID.</p>
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
                "name": "dr_drill_test",
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


## **Returned Value**<a name="section581132243517"></a>

-   Normal

    <a name="table78382212351"></a>
    <table><thead align="left"><tr id="row158246226359"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p382442253510"><a name="p382442253510"></a><a name="p382442253510"></a><strong id="b842352706175024_1"><a name="b842352706175024_1"></a><a name="b842352706175024_1"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p9824152216354"><a name="p9824152216354"></a><a name="p9824152216354"></a><strong id="b84235270615457_4"><a name="b84235270615457_4"></a><a name="b84235270615457_4"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row16824132214354"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p12824172203511"><a name="p12824172203511"></a><a name="p12824172203511"></a>200</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p1782472243510"><a name="p1782472243510"></a><a name="p1782472243510"></a>The server has accepted the request.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    <a name="table68722283512"></a>
    <table><thead align="left"><tr id="row13824822163516"><th class="cellrowborder" valign="top" width="43.43%" id="mcps1.1.3.1.1"><p id="p88241022203518"><a name="p88241022203518"></a><a name="p88241022203518"></a><strong id="b842352706175024_2"><a name="b842352706175024_2"></a><a name="b842352706175024_2"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="56.57%" id="mcps1.1.3.1.2"><p id="p14824122216350"><a name="p14824122216350"></a><a name="p14824122216350"></a><strong id="b84235270615457_5"><a name="b84235270615457_5"></a><a name="b84235270615457_5"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row0824132215356"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p17824182213517"><a name="p17824182213517"></a><a name="p17824182213517"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p10824142214353"><a name="p10824142214353"></a><a name="p10824142214353"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row158241226358"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p17824182243512"><a name="p17824182243512"></a><a name="p17824182243512"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p58241722163520"><a name="p58241722163520"></a><a name="p58241722163520"></a>You must enter a username and the password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row19824112293513"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p138242221355"><a name="p138242221355"></a><a name="p138242221355"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p108241224352"><a name="p108241224352"></a><a name="p108241224352"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row782472293517"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p15824122213350"><a name="p15824122213350"></a><a name="p15824122213350"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p128241722143513"><a name="p128241722143513"></a><a name="p128241722143513"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row15824622163510"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p1482442293519"><a name="p1482442293519"></a><a name="p1482442293519"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p17824172219359"><a name="p17824172219359"></a><a name="p17824172219359"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row2082422253518"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p782472210351"><a name="p782472210351"></a><a name="p782472210351"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p9824172214359"><a name="p9824172214359"></a><a name="p9824172214359"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row9824192203519"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p1682410228356"><a name="p1682410228356"></a><a name="p1682410228356"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p7824022143514"><a name="p7824022143514"></a><a name="p7824022143514"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row1582414227354"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p582416229352"><a name="p582416229352"></a><a name="p582416229352"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p4824422183518"><a name="p4824422183518"></a><a name="p4824422183518"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row782472214352"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p15824122213354"><a name="p15824122213354"></a><a name="p15824122213354"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p68241922143512"><a name="p68241922143512"></a><a name="p68241922143512"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row2082412293514"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p118241221357"><a name="p118241221357"></a><a name="p118241221357"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p18824142219358"><a name="p18824142219358"></a><a name="p18824142219358"></a>Failed to complete the request because of a service error.</p>
    </td>
    </tr>
    <tr id="row12824122211357"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p6824182219352"><a name="p6824182219352"></a><a name="p6824182219352"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p19824152212352"><a name="p19824152212352"></a><a name="p19824152212352"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row14824142213519"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p12824132215355"><a name="p12824132215355"></a><a name="p12824132215355"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p128241922153512"><a name="p128241922153512"></a><a name="p128241922153512"></a>Failed to complete the request because the server receives an invalid response from an upstream server.</p>
    </td>
    </tr>
    <tr id="row1382413225359"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p2082452219354"><a name="p2082452219354"></a><a name="p2082452219354"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p28241722143511"><a name="p28241722143511"></a><a name="p28241722143511"></a>Failed to complete the request because the system is unavailable.</p>
    </td>
    </tr>
    <tr id="row48246223350"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p78246228355"><a name="p78246228355"></a><a name="p78246228355"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p168241922133515"><a name="p168241922133515"></a><a name="p168241922133515"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>



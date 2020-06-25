# Querying DR Drills<a name="sdrs_05_0703"></a>

## Function<a name="section778722103515"></a>

This API is used to query all DR drills in a specified protection group. If you do not specify the protection group, the system lists all the DR drills of the tenant.

## Constraints and Limitations<a name="section578752118358"></a>

None

## URI<a name="section1478822113513"></a>

-   URI format

    GET /v1/\{project\_id\}/disaster-recovery-drills

-   Parameter description

    <a name="table979182173511"></a>
    <table><thead align="left"><tr id="row148131622173515"><th class="cellrowborder" valign="top" width="17.528247175282473%" id="mcps1.1.5.1.1"><p id="p2813132253518"><a name="p2813132253518"></a><a name="p2813132253518"></a><strong id="b84235270615443"><a name="b84235270615443"></a><a name="b84235270615443"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.528247175282473%" id="mcps1.1.5.1.2"><p id="p281362215352"><a name="p281362215352"></a><a name="p281362215352"></a><strong id="b84235270615447"><a name="b84235270615447"></a><a name="b84235270615447"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.428557144285573%" id="mcps1.1.5.1.3"><p id="p1081332263518"><a name="p1081332263518"></a><a name="p1081332263518"></a><strong id="b84235270615453"><a name="b84235270615453"></a><a name="b84235270615453"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="50.51494850514948%" id="mcps1.1.5.1.4"><p id="p19813142220351"><a name="p19813142220351"></a><a name="p19813142220351"></a><strong id="b84235270615457"><a name="b84235270615457"></a><a name="b84235270615457"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row581312226353"><td class="cellrowborder" valign="top" width="17.528247175282473%" headers="mcps1.1.5.1.1 "><p id="p1813172263520"><a name="p1813172263520"></a><a name="p1813172263520"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.528247175282473%" headers="mcps1.1.5.1.2 "><p id="p78131822193520"><a name="p78131822193520"></a><a name="p78131822193520"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.428557144285573%" headers="mcps1.1.5.1.3 "><p id="p38131122183510"><a name="p38131122183510"></a><a name="p38131122183510"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="50.51494850514948%" headers="mcps1.1.5.1.4 "><p id="p081332213352"><a name="p081332213352"></a><a name="p081332213352"></a>Specifies the project ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   **Request filter**  field description

    <a name="table136481148235"></a>
    <table><thead align="left"><tr id="row1964611148237"><th class="cellrowborder" valign="top" width="25%" id="mcps1.1.5.1.1"><p id="p16646161412313"><a name="p16646161412313"></a><a name="p16646161412313"></a><strong id="b317842268"><a name="b317842268"></a><a name="b317842268"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="14.000000000000002%" id="mcps1.1.5.1.2"><p id="p1164610141234"><a name="p1164610141234"></a><a name="p1164610141234"></a><strong id="b1626023206"><a name="b1626023206"></a><a name="b1626023206"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="15%" id="mcps1.1.5.1.3"><p id="p86461214202317"><a name="p86461214202317"></a><a name="p86461214202317"></a><strong id="b1865430743"><a name="b1865430743"></a><a name="b1865430743"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="46%" id="mcps1.1.5.1.4"><p id="p3646111412237"><a name="p3646111412237"></a><a name="p3646111412237"></a><strong id="b123490740"><a name="b123490740"></a><a name="b123490740"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row7646111462318"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p164691416237"><a name="p164691416237"></a><a name="p164691416237"></a>server_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.2 "><p id="p6646131411233"><a name="p6646131411233"></a><a name="p6646131411233"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.3 "><p id="p96462014202314"><a name="p96462014202314"></a><a name="p96462014202314"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.5.1.4 "><p id="p5646914172319"><a name="p5646914172319"></a><a name="p5646914172319"></a>Specifies the ID of a protection group.</p>
    <p id="p5313954812"><a name="p5313954812"></a><a name="p5313954812"></a>For details, see <a href="querying-protection-groups.md">Querying Protection Groups</a>.</p>
    </td>
    </tr>
    <tr id="row14647181422313"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p19646101410237"><a name="p19646101410237"></a><a name="p19646101410237"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.2 "><p id="p20646141482315"><a name="p20646141482315"></a><a name="p20646141482315"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.3 "><p id="p96469140238"><a name="p96469140238"></a><a name="p96469140238"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.5.1.4 "><p id="p164701482319"><a name="p164701482319"></a><a name="p164701482319"></a>Specifies the DR drill name. Fuzzy search is supported.</p>
    </td>
    </tr>
    <tr id="row964781412317"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p1364716149233"><a name="p1364716149233"></a><a name="p1364716149233"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.2 "><p id="p4647114182312"><a name="p4647114182312"></a><a name="p4647114182312"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.3 "><p id="p18647141442317"><a name="p18647141442317"></a><a name="p18647141442317"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.5.1.4 "><p id="p7647151482318"><a name="p7647151482318"></a><a name="p7647151482318"></a>Specifies the DR drill status.</p>
    <p id="p2194153619493"><a name="p2194153619493"></a><a name="p2194153619493"></a>For details, see <a href="dr-drill-status.md">DR Drill Status</a>.</p>
    </td>
    </tr>
    <tr id="row26471314102313"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p10647914142314"><a name="p10647914142314"></a><a name="p10647914142314"></a>drill_vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.2 "><p id="p164717144233"><a name="p164717144233"></a><a name="p164717144233"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.3 "><p id="p66476149235"><a name="p66476149235"></a><a name="p66476149235"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.5.1.4 "><p id="p764712147235"><a name="p764712147235"></a><a name="p764712147235"></a>Specifies the ID of the VPC used for a DR drill.</p>
    </td>
    </tr>
    <tr id="row8647314102313"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p26471814122310"><a name="p26471814122310"></a><a name="p26471814122310"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.2 "><p id="p964761452315"><a name="p964761452315"></a><a name="p964761452315"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.3 "><p id="p1864761442310"><a name="p1864761442310"></a><a name="p1864761442310"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.5.1.4 "><p id="p168455995811"><a name="p168455995811"></a><a name="p168455995811"></a>Specifies the maximum number of results returned each time. The value is a positive integer from 0 to 1000. The default value is <strong id="b842352706161435"><a name="b842352706161435"></a><a name="b842352706161435"></a>1000</strong>.</p>
    </td>
    </tr>
    <tr id="row564818148231"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.5.1.1 "><p id="p36471414122314"><a name="p36471414122314"></a><a name="p36471414122314"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.000000000000002%" headers="mcps1.1.5.1.2 "><p id="p1664771482310"><a name="p1664771482310"></a><a name="p1664771482310"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.5.1.3 "><p id="p1648171472319"><a name="p1648171472319"></a><a name="p1648171472319"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.5.1.4 "><p id="p2648201462319"><a name="p2648201462319"></a><a name="p2648201462319"></a>Specifies the offset of each request. The default value is <strong id="b74201644142916"><a name="b74201644142916"></a><a name="b74201644142916"></a>0</strong>. The value must be a number and cannot be negative.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section118509155316"></a>

-   Request parameters

    None

-   Example request

    GET https://\{Endpoint\}/v1/\{project\_id\}/disaster-recovery-drills


## Response<a name="section11837142115358"></a>

-   Parameter description

    <a name="table12856421203510"></a>
    <table><thead align="left"><tr id="row3815172218357"><th class="cellrowborder" valign="top" width="29.07%" id="mcps1.1.4.1.1"><p id="p1381517225355"><a name="p1381517225355"></a><a name="p1381517225355"></a><strong id="b842352706151210"><a name="b842352706151210"></a><a name="b842352706151210"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.44%" id="mcps1.1.4.1.2"><p id="p8815132253512"><a name="p8815132253512"></a><a name="p8815132253512"></a><strong id="b2135923967"><a name="b2135923967"></a><a name="b2135923967"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.49%" id="mcps1.1.4.1.3"><p id="p781532243513"><a name="p781532243513"></a><a name="p781532243513"></a><strong id="b46304009"><a name="b46304009"></a><a name="b46304009"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row18815322123513"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.1.4.1.1 "><p id="p63741048153010"><a name="p63741048153010"></a><a name="p63741048153010"></a>disaster_recovery_drills</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.1.4.1.2 "><p id="p10815132233511"><a name="p10815132233511"></a><a name="p10815132233511"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.1.4.1.3 "><p id="p881562243512"><a name="p881562243512"></a><a name="p881562243512"></a>Specifies the DR drills.</p>
    <p id="p16579547331"><a name="p16579547331"></a><a name="p16579547331"></a>For details, see <a href="#table687013217358">Table 1</a>.</p>
    </td>
    </tr>
    <tr id="row08151122193517"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.1.4.1.1 "><p id="p581542293513"><a name="p581542293513"></a><a name="p581542293513"></a>count</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.1.4.1.2 "><p id="p18815322113517"><a name="p18815322113517"></a><a name="p18815322113517"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.1.4.1.3 "><p id="p18815142219355"><a name="p18815142219355"></a><a name="p18815142219355"></a>Specifies the number of DR drills.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  1** **disaster\_recovery\_drills**  field description

    <a name="table687013217358"></a>
    <table><thead align="left"><tr id="row58152224359"><th class="cellrowborder" valign="top" width="29.07%" id="mcps1.2.4.1.1"><p id="p381542263514"><a name="p381542263514"></a><a name="p381542263514"></a><strong id="b868335053"><a name="b868335053"></a><a name="b868335053"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.44%" id="mcps1.2.4.1.2"><p id="p781519229359"><a name="p781519229359"></a><a name="p781519229359"></a><strong id="b665028524"><a name="b665028524"></a><a name="b665028524"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.49%" id="mcps1.2.4.1.3"><p id="p881532219350"><a name="p881532219350"></a><a name="p881532219350"></a><strong id="b1091063929"><a name="b1091063929"></a><a name="b1091063929"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row11815182213353"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p5815192253519"><a name="p5815192253519"></a><a name="p5815192253519"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p17816172218355"><a name="p17816172218355"></a><a name="p17816172218355"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p381611221355"><a name="p381611221355"></a><a name="p381611221355"></a>Specifies the DR drill ID.</p>
    </td>
    </tr>
    <tr id="row1281692214358"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p481618223353"><a name="p481618223353"></a><a name="p481618223353"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p081622212355"><a name="p081622212355"></a><a name="p081622212355"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p178168220357"><a name="p178168220357"></a><a name="p178168220357"></a>Specifies the DR drill name.</p>
    </td>
    </tr>
    <tr id="row5816122210357"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p4816142217357"><a name="p4816142217357"></a><a name="p4816142217357"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p1281652283516"><a name="p1281652283516"></a><a name="p1281652283516"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p9816182233510"><a name="p9816182233510"></a><a name="p9816182233510"></a>Specifies the DR drill status. For details, see <a href="dr-drill-status.md">DR Drill Status</a>.</p>
    </td>
    </tr>
    <tr id="row11613744173412"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p15816102210353"><a name="p15816102210353"></a><a name="p15816102210353"></a>server_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p1281620222357"><a name="p1281620222357"></a><a name="p1281620222357"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p28164224351"><a name="p28164224351"></a><a name="p28164224351"></a>Specifies the ID of a protection group.</p>
    </td>
    </tr>
    <tr id="row281617220355"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p681652212354"><a name="p681652212354"></a><a name="p681652212354"></a>drill_vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p68166224355"><a name="p68166224355"></a><a name="p68166224355"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p881620224359"><a name="p881620224359"></a><a name="p881620224359"></a>Specifies the ID of the VPC used for a DR drill.</p>
    </td>
    </tr>
    <tr id="row1081622283516"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p1481615223355"><a name="p1481615223355"></a><a name="p1481615223355"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p08161522173511"><a name="p08161522173511"></a><a name="p08161522173511"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p981662283512"><a name="p981662283512"></a><a name="p981662283512"></a>Specifies the time when a DR drill was created.</p>
    <p id="p96037251917"><a name="p96037251917"></a><a name="p96037251917"></a>The default format is as follows: "yyyy-MM-dd HH:mm:ss.SSS", for example, <strong id="b11541162817347"><a name="b11541162817347"></a><a name="b11541162817347"></a>2019-04-01 12:00:00.000</strong>.</p>
    </td>
    </tr>
    <tr id="row381622212359"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p12816522173513"><a name="p12816522173513"></a><a name="p12816522173513"></a>updated_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p781672213512"><a name="p781672213512"></a><a name="p781672213512"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p178160225352"><a name="p178160225352"></a><a name="p178160225352"></a>Specifies the time when a DR drill was updated.</p>
    <p id="p20627853192"><a name="p20627853192"></a><a name="p20627853192"></a>The default format is as follows: "yyyy-MM-dd HH:mm:ss.SSS", for example, <strong id="b385193412341"><a name="b385193412341"></a><a name="b385193412341"></a>2019-04-01 12:00:00.000</strong>.</p>
    </td>
    </tr>
    <tr id="row381617220359"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p6816122219352"><a name="p6816122219352"></a><a name="p6816122219352"></a>drill_servers</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p881612211359"><a name="p881612211359"></a><a name="p881612211359"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p19816172220358"><a name="p19816172220358"></a><a name="p19816172220358"></a>Specifies the drill servers.</p>
    <p id="p16741135444"><a name="p16741135444"></a><a name="p16741135444"></a>For details, see <a href="#table898673912313">Table 2</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2** **drill\_servers**  field description

    <a name="table898673912313"></a>
    <table><thead align="left"><tr id="row1998523912313"><th class="cellrowborder" valign="top" width="29.07%" id="mcps1.2.4.1.1"><p id="p1198513394315"><a name="p1198513394315"></a><a name="p1198513394315"></a><strong id="b334345166"><a name="b334345166"></a><a name="b334345166"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="17.44%" id="mcps1.2.4.1.2"><p id="p1985839934"><a name="p1985839934"></a><a name="p1985839934"></a><strong id="b1751986888"><a name="b1751986888"></a><a name="b1751986888"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="53.49%" id="mcps1.2.4.1.3"><p id="p39851739733"><a name="p39851739733"></a><a name="p39851739733"></a><strong id="b1322689094"><a name="b1322689094"></a><a name="b1322689094"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row798643912316"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p89867391313"><a name="p89867391313"></a><a name="p89867391313"></a>protected_instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p39865391836"><a name="p39865391836"></a><a name="p39865391836"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p99861939932"><a name="p99861939932"></a><a name="p99861939932"></a>Specifies the protected instance ID of the drill server.</p>
    </td>
    </tr>
    <tr id="row1198615391339"><td class="cellrowborder" valign="top" width="29.07%" headers="mcps1.2.4.1.1 "><p id="p59866391237"><a name="p59866391237"></a><a name="p59866391237"></a>drill_server_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.44%" headers="mcps1.2.4.1.2 "><p id="p69862391638"><a name="p69862391638"></a><a name="p69862391638"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p998643912313"><a name="p998643912313"></a><a name="p998643912313"></a>Specifies the drill server ID.</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example response

    ```
    { 
         "count": 2,
         "disaster_recovery_drills": [
            {
                "id": "e472d26f-9624-42fb-8bfc-717d4714c225",
                "name": "dr_drill_test",
                "status": "available",
                "server_group_id": "c2aee29a-2959-4d01-9755-01cc76a4d17d",
                "drill_vpc_id": "7881f1d2-1f41-419c-873a-14ac620bc46e",
                "created_at": "2018-07-18 06:41:58.681",
                "updated_at": "2018-07-18 09:41:14.677",
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
            },
            {
                "id": "f96ac55f-35dd-4cc3-ba61-36c168900c99",
                "name": "drill_test",
                "status": "available",
                "server_group_id": "3a60f45d-cf5b-49f1-a05e-ddee78cb6eef",
                "drill_vpc_id": "ac784bd6-a79c-4def-9ff8-dc87940d5335",
                "created_at": "2018-07-17 22:38:21.111",
                "updated_at": "2018-07-17 22:47:54.845",
                "drill_servers": []
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


## **Returned Value**<a name="section897722112352"></a>

-   Normal

    <a name="table398016219357"></a>
    <table><thead align="left"><tr id="row1481842213516"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p2081822243510"><a name="p2081822243510"></a><a name="p2081822243510"></a><strong id="b1317832452"><a name="b1317832452"></a><a name="b1317832452"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p118187225354"><a name="p118187225354"></a><a name="p118187225354"></a><strong id="b1784892819"><a name="b1784892819"></a><a name="b1784892819"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6818112243517"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p8818112215352"><a name="p8818112215352"></a><a name="p8818112215352"></a>200</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p2081882211354"><a name="p2081882211354"></a><a name="p2081882211354"></a>The server has accepted the request.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    <a name="table698592133515"></a>
    <table><thead align="left"><tr id="row11818102223512"><th class="cellrowborder" valign="top" width="43.43%" id="mcps1.1.3.1.1"><p id="p15818192217351"><a name="p15818192217351"></a><a name="p15818192217351"></a><strong id="b118277695"><a name="b118277695"></a><a name="b118277695"></a>Returned Value</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="56.57%" id="mcps1.1.3.1.2"><p id="p1381892212354"><a name="p1381892212354"></a><a name="p1381892212354"></a><strong id="b1128450899"><a name="b1128450899"></a><a name="b1128450899"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row581842218356"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p16818102253513"><a name="p16818102253513"></a><a name="p16818102253513"></a>400 Bad Request</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p1181820228356"><a name="p1181820228356"></a><a name="p1181820228356"></a>The server failed to process the request.</p>
    </td>
    </tr>
    <tr id="row68181122143513"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p1481862243520"><a name="p1481862243520"></a><a name="p1481862243520"></a>401 Unauthorized</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p16818192243515"><a name="p16818192243515"></a><a name="p16818192243515"></a>You must enter a username and the password to access the requested page.</p>
    </td>
    </tr>
    <tr id="row1481810227356"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p58184223353"><a name="p58184223353"></a><a name="p58184223353"></a>403 Forbidden</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p981862253518"><a name="p981862253518"></a><a name="p981862253518"></a>You are forbidden to access the requested page.</p>
    </td>
    </tr>
    <tr id="row1981872213511"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p881814225357"><a name="p881814225357"></a><a name="p881814225357"></a>404 Not Found</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p11818202214353"><a name="p11818202214353"></a><a name="p11818202214353"></a>The server could not find the requested page.</p>
    </td>
    </tr>
    <tr id="row181822210353"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p081812213518"><a name="p081812213518"></a><a name="p081812213518"></a>405 Method Not Allowed</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p14819182243518"><a name="p14819182243518"></a><a name="p14819182243518"></a>You are not allowed to use the method specified in the request.</p>
    </td>
    </tr>
    <tr id="row6819192215352"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p1981912224359"><a name="p1981912224359"></a><a name="p1981912224359"></a>406 Not Acceptable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p17819202243511"><a name="p17819202243511"></a><a name="p17819202243511"></a>The response generated by the server could not be accepted by the client.</p>
    </td>
    </tr>
    <tr id="row98190222354"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p9819112218355"><a name="p9819112218355"></a><a name="p9819112218355"></a>407 Proxy Authentication Required</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p1819322143513"><a name="p1819322143513"></a><a name="p1819322143513"></a>You must use the proxy server for authentication so that the request can be processed.</p>
    </td>
    </tr>
    <tr id="row281917223358"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p381972203512"><a name="p381972203512"></a><a name="p381972203512"></a>408 Request Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p208198228358"><a name="p208198228358"></a><a name="p208198228358"></a>The request timed out.</p>
    </td>
    </tr>
    <tr id="row581992233511"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p78191322153512"><a name="p78191322153512"></a><a name="p78191322153512"></a>409 Conflict</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p10819192218355"><a name="p10819192218355"></a><a name="p10819192218355"></a>The request could not be processed due to a conflict.</p>
    </td>
    </tr>
    <tr id="row178191822163517"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p681913226357"><a name="p681913226357"></a><a name="p681913226357"></a>500 Internal Server Error</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p18191022133511"><a name="p18191022133511"></a><a name="p18191022133511"></a>Failed to complete the request because of a service error.</p>
    </td>
    </tr>
    <tr id="row5819522193519"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p981932283510"><a name="p981932283510"></a><a name="p981932283510"></a>501 Not Implemented</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p14819522103517"><a name="p14819522103517"></a><a name="p14819522103517"></a>Failed to complete the request because the server does not support the requested function.</p>
    </td>
    </tr>
    <tr id="row1819122213357"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p28197225351"><a name="p28197225351"></a><a name="p28197225351"></a>502 Bad Gateway</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p118192228352"><a name="p118192228352"></a><a name="p118192228352"></a>Failed to complete the request because the server receives an invalid response from an upstream server.</p>
    </td>
    </tr>
    <tr id="row128196222350"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p19819102243512"><a name="p19819102243512"></a><a name="p19819102243512"></a>503 Service Unavailable</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p38190223354"><a name="p38190223354"></a><a name="p38190223354"></a>Failed to complete the request because the system is unavailable.</p>
    </td>
    </tr>
    <tr id="row281942216356"><td class="cellrowborder" valign="top" width="43.43%" headers="mcps1.1.3.1.1 "><p id="p8819142243515"><a name="p8819142243515"></a><a name="p8819142243515"></a>504 Gateway Timeout</p>
    </td>
    <td class="cellrowborder" valign="top" width="56.57%" headers="mcps1.1.3.1.2 "><p id="p178191722173514"><a name="p178191722173514"></a><a name="p178191722173514"></a>A gateway timeout error occurred.</p>
    </td>
    </tr>
    </tbody>
    </table>



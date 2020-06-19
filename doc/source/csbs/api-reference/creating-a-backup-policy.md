# Creating a Backup Policy<a name="EN-US_TOPIC_0059304223"></a>

## Function<a name="section31829604"></a>

This API is used to back up servers periodically.

## URI<a name="section18030987"></a>

-   URI format

    POST https://\{endpoint\}/v1/\{project\_id\}/policies

-   Parameter description

    **Table  1**  Parameter description

    <a name="table8987571"></a>
    <table><thead align="left"><tr id="row23300495"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p8291924"><a name="p8291924"></a><a name="p8291924"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p557258"><a name="p557258"></a><a name="p557258"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p45137944"><a name="p45137944"></a><a name="p45137944"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p32294887"><a name="p32294887"></a><a name="p32294887"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row65749087"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p24075815"><a name="p24075815"></a><a name="p24075815"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p3983975"><a name="p3983975"></a><a name="p3983975"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p54266568"><a name="p54266568"></a><a name="p54266568"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p65779720"><a name="p65779720"></a><a name="p65779720"></a>Project ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section28061156"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table49115326"></a>
    <table><thead align="left"><tr id="row21353276"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p51893763"><a name="p51893763"></a><a name="p51893763"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p42645295"><a name="p42645295"></a><a name="p42645295"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p31716904"><a name="p31716904"></a><a name="p31716904"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p18932437"><a name="p18932437"></a><a name="p18932437"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row57132447"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p64325485"><a name="p64325485"></a><a name="p64325485"></a>policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p42981800"><a name="p42981800"></a><a name="p42981800"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p58973751"><a name="p58973751"></a><a name="p58973751"></a>policy_create</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p12144515"><a name="p12144515"></a><a name="p12144515"></a>Creation parameters</p>
    <p id="p42412300618"><a name="p42412300618"></a><a name="p42412300618"></a>For details, see <a href="#table44181619">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **policy\_create**

    **Table  3**  Parameter description of field  **policy\_create**

    <a name="table44181619"></a>
    <table><thead align="left"><tr id="row11627299"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p2287175"><a name="p2287175"></a><a name="p2287175"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p51043450"><a name="p51043450"></a><a name="p51043450"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p40878823"><a name="p40878823"></a><a name="p40878823"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p22850356"><a name="p22850356"></a><a name="p22850356"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row38939529"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p67094159"><a name="p67094159"></a><a name="p67094159"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p65917805"><a name="p65917805"></a><a name="p65917805"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p37742028"><a name="p37742028"></a><a name="p37742028"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p27265077155440"><a name="p27265077155440"></a><a name="p27265077155440"></a>Backup policy description</p>
    <p id="p37205460"><a name="p37205460"></a><a name="p37205460"></a>The value consists of 0 to 255 characters and must not contain a greater-than sign (&gt;) or less-than sign (&lt;).</p>
    </td>
    </tr>
    <tr id="row66413686"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p10799501"><a name="p10799501"></a><a name="p10799501"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p2344417"><a name="p2344417"></a><a name="p2344417"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p55680089"><a name="p55680089"></a><a name="p55680089"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p48189633155443"><a name="p48189633155443"></a><a name="p48189633155443"></a>Backup policy name</p>
    <p id="p13793374"><a name="p13793374"></a><a name="p13793374"></a>The value consists of 1 to 255 characters and can contain only letters, digits, underscores (_), and hyphens (-).</p>
    </td>
    </tr>
    <tr id="row57031504"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p56149139"><a name="p56149139"></a><a name="p56149139"></a>parameters</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p51786390"><a name="p51786390"></a><a name="p51786390"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p33948033"><a name="p33948033"></a><a name="p33948033"></a>policy_param</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p65436157"><a name="p65436157"></a><a name="p65436157"></a>Backup parameters</p>
    <p id="p817913224114"><a name="p817913224114"></a><a name="p817913224114"></a>For details, see <a href="#table37852877">Table 4</a>.</p>
    </td>
    </tr>
    <tr id="row52054505"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p55665344"><a name="p55665344"></a><a name="p55665344"></a>provider_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p12599036"><a name="p12599036"></a><a name="p12599036"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p13889029"><a name="p13889029"></a><a name="p13889029"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p51269570"><a name="p51269570"></a><a name="p51269570"></a>Backup provider ID, which specifies whether the backup object is a server or disk. This parameter has a fixed value. For CSBS, the value is <strong id="b23821012346"><a name="b23821012346"></a><a name="b23821012346"></a>fc4d5750-22e7-4798-8a46-f48f62c4c1da</strong>. </p>
    </td>
    </tr>
    <tr id="row58772952"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p62988671"><a name="p62988671"></a><a name="p62988671"></a>resources</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p1808718"><a name="p1808718"></a><a name="p1808718"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p12288494"><a name="p12288494"></a><a name="p12288494"></a>List&lt;resource&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p55843975"><a name="p55843975"></a><a name="p55843975"></a>Backup object list. The list can be blank.</p>
    <p id="p144001011102416"><a name="p144001011102416"></a><a name="p144001011102416"></a>For details, see <a href="#table50789269">Table 5</a>.</p>
    </td>
    </tr>
    <tr id="row32833728"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p42286272"><a name="p42286272"></a><a name="p42286272"></a>scheduled_operations</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p2635980"><a name="p2635980"></a><a name="p2635980"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p12187853"><a name="p12187853"></a><a name="p12187853"></a>List&lt;scheduled_operation_create&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p47692075"><a name="p47692075"></a><a name="p47692075"></a>Scheduling period</p>
    <p id="p133820551248"><a name="p133820551248"></a><a name="p133820551248"></a>For details, see <a href="#table23951472">Table 6</a>.</p>
    </td>
    </tr>
    <tr id="row15378171794412"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p1937919174449"><a name="p1937919174449"></a><a name="p1937919174449"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p1737931718448"><a name="p1737931718448"></a><a name="p1737931718448"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p1737971714449"><a name="p1737971714449"></a><a name="p1737971714449"></a>List&lt;resource_tag&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p9244511113310"><a name="p9244511113310"></a><a name="p9244511113310"></a>Tag list</p>
    <p id="p52026988"><a name="p52026988"></a><a name="p52026988"></a>This list cannot be an empty list.</p>
    <p id="p183916535015"><a name="p183916535015"></a><a name="p183916535015"></a>The list can contain up to 10 keys.</p>
    <p id="p1338589319"><a name="p1338589319"></a><a name="p1338589319"></a>Keys in this list must be unique.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **policy\_param**

    **Table  4**  Parameter description of field  **policy\_param**

    <a name="table37852877"></a>
    <table><thead align="left"><tr id="row29126361"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p10425022"><a name="p10425022"></a><a name="p10425022"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p39120468"><a name="p39120468"></a><a name="p39120468"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p14641346"><a name="p14641346"></a><a name="p14641346"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p45098417"><a name="p45098417"></a><a name="p45098417"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row29093193"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p7738417"><a name="p7738417"></a><a name="p7738417"></a>common</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p22832017"><a name="p22832017"></a><a name="p22832017"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p37454098"><a name="p37454098"></a><a name="p37454098"></a>common_param</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p13883099"><a name="p13883099"></a><a name="p13883099"></a>General backup policy parameters, which are blank by default</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **resource**

    **Table  5**  Parameter description of field  **resource**

    <a name="table50789269"></a>
    <table><thead align="left"><tr id="row18650410"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p34288278"><a name="p34288278"></a><a name="p34288278"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p25887101"><a name="p25887101"></a><a name="p25887101"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p16480457"><a name="p16480457"></a><a name="p16480457"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p59848674"><a name="p59848674"></a><a name="p59848674"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row15904431"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p13190553"><a name="p13190553"></a><a name="p13190553"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p61801863"><a name="p61801863"></a><a name="p61801863"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p39895010"><a name="p39895010"></a><a name="p39895010"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p28168574"><a name="p28168574"></a><a name="p28168574"></a>ID of the object to be backed up</p>
    </td>
    </tr>
    <tr id="row7468195183617"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p10242210163618"><a name="p10242210163618"></a><a name="p10242210163618"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p18242710183616"><a name="p18242710183616"></a><a name="p18242710183616"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p182422103364"><a name="p182422103364"></a><a name="p182422103364"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p1251341411205"><a name="p1251341411205"></a><a name="p1251341411205"></a>Entity object type of backup objects</p>
    <p id="p424214104366"><a name="p424214104366"></a><a name="p424214104366"></a>The value is fixed at <strong id="b16607524864"><a name="b16607524864"></a><a name="b16607524864"></a>OS::Nova::Server</strong> (ECSs).</p>
    </td>
    </tr>
    <tr id="row49383080"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p40606554"><a name="p40606554"></a><a name="p40606554"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p796601"><a name="p796601"></a><a name="p796601"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p64524716"><a name="p64524716"></a><a name="p64524716"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p45273784"><a name="p45273784"></a><a name="p45273784"></a>Backup object name</p>
    </td>
    </tr>
    <tr id="row1777116512367"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p777318533616"><a name="p777318533616"></a><a name="p777318533616"></a>extra_info</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p877312516363"><a name="p877312516363"></a><a name="p877312516363"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p10773185103617"><a name="p10773185103617"></a><a name="p10773185103617"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p1677325193612"><a name="p1677325193612"></a><a name="p1677325193612"></a>Additional information about the backup object</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **scheduled\_operation\_create**

    **Table  6**  Parameter description of field  **scheduled\_operation\_create**

    <a name="table23951472"></a>
    <table><thead align="left"><tr id="row24217494"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p15460030"><a name="p15460030"></a><a name="p15460030"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p44302902"><a name="p44302902"></a><a name="p44302902"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p31765286"><a name="p31765286"></a><a name="p31765286"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p22851383"><a name="p22851383"></a><a name="p22851383"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row39022736"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p6725082"><a name="p6725082"></a><a name="p6725082"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p7860797"><a name="p7860797"></a><a name="p7860797"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p32744800"><a name="p32744800"></a><a name="p32744800"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p54572478155517"><a name="p54572478155517"></a><a name="p54572478155517"></a>Scheduling period description</p>
    <p id="p35083115"><a name="p35083115"></a><a name="p35083115"></a>The value consists of 0 to 255 characters and must not contain a greater-than sign (&gt;) or less-than sign (&lt;).</p>
    </td>
    </tr>
    <tr id="row47312583"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p7114051"><a name="p7114051"></a><a name="p7114051"></a>enabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p39367226"><a name="p39367226"></a><a name="p39367226"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p34628758"><a name="p34628758"></a><a name="p34628758"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p62730120155515"><a name="p62730120155515"></a><a name="p62730120155515"></a>Whether the backup policy is enabled</p>
    <p id="p53466047"><a name="p53466047"></a><a name="p53466047"></a>If it is set to <strong id="b38520628154040"><a name="b38520628154040"></a><a name="b38520628154040"></a>true</strong>, automatic scheduling is enabled. If it is set to <strong id="b1125921504154042"><a name="b1125921504154042"></a><a name="b1125921504154042"></a>false</strong>, automatic scheduling is disabled but you can execute the policy manually.</p>
    </td>
    </tr>
    <tr id="row11432380"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p53607554"><a name="p53607554"></a><a name="p53607554"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p47244617"><a name="p47244617"></a><a name="p47244617"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p1608760"><a name="p1608760"></a><a name="p1608760"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p64762572155525"><a name="p64762572155525"></a><a name="p64762572155525"></a>Scheduling period name</p>
    <p id="p63200760"><a name="p63200760"></a><a name="p63200760"></a>The value consists of 1 to 255 characters and can contain only letters, digits, underscores (_), and hyphens (-).</p>
    </td>
    </tr>
    <tr id="row31935934"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p36673850"><a name="p36673850"></a><a name="p36673850"></a>operation_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p17791834"><a name="p17791834"></a><a name="p17791834"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p31852422"><a name="p31852422"></a><a name="p31852422"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p29909415"><a name="p29909415"></a><a name="p29909415"></a>Operation type, which can be backup </p>
    <p id="p749287"><a name="p749287"></a><a name="p749287"></a>Enumeration values: <strong id="b13695184417270"><a name="b13695184417270"></a><a name="b13695184417270"></a>backup</strong></p>
    </td>
    </tr>
    <tr id="row6743589"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p9359847"><a name="p9359847"></a><a name="p9359847"></a>operation_definition</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p19950166"><a name="p19950166"></a><a name="p19950166"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p5350745"><a name="p5350745"></a><a name="p5350745"></a>operation_definition</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p30757209"><a name="p30757209"></a><a name="p30757209"></a>Scheduling period parameters</p>
    <p id="p161223012915"><a name="p161223012915"></a><a name="p161223012915"></a>For details, see <a href="#table19271238">Table 7</a>.</p>
    </td>
    </tr>
    <tr id="row8379427"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p7644968"><a name="p7644968"></a><a name="p7644968"></a>trigger</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p15262686"><a name="p15262686"></a><a name="p15262686"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p28318060"><a name="p28318060"></a><a name="p28318060"></a>trigger</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p12061563"><a name="p12061563"></a><a name="p12061563"></a>Scheduling policy</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **operation\_definition**

    **Table  7**  Parameter description of field  **operation\_definition**

    <a name="table19271238"></a>
    <table><thead align="left"><tr id="row45318420"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p46913442"><a name="p46913442"></a><a name="p46913442"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p41892468"><a name="p41892468"></a><a name="p41892468"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p37846771"><a name="p37846771"></a><a name="p37846771"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p45689606"><a name="p45689606"></a><a name="p45689606"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row9870614"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p61322250"><a name="p61322250"></a><a name="p61322250"></a>max_backups</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p1046347"><a name="p1046347"></a><a name="p1046347"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p19751145134313"><a name="p19751145134313"></a><a name="p19751145134313"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p155661712122915"><a name="p155661712122915"></a><a name="p155661712122915"></a>Maximum number of backups that can be automatically created for a backup object. The value can be <strong id="b5933112273519"><a name="b5933112273519"></a><a name="b5933112273519"></a>-1</strong> or ranges from <strong id="b1668289357"><a name="b1668289357"></a><a name="b1668289357"></a>0</strong> to <strong id="b090293123511"><a name="b090293123511"></a><a name="b090293123511"></a>99999</strong>. If the value is set to <strong id="b135422352355"><a name="b135422352355"></a><a name="b135422352355"></a>-1</strong>, the backups will not be cleared even though the configured retained backup quantity limit is exceeded.</p>
    </td>
    </tr>
    <tr id="row45592928"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p2039720"><a name="p2039720"></a><a name="p2039720"></a>retention_duration_days</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p30999616"><a name="p30999616"></a><a name="p30999616"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p1736144219433"><a name="p1736144219433"></a><a name="p1736144219433"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p1256618126294"><a name="p1256618126294"></a><a name="p1256618126294"></a>Duration of retaining a backup, in days. The value can be <strong id="b12453130143813"><a name="b12453130143813"></a><a name="b12453130143813"></a>-1</strong> or ranges from <strong id="b24535053817"><a name="b24535053817"></a><a name="b24535053817"></a>0</strong> to <strong id="b13454003388"><a name="b13454003388"></a><a name="b13454003388"></a>99999</strong>. If the value is set to <strong id="b09201952104517"><a name="b09201952104517"></a><a name="b09201952104517"></a>-1</strong>, backups will not be cleared even though the configured retention duration is exceeded.</p>
    </td>
    </tr>
    <tr id="row34962829"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p13416914"><a name="p13416914"></a><a name="p13416914"></a>permanent</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p13028235"><a name="p13028235"></a><a name="p13028235"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p1756314017434"><a name="p1756314017434"></a><a name="p1756314017434"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p48669051"><a name="p48669051"></a><a name="p48669051"></a>Whether backups are permanently retained. <strong id="b331116714482"><a name="b331116714482"></a><a name="b331116714482"></a>false</strong>: no. <strong id="b38111194815"><a name="b38111194815"></a><a name="b38111194815"></a>true</strong>: yes</p>
    </td>
    </tr>
    <tr id="row162191159122615"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p6221105982614"><a name="p6221105982614"></a><a name="p6221105982614"></a>plan_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p122219599269"><a name="p122219599269"></a><a name="p122219599269"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p322125992610"><a name="p322125992610"></a><a name="p322125992610"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p112212059192618"><a name="p112212059192618"></a><a name="p112212059192618"></a>Backup policy ID</p>
    </td>
    </tr>
    <tr id="row48704493272"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p1587014495279"><a name="p1587014495279"></a><a name="p1587014495279"></a>provider_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p78705492277"><a name="p78705492277"></a><a name="p78705492277"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p2870134912712"><a name="p2870134912712"></a><a name="p2870134912712"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p19870104917272"><a name="p19870104917272"></a><a name="p19870104917272"></a>Backup provider ID, which specifies whether the backup object is a server or disk. This parameter has a fixed value. For CSBS, the value is <strong id="b1248303714810"><a name="b1248303714810"></a><a name="b1248303714810"></a>fc4d5750-22e7-4798-8a46-f48f62c4c1da</strong>. </p>
    </td>
    </tr>
    <tr id="row133217534261"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p103231536262"><a name="p103231536262"></a><a name="p103231536262"></a>day_backups</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p173231534268"><a name="p173231534268"></a><a name="p173231534268"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p113231553152611"><a name="p113231553152611"></a><a name="p113231553152611"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p532385317262"><a name="p532385317262"></a><a name="p532385317262"></a>Specifies the maximum number of retained daily backups. The latest backup of each day is saved in the long term. This parameter can be effective together with the maximum number of retained backups specified by <strong id="b1765942714362"><a name="b1765942714362"></a><a name="b1765942714362"></a>max_backups</strong>. If this parameter is configured, <strong id="b1372363555013"><a name="b1372363555013"></a><a name="b1372363555013"></a>timezone</strong> is mandatory.</p>
    </td>
    </tr>
    <tr id="row19217723192813"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p166229112817"><a name="p166229112817"></a><a name="p166229112817"></a>week_backups</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p162472902811"><a name="p162472902811"></a><a name="p162472902811"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p639329162812"><a name="p639329162812"></a><a name="p639329162812"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p18444194418109"><a name="p18444194418109"></a><a name="p18444194418109"></a>Specifies the maximum number of retained weekly backups. The latest backup of each week is saved in the long term. This parameter can be effective together with the maximum number of retained backups specified by <strong id="b13619855105119"><a name="b13619855105119"></a><a name="b13619855105119"></a>max_backups</strong>. If this parameter is configured, <strong id="b537271510536"><a name="b537271510536"></a><a name="b537271510536"></a>timezone</strong> is mandatory.</p>
    </td>
    </tr>
    <tr id="row21651543162818"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p1116617434287"><a name="p1116617434287"></a><a name="p1116617434287"></a>month_backups</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p616604392817"><a name="p616604392817"></a><a name="p616604392817"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p1916619435282"><a name="p1916619435282"></a><a name="p1916619435282"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p3166174318281"><a name="p3166174318281"></a><a name="p3166174318281"></a>Specifies the maximum number of retained monthly backups. The latest backup of each month is saved in the long term. This parameter can be effective together with the maximum number of retained backups specified by <strong id="b228121117529"><a name="b228121117529"></a><a name="b228121117529"></a>max_backups</strong>. If this parameter is configured, <strong id="b14303540125317"><a name="b14303540125317"></a><a name="b14303540125317"></a>timezone</strong> is mandatory.</p>
    </td>
    </tr>
    <tr id="row1078211192919"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p7915112162917"><a name="p7915112162917"></a><a name="p7915112162917"></a>year_backups</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p6920112182912"><a name="p6920112182912"></a><a name="p6920112182912"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p0933121252910"><a name="p0933121252910"></a><a name="p0933121252910"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p1194121272917"><a name="p1194121272917"></a><a name="p1194121272917"></a>Specifies the maximum number of retained yearly backups. The latest backup of each year is saved in the long term. This parameter can be effective together with the maximum number of retained backups specified by <strong id="b17124174875215"><a name="b17124174875215"></a><a name="b17124174875215"></a>max_backups</strong>. If this parameter is configured, <strong id="b57137509532"><a name="b57137509532"></a><a name="b57137509532"></a>timezone</strong> is mandatory.</p>
    </td>
    </tr>
    <tr id="row19554162315296"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p175558232297"><a name="p175558232297"></a><a name="p175558232297"></a>timezone</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p555552311290"><a name="p555552311290"></a><a name="p555552311290"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p1255532311299"><a name="p1255532311299"></a><a name="p1255532311299"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p1267113527713"><a name="p1267113527713"></a><a name="p1267113527713"></a>Time zone where the user is located, for example, UTC+08:00. Set this parameter only after you have configured any of the parameters <strong id="b9978758155419"><a name="b9978758155419"></a><a name="b9978758155419"></a>day_backups</strong>, <strong id="b2813142219555"><a name="b2813142219555"></a><a name="b2813142219555"></a>week_backups</strong>, <strong id="b16365152595513"><a name="b16365152595513"></a><a name="b16365152595513"></a>month_backups</strong>, and <strong id="b1418013013554"><a name="b1418013013554"></a><a name="b1418013013554"></a>year_backups</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    >![](/images/icon-note.gif) **NOTE:**   
    >-   If  **permanent**  is set to  **true**, backups will be retained permanently, despite the settings of  **max\_backups**  and  **retention\_duration\_days**.  
    >-   If  **permanent**  is set to  **false**, settings of  **max\_backups**  and  **retention\_duration\_days**  are effective.  
    >-   If none of  **permanent**,  **max\_backups**, and  **retention\_duration\_days**  is set, backups will be retained permanently.  

-   Parameter description of field  **trigger**

    **Table  8**  Parameter description of field  **trigger**

    <a name="table49879041"></a>
    <table><thead align="left"><tr id="row47309752"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p6884678"><a name="p6884678"></a><a name="p6884678"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p20788012"><a name="p20788012"></a><a name="p20788012"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p6107411"><a name="p6107411"></a><a name="p6107411"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p24938274"><a name="p24938274"></a><a name="p24938274"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row6734338"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p8610523"><a name="p8610523"></a><a name="p8610523"></a>properties</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p26363732"><a name="p26363732"></a><a name="p26363732"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p55087509"><a name="p55087509"></a><a name="p55087509"></a>trigger_properties</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p32903239"><a name="p32903239"></a><a name="p32903239"></a>Scheduler properties</p>
    <p id="p988542119125"><a name="p988542119125"></a><a name="p988542119125"></a>For details, see <a href="#table47916689">Table 9</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **trigger\_properties**

    **Table  9**  Parameter description of field  **trigger\_properties**

    <a name="table47916689"></a>
    <table><thead align="left"><tr id="row23274163"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p6159059"><a name="p6159059"></a><a name="p6159059"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p29121751"><a name="p29121751"></a><a name="p29121751"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p10051624"><a name="p10051624"></a><a name="p10051624"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p8875181"><a name="p8875181"></a><a name="p8875181"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row47801038"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p46678901"><a name="p46678901"></a><a name="p46678901"></a>pattern</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p22894599"><a name="p22894599"></a><a name="p22894599"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p42523246"><a name="p42523246"></a><a name="p42523246"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p1462194645616"><a name="p1462194645616"></a><a name="p1462194645616"></a>Scheduling policy of the scheduler. The value consists of a maximum of 10,240 characters. The scheduling policy complies with iCalendar RFC 2445, but it supports only four parameters, which are <strong id="b493883467145715"><a name="b493883467145715"></a><a name="b493883467145715"></a>FREQ</strong>, <strong id="b1937275926145715"><a name="b1937275926145715"></a><a name="b1937275926145715"></a>BYDAY</strong>, <strong id="b1612469200145715"><a name="b1612469200145715"></a><a name="b1612469200145715"></a>BYHOUR</strong>, and <strong id="b390004774145715"><a name="b390004774145715"></a><a name="b390004774145715"></a>BYMINUTE</strong>. <strong id="b1516398839145715"><a name="b1516398839145715"></a><a name="b1516398839145715"></a>FREQ</strong> can be set only to <strong id="b224731310145715"><a name="b224731310145715"></a><a name="b224731310145715"></a>WEEKLY</strong> or <strong id="b1900044038145715"><a name="b1900044038145715"></a><a name="b1900044038145715"></a>DAILY</strong>. <strong id="b23610045145715"><a name="b23610045145715"></a><a name="b23610045145715"></a>BYDAY</strong> can be set to <strong id="b815356244145715"><a name="b815356244145715"></a><a name="b815356244145715"></a>MO</strong>, <strong id="b459345718145715"><a name="b459345718145715"></a><a name="b459345718145715"></a>TU</strong>, <strong id="b782468707145715"><a name="b782468707145715"></a><a name="b782468707145715"></a>WE</strong>, <strong id="b1340771475145715"><a name="b1340771475145715"></a><a name="b1340771475145715"></a>TH</strong>, <strong id="b399493889145715"><a name="b399493889145715"></a><a name="b399493889145715"></a>FR</strong>, <strong id="b588657796145715"><a name="b588657796145715"></a><a name="b588657796145715"></a>SA</strong>, or <strong id="b1417324580145715"><a name="b1417324580145715"></a><a name="b1417324580145715"></a>SU</strong> (seven days of a week). <strong id="b1173680002145715"><a name="b1173680002145715"></a><a name="b1173680002145715"></a>BYHOUR</strong> ranges from 0 to 23 hours. <strong id="b1323451016145715"><a name="b1323451016145715"></a><a name="b1323451016145715"></a>BYMINUTE</strong> ranges from 0 to 59 minutes. The scheduling interval cannot be less than 1 hour. A maximum of 24 time points are allowed in a day.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **resource\_tag**

    **Table  10**  Parameter description of field  **resource\_tag**

    <a name="table1431115645119"></a>
    <table><thead align="left"><tr id="row4339106155119"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p1334796195117"><a name="p1334796195117"></a><a name="p1334796195117"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p163543612513"><a name="p163543612513"></a><a name="p163543612513"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p193627619517"><a name="p193627619517"></a><a name="p193627619517"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p73671062515"><a name="p73671062515"></a><a name="p73671062515"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row63768665110"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p10380567512"><a name="p10380567512"></a><a name="p10380567512"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p1938817615112"><a name="p1938817615112"></a><a name="p1938817615112"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p1739414617517"><a name="p1739414617517"></a><a name="p1739414617517"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p798643483310"><a name="p798643483310"></a><a name="p798643483310"></a>Tag key</p>
    <p id="p036816391334"><a name="p036816391334"></a><a name="p036816391334"></a>It consists of up to 36 characters.</p>
    <p id="p1815945343312"><a name="p1815945343312"></a><a name="p1815945343312"></a>It cannot be an empty string.</p>
    <p id="p139819543334"><a name="p139819543334"></a><a name="p139819543334"></a>Spaces before and after a key will be deprecated.</p>
    <p id="p14766132412516"><a name="p14766132412516"></a><a name="p14766132412516"></a>It can contain only letters, digits, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    <tr id="row1116111556513"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p1816118554511"><a name="p1816118554511"></a><a name="p1816118554511"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p1516145585115"><a name="p1516145585115"></a><a name="p1516145585115"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p1116145519518"><a name="p1116145519518"></a><a name="p1116145519518"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p11608421163420"><a name="p11608421163420"></a><a name="p11608421163420"></a>Tag value</p>
    <p id="p489413816351"><a name="p489413816351"></a><a name="p489413816351"></a>It consists of up to 43 characters.</p>
    <p id="p14194717123517"><a name="p14194717123517"></a><a name="p14194717123517"></a>It can be an empty string.</p>
    <p id="p1146913338362"><a name="p1146913338362"></a><a name="p1146913338362"></a>Spaces before and after a tag value will be deprecated.</p>
    <p id="p1317535564114"><a name="p1317535564114"></a><a name="p1317535564114"></a>It can contain only letters, digits, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    </tbody>
    </table>


-   Example request

    ```
    POST https://{endpoint}/v1/{project_id}/policies
    {
      "policy" : {
        "name" : "my-plan",
        "description" : "My plan",
        "provider_id" : "fc4d5750-22e7-4798-8a46-f48f62c4c1da",
        "parameters" : {
          "common" : {
          }
        },
        "scheduled_operations" : [ {
          "name" : "my-backup-policy",
          "description" : "My backup policy",
          "enabled" : true,
          "operation_definition" : {
            "max_backups" : 20
          },
          "trigger" : {
            "properties" : {
              "pattern" : "BEGIN:VCALENDAR\r\nBEGIN:VEVENT\r\nRRULE:FREQ=WEEKLY;BYDAY=TH;BYHOUR=12;BYMINUTE=27\r\nEND:VEVENT\r\nEND:VCALENDAR\r\n"
            }
          },
          "operation_type" : "backup"
        }
         
        ],
        "resources" : [ {
          "id" : "45baf976-c20a-4894-a7c3-c94b7376bf55",
          "type" : "OS::Nova::Server",
          "name" : "resource1",
        }, {
          "id" : "5aa119a8-d25b-45a7-8d1b-88e127885635",
          "type" : "OS::Nova::Server",
          "name" : "resource2"
        } ]
      }
    }
    ```


## Response<a name="section51223818"></a>

-   Parameter description

    **Table  11**  Parameter description

    <a name="table39318913"></a>
    <table><thead align="left"><tr id="row29321872"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p26261412"><a name="p26261412"></a><a name="p26261412"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p32672922"><a name="p32672922"></a><a name="p32672922"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p29261003"><a name="p29261003"></a><a name="p29261003"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row21331074"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p50095396"><a name="p50095396"></a><a name="p50095396"></a>policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p43790671"><a name="p43790671"></a><a name="p43790671"></a>policy_resp</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p57383463"><a name="p57383463"></a><a name="p57383463"></a>For details, see <a href="#table17548940">Table 12</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **policy\_resp**

    **Table  12**  Parameter description of field  **policy\_resp**

    <a name="table17548940"></a>
    <table><thead align="left"><tr id="row28512063"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p27775771"><a name="p27775771"></a><a name="p27775771"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p36270756"><a name="p36270756"></a><a name="p36270756"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p52250146"><a name="p52250146"></a><a name="p52250146"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row4403408"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p21131734"><a name="p21131734"></a><a name="p21131734"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p65505804"><a name="p65505804"></a><a name="p65505804"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p4369932"><a name="p4369932"></a><a name="p4369932"></a>Creation time, for example, <strong id="b4510143014819"><a name="b4510143014819"></a><a name="b4510143014819"></a>2017-04-18T01:21:52.701973</strong></p>
    </td>
    </tr>
    <tr id="row39329394"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p31564334"><a name="p31564334"></a><a name="p31564334"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p62749946"><a name="p62749946"></a><a name="p62749946"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p33604774155631"><a name="p33604774155631"></a><a name="p33604774155631"></a>Backup policy description</p>
    <p id="p49580891"><a name="p49580891"></a><a name="p49580891"></a>The value consists of 0 to 255 characters and must not contain a greater-than sign (&gt;) or less-than sign (&lt;).</p>
    </td>
    </tr>
    <tr id="row43574843"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p39901414"><a name="p39901414"></a><a name="p39901414"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p1503005"><a name="p1503005"></a><a name="p1503005"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p54634618"><a name="p54634618"></a><a name="p54634618"></a>Backup policy ID</p>
    </td>
    </tr>
    <tr id="row21949517"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p33080433"><a name="p33080433"></a><a name="p33080433"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p10657415"><a name="p10657415"></a><a name="p10657415"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p11959167155632"><a name="p11959167155632"></a><a name="p11959167155632"></a>Backup policy name</p>
    <p id="p57944264"><a name="p57944264"></a><a name="p57944264"></a>The value consists of 1 to 255 characters and can contain only letters, digits, underscores (_), and hyphens (-).</p>
    </td>
    </tr>
    <tr id="row51736335"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p29893639"><a name="p29893639"></a><a name="p29893639"></a>parameters</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p40066831"><a name="p40066831"></a><a name="p40066831"></a>policy_param</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p24187888"><a name="p24187888"></a><a name="p24187888"></a>Parameters of a backup policy</p>
    <p id="p1285817314139"><a name="p1285817314139"></a><a name="p1285817314139"></a>For details, see <a href="#table60850186">Table 13</a>.</p>
    </td>
    </tr>
    <tr id="row16364404"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p50448361"><a name="p50448361"></a><a name="p50448361"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p10781336"><a name="p10781336"></a><a name="p10781336"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p872994"><a name="p872994"></a><a name="p872994"></a>Project ID</p>
    </td>
    </tr>
    <tr id="row7856948"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p32433056"><a name="p32433056"></a><a name="p32433056"></a>provider_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p58184521"><a name="p58184521"></a><a name="p58184521"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p15325783"><a name="p15325783"></a><a name="p15325783"></a>Backup provider ID, which specifies whether the backup object is a server or disk. This parameter has a fixed value. For CSBS, the value is <strong id="b132869713397"><a name="b132869713397"></a><a name="b132869713397"></a>fc4d5750-22e7-4798-8a46-f48f62c4c1da</strong>. </p>
    </td>
    </tr>
    <tr id="row3714320"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p32424509"><a name="p32424509"></a><a name="p32424509"></a>resources</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p2109397"><a name="p2109397"></a><a name="p2109397"></a>List&lt;resource&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p36643472"><a name="p36643472"></a><a name="p36643472"></a>Backup object list</p>
    <p id="p031412112386"><a name="p031412112386"></a><a name="p031412112386"></a>For details, see <a href="#table8223017">Table 14</a>.</p>
    </td>
    </tr>
    <tr id="row61355793"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p3763354"><a name="p3763354"></a><a name="p3763354"></a>scheduled_operations</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p62413236"><a name="p62413236"></a><a name="p62413236"></a>List&lt;scheduled_operation_resp&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p22307350"><a name="p22307350"></a><a name="p22307350"></a>Scheduling period list</p>
    <p id="p721416394102"><a name="p721416394102"></a><a name="p721416394102"></a>For details, see <a href="#table27342530">Table 15</a>.</p>
    </td>
    </tr>
    <tr id="row66548424"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p21713302"><a name="p21713302"></a><a name="p21713302"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p55969127"><a name="p55969127"></a><a name="p55969127"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p673245135219"><a name="p673245135219"></a><a name="p673245135219"></a>Backup policy status</p>
    <p id="p41984995213"><a name="p41984995213"></a><a name="p41984995213"></a><strong id="b1250102492416"><a name="b1250102492416"></a><a name="b1250102492416"></a>disabled</strong>: indicates that the backup policy is unavailable.</p>
    <p id="p37205434"><a name="p37205434"></a><a name="p37205434"></a><strong id="b842352706201847"><a name="b842352706201847"></a><a name="b842352706201847"></a>enabled</strong>: indicates that the backup policy is available.</p>
    </td>
    </tr>
    <tr id="row22241337193112"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p174623437319"><a name="p174623437319"></a><a name="p174623437319"></a>tags</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p3491104316311"><a name="p3491104316311"></a><a name="p3491104316311"></a>List&lt;resource_tag&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p205016435313"><a name="p205016435313"></a><a name="p205016435313"></a>Tag list</p>
    <p id="p195066436315"><a name="p195066436315"></a><a name="p195066436315"></a>Keys in the tag list must be unique.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **policy\_param**

    **Table  13**  Parameter description of field  **policy\_param**

    <a name="table60850186"></a>
    <table><thead align="left"><tr id="row55096853"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p33660148"><a name="p33660148"></a><a name="p33660148"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p56074324"><a name="p56074324"></a><a name="p56074324"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p45726372"><a name="p45726372"></a><a name="p45726372"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row12848661"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p34108622"><a name="p34108622"></a><a name="p34108622"></a>common</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p45722427"><a name="p45722427"></a><a name="p45722427"></a>common_param</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p12529086"><a name="p12529086"></a><a name="p12529086"></a>Common parameters of a backup policy</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **resource**

    **Table  14**  Parameter description of field  **resource**

    <a name="table8223017"></a>
    <table><thead align="left"><tr id="row13206884"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p63124717"><a name="p63124717"></a><a name="p63124717"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p32472196"><a name="p32472196"></a><a name="p32472196"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p13002210"><a name="p13002210"></a><a name="p13002210"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row46546093"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p12137164"><a name="p12137164"></a><a name="p12137164"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p40822568"><a name="p40822568"></a><a name="p40822568"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p18293684"><a name="p18293684"></a><a name="p18293684"></a>ID of the object to be backed up</p>
    </td>
    </tr>
    <tr id="row30425435"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p48541157"><a name="p48541157"></a><a name="p48541157"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p46976228"><a name="p46976228"></a><a name="p46976228"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p135595518209"><a name="p135595518209"></a><a name="p135595518209"></a>Entity object type of backup objects</p>
    <p id="p46978087"><a name="p46978087"></a><a name="p46978087"></a>The value is fixed at <strong id="b7716720122811"><a name="b7716720122811"></a><a name="b7716720122811"></a>OS::Nova::Server</strong>, indicating that the object type is ECSs.</p>
    </td>
    </tr>
    <tr id="row20149607"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p21505479"><a name="p21505479"></a><a name="p21505479"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p34617244"><a name="p34617244"></a><a name="p34617244"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p52533345"><a name="p52533345"></a><a name="p52533345"></a>Backup object name</p>
    </td>
    </tr>
    <tr id="row1335872524012"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p17358925104016"><a name="p17358925104016"></a><a name="p17358925104016"></a>extra_info</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p835802519403"><a name="p835802519403"></a><a name="p835802519403"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p1235852516402"><a name="p1235852516402"></a><a name="p1235852516402"></a>Additional information about the backup object</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **scheduled\_operation\_resp**

    **Table  15**  Parameter description of field  **scheduled\_operation\_resp**

    <a name="table27342530"></a>
    <table><thead align="left"><tr id="row11737145"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p11184698"><a name="p11184698"></a><a name="p11184698"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p32818621"><a name="p32818621"></a><a name="p32818621"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p41062672"><a name="p41062672"></a><a name="p41062672"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row37742115"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p37212446"><a name="p37212446"></a><a name="p37212446"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p8814574"><a name="p8814574"></a><a name="p8814574"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p63816818155656"><a name="p63816818155656"></a><a name="p63816818155656"></a>Scheduling period description</p>
    <p id="p42891923"><a name="p42891923"></a><a name="p42891923"></a>The value consists of 0 to 255 characters and must not contain a greater-than sign (&gt;) or less-than sign (&lt;).</p>
    </td>
    </tr>
    <tr id="row50482993"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p62590666"><a name="p62590666"></a><a name="p62590666"></a>enabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p18224513"><a name="p18224513"></a><a name="p18224513"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p4722803815572"><a name="p4722803815572"></a><a name="p4722803815572"></a>Whether the backup policy is enabled</p>
    <p id="p66899439"><a name="p66899439"></a><a name="p66899439"></a>The default value is <strong id="b7338628155344"><a name="b7338628155344"></a><a name="b7338628155344"></a>true</strong>. If it is set to <strong id="b40578736155344"><a name="b40578736155344"></a><a name="b40578736155344"></a>false</strong>, automatic scheduling is disabled but manual scheduling is supported.</p>
    </td>
    </tr>
    <tr id="row65224043"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p48656155"><a name="p48656155"></a><a name="p48656155"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p63280397"><a name="p63280397"></a><a name="p63280397"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p1565991715579"><a name="p1565991715579"></a><a name="p1565991715579"></a>Scheduling period name</p>
    <p id="p25438494"><a name="p25438494"></a><a name="p25438494"></a>The value consists of 1 to 255 characters and can contain only letters, digits, underscores (_), and hyphens (-).</p>
    </td>
    </tr>
    <tr id="row27619857"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p22615970"><a name="p22615970"></a><a name="p22615970"></a>operation_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p5687234"><a name="p5687234"></a><a name="p5687234"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p19973119194519"><a name="p19973119194519"></a><a name="p19973119194519"></a>Operation type, which can be backup </p>
    <p id="p1698917917456"><a name="p1698917917456"></a><a name="p1698917917456"></a>Enumeration values: <strong id="b18484193192813"><a name="b18484193192813"></a><a name="b18484193192813"></a>backup</strong></p>
    </td>
    </tr>
    <tr id="row1419028"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p47832452"><a name="p47832452"></a><a name="p47832452"></a>operation_definition</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p27671161"><a name="p27671161"></a><a name="p27671161"></a>operation_definition</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p26771534"><a name="p26771534"></a><a name="p26771534"></a>Scheduling period parameters</p>
    <p id="p184682714386"><a name="p184682714386"></a><a name="p184682714386"></a>For details, see <a href="#table63384596">Table 16</a>.</p>
    </td>
    </tr>
    <tr id="row39617215"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p54877886"><a name="p54877886"></a><a name="p54877886"></a>trigger</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p14760542"><a name="p14760542"></a><a name="p14760542"></a>trigger_resp</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p54753230"><a name="p54753230"></a><a name="p54753230"></a>Scheduling policy</p>
    </td>
    </tr>
    <tr id="row23017027"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p52439899"><a name="p52439899"></a><a name="p52439899"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p58144793"><a name="p58144793"></a><a name="p58144793"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p12107791"><a name="p12107791"></a><a name="p12107791"></a>Scheduling period ID</p>
    </td>
    </tr>
    <tr id="row41861256"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p35318547"><a name="p35318547"></a><a name="p35318547"></a>trigger_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p65191939"><a name="p65191939"></a><a name="p65191939"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p46055736"><a name="p46055736"></a><a name="p46055736"></a>Scheduler ID</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **operation\_definition**

    **Table  16**  Parameter description of field  **operation\_definition**

    <a name="table63384596"></a>
    <table><thead align="left"><tr id="row54750588"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p5612672"><a name="p5612672"></a><a name="p5612672"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p49086813"><a name="p49086813"></a><a name="p49086813"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p16608902"><a name="p16608902"></a><a name="p16608902"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3143820"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p53322838"><a name="p53322838"></a><a name="p53322838"></a>max_backups</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p12633944"><a name="p12633944"></a><a name="p12633944"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p57317856"><a name="p57317856"></a><a name="p57317856"></a>Maximum number of backups that can be retained. The value can be <strong id="b16498172195413"><a name="b16498172195413"></a><a name="b16498172195413"></a>-1</strong> or ranges from <strong id="b14995295418"><a name="b14995295418"></a><a name="b14995295418"></a>0</strong> to <strong id="b124994275418"><a name="b124994275418"></a><a name="b124994275418"></a>99999</strong>. If the value is set to <strong id="b28205127547"><a name="b28205127547"></a><a name="b28205127547"></a>-1</strong>, the backups will not be cleared even though the configured retained backup quantity limit is exceeded.</p>
    </td>
    </tr>
    <tr id="row16230877"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p39632683"><a name="p39632683"></a><a name="p39632683"></a>retention_duration_days</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p50295167"><a name="p50295167"></a><a name="p50295167"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p33411543"><a name="p33411543"></a><a name="p33411543"></a>Duration of retaining a backup, in days. The value can be <strong id="b315941715418"><a name="b315941715418"></a><a name="b315941715418"></a>-1</strong> or ranges from <strong id="b7159181711542"><a name="b7159181711542"></a><a name="b7159181711542"></a>0</strong> to <strong id="b2160151765419"><a name="b2160151765419"></a><a name="b2160151765419"></a>99999</strong>. If the value is set to <strong id="b285319364611"><a name="b285319364611"></a><a name="b285319364611"></a>-1</strong>, backups will not be cleared even though the configured retention duration is exceeded.</p>
    </td>
    </tr>
    <tr id="row23737353"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p43677444"><a name="p43677444"></a><a name="p43677444"></a>permanent</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p12862047"><a name="p12862047"></a><a name="p12862047"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p35192847"><a name="p35192847"></a><a name="p35192847"></a>Whether backups are permanently retained</p>
    </td>
    </tr>
    <tr id="row144931911132919"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p1949381111299"><a name="p1949381111299"></a><a name="p1949381111299"></a>plan_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p549316116294"><a name="p549316116294"></a><a name="p549316116294"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p449312113298"><a name="p449312113298"></a><a name="p449312113298"></a>Backup policy ID</p>
    </td>
    </tr>
    <tr id="row09311432202917"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p99311232192910"><a name="p99311232192910"></a><a name="p99311232192910"></a>provider_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p169311132102916"><a name="p169311132102916"></a><a name="p169311132102916"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p193183282917"><a name="p193183282917"></a><a name="p193183282917"></a>Backup provider ID, which specifies whether the backup object is a server or disk. This parameter has a fixed value. For CSBS, the value is <strong id="b994213206547"><a name="b994213206547"></a><a name="b994213206547"></a>fc4d5750-22e7-4798-8a46-f48f62c4c1da</strong>. </p>
    </td>
    </tr>
    </tbody>
    </table>

    >![](/images/icon-note.gif) **NOTE:**   
    >-   If  **permanent**  is set to  **true**, backups will be retained permanently, despite the settings of  **max\_backups**  and  **retention\_duration\_days**.  
    >-   If  **permanent**  is set to  **false**, settings of  **max\_backups**  and  **retention\_duration\_days**  are effective.  
    >-   If none of  **permanent**,  **max\_backups**, and  **retention\_duration\_days**  is set, backups will be retained permanently.  

-   Parameter description of field  **trigger\_resp**

    **Table  17**  Parameter description of field  **trigger\_resp**

    <a name="table32048331"></a>
    <table><thead align="left"><tr id="row2735555"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p20253366"><a name="p20253366"></a><a name="p20253366"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p6789872"><a name="p6789872"></a><a name="p6789872"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p13108741"><a name="p13108741"></a><a name="p13108741"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row55175115"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p39999337"><a name="p39999337"></a><a name="p39999337"></a>properties</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p39998288"><a name="p39998288"></a><a name="p39998288"></a>trigger_properties_resp</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p18635880"><a name="p18635880"></a><a name="p18635880"></a>Scheduler properties</p>
    <p id="p103468911421"><a name="p103468911421"></a><a name="p103468911421"></a>For details, see <a href="#table55128598">Parameter description of field trigger_properties_resp</a>.</p>
    </td>
    </tr>
    <tr id="row33505193"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p29566141"><a name="p29566141"></a><a name="p29566141"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p38837434"><a name="p38837434"></a><a name="p38837434"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p58824435"><a name="p58824435"></a><a name="p58824435"></a>Scheduler ID</p>
    </td>
    </tr>
    <tr id="row59657871"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p449362"><a name="p449362"></a><a name="p449362"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p62583865"><a name="p62583865"></a><a name="p62583865"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p36128301"><a name="p36128301"></a><a name="p36128301"></a>Scheduler name</p>
    </td>
    </tr>
    <tr id="row56719260"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p30857368"><a name="p30857368"></a><a name="p30857368"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p54863582"><a name="p54863582"></a><a name="p54863582"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p14765176"><a name="p14765176"></a><a name="p14765176"></a>Scheduling type. The value is fixed at <strong id="b48822022195311"><a name="b48822022195311"></a><a name="b48822022195311"></a>time</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **trigger\_properties\_resp**

    **Table  18**  Parameter description of field  **trigger\_properties\_resp**

    <a name="table55128598"></a>
    <table><thead align="left"><tr id="row731260"><th class="cellrowborder" valign="top" width="30.23%" id="mcps1.2.4.1.1"><p id="p59232061"><a name="p59232061"></a><a name="p59232061"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.28%" id="mcps1.2.4.1.2"><p id="p61232441"><a name="p61232441"></a><a name="p61232441"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.49%" id="mcps1.2.4.1.3"><p id="p60880708"><a name="p60880708"></a><a name="p60880708"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row32390328"><td class="cellrowborder" valign="top" width="30.23%" headers="mcps1.2.4.1.1 "><p id="p6370875"><a name="p6370875"></a><a name="p6370875"></a>pattern</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.2.4.1.2 "><p id="p57603733"><a name="p57603733"></a><a name="p57603733"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p487511155745"><a name="p487511155745"></a><a name="p487511155745"></a>Scheduling policy of the scheduler</p>
    <p id="p35390778"><a name="p35390778"></a><a name="p35390778"></a>The value consists of a maximum of 10,240 characters. The scheduling policy complies with iCalendar RFC 2445, but it supports only four parameters, which are <strong id="b43574134475"><a name="b43574134475"></a><a name="b43574134475"></a>FREQ</strong>, <strong id="b1994381524711"><a name="b1994381524711"></a><a name="b1994381524711"></a>BYDAY</strong>, <strong id="b83981318174710"><a name="b83981318174710"></a><a name="b83981318174710"></a>BYHOUR</strong>, and <strong id="b452518219472"><a name="b452518219472"></a><a name="b452518219472"></a>BYMINUTE</strong>. <strong id="b107764239472"><a name="b107764239472"></a><a name="b107764239472"></a>FREQ</strong> can be set to <strong id="b0988182634711"><a name="b0988182634711"></a><a name="b0988182634711"></a>WEEKLY</strong> and <strong id="b144771136184711"><a name="b144771136184711"></a><a name="b144771136184711"></a>DAILY</strong>, <strong id="b972143934713"><a name="b972143934713"></a><a name="b972143934713"></a>BYDAY</strong> can be set to <strong id="b139669424472"><a name="b139669424472"></a><a name="b139669424472"></a>MO</strong>, <strong id="b4777466475"><a name="b4777466475"></a><a name="b4777466475"></a>TU</strong>, <strong id="b1961524924719"><a name="b1961524924719"></a><a name="b1961524924719"></a>WE</strong>, <strong id="b13789115424710"><a name="b13789115424710"></a><a name="b13789115424710"></a>TH</strong>, <strong id="b17733103044816"><a name="b17733103044816"></a><a name="b17733103044816"></a>FR</strong>, <strong id="b14380143419484"><a name="b14380143419484"></a><a name="b14380143419484"></a>SA</strong>, and <strong id="b8756144212483"><a name="b8756144212483"></a><a name="b8756144212483"></a>SU</strong> (seven days of a week), <strong id="b8159184654817"><a name="b8159184654817"></a><a name="b8159184654817"></a>BYHOUR</strong> ranges from 0 hours to 23 hours, and <strong id="b3846204834812"><a name="b3846204834812"></a><a name="b3846204834812"></a>BYMINUTE</strong> ranges from 0 minutes to 59 minutes. The scheduling interval must not be less than 1 hour. A maximum of 24 time points are allowed in a day.</p>
    </td>
    </tr>
    <tr id="row50081552"><td class="cellrowborder" valign="top" width="30.23%" headers="mcps1.2.4.1.1 "><p id="p30073877"><a name="p30073877"></a><a name="p30073877"></a>start_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.2.4.1.2 "><p id="p14648285"><a name="p14648285"></a><a name="p14648285"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p45660399"><a name="p45660399"></a><a name="p45660399"></a>Scheduler start time, for example, <strong id="b1947952945417"><a name="b1947952945417"></a><a name="b1947952945417"></a>2017-04-18T01:21:52</strong></p>
    </td>
    </tr>
    <tr id="row84596471868"><td class="cellrowborder" valign="top" width="30.23%" headers="mcps1.2.4.1.1 "><p id="p12460447864"><a name="p12460447864"></a><a name="p12460447864"></a>format</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.28%" headers="mcps1.2.4.1.2 "><p id="p94608471263"><a name="p94608471263"></a><a name="p94608471263"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.49%" headers="mcps1.2.4.1.3 "><p id="p1446094716618"><a name="p1446094716618"></a><a name="p1446094716618"></a>Scheduler type</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **resource\_tag**

    **Table  19**  Parameter description of field  **resource\_tag**

    <a name="table417313521868"></a>
    <table><thead align="left"><tr id="row92031852365"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p8210115219610"><a name="p8210115219610"></a><a name="p8210115219610"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p322712521565"><a name="p322712521565"></a><a name="p322712521565"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p172363521662"><a name="p172363521662"></a><a name="p172363521662"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1925014528611"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p20260195214611"><a name="p20260195214611"></a><a name="p20260195214611"></a>key</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p1927719521763"><a name="p1927719521763"></a><a name="p1927719521763"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p13925135105714"><a name="p13925135105714"></a><a name="p13925135105714"></a>Tag key</p>
    <p id="p7327206587"><a name="p7327206587"></a><a name="p7327206587"></a>It consists of up to 36 characters.</p>
    <p id="p145821075819"><a name="p145821075819"></a><a name="p145821075819"></a>It cannot be an empty string.</p>
    <p id="p10562107145513"><a name="p10562107145513"></a><a name="p10562107145513"></a>It can contain only letters, digits, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    <tr id="row230320521160"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p11311752965"><a name="p11311752965"></a><a name="p11311752965"></a>value</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p1432910527614"><a name="p1432910527614"></a><a name="p1432910527614"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p1966153512589"><a name="p1966153512589"></a><a name="p1966153512589"></a>Tag value</p>
    <p id="p8808725135910"><a name="p8808725135910"></a><a name="p8808725135910"></a>It consists of up to 43 characters.</p>
    <p id="p919321595"><a name="p919321595"></a><a name="p919321595"></a>It can be an empty string.</p>
    <p id="p17281181312551"><a name="p17281181312551"></a><a name="p17281181312551"></a>It can contain only letters, digits, hyphens (-), and underscores (_).</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
      "policy" : {
        "created_at" : "2017-03-07T09:27:40.928000",
        "description" : "My plan",
        "id" : "f766c171-9336-479a-8b30-b83cabf6381e",
        "name" : "my-plan",
        "parameters" : {
          "common" : {
          }
        },
        "project_id" : "tenant",
        "provider_id" : "c714180d-ea34-4b13-9a5e-577c7c416eec",
        "resources" : [ {
          "id" : "45baf976-c20a-4894-a7c3-c94b7376bf55",
          "name" : "resource1",
          "type" : "OS::Nova::Server",
          "extra_info" : {
        }
        }, {
          "id" : "5aa119a8-d25b-45a7-8d1b-88e127885635",
          "name" : "resource2",
          "type" : "OS::Nova::Server"
        } ],
        "scheduled_operations" : [ {
          "description" : "My backup policy",
          "enabled" : true,
          "id" : "9303a23d-e433-48e7-b88a-5ee6442e434e",
          "name" : "my-backup-policy",
          "operation_definition" : {
            "max_backups" : "20",
            "plan_id" : "f766c171-9336-479a-8b30-b83cabf6381e",
            "provider_id" : "c714180d-ea34-4b13-9a5e-577c7c416eec"
          },
          "operation_type" : "backup",
          "trigger" : {
            "id" : "8178846b-766d-4fe6-941f-b38c76b6f3b9",
            "name" : "default",
            "properties" : {
              "pattern" : "BEGIN:VCALENDAR\r\nBEGIN:VEVENT\r\nRRULE:FREQ=WEEKLY;BYDAY=TH;BYHOUR=12;BYMINUTE=27\r\nEND:VEVENT\r\nEND:VCALENDAR\r\n",
              "start_time" : "2017-03-07 09:27:41",
              "format" : "ical"
            },
            "type" : "time"
          },
          "trigger_id" : "8178846b-766d-4fe6-941f-b38c76b6f3b9"
        }
    ,
       ],
        "status" : "suspended"
      }
    }
    ```


## Status Codes<a name="section58361181"></a>

-   Normal

    <a name="table64319608"></a>
    <table><thead align="left"><tr id="row49498453"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p49951763"><a name="p49951763"></a><a name="p49951763"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p19561042"><a name="p19561042"></a><a name="p19561042"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row40940602"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p27854450"><a name="p27854450"></a><a name="p27854450"></a>200</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p41617954"><a name="p41617954"></a><a name="p41617954"></a>OK</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    <a name="table15611123"></a>
    <table><thead align="left"><tr id="row13876685"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p50269699"><a name="p50269699"></a><a name="p50269699"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p45313789"><a name="p45313789"></a><a name="p45313789"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row46538275"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p11503967"><a name="p11503967"></a><a name="p11503967"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p59406102"><a name="p59406102"></a><a name="p59406102"></a>Invalid request parameters.</p>
    </td>
    </tr>
    <tr id="row64892876"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p21831626"><a name="p21831626"></a><a name="p21831626"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p23531256"><a name="p23531256"></a><a name="p23531256"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row10454712"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p41525362"><a name="p41525362"></a><a name="p41525362"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p208782512197"><a name="p208782512197"></a><a name="p208782512197"></a>No operation permission.</p>
    </td>
    </tr>
    <tr id="row5891508"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p7450164"><a name="p7450164"></a><a name="p7450164"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p66592429"><a name="p66592429"></a><a name="p66592429"></a>Requested object not found.</p>
    </td>
    </tr>
    <tr id="row62460950"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p26172150"><a name="p26172150"></a><a name="p26172150"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p39569378"><a name="p39569378"></a><a name="p39569378"></a>Service internal error.</p>
    </td>
    </tr>
    <tr id="row20580089"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p56374499"><a name="p56374499"></a><a name="p56374499"></a>503</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p2931726"><a name="p2931726"></a><a name="p2931726"></a>Service unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section61541938486"></a>

For details, see  [Error Codes](error-codes.md).


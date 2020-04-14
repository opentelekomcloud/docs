# Updating a Backup Policy<a name="EN-US_TOPIC_0059304225"></a>

## Function<a name="section1748553"></a>

This API is used to update the backup policy of a specific ID.

## URI<a name="section15736982"></a>

-   URI format

    PUT https://\{endpoint\}/v1/\{project\_id\}/policies/\{policy\_id\}

-   Parameter description

    **Table  1**  Parameter description

    <a name="table61283784"></a>
    <table><thead align="left"><tr id="row8855195"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p46182199"><a name="p46182199"></a><a name="p46182199"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p49770635"><a name="p49770635"></a><a name="p49770635"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p4889664"><a name="p4889664"></a><a name="p4889664"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p60518526"><a name="p60518526"></a><a name="p60518526"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row3053548"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p46010802"><a name="p46010802"></a><a name="p46010802"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p35887481"><a name="p35887481"></a><a name="p35887481"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p21204840"><a name="p21204840"></a><a name="p21204840"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p65779720"><a name="p65779720"></a><a name="p65779720"></a>Project ID</p>
    </td>
    </tr>
    <tr id="row23290222"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p7459818"><a name="p7459818"></a><a name="p7459818"></a>policy_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p265482"><a name="p265482"></a><a name="p265482"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p21504054"><a name="p21504054"></a><a name="p21504054"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p64106839"><a name="p64106839"></a><a name="p64106839"></a>Backup policy ID</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section7415111"></a>

-   Parameter description

    **Table  2**  Parameter description

    <a name="table33726359"></a>
    <table><thead align="left"><tr id="row6792275"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p13303384"><a name="p13303384"></a><a name="p13303384"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p3832334"><a name="p3832334"></a><a name="p3832334"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p41983644"><a name="p41983644"></a><a name="p41983644"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p45232043"><a name="p45232043"></a><a name="p45232043"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row39916899"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p12043371"><a name="p12043371"></a><a name="p12043371"></a>policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p35988971"><a name="p35988971"></a><a name="p35988971"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p29425548"><a name="p29425548"></a><a name="p29425548"></a>policy_update</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p34659189"><a name="p34659189"></a><a name="p34659189"></a>For details, see <a href="#table55930959">Table 3</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **policy\_update**

    **Table  3**  Parameter description of field  **policy\_update**

    <a name="table55930959"></a>
    <table><thead align="left"><tr id="row49553172"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p54384032"><a name="p54384032"></a><a name="p54384032"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p43030439"><a name="p43030439"></a><a name="p43030439"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p62913555"><a name="p62913555"></a><a name="p62913555"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p62833228"><a name="p62833228"></a><a name="p62833228"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row56326713"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p66169923"><a name="p66169923"></a><a name="p66169923"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p58163537"><a name="p58163537"></a><a name="p58163537"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p13626060"><a name="p13626060"></a><a name="p13626060"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p1246903016251"><a name="p1246903016251"></a><a name="p1246903016251"></a>Backup policy description</p>
    <p id="p29969051"><a name="p29969051"></a><a name="p29969051"></a>The value consists of 0 to 255 characters and must not contain a greater-than sign (&gt;) or less-than sign (&lt;).</p>
    </td>
    </tr>
    <tr id="row1286006"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p37057631"><a name="p37057631"></a><a name="p37057631"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p48878096"><a name="p48878096"></a><a name="p48878096"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p66811698"><a name="p66811698"></a><a name="p66811698"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p434157216253"><a name="p434157216253"></a><a name="p434157216253"></a>Backup policy name</p>
    <p id="p43038444"><a name="p43038444"></a><a name="p43038444"></a>The value consists of 1 to 255 characters and can contain only letters, digits, underscores (_), and hyphens (-).</p>
    </td>
    </tr>
    <tr id="row51801682"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p35186724"><a name="p35186724"></a><a name="p35186724"></a>parameters</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p31552419"><a name="p31552419"></a><a name="p31552419"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p5609142"><a name="p5609142"></a><a name="p5609142"></a>policy_param</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p51687366"><a name="p51687366"></a><a name="p51687366"></a>Backup parameters</p>
    <p id="p0991104113316"><a name="p0991104113316"></a><a name="p0991104113316"></a>For details, see <a href="#table55353986">Table 4</a>.</p>
    </td>
    </tr>
    <tr id="row62533112"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p32017293"><a name="p32017293"></a><a name="p32017293"></a>resources</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p43263955"><a name="p43263955"></a><a name="p43263955"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p14719473"><a name="p14719473"></a><a name="p14719473"></a>List&lt;resource&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p51426704"><a name="p51426704"></a><a name="p51426704"></a>Backup objects</p>
    <p id="p18570138103815"><a name="p18570138103815"></a><a name="p18570138103815"></a>For details, see <a href="#table29479947">Table 5</a>.</p>
    </td>
    </tr>
    <tr id="row60187160"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p43321754"><a name="p43321754"></a><a name="p43321754"></a>scheduled_operations</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p19401201"><a name="p19401201"></a><a name="p19401201"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p27993477"><a name="p27993477"></a><a name="p27993477"></a>List&lt;scheduled_operation_update&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p52879165"><a name="p52879165"></a><a name="p52879165"></a>Scheduling period. A backup policy has only one backup period.</p>
    <p id="p29281431203414"><a name="p29281431203414"></a><a name="p29281431203414"></a>For details, see <a href="#table43297870">Table 6</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **policy\_param**

    **Table  4**  Parameter description of field  **policy\_param**

    <a name="table55353986"></a>
    <table><thead align="left"><tr id="row53819525"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p64414273"><a name="p64414273"></a><a name="p64414273"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p50173621"><a name="p50173621"></a><a name="p50173621"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p37531530"><a name="p37531530"></a><a name="p37531530"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p20155112"><a name="p20155112"></a><a name="p20155112"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row21951350"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p33228892"><a name="p33228892"></a><a name="p33228892"></a>common</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p7185731"><a name="p7185731"></a><a name="p7185731"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p45173330"><a name="p45173330"></a><a name="p45173330"></a>common_param</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p35161138"><a name="p35161138"></a><a name="p35161138"></a>General backup policy parameters, which are blank by default</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **resource**

    **Table  5**  Parameter description of field  **resource**

    <a name="table29479947"></a>
    <table><thead align="left"><tr id="row44311089"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p32428495"><a name="p32428495"></a><a name="p32428495"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p9462449"><a name="p9462449"></a><a name="p9462449"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p28260928"><a name="p28260928"></a><a name="p28260928"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p7433827"><a name="p7433827"></a><a name="p7433827"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row65269123"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p52307591"><a name="p52307591"></a><a name="p52307591"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p9056472"><a name="p9056472"></a><a name="p9056472"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p62485597"><a name="p62485597"></a><a name="p62485597"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p28168574"><a name="p28168574"></a><a name="p28168574"></a>ID of the object to be backed up</p>
    </td>
    </tr>
    <tr id="row1251416416381"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p25715473388"><a name="p25715473388"></a><a name="p25715473388"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p125774714384"><a name="p125774714384"></a><a name="p125774714384"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p357747103811"><a name="p357747103811"></a><a name="p357747103811"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p386445920208"><a name="p386445920208"></a><a name="p386445920208"></a>Entity object type of backup objects</p>
    <p id="p165714711387"><a name="p165714711387"></a><a name="p165714711387"></a>The value is fixed at <strong id="b49118301759"><a name="b49118301759"></a><a name="b49118301759"></a>OS::Nova::Server</strong> (ECSs).</p>
    </td>
    </tr>
    <tr id="row19231882"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p14278623"><a name="p14278623"></a><a name="p14278623"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p15717800"><a name="p15717800"></a><a name="p15717800"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p65182286"><a name="p65182286"></a><a name="p65182286"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p45273784"><a name="p45273784"></a><a name="p45273784"></a>Backup object name</p>
    </td>
    </tr>
    <tr id="row14942105564612"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p777318533616"><a name="p777318533616"></a><a name="p777318533616"></a>extra_info</p>
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

-   Parameter description of field  **scheduled\_operation\_update**

    **Table  6**  Parameter description of field  **scheduled\_operation\_update**

    <a name="table43297870"></a>
    <table><thead align="left"><tr id="row57309981"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p11596859"><a name="p11596859"></a><a name="p11596859"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p66930353"><a name="p66930353"></a><a name="p66930353"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p52649512"><a name="p52649512"></a><a name="p52649512"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p36752071"><a name="p36752071"></a><a name="p36752071"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row24127799"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p8194720"><a name="p8194720"></a><a name="p8194720"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p59792553"><a name="p59792553"></a><a name="p59792553"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p11358586"><a name="p11358586"></a><a name="p11358586"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p60024434162531"><a name="p60024434162531"></a><a name="p60024434162531"></a>Scheduling period description</p>
    <p id="p47630268"><a name="p47630268"></a><a name="p47630268"></a>The value consists of 0 to 255 characters and must not contain a greater-than sign (&gt;) or less-than sign (&lt;).</p>
    </td>
    </tr>
    <tr id="row26019230"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p27182924"><a name="p27182924"></a><a name="p27182924"></a>enabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p54333246"><a name="p54333246"></a><a name="p54333246"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p38916829"><a name="p38916829"></a><a name="p38916829"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p41523834162534"><a name="p41523834162534"></a><a name="p41523834162534"></a>Whether the backup policy is enabled</p>
    <p id="p65255440"><a name="p65255440"></a><a name="p65255440"></a>The default value is <strong id="b789415133161647"><a name="b789415133161647"></a><a name="b789415133161647"></a>true</strong>. If it is set to <strong id="b146227301161649"><a name="b146227301161649"></a><a name="b146227301161649"></a>false</strong>, automatic scheduling is disabled but manual scheduling is supported.</p>
    </td>
    </tr>
    <tr id="row50428053"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p58140482"><a name="p58140482"></a><a name="p58140482"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p11758583"><a name="p11758583"></a><a name="p11758583"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p12921181"><a name="p12921181"></a><a name="p12921181"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p21377776162541"><a name="p21377776162541"></a><a name="p21377776162541"></a>Scheduling period name</p>
    <p id="p39982747"><a name="p39982747"></a><a name="p39982747"></a>The value consists of 1 to 255 characters and can contain only letters, digits, underscores (_), and hyphens (-).</p>
    </td>
    </tr>
    <tr id="row24300411"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p22176306"><a name="p22176306"></a><a name="p22176306"></a>operation_definition</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p51450324"><a name="p51450324"></a><a name="p51450324"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p6726731"><a name="p6726731"></a><a name="p6726731"></a>operation_definition</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p7994367"><a name="p7994367"></a><a name="p7994367"></a>Scheduling period parameter</p>
    <p id="p212032016391"><a name="p212032016391"></a><a name="p212032016391"></a>For details, see <a href="#table13129592">Table 7</a>.</p>
    </td>
    </tr>
    <tr id="row4840443"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p56531604"><a name="p56531604"></a><a name="p56531604"></a>trigger</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p15657246"><a name="p15657246"></a><a name="p15657246"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p60277441"><a name="p60277441"></a><a name="p60277441"></a>trigger</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p12061563"><a name="p12061563"></a><a name="p12061563"></a>Scheduling policy</p>
    </td>
    </tr>
    <tr id="row53057605"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p2698731"><a name="p2698731"></a><a name="p2698731"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p17270695"><a name="p17270695"></a><a name="p17270695"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p56749022"><a name="p56749022"></a><a name="p56749022"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p33268090"><a name="p33268090"></a><a name="p33268090"></a>Scheduling period ID</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **operation\_definition**

    **Table  7**  Parameter description of field  **operation\_definition**

    <a name="table13129592"></a>
    <table><thead align="left"><tr id="row41156671"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p45356064"><a name="p45356064"></a><a name="p45356064"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p49962569"><a name="p49962569"></a><a name="p49962569"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p20436323"><a name="p20436323"></a><a name="p20436323"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p44729494"><a name="p44729494"></a><a name="p44729494"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row66319241"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p3149412"><a name="p3149412"></a><a name="p3149412"></a>max_backups</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p53775824"><a name="p53775824"></a><a name="p53775824"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p19751145134313"><a name="p19751145134313"></a><a name="p19751145134313"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p1662615433283"><a name="p1662615433283"></a><a name="p1662615433283"></a>Maximum number of backups that can be automatically created for a backup object. The value can be <strong id="b0427123815515"><a name="b0427123815515"></a><a name="b0427123815515"></a>-1</strong> or ranges from <strong id="b194281638165515"><a name="b194281638165515"></a><a name="b194281638165515"></a>0</strong> to <strong id="b20428738185519"><a name="b20428738185519"></a><a name="b20428738185519"></a>99999</strong>. If the value is set to <strong id="b1220154014554"><a name="b1220154014554"></a><a name="b1220154014554"></a>-1</strong>, the backups will not be cleared even though the configured retained backup quantity limit is exceeded.</p>
    </td>
    </tr>
    <tr id="row18540359"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p25374144"><a name="p25374144"></a><a name="p25374144"></a>retention_duration_days</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p42039789"><a name="p42039789"></a><a name="p42039789"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p1736144219433"><a name="p1736144219433"></a><a name="p1736144219433"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p762624392810"><a name="p762624392810"></a><a name="p762624392810"></a>Duration of retaining a backup, in days. The value can be <strong id="b1527574325519"><a name="b1527574325519"></a><a name="b1527574325519"></a>-1</strong> or ranges from <strong id="b15276174317553"><a name="b15276174317553"></a><a name="b15276174317553"></a>0</strong> to <strong id="b527618437553"><a name="b527618437553"></a><a name="b527618437553"></a>99999</strong>. If the value is set to <strong id="b1366584555512"><a name="b1366584555512"></a><a name="b1366584555512"></a>-1</strong>, backups will not be cleared even though the configured retention duration is exceeded.</p>
    </td>
    </tr>
    <tr id="row50663857"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p10131777"><a name="p10131777"></a><a name="p10131777"></a>permanent</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p15367626"><a name="p15367626"></a><a name="p15367626"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p1756314017434"><a name="p1756314017434"></a><a name="p1756314017434"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p29481188"><a name="p29481188"></a><a name="p29481188"></a>Whether backups are permanently retained</p>
    </td>
    </tr>
    <tr id="row17550191123019"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p4550181193010"><a name="p4550181193010"></a><a name="p4550181193010"></a>plan_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p125501611113018"><a name="p125501611113018"></a><a name="p125501611113018"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p195503117308"><a name="p195503117308"></a><a name="p195503117308"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p1355081183018"><a name="p1355081183018"></a><a name="p1355081183018"></a>Backup policy ID</p>
    </td>
    </tr>
    <tr id="row162500328301"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p1250193223013"><a name="p1250193223013"></a><a name="p1250193223013"></a>provider_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p72502324302"><a name="p72502324302"></a><a name="p72502324302"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p1725073283019"><a name="p1725073283019"></a><a name="p1725073283019"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p4250183216305"><a name="p4250183216305"></a><a name="p4250183216305"></a>Backup provider ID, which specifies whether the backup object is a server or disk. This parameter has a fixed value. For CSBS, the value is <strong id="b1258415479559"><a name="b1258415479559"></a><a name="b1258415479559"></a>fc4d5750-22e7-4798-8a46-f48f62c4c1da</strong>. </p>
    </td>
    </tr>
    <tr id="row64851809351"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p103231536262"><a name="p103231536262"></a><a name="p103231536262"></a>day_backups</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p173231534268"><a name="p173231534268"></a><a name="p173231534268"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p113231553152611"><a name="p113231553152611"></a><a name="p113231553152611"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p532385317262"><a name="p532385317262"></a><a name="p532385317262"></a>Specifies the maximum number of retained daily backups. The latest backup of each day is saved in the long term. This parameter can be effective together with the maximum number of retained backups specified by <strong id="b5546816175313"><a name="b5546816175313"></a><a name="b5546816175313"></a>max_backups</strong>. If this parameter is configured, <strong id="b138471811588"><a name="b138471811588"></a><a name="b138471811588"></a>timezone</strong> is mandatory.</p>
    </td>
    </tr>
    <tr id="row54858043511"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p166229112817"><a name="p166229112817"></a><a name="p166229112817"></a>week_backups</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p162472902811"><a name="p162472902811"></a><a name="p162472902811"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p639329162812"><a name="p639329162812"></a><a name="p639329162812"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p1151429152814"><a name="p1151429152814"></a><a name="p1151429152814"></a>Specifies the maximum number of retained weekly backups. The latest backup of each week is saved in the long term. This parameter can be effective together with the maximum number of retained backups specified by <strong id="b2170151818539"><a name="b2170151818539"></a><a name="b2170151818539"></a>max_backups</strong>. If this parameter is configured, <strong id="b11135132311314"><a name="b11135132311314"></a><a name="b11135132311314"></a>timezone</strong> is mandatory.</p>
    </td>
    </tr>
    <tr id="row14855043512"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p1116617434287"><a name="p1116617434287"></a><a name="p1116617434287"></a>month_backups</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p616604392817"><a name="p616604392817"></a><a name="p616604392817"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p1916619435282"><a name="p1916619435282"></a><a name="p1916619435282"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p3166174318281"><a name="p3166174318281"></a><a name="p3166174318281"></a>Specifies the maximum number of retained monthly backups. The latest backup of each month is saved in the long term. This parameter can be effective together with the maximum number of retained backups specified by <strong id="b196757196538"><a name="b196757196538"></a><a name="b196757196538"></a>max_backups</strong>. If this parameter is configured, <strong id="b13798182619313"><a name="b13798182619313"></a><a name="b13798182619313"></a>timezone</strong> is mandatory.</p>
    </td>
    </tr>
    <tr id="row13485190153519"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p7915112162917"><a name="p7915112162917"></a><a name="p7915112162917"></a>year_backups</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p6920112182912"><a name="p6920112182912"></a><a name="p6920112182912"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p0933121252910"><a name="p0933121252910"></a><a name="p0933121252910"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p1194121272917"><a name="p1194121272917"></a><a name="p1194121272917"></a>Specifies the maximum number of retained yearly backups. The latest backup of each year is saved in the long term. This parameter can be effective together with the maximum number of retained backups specified by <strong id="b188601520145319"><a name="b188601520145319"></a><a name="b188601520145319"></a>max_backups</strong>. If this parameter is configured, <strong id="b946383013315"><a name="b946383013315"></a><a name="b946383013315"></a>timezone</strong> is mandatory.</p>
    </td>
    </tr>
    <tr id="row3485160133514"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p175558232297"><a name="p175558232297"></a><a name="p175558232297"></a>timezone</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p555552311290"><a name="p555552311290"></a><a name="p555552311290"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p1255532311299"><a name="p1255532311299"></a><a name="p1255532311299"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p1555511237298"><a name="p1555511237298"></a><a name="p1555511237298"></a>Time zone where the user is located, for example, UTC+08:00. Set this parameter only after you have configured any of the parameters <strong id="b896918321839"><a name="b896918321839"></a><a name="b896918321839"></a>day_backups</strong>, <strong id="b29691532134"><a name="b29691532134"></a><a name="b29691532134"></a>week_backups</strong>, <strong id="b19697326314"><a name="b19697326314"></a><a name="b19697326314"></a>month_backups</strong>, and <strong id="b20970632233"><a name="b20970632233"></a><a name="b20970632233"></a>year_backups</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   If  **permanent**  is set to  **true**, backups will be retained permanently, despite the settings of  **max\_backups**  and  **retention\_duration\_days**.  
    >-   If  **permanent**  is set to  **false**, settings of  **max\_backups**  and  **retention\_duration\_days**  are effective.  
    >-   If none of  **permanent**,  **max\_backups**, and  **retention\_duration\_days**  is set, backups will be retained permanently.  

-   Parameter description of field  **trigger**

    **Table  8**  Parameter description of field  **trigger**

    <a name="table39166022"></a>
    <table><thead align="left"><tr id="row40204823"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p1520393754018"><a name="p1520393754018"></a><a name="p1520393754018"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p1720353717405"><a name="p1720353717405"></a><a name="p1720353717405"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p62192037134012"><a name="p62192037134012"></a><a name="p62192037134012"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p7235937174010"><a name="p7235937174010"></a><a name="p7235937174010"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row45828644"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p21132661"><a name="p21132661"></a><a name="p21132661"></a>properties</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p34024012"><a name="p34024012"></a><a name="p34024012"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p4481550"><a name="p4481550"></a><a name="p4481550"></a>trigger_properties</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p27461285"><a name="p27461285"></a><a name="p27461285"></a>Scheduler properties</p>
    <p id="p19732123354014"><a name="p19732123354014"></a><a name="p19732123354014"></a>For details, see <a href="#table9771641">Table 9</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **trigger\_properties**

    **Table  9**  Parameter description of field  **trigger\_properties**

    <a name="table9771641"></a>
    <table><thead align="left"><tr id="row26921067"><th class="cellrowborder" valign="top" width="25.507449255074494%" id="mcps1.2.5.1.1"><p id="p2875104117402"><a name="p2875104117402"></a><a name="p2875104117402"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.2"><p id="p20890241154011"><a name="p20890241154011"></a><a name="p20890241154011"></a>Mandatory</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.288571142885711%" id="mcps1.2.5.1.3"><p id="p20890041144020"><a name="p20890041144020"></a><a name="p20890041144020"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="45.91540845915409%" id="mcps1.2.5.1.4"><p id="p19907641144017"><a name="p19907641144017"></a><a name="p19907641144017"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row42495518"><td class="cellrowborder" valign="top" width="25.507449255074494%" headers="mcps1.2.5.1.1 "><p id="p19584956"><a name="p19584956"></a><a name="p19584956"></a>pattern</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.2 "><p id="p42877578"><a name="p42877578"></a><a name="p42877578"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.288571142885711%" headers="mcps1.2.5.1.3 "><p id="p50531760"><a name="p50531760"></a><a name="p50531760"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="45.91540845915409%" headers="mcps1.2.5.1.4 "><p id="p26433854162612"><a name="p26433854162612"></a><a name="p26433854162612"></a>Scheduling policy of the scheduler</p>
    <p id="p66540759"><a name="p66540759"></a><a name="p66540759"></a>The value consists of a maximum of 10,240 characters. The scheduling policy complies with iCalendar RFC 2445, but it supports only four parameters, which are <strong id="b170319339218"><a name="b170319339218"></a><a name="b170319339218"></a>FREQ</strong>, <strong id="b41303811216"><a name="b41303811216"></a><a name="b41303811216"></a>BYDAY</strong>, <strong id="b916394492113"><a name="b916394492113"></a><a name="b916394492113"></a>BYHOUR</strong>, and <strong id="b4127174718218"><a name="b4127174718218"></a><a name="b4127174718218"></a>BYMINUTE</strong>. <strong id="b484924910216"><a name="b484924910216"></a><a name="b484924910216"></a>FREQ</strong> can be set to <strong id="b78491452142114"><a name="b78491452142114"></a><a name="b78491452142114"></a>WEEKLY</strong> and <strong id="b15618115522111"><a name="b15618115522111"></a><a name="b15618115522111"></a>DAILY</strong>, <strong id="b1554312589214"><a name="b1554312589214"></a><a name="b1554312589214"></a>BYDAY</strong> can be set to <strong id="b916614115221"><a name="b916614115221"></a><a name="b916614115221"></a>MO</strong>, <strong id="b5910602210"><a name="b5910602210"></a><a name="b5910602210"></a>TU</strong>, <strong id="b137251312142212"><a name="b137251312142212"></a><a name="b137251312142212"></a>WE</strong>, <strong id="b11173516142218"><a name="b11173516142218"></a><a name="b11173516142218"></a>TH</strong>, <strong id="b1865132422214"><a name="b1865132422214"></a><a name="b1865132422214"></a>FR</strong>, <strong id="b133210280223"><a name="b133210280223"></a><a name="b133210280223"></a>SA</strong>, and <strong id="b3362236142219"><a name="b3362236142219"></a><a name="b3362236142219"></a>SU</strong> (seven days of a week), <strong id="b0388123902216"><a name="b0388123902216"></a><a name="b0388123902216"></a>BYHOUR</strong> ranges from 0 hours to 23 hours, and <strong id="b9269448122211"><a name="b9269448122211"></a><a name="b9269448122211"></a>BYMINUTE</strong> ranges from 0 minutes to 59 minutes. The scheduling interval must not be less than 1 hour. A maximum of 24 time points are allowed in a day.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example request

    ```
    PUT https://{endpoint}/v1/{project_id}/policies/{policy_id}
    {
      "policy" : {
        "name" : "my-plan",
        "parameters" : {
          "common" : {
          }
        },
        "scheduled_operations" : [ {
          "id" : "fed3c8f1-7b6e-4e24-b1ad-473838bad569",
          "name" : "my-backup-policy",
          "description" : "My backup policy ",
          "enabled" : true,
          "operation_definition" : {
            "retention_duration_days" : -1,
            "max_backups" : 20
          },
          "trigger" : {
            "properties" : {
              "pattern" : "BEGIN:VCALENDAR\r\nBEGIN:VEVENT\r\nRRULE:FREQ=WEEKLY;BYDAY=TH;BYHOUR=12;BYMINUTE=27\r\nEND:VEVENT\r\nEND:VCALENDAR\r\n"
            }
         }
     }
        ]
      }
    }
    ```


## Response<a name="section66736007"></a>

-   Parameter description

    **Table  10**  Parameter description

    <a name="table1518486"></a>
    <table><thead align="left"><tr id="row17881433"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p13749185144019"><a name="p13749185144019"></a><a name="p13749185144019"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p0766351194020"><a name="p0766351194020"></a><a name="p0766351194020"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p1781451194011"><a name="p1781451194011"></a><a name="p1781451194011"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row17959251"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p45413212"><a name="p45413212"></a><a name="p45413212"></a>policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p59839724"><a name="p59839724"></a><a name="p59839724"></a>policy_resp</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p15179458"><a name="p15179458"></a><a name="p15179458"></a>For details, see <a href="#table21576622">Table 11</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **policy\_resp**

    **Table  11**  Parameter description of field  **policy\_resp**

    <a name="table21576622"></a>
    <table><thead align="left"><tr id="row35113807"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p1143765194118"><a name="p1143765194118"></a><a name="p1143765194118"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p44531512419"><a name="p44531512419"></a><a name="p44531512419"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p19453451411"><a name="p19453451411"></a><a name="p19453451411"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row16513268"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p62506301"><a name="p62506301"></a><a name="p62506301"></a>created_at</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p1573072"><a name="p1573072"></a><a name="p1573072"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p60309994"><a name="p60309994"></a><a name="p60309994"></a>Creation time, for example, <strong id="b29861635309"><a name="b29861635309"></a><a name="b29861635309"></a>2017-04-18T01:21:52.701973</strong></p>
    </td>
    </tr>
    <tr id="row5919040"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p9680242"><a name="p9680242"></a><a name="p9680242"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p27087556"><a name="p27087556"></a><a name="p27087556"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p31141768162627"><a name="p31141768162627"></a><a name="p31141768162627"></a>Backup policy description</p>
    <p id="p46608436"><a name="p46608436"></a><a name="p46608436"></a>The value consists of 0 to 255 characters and must not contain a greater-than sign (&gt;) or less-than sign (&lt;).</p>
    </td>
    </tr>
    <tr id="row16822742"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p20464843"><a name="p20464843"></a><a name="p20464843"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p52111343"><a name="p52111343"></a><a name="p52111343"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p60269294"><a name="p60269294"></a><a name="p60269294"></a>Backup policy ID</p>
    </td>
    </tr>
    <tr id="row5552742"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p47118920"><a name="p47118920"></a><a name="p47118920"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p43811059"><a name="p43811059"></a><a name="p43811059"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p2801454162630"><a name="p2801454162630"></a><a name="p2801454162630"></a>Backup policy name</p>
    <p id="p59034891"><a name="p59034891"></a><a name="p59034891"></a>The value consists of 1 to 255 characters and can contain only letters, digits, underscores (_), and hyphens (-).</p>
    </td>
    </tr>
    <tr id="row61551976"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p19654194"><a name="p19654194"></a><a name="p19654194"></a>parameters</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p35044536"><a name="p35044536"></a><a name="p35044536"></a>policy_param</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p20035139"><a name="p20035139"></a><a name="p20035139"></a>Parameters of a backup policy</p>
    <p id="p18980124118429"><a name="p18980124118429"></a><a name="p18980124118429"></a>For details, see <a href="#table61263219">Table 12</a>.</p>
    </td>
    </tr>
    <tr id="row46098527"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p42993243"><a name="p42993243"></a><a name="p42993243"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p20112558"><a name="p20112558"></a><a name="p20112558"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p18504535"><a name="p18504535"></a><a name="p18504535"></a>Project ID</p>
    </td>
    </tr>
    <tr id="row32323092"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p924762"><a name="p924762"></a><a name="p924762"></a>provider_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p27568912"><a name="p27568912"></a><a name="p27568912"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p18489424"><a name="p18489424"></a><a name="p18489424"></a>Backup provider ID, which specifies whether the backup object is a server or disk. This parameter has a fixed value. For CSBS, the value is <strong id="b2676122117118"><a name="b2676122117118"></a><a name="b2676122117118"></a>fc4d5750-22e7-4798-8a46-f48f62c4c1da</strong>. </p>
    </td>
    </tr>
    <tr id="row32187094"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p57017810"><a name="p57017810"></a><a name="p57017810"></a>resources</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p29043486"><a name="p29043486"></a><a name="p29043486"></a>List&lt;resource&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p3712191"><a name="p3712191"></a><a name="p3712191"></a>Backup object list</p>
    <p id="p872102517512"><a name="p872102517512"></a><a name="p872102517512"></a>For details, see <a href="#table63079129">Table 13</a>.</p>
    </td>
    </tr>
    <tr id="row33409727"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p21833386"><a name="p21833386"></a><a name="p21833386"></a>scheduled_operations</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p38533985"><a name="p38533985"></a><a name="p38533985"></a>List&lt;scheduled_operation_resp&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p34245118"><a name="p34245118"></a><a name="p34245118"></a>Scheduling period list</p>
    <p id="p13554204718554"><a name="p13554204718554"></a><a name="p13554204718554"></a>For details, see <a href="#table37683621">Table 14</a>.</p>
    </td>
    </tr>
    <tr id="row39770609"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p193877"><a name="p193877"></a><a name="p193877"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p64070123"><a name="p64070123"></a><a name="p64070123"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p22297452"><a name="p22297452"></a><a name="p22297452"></a>Backup policy status</p>
    <a name="ul1773515175502"></a><a name="ul1773515175502"></a><ul id="ul1773515175502"><li><strong id="b966812145216"><a name="b966812145216"></a><a name="b966812145216"></a>disabled</strong>: indicates that the backup policy is unavailable.</li><li><strong id="b166321218115217"><a name="b166321218115217"></a><a name="b166321218115217"></a>enabled</strong>: indicates that the backup policy is available.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **policy\_param**

    **Table  12**  Parameter description of field  **policy\_param**

    <a name="table61263219"></a>
    <table><thead align="left"><tr id="row27347124"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p358042504115"><a name="p358042504115"></a><a name="p358042504115"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p1059682574110"><a name="p1059682574110"></a><a name="p1059682574110"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p14596122524119"><a name="p14596122524119"></a><a name="p14596122524119"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row61239864"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p61481956"><a name="p61481956"></a><a name="p61481956"></a>common</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p58843661"><a name="p58843661"></a><a name="p58843661"></a>common_param</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p1607259"><a name="p1607259"></a><a name="p1607259"></a>General backup policy parameters, which are blank by default</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **resource**

    **Table  13**  Parameter description of field  **resource**

    <a name="table63079129"></a>
    <table><thead align="left"><tr id="row38302644"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p2023724864114"><a name="p2023724864114"></a><a name="p2023724864114"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p1025384804110"><a name="p1025384804110"></a><a name="p1025384804110"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p14253114824112"><a name="p14253114824112"></a><a name="p14253114824112"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row61682732"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p30245434"><a name="p30245434"></a><a name="p30245434"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p66494603"><a name="p66494603"></a><a name="p66494603"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p17353758"><a name="p17353758"></a><a name="p17353758"></a>ID of the object to be backed up</p>
    </td>
    </tr>
    <tr id="row21966099"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p34423584"><a name="p34423584"></a><a name="p34423584"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p31809019"><a name="p31809019"></a><a name="p31809019"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p912324712547"><a name="p912324712547"></a><a name="p912324712547"></a>Entity object type of backup objects</p>
    <p id="p26393753"><a name="p26393753"></a><a name="p26393753"></a>The value is fixed at <strong id="b1591314106214"><a name="b1591314106214"></a><a name="b1591314106214"></a>OS::Nova::Server</strong> (ECSs).</p>
    </td>
    </tr>
    <tr id="row36217193"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p47911552"><a name="p47911552"></a><a name="p47911552"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p9773913"><a name="p9773913"></a><a name="p9773913"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p53489517"><a name="p53489517"></a><a name="p53489517"></a>Backup object name</p>
    </td>
    </tr>
    <tr id="row33316617498"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p29165834920"><a name="p29165834920"></a><a name="p29165834920"></a>extra_info</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p793118819495"><a name="p793118819495"></a><a name="p793118819495"></a>Dict</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p179376884913"><a name="p179376884913"></a><a name="p179376884913"></a>Additional information about the backup object</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **scheduled\_operation\_resp**

    **Table  14**  Parameter description of field  **scheduled\_operation\_resp**

    <a name="table37683621"></a>
    <table><thead align="left"><tr id="row16553858"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p1273731419429"><a name="p1273731419429"></a><a name="p1273731419429"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p9767171464213"><a name="p9767171464213"></a><a name="p9767171464213"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p18767141454216"><a name="p18767141454216"></a><a name="p18767141454216"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row39208080"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p21737886"><a name="p21737886"></a><a name="p21737886"></a>description</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p15934571"><a name="p15934571"></a><a name="p15934571"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p37551254162655"><a name="p37551254162655"></a><a name="p37551254162655"></a>Scheduling period description</p>
    <p id="p15631866"><a name="p15631866"></a><a name="p15631866"></a>The value consists of 0 to 255 characters and must not contain a greater-than sign (&gt;) or less-than sign (&lt;).</p>
    </td>
    </tr>
    <tr id="row6469073"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p54232880"><a name="p54232880"></a><a name="p54232880"></a>enabled</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p10731020"><a name="p10731020"></a><a name="p10731020"></a>Boolean</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p5884462516271"><a name="p5884462516271"></a><a name="p5884462516271"></a>Whether the scheduling period is enabled</p>
    <p id="p63906264"><a name="p63906264"></a><a name="p63906264"></a>The default value is <strong id="b94967493416201"><a name="b94967493416201"></a><a name="b94967493416201"></a>true</strong>. If it is set to <strong id="b189463084016203"><a name="b189463084016203"></a><a name="b189463084016203"></a>false</strong>, automatic scheduling is disabled but manual scheduling is supported.</p>
    </td>
    </tr>
    <tr id="row38285471"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p14115433"><a name="p14115433"></a><a name="p14115433"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p1128424"><a name="p1128424"></a><a name="p1128424"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p919618216274"><a name="p919618216274"></a><a name="p919618216274"></a>Scheduling period name</p>
    <p id="p24293483"><a name="p24293483"></a><a name="p24293483"></a>The value consists of 1 to 255 characters and can contain only letters, digits, underscores (_), and hyphens (-).</p>
    </td>
    </tr>
    <tr id="row17314763"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p60318571"><a name="p60318571"></a><a name="p60318571"></a>operation_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p9174976"><a name="p9174976"></a><a name="p9174976"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p4975557"><a name="p4975557"></a><a name="p4975557"></a>Operation type, which can be backup </p>
    <p id="p44780014"><a name="p44780014"></a><a name="p44780014"></a>Enum:[ backup]</p>
    </td>
    </tr>
    <tr id="row366950"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p29723021"><a name="p29723021"></a><a name="p29723021"></a>operation_definition</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p61491078"><a name="p61491078"></a><a name="p61491078"></a>operation_definition</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p14721450"><a name="p14721450"></a><a name="p14721450"></a>Scheduling period parameters</p>
    <p id="p12259195075610"><a name="p12259195075610"></a><a name="p12259195075610"></a>For details, see <a href="#table40981795">Table 15</a>.</p>
    </td>
    </tr>
    <tr id="row65384190"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p61628039"><a name="p61628039"></a><a name="p61628039"></a>trigger</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p10664340"><a name="p10664340"></a><a name="p10664340"></a>trigger_resp</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p58505191"><a name="p58505191"></a><a name="p58505191"></a>Scheduling policy</p>
    <p id="p13659203818579"><a name="p13659203818579"></a><a name="p13659203818579"></a>For details, see <a href="#table20863269">Table 16</a>.</p>
    </td>
    </tr>
    <tr id="row56784672"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p36155702"><a name="p36155702"></a><a name="p36155702"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p54841609"><a name="p54841609"></a><a name="p54841609"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p12985365"><a name="p12985365"></a><a name="p12985365"></a>Scheduling period ID</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **operation\_definition**

    **Table  15**  Parameter description of field  **operation\_definition**

    <a name="table40981795"></a>
    <table><thead align="left"><tr id="row545971"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p1744192415427"><a name="p1744192415427"></a><a name="p1744192415427"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p94561243421"><a name="p94561243421"></a><a name="p94561243421"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p1647112415423"><a name="p1647112415423"></a><a name="p1647112415423"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row21317602"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p49004235"><a name="p49004235"></a><a name="p49004235"></a>max_backups</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p186311723459"><a name="p186311723459"></a><a name="p186311723459"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p23798467162729"><a name="p23798467162729"></a><a name="p23798467162729"></a>Maximum number of backups that can be automatically created for a backup object.</p>
    <p id="p57317856"><a name="p57317856"></a><a name="p57317856"></a>The value can be <strong id="b1350013383241"><a name="b1350013383241"></a><a name="b1350013383241"></a>-1</strong> or ranges from <strong id="b848144310248"><a name="b848144310248"></a><a name="b848144310248"></a>0</strong> to <strong id="b36141946182411"><a name="b36141946182411"></a><a name="b36141946182411"></a>99999</strong>. If the value is set to <strong id="b20853444145613"><a name="b20853444145613"></a><a name="b20853444145613"></a>-1</strong>, the backups will not be cleared even though the configured retained backup quantity limit is exceeded.</p>
    </td>
    </tr>
    <tr id="row46098660"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p43004004"><a name="p43004004"></a><a name="p43004004"></a>retention_duration_days</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p2525137154515"><a name="p2525137154515"></a><a name="p2525137154515"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p14389183162727"><a name="p14389183162727"></a><a name="p14389183162727"></a>Duration of retaining a backup, in days.</p>
    <p id="p33411543"><a name="p33411543"></a><a name="p33411543"></a>The value can be <strong id="b112991838192615"><a name="b112991838192615"></a><a name="b112991838192615"></a>-1</strong> or ranges from <strong id="b122991538152618"><a name="b122991538152618"></a><a name="b122991538152618"></a>0</strong> to <strong id="b1029919380267"><a name="b1029919380267"></a><a name="b1029919380267"></a>99999</strong>. If the value is set to <strong id="b82727605817"><a name="b82727605817"></a><a name="b82727605817"></a>-1</strong>, backups will not be cleared even though the configured retention duration is exceeded.</p>
    </td>
    </tr>
    <tr id="row32268434"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p63606387"><a name="p63606387"></a><a name="p63606387"></a>permanent</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p12172129204511"><a name="p12172129204511"></a><a name="p12172129204511"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p39197282"><a name="p39197282"></a><a name="p39197282"></a>Whether backups are permanently retained</p>
    </td>
    </tr>
    <tr id="row147417323116"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p1674937312"><a name="p1674937312"></a><a name="p1674937312"></a>plan_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p7741536313"><a name="p7741536313"></a><a name="p7741536313"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p2744333111"><a name="p2744333111"></a><a name="p2744333111"></a>Backup policy ID</p>
    </td>
    </tr>
    <tr id="row5857426143120"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p585710262311"><a name="p585710262311"></a><a name="p585710262311"></a>provider_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p5857182693111"><a name="p5857182693111"></a><a name="p5857182693111"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p1185714268314"><a name="p1185714268314"></a><a name="p1185714268314"></a>Backup provider ID, which specifies whether the backup object is a server or disk. This parameter has a fixed value. For CSBS, the value is <strong id="b15403111620314"><a name="b15403111620314"></a><a name="b15403111620314"></a>fc4d5750-22e7-4798-8a46-f48f62c4c1da</strong>. </p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **trigger\_resp**

    **Table  16**  Parameter description of field  **trigger\_resp**

    <a name="table20863269"></a>
    <table><thead align="left"><tr id="row41083722"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p12627339184219"><a name="p12627339184219"></a><a name="p12627339184219"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p46444398422"><a name="p46444398422"></a><a name="p46444398422"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p3644173915423"><a name="p3644173915423"></a><a name="p3644173915423"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row14816487"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p59284808"><a name="p59284808"></a><a name="p59284808"></a>properties</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p4652939"><a name="p4652939"></a><a name="p4652939"></a>trigger_properties_resp</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p41343806"><a name="p41343806"></a><a name="p41343806"></a>Scheduler properties</p>
    <p id="p8781030155810"><a name="p8781030155810"></a><a name="p8781030155810"></a>For details, see <a href="#table28343023">Table 17</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Parameter description of field  **trigger\_properties\_resp**

    **Table  17**  Parameter description of field  **trigger\_properties\_resp**

    <a name="table28343023"></a>
    <table><thead align="left"><tr id="row6676679"><th class="cellrowborder" valign="top" width="29.76%" id="mcps1.2.4.1.1"><p id="p18706554204210"><a name="p18706554204210"></a><a name="p18706554204210"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="16.67%" id="mcps1.2.4.1.2"><p id="p107211754174217"><a name="p107211754174217"></a><a name="p107211754174217"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="53.57000000000001%" id="mcps1.2.4.1.3"><p id="p13721754144211"><a name="p13721754144211"></a><a name="p13721754144211"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row5974287"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p14155245"><a name="p14155245"></a><a name="p14155245"></a>pattern</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p61010004"><a name="p61010004"></a><a name="p61010004"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p45529230162737"><a name="p45529230162737"></a><a name="p45529230162737"></a>Scheduling policy of the scheduler</p>
    <p id="p42863276"><a name="p42863276"></a><a name="p42863276"></a>The value consists of a maximum of 10,240 characters. The scheduling policy complies with iCalendar RFC 2445, but it supports only four parameters, which are <strong id="b11381749182310"><a name="b11381749182310"></a><a name="b11381749182310"></a>FREQ</strong>, <strong id="b16215852132317"><a name="b16215852132317"></a><a name="b16215852132317"></a>BYDAY</strong>, <strong id="b9119145602317"><a name="b9119145602317"></a><a name="b9119145602317"></a>BYHOUR</strong>, and <strong id="b1191295922316"><a name="b1191295922316"></a><a name="b1191295922316"></a>BYMINUTE</strong>. <strong id="b112521723247"><a name="b112521723247"></a><a name="b112521723247"></a>FREQ</strong> can be set to <strong id="b16851196102412"><a name="b16851196102412"></a><a name="b16851196102412"></a>WEEKLY</strong> and <strong id="b17546189202419"><a name="b17546189202419"></a><a name="b17546189202419"></a>DAILY</strong>, <strong id="b870561862413"><a name="b870561862413"></a><a name="b870561862413"></a>BYDAY</strong> can be set to <strong id="b5782132072416"><a name="b5782132072416"></a><a name="b5782132072416"></a>MO</strong>, <strong id="b289912229241"><a name="b289912229241"></a><a name="b289912229241"></a>TU</strong>, <strong id="b1459202512243"><a name="b1459202512243"></a><a name="b1459202512243"></a>WE</strong>, <strong id="b746652742419"><a name="b746652742419"></a><a name="b746652742419"></a>TH</strong>, <strong id="b7989132919249"><a name="b7989132919249"></a><a name="b7989132919249"></a>FR</strong>, <strong id="b1617932102418"><a name="b1617932102418"></a><a name="b1617932102418"></a>SA</strong>, and <strong id="b9277436162413"><a name="b9277436162413"></a><a name="b9277436162413"></a>SU</strong> (seven days of a week), <strong id="b1117940182412"><a name="b1117940182412"></a><a name="b1117940182412"></a>BYHOUR</strong> ranges from 0 hours to 23 hours, and <strong id="b2057724382413"><a name="b2057724382413"></a><a name="b2057724382413"></a>BYMINUTE</strong> ranges from 0 minutes to 59 minutes. The scheduling interval must not be less than 1 hour. A maximum of 24 time points are allowed in a day.</p>
    </td>
    </tr>
    <tr id="row50225165"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p41706593"><a name="p41706593"></a><a name="p41706593"></a>start_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p34121438"><a name="p34121438"></a><a name="p34121438"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p12373079"><a name="p12373079"></a><a name="p12373079"></a>Start time of the scheduler</p>
    </td>
    </tr>
    <tr id="row17192829165514"><td class="cellrowborder" valign="top" width="29.76%" headers="mcps1.2.4.1.1 "><p id="p2169629185510"><a name="p2169629185510"></a><a name="p2169629185510"></a>format</p>
    </td>
    <td class="cellrowborder" valign="top" width="16.67%" headers="mcps1.2.4.1.2 "><p id="p317519299551"><a name="p317519299551"></a><a name="p317519299551"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="53.57000000000001%" headers="mcps1.2.4.1.3 "><p id="p1718552915553"><a name="p1718552915553"></a><a name="p1718552915553"></a>Scheduler type</p>
    <p id="p58968521984"><a name="p58968521984"></a><a name="p58968521984"></a>The value is fixed at <strong id="b6313121510118"><a name="b6313121510118"></a><a name="b6313121510118"></a>ical</strong> (Internet calendar).</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Example response

    ```
    {
      "policy" : {
        "status" : "disabled",
        "provider_id" : "fc4d5750-22e7-4798-8a46-f48f62c4c1da",
        "description" : "",
        "parameters" : {
          "common" : {
          }
        },
        "scheduled_operations" : [ {
          "description" : "My backup policy ",
          "enabled" : true,
          "trigger" : {
            "properties" : {
              "pattern" : "BEGIN:VCALENDAR\r\nBEGIN:VEVENT\r\nRRULE:FREQ=WEEKLY;BYDAY=TH;BYHOUR=12;BYMINUTE=27\r\nEND:VEVENT\r\nEND:VCALENDAR\r\n",
              "start_time" : "2017-04-09 14:31:25",
              "format" : "ical"
            }
          },
          "operation_definition" : {
            "provider_id" : "fc4d5750-22e7-4798-8a46-f48f62c4c1da",
            "plan_id" : "17e2b861-3a35-434d-afbb-073d5cd5af08",
            "max_backups" : "20",
            "retention_duration_days" : "-1",
            "permanent" : "False",
            
          },
          "operation_type" : "backup",
          "id" : "fed3c8f1-7b6e-4e24-b1ad-473838bad569",
          "name" : "my-backup-policy"
        }
    ,
              "format" : "ical"
       ],
        "id" : "17e2b861-3a35-434d-afbb-073d5cd5af08",
        "name" : "my-plan",
        "parameters" : {
          "common" : {
          }
        },
        "created_at" : "2017-04-09T14:31:25.504569",
        "project_id" : "0c89d4e457c3401a89c65420fd45f3a2",
        "resources" : [ {
          "type" : "OS::Nova::Server",
          "id" : "8421f405-1334-4206-b71c-b3f64d39abc4",
          "name" : "wqeq3",
          "extra_info" : {
        }
        } ]
      }
    }
    ```


## Status Codes<a name="section63753158"></a>

-   Normal

    <a name="table44126420"></a>
    <table><thead align="left"><tr id="row52255169"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p4810259"><a name="p4810259"></a><a name="p4810259"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p54086714"><a name="p54086714"></a><a name="p54086714"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row18947742"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p58372134"><a name="p58372134"></a><a name="p58372134"></a>200</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p30522427"><a name="p30522427"></a><a name="p30522427"></a>OK</p>
    </td>
    </tr>
    </tbody>
    </table>

-   Abnormal

    <a name="table56397508"></a>
    <table><thead align="left"><tr id="row6210550"><th class="cellrowborder" valign="top" width="42.42%" id="mcps1.1.3.1.1"><p id="p33292546"><a name="p33292546"></a><a name="p33292546"></a>Status Code</p>
    </th>
    <th class="cellrowborder" valign="top" width="57.58%" id="mcps1.1.3.1.2"><p id="p12341702"><a name="p12341702"></a><a name="p12341702"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row60153835"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p40622489"><a name="p40622489"></a><a name="p40622489"></a>400</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p2087287"><a name="p2087287"></a><a name="p2087287"></a>Invalid request parameters.</p>
    </td>
    </tr>
    <tr id="row18785583"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p45237273"><a name="p45237273"></a><a name="p45237273"></a>401</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p40340487"><a name="p40340487"></a><a name="p40340487"></a>Authentication failed.</p>
    </td>
    </tr>
    <tr id="row27520067"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p14532979"><a name="p14532979"></a><a name="p14532979"></a>403</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p36320668"><a name="p36320668"></a><a name="p36320668"></a>No operation permission.</p>
    </td>
    </tr>
    <tr id="row58450557"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p36874637"><a name="p36874637"></a><a name="p36874637"></a>404</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p34055593"><a name="p34055593"></a><a name="p34055593"></a>Requested object not found.</p>
    </td>
    </tr>
    <tr id="row38064888"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p63357074"><a name="p63357074"></a><a name="p63357074"></a>500</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p31649389"><a name="p31649389"></a><a name="p31649389"></a>Service internal error.</p>
    </td>
    </tr>
    <tr id="row16409050"><td class="cellrowborder" valign="top" width="42.42%" headers="mcps1.1.3.1.1 "><p id="p54064697"><a name="p54064697"></a><a name="p54064697"></a>503</p>
    </td>
    <td class="cellrowborder" valign="top" width="57.58%" headers="mcps1.1.3.1.2 "><p id="p17164332"><a name="p17164332"></a><a name="p17164332"></a>Service unavailable.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Error Codes<a name="section61541938486"></a>

For details, see  [Error Codes](error-codes.md).


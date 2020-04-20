# Querying Details About DB Instances<a name="rds_01_0004"></a>

## Function<a name="section44230431101549"></a>

This API is used to query DB instances according to search criteria.

-   Learn how to  [authorize and authenticate](authentication.md)  this API before using it.
-   Before calling this API, obtain the required  [region and endpoint](https://docs.otc.t-systems.com/en-us/endpoint/index.html).

## URI<a name="section31729879101549"></a>

-   URI format

    GET https://\{_Endpoint_\}/v3/\{project\_id\}/instances?id=\{id\}&name=\{name\}&type=\{type\}&datastore\_type=\{datastore\_type\}&vpc\_id=\{vpc\_id\}&subnet\_id=\{subnet\_id\}&offset=\{offset\}&limit=\{limit\}

-   Example
    -   Querying all DB instances

        https://rds.eu-de.otc.t-systems.com/v3/97b026aa9cc4417888c14c84a1ad9860/instances

    -   Querying DB instances based on specified conditions

        https://rds.eu-de.otc.t-systems.com/v3/97b026aa9cc4417888c14c84a1ad9860/instances?id=ed7cc6166ec24360a5ed5c5c9c2ed726in01&name=hy&type=Ha&datastore\_type=MySQL&vpc\_id=19e5d45d-70fd-4a91-87e9-b27e71c9891f&subnet\_id=bd51fb45-2dcb-4296-8783-8623bfe89bb7&offset=0&limit=10


-   Parameter description

    **Table  1**  Parameter description

    <a name="table23140016101549"></a>
    <table><thead align="left"><tr id="row27795795101549"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.5.1.1"><p id="p36866898101549"><a name="p36866898101549"></a><a name="p36866898101549"></a><strong id="b93591420113513"><a name="b93591420113513"></a><a name="b93591420113513"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="13%" id="mcps1.2.5.1.2"><p id="p156174610411"><a name="p156174610411"></a><a name="p156174610411"></a><strong id="b16291622193519"><a name="b16291622193519"></a><a name="b16291622193519"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25.14%" id="mcps1.2.5.1.3"><p id="p33428750101549"><a name="p33428750101549"></a><a name="p33428750101549"></a><strong id="b17801142220351"><a name="b17801142220351"></a><a name="b17801142220351"></a>Mandatory</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="44.86%" id="mcps1.2.5.1.4"><p id="p23374190101549"><a name="p23374190101549"></a><a name="p23374190101549"></a><strong id="b1867715230358"><a name="b1867715230358"></a><a name="b1867715230358"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row14261210101549"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p104922035165518"><a name="p104922035165518"></a><a name="p104922035165518"></a>project_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p1956194615414"><a name="p1956194615414"></a><a name="p1956194615414"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.14%" headers="mcps1.2.5.1.3 "><p id="p18047737101549"><a name="p18047737101549"></a><a name="p18047737101549"></a>Yes</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.86%" headers="mcps1.2.5.1.4 "><p id="p52580603101549"><a name="p52580603101549"></a><a name="p52580603101549"></a>Specifies the project ID of a tenant in a region.</p>
    <p id="p16476914175718"><a name="p16476914175718"></a><a name="p16476914175718"></a>For details about how to obtain the project ID, see <a href="obtaining-a-project-id.md">Obtaining a Project ID</a>.</p>
    </td>
    </tr>
    <tr id="row197844933113"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p84691445594"><a name="p84691445594"></a><a name="p84691445594"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p8572046164115"><a name="p8572046164115"></a><a name="p8572046164115"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.14%" headers="mcps1.2.5.1.3 "><p id="p346994410599"><a name="p346994410599"></a><a name="p346994410599"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.86%" headers="mcps1.2.5.1.4 "><p id="p84691144145915"><a name="p84691144145915"></a><a name="p84691144145915"></a>Specifies the DB instance ID.</p>
    <p id="p0469164495913"><a name="p0469164495913"></a><a name="p0469164495913"></a>The asterisk (*) is reserved for the system. If the instance ID starts with *, it indicates that fuzzy match is performed based on the value following * Otherwise, the exact match is performed based on the instance ID. The value cannot contain only asterisks (*).</p>
    </td>
    </tr>
    <tr id="row2489615125917"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p16469194410599"><a name="p16469194410599"></a><a name="p16469194410599"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p857164618412"><a name="p857164618412"></a><a name="p857164618412"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.14%" headers="mcps1.2.5.1.3 "><p id="p6469124415911"><a name="p6469124415911"></a><a name="p6469124415911"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.86%" headers="mcps1.2.5.1.4 "><p id="p946944412596"><a name="p946944412596"></a><a name="p946944412596"></a>Specifies the DB instance name.</p>
    <p id="p2469164416591"><a name="p2469164416591"></a><a name="p2469164416591"></a>The asterisk (*) is reserved for the system. If the instance name starts with *, it indicates that fuzzy match is performed based on the value following * Otherwise, the exact match is performed based on the instance name. The value cannot contain only asterisks (*).</p>
    </td>
    </tr>
    <tr id="row1525110198591"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p1773813251016"><a name="p1773813251016"></a><a name="p1773813251016"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p15734616412"><a name="p15734616412"></a><a name="p15734616412"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.14%" headers="mcps1.2.5.1.3 "><p id="p12738925418"><a name="p12738925418"></a><a name="p12738925418"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.86%" headers="mcps1.2.5.1.4 "><p id="p573892515118"><a name="p573892515118"></a><a name="p573892515118"></a>Specifies the instance type based query. The value is <strong id="b7198194835318"><a name="b7198194835318"></a><a name="b7198194835318"></a>Single</strong>, <strong id="b261715012533"><a name="b261715012533"></a><a name="b261715012533"></a>Ha</strong>, or <strong id="b99511153125320"><a name="b99511153125320"></a><a name="b99511153125320"></a>Replica</strong>, which correspond to single instance, primary/standby instances, and read replica, respectively.</p>
    </td>
    </tr>
    <tr id="row4676255803"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p373852511110"><a name="p373852511110"></a><a name="p373852511110"></a>datastore_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p75754610414"><a name="p75754610414"></a><a name="p75754610414"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.14%" headers="mcps1.2.5.1.3 "><p id="p373812511115"><a name="p373812511115"></a><a name="p373812511115"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.86%" headers="mcps1.2.5.1.4 "><p id="p1318733012217"><a name="p1318733012217"></a><a name="p1318733012217"></a>Specifies the database type. Its value can be any of the following and is case-sensitive:</p>
    <a name="ul924933143511"></a><a name="ul924933143511"></a><ul id="ul924933143511"><li>MySQL</li><li>PostgreSQL</li><li>SQLServer</li></ul>
    </td>
    </tr>
    <tr id="row391114581019"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p873811251313"><a name="p873811251313"></a><a name="p873811251313"></a>vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p75794618416"><a name="p75794618416"></a><a name="p75794618416"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.14%" headers="mcps1.2.5.1.3 "><p id="p147381257113"><a name="p147381257113"></a><a name="p147381257113"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.86%" headers="mcps1.2.5.1.4 "><p id="p87381125112"><a name="p87381125112"></a><a name="p87381125112"></a>Specifies the VPC ID.</p>
    <a name="ul475921618452"></a><a name="ul475921618452"></a><ul id="ul475921618452"><li>Method 1: Log in to VPC console and view the VPC ID in the VPC details.</li><li>Method 2: See the "Querying VPCs" section in the <em id="rds_01_0002_i842352697165629"><a name="rds_01_0002_i842352697165629"></a><a name="rds_01_0002_i842352697165629"></a>Virtual Private Cloud API Reference</em>.</li></ul>
    </td>
    </tr>
    <tr id="row57790155118"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p173811251019"><a name="p173811251019"></a><a name="p173811251019"></a>subnet_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p1757194617418"><a name="p1757194617418"></a><a name="p1757194617418"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.14%" headers="mcps1.2.5.1.3 "><p id="p073882514117"><a name="p073882514117"></a><a name="p073882514117"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.86%" headers="mcps1.2.5.1.4 "><p id="p7738172511118"><a name="p7738172511118"></a><a name="p7738172511118"></a>Specifies the network ID of the subnet.</p>
    <a name="ul375971611456"></a><a name="ul375971611456"></a><ul id="ul375971611456"><li>Method 1: Log in to VPC console and click the target subnet on the <strong id="rds_01_0002_b4101174416409"><a name="rds_01_0002_b4101174416409"></a><a name="rds_01_0002_b4101174416409"></a>Subnets</strong> page. You can view the network ID on the displayed page.</li><li>Method 2: See the "Querying Subnets" section in the <em id="rds_01_0002_i102188587418"><a name="rds_01_0002_i102188587418"></a><a name="rds_01_0002_i102188587418"></a>Virtual Private Cloud API Reference</em>.</li></ul>
    </td>
    </tr>
    <tr id="row378505943118"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p18469644135918"><a name="p18469644135918"></a><a name="p18469644135918"></a>offset</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p20571146174113"><a name="p20571146174113"></a><a name="p20571146174113"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.14%" headers="mcps1.2.5.1.3 "><p id="p64691544165913"><a name="p64691544165913"></a><a name="p64691544165913"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.86%" headers="mcps1.2.5.1.4 "><p id="p184691344165912"><a name="p184691344165912"></a><a name="p184691344165912"></a>Specifies the index position. If <strong id="b70205942519474"><a name="b70205942519474"></a><a name="b70205942519474"></a>offset</strong> is set to <em id="i84235269720751"><a name="i84235269720751"></a><a name="i84235269720751"></a>N</em>, the resource query starts from the N+1 piece of data. The value is <strong id="b84235270620630"><a name="b84235270620630"></a><a name="b84235270620630"></a>0</strong> by default, indicating that the query starts from the first piece of data. The value must be a positive number.</p>
    </td>
    </tr>
    <tr id="row31182243218"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.5.1.1 "><p id="p646954415917"><a name="p646954415917"></a><a name="p646954415917"></a>limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="13%" headers="mcps1.2.5.1.2 "><p id="p125714615419"><a name="p125714615419"></a><a name="p125714615419"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.14%" headers="mcps1.2.5.1.3 "><p id="p7469444115910"><a name="p7469444115910"></a><a name="p7469444115910"></a>No</p>
    </td>
    <td class="cellrowborder" valign="top" width="44.86%" headers="mcps1.2.5.1.4 "><p id="p19469194465917"><a name="p19469194465917"></a><a name="p19469194465917"></a>Specifies the number of records to be queried. The default value is <strong id="b78578273159"><a name="b78578273159"></a><a name="b78578273159"></a>100</strong>. The value cannot be a negative number. The minimum value is <strong id="b99981031141518"><a name="b99981031141518"></a><a name="b99981031141518"></a>1</strong> and the maximum value is <strong id="b9972173720152"><a name="b9972173720152"></a><a name="b9972173720152"></a>100</strong>.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Request<a name="section28070818101549"></a>

None

## Response<a name="section62531952101549"></a>

-   Normal response

    **Table  2**  Parameter description

    <a name="table1344412393258"></a>
    <table><thead align="left"><tr id="row849512397255"><th class="cellrowborder" valign="top" width="32.653265326532654%" id="mcps1.2.4.1.1"><p id="p1349533912516"><a name="p1349533912516"></a><a name="p1349533912516"></a><strong id="b6925212132317"><a name="b6925212132317"></a><a name="b6925212132317"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.673367336733676%" id="mcps1.2.4.1.2"><p id="p174959399251"><a name="p174959399251"></a><a name="p174959399251"></a><strong id="b16675874245"><a name="b16675874245"></a><a name="b16675874245"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.673367336733676%" id="mcps1.2.4.1.3"><p id="p174951639112515"><a name="p174951639112515"></a><a name="p174951639112515"></a><strong id="b16524190243"><a name="b16524190243"></a><a name="b16524190243"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row17495183914254"><td class="cellrowborder" valign="top" width="32.653265326532654%" headers="mcps1.2.4.1.1 "><p id="p249563917251"><a name="p249563917251"></a><a name="p249563917251"></a>instances</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.673367336733676%" headers="mcps1.2.4.1.2 "><p id="p15495133902512"><a name="p15495133902512"></a><a name="p15495133902512"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.673367336733676%" headers="mcps1.2.4.1.3 "><p id="p4496103920258"><a name="p4496103920258"></a><a name="p4496103920258"></a>Indicates the DB instance information.</p>
    <p id="p193231246205415"><a name="p193231246205415"></a><a name="p193231246205415"></a>For details, see <a href="#table2058713718267">Table 3</a>.</p>
    </td>
    </tr>
    <tr id="row1449612393259"><td class="cellrowborder" valign="top" width="32.653265326532654%" headers="mcps1.2.4.1.1 "><p id="p1249612391257"><a name="p1249612391257"></a><a name="p1249612391257"></a>total_count</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.673367336733676%" headers="mcps1.2.4.1.2 "><p id="p749613911252"><a name="p749613911252"></a><a name="p749613911252"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.673367336733676%" headers="mcps1.2.4.1.3 "><p id="p1549693920256"><a name="p1549693920256"></a><a name="p1549693920256"></a>Indicates the total number of resources.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  3**  instances field data structure description

    <a name="table2058713718267"></a>
    <table><thead align="left"><tr id="row1012214832618"><th class="cellrowborder" valign="top" width="23.23%" id="mcps1.2.4.1.1"><p id="p312219812612"><a name="p312219812612"></a><a name="p312219812612"></a><strong id="b2522113910257"><a name="b2522113910257"></a><a name="b2522113910257"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="25.25%" id="mcps1.2.4.1.2"><p id="p91221985265"><a name="p91221985265"></a><a name="p91221985265"></a><strong id="b145294404251"><a name="b145294404251"></a><a name="b145294404251"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="51.519999999999996%" id="mcps1.2.4.1.3"><p id="p111226816261"><a name="p111226816261"></a><a name="p111226816261"></a><strong id="b54721741152510"><a name="b54721741152510"></a><a name="b54721741152510"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row12122489261"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p51221889266"><a name="p51221889266"></a><a name="p51221889266"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p1612213892617"><a name="p1612213892617"></a><a name="p1612213892617"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.519999999999996%" headers="mcps1.2.4.1.3 "><p id="p412220818265"><a name="p412220818265"></a><a name="p412220818265"></a>Indicates the DB instance ID.</p>
    </td>
    </tr>
    <tr id="row512218162619"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p7122118182612"><a name="p7122118182612"></a><a name="p7122118182612"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p21225815262"><a name="p21225815262"></a><a name="p21225815262"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.519999999999996%" headers="mcps1.2.4.1.3 "><p id="p2122198142610"><a name="p2122198142610"></a><a name="p2122198142610"></a>Indicates the created DB instance name.</p>
    </td>
    </tr>
    <tr id="row11222822616"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p4123198202614"><a name="p4123198202614"></a><a name="p4123198202614"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p1912318818265"><a name="p1912318818265"></a><a name="p1912318818265"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.519999999999996%" headers="mcps1.2.4.1.3 "><p id="p121231486267"><a name="p121231486267"></a><a name="p121231486267"></a>Indicates the DB instance status.</p>
    <p id="p14123381266"><a name="p14123381266"></a><a name="p14123381266"></a>Value:</p>
    <p id="p121235818262"><a name="p121235818262"></a><a name="p121235818262"></a>If the value is <strong id="b84235270616547_1"><a name="b84235270616547_1"></a><a name="b84235270616547_1"></a>BUILD</strong>, the instance is being created.</p>
    <p id="p1712312817262"><a name="p1712312817262"></a><a name="p1712312817262"></a>If the value is <strong id="b842352706165415"><a name="b842352706165415"></a><a name="b842352706165415"></a>ACTIVE</strong>, the instance is normal.</p>
    <p id="p101231892614"><a name="p101231892614"></a><a name="p101231892614"></a>If the value is <strong id="b842352706165427"><a name="b842352706165427"></a><a name="b842352706165427"></a>FAILED</strong>, the instance is abnormal.</p>
    <p id="p16123485263"><a name="p16123485263"></a><a name="p16123485263"></a>If the value is <strong id="b84235270616547_3"><a name="b84235270616547_3"></a><a name="b84235270616547_3"></a>MODIFYING</strong>, the instance is being scaled up.</p>
    <p id="p111231284264"><a name="p111231284264"></a><a name="p111231284264"></a>If the value is <strong id="b8630202172718"><a name="b8630202172718"></a><a name="b8630202172718"></a>REBOOTING</strong>, the instance is being rebooted.</p>
    <p id="p41231185269"><a name="p41231185269"></a><a name="p41231185269"></a>If the value is <strong id="b84235270616547_7"><a name="b84235270616547_7"></a><a name="b84235270616547_7"></a>RESTORING</strong>, the instance is being restored.</p>
    <p id="p91231389269"><a name="p91231389269"></a><a name="p91231389269"></a>If the value is <strong id="b5168101082716"><a name="b5168101082716"></a><a name="b5168101082716"></a>MODIFYING INSTANCE TYPE</strong>, the instance is changing from primary to standby.</p>
    <p id="p112378152610"><a name="p112378152610"></a><a name="p112378152610"></a>If the value is <strong id="b1148214486276"><a name="b1148214486276"></a><a name="b1148214486276"></a>SWITCHOVER</strong>, the primary/standby switchover is being performed.</p>
    <p id="p171233820263"><a name="p171233820263"></a><a name="p171233820263"></a>If the value is <strong id="b65135702810"><a name="b65135702810"></a><a name="b65135702810"></a>MIGRATING</strong>, the instance is being migrated.</p>
    <p id="p612478102610"><a name="p612478102610"></a><a name="p612478102610"></a>If the value is <strong id="b753162915291"><a name="b753162915291"></a><a name="b753162915291"></a>BACKING UP</strong>, the instance is being backed up.</p>
    <p id="p1412416819260"><a name="p1412416819260"></a><a name="p1412416819260"></a>If the value is <strong id="b16596103714309"><a name="b16596103714309"></a><a name="b16596103714309"></a>MODIFYING DATABASE PORT</strong>, the database port is being changed.</p>
    </td>
    </tr>
    <tr id="row20124108152614"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p131247815269"><a name="p131247815269"></a><a name="p131247815269"></a>private_ips</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p6124686265"><a name="p6124686265"></a><a name="p6124686265"></a>List&lt;String&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.519999999999996%" headers="mcps1.2.4.1.3 "><p id="p812417819261"><a name="p812417819261"></a><a name="p812417819261"></a>Indicates the private IP address list. It is a blank string until an ECS is created.</p>
    </td>
    </tr>
    <tr id="row5124128112611"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p111248842616"><a name="p111248842616"></a><a name="p111248842616"></a>public_ips</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p1212418810269"><a name="p1212418810269"></a><a name="p1212418810269"></a>List&lt;String&gt;</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.519999999999996%" headers="mcps1.2.4.1.3 "><p id="p7124128142615"><a name="p7124128142615"></a><a name="p7124128142615"></a>Indicates the public IP address list.</p>
    </td>
    </tr>
    <tr id="row312488192611"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p512416818269"><a name="p512416818269"></a><a name="p512416818269"></a>port</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p6124386267"><a name="p6124386267"></a><a name="p6124386267"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.519999999999996%" headers="mcps1.2.4.1.3 "><p id="p201241815264"><a name="p201241815264"></a><a name="p201241815264"></a>Indicates the database port number.</p>
    <a name="ul164621729141114"></a><a name="ul164621729141114"></a><ul id="ul164621729141114"><li>The MySQL database port ranges from 1024 to 65535 (excluding 12017 and 33071, which are occupied by the RDS system and cannot be used).</li><li>The PostgreSQL database port ranges from 2100 to 9500.</li><li>The Microsoft SQL Server database port is 1433 or ranges from 2100 to 9500 (excluding 5355 and 5985). </li></ul>
    <p id="p1172615390340"><a name="p1172615390340"></a><a name="p1172615390340"></a>If this parameter is not set, the default value is as follows:</p>
    <a name="ul13855195423417"></a><a name="ul13855195423417"></a><ul id="ul13855195423417"><li>For MySQL, the default value is <strong id="rds_01_0002_b1829614472613"><a name="rds_01_0002_b1829614472613"></a><a name="rds_01_0002_b1829614472613"></a>3306</strong>.</li><li>For PostgreSQL, the default value is <strong id="rds_01_0002_b13817121574"><a name="rds_01_0002_b13817121574"></a><a name="rds_01_0002_b13817121574"></a>5432</strong>.</li><li>For Microsoft SQL Server, the default value is <strong id="rds_01_0002_b1633152143014"><a name="rds_01_0002_b1633152143014"></a><a name="rds_01_0002_b1633152143014"></a>1433</strong>.</li></ul>
    </td>
    </tr>
    <tr id="row712411820262"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p101241481266"><a name="p101241481266"></a><a name="p101241481266"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p31241786269"><a name="p31241786269"></a><a name="p31241786269"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.519999999999996%" headers="mcps1.2.4.1.3 "><p id="p12124198192616"><a name="p12124198192616"></a><a name="p12124198192616"></a>The value is <strong id="b11419161415322"><a name="b11419161415322"></a><a name="b11419161415322"></a>Single</strong>, <strong id="b1742021473220"><a name="b1742021473220"></a><a name="b1742021473220"></a>Ha</strong>, or <strong id="b942051416325"><a name="b942051416325"></a><a name="b942051416325"></a>Replica</strong>, which correspond to single instance, primary/standby instances, and read replica, respectively.</p>
    </td>
    </tr>
    <tr id="row112413820261"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p191242814263"><a name="p191242814263"></a><a name="p191242814263"></a>ha</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p16124148172612"><a name="p16124148172612"></a><a name="p16124148172612"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.519999999999996%" headers="mcps1.2.4.1.3 "><p id="p1612513852611"><a name="p1612513852611"></a><a name="p1612513852611"></a>Indicates the primary/standby DB instance information. Returned only when you obtain a primary/standby DB instance list.</p>
    <p id="p769251117558"><a name="p769251117558"></a><a name="p769251117558"></a>For details, see <a href="#table7736377269">Table 4</a>.</p>
    </td>
    </tr>
    <tr id="row31251489265"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p4125583264"><a name="p4125583264"></a><a name="p4125583264"></a>region</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p4125780262"><a name="p4125780262"></a><a name="p4125780262"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.519999999999996%" headers="mcps1.2.4.1.3 "><p id="p21253816269"><a name="p21253816269"></a><a name="p21253816269"></a>Indicates the region where the DB instance is deployed.</p>
    </td>
    </tr>
    <tr id="row312513892610"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p121253811264"><a name="p121253811264"></a><a name="p121253811264"></a>datastore</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p10125688266"><a name="p10125688266"></a><a name="p10125688266"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.519999999999996%" headers="mcps1.2.4.1.3 "><p id="p112510816261"><a name="p112510816261"></a><a name="p112510816261"></a>Indicates the database information.</p>
    <p id="p1167093118552"><a name="p1167093118552"></a><a name="p1167093118552"></a>For details, see <a href="#table187591675262">Table 5</a>.</p>
    </td>
    </tr>
    <tr id="row1812568112610"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p1012518822614"><a name="p1012518822614"></a><a name="p1012518822614"></a>created</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p14125178152611"><a name="p14125178152611"></a><a name="p14125178152611"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.519999999999996%" headers="mcps1.2.4.1.3 "><p id="p1512538142614"><a name="p1512538142614"></a><a name="p1512538142614"></a>Indicates the creation time in the "yyyy-mm-ddThh:mm:ssZ" format.</p>
    <p id="p13125168192618"><a name="p13125168192618"></a><a name="p13125168192618"></a><strong id="b842352706151812"><a name="b842352706151812"></a><a name="b842352706151812"></a>T</strong> is the separator between the calendar and the hourly notation of time. <strong id="b842352706153833"><a name="b842352706153833"></a><a name="b842352706153833"></a>Z</strong> indicates the time zone offset.</p>
    <p id="p112518202611"><a name="p112518202611"></a><a name="p112518202611"></a>The value is empty when the DB instance is being created. After the DB instance is created, the value is not empty.</p>
    </td>
    </tr>
    <tr id="row181263892618"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p4126128202612"><a name="p4126128202612"></a><a name="p4126128202612"></a>updated</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p18126380262"><a name="p18126380262"></a><a name="p18126380262"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.519999999999996%" headers="mcps1.2.4.1.3 "><p id="p20126481268"><a name="p20126481268"></a><a name="p20126481268"></a>Indicates the update time. The format is the same as that of the <strong id="b842352706111518"><a name="b842352706111518"></a><a name="b842352706111518"></a>created</strong> field.</p>
    <p id="p91260812610"><a name="p91260812610"></a><a name="p91260812610"></a>The value is empty when the DB instance is being created. After the DB instance is created, the value is not empty.</p>
    </td>
    </tr>
    <tr id="row1512615882612"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p812613816267"><a name="p812613816267"></a><a name="p812613816267"></a>db_user_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p21261862611"><a name="p21261862611"></a><a name="p21261862611"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.519999999999996%" headers="mcps1.2.4.1.3 "><p id="p21263832619"><a name="p21263832619"></a><a name="p21263832619"></a>Indicates the default username.</p>
    </td>
    </tr>
    <tr id="row131261785260"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p141261383269"><a name="p141261383269"></a><a name="p141261383269"></a>vpc_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p5126186261"><a name="p5126186261"></a><a name="p5126186261"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.519999999999996%" headers="mcps1.2.4.1.3 "><p id="p8126198102610"><a name="p8126198102610"></a><a name="p8126198102610"></a>Indicates the VPC ID.</p>
    </td>
    </tr>
    <tr id="row1712617817268"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p912611812618"><a name="p912611812618"></a><a name="p912611812618"></a>subnet_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p412610862610"><a name="p412610862610"></a><a name="p412610862610"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.519999999999996%" headers="mcps1.2.4.1.3 "><p id="p1512628132610"><a name="p1512628132610"></a><a name="p1512628132610"></a>Indicates the network ID of the subnet.</p>
    </td>
    </tr>
    <tr id="row71261889261"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p5126158132618"><a name="p5126158132618"></a><a name="p5126158132618"></a>security_group_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p1412648162614"><a name="p1412648162614"></a><a name="p1412648162614"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.519999999999996%" headers="mcps1.2.4.1.3 "><p id="p312698162616"><a name="p312698162616"></a><a name="p312698162616"></a>Indicates the security group ID.</p>
    </td>
    </tr>
    <tr id="row1712688102610"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p6126178152619"><a name="p6126178152619"></a><a name="p6126178152619"></a>flavor_ref</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p712778112619"><a name="p712778112619"></a><a name="p712778112619"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.519999999999996%" headers="mcps1.2.4.1.3 "><p id="p19127185266"><a name="p19127185266"></a><a name="p19127185266"></a>Indicates the specification code.</p>
    </td>
    </tr>
    <tr id="row10127989269"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p91273811266"><a name="p91273811266"></a><a name="p91273811266"></a>volume</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p19127583260"><a name="p19127583260"></a><a name="p19127583260"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.519999999999996%" headers="mcps1.2.4.1.3 "><p id="p15127108132618"><a name="p15127108132618"></a><a name="p15127108132618"></a>Indicates the volume information.</p>
    <p id="p146713272134"><a name="p146713272134"></a><a name="p146713272134"></a>For details, see <a href="#table14771167122611">Table 6</a>.</p>
    </td>
    </tr>
    <tr id="row181274882618"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p212715818262"><a name="p212715818262"></a><a name="p212715818262"></a>switch_strategy</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p71271687262"><a name="p71271687262"></a><a name="p71271687262"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.519999999999996%" headers="mcps1.2.4.1.3 "><p id="p14127148202616"><a name="p14127148202616"></a><a name="p14127148202616"></a>Indicates the database switchover policy. The value can be <strong id="b842352706111711"><a name="b842352706111711"></a><a name="b842352706111711"></a>reliability</strong> or <strong id="b842352706111714"><a name="b842352706111714"></a><a name="b842352706111714"></a>availability</strong>, indicating the reliability first and availability first, respectively.</p>
    </td>
    </tr>
    <tr id="row13127118172614"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p13127178112618"><a name="p13127178112618"></a><a name="p13127178112618"></a>backup_strategy</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p1112713817269"><a name="p1112713817269"></a><a name="p1112713817269"></a>Object</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.519999999999996%" headers="mcps1.2.4.1.3 "><p id="p812798122620"><a name="p812798122620"></a><a name="p812798122620"></a>Indicates the backup policy.</p>
    <p id="p11861938121316"><a name="p11861938121316"></a><a name="p11861938121316"></a>For details, see <a href="#table578797132615">Table 7</a>.</p>
    </td>
    </tr>
    <tr id="row41275872611"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p212717819265"><a name="p212717819265"></a><a name="p212717819265"></a>maintenance_window</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p10128148162614"><a name="p10128148162614"></a><a name="p10128148162614"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.519999999999996%" headers="mcps1.2.4.1.3 "><p id="p17128168152618"><a name="p17128168152618"></a><a name="p17128168152618"></a>Indicates the start time of the maintenance time window in the UTC format.</p>
    </td>
    </tr>
    <tr id="row712828162618"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p1812858152614"><a name="p1812858152614"></a><a name="p1812858152614"></a>nodes</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p195351922184915"><a name="p195351922184915"></a><a name="p195351922184915"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.519999999999996%" headers="mcps1.2.4.1.3 "><p id="p1512810892618"><a name="p1512810892618"></a><a name="p1512810892618"></a>Indicates the primary/standby DB instance information.</p>
    <p id="p118919506137"><a name="p118919506137"></a><a name="p118919506137"></a>For details, see <a href="#table1179987152611">Table 8</a>.</p>
    </td>
    </tr>
    <tr id="row212815832613"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p012888122618"><a name="p012888122618"></a><a name="p012888122618"></a>related_instance</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p18380920114911"><a name="p18380920114911"></a><a name="p18380920114911"></a>Array of objects</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.519999999999996%" headers="mcps1.2.4.1.3 "><p id="p161289862617"><a name="p161289862617"></a><a name="p161289862617"></a>Indicates the list of associated DB instances.</p>
    <p id="p33188091418"><a name="p33188091418"></a><a name="p33188091418"></a>For details, see <a href="#table15816167142613">Table 9</a>.</p>
    </td>
    </tr>
    <tr id="row3128118202611"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p1212817822619"><a name="p1212817822619"></a><a name="p1212817822619"></a>disk_encryption_id</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p101284862612"><a name="p101284862612"></a><a name="p101284862612"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.519999999999996%" headers="mcps1.2.4.1.3 "><p id="p11128168122612"><a name="p11128168122612"></a><a name="p11128168122612"></a>Indicates the disk encryption key ID.</p>
    </td>
    </tr>
    <tr id="row10128384263"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p14128582264"><a name="p14128582264"></a><a name="p14128582264"></a>time_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="25.25%" headers="mcps1.2.4.1.2 "><p id="p171288842614"><a name="p171288842614"></a><a name="p171288842614"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.519999999999996%" headers="mcps1.2.4.1.3 "><p id="p1012858132612"><a name="p1012858132612"></a><a name="p1012858132612"></a>Indicates the time zone.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  4**  ha field data structure description

    <a name="table7736377269"></a>
    <table><thead align="left"><tr id="row01299822617"><th class="cellrowborder" valign="top" width="23.23%" id="mcps1.2.4.1.1"><p id="p5130208112619"><a name="p5130208112619"></a><a name="p5130208112619"></a><strong id="b1278276876"><a name="b1278276876"></a><a name="b1278276876"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.220000000000002%" id="mcps1.2.4.1.2"><p id="p6130118162616"><a name="p6130118162616"></a><a name="p6130118162616"></a><strong id="b1528075703"><a name="b1528075703"></a><a name="b1528075703"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="54.55%" id="mcps1.2.4.1.3"><p id="p1813038172617"><a name="p1813038172617"></a><a name="p1813038172617"></a><strong id="b1679499161"><a name="b1679499161"></a><a name="b1679499161"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row131308832618"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p1413038202617"><a name="p1413038202617"></a><a name="p1413038202617"></a>replication_mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.2 "><p id="p151302812612"><a name="p151302812612"></a><a name="p151302812612"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.55%" headers="mcps1.2.4.1.3 "><p id="p12130789263"><a name="p12130789263"></a><a name="p12130789263"></a>Indicates the replication mode for the standby DB instance.</p>
    <p id="p613098162616"><a name="p613098162616"></a><a name="p613098162616"></a>The value cannot be empty.</p>
    <a name="ul30551132181655"></a><a name="ul30551132181655"></a><ul id="ul30551132181655"><li>For MySQL, the value is <strong id="b2884192213316"><a name="b2884192213316"></a><a name="b2884192213316"></a>async</strong> or <strong id="b158841922339"><a name="b158841922339"></a><a name="b158841922339"></a>semisync</strong>.</li><li>For PostgreSQL, the value is <strong id="b688817221735"><a name="b688817221735"></a><a name="b688817221735"></a>async</strong> or <strong id="b128881122337"><a name="b128881122337"></a><a name="b128881122337"></a>sync</strong>.</li><li>For Microsoft SQL Server, the value is <strong id="b20893122216318"><a name="b20893122216318"></a><a name="b20893122216318"></a>sync</strong>.</li></ul>
    <div class="note" id="note58913671181655"><a name="note58913671181655"></a><a name="note58913671181655"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul60460995181655"></a><a name="ul60460995181655"></a><ul id="ul60460995181655"><li><strong id="b7901132216310"><a name="b7901132216310"></a><a name="b7901132216310"></a>async</strong> indicates the asynchronous replication mode.</li><li><strong id="b79046221933"><a name="b79046221933"></a><a name="b79046221933"></a>semisync</strong> indicates the semi-synchronous replication mode.</li><li><strong id="b1790742210310"><a name="b1790742210310"></a><a name="b1790742210310"></a>sync</strong> indicates the synchronous replication mode.</li></ul>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  5**  datastore field data structure description

    <a name="table187591675262"></a>
    <table><thead align="left"><tr id="row131330815263"><th class="cellrowborder" valign="top" width="23.23%" id="mcps1.2.4.1.1"><p id="p613316812264"><a name="p613316812264"></a><a name="p613316812264"></a><strong id="b496687195"><a name="b496687195"></a><a name="b496687195"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.220000000000002%" id="mcps1.2.4.1.2"><p id="p3133188122610"><a name="p3133188122610"></a><a name="p3133188122610"></a><strong id="b552035273"><a name="b552035273"></a><a name="b552035273"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="54.55%" id="mcps1.2.4.1.3"><p id="p21331385269"><a name="p21331385269"></a><a name="p21331385269"></a><strong id="b1869307043"><a name="b1869307043"></a><a name="b1869307043"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row613358122613"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p12134178132620"><a name="p12134178132620"></a><a name="p12134178132620"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.2 "><p id="p1713415882612"><a name="p1713415882612"></a><a name="p1713415882612"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.55%" headers="mcps1.2.4.1.3 "><p id="p1713419813260"><a name="p1713419813260"></a><a name="p1713419813260"></a>Indicates the DB engine.</p>
    </td>
    </tr>
    <tr id="row16134281267"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p11134386261"><a name="p11134386261"></a><a name="p11134386261"></a>version</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.2 "><p id="p15134148102620"><a name="p15134148102620"></a><a name="p15134148102620"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.55%" headers="mcps1.2.4.1.3 "><p id="p181347842615"><a name="p181347842615"></a><a name="p181347842615"></a>Indicates the database version.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  6**  volume field data structure description

    <a name="table14771167122611"></a>
    <table><thead align="left"><tr id="row1713628182616"><th class="cellrowborder" valign="top" width="23.23%" id="mcps1.2.4.1.1"><p id="p913708102613"><a name="p913708102613"></a><a name="p913708102613"></a><strong id="b93749741"><a name="b93749741"></a><a name="b93749741"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.220000000000002%" id="mcps1.2.4.1.2"><p id="p1113768112615"><a name="p1113768112615"></a><a name="p1113768112615"></a><strong id="b1405944312"><a name="b1405944312"></a><a name="b1405944312"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="54.55%" id="mcps1.2.4.1.3"><p id="p71376812616"><a name="p71376812616"></a><a name="p71376812616"></a><strong id="b649116548"><a name="b649116548"></a><a name="b649116548"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row161373852620"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p13137148152619"><a name="p13137148152619"></a><a name="p13137148152619"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.2 "><p id="p41371185261"><a name="p41371185261"></a><a name="p41371185261"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.55%" headers="mcps1.2.4.1.3 "><p id="p4137389266"><a name="p4137389266"></a><a name="p4137389266"></a>Indicates the volume type.</p>
    </td>
    </tr>
    <tr id="row61371486268"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p013716812613"><a name="p013716812613"></a><a name="p013716812613"></a>size</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.2 "><p id="p5137108142610"><a name="p5137108142610"></a><a name="p5137108142610"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.55%" headers="mcps1.2.4.1.3 "><p id="p1813820832618"><a name="p1813820832618"></a><a name="p1813820832618"></a>Indicates the volume size.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  7**  backup\_strategy field data structure description

    <a name="table578797132615"></a>
    <table><thead align="left"><tr id="row171405802610"><th class="cellrowborder" valign="top" width="23.23%" id="mcps1.2.4.1.1"><p id="p61401783265"><a name="p61401783265"></a><a name="p61401783265"></a><strong id="b118179231"><a name="b118179231"></a><a name="b118179231"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.220000000000002%" id="mcps1.2.4.1.2"><p id="p4140287264"><a name="p4140287264"></a><a name="p4140287264"></a><strong id="b717084053"><a name="b717084053"></a><a name="b717084053"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="54.55%" id="mcps1.2.4.1.3"><p id="p101401384269"><a name="p101401384269"></a><a name="p101401384269"></a><strong id="b1919243190"><a name="b1919243190"></a><a name="b1919243190"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row111402862612"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p91403822614"><a name="p91403822614"></a><a name="p91403822614"></a>start_time</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.2 "><p id="p1414018813267"><a name="p1414018813267"></a><a name="p1414018813267"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.55%" headers="mcps1.2.4.1.3 "><p id="p161401381268"><a name="p161401381268"></a><a name="p161401381268"></a>Indicates the backup time window. Automated backups will be triggered during the backup time window.</p>
    <p id="p1914115872619"><a name="p1914115872619"></a><a name="p1914115872619"></a>The time is in the UTC format.</p>
    </td>
    </tr>
    <tr id="row91412081260"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p141411814267"><a name="p141411814267"></a><a name="p141411814267"></a>keep_days</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.2 "><p id="p14141188192618"><a name="p14141188192618"></a><a name="p14141188192618"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.55%" headers="mcps1.2.4.1.3 "><p id="p3141138182619"><a name="p3141138182619"></a><a name="p3141138182619"></a>Indicates the number of days to retain the generated backup files.</p>
    <p id="p1914188122614"><a name="p1914188122614"></a><a name="p1914188122614"></a>The value range is from 0 to 732. If the value is <strong id="b84235270611238"><a name="b84235270611238"></a><a name="b84235270611238"></a>0</strong>, the automated backup policy is not configured or has been disabled. To extend the retention period, contact customer service. Automated backups can be retained for up to 2562 days.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  8**  nodes field data structure description

    <a name="table1179987152611"></a>
    <table><thead align="left"><tr id="row1214388172616"><th class="cellrowborder" valign="top" width="23.23%" id="mcps1.2.4.1.1"><p id="p7143208102615"><a name="p7143208102615"></a><a name="p7143208102615"></a>Name</p>
    </th>
    <th class="cellrowborder" valign="top" width="22.220000000000002%" id="mcps1.2.4.1.2"><p id="p514314814266"><a name="p514314814266"></a><a name="p514314814266"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="54.55%" id="mcps1.2.4.1.3"><p id="p9143198142613"><a name="p9143198142613"></a><a name="p9143198142613"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row141432083267"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p1714313815266"><a name="p1714313815266"></a><a name="p1714313815266"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.2 "><p id="p10143185266"><a name="p10143185266"></a><a name="p10143185266"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.55%" headers="mcps1.2.4.1.3 "><p id="p914316812265"><a name="p914316812265"></a><a name="p914316812265"></a>Indicates the node ID.</p>
    </td>
    </tr>
    <tr id="row214388192612"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p10143198142611"><a name="p10143198142611"></a><a name="p10143198142611"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.2 "><p id="p1114338112612"><a name="p1114338112612"></a><a name="p1114338112612"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.55%" headers="mcps1.2.4.1.3 "><p id="p414313872615"><a name="p414313872615"></a><a name="p414313872615"></a>Indicates the node name.</p>
    </td>
    </tr>
    <tr id="row1314318819263"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p17143118122616"><a name="p17143118122616"></a><a name="p17143118122616"></a>role</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.2 "><p id="p18145138112614"><a name="p18145138112614"></a><a name="p18145138112614"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.55%" headers="mcps1.2.4.1.3 "><p id="p814516872618"><a name="p814516872618"></a><a name="p814516872618"></a>Indicates the node type. The value can be <strong id="b842352706113246"><a name="b842352706113246"></a><a name="b842352706113246"></a>master</strong>, <strong id="b842352706113249"><a name="b842352706113249"></a><a name="b842352706113249"></a>slave</strong>, or <strong id="b842352706113253"><a name="b842352706113253"></a><a name="b842352706113253"></a>readreplica</strong>, indicating the primary node, standby node, and read replica node, respectively.</p>
    </td>
    </tr>
    <tr id="row161456872616"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p214578162611"><a name="p214578162611"></a><a name="p214578162611"></a>status</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.2 "><p id="p51451283263"><a name="p51451283263"></a><a name="p51451283263"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.55%" headers="mcps1.2.4.1.3 "><p id="p114515814267"><a name="p114515814267"></a><a name="p114515814267"></a>Indicates the node status.</p>
    </td>
    </tr>
    <tr id="row9145168102610"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p171451087262"><a name="p171451087262"></a><a name="p171451087262"></a>availability_zone</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.2 "><p id="p714518818267"><a name="p714518818267"></a><a name="p714518818267"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.55%" headers="mcps1.2.4.1.3 "><p id="p131459819268"><a name="p131459819268"></a><a name="p131459819268"></a>Indicates the AZ.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  9**  related\_instance field data structure description

    <a name="table15816167142613"></a>
    <table><thead align="left"><tr id="row4147148102612"><th class="cellrowborder" valign="top" width="23.23%" id="mcps1.2.4.1.1"><p id="p514720872619"><a name="p514720872619"></a><a name="p514720872619"></a><strong id="b576045617"><a name="b576045617"></a><a name="b576045617"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="22.220000000000002%" id="mcps1.2.4.1.2"><p id="p51471382264"><a name="p51471382264"></a><a name="p51471382264"></a><strong id="b1665235674"><a name="b1665235674"></a><a name="b1665235674"></a>Type</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="54.55%" id="mcps1.2.4.1.3"><p id="p614718817265"><a name="p614718817265"></a><a name="p614718817265"></a><strong id="b1977839152"><a name="b1977839152"></a><a name="b1977839152"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row13147886260"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p81470811265"><a name="p81470811265"></a><a name="p81470811265"></a>id</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.2 "><p id="p1114718832613"><a name="p1114718832613"></a><a name="p1114718832613"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.55%" headers="mcps1.2.4.1.3 "><p id="p814816816263"><a name="p814816816263"></a><a name="p814816816263"></a>Indicates the associated DB instance ID.</p>
    </td>
    </tr>
    <tr id="row14148685268"><td class="cellrowborder" valign="top" width="23.23%" headers="mcps1.2.4.1.1 "><p id="p01483872612"><a name="p01483872612"></a><a name="p01483872612"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="22.220000000000002%" headers="mcps1.2.4.1.2 "><p id="p10148784263"><a name="p10148784263"></a><a name="p10148784263"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="54.55%" headers="mcps1.2.4.1.3 "><p id="p75017462385"><a name="p75017462385"></a><a name="p75017462385"></a>Indicates the associated DB instance type.</p>
    <a name="ul436512209393"></a><a name="ul436512209393"></a><ul id="ul436512209393"><li><strong id="b978194910446"><a name="b978194910446"></a><a name="b978194910446"></a>replica_of</strong>: indicates the primary DB instance.</li><li><strong id="b72493481257"><a name="b72493481257"></a><a name="b72493481257"></a>replica</strong>: indicates read replicas.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

-   Example normal response

    Query DB instances based on specified conditions.

    ```
    {
    	"instances": [{
    		"id": "ed7cc6166ec24360a5ed5c5c9c2ed726in01",
    		"status": "ACTIVE",
    		"name": "mysql-0820-022709-01",
    		"port": 3306,
    		"type": "Single",
    		"region": "eu-de",
    		"datastore": {
    			"type": "MySQL",
    			"version": "5.7"
    		},
    		"created": "2018-08-20T02:33:49+0800",
    		"updated": "2018-08-20T02:33:50+0800",
    		"volume": {
    			"type": "ULTRAHIGH",
    			"size": 100
    		},
    		"nodes": [{
    			"id": "06f1c2ad57604ae89e153e4d27f4e4b8no01",
    			"name": "mysql-0820-022709-01_node0",
    			"role": "master",
    			"status": "ACTIVE",
    			"availability_zone": "eu-de-01"
    		}],
    		"private_ips": ["192.168.0.142"],
    		"public_ips": ["10.154.219.187", "10.154.219.186"],
    		"db_user_name": "root",
    		"vpc_id": "b21630c1-e7d3-450d-907d-39ef5f445ae7",
    		"subnet_id": "45557a98-9e17-4600-8aec-999150bc4eef",
    		"security_group_id": "38815c5c-482b-450a-80b6-0a301f2afd97",
    		"flavor_ref": "rds.mysql.s1.large",
    		"switch_strategy": "",
    		"backup_strategy": {
    			"start_time": "19:00-20:00",
    			"keep_days": 7
    		},
    		"maintenance_window": "02:00-06:00",
    		"related_instance": [],
    		"disk_encryption_id": "",
    		"time_zone": ""
    	}],
    	"total_count": 1
    }
    ```

    ```
    {
    	"instances": [{
    	"id": "ed7cc6166ec24360a5ed5c5c9c2ed726in01",
    	"status": "ACTIVE",
    	"name": "mysql-0820-022709-01",
    	"port": 3306,
    	"type": "Single",
    	"region": "aaa",
    	"datastore": {
    		"type": "MySQL",
    		"version": "5.7"
    	},
    	"created": "2018-08-20T02:33:49+0800",
    	"updated": "2018-08-20T02:33:50+0800",
    	"volume": {
    		"type": "ULTRAHIGH",
    		"size": 100
    	},
    	"nodes": [{
    		"id": "06f1c2ad57604ae89e153e4d27f4e4b8no01",
    		"name": "mysql-0820-022709-01_node0",
    		"role": "master",
    		"status": "ACTIVE",
    		"availability_zone": "bbb"
    	}],
    	"private_ips": ["192.168.0.142"],
    	"public_ips": ["10.154.219.187", "10.154.219.186"],
    	"db_user_name": "root",
    	"vpc_id": "b21630c1-e7d3-450d-907d-39ef5f445ae7",
    	"subnet_id": "45557a98-9e17-4600-8aec-999150bc4eef",
    	"security_group_id": "38815c5c-482b-450a-80b6-0a301f2afd97",
    	"flavor_ref": "rds.mysql.s1.large",
    	"switch_strategy": "",
    	"backup_strategy": {
    		"start_time": "19:00-20:00",
    		"keep_days": 7
    	},
    	"maintenance_window": "02:00-06:00",
    	"related_instance": [],
    	"time_zone": ""
            
               
                  
                    
                
                
                    
                    
               
             
    }], "total_count": 1
    }
    ```


-   Query all DB instances.

    ```
    {
    	"instances": [{
    		"id": "ed7cc6166ec24360a5ed5c5c9c2ed726in01",
    		"status": "ACTIVE",
    		"name": "mysql-0820-022709-01",
    		"port": 3306,
    		"type": "Single",
    		"region": "eu-de",
    		"datastore": {
    			"type": "MySQL",
    			"version": "5.7"
    		},
    		"created": "2018-08-20T02:33:49+0800",
    		"updated": "2018-08-20T02:33:50+0800",
    		"volume": {
    			"type": "ULTRAHIGH",
    			"size": 100
    		},
    		"nodes": [{
    			"id": "06f1c2ad57604ae89e153e4d27f4e4b8no01",
    			"name": "mysql-0820-022709-01_node0",
    			"role": "master",
    			"status": "ACTIVE",
    			"availability_zone": "eu-de-01"
    		}],
    		"private_ips": ["192.168.0.142"],
    		"public_ips": ["10.154.219.187", "10.154.219.186"],
    		"db_user_name": "root",
    		"vpc_id": "b21630c1-e7d3-450d-907d-39ef5f445ae7",
    		"subnet_id": "45557a98-9e17-4600-8aec-999150bc4eef",
    		"security_group_id": "38815c5c-482b-450a-80b6-0a301f2afd97",
    		"flavor_ref": "rds.mysql.s1.large",
    		"switch_strategy": "",
    		"backup_strategy": {
    			"start_time": "19:00-20:00",
    			"keep_days": 7
    		},
    		"maintenance_window": "02:00-06:00",
    		"related_instance": [],
    		"disk_encryption_id": "",
    		"time_zone": ""
                    
                       
                           
                            
                        
                        
                            
                            
                        
                    
    	}, {
    		"id": "ed7cc6166ec24360a5ed5c5c9c2ed726in02",
    		"status": "ACTIVE",
    		"name": "mysql-0820-022709-02",
    		"port": 3306,
    		"type": "Single",
    		"region": "eu-de",
    		"datastore": {
    			"type": "MySQL",
    			"version": "5.6"
    		},
    		"created": "2019-08-20T02:33:49+0800",
    		"updated": "2019-08-20T02:33:50+0800",
    		"volume": {
    			"type": "ULTRAHIGH",
    			"size": 100
    		},
    		"nodes": [{
    			"id": "06f1c2ad57604ae89e153e4d27f4e4b8no01",
    			"name": "mysql-0820-022709-01_node0",
    			"role": "master",
    			"status": "ACTIVE",
    			"availability_zone": "eu-de-01"
    		}],
    		"private_ips": ["192.168.0.142"],
    		"public_ips": ["10.154.219.187", "10.154.219.186"],
    		"db_user_name": "root",
    		"vpc_id": "b21630c1-e7d3-450d-907d-39ef5f445ae7",
    		"subnet_id": "45557a98-9e17-4600-8aec-999150bc4eef",
    		"security_group_id": "38815c5c-482b-450a-80b6-0a301f2afd97",
    		"flavor_ref": "rds.mysql.s1.large",
    		"switch_strategy": "",
    		"backup_strategy": {
    			"start_time": "19:00-20:00",
    			"keep_days": 7
    		},
    		"maintenance_window": "02:00-06:00",
    		"related_instance": [],
    		"disk_encryption_id": "",
    		"time_zone": ""
                   
                       
                            
                           
                       
                        
                            
                            
                       
                   
    	}],
    	"total_count": 2
    }
    ```

-   Abnormal Response

    For details, see  [Abnormal Request Results](abnormal-request-results.md).


## Status Code<a name="section4778540915440"></a>

For details, see  [Status Codes](status-codes.md).

## Error Code<a name="section946032144017"></a>

For details, see  [Error Codes](error-codes.md).

